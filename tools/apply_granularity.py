"""Apply a granularity review (R-129) for one category.
usage (from the repo root): python3 tools/apply_granularity.py BATCH CODE [--check]
- verify/out/<BATCH>_kinds.tsv: new kinds splitting a too-coarse kind. A row whose source is not a full or partial fetch in
  verify/work/<BATCH>/fetched.tsv is held (not loaded). Loaded through tools/data_write.py (backup, validation).
- verify/out/<BATCH>_nf_moves.tsv (named_form_id, new_kind_id): named forms re-filed under a loaded new kind.
- verify/out/<BATCH>_new_display.tsv (kind_id, display_name, also_called, description, group_id, old_kind_id, old_display_name):
  display row and shelf for each loaded new kind; the old kind's display name follows old_display_name.
- verify/out/<BATCH>_cards.tsv (card_id, code, name, description, members): sibling kinds shown as one card; every member must
  be a live kind of CODE and all members must share one shelf. Replaces CODE's rows in framework/structure/navigation/cards.tsv.
Writes through common.write_tsv (backup to bak/, temp file)."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

b, code = sys.argv[1], sys.argv[2]; check = "--check" in sys.argv
out, nav = ROOT / "verify/out", ROOT / "framework/structure/navigation"
rd = lambda n: [r for r in read_tsv(out / f"{b}_{n}.tsv") if any(v.strip() for v in r.values())] if (out / f"{b}_{n}.tsv").exists() else []
log = ROOT / f"verify/work/{b}/fetched.tsv"
ok_urls = {r["url"].strip() for r in read_tsv(log) if r.get("fetch_status", "").strip() in ("full", "partial")} if log.exists() else set()
K = read_tsv(ROOT / "data/kinds.tsv"); live = {k["kind_id"] for k in K if k["code"] == code and k["status"] != "retired"}; allk = {k["kind_id"] for k in K}
new = rd("kinds"); load, held = [], []
for r in new:
    srcs = [s.strip() for s in r["sources"].split("|") if s.strip()]
    good = r["code"] == code and r["kind_id"] not in allk and srcs and all(s in ok_urls for s in srcs)
    (load if good else held).append(r)
ids = {r["kind_id"] for r in load}
moves = [m for m in rd("nf_moves") if m["new_kind_id"] in ids]
nd = [d for d in rd("new_display") if d["kind_id"] in ids]
G = read_tsv(nav / "groups.tsv"); shelf = {}
for g in G:
    for m in g["members"].split(";"):
        if m.strip(): shelf[m.strip()] = g["group_id"]
cards, err = rd("cards"), []
for c in cards:
    ms = [m.strip() for m in c["members"].split(";") if m.strip()]
    if len(ms) < 2: err.append(f"{c['card_id']}: fewer than two members")
    for m in ms:
        if m not in live: err.append(f"{c['card_id']}: {m} is not a live {code} kind")
    if len({shelf.get(m) for m in ms}) > 1: err.append(f"{c['card_id']}: members on different shelves")
for d in nd:
    if d["group_id"] not in {g["group_id"] for g in G}: err.append(f"{d['kind_id']}: group {d['group_id']} unknown")
print(f"{b} {code}: {len(load)} new kinds ({len(held)} held: {[r['kind_id'] for r in held]}), {len(moves)} named-form moves, {len(cards)} cards")
for e in err: print("  ERROR:", e)
if err or check: sys.exit(1 if err else 0)
if held: write_tsv(out / f"{b}_kinds_held.tsv", held, TABLES["kinds"][1])
if load:
    p = ROOT / f"verify/work/{b}/kinds_in.tsv"; write_tsv(p, load, TABLES["kinds"][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "kinds", str(p)], capture_output=True, text=True); print((r.stdout + r.stderr).strip())
if moves:
    mv = {m["named_form_id"].strip(): m["new_kind_id"].strip() for m in moves}
    NF = read_tsv(ROOT / "data/named_forms.tsv"); n = 0
    for x in NF:
        if x["named_form_id"] in mv: x["kind_id"] = mv[x["named_form_id"]]; n += 1
    write_tsv(ROOT / "data/named_forms.tsv", NF, TABLES["named_forms"][1]); print(f"named_forms: {n} re-filed")
if nd:
    for g in G:
        add = [d["kind_id"] for d in nd if d["group_id"] == g["group_id"]]
        if add: g["members"] = "; ".join([m.strip() for m in g["members"].split(";") if m.strip()] + add)
    write_tsv(nav / "groups.tsv", G, ["code", "group_id", "group_name", "level", "parent_group", "members"])
    DC = ["kind_id", "display_name", "also_called", "description", "notes"]; D = read_tsv(nav / "display.tsv")
    ren = {d["old_kind_id"].strip(): d["old_display_name"].strip() for d in nd if d.get("old_kind_id", "").strip() and d.get("old_display_name", "").strip()}
    for x in D:
        if x["kind_id"] in ren: x["display_name"] = ren[x["kind_id"]]
    D += [{"kind_id": d["kind_id"], "display_name": d["display_name"], "also_called": d["also_called"], "description": d["description"], "notes": b} for d in nd]
    write_tsv(nav / "display.tsv", D, DC)
cp = nav / "cards.tsv"; CC = ["card_id", "code", "name", "description", "members"]
old = [c for c in read_tsv(cp) if c["code"] != code] if cp.exists() else []
write_tsv(cp, old + [{k: c.get(k, "") for k in CC} for c in cards], CC)
print("  applied")
