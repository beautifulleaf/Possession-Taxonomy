"""Stage-2 memo statistics: size, dagger marks, OWNER marks, conformance log, per memo.

Writes verify/out/S2_stats.tsv. Counts are text-pattern counts, not semantic counts.
"""
import re
from common import ROOT, write_tsv

def main():
    rows = []
    for p in sorted(q for q in (ROOT / "framework" / "structure").glob("[A-J]*.md") if re.fullmatch(r"[A-J]\d+", q.stem)):
        t = p.read_text(encoding="utf-8")
        verdict = ""
        rev = ROOT / "framework" / "structure" / f"_review_{p.stem[0]}.md"
        if rev.exists():
            for line in rev.read_text(encoding="utf-8").splitlines():
                if line.startswith(f"| {p.stem} "):
                    verdict = line.split("|")[2].strip().strip("*")
                    break
        rows.append({
            "code": p.stem,
            "kb": round(len(t.encode("utf-8")) / 1024),
            "dagger": t.count("†"),
            "owner_marks": len(re.findall(r"OWNER", t)),
            "conformed": "yes" if re.search(r"^## 11\b", t, re.M) else "no",
            "review_verdict": verdict,
        })
    write_tsv(ROOT / "verify" / "out" / "S2_stats.tsv", rows,
              ["code", "kb", "dagger", "owner_marks", "conformed", "review_verdict"])
    print(len(rows), "memos;", sum(r["conformed"] == "yes" for r in rows), "conformed")

if __name__ == "__main__":
    main()
