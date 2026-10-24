"""Retire kinds absorbed by a merge decision (R-118 a): status becomes "retired", notes say "merged into <id>"; the id
is never reused or deleted. Run after the merge's named-form moves (tools/apply_dp.py). Refuses while named forms still
sit under a retired kind. usage: retire_kinds.py BATCH  (reads verify/out/<BATCH>_merges.tsv: kind_id, other_code = kept kind)"""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def main():
    b = sys.argv[1]
    mg = read_tsv(ROOT / f"verify/out/{b}_merges.tsv")
    kinds = {k["kind_id"]: k for k in read_tsv(ROOT / "data/kinds.tsv")}
    used = {r["kind_id"] for r in read_tsv(ROOT / "data/named_forms.tsv")}
    out = []
    for r in mg:
        kid, keep = r["kind_id"].strip(), r["other_code"].strip()
        if kid not in kinds: print("not stored, nothing to retire:", kid); continue
        if kid in used: print("named forms still under", kid, "- apply the moves first"); continue
        k = dict(kinds[kid]); k["status"] = "retired"
        k["notes"] = (f"merged into {keep} ({b}); " + k["notes"]).strip("; ")
        out.append(k)
    if not out: return
    p = ROOT / f"verify/work/{b}/kinds_retire.tsv"; p.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(p, out, TABLES["kinds"][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "kinds", str(p)], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())

if __name__ == "__main__":
    main()
