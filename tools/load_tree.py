"""Load a decided tree (verify/out/TREE_<CODE>.md, or a frozen audit/KL_<CODE>_tree*.md) into the stage-3 tables.
usage: load_tree.py CODE [TREE_FILE]
- data/nodes.tsv: one row per category, sub-family and leaf (structure; no sources needed), written through
  tools/data_write.py add (validation and backup there).
- verify/out/HV_<CODE>_worklist.tsv: one row per kind (kind_id, sub_family, leaf, name, definition, dagger), the
  harvest's list of kinds to attest. Kinds enter data/kinds.tsv only from a harvest row with a fetched source."""
import re, subprocess, sys
from common import ROOT, write_tsv
from schema import TABLES

def parse(code, text):
    nodes, kinds = [{"node_id": code, "code": code, "level": "category", "parent_id": "", "name": "", "axis": "", "sort": "0"}], []
    sf = leaf = None; sort = 0
    for ln in text.split("\n"):
        m = re.match(rf"^## ({code}\.\d+)\s+(.*)$", ln) or re.match(r"^## (\d+)\s+(.*)$", ln)  # A2: "## 1 Sneakers"
        if m:
            sf = m.group(1) if m.group(1).startswith(code) else f"{code}.{m.group(1)}"
            leaf = None; sort += 1
            nodes.append({"node_id": sf, "code": code, "level": "sub_family", "parent_id": code,
                          "name": m.group(2).strip(), "axis": "", "sort": str(sort)}); continue
        if ln.startswith("## "): sf = leaf = None; continue
        m = (re.match(rf"^### ({code}\.\d+\.\d+)\s+(.*)$", ln) or re.match(rf"^Leaf ({code}\.\d+\.\d+)\s+(.*)$", ln)
             or re.match(r"^Leaf (\d+\.\d+)\s+(.*)$", ln))  # C1 "Leaf C1.1.1 Saws", A2 "Leaf 2.1 Fastened: ..."
        if m and sf:
            leaf = m.group(1) if m.group(1).startswith(code) else f"{code}.{m.group(1)}"; sort += 1
            nodes.append({"node_id": leaf, "code": code, "level": "leaf", "parent_id": sf,
                          "name": m.group(2).strip(), "axis": "", "sort": str(sort)}); continue
        if sf and re.match(r"^(Leaf axis|Kind axis|Kind key)", ln.strip()):
            target = leaf if (leaf and ln.strip().startswith(("Kind axis", "Kind key"))) else sf
            for n in nodes:
                if n["node_id"] == target and not n["axis"]: n["axis"] = ln.strip()
            continue
        m = re.match(rf"^\s*-\s+\**({code}(?:\.\d+)+)\**\s+(.*)$", ln)
        if m and sf:
            kid, rest = m.group(1), m.group(2).strip()
            name, _, definition = rest.partition(":")
            dagger = "yes" if rest.endswith("†") else ""
            kinds.append({"kind_id": kid, "sub_family": sf, "leaf": leaf if leaf and kid.startswith(leaf + ".") else "",
                          "name": name.strip("* ").strip(), "definition": definition.strip().rstrip("†").strip(),
                          "dagger": dagger})
    # a bullet id with children is a leaf written as a list line (G2, H2 style); leaf 0 is leaf = null (R-58)
    ids = [k["kind_id"] for k in kinds]
    leaves = {i for i in ids if any(o.startswith(i + ".") for o in ids)}
    for k in kinds:
        if k["kind_id"] in leaves:
            sort += 1
            nodes.append({"node_id": k["kind_id"], "code": code, "level": "leaf", "parent_id": k["sub_family"],
                          "name": k["name"], "axis": k["definition"], "sort": str(sort)})
    kinds = [k for k in kinds if k["kind_id"] not in leaves]
    for k in kinds:
        if not k["leaf"]:
            k["leaf"] = next((l for l in leaves if k["kind_id"].startswith(l + ".")), "")
        if k["leaf"].endswith(".0"): k["leaf"] = ""
    nodes = [n for n in nodes if not (n["level"] == "leaf" and n["node_id"].endswith(".0"))]
    return nodes, kinds

def main():
    code = sys.argv[1]
    tree = ROOT / (sys.argv[2] if len(sys.argv) > 2 else f"verify/out/TREE_{code}.md")
    nodes, kinds = parse(code, tree.read_text(encoding="utf-8"))
    ids = [k["kind_id"] for k in kinds]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: sys.exit(f"duplicate kind ids: {sorted(dup)}")
    for n in nodes: n["notes"] = f"from {tree.relative_to(ROOT)}"; n["sources"] = ""; n["fetch_status"] = ""
    tmp = ROOT / f"verify/work/load_tree_{code}_nodes.tsv"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(tmp, nodes, TABLES["nodes"][1])
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "nodes", str(tmp)], check=True)
    write_tsv(ROOT / f"verify/out/HV_{code}_worklist.tsv", kinds, ["kind_id", "sub_family", "leaf", "name", "definition", "dagger"])
    print(f"{code}: {sum(n['level'] == 'sub_family' for n in nodes)} sub-families, "
          f"{sum(n['level'] == 'leaf' for n in nodes)} leaves, {len(kinds)} kinds ({sum(k['dagger'] == 'yes' for k in kinds)} †)")

if __name__ == "__main__":
    main()
