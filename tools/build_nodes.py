"""Union of harvested source category nodes -> data/source_nodes.tsv, and crosswalk batches verify/in/CW0N.tsv.
usage: build_nodes.py N_BATCHES"""
import sys, glob
from common import ROOT, read_tsv, write_tsv
nb = int(sys.argv[1])
out, seen = [], set()
for f in sorted(glob.glob(str(ROOT / "verify/out/H0*.tsv"))):
    b = f.rsplit("/", 1)[1][:3]
    for r in read_tsv(f):
        path = [x.strip() for x in (r.get("level1"), r.get("level2"), r.get("level3")) if x and x.strip()]
        if not path: continue
        k = (r.get("source", "").strip(), tuple(path))
        if k in seen: continue
        seen.add(k)
        out.append({"batch": b, "source": r.get("source", "").strip(), "path": " > ".join(path),
                    "note": (r.get("note") or "").strip()})
for i, r in enumerate(out, 1): r["nid"] = f"N{i:04d}"
write_tsv(ROOT / "data/source_nodes.tsv", out, ["nid", "batch", "source", "path", "note"])
size = -(-len(out) // nb)
for j in range(nb):
    part = out[j * size:(j + 1) * size]
    write_tsv(ROOT / f"verify/in/CW{j+1:02d}.tsv", part, ["nid", "source", "path", "note"])
print(len(out), "nodes;", nb, "batches of", size)
