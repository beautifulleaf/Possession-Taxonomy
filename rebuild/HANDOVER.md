# Handover — Possession Taxonomy rebuild
Published artifact: https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n (page index.html + reader/<CODE>.json per category + reader/_brands.json, _traditions.json, _baby.json).
Audit doc: https://claude.ai/artifact/NGAY6hxjvndTauugtusdX8 .

Workspace layout (recreate at ~/pt or any dir; scripts use their own dir):
- RULES.md (binding owner rules), SCHEMA.md (agent brief + schema v2), FINDINGS.md (per-category fixes), HANDOVER.md
- build.py (makes index.html from template_v1.html + app.js + meta.json + reader/), merge.py (out/<CODE>* → reader/, registers, moves, baby view), validate.py
- reader/ (current published data), out/ (agent outputs; A5 done), work/ (scratch), done.json, moves_applied.json
SCHEMA.md paths assume /home/user/Possession-Taxonomy/rebuild — update them to the new location.

State: A5 rebuilt (pilot, approved for method). 41 kinds tagged "baby". Data errors fixed. Everything else pending.
Loop per batch: run agents (one category each, prompt = SCHEMA.md + RULES.md + FINDINGS row) → validate → merge.py <codes> → build.py → publish index.html + changed reader files to the artifact URL.
New categories (G3, H4, J8, J9, recodes J10/E5/E6) need meta.json entries + their files; moves feed them (run donors first).
Sources: Wikipedia/Wikidata APIs (throttle), Firecrawl/Parallel search+scrape, official DB APIs via keys (network secrets; header names per API docs), never work around bot walls.

## Rebuild complete (2026-10-27)
- All 57 categories rebuilt and merged (done.json); published as artifact v23 (https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n).
- Totals: kinds 6,716 → 7,932 (A5 pilot not in the before count); 17,595 archetypes; flat models 41,184 → 18,557; models + archetypes + versions 64,559; brand register 10,938; 747 traditions; 187 rare mineral species.
- Registers are nested per category: build.py runs tools/registers.py, which writes reader/brands/<C>.json, reader/traditions/<C>.json, reader/species/<C>.json and reader/_brand_index.json (Brands A–Z finder). The page shows Kinds / Brands / Traditions / Rare species tabs per category.
- Same-name different companies are separated through work/_clash/map.tsv (applied in merge.py; entries keep the original name in "an" for maker links). Same-country homonyms were not scanned.
- Frozen pre-rebuild data for every category is in work/<C>/old.json (the source check reads it; reader/<C>.json is the rebuilt file).
- Moved kinds: merge.py re-applies incoming moves; moves_covered.json folds a moved kind into a named kind, or renames it on arrival with a leading "=".
- Follow-ups: rebuild/work/_followups.md (all closed except a process note: split workers in one category need separate scratch folders).

## 2026-10-28 (branch claude/toy-organization-system-mapqhu)
- Owner decisions (BRIEF.md, RULES.md): pursuits (Physical, Creative, Intellectual, Spiritual) belong to separate taxonomies, so categories stay object-focused; F4 is grouped by object form first, with the faith tradition as a kind tag (tools/f4_form_first.py).
- E1: new department "Puzzles, fidgets & desk toys" (batch E1PZ, prompt verify/in/E1PZ.prompt.txt, report out/E1PZ_report.md): 28 kinds and 86 archetypes, +23 brands and designers; "Electronic handheld toy" on the Skill toys shelf; Mattel Auto Race moved to E5 "LCD handheld game" (tools/e1_handheld_fix.py).
- Published artifact v26. The live reader/_brands.json had been an older copy (10,847 brands); v26 carries the current register.
- Suggested next audits (object-focused): rest of E1 (craft toys, marbles, circus props, model rocketry), pocket knives and multitools in C1, E2 equipment grouped by object, C4 by material and tool type.
