"""Split a domain decision pass (DPH_<D>, R-118 a) into per-category batches DPH_<CODE> for tools/apply_dp.py:
kinds rows by their code column, moves by the category of the named form's kind. Kinds rows decided "merge" (kind_id
absorbed into other_code) go to verify/out/DPH_<CODE>_merges.tsv for tools/retire_kinds.py.
usage: split_dph.py DPH_<D> CODE [CODE ...]"""
import sys
from common import ROOT, read_tsv, write_tsv

def main():
    b, codes = sys.argv[1], sys.argv[2:]
    nf = {r["named_form_id"]: r["kind_id"] for r in read_tsv(ROOT / "data/named_forms.tsv")}
    kinds = read_tsv(ROOT / f"verify/out/{b}_kinds.tsv") if (ROOT / f"verify/out/{b}_kinds.tsv").exists() else []
    moves = read_tsv(ROOT / f"verify/out/{b}_moves.tsv") if (ROOT / f"verify/out/{b}_moves.tsv").exists() else []
    kh = list(kinds[0].keys()) if kinds else ["candidate", "code", "decision", "kind_id", "parent", "name", "definition",
                                              "other_code", "source_url", "reason"]
    mh = list(moves[0].keys()) if moves else ["named_form_id", "action", "line_id", "line_name", "kinds", "new_kind_id", "reason"]
    for c in codes:
        k = [r for r in kinds if r["code"].strip() == c]
        m = [r for r in moves if nf.get(r["named_form_id"], "").split(".")[0] == c]
        write_tsv(ROOT / f"verify/out/DPH_{c}_kinds.tsv", [r for r in k if r["decision"].strip() != "merge"], kh)
        write_tsv(ROOT / f"verify/out/DPH_{c}_moves.tsv", m, mh)
        mg = [r for r in k if r["decision"].strip() == "merge"]
        if mg: write_tsv(ROOT / f"verify/out/DPH_{c}_merges.tsv", mg, kh)
        print(f"DPH_{c}: kinds {len(k)}, moves {len(m)}, merges {len(mg)}")

if __name__ == "__main__":
    main()
