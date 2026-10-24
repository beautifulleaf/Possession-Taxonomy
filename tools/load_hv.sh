#!/bin/bash
# usage: ld.sh BATCH...  (fix header, drop stored makers and stored lines, load)
cd /home/user/Possession-Taxonomy
for b in "$@"; do python3 tools/fix_fetch_log_header.py $b; python3 tools/drop_stored_makers.py $b
python3 - $b <<'PY'
import sys, os; sys.path.insert(0,'tools')
from common import read_tsv, write_tsv
b=sys.argv[1]; p=f'verify/out/{b}_lines.tsv'
if os.path.exists(p):
    st={r['line_id'] for r in read_tsv('data/lines.tsv')}; rows=read_tsv(p)
    if rows:
        keep=[r for r in rows if r['line_id'] not in st]
        if len(keep)!=len(rows): print(b,'stored lines kept:',[r['line_id'] for r in rows if r['line_id'] in st]); write_tsv(p,keep,list(rows[0].keys()))
PY
timeout 900 python3 tools/load_s4.py $b 2>&1 | grep -v "^  " | grep -E "need review|stored|REJECT|nothing|==|ok" ; done
