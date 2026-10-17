"""Load a scene (SCB_*) or regional (REG_*) clothing batch into data/ (R-74 to R-76).
usage: load_batch.py BATCH [CODE]   (CODE default A1)
Order: makers (merged by data_write), maker_kinds, lines, named forms, scene tags. A maker of the batch that no
maker_kinds, named-form, line or scene-tag row ties to the category gets a category-level maker_kinds row
(kind_id = CODE) on its own sources: the batch prompts admit a maker only from a page that lists it as a brand or
designer of clothing (a fashion-week roster, a clothing-brand list), which shows the category but not the garment
(R-76). Scene proposals are not loaded here: they go to verify/out/scene_proposals_all.tsv for a check."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def run(table, path):
    if path.exists() and len(read_tsv(path)):
        r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", table, str(path)], capture_output=True, text=True)
        print((r.stdout + r.stderr).strip())
        return r.returncode == 0
    return True

def main():
    b = sys.argv[1]; code = sys.argv[2] if len(sys.argv) > 2 else "A1"
    out = ROOT / "verify/out"
    f = lambda s: out / f"{b}_{s}.tsv"
    ok = run("makers", f("makers"))
    tied = set()
    for s, col in (("maker_kinds", "maker_id"), ("named_forms", "maker_id"), ("lines", "maker_id"), ("scene_tags", "subject_id")):
        if f(s).exists(): tied |= {r[col] for r in read_tsv(f(s)) if r.get(col)}
    extra = []
    if f("makers").exists():
        for m in read_tsv(f("makers")):
            if m["maker_id"] not in tied and m.get("sources"):
                extra.append({"offer_id": f"MK-{m['maker_id'][2:]}-{code}", "maker_id": m["maker_id"], "kind_id": code,
                              "notes": "category level: listed as a clothing brand or designer; garment type not shown (R-76)",
                              "sources": m["sources"], "fetch_status": m["fetch_status"]})
    mk = read_tsv(f("maker_kinds")) if f("maker_kinds").exists() else []
    tmp = ROOT / f"verify/work/load_{b}_maker_kinds.tsv"; tmp.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(tmp, mk + extra, TABLES["maker_kinds"][1])
    ok &= run("maker_kinds", tmp)
    ok &= run("lines", f("lines"))
    ok &= run("named_forms", f("named_forms"))
    ok &= run("scene_tags", f("scene_tags"))
    if f("scene_proposals").exists():
        props = [dict(r, batch=b) for r in read_tsv(f("scene_proposals"))]
        allp = out / "scene_proposals_all.tsv"
        prev = [r for r in read_tsv(allp) if r.get("batch") != b] if allp.exists() else []
        write_tsv(allp, prev + props, TABLES["scenes"][1] + ["batch"])
        print(f"{len(props)} scene proposals queued")
    print(f"{b}: category-level ties added for {len(extra)} makers; {'ok' if ok else 'SOME ROWS REJECTED: see verify/out/data_rejects_*.tsv'}")

if __name__ == "__main__":
    main()
