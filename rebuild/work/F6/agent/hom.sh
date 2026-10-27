#!/bin/bash
# usage: hom.sh name1 name2 ... ; maps the N newest webfetch pdfs (by name order) to names
D=/root/.claude/projects/-home-user-Possession-Taxonomy/991a120d-58ce-5be7-b478-357308cba37c/tool-results
N=$#
files=$(ls $D/webfetch-*.pdf | sort -t- -k2 -n | tail -n $N)
i=0; for n in "$@"; do i=$((i+1)); f=$(echo "$files" | sed -n "${i}p"); pdftotext -layout $f /home/user/Possession-Taxonomy/rebuild/work/F6/agent/hom/$n.txt 2>/dev/null; echo $n $(wc -c < /home/user/Possession-Taxonomy/rebuild/work/F6/agent/hom/$n.txt) $(grep -c -i $n /home/user/Possession-Taxonomy/rebuild/work/F6/agent/hom/$n.txt); done
