"""Tally crosswalk verdicts. usage: score_crosswalk.py PREFIX (e.g. CW) -> prints totals, writes verify/out/<PREFIX>_issues.tsv"""
import sys, glob
from collections import Counter
from common import ROOT, read_tsv, write_tsv
P = sys.argv[1]
nodes = {r["nid"]: r for r in read_tsv(ROOT / "data/source_nodes.tsv")}
rows = []
for f in sorted(glob.glob(str(ROOT / f"verify/out/{P}[0-9]*.tsv"))):
    rows += read_tsv(f)
c = Counter()
issues = []
for r in rows:
    v = (r.get("verdict") or "").strip()
    k = "single" if len(v) == 2 and v[0].isalpha() and v[1].isdigit() else v
    c[k] += 1
    if v in ("NOHOME", "AMBIG"):
        n = nodes.get(r["nid"], {})
        issues.append({"nid": r["nid"], "verdict": v, "codes": r.get("codes", ""), "source": n.get("source", ""), "path": n.get("path", ""), "note": r.get("note", "")})
N = len(rows)
print(f"{P}: {N} nodes  " + "  ".join(f"{k} {v} ({100*v/N:.1f}%)" for k, v in c.most_common()))
inscope = N - c["OUT"]
print(f"homed (single+SPAN+MIXED_OUT) {c['single']+c['SPAN']+c['MIXED_OUT']} of {inscope} in-scope nodes = {100*(c['single']+c['SPAN']+c['MIXED_OUT'])/inscope:.1f}%; NOHOME {100*c['NOHOME']/inscope:.1f}%, AMBIG {100*c['AMBIG']/inscope:.1f}%")
write_tsv(ROOT / f"verify/out/{P}_issues.tsv", issues, ["nid", "verdict", "codes", "source", "path", "note"])
