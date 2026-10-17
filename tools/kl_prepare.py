"""Kind-level test, part 1: settle ids, freeze trees, build placer files (R-58 to R-63).
usage: kl_prepare.py normalise   -> E1, F2, I2 builder ids (<CODE>-Knn) to tree-path ids; crosswalk to verify/out/KL_id_crosswalk.tsv
       kl_prepare.py fixitems    -> item fixes decided in R-62 (backup to bak/)
       kl_prepare.py freeze      -> audit/KL_<CODE>_tree.md (never overwritten), verify/in/KL_<CODE>_place.tsv (no expected_kind),
                                    verify/out/KL_untested.tsv (tree kinds no item expects); checks every expected_kind is a tree kind
Tree-path ids (R-58): <CODE>.n sub-family, <CODE>.n.m leaf, kind <CODE>.n.m.kk, or <CODE>.n.kk where a sub-family has no leaf."""
import re, sys, shutil, time, filecmp
from common import ROOT, read_tsv, write_tsv

CODES = "A2 B8 C1 D4 E1 F2 F4 G2 H2 I2 J5".split()
OUT, AUD, VIN = ROOT / "verify/out", ROOT / "audit", ROOT / "verify/in"
ITEM_FIELDS = ["id", "item", "definition", "expected_kind", "source_url"]

def backup(p):
    (ROOT / "bak").mkdir(exist_ok=True)
    shutil.copy2(p, ROOT / "bak" / f"{p.name}.{time.strftime('%Y%m%d-%H%M%S')}")

def write_text(p, s):
    backup(p)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(s, encoding="utf-8")
    tmp.replace(p)

IDS_LINE = ("Ids (R-58): {c}.n is a sub-family and {c}.n.m a leaf; the id you give is the kind, "
            "{c}.n.m.kk, or {c}.n.kk where a sub-family has no leaf.")

def normalise(code):
    p = OUT / f"KL_{code}_tree.md"
    lines = p.read_text(encoding="utf-8").split("\n")
    kid = re.compile(rf"^- ({code}-K\d+)\b")
    sf = None; leaf = None; nleaf = 0; nkind = 0
    xw, out = [], []
    def next_nonempty(i):
        for j in range(i + 1, len(lines)):
            if lines[j].strip(): return lines[j]
        return ""
    for i, ln in enumerate(lines):
        m = re.match(rf"^## ({code}\.\d+)\b", ln)
        if m:
            sf, leaf, nleaf, nkind = m.group(1), None, 0, 0
            out.append(ln); continue
        if ln.startswith("## "):
            sf = leaf = None; out.append(ln); continue
        if sf:
            m3 = re.match(rf"^### ({code}\.\d+\.\d+)\b", ln)
            if m3:                                   # F2 style leaf heading
                leaf, nkind = m3.group(1), 0; out.append(ln); continue
            if ln.startswith("Leaf: "):              # I2 style leaf heading
                nleaf += 1; leaf, nkind = f"{sf}.{nleaf}", 0
                out.append(f"### {leaf} {ln[6:]}"); continue
            if (ln.strip() and not ln.startswith(("-", "#", "Leaf axis", "No leaf"))
                    and kid.match(next_nonempty(i))):  # E1 style plain leaf heading
                nleaf += 1; leaf, nkind = f"{sf}.{nleaf}", 0
                out.append(f"### {leaf} {ln.strip()}"); continue
            m = kid.match(ln)
            if m:
                nkind += 1
                new = f"{leaf or sf}.{nkind:02d}"
                name = ln[m.end():].strip().split(":")[0]
                xw.append({"code": code, "old_id": m.group(1), "new_id": new, "kind": name})
                out.append(f"- {new}" + ln[m.end():]); continue
        out.append(ln)
    mp = {r["old_id"]: r["new_id"] for r in xw}
    text = "\n".join(out)
    text = re.sub(rf"\b{code}-K\d+\b", lambda m: mp.get(m.group(0), m.group(0)), text)
    left = re.findall(rf"\b{code}-K\d+\b", text)
    if left: sys.exit(f"{code}: ids without a kind line: {sorted(set(left))}")
    # ids sentence after the first paragraph that follows the title
    t = text.split("\n\n", 2)
    text = "\n\n".join([t[0], t[1], IDS_LINE.format(c=code), t[2]])
    write_text(p, text)
    ip = OUT / f"KL_{code}_items.tsv"
    items = read_tsv(ip)
    for r in items:
        old = r["expected_kind"].strip()
        if old not in mp: sys.exit(f"{code}: item {r['id']} expects unknown {old}")
        r["expected_kind"] = mp[old]
    write_tsv(ip, items, ITEM_FIELDS)
    return xw

ITEM_FIXES = {  # R-62
    "KL-F2-22": {"definition": "Hand-painted, clear-glazed slip-cast earthenware figure of a girl sitting in an apple tree, "
                               "10.25 in high, sculpted by Arthur Moeller in 1940, number 141 in a German maker's series."},
}

def fixitems():
    for code in CODES:
        ip = OUT / f"KL_{code}_items.tsv"
        items = read_tsv(ip); hit = False
        for r in items:
            if r["id"] in ITEM_FIXES:
                r.update(ITEM_FIXES[r["id"]]); hit = True
        if hit: write_tsv(ip, items, ITEM_FIELDS); print("fixed", code)

def tree_kinds(code, text):
    """id lines: '- <id> name: def', '  - <id> ...', '  - **<id> name**: def'."""
    ks = {}
    for ln in text.split("\n"):
        m = re.match(rf"^\s*-\s+\**({code}(?:\.\d+)+)\**\s+(.*)$", ln)
        if not m: continue
        ks[m.group(1)] = re.split(r"[:.]\s|\*\*", m.group(2).strip("* "))[0].strip("* ")
    return {k: v for k, v in ks.items() if not any(o.startswith(k + ".") for o in ks)}  # an id with children is a leaf

def freeze():
    AUD.mkdir(exist_ok=True)
    untested, bad = [], []
    for code in CODES:
        src, dst = OUT / f"KL_{code}_tree.md", AUD / f"KL_{code}_tree.md"
        if dst.exists():
            if not filecmp.cmp(src, dst, shallow=False): sys.exit(f"{dst} exists and differs: frozen copies are never edited")
        else:
            shutil.copy2(src, dst)
        text = dst.read_text(encoding="utf-8")
        ks = tree_kinds(code, text)
        items = read_tsv(OUT / f"KL_{code}_items.tsv")
        exp = {r["expected_kind"].strip() for r in items}
        bad += [(code, r["id"], r["expected_kind"]) for r in items if r["expected_kind"].strip() not in ks]
        untested += [{"code": code, "kind_id": k, "kind": v} for k, v in ks.items() if k not in exp]
        write_tsv(VIN / f"KL_{code}_place.tsv", items, ["id", "item", "definition"])
        print(f"{code}: {len(ks)} kinds in tree, {len(items)} items, {len(exp)} kinds expected, {len(ks) - len(exp & set(ks))} untested")
    write_tsv(OUT / "KL_untested.tsv", untested, ["code", "kind_id", "kind"])
    if bad: sys.exit(f"expected kinds not found in the frozen tree: {bad}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "normalise":
        if (OUT / "KL_id_crosswalk.tsv").exists(): sys.exit("crosswalk exists: ids already normalised")
        xw = []
        for c in ["E1", "F2", "I2"]: xw += normalise(c)
        write_tsv(OUT / "KL_id_crosswalk.tsv", xw, ["code", "old_id", "new_id", "kind"])
        print(len(xw), "ids normalised")
    elif cmd == "fixitems": fixitems()
    elif cmd == "freeze": freeze()
    else: sys.exit(__doc__)
