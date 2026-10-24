"""Build the shopper-facing reader page for one category (R-126 readability exemplar).
usage: build_reader_page.py CODE [--proposal BATCH]
Reads display names (framework/structure/navigation/display.tsv), display groups and quality markers
(framework/structure/navigation/groups.tsv, markers.tsv), kinds, named forms, lines and makers. With --proposal BATCH
the groups, display names and markers come from verify/out/<BATCH>_groups.tsv, _display.tsv and _markers.tsv instead,
so a proposal can be seen before it is applied. Writes pages/reader_<CODE>.html with its data inline. No ids, sources
chips or working terms are shown (READABILITY_RULES.md). The page is generated; edit this script, never the HTML."""
import json, re, sys
from common import ROOT, read_tsv

code = sys.argv[1]
prop = sys.argv[sys.argv.index("--proposal") + 1] if "--proposal" in sys.argv else None
nav = ROOT / "framework/structure/navigation"
src = (lambda t: ROOT / f"verify/out/{prop}_{t}.tsv") if prop else (lambda t: nav / f"{t}.tsv")
K = {k["kind_id"]: k for k in read_tsv(ROOT / "data/kinds.tsv") if k["code"] == code}
D = {d["kind_id"]: d for d in read_tsv(src("display"))} if src("display").exists() else {}
G = [g for g in read_tsv(src("groups")) if g["code"] == code]
MK = [m for m in read_tsv(src("markers")) if m["code"] == code]
M = {m["maker_id"]: m["name"] for m in read_tsv(ROOT / "data/makers.tsv")}
NF, LN = {}, {}
for n in read_tsv(ROOT / "data/named_forms.tsv"):
    if n["kind_id"] in K: NF.setdefault(n["kind_id"], []).append(n)
for l in read_tsv(ROOT / "data/lines.tsv"):
    for k in re.split(r"[;|]", l["kinds"]):
        if k.strip() in K: LN.setdefault(k.strip(), []).append(l)

def name_of(kid):
    if kid in D: return D[kid]["display_name"], D[kid]["also_called"]
    n = K[kid]["name"]; also = re.findall(r"[\[(]([^\])]*)[\])]", n)
    base = re.sub(r"\s*[\[(][^\])]*[\])]", "", n).strip()
    return base[:1].upper() + base[1:], " · ".join(a.strip() for a in also)

def kind_row(kid):
    k = K[kid]; dn, also = name_of(kid)
    ex = sorted(NF.get(kid, []), key=lambda n: (M.get(n["maker_id"], "~"), n["name"]))
    models = [[n["name"], M.get(n["maker_id"], "")] for n in ex]
    ranges = [[l["name"], M.get(l["maker_id"], "")] for l in LN.get(kid, [])]
    first = (k["sources"].split(" | ") or [""])[0].strip()
    return {"n": dn, "a": also, "d": k["definition"][:1].upper() + k["definition"][1:], "m": models, "r": ranges, "s": first}

depts = []
for t in [g for g in G if g["level"] == "1"]:
    subs = [g for g in G if g["parent_group"] == t["group_id"]] or [t]
    shelves = [{"n": s["group_name"], "k": [kind_row(m) for m in s["members"].split("; ") if m in K]} for s in subs]
    best = [{"m": m["marker"], "v": m["values"], "w": m["why"]} for m in MK if m["group_id"] == t["group_id"]]
    depts.append({"n": t["group_name"], "id": re.sub(r"[^a-z0-9]+", "-", t["group_name"].lower()).strip("-"), "s": shelves, "b": best})
data = {"code": code, "depts": depts}
title = {"C1": "Tools and workshop equipment"}.get(code, code)
tpl = (ROOT / "tools/reader_template.html").read_text()
out = tpl.replace("__TITLE__", title).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
p = ROOT / f"pages/reader_{code}.html"; p.write_text(out)
print(p, len(out) // 1024, "KB;", len(depts), "departments,", sum(len(d["s"]) for d in depts), "shelves,",
      sum(len(s["k"]) for d in depts for s in d["s"]), "kinds")
