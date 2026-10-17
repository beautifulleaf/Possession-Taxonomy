"""Write the adopted kind ids (R-58) back into the 11 rework memos as section 13 "Kind ids".
usage: kl_memo_ids.py   -> reads audit/KL_<CODE>_tree.md (latest frozen tree, or the file named in FROZEN) and
verify/out/KL_id_crosswalk.tsv; inserts or replaces section 13 before "## Sources" in framework/structure/<CODE>.md (backup to bak/)."""
import re
from common import ROOT, read_tsv
from kl_prepare import CODES, tree_kinds, write_text

FROZEN = {"A2": "KL_A2_tree_v2.md", "B8": "KL_B8_tree_v2.md", "G2": "KL_G2_tree_v2.md"}  # code -> audit file name, when a fixed tree supersedes KL_<CODE>_tree.md

def main():
    xw = {}
    for r in read_tsv(ROOT / "verify/out/KL_id_crosswalk.tsv"):
        xw.setdefault(r["code"], {})[r["new_id"]] = r["old_id"]
    for code in CODES:
        tree = ROOT / "audit" / FROZEN.get(code, f"KL_{code}_tree.md")
        ks = tree_kinds(code, tree.read_text(encoding="utf-8"))
        old = xw.get(code, {})
        lines = ["## 13. Kind ids (R-58)", "",
                 f"Adopted kind ids, tree-path scheme, from the frozen tree audit/{tree.name}. "
                 "An id is never renumbered; memo kind numbers elsewhere in this memo are memo-internal references."
                 + (" The builder ids in the third column are superseded." if old else ""), "",
                 "| Kind id | Kind |" + (" Builder id |" if old else ""),
                 "|---|---|" + ("---|" if old else "")]
        for k, v in ks.items():
            lines.append(f"| {k} | {v} |" + (f" {old.get(k, '')} |" if old else ""))
        sec = "\n".join(lines) + "\n\n"
        p = ROOT / "framework/structure" / f"{code}.md"
        s = p.read_text(encoding="utf-8")
        s = re.sub(r"## 13\. Kind ids \(R-58\)\n.*?(?=\n## |\Z)", "", s, flags=re.S).rstrip("\n") + "\n"
        if "\n## Sources" in s:
            a, b = s.split("\n## Sources", 1)
            s = a.rstrip("\n") + "\n\n" + sec + "## Sources" + b
        else:
            s = s.rstrip("\n") + "\n\n" + sec
        write_text(p, s)
        print(code, len(ks), "kind ids written")

if __name__ == "__main__":
    main()
