"""Add the header row (url, fetch_status, gave) to batch fetch logs written without one (session 7: HV_D5_NK3), so
check_batch.py reads them. usage: fix_fetch_log_header.py BATCH [...]"""
import sys
from common import ROOT

for b in sys.argv[1:]:
    p = ROOT / f"verify/work/{b}/fetched.tsv"
    if not p.exists(): print(b, "no log"); continue
    t = p.read_text()
    if t.startswith("http"):
        p.write_text("url\tfetch_status\tgave\n" + t); print(b, "header added")
