"""Load a quality-signal or platform batch (QS_, PF_; R-118): drop sources the batch's fetch log does not show
(tools/check_batch.py --fix), then add each output table in foreign-key order through tools/data_write.py.
usage: load_qs.py BATCH CODE
Tables read from verify/out/<BATCH>_<table>.tsv when present: schemes, standards, makers, maker_kinds, lines,
named_forms, tier_entries, standard_values, attributes, platforms, compatibility. A named form whose kind is unknown is
held in verify/out/<BATCH>_named_forms_held.tsv, with the tier entries and standard values that rest on it."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

ORDER = ["schemes", "standards", "makers", "maker_kinds", "lines", "named_forms", "platforms", "scene_tags", "tier_entries",
         "standard_values", "attributes", "compatibility"]

def run(*a):
    r = subprocess.run([sys.executable, *map(str, a)], capture_output=True, text=True, cwd=ROOT / "tools")
    out = (r.stdout + r.stderr).strip()
    if out: print(out)
    return r.returncode == 0

def main():
    b, code = sys.argv[1], sys.argv[2]
    run(ROOT / "tools/check_batch.py", b, code, "--fix")
    kinds = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv")}
    held = set()
    for t in ORDER:
        p = ROOT / f"verify/out/{b}_{t}.tsv"
        if not p.exists(): continue
        rows = [r for r in read_tsv(p) if (r.get(TABLES[t][0]) or "").strip()]
        if t == "named_forms":
            bad = [r for r in rows if r["kind_id"].strip() not in kinds]
            if bad:
                write_tsv(ROOT / f"verify/out/{b}_named_forms_held.tsv", bad, TABLES[t][1])
                held = {r["named_form_id"] for r in bad}
                rows = [r for r in rows if r["named_form_id"] not in held]
        if t in ("tier_entries", "standard_values", "attributes", "compatibility") and held:
            col = "from_id" if t == "compatibility" else "subject_id"
            rows = [r for r in rows if r[col] not in held]
        rows = [r for r in rows if (r.get("sources") or "").strip()]
        if t in ("tier_entries", "standard_values", "attributes"):  # a subject must be stored (QS_I1 lesson)
            nfs = {n["named_form_id"] for n in read_tsv(ROOT / "data/named_forms.tsv")}
            lost = [r for r in rows if r.get("subject_type", "named_form") == "named_form" and r["subject_id"] not in nfs]
            if lost:
                write_tsv(ROOT / f"verify/out/{b}_{t}_held.tsv", lost, TABLES[t][1]); print(f"{t}: {len(lost)} held, subject not stored")
                rows = [r for r in rows if r not in lost]
        if t == "compatibility":  # both ends must be stored platforms or named forms
            ok = {n["named_form_id"] for n in read_tsv(ROOT / "data/named_forms.tsv")} | {
                x["platform_id"] for x in read_tsv(ROOT / "data/platforms.tsv")}
            lost = [r for r in rows if r["from_id"] not in ok or r["to_id"] not in ok]
            if lost:
                write_tsv(ROOT / f"verify/out/{b}_compatibility_held.tsv", lost, TABLES[t][1]); print(f"compatibility: {len(lost)} held")
                rows = [r for r in rows if r not in lost]
        if not rows: continue
        tmp = ROOT / f"verify/work/{b}/{t}_load.tsv"; tmp.parent.mkdir(parents=True, exist_ok=True)
        write_tsv(tmp, rows, TABLES[t][1])
        if not run(ROOT / "tools/data_write.py", "add", t, tmp):
            print(f"{b}: {t} refused; fix the rejects and re-run (later tables not loaded)"); sys.exit(1)

if __name__ == "__main__":
    main()
