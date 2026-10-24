"""Apply the A1 kinds review DP_A1K (R-105).
usage: apply_dp_a1k.py
1. Kind wording (ids unchanged, R-58): tailored trousers widen to every plain trouser, overcoat to every coat below the
   hip that no other coat kind covers, work pants name scrub trousers, shell jacket names softshell.
2. Storefronts: makers judged storefront in verify/out/DP_A1K_storefronts.tsv get supply_role "retailer (multi-brand)"
   (kept in the ledger, left out of the brand count by tools/coverage.py, as manufacturers are, R-91); own-label
   judgements set "retail own-label" where the role is empty.
3. New kinds go to verify/in/HV_A1_NK_worklist.tsv for attestation (the decision pass cites no fetch log).
Writes through common.write_tsv (backups in bak/) and runs data_write check."""
import subprocess, sys
from common import ROOT, read_tsv, write_tsv
from schema import TABLES

WORDING = {
    "A1.2.2.07": ("Trousers (tailored or casual)", "trousers with a fly and waistband sold apart from a suit, tailored or casual, "
                  "of any leg shape (wide-leg, straight, pleated), that no more specific trouser kind covers."),
    "A1.4.2.06": (None, "cloth, wool or leather coat ending below the hip, tailored or plain, that no other coat kind covers "
                  "(worn over a suit or jacket, or on its own)."),
    "A1.2.2.03": (None, "hard-wearing trousers made for work in cotton twill, duck or similar fabric, scrub trousers included."),
    "A1.4.1.12": (None, "waterproof or windproof jacket with no insulation, for rain and wind, softshell included."),
}

def main():
    kinds = read_tsv(ROOT / "data/kinds.tsv")
    for k in kinds:
        if k["kind_id"] in WORDING:
            name, d = WORDING[k["kind_id"]]
            if name: k["name"] = name
            k["definition"] = d
            if "R-105" not in k["notes"]: k["notes"] = (k["notes"] + "; " if k["notes"] else "") + "wording widened (DP_A1K, R-105)"
    write_tsv(ROOT / "data/kinds.tsv", kinds, TABLES["kinds"][1])
    sf = {r["maker_id"]: r["decision"] for r in read_tsv(ROOT / "verify/out/DP_A1K_storefronts.tsv")}
    mk = read_tsv(ROOT / "data/makers.tsv"); n_sf = n_ol = 0
    for m in mk:
        d = sf.get(m["maker_id"])
        if d == "storefront" and m["supply_role"] != "retailer (multi-brand)": m["supply_role"] = "retailer (multi-brand)"; n_sf += 1
        elif d == "own-label" and not m["supply_role"]: m["supply_role"] = "retail own-label"; n_ol += 1
    write_tsv(ROOT / "data/makers.tsv", mk, TABLES["makers"][1])
    new = [r for r in read_tsv(ROOT / "verify/out/DP_A1K_kinds.tsv") if r["decision"] == "new_kind"]
    write_tsv(ROOT / "verify/in/HV_A1_NK_worklist.tsv", new, list(new[0].keys()))
    print(f"wording {len(WORDING)}; storefronts {n_sf}; own-label roles set {n_ol}; new kinds to attest {len(new)}")
    subprocess.run([sys.executable, str(ROOT / "tools/data_write.py"), "check", "kinds", "makers"])

if __name__ == "__main__":
    main()
