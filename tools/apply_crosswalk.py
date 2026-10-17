"""Move one category's data onto a rebuilt tree (R-71: D1 restructure).
usage: apply_crosswalk.py CODE TREE.md CROSSWALK.tsv
- CROSSWALK.tsv: old_kind_id, new_kind_id (every kind of CODE in data/kinds.tsv must appear).
- data/nodes.tsv: the category's sub-family and leaf rows are replaced from TREE.md (tools/load_tree.py parser).
- data/kinds.tsv: kind_id, sub_family, leaf and sort follow the new tree; name and definition come from TREE.md;
  sources, fetch_status and notes are kept (the attestation does not change with the id).
- data/named_forms.tsv: kind_id follows; named_form_id is renamed NF-<new kind>-<nnn> keeping its number;
  references to renamed named forms (base_named_form_id, flanker_of) follow.
- data/lines.tsv: the kinds list follows. The old-to-new named-form ids go to verify/out/<CODE>_nf_crosswalk.tsv.
All writes go through common.write_tsv (backup to bak/, temp file)."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
from load_tree import parse

def main():
    code, tree, xw_path = sys.argv[1], ROOT / sys.argv[2], ROOT / sys.argv[3]
    xw = {r["old_kind_id"].strip(): r["new_kind_id"].strip() for r in read_tsv(xw_path)}
    nodes_new, kinds_new = parse(code, tree.read_text(encoding="utf-8"))
    tree_k = {k["kind_id"]: (i, k) for i, k in enumerate(kinds_new)}
    kinds = read_tsv(ROOT / "data/kinds.tsv")
    mine = [k for k in kinds if k["code"] == code]
    missing = [k["kind_id"] for k in mine if k["kind_id"] not in xw]
    if missing: sys.exit(f"kinds without a crosswalk row: {missing}")
    bad = [v for v in xw.values() if v not in tree_k]
    if bad: sys.exit(f"crosswalk targets not in the tree: {bad}")
    if len(set(xw.values())) != len(xw): sys.exit("two old kinds map to one new kind")
    for k in mine:
        i, t = tree_k[xw[k["kind_id"]]]
        k.update({"kind_id": t["kind_id"], "sub_family": t["sub_family"], "leaf": t["leaf"], "sort": str(i + 1),
                  "name": t["name"], "definition": t["definition"] or k["definition"]})
    write_tsv(ROOT / "data/kinds.tsv", kinds, TABLES["kinds"][1])
    nodes = [n for n in read_tsv(ROOT / "data/nodes.tsv") if n["code"] != code]
    for n in nodes_new: n.update({"notes": f"from {tree.relative_to(ROOT)}", "sources": "", "fetch_status": ""})
    write_tsv(ROOT / "data/nodes.tsv", nodes + nodes_new, TABLES["nodes"][1])
    nfs = read_tsv(ROOT / "data/named_forms.tsv")
    nf_map = {}
    for n in nfs:
        if n["kind_id"] in xw:
            new_k = xw[n["kind_id"]]
            num = n["named_form_id"].rsplit("-", 1)[-1]
            new_id = f"NF-{new_k}-{num}"
            nf_map[n["named_form_id"]] = new_id
            n["named_form_id"], n["kind_id"] = new_id, new_k
    for n in nfs:
        for col in ("base_named_form_id", "flanker_of"):
            if n.get(col) in nf_map: n[col] = nf_map[n[col]]
    if len({n["named_form_id"] for n in nfs}) != len(nfs): sys.exit("named-form id collision after renaming")
    write_tsv(ROOT / "data/named_forms.tsv", nfs, TABLES["named_forms"][1])
    lines = read_tsv(ROOT / "data/lines.tsv")
    for l in lines:
        l["kinds"] = ";".join(xw.get(k, k) for k in l["kinds"].split(";") if k)
    write_tsv(ROOT / "data/lines.tsv", lines, TABLES["lines"][1])
    write_tsv(ROOT / f"verify/out/{code}_nf_crosswalk.tsv", [{"old": a, "new": b} for a, b in nf_map.items()], ["old", "new"])
    print(f"{code}: {len(mine)} kinds, {len(nodes_new)} nodes, {len(nf_map)} named forms renamed")

if __name__ == "__main__":
    main()
