"""Move kinds to another category (R-128): one home per object, ids never reused (R-58).
usage (from the repo root): python3 tools/move_kinds.py BATCH
Reads verify/out/<BATCH>_kind_moves.tsv: old_kind_id, new_kind_id, sub_family, leaf, group_id, display_name, also_called, reason.
- data/kinds.tsv: a copy of the old row enters under new_kind_id (code, sub_family, leaf from the move; notes "moved from
  <old> (<BATCH>)"); the old row gets status "retired" and notes "moved to <new> (<BATCH>)". Sources and attestation stay.
- named_forms, maker_kinds, attributes, tier_entries (subject or kind columns) and standard_values follow to the new id;
  named-form ids are kept (opaque ids). lines.kinds and schemes.kinds_served follow.
- Navigation: the old id leaves its display group and display row; the new id joins group_id with a display row.
Every write goes through common.write_tsv (backup to bak/, temp file)."""
import re, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

b = sys.argv[1]
mv = [r for r in read_tsv(ROOT / f"verify/out/{b}_kind_moves.tsv") if r["old_kind_id"].strip()]
M = {r["old_kind_id"].strip(): r for r in mv}
kp = ROOT / "data/kinds.tsv"; K = read_tsv(kp); have = {k["kind_id"] for k in K}
for o, r in M.items():
    assert o in have, f"{o} not stored"; assert r["new_kind_id"] not in have, f"{r['new_kind_id']} already used"
add = []
for k in K:
    r = M.get(k["kind_id"])
    if not r: continue
    n = dict(k); n.update(kind_id=r["new_kind_id"], code=r["new_kind_id"].split(".")[0], sub_family=r["sub_family"], leaf=r["leaf"],
                          notes=(f"moved from {k['kind_id']} ({b}); " + k["notes"]).strip("; "))
    add.append(n); k["status"] = "retired"; k["notes"] = (f"moved to {r['new_kind_id']} ({b}); " + k["notes"]).strip("; ")
write_tsv(kp, K + add, TABLES["kinds"][1])
sub = {o: r["new_kind_id"] for o, r in M.items()}
def swap_list(v):
    parts = re.split(r"(\s*[;|]\s*)", v)
    return "".join(sub.get(p, p) for p in parts)
for t, cols in [("named_forms", ["kind_id"]), ("maker_kinds", ["kind_id"]), ("attributes", ["subject_id"]),
                ("tier_entries", ["subject_id"]), ("standard_values", ["subject_id"]), ("lines", ["kinds"]), ("schemes", ["kinds_served"])]:
    p = ROOT / f"data/{t}.tsv"
    if not p.exists(): continue
    rows = read_tsv(p); n = 0
    for r in rows:
        for c in cols:
            if c in r:
                new = swap_list(r[c]) if c in ("kinds", "kinds_served") else sub.get(r[c], r[c])
                if new != r[c]: r[c] = new; n += 1
    if n: write_tsv(p, rows, TABLES[t][1]); print(f"{t}: {n} references moved")
nav = ROOT / "framework/structure/navigation"
G = read_tsv(nav / "groups.tsv")
for g in G:
    ms = [m.strip() for m in g["members"].split(";") if m.strip() and m.strip() not in M]
    for r in mv:
        if g["group_id"] == r["group_id"]: ms.append(r["new_kind_id"])
    g["members"] = "; ".join(ms)
write_tsv(nav / "groups.tsv", G, ["code", "group_id", "group_name", "level", "parent_group", "members"])
D = [d for d in read_tsv(nav / "display.tsv") if d["kind_id"] not in M]
D += [{"kind_id": r["new_kind_id"], "display_name": r["display_name"], "also_called": r["also_called"], "description": "", "notes": b} for r in mv]
write_tsv(nav / "display.tsv", D, ["kind_id", "display_name", "also_called", "description", "notes"])
print(f"{len(mv)} kinds moved: " + ", ".join(f"{o} -> {r['new_kind_id']}" for o, r in M.items()))
