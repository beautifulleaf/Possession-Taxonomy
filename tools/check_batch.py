"""Pre-load check of a web batch (R-101): guessed URLs and same-name makers of other trades.
usage: check_batch.py BATCH [CODE] [--fix]
1. Every source in the batch's outputs (verify/out/<BATCH>_*.tsv) must be a page the batch fetched: a URL missing from
   verify/work/<BATCH>/fetched.tsv (or logged failed/blocked) is treated as guessed or unfetched. The check lists them;
   with --fix it removes them from the rows (rows left without a source go to <file>_unattested.tsv; backups in bak/).
   A batch without a fetch log is reported and nothing is fixed: it must not be loaded as is.
2. A maker row whose id is already in data/makers.tsv but tied only to other categories, or whose country differs from
   the stored one, is listed for review: a same-name maker of another trade must get its own id M-<name>-<trade>
   (MKH_COMMON). Review the list and fix ids by hand in the batch output (never in data/) before loading.
CODE defaults to the second part of the batch name (MKH_C6_NAO -> C6)."""
import sys
from collections import defaultdict
from common import ROOT, read_tsv, write_tsv

def canon(u):
    u = u.strip()
    for p in ("https://", "http://"):
        if u.startswith(p): u = u[len(p):]
    if u.startswith("www."): u = u[4:]
    return u.rstrip("/").split("#")[0]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fix = "--fix" in sys.argv
    b = args[0]; code = args[1] if len(args) > 1 else b.split("_")[1]
    log = ROOT / f"verify/work/{b}/fetched.tsv"
    files = sorted(f for f in (ROOT / "verify/out").glob(f"{b}_*.tsv")
                   if not f.stem.endswith(("_unattested", "_nosource", "_dropped", "_skipped")))
    ok_urls = set()
    if log.exists():
        for r in read_tsv(log):
            u = (r.get("url") or "").strip(); s = (r.get("fetch_status") or r.get("status") or "").strip().lower()
            if u and s not in ("failed", "blocked", "excerpt-only", "nav-only", "error"): ok_urls.add(canon(u))
    else:
        print(f"{b}: NO FETCH LOG at {log.relative_to(ROOT)}; sources cannot be checked")
    total_bad = 0
    for f in files:
        rows = read_tsv(f)
        if not rows or "sources" not in rows[0]: continue
        bad_rows, keep, lost = 0, [], []
        for r in rows:
            us = [u.strip() for u in r["sources"].split("|") if u.strip()]
            fs = [x.strip() for x in r.get("fetch_status", "").split("|")]
            fs += [""] * (len(us) - len(fs))
            good = [(u, s) for u, s in zip(us, fs) if canon(u) in ok_urls]
            if len(good) != len(us):
                bad_rows += 1
                if bad_rows <= 5: print(f"  {f.name}: not in log: {[u for u in us if canon(u) not in ok_urls][:3]}")
            if fix and log.exists():
                r["sources"] = " | ".join(u for u, _ in good); r["fetch_status"] = " | ".join(s or "full" for _, s in good)
                (keep if good else lost).append(r)
        total_bad += bad_rows
        print(f"{f.name}: {len(rows)} rows, {bad_rows} with a source not in the fetch log")
        if fix and log.exists() and bad_rows:
            cols = list(rows[0].keys())
            write_tsv(f, keep, cols)
            if lost:
                if f.stem.endswith("makers"):  # a maker that lost every source also loses its ties in this batch
                    print(f"    {len(lost)} makers left without a source set aside")
                write_tsv(f.with_name(f.stem + "_unattested.tsv"), lost, cols)
    # same-name makers of other trades
    mk = {m["maker_id"]: m for m in read_tsv(ROOT / "data/makers.tsv")}
    code_of = {k["kind_id"]: k["code"] for k in read_tsv(ROOT / "data/kinds.tsv")}
    ties = defaultdict(set)
    for t in read_tsv(ROOT / "data/maker_kinds.tsv"): ties[t["maker_id"]].add(code_of.get(t["kind_id"], t["kind_id"]))
    for n in read_tsv(ROOT / "data/named_forms.tsv"):
        if n["maker_id"]: ties[n["maker_id"]].add(code_of.get(n["kind_id"], "?"))
    mf = ROOT / f"verify/out/{b}_makers.tsv"
    if mf.exists():
        flag = []
        for r in read_tsv(mf):
            old = mk.get(r["maker_id"])
            if not old: continue
            other = ties[r["maker_id"]] - {code}
            diff_c = old["country"] and r.get("country") and old["country"] != r["country"]
            if (other and code not in ties[r["maker_id"]]) or diff_c:
                flag.append((r["maker_id"], "/".join(sorted(other)), old["country"], r.get("country", ""),
                             old["notes"][:60], r.get("notes", "")[:60]))
        print(f"\n{len(flag)} reused maker ids to review (id, stored categories, stored country, batch country, stored notes | batch notes):")
        for x in flag: print("  " + " ; ".join(x))
    print(f"\n{b}: {total_bad} rows with unlogged sources" + (" (fixed)" if fix and log.exists() and total_bad else ""))

if __name__ == "__main__":
    main()
