"""Re-normalise makers.country to ISO 3166-1 alpha-2 (R-75(b)); needed after rows were written while pycountry was
missing (R-79(h)). usage: normalise_countries.py  -> rewrites data/makers.tsv (backup in bak/), prints what stays unresolved."""
from collections import Counter
from common import ROOT, read_tsv, write_tsv
from regions import country
from schema import TABLES

rows = read_tsv(ROOT / "data/makers.tsv"); changed = 0; left = Counter()
for r in rows:
    v = (r.get("country") or "").strip(); c = country(v)
    if c and c != v: r["country"] = c; changed += 1
    elif v and not c: left[v] += 1
write_tsv(ROOT / "data/makers.tsv", rows, TABLES["makers"][1])
print(f"{changed} countries converted; unresolved: {dict(left.most_common(30))}")
