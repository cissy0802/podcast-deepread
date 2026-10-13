#!/usr/bin/env bash
# podcast-deepread — preflight.
#
# The engine runs this itself at the start of every run (CLAUDE.md §0) rather
# than trusting a .preflight left by the environment's own setup script: this
# routine may share an environment with the other deepread sites, whose probes
# test their sources, not these.
#
# Two things must hold before a run may write anything:
#
#   1. The private transcripts repo can be cloned. Unlike the sibling sites,
#      this one cannot read its source at runtime — YouTube refuses caption
#      requests from datacenter IPs, and these shows' own transcripts are
#      paywalled. Transcripts are pulled on a laptop and parked in
#      cissy0802/podcast-transcripts, so no clone means no episode text, and
#      no episode text means no issue. Whether the cloud harness's GitHub
#      credential reaches a second, private repo is UNVERIFIED as of the first
#      run — that is exactly what this probe settles, loudly.
#
#   2. General egress works, for the research the second half of each page
#      rests on (papers, critiques, follow-ups).
#
# Probes are hosts this repo actually reads from, never neutral hosts like
# example.com: under Custom network access those are blocked by design, and
# using one as a control turns a correctly configured environment into a false
# BLOCKED. Three research hosts, so one site down for maintenance can't abort
# a run.
#
# Never exits non-zero — a failed preflight is a fact for the engine to act on.

set -u

PREFLIGHT=".preflight"
TRANSCRIPT_REPO="https://github.com/cissy0802/podcast-transcripts.git"
TRANSCRIPT_DIR="${TRANSCRIPT_DIR:-../podcast-transcripts}"

probe() {
  curl -sS -o /dev/null --max-time 8 \
    -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36' \
    -w '%{http_code}' "$1" 2>/dev/null
}

# ---------- 1. transcripts ----------
TRANSCRIPTS=0
TRANSCRIPT_NOTE=""
COUNT=0
if [ -d "$TRANSCRIPT_DIR/.git" ]; then
  if git -C "$TRANSCRIPT_DIR" pull -q --ff-only 2>/dev/null; then
    TRANSCRIPTS=1; TRANSCRIPT_NOTE="already cloned, updated"
  else
    TRANSCRIPTS=1; TRANSCRIPT_NOTE="already cloned, pull failed (using existing copy)"
  fi
else
  CLONE_ERR=$(git clone -q --depth 1 "$TRANSCRIPT_REPO" "$TRANSCRIPT_DIR" 2>&1)
  if [ -d "$TRANSCRIPT_DIR/.git" ]; then
    TRANSCRIPTS=1; TRANSCRIPT_NOTE="cloned"
  else
    TRANSCRIPT_NOTE="clone failed: $(printf '%s' "$CLONE_ERR" | tr '\n' ' ' | cut -c1-200)"
  fi
fi
[ "$TRANSCRIPTS" = "1" ] && COUNT=$(ls "$TRANSCRIPT_DIR"/transcripts/*.txt 2>/dev/null | wc -l | tr -d ' ')

# ---------- 2. egress ----------
OK=0
RESULTS=""
for u in https://pubmed.ncbi.nlm.nih.gov/ https://www.nature.com/ https://arxiv.org/; do
  code=$(probe "$u")
  [ -z "$code" ] && code="000"
  RESULTS="${RESULTS}  ${u} -> ${code}"$'\n'
  case "$code" in 2*|3*) OK=1 ;; esac
done

{
  echo "# preflight — written by setup.sh"
  echo "checked_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo ""
  if [ "$TRANSCRIPTS" = "1" ]; then
    echo "transcripts: OK ($TRANSCRIPT_NOTE; $COUNT files in $TRANSCRIPT_DIR/transcripts/)"
  else
    echo "transcripts: BLOCKED ($TRANSCRIPT_NOTE)"
    echo ""
    echo "  The private transcripts repo could not be cloned, so no episode text is"
    echo "  available. There is no fallback: YouTube will not serve captions to this"
    echo "  IP, and these shows' own transcripts are paywalled. Do NOT write from"
    echo "  memory or from second-hand summaries of the episode."
    echo ""
    echo "  Publish nothing, touch no files, send one PushNotification saying the"
    echo "  cloud harness's GitHub credential does not reach"
    echo "  cissy0802/podcast-transcripts, and end the run. The fallback BigCat"
    echo "  chose is to serve the transcripts from R2 over public HTTPS instead."
  fi
  echo ""
  if [ "$OK" = "1" ]; then
    echo "egress: OK"
  else
    echo "egress: BLOCKED"
    echo ""
    echo "  All three research probes failed. They are three different hosts this"
    echo "  repo reads from, so this is the environment's network policy, not one"
    echo "  site blocking bots. Do not test user agents or alternate hosts, and do"
    echo "  not fall back to writing the research sections from memory. Publish"
    echo "  nothing, send one PushNotification saying the environment's Network"
    echo "  access needs checking (Trusted covers package registries and GitHub"
    echo "  only; under Custom the research domains must be in Allowed domains),"
    echo "  then end the run."
  fi
  echo ""
  echo "probes:"
  printf '%s' "$RESULTS"
} > "$PREFLIGHT"

cat "$PREFLIGHT"
exit 0
