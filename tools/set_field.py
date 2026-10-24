"""Set one field of one stored row (decision-pass wording changes, R-58: ids unchanged).
usage: set_field.py TABLE ID FIELD VALUE   (writes through common.write_tsv, backup in bak/)"""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

t, i, f, v = sys.argv[1:5]
key, cols = TABLES[t]
assert f in cols and f not in (key, "sources", "fetch_status"), f"bad field {f}"
rows = read_tsv(ROOT / f"data/{t}.tsv"); hit = [r for r in rows if r[key] == i]
assert hit, f"{i} not in {t}"
hit[0][f] = v
write_tsv(ROOT / f"data/{t}.tsv", rows, cols); print(f"{t} {i}.{f} set")
