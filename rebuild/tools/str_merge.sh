#!/bin/bash
# Merge finished STR categories, validate v3, commit and push. Usage: tools/str_merge.sh A4 [B1 ...]
cd "$(dirname "$0")/.." || exit 1
for c in "$@"; do
  python3 merge.py "$c" 2>&1 | grep -v '^done' | tail -4
  python3 validate.py --v3 "reader/$c.json" || exit 1
done
cd .. && git add -A && git commit -qm "Structure pass merged: $*

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01E7ZePoyt9poV565DQZwoZn" && git push -q origin main && echo pushed
