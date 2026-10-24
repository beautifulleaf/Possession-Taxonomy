"""Add the header row (url, fetch_status, gave) to batch fetch logs written without one (session 7: HV_D5_NK3), and
move notes written after a URL ("<url> (Parallel)", "<url> (offset 100000)", HV_H1_1) into the gave column, so
check_batch.py matches them. usage: fix_fetch_log_header.py BATCH [...]"""
import sys
from common import ROOT

for b in sys.argv[1:]:
    p = ROOT / f"verify/work/{b}/fetched.tsv"
    if not p.exists(): print(b, "no log"); continue
    t = p.read_text()
    if t.startswith("http"):
        t = "url\tfetch_status\tgave\n" + t; print(b, "header added")
    out, n = [], 0
    for ln in t.split("\n"):
        f = ln.split("\t")
        if f and f[0].startswith("http") and " (" in f[0]:
            u, note = f[0].split(" (", 1); f[0] = u.strip(); n += 1
            if len(f) > 2: f[2] = f"({note} {f[2]}".strip()
            else: f += [""] * (3 - len(f)); f[2] = "(" + note
        out.append("\t".join(f))
    p.write_text("\n".join(out))
    if n: print(b, n, "URL notes moved to gave")
