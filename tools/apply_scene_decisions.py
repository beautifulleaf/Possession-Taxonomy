"""Apply a scene decision list (R-81, R-95): accepted proposals enter data/scenes.tsv (with the cluster and parent
given in the decision), merged ones are re-pointed, and the waiting tags of verify/out/scene_tags_proposed_all.tsv
on accepted or merged scenes load into data/scene_tags.tsv.
usage: apply_scene_decisions.py DECISIONS.tsv  (columns: scene_id, decision accept/merge/reject, target, cluster,
parent_id, reason)"""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

dec = read_tsv(sys.argv[1])
props = {r["scene_id"]: r for r in read_tsv(ROOT / "verify/out/scene_proposals_all.tsv")}
loaded = {r["scene_id"] for r in read_tsv(ROOT / "data/scenes.tsv")}
acc, to = [], {}
for d in dec:
    if d["decision"] == "accept":
        p = dict(props[d["scene_id"]]); p["cluster"] = d["cluster"] or p["cluster"]; p["parent_id"] = d["parent_id"]
        acc.append(p); to[d["scene_id"]] = d["scene_id"]
    elif d["decision"] == "merge":
        to[d["scene_id"]] = d["target"]
w = ROOT / "verify/work/apply_scenes"; w.mkdir(parents=True, exist_ok=True)
def add(t, rows):
    if not rows: return
    write_tsv(w / f"{t}.tsv", rows, TABLES[t][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", t, str(w / f"{t}.tsv")], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())
add("scenes", acc)
ok = loaded | {a["scene_id"] for a in acc}
tags = {}
for t in read_tsv(ROOT / "verify/out/scene_tags_proposed_all.tsv"):
    s = to.get(t["scene_id"])
    if s and s in ok:
        t = dict(t); t["scene_id"] = s; t["tag_id"] = f"TG-{s[3:]}-{t['subject_id'][2:]}"
        tags.setdefault(t["tag_id"], t)
known = {m["maker_id"] for m in read_tsv(ROOT / "data/makers.tsv")}
add("scene_tags", [t for t in tags.values() if t["subject_id"] in known])
print(f"{len(acc)} scenes accepted, {sum(d['decision'] == 'merge' for d in dec)} merged, {len(tags)} waiting tags placed")
