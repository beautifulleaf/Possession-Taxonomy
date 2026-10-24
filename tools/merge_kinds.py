"""Merge duplicate kinds into the kept kind (R-128): every reference follows to the kept id, the merged kind is retired
("merged into <id>", id never reused, R-58) and leaves the display layer. usage: python3 tools/merge_kinds.py BATCH
Reads verify/out/<BATCH>_kind_merges.tsv: kind_id, keep_kind_id, reason. Writes through common.write_tsv (backup to bak/)."""
import re, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
b = sys.argv[1]
M = {r["kind_id"].strip(): r["keep_kind_id"].strip() for r in read_tsv(ROOT / f"verify/out/{b}_kind_merges.tsv") if r["kind_id"].strip()}
K = read_tsv(ROOT / "data/kinds.tsv"); ids = {k["kind_id"] for k in K}
for a, keep in M.items(): assert a in ids and keep in ids, (a, keep)
for k in K:
    if k["kind_id"] in M: k["status"] = "retired"; k["notes"] = (f"merged into {M[k['kind_id']]} ({b}); " + k["notes"]).strip("; ")
write_tsv(ROOT / "data/kinds.tsv", K, TABLES["kinds"][1])
for t, cols in [("named_forms", ["kind_id"]), ("maker_kinds", ["kind_id"]), ("attributes", ["subject_id"]), ("tier_entries", ["subject_id"]),
                ("standard_values", ["subject_id"]), ("lines", ["kinds"]), ("schemes", ["kinds_served"])]:
    p = ROOT / f"data/{t}.tsv"
    if not p.exists(): continue
    rows = read_tsv(p); n = 0
    for r in rows:
        for c in cols:
            if c not in r: continue
            if c in ("kinds", "kinds_served"):
                parts = [M.get(x.strip(), x.strip()) for x in re.split(r"[;|]", r[c]) if x.strip()]
                sep = " | " if "|" in r[c] else ";"
                new = sep.join(dict.fromkeys(parts))
            else: new = M.get(r[c], r[c])
            if new != r[c]: r[c] = new; n += 1
    if n: write_tsv(p, rows, TABLES[t][1]); print(f"{t}: {n} references merged")
nav = ROOT / "framework/structure/navigation"
G = read_tsv(nav / "groups.tsv")
for g in G: g["members"] = "; ".join(m.strip() for m in g["members"].split(";") if m.strip() and m.strip() not in M)
write_tsv(nav / "groups.tsv", G, ["code", "group_id", "group_name", "level", "parent_group", "members"])
write_tsv(nav / "display.tsv", [d for d in read_tsv(nav / "display.tsv") if d["kind_id"] not in M], ["kind_id", "display_name", "also_called", "description", "notes"])
print(f"{len(M)} kinds merged: " + ", ".join(f"{a} -> {k}" for a, k in M.items()))
