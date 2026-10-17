"""Merge the stage-3 source census (verify/out/S3C_*.tsv) into data/source_catalogues.tsv.

One row per (category code, url); later census files add codes to a url already seen
in another category only as a separate row. Prints sources per category, so thin
categories show up before harvest planning.
"""
import glob
from collections import Counter
from common import ROOT, read_tsv, write_tsv

FIELDS = ["code", "source", "url", "type", "lists", "approx_entries", "organised_by",
          "region_language", "access", "fit", "notes", "census_batch"]


def main():
    rows, seen = [], set()
    for path in sorted(glob.glob(str(ROOT / "verify/out/S3C_*.tsv"))):
        batch = path.rsplit("/", 1)[1].rsplit(".", 1)[0]
        for r in read_tsv(path):
            code = (r.get("code") or "").strip()
            url = (r.get("url") or "").strip()
            if not code or not url or (code, url) in seen:
                continue
            seen.add((code, url))
            r["census_batch"] = batch
            rows.append(r)
    rows.sort(key=lambda r: (r["code"][0], int("".join(c for c in r["code"][1:] if c.isdigit()) or 0), r["census_batch"]))
    write_tsv(ROOT / "data/source_catalogues.tsv", rows, FIELDS)
    per = Counter(r["code"] for r in rows)
    print(len(rows), "sources in", len(per), "categories")
    print(" ".join(f"{c}:{n}" for c, n in sorted(per.items(), key=lambda x: (x[0][0], int(x[0][1:]) if x[0][1:].isdigit() else 0))))


if __name__ == "__main__":
    main()
