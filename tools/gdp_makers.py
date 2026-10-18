"""Bring held makers back for a recovery batch (R-87, R-92): for BATCH, write verify/out/<BATCH>_makers.tsv with the
held maker rows (verify/out/*_held_unconfirmed.tsv and verify/out/held_makers.tsv) of the makers the batch tied at
garment level, so load_s4.py can load them with their new ties. usage: gdp_makers.py BATCH"""
import glob, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

b = sys.argv[1]
tied = {r["maker_id"] for r in read_tsv(ROOT / f"verify/out/{b}_maker_kinds.tsv")}
held = {}
for f in glob.glob(str(ROOT / "verify/out/*_held_unconfirmed.tsv")) + [str(ROOT / "verify/out/held_makers.tsv")]:
    for r in read_tsv(f): held.setdefault(r["maker_id"], r)
rows = [held[m] for m in sorted(tied) if m in held]
write_tsv(ROOT / f"verify/out/{b}_makers.tsv", rows, TABLES["makers"][1])
print(f"{b}: {len(rows)} held makers restored for {len(tied)} tied ids")
