"""Repair the escape doubling of R-82: before the fix, write_tsv escaped quotes and backslashes that read_tsv read back
literally, so every rewrite doubled them. Collapses each run of backslashes before a quote (or before * and _, which
also gained them) to nothing. usage: fix_backslashes.py FILE.tsv ...  (backup in bak/ via write_tsv)"""
import re, sys
from common import read_tsv, write_tsv

for p in sys.argv[1:]:
    rows = read_tsv(p)
    if not rows: continue
    cols = list(rows[0].keys()); n = 0
    for r in rows:
        for k, v in r.items():
            if v and "\\" in v:
                w = re.sub(r'\\+(?=["*_])', "", v)
                if w != v: r[k] = w; n += 1
    if n: write_tsv(p, rows, cols); print(f"{p}: {n} fields repaired")
