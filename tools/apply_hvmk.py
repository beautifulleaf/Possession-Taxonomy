"""Apply the HVMK decisions (R-70): named forms that are lines move to data/lines.tsv; non-named-forms are dropped;
misfiled named forms move kind. New kinds from verify/out/HVMK_kinds.tsv enter data/kinds.tsv only with a fetched
source, so they are written to verify/out/HVMK_new_kinds_worklist.tsv for attestation, not to data/.
usage: apply_hvmk.py   (backups and validation through tools/data_write.py; dropped rows are kept in verify/out/HVMK_dropped.tsv)"""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def main():
    moves = {r["named_form_id"]: r for r in read_tsv(ROOT / "verify/out/HVMK_moves.tsv")}
    nf = read_tsv(ROOT / "data/named_forms.tsv")
    keep, dropped, lines = [], [], {}
    for r in nf:
        m = moves.get(r["named_form_id"])
        if not m: keep.append(r); continue
        act = m["action"].strip()
        if act == "to_line":
            lid = m["line_id"].strip()
            L = lines.setdefault(lid, {"line_id": lid, "maker_id": r["maker_id"], "name": m["line_name"].strip(),
                                       "kinds": m["kinds"].strip() or r["kind_id"], "line_rank": "", "built_by_maker_id": "",
                                       "licensor_id": "", "years": "", "notes": "from " + r["named_form_id"],
                                       "sources": r["sources"], "fetch_status": r["fetch_status"]})
            if r["kind_id"] not in L["kinds"].split(";"): L["kinds"] += ";" + r["kind_id"]
            dropped.append({**r, "notes": f"to line {lid}"})
        elif act == "drop":
            dropped.append({**r, "notes": "dropped: " + m["reason"]})
        elif act == "move_kind":
            r["kind_id"] = m["new_kind_id"].strip(); keep.append(r)
        else:
            sys.exit(f"unknown action {act} for {r['named_form_id']}")
    tmp = ROOT / "verify/work/HVMK/lines_in.tsv"
    write_tsv(tmp, list(lines.values()), TABLES["lines"][1])
    if lines:
        subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "lines", str(tmp)], check=True)
    for r in keep:
        if r["named_form_id"] in moves and moves[r["named_form_id"]]["action"] == "to_line": r["line_id"] = moves[r["named_form_id"]]["line_id"]
    write_tsv(ROOT / "data/named_forms.tsv", keep, TABLES["named_forms"][1])
    write_tsv(ROOT / "verify/out/HVMK_dropped.tsv", dropped, TABLES["named_forms"][1])
    new = [r for r in read_tsv(ROOT / "verify/out/HVMK_kinds.tsv") if r["decision"].strip() == "new_kind"]
    write_tsv(ROOT / "verify/out/HVMK_new_kinds_worklist.tsv", new, list(new[0].keys()) if new else ["candidate"])
    print(f"lines {len(lines)}, named forms kept {len(keep)}, moved out {len(dropped)}, new kinds to attest {len(new)}")

if __name__ == "__main__":
    main()
