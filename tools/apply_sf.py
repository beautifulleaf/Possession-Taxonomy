"""Apply a storefront check (R-105 e, R-113 c): BATCH_decisions.tsv rows (maker_id, decision, evidence, sources,
fetch_status) set supply_role "retail own-label" or "retailer (multi-brand)" on stored makers through data_write
(makers merge: the decision's source is added, other fields kept). 'unclear' rows are left as they are.
usage: apply_sf.py BATCH"""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

b = sys.argv[1]
mk = {m["maker_id"]: m for m in read_tsv(ROOT / "data/makers.tsv")}
role = {"own-label": "retail own-label", "storefront": "retailer (multi-brand)"}
out = []
for r in read_tsv(ROOT / f"verify/out/{b}_decisions.tsv"):
    d = r["decision"].strip(); m = mk.get(r["maker_id"])
    if d not in role or not m or not r.get("sources", "").strip(): continue
    old = [x.strip() for x in m["supply_role"].split(";") if x.strip() and x.strip() not in role.values()]
    out.append({"maker_id": m["maker_id"], "supply_role": "; ".join(old + [role[d]]),
                "notes": f"{b}: {d} ({r.get('evidence', '')})", "sources": r["sources"], "fetch_status": r["fetch_status"]})
p = ROOT / f"verify/work/{b}/apply_makers.tsv"; write_tsv(p, out, TABLES["makers"][1])
print(subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "makers", str(p)], capture_output=True, text=True).stdout.strip())
