"""Move makers that only issue objects to the issuer ledger (CV-4, R-44, R-124 a).
usage: makers_to_issuers.py CODE MAKER_IDS.txt
MAKER_IDS.txt: one maker_id per line, with an optional tab and issuer type (else the type is read from maker_class).
A maker moves only when every row pointing to it (named forms, maker_kinds, lines) lies in CODE's kinds; others are
listed and kept. Each moved maker becomes an issuer row I-<slug> with its sources; its named forms lose the maker
(maker_bound no) and their notes begin "issuer I-<slug>;"; its maker_kinds ties and maker row are removed. The moved
rows are kept in verify/out/ISS_<CODE>_moved_makers.tsv."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

TYPE = {"transport operator or association": "transit authority", "network operator": "telecom operator",
        "retail own-label": "retailer", "bank": "bank"}
D = ROOT / "data"

def main():
    code, lst = sys.argv[1], sys.argv[2]
    want = {}
    for line in open(lst, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if p[0].strip(): want[p[0].strip()] = p[1].strip() if len(p) > 1 else ""
    kinds = {k["kind_id"]: k["code"] for k in read_tsv(D / "kinds.tsv")}
    nf, mk, ln, mks = (read_tsv(D / f"{t}.tsv") for t in ("named_forms", "maker_kinds", "lines", "makers"))
    outside = {r["maker_id"] for r in nf if kinds.get(r["kind_id"]) != code} | {
        r["maker_id"] for r in mk if kinds.get(r["kind_id"], r["kind_id"]) != code} | {r["maker_id"] for r in ln}
    makers = {m["maker_id"]: m for m in mks}
    move = {m for m in want if m in makers and m not in outside}
    kept = sorted(set(want) - move)
    iss = {r["issuer_id"]: r for r in read_tsv(D / "issuers.tsv")}
    to = {}
    for m in sorted(move):
        r = makers[m]; iid = "I-" + m[2:]
        to[m] = iid
        typ = want[m] or TYPE.get(r["maker_class"], "other")
        iss[iid] = {"issuer_id": iid, "name": r["name"], "country": r["country"], "type": typ,
                    "years": "-".join(x for x in (r["founded"], r["ended"]) if x),
                    "sources": r["sources"], "fetch_status": r["fetch_status"]}
    n = 0
    for r in nf:
        if r["maker_id"] in to:
            r["notes"] = f"issuer {to[r['maker_id']]}; " + r["notes"] if r["notes"] else f"issuer {to[r['maker_id']]}"
            r["maker_id"] = ""; r["maker_bound"] = "no"; n += 1
    write_tsv(D / "issuers.tsv", list(iss.values()), TABLES["issuers"][1])
    write_tsv(D / "named_forms.tsv", nf, TABLES["named_forms"][1])
    write_tsv(D / "maker_kinds.tsv", [r for r in mk if r["maker_id"] not in to], TABLES["maker_kinds"][1])
    write_tsv(ROOT / f"verify/out/ISS_{code}_moved_makers.tsv", [makers[m] for m in sorted(move)], TABLES["makers"][1])
    write_tsv(D / "makers.tsv", [m for m in mks if m["maker_id"] not in to], TABLES["makers"][1])
    print(f"{code}: {len(move)} makers moved to issuers, {n} named forms re-pointed; kept (used outside {code} or unknown): {len(kept)}")
    for k in kept: print("  kept", k)

if __name__ == "__main__":
    main()
