"""Reference distribution of a category's brands by country (owner principle, BRIEF 2026-10-17; R-78).
usage: coverage_ref.py [CODE]   (default A1)
Reads verify/out/coverage_proxies_<CODE>.tsv (country, proxy, value, unit, year, source, fetch_status, notes: raw
figures, each on a fetched page) and writes verify/out/coverage_reference_<CODE>.tsv (country, expected_share,
basis, sources, fetch_status). Method (R-78): each proxy family is turned into country shares over the countries it
covers; a country's expected share is the geometric mean of its shares in the families that cover it (robust to one
family's outliers, e.g. trademark-volume inflation at one office), and the results are renormalised to sum to 1.
Families: market (P1), trademarks (P2, else P2b), wikipedia (P3, else P3b), firms (P4). Only full or partial rows."""
import math, sys
from collections import defaultdict
from common import ROOT, read_tsv, write_tsv
from regions import country

FAMILIES = {"market": ["P1"], "trademarks": ["P2", "P2b"], "wikipedia": ["P3", "P3b"], "firms": ["P4"]}
MIN_COUNTRIES = 15  # a proxy covering fewer countries is too thin to set shares on its own

def main():
    code = sys.argv[1] if len(sys.argv) > 1 else "A1"
    rows = [r for r in read_tsv(ROOT / f"verify/out/coverage_proxies_{code}.tsv")
            if (r.get("fetch_status") or "").split("|")[0].strip() in ("full", "partial")]
    raw = defaultdict(dict); src = defaultdict(lambda: defaultdict(set))
    for r in rows:
        c = country(r["country"])
        try: v = float(str(r["value"]).replace(",", ""))
        except ValueError: continue
        if not c or v <= 0: continue
        p = r["proxy"].strip()
        raw[p][c] = max(v, raw[p].get(c, 0))  # duplicates: keep the larger figure of one proxy
        src[c][p].add((r["source"].strip(), (r.get("fetch_status") or "").strip()))
    shares = {}  # family -> country -> share
    for fam, proxies in FAMILIES.items():
        for p in proxies:  # first proxy of the family that is broad enough
            if len(raw.get(p, {})) >= MIN_COUNTRIES:
                tot = sum(raw[p].values())
                shares[fam] = {c: v / tot for c, v in raw[p].items()}
                shares[fam + "_proxy"] = p
                break
    fams = [f for f in FAMILIES if f in shares]
    countries = set().union(*(shares[f].keys() for f in fams)) if fams else set()
    gm = {}
    for c in countries:
        vals = [shares[f][c] for f in fams if c in shares[f]]
        gm[c] = math.exp(sum(math.log(v) for v in vals) / len(vals))
    tot = sum(gm.values()) or 1
    out = []
    for c, v in sorted(gm.items(), key=lambda x: -x[1]):
        basis = "; ".join(f"{f} {shares[f + '_proxy']} {100 * shares[f][c]:.2f}%" for f in fams if c in shares[f])
        ss = [(u, s) for f in fams if c in shares[f] for u, s in sorted(src[c][shares[f + "_proxy"]])]
        out.append({"country": c, "expected_share": f"{v / tot:.5f}", "basis": basis,
                    "sources": " | ".join(u for u, _ in ss), "fetch_status": " | ".join(s for _, s in ss)})
    write_tsv(ROOT / f"verify/out/coverage_reference_{code}.tsv", out,
              ["country", "expected_share", "basis", "sources", "fetch_status"])
    print(f"{code}: reference for {len(out)} countries from families " + ", ".join(f"{f}={shares[f + '_proxy']}({len(shares[f])})" for f in fams))
    for r in out[:25]: print(f"  {r['country']}  {100 * float(r['expected_share']):5.2f}%   {r['basis']}")

if __name__ == "__main__":
    main()
