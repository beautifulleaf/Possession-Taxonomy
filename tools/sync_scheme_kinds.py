"""Widen each scheme's kinds_served to the kinds of the named forms its tier entries rate (R-124 g).
usage: sync_scheme_kinds.py"""
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
D = ROOT / "data"
nfk = {r["named_form_id"]: r["kind_id"] for r in read_tsv(D / "named_forms.tsv")}
use = {}
for t in read_tsv(D / "tier_entries.tsv"):
    k = nfk.get(t["subject_id"]) if t["subject_type"] == "named_form" else (t["subject_id"] if t["subject_type"] == "kind" else None)
    if k: use.setdefault(t["scheme_id"], set()).add(k)
sch = read_tsv(D / "schemes.tsv"); n = 0
for s in sch:
    have = [x.strip() for x in s["kinds_served"].split("|") if x.strip()]
    add = sorted(use.get(s["scheme_id"], set()) - set(have))
    if add: s["kinds_served"] = " | ".join(have + add); n += len(add)
write_tsv(D / "schemes.tsv", sch, TABLES["schemes"][1])
print(f"{n} kinds added to scheme kinds_served")
