"""Append a DPH decision pass's memo notes to each category memo (R-118 a) as section 14, replacing an earlier
section 14 of the same pass. usage: append_memo_notes.py BATCH [BATCH ...]
Reads verify/out/<BATCH>_memo_notes.md ("## <CODE>" sections); backups of changed memos in bak/."""
import re, shutil, sys, time
from common import ROOT

HEAD = "## 14. Structure decisions for the build (DPH, session 7)"

def main():
    stamp = time.strftime("%Y%m%d%H%M%S")
    for b in sys.argv[1:]:
        text = (ROOT / f"verify/out/{b}_memo_notes.md").read_text()
        parts = re.split(r"^## +([A-J]\d{1,2})\b.*$", text, flags=re.M)
        for code, body in zip(parts[1::2], parts[2::2]):
            memo = ROOT / f"framework/structure/{code}.md"
            if not memo.exists(): print("no memo", code); continue
            old = memo.read_text()
            i = old.find(HEAD)
            if i >= 0: old = old[:i].rstrip() + "\n"
            (ROOT / "bak").mkdir(exist_ok=True)
            shutil.copy(memo, ROOT / f"bak/{code}.md.{stamp}")
            memo.write_text(old.rstrip() + f"\n\n{HEAD}\nFrom verify/out/{b}_report.md; binds the build like memo text (R-118 a).\n\n{body.strip()}\n")
            print(b, code, "section 14 written")

if __name__ == "__main__":
    main()
