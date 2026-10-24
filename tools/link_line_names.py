"""Link named forms to their maker's line of the same name (R-124 c; DPW1_B1 line gaps).
usage: link_line_names.py [MAKER_ID:NAME ...]
1. Each NAME given makes a new line L-<maker slug>-<name slug> for MAKER_ID when two or more of its named forms carry
   that name (BILLY / OXBERG counts for BILLY); its sources are the named forms' sources.
2. A named form with no line whose name (or first part before " / ") equals, after normalising, the name of a line of
   the same maker gets that line_id. Run tools/fix_lines.py afterwards so the lines list their kinds."""
import re, sys, unicodedata
from common import ROOT, read_tsv, write_tsv, norm
from schema import TABLES
D = ROOT / "data"
def slug(s): return re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).strip("-")
def key(s): return norm(s.split(" / ")[0])
nf = read_tsv(D / "named_forms.tsv"); lines = {l["line_id"]: l for l in read_tsv(D / "lines.tsv")}
for a in sys.argv[1:]:
    m, name = a.split(":", 1)
    rows = [r for r in nf if r["maker_id"] == m and key(r["name"]) == key(name)]
    if len(rows) < 2: print("too few named forms for", a); continue
    lid = f"L-{slug(m[2:])}-{slug(name)}"
    if lid in lines: continue
    src = []
    for r in rows:
        for u, f in zip(r["sources"].split(" | "), r["fetch_status"].split(" | ")):
            if u not in [x for x, _ in src]: src.append((u, f))
    lines[lid] = {"line_id": lid, "maker_id": m, "name": name, "kinds": ";".join(dict.fromkeys(r["kind_id"] for r in rows)),
                  "notes": "range over several kinds (R-124 c)", "sources": " | ".join(u for u, _ in src), "fetch_status": " | ".join(f for _, f in src)}
by = {}
for l in lines.values(): by.setdefault((l["maker_id"], key(l["name"])), l["line_id"])
n = 0
for r in nf:
    if not r["line_id"] and r["maker_id"] and (r["maker_id"], key(r["name"])) in by:
        r["line_id"] = by[(r["maker_id"], key(r["name"]))]; n += 1
write_tsv(D / "lines.tsv", list(lines.values()), TABLES["lines"][1]); write_tsv(D / "named_forms.tsv", nf, TABLES["named_forms"][1])
print(f"{len(lines)} lines; {n} named forms linked to a same-name line")
