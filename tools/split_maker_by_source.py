"""Split a conflated maker by source URL (R-113): ties whose source contains MATCH move to NEW_ID.
usage: split_maker_by_source.py OLD_ID NEW_ID MATCH LEDGER_SOURCE "NAME" "NATIVE" "PLACE" "NOTES"
NEW_ID gets OLD_ID's other fields, with name, native name, place and notes given and LEDGER_SOURCE (a source OLD_ID
already holds) moved over; OLD_ID loses that source and its note part. maker_kinds rows with several sources split:
the sources containing MATCH go to a NEW_ID row. Writes through common.write_tsv (backups in bak/)."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

def pairs(r): return list(zip([u.strip() for u in r["sources"].split("|")], [f.strip() for f in r["fetch_status"].split("|")]))
def put(r, ps): r["sources"] = " | ".join(u for u, _ in ps); r["fetch_status"] = " | ".join(f for _, f in ps)

def main():
    old, new, match, lsrc, name, native, place, notes = sys.argv[1:9]
    mk = read_tsv(ROOT / "data/makers.tsv")
    o = next(m for m in mk if m["maker_id"] == old)
    assert new not in {m["maker_id"] for m in mk}, f"{new} exists"
    n = dict(o); n.update(maker_id=new, name=name, native_name=native, place=place, notes=notes)
    ps = pairs(o); put(n, [p for p in ps if p[0] == lsrc]); put(o, [p for p in ps if p[0] != lsrc])
    assert n["sources"], "ledger source not held by OLD_ID"
    o["notes"] = "; ".join(x for x in o["notes"].split("; ") if x.strip() and not x.strip().endswith(place))
    mk.append(n); write_tsv(ROOT / "data/makers.tsv", mk, TABLES["makers"][1])
    ties = read_tsv(ROOT / "data/maker_kinds.tsv"); out = []; moved = 0
    for t in ties:
        if t["maker_id"] != old: out.append(t); continue
        ps = pairs(t); mine = [p for p in ps if match in p[0]]; rest = [p for p in ps if match not in p[0]]
        if mine:
            nt = dict(t); nt.update(maker_id=new, offer_id=f"MK-{new[2:]}-{t['kind_id']}"); put(nt, mine); out.append(nt); moved += 1
        if rest: put(t, rest); out.append(t)
    write_tsv(ROOT / "data/maker_kinds.tsv", out, TABLES["maker_kinds"][1])
    print(f"{new}: created, {moved} ties moved")

if __name__ == "__main__":
    main()
