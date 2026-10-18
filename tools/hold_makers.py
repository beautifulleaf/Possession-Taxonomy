"""Take makers back out of the A1 count when their only evidence is a roster that does not show clothing (R-87).
usage: hold_makers.py LIST.tsv REASON  (LIST has maker_id) -> removes their category-level A1 maker_kinds rows; a maker
with no other row pointing to it (garment ties, named forms, lines, scene tags, relations, children) leaves
data/makers.tsv for verify/out/held_makers.tsv with the reason, to come back when a page shows its garments."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

D = ROOT / "data"
ids = {r["maker_id"] for r in read_tsv(sys.argv[1])}; reason = sys.argv[2]
mk = read_tsv(D / "maker_kinds.tsv")
keep_mk = [r for r in mk if not (r["maker_id"] in ids and r["kind_id"] == "A1")]
write_tsv(D / "maker_kinds.tsv", keep_mk, TABLES["maker_kinds"][1])
used = {r["maker_id"] for r in keep_mk} | {r["maker_id"] for r in read_tsv(D / "named_forms.tsv")} \
     | {r["maker_id"] for r in read_tsv(D / "lines.tsv")} | {r["subject_id"] for r in read_tsv(D / "scene_tags.tsv")} \
     | {r["maker_id"] for r in read_tsv(D / "maker_relations.tsv")} | {r["other_id"] for r in read_tsv(D / "maker_relations.tsv")}
makers = read_tsv(D / "makers.tsv")
used |= {m["parent_id"] for m in makers if m.get("parent_id")}
out = [m for m in makers if m["maker_id"] in ids and m["maker_id"] not in used]
write_tsv(D / "makers.tsv", [m for m in makers if m not in out], TABLES["makers"][1])
p = ROOT / "verify/out/held_makers.tsv"
old = read_tsv(p) if p.exists() else []
write_tsv(p, old + [dict(m, reason=reason) for m in out], TABLES["makers"][1] + ["reason"])
print(f"{len(mk) - len(keep_mk)} category-level ties removed; {len(out)} makers held in verify/out/held_makers.tsv")
