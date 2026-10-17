"""Apply audit fixes to probe definitions and gold homes (backup and temp-file write via common).
usage: fix_probes.py   -> applies the FIXES below to data/probes.tsv and data/gold_*.tsv; re-running is a no-op."""
from common import ROOT, read_tsv, write_tsv

DEF = {  # R-69, AU4
    "Q0165": "A structured handbag with a rounded rectangular body and top handles, styled after the bags once made to carry a bowling ball but not made to hold one.",
    "T0081": "A prepaid right to ten classes at one yoga studio, held on a card, in an app or on the studio's account.",
    "R0069": "A dishwasher built in under a kitchen worktop behind a door panel that matches the kitchen units.",
}
GOLD = {"gold_RG2.tsv": {"T0036": "J5"}}  # R-69: jarred pasta sauce is J5 by the v0.6 sentence

def main():
    p = ROOT / "data/probes.tsv"
    rows = read_tsv(p); fields = list(rows[0].keys()); n = 0
    for r in rows:
        if r["id"] in DEF and r["definition"] != DEF[r["id"]]: r["definition"] = DEF[r["id"]]; n += 1
    if n: write_tsv(p, rows, fields)
    print("probe definitions changed:", n)
    for f, fix in GOLD.items():
        gp = ROOT / "data" / f
        g = read_tsv(gp); gf = list(g[0].keys()); m = 0
        for r in g:
            if r["id"] in fix and r["expected"] != fix[r["id"]]: r["expected"] = fix[r["id"]]; m += 1
        if m: write_tsv(gp, g, gf)
        print(f, "gold changed:", m)

if __name__ == "__main__":
    main()
