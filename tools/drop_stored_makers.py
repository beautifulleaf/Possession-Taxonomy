"""Before loading a batch: drop rows of verify/out/<BATCH>_makers.tsv whose maker_id is already stored, so a reused
maker keeps its stored row (the loaders add or replace; a batch row would overwrite the fuller stored one).
usage: drop_stored_makers.py BATCH [...]"""
import sys
from common import ROOT, read_tsv, write_tsv
stored = {r["maker_id"] for r in read_tsv(ROOT / "data/makers.tsv")}
for b in sys.argv[1:]:
    p = ROOT / f"verify/out/{b}_makers.tsv"
    if not p.exists(): continue
    rows = read_tsv(p)
    if not rows: continue
    keep = [r for r in rows if r["maker_id"] not in stored]
    write_tsv(p, keep, list(rows[0].keys()))
    print(f"{b}: {len(rows) - len(keep)} stored maker rows dropped, {len(keep)} new kept")
