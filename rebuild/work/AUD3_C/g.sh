#!/bin/bash
# grep a term across all reader category files, report files and counts
cd /home/user/Possession-Taxonomy/rebuild/reader
for t in "$@"; do echo "== $t: $(grep -oi "$t" [A-J]*.json | cut -d: -f1 | sort | uniq -c | tr '\n' ' ')"; done
