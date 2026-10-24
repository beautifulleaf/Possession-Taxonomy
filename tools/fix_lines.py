"""Line kind lists and line ids (R-102).
usage: fix_lines.py
1. Every line gains the kinds of the named forms filed under it (a line spans the kinds of its models, R-70): the
   models were filed under their real kind, so the line's list was short (ASUS ROG Strix, Prime, ProArt and others).
2. Explicit fixes from the D1 review (MOD_D1_*_report.md): a kind a line never covered is removed, a misspelled id is
   reissued (the old id is kept in notes and every named form follows), and kinds the reports name are added.
Writes data/lines.tsv and data/named_forms.tsv through common.write_tsv (backups in bak/), then runs data_write check."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

REMOVE = {"L-asrock-challenger": ["D1.2.3.01"]}  # Challenger is a Radeon graphics-card line, not a motherboard line
RENAME = {"L-xpg-lavente": ("L-xpg-levante", "Levante")}  # XPG's pages spell it Levante
ADD = {"L-dell-precision": ["D1.1.03"], "L-hp-spectre": ["D1.1.03"],  # all-in-one models (Precision 5720, Spectre One)
       "L-epson-endeavor": ["D1.1.02", "D1.1.04"]}  # Endeavor desktops (tower and compact)

def main():
    lines = read_tsv(ROOT / "data/lines.tsv"); nf = read_tsv(ROOT / "data/named_forms.tsv")
    kinds = {k["kind_id"] for k in read_tsv(ROOT / "data/kinds.tsv")}
    for n in nf:
        if n["line_id"] in RENAME: n["line_id"] = RENAME[n["line_id"]][0]
    by = {}
    for l in lines:
        if l["line_id"] in RENAME:
            new, name = RENAME[l["line_id"]]
            l["notes"] = (l["notes"] + "; " if l["notes"] else "") + f"id reissued from {l['line_id']} (R-102)"
            l["line_id"], l["name"] = new, name
        by[l["line_id"]] = l
    for lid, ks in REMOVE.items():
        if lid in by: by[lid]["kinds"] = ";".join(k for k in by[lid]["kinds"].split(";") if k not in ks)
    for lid, ks in ADD.items():
        if lid in by:
            cur = [k for k in by[lid]["kinds"].split(";") if k]
            by[lid]["kinds"] = ";".join(cur + [k for k in ks if k not in cur and k in kinds])
    added = 0
    for n in nf:
        l = by.get(n["line_id"])
        if l and n["kind_id"] in kinds and n["kind_id"] not in l["kinds"].split(";"):
            l["kinds"] = ";".join([k for k in l["kinds"].split(";") if k] + [n["kind_id"]]); added += 1
    write_tsv(ROOT / "data/lines.tsv", list(by.values()), TABLES["lines"][1])
    write_tsv(ROOT / "data/named_forms.tsv", nf, TABLES["named_forms"][1])
    print(f"lines: {added} kinds added from their named forms; {len(REMOVE)} removals, {len(RENAME)} renames, {len(ADD)} explicit additions")
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "check", "lines", "named_forms"])

if __name__ == "__main__":
    main()
