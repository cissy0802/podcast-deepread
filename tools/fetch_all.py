#!/usr/bin/env python3
"""Fetch every transcript TOPICS.md calls for, into the private transcripts repo.

Usage:
    python3 tools/fetch_all.py [--topics TOPICS.md] [--dest ../podcast-transcripts]

Run on a laptop, never in the cloud: YouTube refuses caption requests from
datacenter IPs, which is the whole reason transcripts are pre-fetched and parked
in a private repo for the engine to clone.

Already-present transcripts are skipped, so this is safe to re-run after adding
episodes to TOPICS.md or after a partial run.

Failures are listed at the end and the exit code is non-zero. An episode with no
transcript is not a small gap: the engine refuses to write that issue at all, so
a silent shortfall here becomes a run that stops later for reasons nobody traced
back to this script.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

TOOL = Path(__file__).parent / "fetch_transcript.py"


def parse_topics(path):
    """[(slug, url)] in list order, from the TOPICS.md entry shape."""
    text = Path(path).read_text(encoding="utf-8")
    entries, url = [], None
    for line in text.splitlines():
        m = re.match(r"\s*-\s*source:\s*<([^>]+)>", line)
        if m:
            url = m.group(1)
            continue
        m = re.match(r"\s*-\s*slug:\s*`([^`]+)`", line)
        if m and url:
            entries.append((m.group(1), url))
            url = None
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topics", default="TOPICS.md")
    ap.add_argument("--dest", default="../podcast-transcripts")
    ap.add_argument("--limit", type=int, help="stop after this many new fetches")
    args = ap.parse_args()

    out_dir = Path(args.dest) / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)

    entries = parse_topics(args.topics)
    if not entries:
        sys.exit(f"ERROR: no entries parsed from {args.topics}")
    print(f"{len(entries)} episodes in {args.topics}, writing to {out_dir}\n")

    done, skipped, failed = [], [], []
    for i, (slug, url) in enumerate(entries, 1):
        target = out_dir / f"{slug}.txt"
        if target.exists() and target.stat().st_size > 2000:
            skipped.append(slug)
            continue
        if args.limit and len(done) >= args.limit:
            break
        print(f"[{i}/{len(entries)}] {slug}", flush=True)
        p = subprocess.run(
            [sys.executable, str(TOOL), url, "-o", str(target)],
            capture_output=True, text=True,
        )
        if p.returncode != 0 or not target.exists():
            why = (p.stderr.strip().splitlines() or ["unknown"])[-1][:140]
            print(f"    FAILED: {why}", flush=True)
            failed.append((slug, url, why))
            target.unlink(missing_ok=True)
            continue
        print(f"    {p.stdout.strip()}", flush=True)
        done.append(slug)

    print(f"\n{'=' * 60}")
    print(f"fetched {len(done)}  ·  already present {len(skipped)}  ·  failed {len(failed)}")
    if failed:
        print("\nFAILED — these episodes have no transcript, so the engine cannot")
        print("write them. Re-run to retry, or drop them from TOPICS.md:")
        for slug, url, why in failed:
            print(f"  {slug}\n    {url}\n    {why}")
        sys.exit(1)


if __name__ == "__main__":
    main()
