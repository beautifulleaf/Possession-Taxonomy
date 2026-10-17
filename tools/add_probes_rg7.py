"""Round 7: add the checked regression set (verify/out/RG7_checked.tsv) to data/probes.tsv,
write its intended homes to data/gold_RG7.tsv, and build the blind batch verify/in/BP7A.tsv
(every probe, shuffled; placers see only id, item, definition).

usage: add_probes_rg7.py SEED
Rows with verdict 'drop' are skipped; expected_checked / definition_checked override the
candidate values when filled. New ids are K0001... in candidate order. Re-running replaces
the K rows instead of adding them twice.
"""
import random
import sys
from common import ROOT, read_tsv, write_tsv, norm

FIELDS = ["id", "round", "item", "definition", "stratum", "type", "batch", "source_url"]


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 707
    probes = [r for r in read_tsv(ROOT / "data/probes.tsv") if not r["id"].startswith("K")]
    seen = {norm(r["item"]) for r in probes}
    new, gold, skipped = [], [], 0
    for r in read_tsv(ROOT / "verify/out/RG7_checked.tsv"):
        if (r.get("verdict") or "").strip() == "drop":
            skipped += 1
            continue
        item = r["item"].strip()
        if norm(item) in seen:
            skipped += 1
            continue
        seen.add(norm(item))
        pid = f"K{len(new) + 1:04d}"
        definition = (r.get("definition_checked") or "").strip() or r["definition"].strip()
        expected = (r.get("expected_checked") or "").strip() or r["expected"].strip()
        new.append({"id": pid, "round": "7", "item": item, "definition": definition,
                    "stratum": "regression v0.7.1", "type": "regression", "batch": "RG7",
                    "source_url": ""})
        gold.append({"id": pid, "item": item, "expected": expected, "k_ref": r.get("k_ref", "")})
    rows = probes + new
    write_tsv(ROOT / "data/probes.tsv", rows, FIELDS)
    write_tsv(ROOT / "data/gold_RG7.tsv", gold, ["id", "item", "expected", "k_ref"])
    batch = [{"id": r["id"], "item": r["item"], "definition": r["definition"]} for r in rows]
    random.Random(seed).shuffle(batch)
    write_tsv(ROOT / "verify/in/BP7A.tsv", batch, ["id", "item", "definition"])
    print(f"{len(probes)} existing + {len(new)} new probes ({skipped} skipped); batch {len(batch)} rows")


if __name__ == "__main__":
    main()
