"""Tie makers to the new A1 kinds of DP_A1K from the garment words already recorded on their ties (R-105 f).
usage: retie_a1k.py
A GD or REG maker_kinds row's notes list the menu words its source page showed. Where those words name one of the
new kinds unambiguously, the maker gains a tie to that kind on the same source (the page showed it). Ambiguous words
are left alone: "jersey" (also a fabric), "mac", "bomber" (the flight jacket kind), "fur" alone (trim).
Bandhgala rows filed on the sherwani, whose notes do not name a sherwani, move to the blazer (hip length, R-105 b).
Writes data/maker_kinds.tsv through data_write.py (add) and common.write_tsv (move); backups in bak/."""
import re, subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

NEW = {"A1.3.1.10": r"\bco-?ords?\b|co-ordinate set", "A1.1.1.05": r"\bscrubs?\b(?! cap)", "A1.4.2.12": r"\blab coats?\b",
       "A1.4.2.10": r"\braincoats?\b|\bmackintosh", "A1.7.10": r"\bsuspenders?\b|\bbraces\b",
       "A1.4.2.11": r"\bfur coats?\b|\bshubas?\b|\bmink coats?\b"}

def main():
    mk = read_tsv(ROOT / "data/maker_kinds.tsv")
    have = {(r["maker_id"], r["kind_id"]) for r in mk}
    add, moved = {}, 0
    for r in mk:
        if not r["kind_id"].startswith("A1."): continue
        for kid, pat in NEW.items():
            if (r["maker_id"], kid) in have or (r["maker_id"], kid) in add: continue
            m = re.search(pat, r["notes"], re.I)
            if m:
                add[(r["maker_id"], kid)] = {"offer_id": f"MK-{r['maker_id'][2:]}-{kid}", "maker_id": r["maker_id"], "kind_id": kid,
                                             "notes": f"'{m.group(0)}' on the page of {r['offer_id']} (R-105)",
                                             "sources": r["sources"], "fetch_status": r["fetch_status"]}
    for r in mk:
        if r["kind_id"] == "A1.4.2.09" and re.search(r"bandh?gala|jodhpuri", r["notes"], re.I) and not re.search(r"sherwani", r["notes"], re.I):
            if (r["maker_id"], "A1.4.1.01") in have: r["kind_id"] = "DROP"
            else: r["kind_id"] = "A1.4.1.01"; r["offer_id"] = f"MK-{r['maker_id'][2:]}-A1.4.1.01"; have.add((r["maker_id"], "A1.4.1.01"))
            moved += 1
    write_tsv(ROOT / "data/maker_kinds.tsv", [r for r in mk if r["kind_id"] != "DROP"], TABLES["maker_kinds"][1])
    p = ROOT / "verify/work/retie_a1k.tsv"; write_tsv(p, list(add.values()), TABLES["maker_kinds"][1])
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", "maker_kinds", str(p)])
    from collections import Counter
    print(f"ties added {len(add)}: {dict(Counter(k for _, k in add))}; bandhgala rows moved to blazer {moved}")

if __name__ == "__main__":
    main()
