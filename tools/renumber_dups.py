"""Give repeated ids inside one batch output a distinct suffix before loading (R-107).
usage: renumber_dups.py OUTPUT.tsv  -> the first row keeps its id, each later repeat gets <id>-D<n> (backup in bak/).
A resumed batch whose numbering restarted writes the same NF id twice for two different named forms."""
import sys
from common import read_tsv, write_tsv

rows = read_tsv(sys.argv[1]); key = list(rows[0].keys())[0]; seen = set(); n = 0
for r in rows:
    if r[key] in seen:
        i = 1
        while f"{r[key]}-D{i}" in seen: i += 1
        r[key] = f"{r[key]}-D{i}"; n += 1
    seen.add(r[key])
write_tsv(sys.argv[1], rows, list(rows[0].keys())); print(f"{sys.argv[1]}: {n} repeated ids renumbered")
