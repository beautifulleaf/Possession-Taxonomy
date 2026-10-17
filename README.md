# Possession taxonomy

A taxonomy of the things people own and keep: every generic type of object a person can have, from clothing and tools to vehicles, property, media, plants and digital goods. Stand-alone domain, built with the method of the Culinary and Pleasure taxonomies.

## Plan
- **Stage 1 – top-level categories.** A list of top-level categories, each with one membership test and precedence sentences for blurred edges, built outside-in from existing classifications and tested by blind placement of real possessions. Nothing below the categories is fixed in stage 1.
- **Stage 2 – one structure study per category.** A research memo per category on how the domain itself is organised (axes, depth, tiers, makers, scenes, order), from which the owner approves that category's structure. Pilot on Clothing and PC components.
- **Stage 3 – build.** Harvest kinds under the approved structures, attest, audit, publish.

## State
Stage 1 done for owner review: `framework/CATEGORIES_v0_6.md` (53 categories) and `framework/STAGE1_REVIEW.md`.
Stage 2 research done for owner review: one structure memo per category (`framework/structure/<CODE>.md`, 53), ten domain reviews (`_review_A.md` … `_review_J.md`), a conformance pass on every memo (section 11 of each), shared conventions (`_conventions.md`) and top-level conflicts (`_framework_conflicts.md`). Start with `framework/structure/STAGE2_SUMMARY.md` and `STAGE2_OWNER_QUESTIONS.md`. Nothing in stage 2 is approved yet. See STATUS.md.

## Layout
- `BRIEF.md` – owner decisions. `STATUS.md` – session log, phases, owner queue.
- `framework/` – the category framework (CATEGORIES_v*.md) and `framework/structure/` (stage-2 memos, reviews, conventions, summary).
- `data/` – TSV data (source category harvest, probe samples, placements).
- `tools/` – scripts (backups to bak/, git-ignored).
- `verify/in` – agent prompts and batches; `verify/out` – agent outputs; `verify/work` – scratch (git-ignored).
