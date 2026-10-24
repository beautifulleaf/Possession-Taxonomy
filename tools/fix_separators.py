"""Normalise source separators in stored tables (R-110): some batches joined several sources and their statuses with
"; " instead of " | ", which leaves one unreadable source string. usage: fix_separators.py [TABLE ...]"""
import re, subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

for t in sys.argv[1:] or ["named_forms", "lines", "maker_kinds", "makers", "kinds"]:
    rows = read_tsv(ROOT / f"data/{t}.tsv"); n = 0
    for r in rows:
        s = re.sub(r"\s*[;,]\s+(?=https?://)", " | ", r.get("sources", ""))
        if s != r.get("sources", ""):
            r["sources"] = s; r["fetch_status"] = re.sub(r"\s*[;,]\s*", " | ", r["fetch_status"]); n += 1
    if n: write_tsv(ROOT / f"data/{t}.tsv", rows, TABLES[t][1])
    print(f"{t}: {n} rows normalised")
# a row with several sources but one status: take each source's status from the batch fetch logs; a source no log
# holds as full or partial is dropped (the row keeps at least one fetched source or is reported)
import glob
log = {}
for f in glob.glob(str(ROOT / "verify/work/*/fetched.tsv")):
    for r in read_tsv(f):
        u = (r.get("url") or "").strip(); v = (r.get("fetch_status") or r.get("status") or "").strip().lower()
        if u and v in ("full", "partial"): log[u.rstrip("/")] = v
for t in ("named_forms", "lines"):
    rows = read_tsv(ROOT / f"data/{t}.tsv"); n = 0
    for r in rows:
        us = [u.strip() for u in r["sources"].split("|") if u.strip()]; fs = [x.strip() for x in r["fetch_status"].split("|") if x.strip()]
        if len(us) > 1 and len(fs) != len(us):
            keep = [(u, log[u.rstrip("/")]) for u in us if u.rstrip("/") in log]
            if keep: r["sources"] = " | ".join(u for u, _ in keep); r["fetch_status"] = " | ".join(v for _, v in keep); n += 1
            else: print(f"{t} {r[TABLES[t][0]]}: no source found in any fetch log")
    if n: write_tsv(ROOT / f"data/{t}.tsv", rows, TABLES[t][1])
    print(f"{t}: {n} statuses rebuilt from fetch logs")
subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "check", "named_forms", "lines"])
