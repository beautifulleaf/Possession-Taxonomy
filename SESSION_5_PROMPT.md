# Session 5 prompt — Possession taxonomy

Continue the Possession taxonomy in /home/user/Possession-Taxonomy on branch `claude/stoic-ptolemy-4nctsh`. Read CLAUDE.md, BRIEF.md (navigation, regional coverage, proportional coverage), the last section of STATUS.md, framework/structure/decisions/D4_residual.md R-77 to R-95, framework/structure/STAGE3_PLAN.md (step 2b is new), and this file. Work autonomously: decide open points as new R-items, commit and push after every phase.

## Where things stand
- A1 Clothing: 257 A1/D1 kinds (11 regional kinds added, R-84); 206 scenes in 15 clusters, 7,746 brand tags; 28,445 clothing brands, 2 % without a country; reference distribution verify/out/coverage_reference_A1.tsv; no country below half its expected share (tools/coverage.py A1). About 12,000 brands still have only a category-level tie.
- Loader: every batch loads with `python3 tools/load_s4.py BATCH` (fetch-log check, merged-id remap, deferred rows, tidy). Recovery batches of held makers first run tools/gdp_makers.py BATCH. Held makers: verify/out/held_makers.tsv and verify/out/*_held_unconfirmed.tsv.
- Pilot page: https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk (tools/build_pilot_page.py writes pages/pilot.html and pages/pilot-data.json; publish both, the JSON through `files`).
- Agents: WebSearch/WebFetch only (Parallel is out of credit); at most about 12 at once (WebFetch limits each domain).

## Do, in order
1. Load any GD_* batch whose verify/out/<BATCH>_maker_kinds.tsv exists but is not loaded (compare with git log), and REG_PKTR; run tools/merge_makers.py --auto, tools/coverage.py A1; top up any country that falls below 0.5.
2. Kinds review (one Opus pass, like DP_S4B): scrubs, lab coat, wetsuit, fur coat, raincoat, pheran, co-ord set, Nehru jacket and bandhgala, Mandarin jacket, kaftan (now mapped to dress), and the storefront question (whether department stores and retailers count as clothing brands in coverage).
3. Remaining GD lists for brands still at category level (generate new lists for brands no GD list covered), prioritising regions with high yields (US, India, Japan, Korea, Europe).
4. Step 6 of SESSION_4_PROMPT.md: the STAGE3_PLAN.md depth passes (D1 chip, card and laptop models; A1 signature pieces per scene) and wave 1 (B10, C6, I1, D5, J4, J2, B3, J3), each with its reference distribution before the maker harvest (STAGE3_PLAN step 2b) and the navigation rule (scene, brand or shopper path).
5. Republish the pilot page and update STATUS.md and README.
