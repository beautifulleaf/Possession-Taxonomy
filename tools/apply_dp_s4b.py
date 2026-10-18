"""Apply the DP_S4B decision pass (session 4 step 2(b)(c); R-84) to data/.
usage: apply_dp_s4b.py
- new kinds (verify/out/DP_S4B_kinds.tsv) and their named forms (DP_S4B_named_forms.tsv) are added through data_write;
- the kurta kind A1.1.2.05 is reworded to the generic tunic shirt (decision row "tunic");
- named forms replaced by a new kind (manteau, keffiyeh) and the kendo hakama forms (E2 under key step 17) leave
  A1: they are moved to verify/out/S4_moved_named_forms.tsv with the reason, never lost;
- re-ties (DP_S4B_reties.tsv): a new maker_kinds row on the given source (fetch_status taken from the maker's own
  source list or the batch fetch log); when old_kind_id is not "keep", the maker's row on the stand-in kind goes;
- open items: Alienware relation and parent, three Alienware named forms moved from M-dell, Chantique to AE,
  ILM to US. Kenza Boutique keeps YE until its source is fetched again (the decision rested on a page the batch
  could not refetch)."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

D = ROOT / "data"; O = ROOT / "verify/out"; W = ROOT / "verify/work/apply_dp_s4b"; W.mkdir(parents=True, exist_ok=True)

def add(table, rows):
    if not rows: return
    p = W / f"{table}.tsv"; write_tsv(p, rows, TABLES[table][1])
    r = subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "add", table, str(p)], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())
    if r.returncode: sys.exit("stopped")

def rewrite(table, rows): write_tsv(D / f"{table}.tsv", rows, TABLES[table][1])

# 1 kinds
add("kinds", read_tsv(O / "DP_S4B_kinds.tsv"))
kinds = read_tsv(D / "kinds.tsv")
dec = {d["candidate"]: d for d in read_tsv(O / "DP_S4B_decisions.tsv")}
for k in kinds:
    if k["kind_id"] == "A1.1.2.05":
        k["name"] = "Tunic shirt (kurta) [kurti]"; k["definition"] = dec["tunic"]["definition"]
        k["notes"] = (k["notes"] + "; " if k["notes"] else "") + "reworded to the generic tunic shirt (R-84)"
rewrite("kinds", kinds)
# 2 named forms out of A1, then in
nfs = read_tsv(D / "named_forms.tsv")
moved = {"NF-A1.4.2.06-R001": "manteau: named form of the abaya (NF-A1.4.2.08-D…), R-84",
         "NF-A1.6.03-083": "keffiyeh: named form of the headscarf or scarf decided in DP_S4B, R-84",
         "NF-A1.7.01-R001": "keffiyeh: duplicate under scarf, R-84"}
for i in ("021", "022", "023", "024", "025", "026", "042"):
    moved[f"NF-A1.2.2.05-{i}"] = "kendo hakama: E2 under key step 17 (R-70, R-84); load into E2 when E2 is built"
out = [dict(n, reason=moved[n["named_form_id"]]) for n in nfs if n["named_form_id"] in moved]
write_tsv(O / "S4_moved_named_forms.tsv", out, TABLES["named_forms"][1] + ["reason"])
rewrite("named_forms", [n for n in nfs if n["named_form_id"] not in moved]); print(f"named forms moved out: {len(out)}")
add("named_forms", read_tsv(O / "DP_S4B_named_forms.tsv"))
# 3 re-ties
makers = {m["maker_id"]: m for m in read_tsv(D / "makers.tsv")}
log = {r["url"].strip(): r["fetch_status"].strip() for r in read_tsv(ROOT / "verify/work/DP_S4B/fetched.tsv")} if (ROOT / "verify/work/DP_S4B/fetched.tsv").exists() else {}
mk = read_tsv(D / "maker_kinds.tsv"); new, drop, skip = [], set(), 0
for r in read_tsv(O / "DP_S4B_reties.tsv"):
    m = makers.get(r["maker_id"])
    if not m: skip += 1; continue
    st = dict(zip([u.strip() for u in m["sources"].split("|")], [f.strip() for f in m["fetch_status"].split("|")]))
    pairs = [(u.strip(), st.get(u.strip()) or log.get(u.strip(), "")) for u in (r.get("sources") or "").split("|") if u.strip()]
    pairs = [(u, f) for u, f in pairs if f in ("full", "partial")]
    if not pairs:  # fall back on the maker's own fetched sources, which carry the garment in its notes
        pairs = [(u, f) for u, f in st.items() if f in ("full", "partial")][:1]
    if not pairs: skip += 1; continue
    new.append({"offer_id": r["offer_id"], "maker_id": r["maker_id"], "kind_id": r["new_kind_id"], "notes": r["reason"][:120],
                "sources": " | ".join(u for u, _ in pairs), "fetch_status": " | ".join(f for _, f in pairs)})
    if r["old_kind_id"] != "keep": drop.add((r["maker_id"], r["old_kind_id"]))
rewrite("maker_kinds", [x for x in mk if (x["maker_id"], x["kind_id"]) not in drop])
print(f"re-ties: {len(new)} rows, {len(drop)} stand-ins removed, {skip} skipped")
add("maker_kinds", new)
# 4 open items
sec = ["https://www.sec.gov/Archives/edgar/data/0000826083/000115752306002942/a5108869ex991.txt",
       "https://www.sec.gov/Archives/edgar/data/0000826083/000115752306004905/a5144598ex99_1.txt"]
add("maker_relations", [{"relation_id": "MR-alienware-dell", "maker_id": "M-alienware", "other_id": "M-dell",
                         "relation": "subsidiary of", "scope": "company and brand", "years": "2006-",
                         "sources": " | ".join(sec), "fetch_status": "full | full"}])
ms = read_tsv(D / "makers.tsv")
for m in ms:
    if m["maker_id"] == "M-alienware": m["parent_id"] = "M-dell"; m["country"] = m["country"] or "US"
    if m["maker_id"] == "M-chantique":
        m["country"] = "AE"; m["place"] = "Dubai"
        m["notes"] = (m["notes"] + "; " if m["notes"] else "") + "founded as an atelier in Brunei; taken over in 2017 by Dubai-based Fadzil Hadin (R-84)"
    if m["maker_id"] == "M-ilm":
        m["country"] = "US"
        if "bikebd.com" not in m["sources"]:
            m["sources"] += " | https://www.bikebd.com/motorcycle/brand/ilm-helmet"; m["fetch_status"] += " | full"
rewrite("makers", ms)
nfs = read_tsv(D / "named_forms.tsv")
for n in nfs:
    if n["named_form_id"] in ("NF-D1.1.02-006", "NF-D1.1.02-007", "NF-D1.3.4.01-029") and n["maker_id"] == "M-dell": n["maker_id"] = "M-alienware"
rewrite("named_forms", nfs)
print("open items applied")
