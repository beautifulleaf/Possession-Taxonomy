"""Apply a stage-3 decision pass for one category (R-70, R-101): named forms that are lines move to data/lines.tsv;
non-named-forms are dropped; misfiled named forms move kind; new kinds whose source page is in the category's harvest
fetch logs (logged full or partial) enter data/kinds.tsv, the rest go to a worklist for attestation.
usage: apply_dp.py BATCH CODE
Reads verify/out/<BATCH>_moves.tsv and <BATCH>_kinds.tsv (columns as verify/in/DPW1_COMMON.txt); dropped rows are
kept in verify/out/<BATCH>_dropped.tsv; backups and validation through tools/data_write.py."""
import glob, subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def add(table, rows, tag):
    if not rows: return
    p = ROOT / f"verify/work/{tag}/{table}_in.tsv"; p.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(p, rows, TABLES[table][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", table, str(p)], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())

def main():
    b, code = sys.argv[1], sys.argv[2]
    mp = ROOT / f"verify/out/{b}_moves.tsv"
    moves = {r["named_form_id"]: r for r in read_tsv(mp)} if mp.exists() else {}
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
    lines = {k: v for k, v in lines.items() if v["maker_id"]}  # a line needs its maker (C1)
    add("lines", list(lines.values()), b)
    write_tsv(ROOT / "data/named_forms.tsv", keep, TABLES["named_forms"][1])
    write_tsv(ROOT / f"verify/out/{b}_dropped.tsv", dropped, TABLES["named_forms"][1])
    log = {}
    for f in glob.glob(str(ROOT / f"verify/work/*_{code}_*/fetched.tsv")):
        for r in read_tsv(f):
            u = (r.get("url") or "").strip(); s = (r.get("fetch_status") or r.get("status") or "").strip().lower()
            if u and s in ("full", "partial"): log[u] = s
    kp = ROOT / f"verify/out/{b}_kinds.tsv"
    new = [r for r in read_tsv(kp) if r["decision"].strip() == "new_kind"] if kp.exists() else []
    known = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv")}
    ready, wait = [], []
    for r in new:
        u = r["source_url"].strip(); kid = r["kind_id"].strip()
        if kid in known: continue
        if u in log:
            p = r["parent"].strip(); parts = kid.split(".")
            ready.append({"kind_id": kid, "code": code, "sub_family": ".".join(parts[:2]), "leaf": ".".join(parts[:3]) if len(parts) == 4 else "",
                          "name": r["name"].strip(), "native_name": "", "definition": r["definition"].strip(), "sort": parts[-1].lstrip("0") or "0",
                          "status": "attested", "memo_ref": b, "tested": "top-level", "notes": r["reason"].strip()[:120],
                          "sources": u, "fetch_status": log[u]})
        else: wait.append(r)
    add("kinds", ready, b)
    write_tsv(ROOT / f"verify/out/{b}_new_kinds_worklist.tsv", wait, list(wait[0].keys()) if wait else ["candidate"])
    print(f"{b}: lines {len(lines)}, named forms kept {len(keep)}, moved out {len(dropped)}, new kinds added {len(ready)}, to attest {len(wait)}")

if __name__ == "__main__":
    main()
