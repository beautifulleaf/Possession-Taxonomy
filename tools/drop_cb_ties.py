"""Remove the category-level A1 ties load_batch.py adds for a country-backfill batch (CB_*): those batches only
fill countries of makers already tied (by scene tags or rows), and their pages show a base, not clothing (R-90).
usage: drop_cb_ties.py BATCH"""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

b = sys.argv[1]
ids = {r["maker_id"] for r in read_tsv(ROOT / f"verify/out/{b}_makers.tsv")}
srcs = {r["maker_id"]: r["sources"] for r in read_tsv(ROOT / f"verify/out/{b}_makers.tsv")}
mk = read_tsv(ROOT / "data/maker_kinds.tsv")
keep = [r for r in mk if not (r["kind_id"] == "A1" and r["maker_id"] in ids and r["sources"] == srcs[r["maker_id"]])]
write_tsv(ROOT / "data/maker_kinds.tsv", keep, TABLES["maker_kinds"][1])
print(f"{b}: {len(mk) - len(keep)} category-level ties from country pages removed")
