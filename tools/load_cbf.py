"""Load a country backfill batch CBF_n (R-101): only countries of makers already in the ledger.
usage: load_cbf.py BATCH [BATCH ...]
Runs check_batch.py --fix (sources must be in the batch's fetch log), keeps rows whose maker_id is in data/makers.tsv
and whose country is filled, and adds them through data_write.py (makers are merged: country, place and founded are
filled in, sources appended). No ties are created."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

for b in sys.argv[1:]:
    print(f"== {b}")
    r = subprocess.run([sys.executable, str(ROOT / "tools/check_batch.py"), b, "-", "--fix"], capture_output=True, text=True)
    print("\n".join(l for l in r.stdout.splitlines() if "rows with" in l or "NO FETCH LOG" in l))
    if "NO FETCH LOG" in r.stdout: print("  not loaded"); continue
    f = ROOT / f"verify/out/{b}_makers.tsv"
    if not f.exists(): print("  no output"); continue
    known = {m["maker_id"]: m for m in read_tsv(ROOT / "data/makers.tsv")}
    rows = [x for x in read_tsv(f) if x["maker_id"] in known and x.get("country", "").strip() and x.get("sources", "").strip()]
    for x in rows:
        x["country"] = x["country"].strip().upper()
        for c in ("maker_class", "supply_role", "parent_id", "licensor_id", "authority_id", "school_ids", "extension"):
            x[c] = ""  # a backfill never changes what the maker is
    tmp = ROOT / f"verify/work/load_{b}_makers.tsv"
    write_tsv(tmp, rows, TABLES["makers"][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "makers", str(tmp)], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()); print(f"  {len(rows)} countries filled")
