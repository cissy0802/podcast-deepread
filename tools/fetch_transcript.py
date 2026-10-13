#!/usr/bin/env python3
"""Fetch a podcast episode transcript from YouTube auto-captions.

Usage:
    python3 tools/fetch_transcript.py <youtube url or video id> [-o out.txt]

Why this exists instead of fetching a transcript page at runtime: the
publisher-side transcripts for most of these shows are paywalled (Huberman Lab
gates them behind Supercast), and YouTube refuses caption requests coming from
datacenter IPs ("Sign in to confirm you're not a bot"). So transcripts are
pulled HERE, on a residential connection, and parked in R2 — the cloud routine
only ever reads them back. Exit code 2 means "no transcript", which is a hard
stop for the caller, never permission to write from memory.

Output is plain UTF-8 text: a metadata header, then paragraphs prefixed with
[hh:mm:ss] so a reader can cite a moment in the episode.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Preference order. en-orig is the ASR track in the speaker's own language,
# which for these shows is English; plain "en" on the same video is often a
# machine TRANSLATION of that track back into English, which round-trips the
# wording and quietly corrupts quotes. Always prefer en-orig.
SUB_LANGS = ["en-orig", "en"]

# Start a new paragraph when the gap between caption cues exceeds this. ASR
# has no paragraph marks; a real pause in speech is the best proxy available.
PARA_GAP_MS = 2000
# ...and force a break in a long unbroken stretch so paragraphs stay readable.
PARA_MAX_CHARS = 700
# ...and when the track has no punctuation at all (some shows' ASR comes back
# as one unpunctuated stream with overlapping cue times, so neither the gap nor
# the sentence test ever fires), break anyway past this length. Without it a
# 2-hour episode came out as one 20k-word paragraph under a single timestamp —
# 39 of 133 transcripts on 2026-10-12 — and nothing in it could be cited by time.
PARA_HARD_MAX_CHARS = 1500


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def video_id(arg):
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([\w-]{11})", arg)
    if m:
        return m.group(1)
    if re.fullmatch(r"[\w-]{11}", arg):
        return arg
    return None


def fetch(url, workdir):
    """Download metadata + the best available caption track. Returns (info, json3_path)."""
    info_p = run(["yt-dlp", "--no-update", "--skip-download", "--dump-json", url])
    if info_p.returncode != 0:
        sys.exit(f"ERROR: could not read video metadata\n{info_p.stderr.strip()[:500]}")
    info = json.loads(info_p.stdout)

    available = set(info.get("automatic_captions") or {}) | set(info.get("subtitles") or {})
    lang = next((l for l in SUB_LANGS if l in available), None)
    if lang is None:
        print(f"ERROR: no English caption track on {url}", file=sys.stderr)
        print(f"       tracks offered: {sorted(available)[:20]}", file=sys.stderr)
        sys.exit(2)

    out = Path(workdir) / "sub"
    dl = run([
        "yt-dlp", "--no-update", "--skip-download",
        "--write-auto-subs", "--write-subs",
        "--sub-langs", lang, "--sub-format", "json3",
        "-o", str(out) + ".%(ext)s", url,
    ])
    files = sorted(Path(workdir).glob("sub*.json3"))
    if not files:
        print(f"ERROR: caption track '{lang}' was offered but did not download", file=sys.stderr)
        print(dl.stderr.strip()[:500], file=sys.stderr)
        sys.exit(2)
    return info, files[0], lang


def parse_json3(path):
    """json3 -> [(start_ms, end_ms, text)] cues, whitespace normalised, empties dropped."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    cues = []
    for ev in data.get("events", []):
        segs = ev.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            start = ev.get("tStartMs", 0)
            cues.append((start, start + (ev.get("dDurationMs") or 0), text))
    return cues


def paragraphs(cues):
    """Group cues into paragraphs, breaking on real silence or at sentence ends.

    A break needs a gap measured from the previous cue's END (a gap from its
    start is just how long that cue lasted, which is every cue). ASR emits no
    paragraph marks, so silence is the only structural signal available; the
    length cap keeps a monologue stretch from becoming one wall of text, and
    only breaks after a finished sentence so quotes stay intact.
    """
    out, buf, start, prev_end = [], [], None, None

    def flush(next_t):
        nonlocal buf, start
        if buf:
            out.append((start, " ".join(buf)))
        buf, start = [], next_t

    for t, end, text in cues:
        if start is None:
            start = t
        # A turn marker can appear mid-cue, so split the cue around it rather
        # than only breaking between cues.
        pieces = [p.strip() for p in re.split(r"\s*>>\s*", text)]
        for i, piece in enumerate(pieces):
            if i > 0:                       # every piece after the first opens a new turn
                flush(t)
            elif buf:
                gap_break = prev_end is not None and t - prev_end > PARA_GAP_MS
                sentence_end = buf[-1].rstrip().endswith((".", "?", "!"))
                buf_len = sum(len(b) + 1 for b in buf)
                len_break = (sentence_end and buf_len > PARA_MAX_CHARS) or buf_len > PARA_HARD_MAX_CHARS
                if gap_break or len_break:
                    flush(t)
            if piece:
                buf.append(piece)
        prev_end = max(end, t)
    flush(None)
    return out


def hms(ms):
    s = int(ms // 1000)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    args = ap.parse_args()

    vid = video_id(args.url)
    url = f"https://www.youtube.com/watch?v={vid}" if vid else args.url

    with tempfile.TemporaryDirectory() as wd:
        info, sub, lang = fetch(url, wd)
        cues = parse_json3(sub)

    if not cues:
        print(f"ERROR: caption file for {url} parsed to zero cues", file=sys.stderr)
        sys.exit(2)

    paras = paragraphs(cues)
    body = "\n\n".join(f"[{hms(t)}] {p}" for t, p in paras)
    words = len(body.split())

    # A 2-hour episode is ~20k words. Anything tiny means the track was a
    # trailer, a Short, or a broken fetch — say so rather than hand back a stub.
    if words < 1500:
        print(f"WARNING: only {words} words — check this is the full episode", file=sys.stderr)

    header = "\n".join([
        f"title: {info.get('title', '')}",
        f"channel: {info.get('uploader', '')}",
        f"video_id: {info.get('id', '')}",
        f"url: {url}",
        f"upload_date: {info.get('upload_date', '')}",
        f"duration_s: {info.get('duration', '')}",
        f"view_count: {info.get('view_count', '')}",
        f"caption_track: {lang} (YouTube ASR — machine transcript, not publisher-authored)",
        f"words: {words}",
        f"turns: {len(paras)}",
        "",
        "# Each paragraph below is one speaker turn (YouTube ASR marks turn changes,",
        "# so turns are reliable) OR a pause/length break inside a long turn. Turns are",
        "# NOT NAMED: in a two-person interview the host opens and speakers alternate,",
        "# but ASR does drop turns, so attribute a quote to a named person only when the",
        "# surrounding context settles it. This is a machine transcript, not a",
        "# publisher-authored one: verify any wording that carries weight against the",
        "# audio at the timestamp before quoting it.",
        "",
        "-" * 60,
        "",
    ])

    text = header + body + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"{args.out}  ·  {words} words  ·  {len(paras)} paragraphs  ·  {lang}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
