"""Load a grocery origin-and-grade batch (OG_*, VR_*, GR_*; R-112): designations, varieties and grading scales.
usage: load_og.py BATCH [BATCH ...]
Steps: tools/check_batch.py --fix (a source missing from the batch's fetch log is dropped, R-101 b) and
drop_excerpt_sources.py; then per table: unknown kind ids are cleared (kept in notes as "kind? <id>"), repeated ids in
the batch keep their first row, and rows go through tools/data_write.py. A designation that binds one kind becomes a
non-maker named form of that kind (JC1) unless the kind already has a named form of that name (NF-<kind>-O<nnn>).
Rows whose notes say "missing kind?" are listed in verify/out/<BATCH>_missing_kinds.tsv for the decision pass."""
import re, subprocess, sys
from common import ROOT, read_tsv, write_tsv, norm
from schema import TABLES

SCHEME_WORDS = r"\b(pdo|pgi|tsg|dop|igp|aop|aoc|doc|do|gi|ig|uk|protected designation of origin|protected geographical indication)\b"

def run(*a):
    r = subprocess.run([sys.executable, *map(str, a)], capture_output=True, text=True, cwd=ROOT / "tools")
    out = (r.stdout + r.stderr).strip()
    if out: print(out)
    return r.returncode == 0

def base(s): return re.sub(r"\s+", " ", re.sub(SCHEME_WORDS, " ", norm(s))).strip()

def main():
    kinds = {k["kind_id"]: k for k in read_tsv(ROOT / "data/kinds.tsv")}
    for b in sys.argv[1:]:
        print(f"== {b}")
        log = ROOT / f"verify/work/{b}/fetched.tsv"
        if not log.exists(): print(f"{b}: no fetch log, not loaded"); continue
        run(ROOT / "tools/check_batch.py", b, b.split("_")[1], "--fix")
        missing = []
        for table in ("designations", "varieties", "grading_scales"):
            f = ROOT / f"verify/out/{b}_{table}.tsv"
            if not f.exists(): continue
            run(ROOT / "tools/drop_excerpt_sources.py", f, log)
            rows = read_tsv(f)
            if not rows: continue
            key, cols = TABLES[table]
            seen, clean = set(), []
            for r in rows:
                r = {c: (r.get(c) or "").strip() for c in cols}
                if not r[key] or r[key] in seen: continue
                seen.add(r[key])
                if r.get("kind_id") and r["kind_id"] not in kinds:
                    r["notes"] = (r["notes"] + "; " if r["notes"] else "") + f"kind? {r['kind_id']}"; r["kind_id"] = ""
                if "kinds_served" in r and r["kinds_served"]:
                    ks = [k.strip() for k in re.split(r"[|;,]", r["kinds_served"]) if k.strip()]
                    r["kinds_served"] = " | ".join(k for k in ks if k in kinds)
                if table == "designations":
                    if r["kind_id"] and not r["binds"]: r["binds"] = "kind"
                    if r["binds"] == "kind" and not r["kind_id"] and r["kinds_served"].count("|") == 0 and r["kinds_served"]:
                        r["kind_id"] = r["kinds_served"]
                if "missing kind" in r.get("notes", "").lower(): missing.append({"batch": b, "table": table, "id": r[key],
                                                                                   "name": r["name"], "notes": r["notes"], "source": r["sources"].split(" | ")[0]})
                clean.append(r)
            tmp = ROOT / f"verify/work/{b}/load_{table}.tsv"; write_tsv(tmp, clean, cols)
            run(ROOT / "tools/data_write.py", "add", table, tmp)
            if table == "designations": named_forms(clean, kinds, b)
        if missing:
            write_tsv(ROOT / f"verify/out/{b}_missing_kinds.tsv", missing, list(missing[0].keys()))
            print(f"{b}: {len(missing)} 'missing kind?' rows listed")

def named_forms(rows, kinds, b):
    nf = read_tsv(ROOT / "data/named_forms.tsv")
    have = {}
    for r in nf: have.setdefault(r["kind_id"], set()).add(base(r["name"]))
    used = {r["named_form_id"] for r in nf}
    by_ds = {r["notes"].split("designation ", 1)[1].split(";")[0].strip(): r for r in nf if r["notes"].startswith("designation ")}
    new = []
    for d in rows:
        if d["binds"] != "kind" or not d["kind_id"]: continue
        old = by_ds.get(d["designation_id"])
        if old:  # a re-run renamed or re-sourced the designation: its named form follows (same id)
            nm = f"{d['name']} {d['scheme']}".strip()
            if (old["name"], old["kind_id"], old["sources"]) != (nm, d["kind_id"], d["sources"]):
                new.append({**old, "name": nm, "kind_id": d["kind_id"], "sources": d["sources"], "fetch_status": d["fetch_status"]})
            continue
        if base(d["name"]) in have.get(d["kind_id"], set()): continue
        n = 1
        while f"NF-{d['kind_id']}-O{n:03d}" in used: n += 1
        i = f"NF-{d['kind_id']}-O{n:03d}"; used.add(i); have.setdefault(d["kind_id"], set()).add(base(d["name"]))
        year = (re.search(r"(1[89]|20)\d\d", d["date"]) or [""])[0]
        new.append({"named_form_id": i, "kind_id": d["kind_id"], "name": f"{d['name']} {d['scheme']}".strip(),
                    "maker_bound": "no", "first_year": year, "region": d["country"],
                    "notes": f"designation {d['designation_id']}", "sources": d["sources"], "fetch_status": d["fetch_status"]})
    if new:
        tmp = ROOT / f"verify/work/{b}/load_named_forms_og.tsv"; write_tsv(tmp, new, TABLES["named_forms"][1])
        run(ROOT / "tools/data_write.py", "add", "named_forms", tmp)

if __name__ == "__main__":
    main()
