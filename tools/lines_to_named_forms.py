"""Single-kind lines that are named forms by C2(d) (R-124 d).
usage: lines_to_named_forms.py CODE [CODE ...]
A line whose kind list holds one kind of CODE and under which at most one named form is filed becomes a maker-bound
named form NF-<kind>-L<nnn> (name, maker, sources and notes kept); a named form filed under it keeps the new named form
as base_named_form_id. Lines with two or more models filed under them stay lines (R-70). Converted rows are kept in
verify/out/lines_to_named_forms.tsv."""
import collections, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
D = ROOT / "data"
codes = set(sys.argv[1:])
lines = read_tsv(D / "lines.tsv"); nf = read_tsv(D / "named_forms.tsv")
cnt = collections.Counter(r["line_id"] for r in nf)
ids = {r["named_form_id"] for r in nf}
conv, keep, new = [], [], {}
for l in lines:
    ks = [k for k in l["kinds"].split(";") if k.strip()]
    if len(ks) == 1 and ks[0].split(".")[0] in codes and cnt[l["line_id"]] <= 1:
        n = 1
        while f"NF-{ks[0]}-L{n:03d}" in ids: n += 1
        i = f"NF-{ks[0]}-L{n:03d}"; ids.add(i); new[l["line_id"]] = i; conv.append(l)
        nf.append({"named_form_id": i, "kind_id": ks[0], "name": l["name"], "maker_bound": "yes", "maker_id": l["maker_id"],
                   "first_year": l["years"][:4] if l["years"][:4].isdigit() else "", "licensor_id": l["licensor_id"],
                   "notes": (f"was line {l['line_id']} (R-124 d); " + l["notes"]).strip("; "), "sources": l["sources"], "fetch_status": l["fetch_status"]})
    else: keep.append(l)
for r in nf:
    if r.get("line_id") in new: r["base_named_form_id"] = r["base_named_form_id"] or new[r["line_id"]]; r["line_id"] = ""
write_tsv(D / "named_forms.tsv", nf, TABLES["named_forms"][1]); write_tsv(D / "lines.tsv", keep, TABLES["lines"][1])
write_tsv(ROOT / "verify/out/lines_to_named_forms.tsv", conv, TABLES["lines"][1])
print(f"{len(conv)} lines became named forms")
