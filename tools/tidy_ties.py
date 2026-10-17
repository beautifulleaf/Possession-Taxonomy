"""Drop category-level maker_kinds rows (kind_id = CODE) for makers that now have a garment-level row (R-76).
usage: tidy_ties.py [CODE]   (default A1; backup and temp-file write via common)"""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

code = sys.argv[1] if len(sys.argv) > 1 else "A1"
kinds = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv") if k["code"] == code}
rows = read_tsv(ROOT / "data/maker_kinds.tsv")
garment = {r["maker_id"] for r in rows if r["kind_id"] in kinds}
keep = [r for r in rows if not (r["kind_id"] == code and r["maker_id"] in garment)]
write_tsv(ROOT / "data/maker_kinds.tsv", keep, TABLES["maker_kinds"][1])
print(f"{code}: {len(rows) - len(keep)} category-level rows replaced by garment-level ties; {sum(r['kind_id'] == code for r in keep)} remain")
