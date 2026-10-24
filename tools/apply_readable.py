"""Apply a readability review (R-126) for one category: display names, display groups and quality markers.
usage (from the repo root): python3 tools/apply_readable.py BATCH CODE [--check]
Reads verify/out/<BATCH>_display.tsv (kind_id, display_name, also_called, description, notes), _groups.tsv (code, group_id,
group_name, level, parent_group, members) and, when present, _markers.tsv (the markers.tsv columns). Checks that every
kind of CODE sits in exactly one group, that members and display rows name stored kinds of CODE, and reports group sizes
outside READABILITY_RULES.md (shelves of one, groups over fifteen, first levels outside five to nine). With --check
nothing is written. Otherwise backs up the three navigation files to bak/ and replaces CODE's rows in them."""
import shutil, sys, time
from common import ROOT, read_tsv, write_tsv

b, code = sys.argv[1], sys.argv[2]
nav = ROOT / "framework/structure/navigation"
K = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv") if k["code"] == code}
D = [r for r in read_tsv(ROOT / f"verify/out/{b}_display.tsv") if r["kind_id"].strip()]
G = [g for g in read_tsv(ROOT / f"verify/out/{b}_groups.tsv") if g["group_id"].strip()]
mp = ROOT / f"verify/out/{b}_markers.tsv"
MK = [m for m in read_tsv(mp) if m["marker"].strip()] if mp.exists() else None
err, warn = [], []
seen = {}
for g in G:
    if g["code"] != code: err.append(f"group {g['group_id']} has code {g['code']}")
    for m in [x.strip() for x in g["members"].split(";") if x.strip()]:
        if m not in K: err.append(f"{g['group_id']}: {m} is not a stored {code} kind")
        if m in seen: err.append(f"{m} in {seen[m]} and {g['group_id']}")
        seen[m] = g["group_id"]
miss = K - set(seen)
if miss: err.append(f"{len(miss)} kinds in no group: {sorted(miss)[:10]}")
ids = {g["group_id"] for g in G}
for g in G:
    if g["level"] == "2" and g["parent_group"] not in ids: err.append(f"{g['group_id']}: parent {g['parent_group']} missing")
for r in D:
    if r["kind_id"] not in K: err.append(f"display row {r['kind_id']} is not a stored {code} kind")
    if not r["display_name"].strip(): err.append(f"display row {r['kind_id']} has no name")
tops = [g for g in G if g["level"] == "1"]
if not 5 <= len(tops) <= 9: warn.append(f"{len(tops)} first-level groups")
for g in G:
    n = len([x for x in g["members"].split(";") if x.strip()])
    has_kids = any(x["parent_group"] == g["group_id"] for x in G)
    if not has_kids and n == 1: warn.append(f"{g['group_id']} {g['group_name']}: one kind")
    if n > 15: warn.append(f"{g['group_id']} {g['group_name']}: {n} kinds")
if MK is not None:
    for m in MK:
        if m["group_id"] not in ids: err.append(f"marker '{m['marker']}' points at {m['group_id']}, not a new group")
print(f"{b} {code}: {len(K)} kinds, {len(D)} display rows, {len(tops)} departments, {len(G) - len(tops)} shelves")
for w in warn: print("  warn:", w)
for e in err: print("  ERROR:", e)
if err or "--check" in sys.argv: sys.exit(1 if err else 0)

stamp = time.strftime("%Y%m%d-%H%M%S")
(ROOT / "bak").mkdir(exist_ok=True)
DCOLS = ["kind_id", "display_name", "also_called", "description", "notes"]
dp = nav / "display.tsv"
old = read_tsv(dp) if dp.exists() else []
for p in (dp, nav / "groups.tsv", nav / "markers.tsv"):
    if p.exists(): shutil.copy(p, ROOT / f"bak/{p.stem}.{stamp}.tsv")
keep = [r for r in old if r["kind_id"] not in K]
write_tsv(dp, keep + [{c: r.get(c, "") for c in DCOLS} for r in D], DCOLS)
GC = ["code", "group_id", "group_name", "level", "parent_group", "members"]
allg = [g for g in read_tsv(nav / "groups.tsv") if g["code"] != code]
write_tsv(nav / "groups.tsv", allg + [{c: g.get(c, "") for c in GC} for g in G], GC)
if MK is not None:
    MC = ["code", "group_id", "marker", "values", "why", "evidence_rows"]
    allm = [m for m in read_tsv(nav / "markers.tsv") if m["code"] != code]
    write_tsv(nav / "markers.tsv", allm + [{c: m.get(c, "") for c in MC} for m in MK], MC)
else:
    old_ids = {g["group_id"] for g in read_tsv(ROOT / f"bak/groups.{stamp}.tsv") if g["code"] == code}
    stale = [m for m in read_tsv(nav / "markers.tsv") if m["code"] == code and m["group_id"] in old_ids - ids]
    if stale: print(f"  note: {len(stale)} stored markers point at replaced groups; give the batch a _markers.tsv")
print(f"  applied: display.tsv, groups.tsv{', markers.tsv' if MK is not None else ''} (backups bak/*.{stamp}.tsv)")
