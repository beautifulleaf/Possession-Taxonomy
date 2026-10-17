# Possession taxonomy

A taxonomy of the things people own and keep: every generic type of object a person can have, from clothing and tools to vehicles, property, media, plants and digital goods. Stand-alone domain, built with the method of the Culinary and Pleasure taxonomies.

## Plan
- **Stage 1 – top-level categories.** A list of top-level categories, each with one membership test and precedence sentences for blurred edges, built outside-in from existing classifications and tested by blind placement of real possessions. Nothing below the categories is fixed in stage 1.
- **Stage 2 – one structure study per category.** A research memo per category on how the domain itself is organised (axes, depth, tiers, makers, scenes, order), from which the owner approves that category's structure. Pilot on Clothing and PC components.
- **Stage 3 – build.** Harvest kinds under the approved structures, attest, audit, publish.

## State
Stage 1 done: 53 top-level categories; the live key is `framework/CATEGORIES_v0_7_3.md` (round 7 on v0.7.2: 99.6 % unanimous on 1,423 items, κ 0.997).
Stage 2 decided (the owner delegated the answers): one structure memo per category (`framework/structure/<CODE>.md`), shared conventions `CONVENTIONS_v1.md`, decisions in `framework/structure/decisions/` (D1–D3, D4_residual R-0 to R-70). Start with `framework/structure/STAGE2_DECIDED.md`. The 11 rework categories passed a blind kind-level test (330/330 after rework).
Stage 3 started: data tables in `data/` (schema `tools/schema.py`, written only by `tools/data_write.py`); pilot A1 and D1 harvested (209 kinds attested, about 2,000 named forms, 262 lines, 1,362 makers). Plan: `framework/structure/STAGE3_PLAN.md`. See STATUS.md.

## Layout
- `BRIEF.md` – owner decisions. `STATUS.md` – session log, phases, owner queue.
- `framework/` – the category framework (CATEGORIES_v*.md) and `framework/structure/` (stage-2 memos, reviews, conventions, summary).
- `data/` – TSV data: stage-1 sources and probes, gold sets, and the stage-3 tables (nodes, kinds, named_forms, lines, makers and the other CONVENTIONS_v1 tables).
- `pages/` – generated review pages (stage2_review.html, published as https://claude.ai/artifact/WrwQ9sYpZYYg6YCd3FFdkN; rebuild with tools/build_stage2_page.py).
- `tools/` – scripts (backups to bak/, git-ignored).
- `verify/in` – agent prompts and batches; `verify/out` – agent outputs; `verify/work` – scratch (git-ignored).
