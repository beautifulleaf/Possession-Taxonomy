"""Add structure rows (data/nodes.tsv) for leaves that new kinds sit in but the tree did not have (R-105).
usage: add_leaf_nodes.py   -> for every kind whose leaf id is missing from nodes, add a leaf node named from the
decision pass's parent column ("B10.7.2 Housing and containment (new leaf)" in verify/out/DPW1_<CODE>_kinds.tsv)."""
import glob, re, subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

nodes = {n["node_id"] for n in read_tsv(ROOT / "data/nodes.tsv")}
names = {}
for f in glob.glob(str(ROOT / "verify/out/DP*_kinds.tsv")):
    for r in read_tsv(f):
        m = re.match(r"^\s*([A-J]\d+\.\d+\.\d+)\s+(.+?)\s*(\(new leaf\))?\s*$", r.get("parent", ""))
        if m: names.setdefault(m.group(1), (m.group(2), f.split("/")[-1].replace("_kinds.tsv", "")))
add = {}
for k in read_tsv(ROOT / "data/kinds.tsv"):
    leaf = k["leaf"]
    if leaf and leaf not in nodes and leaf not in add:
        name, src = names.get(leaf, ("", ""))
        if not name: print(f"no name for leaf {leaf} (kind {k['kind_id']})"); continue
        add[leaf] = {"node_id": leaf, "code": k["code"], "level": "leaf", "parent_id": k["sub_family"], "name": name,
                     "axis": "", "sort": leaf.split(".")[-1], "notes": f"new leaf from {src} (R-105)", "sources": "", "fetch_status": ""}
if add:
    p = ROOT / "verify/work/add_leaf_nodes.tsv"; write_tsv(p, list(add.values()), TABLES["nodes"][1])
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "nodes", str(p)])
print(f"{len(add)} leaf nodes added: {', '.join(add)}")
