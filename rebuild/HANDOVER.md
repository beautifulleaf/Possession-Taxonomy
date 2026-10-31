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

## 2026-10-28, continued: audits AUD3 and fixes for every category (artifact v28)
- Audit batch 2 (v27): E1 rest (creative toys, circus props, model rocketry, marbles), C1 pocket knives & EDC, C4 regrouped by goods, E2 split A/B and assembled by tools/e2_assemble.py.
- Cold audits AUD3 (Opus, verify/out/AUD3_<group>.md) for every remaining category; one Sonnet fixer per category (prompts verify/in/FIX_<CODE>.prompt.txt over FIX_COMMON.txt; reports out/FIX_<CODE>_report.md).
- Owner decisions this round (BRIEF.md): built-in lights → G3 "Built-in lighting"; locks stay in B8; packaged prepared foods are in (J5 "Prepared & frozen foods").
- merge.py now: moves_place.json puts moved kinds on a named "Dept / Shelf" or drops them ("-"); otherwise picks the best word-matching shelf instead of creating a stray department; moves_covered.json folds archetypes as well as models; repeated model rows in moved kinds are de-duplicated.
- J4's 453 RHS garden cultivars moved to C3 (445 adopted; 16 per-crop seed kinds).
- Totals: kinds 7,932 → 7,811 (merges of attribute-only kinds), archetypes 17,595 → 18,649, brands 12,813, traditions 835. tools/lost_check.py <ref> lists vanished names (all checked: renames, merges into types, catch-alls, concepts).
- app.js: archetype field `ex` shown as "Example:"; brands flagged `stub` grouped last as "Listed only".
- Follow-ups (rebuild/work/_fixqueue.md): cross-link field in the schema (many cross-category pairs left as duplicates: D3/E3 turntables and mics, C4/C5 inkstones, B5/G3 range cookers, D2/E5 XR glasses, D1/E5 THEC64, B4/F2 Venini, C2/C8 barbecue fuel); J7-5 wine re-levelled by appellation > producer > classification; E3-7 orchestral vs folk split by culture; E4-5 Japanese swords by school and period with a smith register; F2-6 ULAN artist register; C3-3 living-plants species register; J2 species vs family consistency; many unsourced icons listed per report (blocked databases: Watchbase, Fragrantica, Parfumo, vitra.com, Shimano).

## 2026-10-31 (session 13, on main): structure pass STR, artifact v30
- main now carries this rebuild (merged from claude/toy-organization-system-mapqhu). Work on main.
- Schema v3 (verify/in/STR_COMMON.txt): category `ax`, `key`; department `t`, `ax`; shelf `t`, `ax`; kind `tt` [[axis,[types]]] and `see` [[CODE,kind,why]]. Check with `validate.py --v3`.
- Loop per category: agent edits out/<CODE>.json (+ _renames.json, _moves.json) → tools/str_merge.sh <CODE> (merge, validate, commit, push) → build.py → publish.
- After any pass that demotes archetypes: tools/restore_lost.py --write (from work/STR_<CODE>/bak), then tools/see_check.py --fix.
- Framework v0.8: framework/CATEGORIES_v0_8.md; page data framework/key_v0_8.json (build.py embeds it).
