"""Undo a same-name merge after a load (R-106): a batch reused the id of a maker of another trade.
usage: split_homonym.py OLD_ID NEW_ID BATCH
Creates NEW_ID from the batch's maker row; strips that row's sources and notes back out of OLD_ID; moves the batch's
maker_kinds, named forms and lines rows of OLD_ID (matched by offer/named-form/line id in the batch outputs) to NEW_ID.
Writes through common.write_tsv (backups in bak/), then runs data_write check."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def main():
    old, new, b = sys.argv[1:4]
    out = ROOT / "verify/out"
    brow = next(r for r in read_tsv(out / f"{b}_makers.tsv") if r["maker_id"] in (old, new))
    mk = read_tsv(ROOT / "data/makers.tsv")
    bsrc = [u.strip() for u in brow["sources"].split("|") if u.strip()]
    for m in mk:
        if m["maker_id"] == old:
            pairs = list(zip([u.strip() for u in m["sources"].split("|")], [f.strip() for f in m["fetch_status"].split("|")]))
            keep = [(u, f) for u, f in pairs if u not in bsrc] or pairs[:1]
            m["sources"] = " | ".join(u for u, _ in keep); m["fetch_status"] = " | ".join(f for _, f in keep)
            if brow["notes"] and brow["notes"] in m["notes"]:
                m["notes"] = m["notes"].replace("; " + brow["notes"], "").replace(brow["notes"], "").strip("; ")
    if not any(m["maker_id"] == new for m in mk): mk.append({**brow, "maker_id": new})
    write_tsv(ROOT / "data/makers.tsv", mk, TABLES["makers"][1])
    for t, key in (("maker_kinds", "offer_id"), ("named_forms", "named_form_id"), ("lines", "line_id")):
        f = out / f"{b}_{t}.tsv"
        if not f.exists(): continue
        ids = {r[key] for r in read_tsv(f) if r.get("maker_id") == old}
        rows = read_tsv(ROOT / f"data/{t}.tsv"); n = 0
        for r in rows:
            if r[key] in ids and r["maker_id"] == old:
                r["maker_id"] = new; n += 1
                if t == "maker_kinds": r["offer_id"] = f"MK-{new[2:]}-{r['kind_id']}"
        if n: write_tsv(ROOT / f"data/{t}.tsv", rows, TABLES[t][1]); print(f"{t}: {n} rows moved to {new}")
    for f in out.glob(f"{b}_*.tsv"):  # the batch output follows, so a reload cannot merge them again
        rows = read_tsv(f)
        if rows and "maker_id" in rows[0] and any(r["maker_id"] == old for r in rows):
            for r in rows:
                if r["maker_id"] == old:
                    r["maker_id"] = new
                    if "offer_id" in r: r["offer_id"] = f"MK-{new[2:]}-{r['kind_id']}"
            write_tsv(f, rows, list(rows[0].keys()))
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "check", "makers", "maker_kinds", "named_forms", "lines"])

if __name__ == "__main__":
    main()
