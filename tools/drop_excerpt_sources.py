"""Drop sources a batch marked full/partial although its own fetch log says the page was not fetched (search
excerpt only, title only, blocked) (CLAUDE.md: search excerpts never attest; R-78).
usage: drop_excerpt_sources.py OUTPUT.tsv FETCH_LOG.tsv  -> rewrites OUTPUT (backup in bak/); a row's
definition_source moves to its first remaining source; rows left with no source go to OUTPUT_unattested.tsv."""
import re, sys
from pathlib import Path
from common import read_tsv, write_tsv

BAD = re.compile(r"^\s*(article )?excerpt:|\bfull\s+(article )?excerpt:|excerpt only|only (as )?search excerpt|search excerpt only|not fetched|returned only (the )?title|fetch blocked", re.I)

def main():
    out, log = Path(sys.argv[1]), Path(sys.argv[2])
    st = {}
    for r in read_tsv(log):
        u = (r.get("url") or "").strip(); what = " ".join(str(v) for k, v in r.items() if k not in ("url", "fetch_status", "status"))
        if u: st[u] = "excerpt-only" if BAD.search(what) or (r.get("fetch_status") or "").strip() in ("blocked", "failed") else (r.get("fetch_status") or "").strip()
    rows = read_tsv(out); cols = list(rows[0].keys()); keep, lost, n = [], [], 0
    for r in rows:
        pairs = list(zip([u.strip() for u in r["sources"].split("|")], [f.strip() for f in r["fetch_status"].split("|")]))
        good = [(u, f) for u, f in pairs if st.get(u, f) not in ("excerpt-only", "blocked", "failed")]
        if len(good) != len(pairs): n += 1
        r["sources"] = " | ".join(u for u, _ in good); r["fetch_status"] = " | ".join(f for _, f in good)
        if "definition_source" in r and r["definition_source"] not in [u for u, _ in good]:
            r["definition_source"] = good[0][0] if good else ""
        (keep if good else lost).append(r)
    write_tsv(out, keep, cols)
    if lost: write_tsv(out.with_name(out.stem + "_unattested.tsv"), lost, cols)
    print(f"{out.name}: {n} rows lost excerpt-only sources; {len(lost)} rows left without a source")

if __name__ == "__main__":
    main()
