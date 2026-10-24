"""Keep designations binding one kind (binds = kind) on the kind of their named form (notes "designation <id>", JC1,
R-112) after named forms move kind (DPH_J3 split, R-119). usage: sync_designation_kinds.py"""
import os, shutil, time
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

nf = {}
for r in read_tsv(ROOT / "data/named_forms.tsv"):
    if r["notes"].startswith("designation "): nf[r["notes"].split()[1]] = r["kind_id"]
p = ROOT / "data/designations.tsv"; rows = read_tsv(p); n = 0
for d in rows:
    k = nf.get(d["designation_id"])
    if d["binds"] == "kind" and k and d["kind_id"] != k: d["kind_id"] = k; n += 1
if n:
    (ROOT / "bak").mkdir(exist_ok=True); shutil.copy(p, ROOT / f"bak/designations.tsv.{time.strftime('%Y%m%d%H%M%S')}")
    tmp = p.with_suffix(".tmp"); write_tsv(tmp, rows, TABLES["designations"][1]); os.replace(tmp, p)
print(n, "designations moved to their named form's kind")
