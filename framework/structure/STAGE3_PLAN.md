# Stage 3 plan: harvest order and method

Written in session 3 after the A1 and D1 pilot (decision R-70). Order from STAGE2_SUMMARY.md §6 ("Data-phase order"), adjusted for what has happened since: the 11 rework categories are now decided and tested at kind level, so they no longer wait; there is no separate sourcing pass (owner ruling), so every † claim is attested inside its category's harvest.

## Order

| Wave | Categories | Why here |
|---|---|---|
| 0 (done) | A1 Clothing, D1 Computers & Components | owner's pilot pair; 209/209 kinds attested |
| 1 | B10, C6, I1, D5, J4, J2, B3, J3 | §6 step 3: ready or nearly ready, fewest † |
| 2 | A2, B8, C1, D4, E1, F2, F4, G2, H2, I2, J5 | decided and tested at kind level (R-60 to R-67); trees already carry R-58 ids and are loaded in data/nodes.tsv |
| 3 | A3, A4, A5, B1, B2, B4, B5, B6, B7, B9 | the other minor-fix categories, domain A and B first |
| 4 | C2, C3, C4, C5, C7, C8, D2, D3, E2, E3, E4 | heavy † counts (E4 98, C8 80, E2 74) or very large trees (C3 up to 1,400 kinds) |
| 5 | F1, F3, F5, F6, G1, H1, H3, I3, J1, J6, J7 | remaining; F3 and F6 lean on registries and catalogues that need a census check first |

Within a wave, categories run in parallel up to the agent limit (20 at once).

## Method per category (from the pilot)

1. **Tree.** If the category has no R-58 ids yet, a Sonnet builder writes verify/out/TREE_<CODE>.md from the memo (verify/in/TREE_COMMON.txt). tools/load_tree.py loads sub-families and leaves into data/nodes.tsv and writes the kind worklist verify/out/HV_<CODE>_worklist.tsv. For the 11 tested categories, load the frozen tree in audit/ (done).
2. **Census check.** The pilot showed that the anchor catalogues in data/source_catalogues.tsv are mostly maker directories. Before harvesting, add for each category at least one kind-level source (a retailer category tree or a database with types) where the census has none.
3. **Harvest.** One Sonnet batch per group of sub-families of about 20 to 40 kinds (verify/in/HV_COMMON.txt): attest every kind on a fetched page, record named forms and makers from the fetched pages without a cap, log every fetch with its status. Rows enter data/ only through tools/data_write.py (validation: id, a fetched source, fetch_status per source, foreign keys).
4. **Decision pass.** One Opus pass per category (as verify/in/HVMK.prompt.txt): decide "missing kind?" candidates against the memo (new kind with the next free R-58 id, named form, attribute, covered, other category); move maker tiers and series that span models or kinds to data/lines.tsv; drop attributes, aliases and other-category rows (tools/apply_hvmk.py, generalised per category).
5. **New kinds.** One Sonnet batch attests the new kinds before they enter data/kinds.tsv (as HV_NK).
6. **Depth passes.** Then repeated harvest passes per sub-family for named forms, variants, tier entries, scenes and registers until the attested sources run out (owner: depth and breadth, no caps). The pilot's open depth work: chip, card and laptop models in D1 (the lines are in, the models are not); subculture and scene makers in A1 (Lolita, streetwear, amekaji, Japanese denim) with C8 scene tags.

## Lessons written into the method
- Put the lines rule (a tier or series spanning several models or kinds is a lines row) into the harvest prompt itself; the pilot recorded 270 lines as named forms.
- Harvesters must reuse maker ids already in data/makers.tsv (the pilot produced M-dell and M-alienware for one maker) and record parent makers as maker-relations rows.
- Attributes named on shop pages (craft, cut, neckline, fastening, material) are never named forms (C2(b)); the decision pass dropped 55 such A1 rows.
- A "missing kind?" seen only on a list or navigation page needs a fetched page showing the type before it enters (16 of the 37 new pilot kinds).
