"""Regional coverage of a category's brands (owner rule, BRIEF 2026-10-17; R-75).
usage: coverage.py [CODE]   (default A1) -> prints brands linked to the category per region and per country,
and writes verify/out/coverage_<CODE>.tsv (region, country, brands). A maker counts for the category when a
named form or maker_kinds row sits under one of its kinds, a line spans one of its kinds, or (A1 only) it has a
scene tag. Makers without a country are counted as "unknown country" so the gap stays visible.
With verify/out/coverage_reference_<CODE>.tsv (tools/coverage_ref.py, R-78) it also prints, per region and country,
the actual share, the expected share and their ratio, and flags each country expected to hold at least 0.5 % of
brands whose ratio is below 0.5 (owner principle: coverage proportional to the world's distribution)."""
import math, sys
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
    # brands only: makers recorded only as manufacturers in a producers' directory are attested makers but not brands,
    # and the reference counts brands (R-91)
    linked = {m for m in linked if not any(s in makers.get(m, {}).get("supply_role", "") for s in ("manufacturer", "retailer (multi-brand)"))}  # storefronts too (R-105)
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
    ref_p = ROOT / f"verify/out/coverage_reference_{code}.tsv"
    ref = {r["country"]: float(r["expected_share"]) for r in read_tsv(ref_p)} if ref_p.exists() else {}
    known = sum(by_c.values()) or 1
    share = lambda n: n / known
    ratio = lambda a, e: (a / e) if e else None
    rows = []
    for c in sorted(set(by_c) | set(ref), key=lambda c: (-by_c[c], c)):
        a, e = share(by_c[c]), ref.get(c, 0.0); q = ratio(a, e)
        flag = "LOW" if (e >= 0.005 and q is not None and q < 0.5) else ""
        rows.append({"region": REGION_OF.get(c, "other"), "country": c, "brands": by_c[c], "share": f"{a:.4f}",
                     "expected": f"{e:.4f}" if ref else "", "ratio": f"{q:.2f}" if q is not None else "", "flag": flag,
                     "needed_for_half": max(0, math.ceil((0.5 * e * known - by_c[c]) / (1 - 0.5 * e))) if flag else ""})
    rows.append({"region": "unknown", "country": "", "brands": unknown})
    write_tsv(ROOT / f"verify/out/coverage_{code}.tsv", rows,
              ["region", "country", "brands", "share", "expected", "ratio", "flag", "needed_for_half"])
    if ref:
        print(f"\nAgainst the reference ({len(ref)} countries; actual share of the {known} brands with a country):")
        print(f"  {'region':28s} {'actual':>7s} {'expected':>8s} {'ratio':>6s}")
        for r in list(REGIONS) + ["other"]:
            e = sum(v for c, v in ref.items() if REGION_OF.get(c, "other") == r); a = share(by_r[r]); q = ratio(a, e)
            print(f"  {r:28s} {100 * a:6.1f}% {100 * e:7.1f}% {q:6.2f}" if q is not None else f"  {r:28s} {100 * a:6.1f}%        -")
        flagged = [x for x in rows if x.get("flag")]
        print(f"\n  {len(flagged)} countries flagged (expected >= 0.5 %, ratio < 0.5):")
        for x in sorted(flagged, key=lambda x: float(x["ratio"])):
            print(f"    {x['country']}  brands {x['brands']:>5}  actual {100 * float(x['share']):5.2f}%  expected {100 * float(x['expected']):5.2f}%  ratio {x['ratio']}  (+{x['needed_for_half']} brands to reach 0.5)")

if __name__ == "__main__":
    main()
