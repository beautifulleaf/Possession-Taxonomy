"""Apply a scene vocabulary pass (R-114 b): BATCH_scenes.tsv rows enter data/scenes.tsv through data_write (their
sources must be in the candidate batches' fetch logs: checked with check_batch-style canonical URLs), and
BATCH_changes.tsv acts on stored scenes: merge_into (tags re-pointed to the kept scene, the merged scene removed and its
name kept in the kept scene's description as "also: <name>"), move_cluster, set_parent.
usage: apply_scene_changes.py BATCH LOG_BATCH [LOG_BATCH ...]"""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES
from check_batch import canon

b, logs = sys.argv[1], sys.argv[2:]
ok = set()
for l in logs:
    for r in read_tsv(ROOT / f"verify/work/{l}/fetched.tsv"):
        if (r.get("fetch_status") or "").strip().lower() in ("full", "partial", "ok"): ok.add(canon(r["url"]))
new = read_tsv(ROOT / f"verify/out/{b}_scenes.tsv"); keep = []
for r in new:
    pairs = [(u.strip(), f.strip()) for u, f in zip(r["sources"].split("|"), r["fetch_status"].split("|")) if canon(u) in ok]
    if not pairs: print("unlogged, skipped:", r["scene_id"]); continue
    r["sources"] = " | ".join(u for u, _ in pairs); r["fetch_status"] = " | ".join(f for _, f in pairs)
    if canon(r["definition_source"]) not in ok: r["definition_source"] = pairs[0][0]
    keep.append(r)
p = ROOT / f"verify/work/{b}/scenes_in.tsv"; write_tsv(p, keep, TABLES["scenes"][1])
print(subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "scenes", str(p)], capture_output=True, text=True).stdout.strip())
sc = read_tsv(ROOT / "data/scenes.tsv"); by = {s["scene_id"]: s for s in sc}; tags = read_tsv(ROOT / "data/scene_tags.tsv"); drop = set()
for c in read_tsv(ROOT / f"verify/out/{b}_changes.tsv"):
    s, a, t = c["scene_id"], c["action"], c["target"]
    if s not in by: print("unknown scene", s); continue
    if a == "merge_into" and t in by:
        have = {(x["subject_id"], x["scene_id"]) for x in tags}
        for x in tags:
            if x["scene_id"] == s:
                if (x["subject_id"], t) in have: drop.add(x["tag_id"]); continue
                x["scene_id"] = t; x["tag_id"] = f"TG-{t[3:]}-{x['subject_id'][2:]}"
        by[t]["description"] = by[t]["description"].rstrip(". ") + f". Also: {by[s]['name']}."; del by[s]
    elif a == "move_cluster": by[s]["cluster"] = t
    elif a == "set_parent" and t in by: by[s]["parent_id"] = t
    print(a, s, t)
write_tsv(ROOT / "data/scenes.tsv", list(by.values()), TABLES["scenes"][1])
write_tsv(ROOT / "data/scene_tags.tsv", [x for x in tags if x["tag_id"] not in drop], TABLES["scene_tags"][1])
