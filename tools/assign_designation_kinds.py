"""Assign stored designations to kinds after a decision pass (R-112): FILE has designation_id, kind_id.
usage: assign_designation_kinds.py FILE   -> sets kind_id and binds=kind, clears the "missing kind?" note, and adds
the non-maker named form of each newly bound designation (as load_og.py does); unknown kind ids are listed and skipped."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
from load_og import named_forms

kinds = {k["kind_id"]: k for k in read_tsv(ROOT / "data/kinds.tsv")}
want = {r["designation_id"]: r["kind_id"].strip() for r in read_tsv(sys.argv[1]) if r.get("kind_id", "").strip()}
rows = read_tsv(ROOT / "data/designations.tsv"); done, bad = [], []
for d in rows:
    k = want.get(d["designation_id"])
    if not k: continue
    if k not in kinds: bad.append((d["designation_id"], k)); continue
    d["kind_id"], d["binds"] = k, "kind"
    d["notes"] = "; ".join(x for x in d["notes"].split("; ") if "missing kind" not in x.lower())
    done.append(d)
write_tsv(ROOT / "data/designations.tsv", rows, TABLES["designations"][1])
print(f"{len(done)} designations bound; {len(bad)} unknown kinds: {bad[:10]}")
named_forms(done, kinds, "assign_" + __import__("pathlib").Path(sys.argv[1]).stem)
