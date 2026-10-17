"""Regional coverage of a category's brands (owner rule, BRIEF 2026-10-17; R-75).
usage: coverage.py [CODE]   (default A1) -> prints brands linked to the category per region and per country,
and writes verify/out/coverage_<CODE>.tsv (region, country, brands). A maker counts for the category when a
named form or maker_kinds row sits under one of its kinds, a line spans one of its kinds, or (A1 only) it has a
scene tag. Makers without a country are counted as "unknown country" so the gap stays visible."""
import sys
from collections import Counter, defaultdict
from common import ROOT, read_tsv, write_tsv
from regions import REGIONS, REGION_OF, country

def load(t):
    p = ROOT / "data" / f"{t}.tsv"
    return read_tsv(p) if p.exists() else []

def main():
    code = sys.argv[1] if len(sys.argv) > 1 else "A1"
    kinds = {k["kind_id"] for k in load("kinds") if k["code"] == code}
    linked = set()
    linked |= {n["maker_id"] for n in load("named_forms") if n["kind_id"] in kinds and n["maker_id"]}
    linked |= {l["maker_id"] for l in load("lines") if any(k in kinds for k in l["kinds"].split(";"))}
    linked |= {m["maker_id"] for m in load("maker_kinds") if m["kind_id"] in kinds or m["kind_id"] == code}
    if code == "A1":
        linked |= {t["subject_id"] for t in load("scene_tags") if t["subject_type"] == "maker"}
    makers = {m["maker_id"]: m for m in load("makers")}
    by_c = Counter(); by_r = Counter(); unknown = 0
    for m in linked:
        c = country(makers.get(m, {}).get("country", ""))
        if not c: unknown += 1; continue
        by_c[c] += 1; by_r[REGION_OF.get(c, "other")] += 1
    total = len(linked)
    print(f"{code}: {total} brands linked; {unknown} without a country ({100 * unknown / max(total, 1):.0f} %)")
    for r in list(REGIONS) + ["other"]:
        cs = sorted(((c, n) for c, n in by_c.items() if REGION_OF.get(c, "other") == r), key=lambda x: -x[1])
        print(f"  {r:28s} {by_r[r]:5d}   " + ", ".join(f"{c} {n}" for c, n in cs[:12]))
    rows = [{"region": REGION_OF.get(c, "other"), "country": c, "brands": n} for c, n in by_c.most_common()]
    rows.append({"region": "unknown", "country": "", "brands": unknown})
    write_tsv(ROOT / f"verify/out/coverage_{code}.tsv", rows, ["region", "country", "brands"])

if __name__ == "__main__":
    main()
