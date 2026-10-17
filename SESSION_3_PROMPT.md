# Session 3 prompt — Possession taxonomy

Continue the Possession taxonomy in /home/user/Possession-Taxonomy on branch `claude/adoring-gates-42vva3`. Read CLAUDE.md, BRIEF.md (especially "Owner decisions on stage 2"), the last two sections of STATUS.md and this file before acting. Work autonomously: the owner has delegated the stage-2 answers to Claude ("Your judgment for the answers"), so decide open points yourself, record each one as a new R-item in framework/structure/decisions/D4_residual.md, and commit after every phase.

## Where things stand
- Framework: framework/CATEGORIES_v0_7_1.md is live and untested. The last blind round tested v0.6 (round 6: 99.8 % unanimous, κ 0.999, 95/96 gold).
- Conventions: framework/structure/CONVENTIONS_v1.md. Decisions: framework/structure/decisions/D1–D3 and D4_residual (R-0 to R-57).
- 53 structure memos (framework/structure/<CODE>.md) are decided. Section 12 of each lists the decisions applied, and there are no open OWNER marks. The † claims, about 3,600, are the attestation list for the stage-3 harvest. There is no separate sourcing pass.
- Owner rules: depth and breadth are the point, with no caps. One fetched page proves existence. Use existing catalogues first (data/source_catalogues.tsv, 937 sources). Genres of games, music and film are never levels or tags here; they belong to other taxonomies.

## Do, in order
1. **Kind-level test, part 1 (11 rework categories: A2 B8 C1 D4 E1 F2 F4 G2 H2 I2 J5). All 11 trees and 30-item sets were built in session 2.**
   - Check that verify/out/KL_<CODE>_tree.md and KL_<CODE>_items.tsv exist for each. Re-run any missing builder with verify/in/KL_<CODE>.prompt.txt (Sonnet, web).
   - Copy each tree, frozen, to audit/KL_<CODE>_tree.md.
   - Write verify/in/KL_PLACE_COMMON.txt. A placer files each item into one kind id of the frozen tree (or "none fits"), with confidence and a note. It reads only the frozen tree and the item file without expected_kind; build that file with a tools/ script.
   - Run 3 Sonnet placers per category. Write tools/score_kl.py to score unanimity and accuracy against expected_kind per category.
   - Fix trees where agreement is low, by an Opus pass on that memo, and log the fix as an R-item.
   - Builder notes (session 2) to settle before placing, each as an R-item:
     - Kind ids were assigned by the builders (the memos had none), each in its own scheme: A2/B8/C1/D4/G2/H2/I2/J5/F4 use dotted paths, E1 keeps memo numbers as E1-Knn, F2 uses F2-Knn. J5's ids do not match the memo's 1–115 numbering. Adopt or normalise the ids, and write the chosen ids back into the memos.
     - J5 split multi-term memo lines into separate kinds (fermented seasonings, tomato products, sauerkraut/kimchi). It also placed mung bean and black gram under Beans, and pigeon pea under Chickpeas & other pulses. Seven J5 leaves have no kinds decided. J5 items 13, 18, 22 and 25 are partly settled by precedence sentences the tree itself carries.
     - Judgment-call expected answers that a split may reflect rather than a tree fault: C1-05 axe/maul, C1-20 ladder, C1-26 wheeled toolbox; H2-18 commode chair, H2-01 care pendant; F2-22 Hummel (K51 earthenware per memo, but the page says porcelain).
     - F2-26's "carved by hand" comes from a search excerpt; re-check it against a fetched page or drop it from the definition. F4 left the mezuzah case out (F4.3.3 or F4.7 is undecided).
     - Coverage was sub-family only. Untested kinds are listed in each builder's report: B8 locks, F4.7.2, E1.7/E1.9 and others. The harvest must still attest them.
2. **v0.7.2.** Apply R-57(d) and any key fix from step 1, then freeze audit/CATEGORIES_R7.md.
3. **Round 7.**
   - Run verify/in/RG7V.prompt.txt (Opus cold check of the 493 regression candidates; point it at the frozen R7 key).
   - Run `python3 tools/add_probes_rg7.py 707` to append the K rows, write data/gold_RG7.tsv and build verify/in/BP7A.tsv.
   - Run 3 fresh Sonnet placers with verify/in/BLIND_COMMON.txt against audit/CATEGORIES_R7.md.
   - Score with `python3 tools/score_blind.py BP7` and check accuracy against data/gold_RG2.tsv and gold_RG7.tsv.
   - Run a cold Opus audit (AU4) of every non-unanimous item and gold miss, then fix the key as v0.7.3 if needed.
4. **Owner page.** Write framework/structure/STAGE2_DECIDED.md, an Opus summary of the decided structures: one row per category, plus the main decisions and the test results. Extend tools/build_stage2_page.py to render it as a third tab. Republish to https://claude.ai/artifact/WrwQ9sYpZYYg6YCd3FFdkN; read that artifact first, since this is a new conversation.
5. **Stage 3 start.**
   - Design the data tables from CONVENTIONS_v1 as data/*.tsv schemas with tools/ writers: kinds, maker ledger, lines, named forms, variants, aliases, compatibility, jurisdiction, standards and designations, varieties, issuers, grading scales, school table and scheme registry.
   - Pilot the harvest on A1 Clothing and D1 Computers. Seed from their anchor catalogues in data/source_catalogues.tsv. Attest each kind and named form on one fetched page, and keep fetch_status per row.
   - Then plan the remaining categories in the order STAGE2_SUMMARY.md §6 gives.
6. Update STATUS.md ("Session 3") and README, and commit and push after each phase.

## Working rules (from CLAUDE.md, plus lessons from session 2)
- Web only through WebSearch/WebFetch or mcp__Parallel_Auth__web_search / web_fetch (allow_live_fetch on); never curl, wget or Python fetching. Data changes only through tools/ scripts with backups.
- Sonnet does harvesting, placers and memo editing; Opus does cold checks, audits and rework.
- Agents never run git. Every prompt goes in verify/in/ with a RESUME RULE, and helper files only in verify/work/<BATCH>/.
- Give agents explicit inputs and outputs. Where an agent finds a gap, decide it as an R-item rather than leaving it open, and record any key wording it reports for the next key revision.
