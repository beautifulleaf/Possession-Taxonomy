"""Session-4 batch load in one step (R-78, R-79): for BATCH, drop sources its fetch log shows were not fetched, defer
scene tags whose maker is not yet anywhere, load with load_batch.py, then load any deferred scene tags and named forms
whose makers now exist, and tidy category-level ties. usage: load_s4.py BATCH [BATCH ...]
A stage-3 harvest batch HV_<CODE>_n loads its attested kinds first and ties untied makers at category <CODE>
(R-97); every other batch is an A1 batch."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def run(*a):
    r = subprocess.run([sys.executable, *map(str, a)], capture_output=True, text=True, cwd=ROOT / "tools")
    out = (r.stdout + r.stderr).strip()
    if out: print(out)
    return r.returncode == 0

def retry(name, table):
    p = ROOT / f"verify/out/deferred_{name}.tsv"
    if not p.exists(): return
    rows = read_tsv(p)
    if not rows: return
    known = {m["maker_id"] for m in read_tsv(ROOT / "data/makers.tsv")}
    col = "subject_id" if table == "scene_tags" else "maker_id"
    ok = [r for r in rows if r[col] in known]
    if not ok: return
    tmp = ROOT / f"verify/work/deferred_{name}_ready.tsv"; tmp.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(tmp, ok, TABLES[table][1])
    if run(ROOT / "tools/data_write.py", "add", table, tmp):
        write_tsv(p, [r for r in rows if r[col] not in known], list(rows[0].keys()))
        print(f"deferred {name}: {len(ok)} loaded, {len(rows) - len(ok)} still waiting")

def remap(b):
    """Point a batch's maker ids at the ids kept by tools/merge_makers.py (R-86, R-89), so a load never recreates a
    merged-away maker."""
    to = {}
    for m in ("maker_merges", "maker_merges_manual", "MRG_S4_merges"):
        p = ROOT / f"verify/out/{m}.tsv"
        if p.exists(): to.update({r["drop_id"]: r["keep_id"] for r in read_tsv(p)})
    if not to: return
    for f in sorted((ROOT / "verify/out").glob(f"{b}_*.tsv")):
        rows = read_tsv(f)
        if not rows: continue
        n = 0
        for r in rows:
            for c in ("maker_id", "subject_id", "parent_id", "built_by_maker_id", "licensor_id"):
                if r.get(c) in to: r[c] = to[r[c]]; n += 1
            if n and "offer_id" in r and r.get("kind_id"): r["offer_id"] = f"MK-{r['maker_id'][2:]}-{r['kind_id']}"
            if n and "tag_id" in r and r.get("subject_type") == "maker": r["tag_id"] = f"TG-{r['scene_id'][3:]}-{r['subject_id'][2:]}"
        if n:
            key = list(rows[0].keys())[0]; seen = {}
            for r in rows: seen.setdefault(r[key], r)
            write_tsv(f, list(seen.values()), list(rows[0].keys())); print(f"{f.name}: {n} merged ids remapped")

for b in sys.argv[1:]:
    print(f"== {b}")
    remap(b)
    log = ROOT / f"verify/work/{b}/fetched.tsv"
    for f in sorted((ROOT / "verify/out").glob(f"{b}_*.tsv")):
        if log.exists() and any(f.stem.endswith(s) for s in ("makers", "maker_kinds", "scene_tags", "named_forms", "lines", "roster_only")):
            run(ROOT / "tools/drop_excerpt_sources.py", f, log)
    if (ROOT / f"verify/out/{b}_scene_tags.tsv").exists(): run(ROOT / "tools/defer_unknown_tags.py", b)
    code = b.split("_")[1] if b.startswith("HV_") else "A1"
    kf = ROOT / f"verify/out/{b}_kinds.tsv"
    if code != "A1" and kf.exists() and read_tsv(kf): run(ROOT / "tools/data_write.py", "add", "kinds", kf)
    run(ROOT / "tools/load_batch.py", b, code)
retry("scene_tags", "scene_tags"); retry("named_forms", "named_forms")
run(ROOT / "tools/tidy_ties.py")
