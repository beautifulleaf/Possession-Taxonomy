"""Score the kind-level placement test (session 3, step 1).
usage: score_kl.py [CODE ...]   -> reads verify/out/KLP_<CODE>_[A-Z].tsv (id, kind, alt, confidence, note)
and verify/out/KL_<CODE>_items.tsv (expected_kind). Writes verify/out/KLP_score.tsv (per item) and
verify/out/KLP_summary.tsv (per category); prints unanimity, majority, Fleiss kappa and accuracy per category.
Accuracy: a placer answer is right when it equals expected_kind. Majority accuracy counts the majority answer."""
import sys, glob, re
from collections import Counter
from common import ROOT, read_tsv, write_tsv

CODES = sys.argv[1:] or "A2 B8 C1 D4 E1 F2 F4 G2 H2 I2 J5".split()
OUT = ROOT / "verify/out"

def ans(r):
    v = (r.get("kind") or "").strip().strip("*").split()
    return v[0].rstrip(".:,;") if v else ""

def kappa(table, n):
    cats = sorted({c for t in table for c in t})
    N = len(table)
    if N == 0 or n < 2: return float("nan")
    pj = {c: sum(t[c] for t in table) / (N * n) for c in cats}
    Pbar = sum((sum(t[c] ** 2 for c in cats) - n) / (n * (n - 1)) for t in table) / N
    Pe = sum(v * v for v in pj.values())
    return (Pbar - Pe) / (1 - Pe) if Pe < 1 else 1.0

rows, summ = [], []
for code in CODES:
    files = sorted(glob.glob(str(OUT / f"KLP_{code}_[A-Z].tsv")))
    if not files: print(f"{code}: no placer files"); continue
    placers = {re.search(r"_([A-Z])\.tsv$", f).group(1): {r["id"]: r for r in read_tsv(f)} for f in files}
    items = {r["id"]: r for r in read_tsv(OUT / f"KL_{code}_items.tsv")}
    names = sorted(placers)
    missing = {n: sorted(set(items) - set(p)) for n, p in placers.items() if set(items) - set(p)}
    if missing: print(f"{code}: missing rows {missing}")
    ids = [i for i in items if all(i in placers[n] for n in names)]
    table, unan = [], 0
    right = maj_right = maj = 0
    for i in ids:
        votes = [ans(placers[n][i]) for n in names]
        c = Counter(votes); table.append(c)
        top, k = c.most_common(1)[0]
        u = k == len(votes); m = k * 2 > len(votes)
        exp = items[i]["expected_kind"].strip()
        unan += u; maj += m
        right += sum(v == exp for v in votes)
        maj_right += m and top == exp
        rows.append({"code": code, "id": i, "item": items[i]["item"], "expected": exp, "votes": " ".join(votes),
                     "verdict": "unanimous" if u else ("majority" if m else "split"),
                     "majority_right": "yes" if (m and top == exp) else "no",
                     "conf": " ".join((placers[n][i].get("confidence") or "").strip() for n in names),
                     "alts": " | ".join(f"{n}:{placers[n][i].get('alt','')}" for n in names if (placers[n][i].get("alt") or "").strip()),
                     "notes": " | ".join(f"{n}:{placers[n][i].get('note','')}" for n in names if (placers[n][i].get("note") or "").strip())})
    N = len(ids); n = len(names)
    s = {"code": code, "items": N, "placers": n, "unanimous": unan, "majority": maj,
         "kappa": f"{kappa(table, n):.3f}", "placer_accuracy": f"{100 * right / (N * n):.1f}" if N else "",
         "majority_accuracy": f"{100 * maj_right / N:.1f}" if N else ""}
    summ.append(s)
    print(f"{code}: {N} items x {n} placers  unanimous {unan} ({100*unan/N:.0f}%)  majority {maj}  kappa {s['kappa']}  "
          f"placer accuracy {s['placer_accuracy']}%  majority accuracy {s['majority_accuracy']}%")
if len(CODES) > 1 or not sys.argv[1:]:
    write_tsv(OUT / "KLP_score.tsv", rows, ["code", "id", "item", "expected", "votes", "verdict", "majority_right", "conf", "alts", "notes"])
    write_tsv(OUT / "KLP_summary.tsv", summ, ["code", "items", "placers", "unanimous", "majority", "kappa", "placer_accuracy", "majority_accuracy"])
    T = sum(s["items"] for s in summ)
    if T:
        print(f"ALL: {T} items  unanimous {sum(s['unanimous'] for s in summ)}  "
              f"majority right {sum(r['majority_right'] == 'yes' for r in rows)}")
