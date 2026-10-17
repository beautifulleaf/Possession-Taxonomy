"""Move a batch's scene tags whose maker is neither in data/makers.tsv nor in the batch's own makers file to
verify/out/deferred_scene_tags.tsv (they wait for the batch that creates the maker; R-79).
usage: defer_unknown_tags.py BATCH"""
import sys
from common import ROOT, read_tsv, write_tsv

b = sys.argv[1]; out = ROOT / "verify/out"
known = {m["maker_id"] for m in read_tsv(ROOT / "data/makers.tsv")}
mf = out / f"{b}_makers.tsv"
if mf.exists(): known |= {m["maker_id"] for m in read_tsv(mf)}
tf = out / f"{b}_scene_tags.tsv"
tags = read_tsv(tf); cols = list(tags[0].keys())
wait = [t for t in tags if t["subject_type"] == "maker" and t["subject_id"] not in known]
if wait:
    dp = out / "deferred_scene_tags.tsv"
    old = read_tsv(dp) if dp.exists() else []
    have = {t["tag_id"] for t in old}
    old += [{c: t.get(c, "") for c in cols} for t in wait if t["tag_id"] not in have]
    write_tsv(dp, old, cols)
    write_tsv(tf, [t for t in tags if t not in wait], cols)
print(f"{b}: {len(wait)} tags deferred (maker not yet in data)")
