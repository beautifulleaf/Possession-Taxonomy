"""Repair node names that kept memo markdown and were cut at a colon (DPH_G finding, session 7): 'Houses** (kind axis'
with axis 'attachment ...)' becomes name 'Houses', axis 'attachment ...'; other bold residue is stripped.
usage: fix_node_markdown.py  (backup in bak/, written through common.write_tsv to a temp file then renamed)"""
import os, shutil, time
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

p = ROOT / "data/nodes.tsv"
rows = read_tsv(p); n = 0
for r in rows:
    if "**" not in r["name"]: continue
    name, _, rest = r["name"].partition("**")
    rest = rest.strip()
    if rest.startswith("(kind axis"):
        r["axis"] = r["axis"].strip().rstrip(")").strip()
    elif rest.startswith("(") and rest.endswith(")"):
        r["notes"] = (r["notes"] + "; " if r["notes"] else "") + rest[1:-1]
    r["name"] = name.strip(); n += 1
(ROOT / "bak").mkdir(exist_ok=True)
shutil.copy(p, ROOT / f"bak/nodes.tsv.{time.strftime('%Y%m%d%H%M%S')}")
tmp = p.with_suffix(".tmp"); write_tsv(tmp, rows, TABLES["nodes"][1]); os.replace(tmp, p)
print(n, "node names repaired")
