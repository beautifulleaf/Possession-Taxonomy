"""Merge probe items from verify/out/P*.tsv into data/probes.tsv and blind batches.
usage: build_probes.py SEED N_ROUND1   -> verify/in/BP1.tsv (first N), verify/in/BP2.tsv (rest)
Placers see only id, item, definition. Stratum/type stay in data/probes.tsv."""
import sys, random, glob
from common import ROOT, read_tsv, write_tsv, norm

seed, n1 = int(sys.argv[1]), int(sys.argv[2])
rows, seen, dups = [], set(), 0
for p in sorted(glob.glob(str(ROOT / "verify/out/P0*.tsv"))):
    batch = p.rsplit("/", 1)[1].split(".")[0]
    for r in read_tsv(p):
        k = norm(r.get("item", ""))
        if not k or not r.get("definition"):
            continue
        if k in seen:
            dups += 1; continue
        seen.add(k)
        r["batch"] = batch
        rows.append(r)
random.Random(seed).shuffle(rows)
for i, r in enumerate(rows, 1):
    r["id"] = f"Q{i:04d}"
    r["round"] = "1" if i <= n1 else "2"
F = ["id", "round", "item", "definition", "stratum", "type", "batch", "source_url"]
write_tsv(ROOT / "data/probes.tsv", rows, F)
write_tsv(ROOT / "verify/in/BP1.tsv", [r for r in rows if r["round"] == "1"], ["id", "item", "definition"])
write_tsv(ROOT / "verify/in/BP2.tsv", [r for r in rows if r["round"] == "2"], ["id", "item", "definition"])
from collections import Counter
print(f"{len(rows)} items ({dups} duplicates dropped); round1 {min(n1,len(rows))}, round2 {max(0,len(rows)-n1)}")
print("types:", dict(Counter(r.get('type','') for r in rows)))
