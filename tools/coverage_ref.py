"""Reference distribution of a category's brands by country (owner principle, BRIEF 2026-10-17; R-80).
usage: coverage_ref.py [CODE]   (default A1)
Reads verify/out/coverage_proxies_<CODE>.tsv (country, proxy, value, unit, year, source, fetch_status, notes: raw
figures, each on a fetched page) and writes verify/out/coverage_reference_<CODE>.tsv (country, expected_share,
basis, sources, fetch_status). Method (R-80):
- market: the category's market size. P1 (one consistent market-research family) where it covers the country;
  else P1b (other market figures) scaled by the median P1/P1b ratio of the countries both cover; else modelled as
  GDP (proxy G) times the median P1/GDP ratio, so every country has a market estimate. Export or production
  figures are not a market (they favour producer countries and re-export hubs): P1b rows whose unit or notes say
  export are set aside and GDP fills those countries instead (R-98). Production in tonnes (P1/P1b rows whose unit
  says tonne) is its own family, kept when it covers 15 countries (R-99).
- trademarks: P2 when it covers at least MIN_COUNTRIES countries, else P2b (all-class filing activity by origin).
- wikipedia: P3 + P3b page counts (brand and company categories by country).
- A family covering under half of world GDP (a regional source such as an EU-only count) is left out: its shares
  are taken over a regional total and are not comparable.
Each family gives country shares; a country's expected share is the geometric mean of its shares in the families
that cover it (robust to one family's outliers, e.g. trademark-volume inflation at some offices), renormalised to
sum to 1. Only full or partial rows count."""
import math, statistics, sys
from collections import defaultdict
from common import ROOT, read_tsv, write_tsv
from regions import country

MIN_COUNTRIES = 15

def main():
    code = sys.argv[1] if len(sys.argv) > 1 else "A1"
    rows = [r for r in read_tsv(ROOT / f"verify/out/coverage_proxies_{code}.tsv")
            if (r.get("fetch_status") or "").split("|")[0].strip() in ("full", "partial")]
    raw = defaultdict(lambda: defaultdict(list)); src = defaultdict(lambda: defaultdict(set))
    for r in rows:
        c = country(r["country"])
        try: v = float(str(r["value"]).replace(",", ""))
        except ValueError: continue
        if not c or v <= 0: continue
        p = r["proxy"].strip()
        txt = (r.get("unit", "") + " " + r.get("notes", "")).lower()
        if p in ("P1", "P1b") and "export" in txt: continue  # R-98: trade is not a market
        if p in ("P1", "P1b") and "tonne" in txt: p = "P5"  # R-99: physical production, its own family
        raw[p][c].append(v); src[c][p].add((r["source"].strip(), (r.get("fetch_status") or "").strip()))
    val = {p: {c: statistics.median(vs) for c, vs in d.items()} for p, d in raw.items()}  # one figure per country
    gdp = val.get("G", {}); world = sum(gdp.values()) or 1
    fam, used = {}, defaultdict(dict)  # family -> country -> value; used[family][country] = proxies behind it
    # market
    p1, p1b = val.get("P1", {}), val.get("P1b", {})
    k_b = statistics.median(p1[c] / p1b[c] for c in p1 if c in p1b) if any(c in p1b for c in p1) else None
    k_g = statistics.median(p1[c] / gdp[c] for c in p1 if c in gdp) if any(c in gdp for c in p1) else None
    m = {}
    for c in set(p1) | set(p1b) | set(gdp):
        if c in p1: m[c] = p1[c]; used["market"][c] = ["P1"]
        elif c in p1b and k_b: m[c] = p1b[c] * k_b; used["market"][c] = ["P1b"]
        elif c in gdp and k_g: m[c] = gdp[c] * k_g; used["market"][c] = ["G"]
    if m: fam["market"] = m
    # trademarks
    for p in ("P2", "P2b"):
        if len(val.get(p, {})) >= MIN_COUNTRIES:
            fam["trademarks"] = dict(val[p]); used["trademarks"] = {c: [p] for c in val[p]}; break
    # wikipedia
    w = defaultdict(float)
    for p in ("P3", "P3b"):
        for c, v in val.get(p, {}).items(): w[c] += v; used["wikipedia"].setdefault(c, []).append(p)
    if len(w) >= MIN_COUNTRIES: fam["wikipedia"] = dict(w)
    # production (R-99: for categories whose makers are the producers, e.g. growers and fisheries in J2, J4)
    if len(val.get("P5", {})) >= MIN_COUNTRIES:
        fam["production"] = dict(val["P5"]); used["production"] = {c: ["P5"] for c in val["P5"]}
    # firms (kept only if global)
    if val.get("P4"): fam["firms"] = dict(val["P4"]); used["firms"] = {c: ["P4"] for c in val["P4"]}
    for f in list(fam):
        cover = sum(gdp.get(c, 0) for c in fam[f]) / world
        if cover < 0.5: print(f"family {f} left out: covers {100 * cover:.0f} % of world GDP"); del fam[f]
    shares = {f: {c: v / sum(d.values()) for c, v in d.items()} for f, d in fam.items()}
    countries = set().union(*shares.values()) if shares else set()
    gm = {c: math.exp(statistics.fmean(math.log(shares[f][c]) for f in shares if c in shares[f])) for c in countries}
    tot = sum(gm.values()) or 1
    out = []
    for c, v in sorted(gm.items(), key=lambda x: -x[1]):
        basis = "; ".join(f"{f} {'+'.join(used[f][c])} {100 * shares[f][c]:.2f}%" for f in shares if c in shares[f])
        ss = sorted({x for f in shares if c in shares[f] for p in used[f][c] for x in src[c][p]})
        out.append({"country": c, "expected_share": f"{v / tot:.5f}", "basis": basis,
                    "sources": " | ".join(u for u, _ in ss), "fetch_status": " | ".join(s for _, s in ss)})
    write_tsv(ROOT / f"verify/out/coverage_reference_{code}.tsv", out, ["country", "expected_share", "basis", "sources", "fetch_status"])
    print(f"{code}: reference for {len(out)} countries; families " + ", ".join(f"{f}({len(d)})" for f, d in shares.items())
          + (f"; P1/P1b {k_b:.2f}" if k_b else "") + (f"; P1/GDP {k_g:.5f}" if k_g else ""))
    for r in out[:30]: print(f"  {r['country']}  {100 * float(r['expected_share']):5.2f}%   {r['basis']}")

if __name__ == "__main__":
    main()
