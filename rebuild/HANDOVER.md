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
