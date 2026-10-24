"""Build the shopper-facing reader (R-126): every category in a top strip, the open category's departments and shelves in a
sidebar, items in the main column, as the Culinary taxonomy page is laid out (owner, session 12).
usage: build_reader_page.py [--proposal CODE:BATCH ...]
Writes pages/reader.html (shell with the category list and a search index) and pages/reader/<CODE>.json per category.
Display names come from framework/structure/navigation/display.tsv, groups and quality markers from groups.tsv and
markers.tsv; --proposal C1:RD_C1 takes C1's groups, display names and markers from verify/out/RD_C1_*.tsv instead, so a
proposal can be read before it is applied. Kinds without a display row get the mechanical clean-up of READABILITY_RULES.md
(synonyms out of the name, sentence case); kinds in no group go to a closing "Other" shelf. No ids, source chips or
working terms are shown. The page is generated; edit this script or tools/reader_template.html, never the output."""
import json, re, sys
from collections import defaultdict
from common import ROOT, read_tsv

props = dict(a.split(":") for a in sys.argv[sys.argv.index("--proposal") + 1:]) if "--proposal" in sys.argv else {}
nav = ROOT / "framework/structure/navigation"
fw = (ROOT / "framework/CATEGORIES_v0_7_3.md").read_text()
DOMAINS, CATS = [], []
for line in fw[fw.index("## Categories"):fw.index("## Appendix A")].splitlines():
    if m := re.match(r"^### ([A-J]) — (.+)$", line): DOMAINS.append({"d": m.group(1), "n": m.group(2).strip()})
    elif m := re.match(r"^- \*\*([A-J]\d+) ([^*]+)\*\*", line): CATS.append({"c": m.group(1), "n": m.group(2).strip(), "d": m.group(1)[0]})

kinds = defaultdict(dict)
for k in read_tsv(ROOT / "data/kinds.tsv"):
    if k["status"] != "retired": kinds[k["code"]][k["kind_id"]] = k
disp = {d["kind_id"]: d for d in read_tsv(nav / "display.tsv")} if (nav / "display.tsv").exists() else {}
groups, markers = defaultdict(list), defaultdict(list)
for g in read_tsv(nav / "groups.tsv"): groups[g["code"]].append(g)
for m in read_tsv(nav / "markers.tsv"): markers[m["code"]].append(m)
for code, b in props.items():
    groups[code] = [g for g in read_tsv(ROOT / f"verify/out/{b}_groups.tsv") if g["code"] == code]
    markers[code] = [m for m in read_tsv(ROOT / f"verify/out/{b}_markers.tsv") if m["code"] == code]
    disp.update({d["kind_id"]: d for d in read_tsv(ROOT / f"verify/out/{b}_display.tsv")})
cardof = {}  # R-129: sibling kinds shown as one card
if (nav / "cards.tsv").exists():
    for c in read_tsv(nav / "cards.tsv"):
        for m in c["members"].split(";"):
            if m.strip(): cardof[m.strip()] = c
mk = {m["maker_id"]: m["name"] for m in read_tsv(ROOT / "data/makers.tsv")}
iss = {i["issuer_id"]: i["name"] for i in read_tsv(ROOT / "data/issuers.tsv")}
nfs, lns = defaultdict(list), defaultdict(list)
for n in read_tsv(ROOT / "data/named_forms.tsv"): nfs[n["kind_id"]].append(n)
for l in read_tsv(ROOT / "data/lines.tsv"):
    for k in re.split(r"[;|]", l["kinds"]):
        if k.strip(): lns[k.strip()].append(l)

def name_of(k):
    if k["kind_id"] in disp: return disp[k["kind_id"]]["display_name"], disp[k["kind_id"]]["also_called"]
    n = k["name"]; also = [a.strip() for a in re.findall(r"[\[(]([^\])]*)[\])]", n)]
    base = re.sub(r"\s*[\[(][^\])]*[\])]", "", n).strip()
    if k.get("native_name"): also.append(k["native_name"])
    return base[:1].upper() + base[1:], " · ".join(a for a in also if a)

def who(n):
    if n["maker_id"]: return mk.get(n["maker_id"], "")
    m = re.match(r"issuer (I-[a-z0-9-]+)", n["notes"] or "")
    return "issued by " + iss.get(m.group(1), "") if m else ""

def item(k):
    dn, also = name_of(k)
    models = sorted(([n["name"], who(n)] for n in nfs[k["kind_id"]]), key=lambda x: (x[1] or "~", x[0]))
    ranges = sorted([l["name"], mk.get(l["maker_id"], "")] for l in lns[k["kind_id"]])
    d = ((disp.get(k["kind_id"]) or {}).get("description") or k["definition"]).strip()
    return {"n": dn, "a": also, "d": d[:1].upper() + d[1:], "m": models, "r": ranges, "s": (k["sources"].split(" | ") or [""])[0].strip()}

# scene view (clothing is navigated genre first, owner 2026-10-17 and session 6; R-71): clusters > scenes > brands
SC = read_tsv(ROOT / "data/scenes.tsv"); TG = [t for t in read_tsv(ROOT / "data/scene_tags.tsv") if t["subject_type"] == "maker"]
def scene_view(code, K):
    pieces = defaultdict(list)
    for kid in K:
        for n in nfs[kid]:
            if n["maker_id"]: pieces[n["maker_id"]].append(n["name"])
    by_scene = defaultdict(list)
    for t in TG: by_scene[t["scene_id"]].append(t)
    out = []
    for cl in dict.fromkeys(x["cluster"] for x in SC if x["cluster"] and code in x["domains"].split(",")):
        scenes = []
        for x in [x for x in SC if x["cluster"] == cl and code in x["domains"].split(",")]:
            tags = sorted(by_scene[x["scene_id"]], key=lambda t: (t["strength"] != "core", mk.get(t["subject_id"], "").lower()))
            if not tags: continue
            scenes.append({"n": x["name"] + (f" [{x['native_name']}]" if x["native_name"] else ""), "d": x["description"], "src": x["definition_source"],
                           "b": [[mk.get(t["subject_id"], t["subject_id"]), 1 if t["strength"] == "core" else 0, sorted(set(pieces.get(t["subject_id"], [])))[:8]] for t in tags]})
        if scenes: out.append({"n": cl, "s": scenes})
    return out

(ROOT / "pages/reader").mkdir(exist_ok=True)
index, counts = [], {}
for c in CATS:
    code = c["c"]; K = kinds.get(code, {}); G = groups.get(code, []); placed = set(); depts = []
    for t in [g for g in G if g["level"] == "1"]:
        subs = [g for g in G if g["parent_group"] == t["group_id"]]
        own = [m for m in t["members"].split("; ") if m in K]
        shelves = ([{"n": t["group_name"], "k": own}] if own else []) + [{"n": s["group_name"], "k": [m for m in s["members"].split("; ") if m in K]} for s in subs]
        shelves = [s for s in shelves if s["k"]]
        if not shelves: continue
        for s in shelves: placed.update(s["k"])
        best = [{"m": m["marker"], "v": m["values"], "w": m["why"]} for m in markers[code] if {x.strip() for x in m["group_id"].split(";")} & ({t["group_id"]} | {s["group_id"] for s in subs})]
        depts.append({"n": t["group_name"], "s": shelves, "b": best})
    rest = [k for k in K if k not in placed]
    if rest: depts.append({"n": "Other", "s": [{"n": "Not yet grouped", "k": sorted(rest)}], "b": []})
    for d in depts:
        for s in d["s"]:
            rows, done = [], set()
            for kid in s["k"]:
                c = cardof.get(kid)
                if not c: rows.append(item(K[kid])); continue
                if c["card_id"] in done: continue
                done.add(c["card_id"]); its = [item(K[m.strip()]) for m in c["members"].split(";") if m.strip() in K]
                rows.append({"n": c["name"], "a": " · ".join(x for x in dict.fromkeys(a for i in its for a in i["a"].split(" · ")) if x),
                             "d": c["description"], "t": [i["n"] for i in its], "m": [m for i in its for m in i["m"]], "r": [r for i in its for r in i["r"]], "s": ""})
            s["k"] = rows
            for i, it in enumerate(s["k"]): index.append([code, it["n"], " · ".join(x for x in [it["a"], " · ".join(it.get("t", []))] if x)])
    counts[code] = len(K)
    whole = [{"m": m["marker"], "v": m["values"], "w": m["why"]} for m in markers[code] if m["group_id"].strip() == code]
    extra = {"scenes": scene_view(code, K)} if code == "A1" else {}
    (ROOT / f"pages/reader/{code}.json").write_text(json.dumps({"c": code, "b": whole, **extra, "rev": code in props or (bool(K) and all(k in disp for k in K)), "depts": depts}, ensure_ascii=False, separators=(",", ":")))
for c in CATS: c["k"] = counts.get(c["c"], 0)
shell = {"domains": DOMAINS, "cats": CATS, "index": index}
tpl = (ROOT / "tools/reader_template.html").read_text()
out = tpl.replace("__DATA__", json.dumps(shell, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
(ROOT / "pages/reader.html").write_text(out)
size = sum(p.stat().st_size for p in (ROOT / "pages/reader").glob("*.json"))
print(f"pages/reader.html {len(out) // 1024} KB; {len(CATS)} categories, {sum(counts.values())} kinds; category files {size // 1024} KB")
