"""Apply display-group changes of the DPH decision passes (R-118 a) to framework/structure/navigation/groups.tsv.
usage: apply_groups_changes.py DPH_<D> [...]   (reads verify/out/<BATCH>_groups_changes.tsv)
Actions: add (a new group), rename (name, level and parent as given), move_members (the group's member list becomes the
given list; members are also removed from any other group of the category, since every kind sits in one group). A
member that is not yet a stored kind or node (a new kind waiting for attestation) is held in
verify/out/<BATCH>_groups_pending.tsv; re-run after the attestation loads. Backup in bak/."""
import shutil, sys, time
from common import ROOT, read_tsv, write_tsv

P = ROOT / "framework/structure/navigation/groups.tsv"

def main():
    known = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv")} | {n["node_id"] for n in read_tsv(ROOT / "data/nodes.tsv")}
    rows = read_tsv(P); cols = list(rows[0].keys())
    (ROOT / "bak").mkdir(exist_ok=True); shutil.copy(P, ROOT / f"bak/groups.tsv.{time.strftime('%Y%m%d%H%M%S')}")
    by = {r["group_id"]: r for r in rows}
    for b in sys.argv[1:]:
        pending = []
        for c in read_tsv(ROOT / f"verify/out/{b}_groups_changes.tsv"):
            gid, act = c["group_id"].strip(), c["action"].strip()
            mem = [m.strip() for m in c.get("members", "").split(";") if m.strip()]
            ok = [m for m in mem if m in known]
            if len(ok) < len(mem): pending.append({**c, "members": "; ".join(m for m in mem if m not in known)})
            if act == "add" and gid not in by:
                by[gid] = {"code": c["code"], "group_id": gid, "group_name": c["group_name"], "level": c["level"],
                           "parent_group": c["parent_group"], "members": "; ".join(ok)}
            elif gid not in by:
                print(b, "unknown group", gid); continue
            elif act == "rename":
                by[gid].update(group_name=c["group_name"], level=c["level"] or by[gid]["level"],
                               parent_group=c["parent_group"] or by[gid]["parent_group"])
            elif act == "move_members":
                for g in by.values():  # one group per kind within a category
                    if g["code"] == c["code"] and g["group_id"] != gid:
                        g["members"] = "; ".join(m for m in g["members"].split("; ") if m and m not in ok)
                old = [m for m in by[gid]["members"].split("; ") if m]
                by[gid]["members"] = "; ".join(dict.fromkeys(old + ok))
            print(b, act, gid, len(ok), "members")
        write_tsv(ROOT / f"verify/out/{b}_groups_pending.tsv", pending, list(pending[0].keys()) if pending else ["group_id"])
        if pending: print(b, len(pending), "rows with members waiting for attestation")
    write_tsv(P, list(by.values()), cols)

if __name__ == "__main__":
    main()
