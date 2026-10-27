#!/bin/bash
# map recent pdfs (timestamp >= $1) by name guessed from the "Name:" /title; usage hom2.sh MINTS name1 name2...
D=/root/.claude/projects/-home-user-Possession-Taxonomy/991a120d-58ce-5be7-b478-357308cba37c/tool-results
min=$1; shift
for f in $(ls $D/webfetch-*.pdf); do ts=$(basename $f | sed 's/webfetch-\([0-9]*\)-.*/\1/'); [ $ts -ge $min ] || continue
 t=$(pdftotext -layout $f - 2>/dev/null | grep -v '^\s*$' | head -3 | tr '\n' ' ' | tr 'A-Z' 'a-z')
 for n in "$@"; do case "$t" in *"$n"*) pdftotext -layout $f /home/user/Possession-Taxonomy/rebuild/work/F6/agent/hom/$n.txt 2>/dev/null; echo "$n <- $ts";; esac; done
done
