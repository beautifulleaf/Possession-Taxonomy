"""Session-4 batch load in one step (R-78, R-79): for BATCH, drop sources its fetch log shows were not fetched, defer
scene tags whose maker is not yet anywhere, load with load_batch.py, then load any deferred scene tags and named forms
whose makers now exist, and tidy category-level ties. usage: load_s4.py BATCH [BATCH ...]"""
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

for b in sys.argv[1:]:
    print(f"== {b}")
    log = ROOT / f"verify/work/{b}/fetched.tsv"
    for f in sorted((ROOT / "verify/out").glob(f"{b}_*.tsv")):
        if log.exists() and any(f.stem.endswith(s) for s in ("makers", "maker_kinds", "scene_tags", "named_forms", "lines", "roster_only")):
            run(ROOT / "tools/drop_excerpt_sources.py", f, log)
    if (ROOT / f"verify/out/{b}_scene_tags.tsv").exists(): run(ROOT / "tools/defer_unknown_tags.py", b)
    run(ROOT / "tools/load_batch.py", b)
retry("scene_tags", "scene_tags"); retry("named_forms", "named_forms")
run(ROOT / "tools/tidy_ties.py")
