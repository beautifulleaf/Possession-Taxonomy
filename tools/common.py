"""Shared helpers: repo root, TSV read/write via temp file with backup."""
import csv, os, shutil, sys, time, unicodedata, re
from pathlib import Path

ROOT = Path(os.environ.get("POS_ROOT") or Path(__file__).resolve().parent.parent)
csv.field_size_limit(sys.maxsize)

def read_tsv(path):
    path = Path(path)
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def write_tsv(path, rows, fields):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        bak = ROOT / "bak"
        bak.mkdir(exist_ok=True)
        shutil.copy2(path, bak / f"{path.name}.{time.strftime('%Y%m%d-%H%M%S')}")
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        # no quote or escape character: read_tsv reads fields literally, so an escape written here would be read back
        # as data and doubled on every rewrite (R-82); tabs and line breaks, the only unsafe characters, are replaced
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", quoting=csv.QUOTE_NONE, quotechar=None,
                           escapechar=None, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: (str(r.get(k, "") or "").replace("\t", " ").replace("\r", " ").replace("\n", " ")) for k in fields})
    os.replace(tmp, path)

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    if s.endswith("es") and len(s) > 4: s = s[:-2]
    elif s.endswith("s") and len(s) > 3: s = s[:-1]
    return s
