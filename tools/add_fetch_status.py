"""CV-39: add a fetch_status column to every verify/out/S2_<CODE>_sources.tsv.

Values: full, partial, nav-only, failed, excerpt (seen only in a search excerpt).
The value is inferred from the row's own text (what_it_shows / notes), so a second
column fetch_status_basis says "auto" until a person or agent confirms it.
Rows marked excerpt are also listed in verify/out/S2_<CODE>_excerpts.tsv; they are
not attestation (CONVENTIONS_v1, sources section).
Backs up each file to bak/ and writes through a temp file (common.write_tsv).
"""
import re
from common import ROOT, read_tsv, write_tsv

RULES = [
    ("failed", r"\b(fetch(ed)? failed|failed to (load|fetch)|(webfetch|fetch\w*|http|error|status|returned|got|code|refused( with)?|with)\W{0,3}(40[134]|429|5\d\d)\b|(40[134]|429|5\d\d) (error|forbidden|not found|unauthori[sz]ed)|not reachable|unreachable|blocked|bot check|timed? ?out)"),
    ("excerpt", r"\b(search (result|excerpt|snippet)s?|excerpt only|seen only in search|from (a )?search excerpt|via search)\b"),
    ("nav-only", r"\b(nav(igation)?[- ]only|shell only|page shell|only (the )?(menu|navigation|footer)|script[- ]loaded|did not render)\b"),
    ("partial", r"\b(partial(ly)?|truncated|first page only|garbled|incomplete)\b"),
]


def status(text):
    t = (text or "").lower()
    for value, pattern in RULES:
        if re.search(pattern, t):
            return value
    return "full"


def main():
    counts = {}
    for path in sorted((ROOT / "verify" / "out").glob("S2_*_sources.tsv")):
        rows = read_tsv(path)
        if not rows:
            continue
        fields = list(rows[0].keys())
        redo = "fetch_status" in fields
        if redo:
            fields = [f for f in fields if f not in ("fetch_status", "fetch_status_basis")]
        text_cols = [c for c in fields if c not in ("url", "fetch_status", "fetch_status_basis")]
        for r in rows:
            if redo and r.get("fetch_status_basis") not in ("", "auto", None):
                continue  # a checked value is never overwritten
            r["fetch_status"] = status(" ".join(r.get(c, "") for c in text_cols))
            r["fetch_status_basis"] = "auto"
        write_tsv(path, rows, fields + ["fetch_status", "fetch_status_basis"])
        exc = [r for r in rows if r["fetch_status"] == "excerpt"]
        if exc:
            write_tsv(path.with_name(path.name.replace("_sources", "_excerpts")), exc, fields + ["fetch_status"])
        code = path.name.split("_")[1]
        counts[code] = {v: sum(r["fetch_status"] == v for r in rows) for v in ("full", "partial", "nav-only", "failed", "excerpt")}
    for code, c in counts.items():
        print(code, " ".join(f"{k}={v}" for k, v in c.items()))
    print(len(counts), "files updated")


if __name__ == "__main__":
    main()
