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
subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "check", "named_forms", "lines"])
