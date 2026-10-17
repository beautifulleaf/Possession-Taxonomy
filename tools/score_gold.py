"""Check a blind round against gold sets.
usage: score_gold.py BP7 data/gold_RG2.tsv data/gold_RG7.tsv
Reads verify/out/<R>_score.tsv (from score_blind.py: id, votes, verdict) and each gold file (id, item, expected).
Writes verify/out/<R>_gold.tsv (every gold row with its votes and hit) and prints accuracy per gold set and per k_ref."""
import sys
from collections import Counter, defaultdict
from common import ROOT, read_tsv, write_tsv

R, golds = sys.argv[1], sys.argv[2:]
score = {r["id"]: r for r in read_tsv(ROOT / f"verify/out/{R}_score.tsv")}
rows = []
for g in golds:
    name = g.rsplit("/", 1)[-1].replace(".tsv", "")
    hit = n = 0
    byref = defaultdict(lambda: [0, 0])
    for r in read_tsv(ROOT / g):
        s = score.get(r["id"])
        if not s: continue
        votes = s["votes"].split()
        top = Counter(votes).most_common(1)[0][0]
        exp = r["expected"].strip()
        ok = top == exp
        n += 1; hit += ok
        ref = (r.get("k_ref") or "").strip()
        if ref: byref[ref][0] += 1; byref[ref][1] += ok
        rows.append({"gold": name, "id": r["id"], "item": r["item"], "expected": exp, "votes": s["votes"],
                     "verdict": s["verdict"], "hit": "yes" if ok else "no"})
    print(f"{name}: {hit}/{n} majority at the gold home ({100 * hit / n:.1f}%)" if n else f"{name}: no rows scored")
    miss = [k for k, v in byref.items() if v[1] < v[0]]
    if miss: print("  refs with misses:", ", ".join(f"{k} {byref[k][1]}/{byref[k][0]}" for k in sorted(miss)))
write_tsv(ROOT / f"verify/out/{R}_gold.tsv", rows, ["gold", "id", "item", "expected", "votes", "verdict", "hit"])
