step0: backups done, lib.py written; mks: E2 399, H1 214, J9 343 (top-level entries only, versions skipped). Starting E2 fetch batches of 10 makers; batch lists in batches_<CODE>.json, raw answers in raw/<CODE>_<n>.txt
E2 batches 0-2 fetched: no usable hits (Hi-Tec conflict: infobox parent Cherokee Inc. vs lead privately held -> unset). Record hits in res_<CODE>.tsv (mk,resolved,own,tier,own_y,note). sources.tsv to be generated at the end from batches_*.json + fetched index ranges in this file.
E2 batches 3-10 fetched (first-seen order, 3% yield, mostly missing/disambig). Switching strategy: rank makers by entry count, use better Wikipedia titles (title map in titles_<CODE>.json). Hits so far in res_E2.tsv (Wavin->Orbia held, check entry)
E2: 3 more batches (titles by count) done; hits appended. tier '-' means leave blank (owner not a V4 global group, no independence statement)
E2: 14 calls total, done fetching (yield too low; Marucci owner span ends 2026 -> conflict unset; Spitfire/Bones title mismatch skipped). Next: apply E2, then H1, J9
H1: 2 calls done (hits in res_H1.tsv; Revlon infobox MacAndrews&Forbes stale -> unset conflict; Zest split by region -> unset). More H1 plausible-title batches next, then J9
H1: 4 calls done, hits added. Skipped: Fenty Beauty (mk is Fenty Hair), Libra->Libresse mismatch, Heno de Pravia vague. Next: J9
J9: call 1 done (hits in res_J9.tsv). call 2 (>50 titles) errored, resplit
J9: 3 calls done total (+1 errored); hits added. Next: apply script apply.py, validate, sources.tsv, report
