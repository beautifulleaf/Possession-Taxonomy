"""Merge twin line rows (the same range under two ids; R-124 b).
usage: merge_lines.py PAIRS.tsv     (columns keep_id, drop_id, reason)
The kept row takes the union of both kind lists and sources and fills its empty fields from the dropped row; named
forms pointing to the dropped id move to the kept id. Dropped rows are kept in verify/out/line_merges_dropped.tsv."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

D = ROOT / "data"

def main():
    pairs = read_tsv(sys.argv[1])
    lines = {l["line_id"]: l for l in read_tsv(D / "lines.tsv")}
    cols = TABLES["lines"][1]; to, gone = {}, []
    for p in pairs:
        k, d = p["keep_id"], p["drop_id"]
        if k not in lines or d not in lines: print("skipped", k, d); continue
        a, b = lines[k], lines.pop(d); to[d] = k; gone.append(b)
        for c in cols:
            if not (a.get(c) or "").strip() and (b.get(c) or "").strip(): a[c] = b[c]
        ks = [x for x in a["kinds"].split(";") if x.strip()]
        a["kinds"] = ";".join(ks + [x for x in b["kinds"].split(";") if x.strip() and x not in ks])
        pa = list(zip(a["sources"].split(" | "), a["fetch_status"].split(" | ")))
        for u, f in zip(b["sources"].split(" | "), b["fetch_status"].split(" | ")):
            if u.strip() and u.strip() not in [x for x, _ in pa]: pa.append((u.strip(), f.strip()))
        a["sources"] = " | ".join(x for x, _ in pa); a["fetch_status"] = " | ".join(y for _, y in pa)
    nf = read_tsv(D / "named_forms.tsv"); n = 0
    for r in nf:
        if r["line_id"] in to: r["line_id"] = to[r["line_id"]]; n += 1
    write_tsv(D / "lines.tsv", list(lines.values()), cols)
    write_tsv(D / "named_forms.tsv", nf, TABLES["named_forms"][1])
    write_tsv(ROOT / "verify/out/line_merges_dropped.tsv", gone, cols)
    print(f"{len(to)} lines merged, {n} named forms re-pointed")

if __name__ == "__main__":
    main()
