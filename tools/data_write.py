"""The only writer of the stage-3 tables in data/ (schema in tools/schema.py).
usage: data_write.py init                  -> create every missing data/<table>.tsv with its header
       data_write.py add TABLE INPUT.tsv    -> validate INPUT rows and add them (an existing id is replaced)
       data_write.py check [TABLE ...]      -> re-validate stored tables, print problems
Validation (nodes exempt from the source rules): id present and unique; at least one http(s) source; one fetch_status per source; at least one source
'full' or 'partial' (a page was fetched: search excerpts never attest); foreign keys (kind_id, named_form_id,
maker_id, line_id, scheme_id, scene_id, standard_id) point to stored rows. Rejected rows go to
verify/out/data_rejects_<TABLE>.tsv with a reason; nothing partial is written."""
import sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES, FETCH_STATUS

DATA = ROOT / "data"
FK = {"kind_id": "kinds", "named_form_id": "named_forms", "maker_id": "makers", "line_id": "lines",
      "scheme_id": "schemes", "scene_id": "scenes", "standard_id": "standards", "register_id": "registers"}

NO_SOURCE = {"nodes"}  # sub-families and leaves are structure from the decided memos, not attested objects

def path(t): return DATA / f"{t}.tsv"

def load(t):
    return read_tsv(path(t)) if path(t).exists() else []

def ids(t):
    return {r[TABLES[t][0]] for r in load(t)}

def problems(table, r, known):
    key, cols = TABLES[table]
    out = []
    if not (r.get(key) or "").strip(): out.append(f"no {key}")
    if table in NO_SOURCE: src_check = False
    else: src_check = True
    src = [s.strip() for s in (r.get("sources") or "").split("|") if s.strip()]
    fs = [s.strip() for s in (r.get("fetch_status") or "").split("|") if s.strip()]
    if src_check and not src: out.append("no source")
    if any(not s.startswith(("http://", "https://")) for s in src): out.append("source not a URL")
    if len(fs) != len(src): out.append("fetch_status count differs from sources")
    if any(f not in FETCH_STATUS for f in fs): out.append("bad fetch_status")
    if src_check and not any(f in ("full", "partial") for f in fs): out.append("no fetched page")
    for col, ft in FK.items():
        if col in cols and col != key and (r.get(col) or "").strip():
            if r[col].strip() not in known.setdefault(ft, ids(ft)): out.append(f"{col} {r[col]} unknown")
    if table in ("scene_tags", "tier_entries") and (r.get("subject_type") or "").strip() == "maker":
        if r["subject_id"].strip() not in known.setdefault("makers", ids("makers")): out.append(f"maker {r['subject_id']} unknown")
    return out

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "init":
        for t, (_, cols) in TABLES.items():
            if not path(t).exists(): write_tsv(path(t), [], cols); print("created", path(t).name)
    elif cmd == "add":
        table, src = sys.argv[2], sys.argv[3]
        key, cols = TABLES[table]
        new = read_tsv(src)
        known, bad, seen = {}, [], set()
        for r in new:
            p = problems(table, r, known)
            if r.get(key) in seen: p.append("duplicate id in input")
            seen.add(r.get(key))
            if p: bad.append({**{c: r.get(c, "") for c in cols}, "reason": "; ".join(p)})
        if bad:
            write_tsv(ROOT / f"verify/out/data_rejects_{table}.tsv", bad, cols + ["reason"])
            sys.exit(f"{len(bad)} of {len(new)} rows rejected (verify/out/data_rejects_{table}.tsv); nothing written")
        rows = {r[key]: r for r in load(table)}
        for r in new: rows[r[key]] = r
        write_tsv(path(table), list(rows.values()), cols)
        print(f"{table}: {len(new)} rows added or replaced, {len(rows)} stored")
    elif cmd == "check":
        known = {}
        for t in sys.argv[2:] or TABLES:
            for r in load(t):
                p = problems(t, r, known)
                if p: print(t, r.get(TABLES[t][0]), "; ".join(p))
    else:
        sys.exit(__doc__)

if __name__ == "__main__":
    main()
