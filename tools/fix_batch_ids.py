"""Fix a batch's maker ids and countries after check_batch.py review, before loading (R-101 b).
usage: fix_batch_ids.py BATCH [--rename OLD=NEW ...] [--keep-country ID ...]
--rename gives a same-name maker of another trade its own id in every verify/out/<BATCH>_*.tsv (maker_id, parent_id,
offer_id); --keep-country blanks the batch's country for makers whose stored country stands (the writer then keeps it)."""
import sys
from common import ROOT, read_tsv, write_tsv

def main():
    b = sys.argv[1]; ren, keep, mode = {}, set(), None
    for a in sys.argv[2:]:
        if a.startswith("--"): mode = a; continue
        if mode == "--rename": o, n = a.split("="); ren[o] = n
        elif mode == "--keep-country": keep.add(a)
    for f in sorted((ROOT / "verify/out").glob(f"{b}_*.tsv")):
        rows = read_tsv(f)
        if not rows: continue
        n = 0
        for r in rows:
            for c in ("maker_id", "parent_id", "subject_id"):
                if r.get(c) in ren: r[c] = ren[r[c]]; n += 1
            if "offer_id" in r and r.get("maker_id") and r.get("kind_id"): r["offer_id"] = f"MK-{r['maker_id'][2:]}-{r['kind_id']}"
            if f.stem.endswith("makers") and r.get("maker_id") in keep and r.get("country"): r["country"] = ""; n += 1
        if n: write_tsv(f, rows, list(rows[0].keys())); print(f"{f.name}: {n} fields changed")

if __name__ == "__main__":
    main()
