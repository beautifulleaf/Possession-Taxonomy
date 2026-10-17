"""Score a blind placement round.
usage: score_blind.py BP1  -> reads verify/out/BP1_A.tsv, BP1_B.tsv, BP1_C.tsv (id, category, alt, confidence, note)
Writes verify/out/BP1_score.tsv (per item) and prints unanimity, majority, Fleiss kappa, per-category agreement."""
import sys, glob
from collections import Counter, defaultdict
from common import ROOT, read_tsv, write_tsv

R = sys.argv[1]
files = sorted(glob.glob(str(ROOT / f"verify/out/{R}_[A-Z].tsv")))
placers = {f.rsplit("_", 1)[1].split(".")[0]: {r["id"]: r for r in read_tsv(f)} for f in files}
probes = {r["id"]: r for r in read_tsv(ROOT / "data/probes.tsv")}
ids = sorted(set.intersection(*[set(p) for p in placers.values()]))
names = sorted(placers)
def cat(r): return (r.get("category") or "").strip().split()[0].rstrip(".:") if r.get("category") else ""
rows, unan, maj = [], 0, 0
cats = set()
table = []
for i in ids:
    votes = [cat(placers[n][i]) for n in names]
    cats.update(votes)
    c = Counter(votes)
    top, k = c.most_common(1)[0]
    u = k == len(votes); m = k * 2 > len(votes)
    unan += u; maj += m
    table.append(c)
    rows.append({"id": i, "item": probes.get(i, {}).get("item", ""), "type": probes.get(i, {}).get("type", ""),
                 "votes": " ".join(votes), "verdict": "unanimous" if u else ("majority" if m else "split"),
                 "alts": " | ".join(f"{n}:{placers[n][i].get('alt','')}" for n in names if placers[n][i].get('alt')),
                 "notes": " | ".join(f"{n}:{placers[n][i].get('note','')}" for n in names if placers[n][i].get('note'))})
# Fleiss kappa
N, n = len(table), len(names)
cl = sorted(cats)
pj = {c: sum(t[c] for t in table) / (N * n) for c in cl}
Pi = [(sum(t[c] ** 2 for c in cl) - n) / (n * (n - 1)) for t in table]
Pbar = sum(Pi) / N; Pe = sum(v * v for v in pj.values())
kappa = (Pbar - Pe) / (1 - Pe) if Pe < 1 else 1.0
write_tsv(ROOT / f"verify/out/{R}_score.tsv", rows, ["id", "item", "type", "votes", "verdict", "alts", "notes"])
print(f"{R}: {N} items, {n} placers ({','.join(names)})")
print(f"unanimous {unan} ({100*unan/N:.1f}%)  majority {maj} ({100*maj/N:.1f}%)  split {N-maj}  Fleiss kappa {kappa:.3f}")
by = defaultdict(lambda: [0, 0])
for t in table:
    top = t.most_common(1)[0][0]
    by[top][0] += 1; by[top][1] += t.most_common(1)[0][1] == n
print("per category (majority home: items, unanimous%):")
for c in sorted(by): print(f"  {c:8s} {by[c][0]:4d}  {100*by[c][1]/by[c][0]:5.1f}%")
nonunan = Counter()
for t in table:
    if len(t) > 1:
        ks = sorted(t); nonunan[" / ".join(ks)] += 1
print("most frequent disagreement pairs:")
for k, v in nonunan.most_common(15): print(f"  {v:3d}  {k}")
