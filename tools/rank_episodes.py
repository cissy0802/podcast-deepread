#!/usr/bin/env python3
"""Rank one podcast channel's full episodes by YouTube view count.

Usage:
    python3 tools/rank_episodes.py @hubermanlab --min-minutes 25 --top 40 -o huberman.json

TOPICS.md is built per-podcast quota, ranked by plays INSIDE each podcast —
raw view counts are not comparable across channels, where a 5-10x gap tracks
subscriber base rather than episode quality.

Two passes, because yt-dlp's flat listing returns duration but not view count,
and full extraction costs ~1.5s per video. Pass 1 enumerates the whole channel
flat (seconds) and drops anything too short to be a full episode — on these
channels most uploads are clips. Pass 2 fully extracts only the survivors.

Note: YouTube's own "sort by popular" channel URL (?view=0&sort=p) is ignored
by yt-dlp, which silently returns date order. Ranking has to happen here.
"""
import argparse
import json
import re
import subprocess
import sys


# Errors meaning "nobody here can get this episode", as opposed to "the request
# failed". Subscription-funded shows gate much of their back catalogue this way
# — Making Sense keeps 187 of 443 uploads behind its All Access tier — and those
# episodes are out of scope for this site anyway, since an episode that cannot
# be transcribed cannot be read closely.
# Uploads that rank well but cannot carry an issue of this site. This is a
# narrow list on purpose: it covers formats with no single argument to follow —
# listener questions answered one after another, housekeeping, promos.
#
# Solo lectures are deliberately NOT here. A one-person talk built around one
# idea (Carroll's "Biggest Ideas in the Universe", his Solo episodes, Sarah
# Paine's history lectures) is the easiest thing on these feeds to read closely:
# one continuous argument rather than a conversation that wanders.
NOISE_PATTERNS = (
    r"Ask Me Anything", r"\bAMA\b", r"\bQ&A\b",
    r"Holiday Message", r"Year in Review", r"Retrospective", r"Best of \d{4}",
    r"Live Show", r"Livestream", r"Trailer", r"Announcement", r"Coming Soon",
)

# Cap on episodes sharing one recurring name, so a single voice cannot take a
# channel's whole quota — Dwarkesh's top five is four Sarah Paine lectures, all
# excellent, but as four issues they would read as one issue told four times.
# This is a variety limit, not a quality judgement.
MAX_PER_GUEST = 3

GATED_PATTERNS = (
    "members-only",
    "available to this channel's members",   # 2026 wording; A Life Engineered gates its "Principal" tier this way
    "All Access",
    "Join this channel",
    "Private video",
    "video is unavailable",
    "Video unavailable",
    "age-restricted",
    "Sign in to confirm your age",
)


def flat_list(channel):
    """(id, duration_s, title) for every video on the channel — fast, no view counts."""
    url = f"https://www.youtube.com/{channel}/videos" if channel.startswith("@") else channel
    p = subprocess.run(
        ["yt-dlp", "--no-update", "--flat-playlist", "--print", "%(id)s\t%(duration)s\t%(title)s", url],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        sys.exit(f"ERROR: could not list {url}\n{p.stderr.strip()[:500]}")
    rows = []
    for line in p.stdout.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        vid, dur, title = parts
        try:
            rows.append((vid, float(dur), title))
        except ValueError:
            continue  # live/upcoming entries have no duration
    return rows


def hydrate(vids, max_fail_ratio=0.05):
    """Full extraction for view counts.

    Individual videos can legitimately fail (deleted, members-only), so one
    failure is not fatal. But a run of failures means YouTube started throttling
    mid-harvest, and a ranking built from whatever survived is not a ranking by
    views — it silently becomes "ranked among the episodes that happened to
    answer". That must fail loudly, not degrade into a plausible-looking list.
    """
    out, failures, gated = [], [], []
    for i, vid in enumerate(vids, 1):
        p = subprocess.run(
            ["yt-dlp", "--no-update", "--skip-download", "--dump-json",
             f"https://www.youtube.com/watch?v={vid}"],
            capture_output=True, text=True,
        )
        if p.returncode != 0:
            why = (p.stderr.strip().splitlines() or ["unknown"])[-1][:100]
            if any(pat in why for pat in GATED_PATTERNS):
                # Paywalled or withdrawn. Not a harvest failure: the episode is
                # simply not available to anyone here, so it could never be read
                # and deepread either. Excluding it is the correct outcome, and
                # ranking the rest stays honest — "top viewed among the episodes
                # that can actually be obtained".
                gated.append((vid, why))
            else:
                failures.append((vid, why))
                print(f"  skip {vid}: {why}", file=sys.stderr)
            continue
        d = json.loads(p.stdout)
        out.append({
            "id": d["id"],
            "title": d.get("title", ""),
            "views": d.get("view_count") or 0,
            "duration_s": d.get("duration") or 0,
            "upload_date": d.get("upload_date", ""),
            "url": f"https://www.youtube.com/watch?v={d['id']}",
        })
        if i % 25 == 0:
            print(f"  ...{i}/{len(vids)}  ({len(failures)} failed, {len(gated)} paywalled)",
                  file=sys.stderr)

    # The ratio is taken over reachable episodes only. Counting paywalled ones as
    # failures would trip the gate on any subscription-funded show, where the
    # right answer is to rank what is left, not to abort.
    reachable = len(vids) - len(gated)
    if reachable and len(failures) / reachable > max_fail_ratio:
        print(f"\nERROR: {len(failures)}/{reachable} reachable lookups failed "
              f"(> {max_fail_ratio:.0%}). These are not paywall errors, so this is "
              f"almost certainly throttling, and a ranking from the survivors would "
              f"not be a ranking by views. Wait and re-run rather than trusting a "
              f"partial list.", file=sys.stderr)
        for vid, why in failures[:5]:
            print(f"  {vid}: {why}", file=sys.stderr)
        sys.exit(3)
    if gated:
        print(f"  {len(gated)}/{len(vids)} are paywalled or withdrawn — excluded, "
              f"ranking covers the {reachable} obtainable episodes", file=sys.stderr)
    if failures:
        print(f"  {len(failures)}/{reachable} lookups failed (within tolerance)", file=sys.stderr)
    return out


ROLE_WORDS = re.compile(
    r"\b(award|winner|creator|co-creator|professor|vp|engineer|eng|director|cto|manager|head|founder|lead|chief)\b", re.I)


def guest_key(title):
    """A rough identity for the guest or series a title belongs to.

    Only needs to be good enough to catch a recurring name dominating a ranking;
    a miss costs one near-duplicate issue, not a wrong ranking. Titles here look
    like "Sarah Paine — The war for India", "Episode 28: Roger Penrose on ...",
    "Porsche (with Doug DeMuro)" or "Dr. Andy Galpin: How to Build Strength".
    """
    # A numbered lecture series keys on the series, not a person: its titles
    # carry no name, so without this every instalment looks unrelated and the
    # cap never fires — "Biggest Ideas in the Universe" took 7 of Mindscape's 10.
    m = re.match(r"\s*(?:The\s+)?(.+?)\s*\|\s*\d+\.\s", title)
    if m:
        return "series:" + m.group(1).strip().lower()

    t = re.sub(r"^(Mindscape|Episode|Ep\.?)\s*#?\d*\s*[|:]?\s*", "", title, flags=re.I)
    t = re.sub(r"\s*\|.*$", "", t)                      # trailing " | Lex Fridman Podcast #310"
    name = None
    m = re.search(r"\(with ([^)]+)\)", t, re.I)         # "Porsche (with Doug DeMuro)"
    if m:
        name = m.group(1)
    if name is None:                                     # "Sarah Paine — ...", "Dr. Andy Galpin: ..."
        m = re.match(r"\s*((?:Dr\.|Prof\.)?\s*[A-Z][\w.'-]+(?:\s+[A-Z][\w.'-]+){0,3})\s*[—–:-]\s", t)
        name = m.group(1) if m else None
    if name is None:                                     # "Roger Penrose on Spacetime..."
        m = re.match(r"\s*([A-Z][\w.'-]+(?:\s+[A-Z][\w.'-]+){0,3})\s+on\s+", t)
        name = m.group(1) if m else None
    # A role or title is not a person. Peterman Pod opens titles with the guest's
    # credential and puts the name after the pipe — "Turing Award Winner: ... |
    # Leslie Lamport" — so the name-first patterns above read the credential as
    # the guest, and every Turing laureate shared one cap of 3 (Pearl, Patterson,
    # Hellman and Wigderson were silently dropped). Fall back to the pipe name.
    if name and ROLE_WORDS.search(name):
        m = re.search(r"\|\s*([A-Z][\w.'-]+(?:\s+[A-Z][\w.'-]+){0,3})\s*$", title)
        name = m.group(1) if m else None
    if name is None:
        return None

    # Normalise to first + last, dropping honorifics and middle initials, so
    # "Sarah Paine" and "Sarah C. M. Paine" are one person and share one cap.
    parts = [p for p in name.strip().lower().split()
             if p not in ("dr.", "dr", "prof.", "prof") and not re.fullmatch(r"[a-z]\.?", p)]
    if not parts:
        return None
    return " ".join(parts[:1] + parts[-1:]) if len(parts) > 1 else parts[0]


def select(eps, top, max_per_guest=MAX_PER_GUEST):
    """Drop noise, cap per guest, keep view order. Returns (selected, dropped)."""
    noise = re.compile("|".join(NOISE_PATTERNS), re.I)
    chosen, dropped, seen = [], [], {}
    for e in eps:
        if noise.search(e["title"]):
            dropped.append((e, "noise"))
            continue
        k = guest_key(e["title"])
        if k:
            seen[k] = seen.get(k, 0) + 1
            if seen[k] > max_per_guest:
                dropped.append((e, f"guest cap: {k}"))
                continue
        chosen.append(e)
        if len(chosen) >= top:
            break
    return chosen, dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", help="@handle or channel/playlist URL")
    ap.add_argument("--min-minutes", type=float, default=25,
                    help="drop anything shorter — clips, trailers, Shorts (default 25)")
    ap.add_argument("--max-minutes", type=float, default=300)
    ap.add_argument("--top", type=int, default=40, help="how many to keep after ranking")
    ap.add_argument("--limit-hydrate", type=int, default=250,
                    help="cap on pass-2 extractions; newest survivors are kept")
    ap.add_argument("-o", "--out", help="write JSON here instead of stdout")
    args = ap.parse_args()

    rows = flat_list(args.channel)
    print(f"{args.channel}: {len(rows)} uploads listed", file=sys.stderr)

    lo, hi = args.min_minutes * 60, args.max_minutes * 60
    keep = [(v, d, t) for v, d, t in rows if lo <= d <= hi]
    print(f"  {len(keep)} look like full episodes ({args.min_minutes:g}-{args.max_minutes:g} min)",
          file=sys.stderr)

    if len(keep) > args.limit_hydrate:
        print(f"  capping view-count lookup at the {args.limit_hydrate} newest", file=sys.stderr)
        keep = keep[:args.limit_hydrate]

    eps = hydrate([v for v, _, _ in keep])
    eps.sort(key=lambda e: e["views"], reverse=True)

    # Cache every hydrated episode, not just the slice that survives the current
    # filters. The view-count lookup is the whole cost of this script (~1s each,
    # hours across the roster); filters and quotas get revised far more often
    # than the numbers change, and re-selecting from this file is instant.
    if args.out:
        raw = args.out[:-5] + ".raw.json" if args.out.endswith(".json") else args.out + ".raw"
        with open(raw, "w", encoding="utf-8") as f:
            json.dump({"channel": args.channel, "episodes": eps}, f, ensure_ascii=False, indent=2)
        print(f"  cached {len(eps)} hydrated episodes -> {raw}", file=sys.stderr)

    chosen, dropped = select(eps, args.top)

    payload = {"channel": args.channel, "episodes": chosen}
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        short = "" if len(chosen) >= args.top else f"  (SHORT of {args.top})"
        print(f"\n{args.out}: {len(chosen)} selected, {len(dropped)} filtered out{short}",
              file=sys.stderr)
        for e in chosen[:10]:
            print(f"  {e['views']:>10,}  {e['duration_s']//60:>4}m  {e['title'][:62]}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
