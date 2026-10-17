"""Concatenate TSV files with the same header into one (backup and temp-file write via common).
usage: merge_tsv.py OUT IN1 IN2 ..."""
import sys
from common import read_tsv, write_tsv

rows, fields = [], None
for p in sys.argv[2:]:
    rs = read_tsv(p)
    if rs and fields is None: fields = list(rs[0].keys())
    rows += rs
write_tsv(sys.argv[1], rows, fields)
print(len(rows), "rows ->", sys.argv[1])
