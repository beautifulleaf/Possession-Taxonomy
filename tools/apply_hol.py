"""Apply holistic-organisation proposals (R-115 c): merge verify/out/HOL_DP_<n>_proposals.tsv, _groups.tsv and
_markers.tsv into framework/structure/navigation/{proposals,groups,markers}.tsv, one category's rows replacing its
earlier ones. Groups are display structure: they regroup kinds for navigation and never change kind ids (R-58).
Checks that every member of a built category's groups is a known node or kind and lists kinds left out.
usage: apply_hol.py HOL_DP_<n> [...]"""
import sys
from common import ROOT, read_tsv, write_tsv

NAV = ROOT / "framework/structure/navigation"

def merge(name, new, key="code"):
    p = NAV / f"{name}.tsv"
    old = read_tsv(p) if p.exists() else []
    codes = {r[key] for r in new}
    rows = [r for r in old if r[key] not in codes] + new
    cols = list(dict.fromkeys([c for r in (new or old) for c in r.keys()]))
    write_tsv(p, rows, cols); return len(new)

def main():
    kinds = {k["kind_id"]: k for k in read_tsv(ROOT / "data/kinds.tsv")}
    nodes = {n["node_id"] for n in read_tsv(ROOT / "data/nodes.tsv")}
    for b in sys.argv[1:]:
        out = ROOT / "verify/out"
        for name in ("proposals", "groups", "markers"):
            f = out / f"{b}_{name}.tsv"
            if f.exists() and read_tsv(f): print(f"{b} {name}: {merge(name, read_tsv(f))} rows")
        g = out / f"{b}_groups.tsv"
        if not g.exists(): continue
        rows = read_tsv(g)
        for code in sorted({r["code"] for r in rows}):
            mem = set()
            for r in rows:
                if r["code"] != code: continue
                for m in [x.strip() for x in r["members"].split(";") if x.strip()]:
                    if m in kinds: mem.add(m)
                    elif m in nodes: mem |= {k for k, v in kinds.items() if v["sub_family"] == m or v["leaf"] == m}
                    else: print(f"  {code}: unknown member {m}")
            left = [k for k, v in kinds.items() if v["code"] == code and k not in mem]
            print(f"  {code}: {len(mem)} kinds grouped, {len(left)} left out {left[:8]}")

if __name__ == "__main__":
    main()
