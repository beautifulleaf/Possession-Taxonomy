"""Merge duplicate maker rows (the same brand under two ids; R-86).
usage: merge_makers.py --auto            -> find pairs: same normalised name (legal and generic words dropped) and the
                                            same non-empty country; write verify/out/maker_merges.tsv and apply
       merge_makers.py PAIRS.tsv         -> apply a reviewed list (keep_id, drop_id, reason)
The kept id is the one with more rows pointing to it (ties: the shorter id). The dropped row's filled fields fill
the kept row's empty ones and its sources are added; every reference (maker_kinds, named_forms, lines, scene_tags,
maker_relations, makers.parent_id and licensor_id) moves to the kept id, and rows that become duplicates collapse.
Pairs where one country is empty, or the countries differ, are never merged automatically (homonyms are common:
R-79, R-83); they are listed in verify/out/maker_merge_candidates.tsv for review."""
import collections, re, sys
from common import ROOT, read_tsv, write_tsv, norm
from schema import TABLES

D = ROOT / "data"
STOP = r"\b(the|inc|llc|ltd|limited|co|corp|company|clothing|clothes|apparel|brand|official|&|and)\b"

def key(n):
    return re.sub(r"[^a-z0-9]", "", re.sub(STOP, " ", norm(n)))

def load(t): return read_tsv(D / f"{t}.tsv")

def refs():
    c = collections.Counter()
    for r in load("maker_kinds"): c[r["maker_id"]] += 1
    for r in load("named_forms"): c[r["maker_id"]] += 1
    for r in load("lines"): c[r["maker_id"]] += 1
    for r in load("scene_tags"): c[r["subject_id"]] += 1
    return c

def auto():
    mk = load("makers"); g = collections.defaultdict(list)
    for m in mk:
        k = key(m["name"])
        if len(k) >= 3: g[k].append(m)
    c = refs(); pairs, review = [], []
    for k, v in g.items():
        if len(v) < 2: continue
        by_c = collections.defaultdict(list)
        for m in v: by_c[m["country"]].append(m)
        for ctry, ms in by_c.items():
            if ctry and len(ms) > 1:
                ms = sorted(ms, key=lambda m: (-c[m["maker_id"]], len(m["maker_id"])))
                pairs += [{"keep_id": ms[0]["maker_id"], "drop_id": m["maker_id"], "reason": f"same name key '{k}' and country {ctry}"} for m in ms[1:]]
        if len(by_c) > 1:
            review.append({"name_key": k, "makers": " ; ".join(f"{m['maker_id']} ({m['country'] or '-'})" for m in v)})
    write_tsv(ROOT / "verify/out/maker_merge_candidates.tsv", review, ["name_key", "makers"])
    return pairs

def apply(pairs):
    to = {p["drop_id"]: p["keep_id"] for p in pairs}
    def res(x):
        seen = set()
        while x in to and x not in seen: seen.add(x); x = to[x]
        return x
    mk = {m["maker_id"]: m for m in load("makers")}; cols = TABLES["makers"][1]
    for d in list(to):
        k = res(d)
        if d not in mk or k not in mk: continue
        a, b = mk[k], mk.pop(d)
        for col in cols:
            if not (a.get(col) or "").strip() and (b.get(col) or "").strip(): a[col] = b[col]
        pa = list(zip(a["sources"].split(" | "), a["fetch_status"].split(" | ")))
        for u, f in zip(b["sources"].split(" | "), b["fetch_status"].split(" | ")):
            if u.strip() and u.strip() not in [x for x, _ in pa]: pa.append((u.strip(), f.strip()))
        a["sources"] = " | ".join(x for x, _ in pa); a["fetch_status"] = " | ".join(y for _, y in pa)
        if b.get("notes") and b["notes"] not in (a.get("notes") or ""): a["notes"] = ((a.get("notes") or "") + "; " + b["notes"]).strip("; ")
    for m in mk.values():
        for col in ("parent_id", "licensor_id"):
            if m.get(col) in to: m[col] = res(m[col])
        if m.get("parent_id") == m["maker_id"]: m["parent_id"] = ""
    write_tsv(D / "makers.tsv", list(mk.values()), cols)
    def move(table, idcol, cols_, newid=None):
        rows = load(table); out = {}
        for r in rows:
            for c in cols_:
                if r.get(c) in to: r[c] = res(r[c])
            if newid: r[idcol] = newid(r)
            out.setdefault(r[idcol], r)
        write_tsv(D / f"{table}.tsv", list(out.values()), TABLES[table][1])
        return len(rows) - len(out)
    n1 = move("maker_kinds", "offer_id", ["maker_id"], lambda r: f"MK-{r['maker_id'][2:]}-{r['kind_id']}")
    move("named_forms", "named_form_id", ["maker_id", "licensor_id"])
    move("lines", "line_id", ["maker_id", "built_by_maker_id", "licensor_id"])
    n2 = move("scene_tags", "tag_id", ["subject_id"], lambda r: f"TG-{r['scene_id'][3:]}-{r['subject_id'][2:]}" if r["subject_type"] == "maker" else r["tag_id"])
    move("maker_relations", "relation_id", ["maker_id", "other_id"])
    print(f"{len(to)} makers merged; {n1} maker_kinds and {n2} scene_tags rows collapsed")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        pairs = auto(); write_tsv(ROOT / "verify/out/maker_merges.tsv", pairs, ["keep_id", "drop_id", "reason"])
    else:
        pairs = read_tsv(sys.argv[1])
    apply(pairs)
