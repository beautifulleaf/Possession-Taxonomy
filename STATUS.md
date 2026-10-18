# Possession taxonomy — status

## Session 1 (2026-10-17) — Stage 1: top-level categories
Search cap: `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` = 100000. Test WebFetch (Google Product Taxonomy file) and Parallel web_search (Getty AAT) both work.

| Phase | What | State |
|---|---|---|
| 0 | Scaffold repo (CLAUDE, BRIEF, settings, layout) | done |
| 1 | Harvest source classifications H01–H06; collect probe items P01–P04 | done: 4,007 source nodes (data/source_nodes.tsv); 438 probe items (data/probes.tsv: 300 round 1, 138 round 2) |
| 2 | Draft category framework v0 | done: framework/CATEGORIES_v0.md (9 domains, 37 categories, 27-step key); frozen copy audit/CATEGORIES_R1.md |
| 3 | Round 1 (BP1, CW01–04, AU1) → v0.1; round 2 (BP2, CWR1–2, AU2) → v0.2; round 3 (BP3 + audit regression set) → v0.3 | done |
| 4 | Close: results, owner queue, stage-2 memo template, review page | done |

### Harvest notes (phase 1)
- Sources reached: Google Product Taxonomy (complete), Shopify (level 1, partial level 2), GS1 GPC segments; Getty AAT Objects facet, Nomenclature 4.0 (complete), SHIC sections; COICOP 2018, UNSPSC, HS 2022, BLS CPI; Etsy, Walmart, IKEA, Mercari, Rakuten, JD, Mercado Libre, Allegro, Jumia, Craigslist, Facebook Marketplace; Christie's, Sotheby's, Heritage, Phillips, Catawiki, LiveAuctioneers, Invaluable, eBay collectibles, Depop, Grailed, Reverb, Chrono24, Discogs; NAIC, III, State Farm, UK contents lists, ISO scheduled property, US bankruptcy Schedule B, a probate inventory, property and digital-asset guidance.
- Not reached: Amazon browse tree, eBay full tree, Taobao/Tmall, Flipkart, Avito, Bonhams (403). The unauthenticated Parallel endpoint returned 429 to two agents; the authenticated one worked.

### Round 1 results (framework v0, audit/CATEGORIES_R1.md)
| Test | Result |
|---|---|
| Blind placement BP1 (300 items, 3 Sonnet placers) | 96.0 % unanimous, 100 % majority, Fleiss κ 0.972 |
| Source crosswalk CW01–04 (4,007 outside category nodes) | 95.1 % of in-scope nodes homed; NOHOME 2.5 %; AMBIG 2.4 % |
| Cold audit AU1 (Opus) | 35 findings (verify/out/AU1.md) |

- Placement disagreements (12) all came from four wordings: sport armour vs "armour of any use"; computer peripherals vs speakers/cameras/controllers; worn ritual objects (tefillin) and ritual lamps/instruments; corrective eyewear vs eyewear.
- Crosswalk gaps: building materials, fasteners, paint, adhesives, fuels; household consumables (detergents, batteries, air fresheners, pest control, gift wrap); medicines; natural specimens and loose gemstones; standalone GPS and trackers; loose electronic components; fireworks; commercial signage and trade equipment.
- Audit, accepted: narrow the health step (it captured all protective gear and fitness trackers); make the key total (S1a, function-worded C1 with materials, X0 bin, natural specimens); move music ahead of electronics; drop 'smart-home' and 'built-in' as axes; re-cut household categories by task instead of power source; split craft vs tools by craft type, not hobby vs work; religious objects worn or not; money, stamps and awards as one category; key declared authoritative.

### Decisions (framework v0.1)
- 44 categories (was 37) in 9 domains plus an X0 holding bin. New: A5 Clocks & Watches, B3 Lighting, B6 Cleaning & Laundry, B7 Storage & Organisation, B8 Climate & Water, B9 Home Safety & Security, C6 Optical & Scientific Instruments, C7 Farm & Trade Equipment, F6 Natural History & Specimens. Renamed: B2 Soft Furnishings, B5 Kitchen & Dining (powered or not), B10 Cellar & Smoking, C1 Tools, Hardware & Materials, C3 Plants & Living Cultures, D2 Phones, Tablets & Personal Devices, D3 Audio & Video, D4 Cameras & Photography, E2 Sports, Fitness & Recreation, F3 Coins, Stamps, Medals & Collectibles. Each split is for a different designed function and a different inner structure, never for size.
- Rights and financial instruments (tickets, timeshares, shares) are OUT; their paper tokens are F5. Physical cash is in (F3).
- **Wine and spirits stay in scope (owner, BRIEF) but by object, not motive:** every bottled alcoholic drink and tobacco product owned is B10 stock; all other food and drink is OUT. The audit proposed dropping drink entirely as a motive test; that would change an owner decision, so it went to the owner queue instead.

### Round 2 results (framework v0.1, audit/CATEGORIES_R2.md)
| Test | Result |
|---|---|
| Blind placement BP2, all 438 items, 3 fresh Sonnet placers | 98.4 % unanimous, 99.8 % majority, Fleiss κ 0.988 |
| Fresh items only (138, never placed before) | 96.4 % unanimous |
| Round-1 items re-placed (300) | 99.3 % unanimous (was 96.0 %) |
| Crosswalk regression CWR1–2 (190 round-1 problem nodes + 310 clean nodes) | 160 of 190 problem nodes resolved; 10 of 310 clean nodes newly ambiguous; estimated full-crosswalk NOHOME+AMBIG 4.0 % (was 4.9 %) |
| Cold audit AU2 (fresh Opus) | 55 findings (verify/out/AU2.md); verdict "sound in shape, not yet in boundaries" |

- Remaining splits: casino chips, Dictabelt, family Bible, computer microphone, tool bag, cigar box, barcode scanner. Remaining crosswalk NOHOMEs are empty catch-all buckets plus valves/regulators and wood pulp.
- AU2's main points: several lead questions excluded their own examples under S1a (suitcases, tripods, game discs); bracketed notes had no stated force; S3's "one kind vs a class" was undecidable; steps 6, 21, 23 and 12 were too broad (firewood as a specimen, kitchen scales as instruments, footballs as games, wedding rings as rites); installation, market, setting, occasion, user and connectivity still decided some boundaries.

### Decisions (framework v0.2)
- Key mechanics: S1a branch order declared; S1b notes bind; lead questions of the worn/carried, body-care, electronics, play and tools steps rewritten to include their own examples.
- S3 rewritten: only cases, bags, covers and stands for one object at a time are parts; furniture and storage, anything worn, building products and plant-growing goods are never parts; cleaning products always B6, fuels always C8.
- Installation is no longer a boundary: G2 holds land and whole structures; building products are C8 installed or not; fitted cabinetry is B1; fitted carpets and blinds B2; sanitaryware and hot tubs B7.
- Market and setting removed: commercial catering joins B5, point-of-sale D1, shop signs B4, shop fittings B1; camp furniture, stoves and lanterns go by function; C7 becomes Farm & Forestry and moves early in the key.
- Merged B1 Furniture with B7 Storage (split only by size). Split C1 into C1 Tools & Workshop Equipment and C8 Building Materials & Hardware (different inner structures). Count stays 44 plus X0.
- Narrowed: specimens (step 6) to objects kept as specimens; science (C6) to observation and study; play (E1) to play and table/board/card/dice games, sports to E2; religious (F4) to religious practice and the dead, occasion a modifier.
- Figures: ornamental figurines F2; character and collectible figures E1; garden statues B4; models and kits E1 built or not; F3 narrowed to money, postage, awards and non-game trading cards.
- Scope: digital licences are not rights (I1); living cultures are in; burial plots however held; access and payment cards F5; human remains OUT; alcohol in sealed containers and smoking products (tobacco, cannabis, nicotine) in B9.

- **Process fault (round 3):** the three placers shared the session scratchpad; placer C read about 174 of another placer's rows and wrote into its file. C's output is kept as verify/out/BP3x_C_contaminated.tsv and excluded; a fresh placer D replaces it. BLIND_COMMON.txt now confines scratch files to verify/work/<BATCH>/. A's and B's outputs were checked complete and are their own final files.

### Round 3 results (framework v0.2, audit/CATEGORIES_R3.md)
| Test | Result |
|---|---|
| Blind placement BP3, 698 items (438 probes + 260 regression objects from both audits), placers A, B, D | 97.4 % unanimous, 100 % majority, no splits, Fleiss κ 0.982 |
| Probes only (438) | 98.4 % unanimous |
| Audit regression objects (260) | 95.8 % unanimous |

- Non-unanimous (18): computer speakers, Dictabelt, meditation mat, steel-toe and safety boots, scrapbook, tricycle, medical alert bracelet, riding hat, cigarette case, Easter basket, ceremonial mace, judge's gavel, sack truck, shirt button, animal hide, empty picture frame, jeweller's saw. Majority homes for the regression set were checked by hand; the questionable ones (garden tractor in C7, hide in F6, mace and gavel in X0 or B4) are fixed in v0.3.
- **v0.3** adds one precedence sentence for each of these (footwear branch before protective clothing; equestrian riding hats E2; medical alert tags H2; sack trucks and hand carts C1; shopping trolleys A4; garden tractors C2; regalia of office F3; computer speakers D3; all recording carriers F1; meditation mats B2; blank scrapbooks C4; children's tricycles E1; cigarette cases B9; picture frames B4; festival baskets B1; loose notions and tanned hides C4). v0.3 has not been re-tested.

### Session 1 summary
- Stage 1 delivered: framework/CATEGORIES_v0_3.md (44 categories in 9 domains, 32-step key, S1–S6, Appendix A modifiers) and framework/STAGE1_REVIEW.md (one-page review). Stage-2 memo template: framework/STAGE2_MEMO_TEMPLATE.md.
- Data: data/source_nodes.tsv (4,007 outside nodes from 30 classifications), data/probes.tsv (438 sourced probe items + 260 audit regression objects). Tools: tools/build_probes.py, build_nodes.py, score_blind.py, score_crosswalk.py.
- Agents: 6 harvest, 4 probe collectors, 13 blind placers (one excluded), 6 crosswalk, 2 Opus cold auditors, 1 regression builder. Web use (agents' own counts plus mine): 88 searches and about 320 fetches; no cap notice.

## OWNER QUEUE (superseded, see 'Owner queue (current)' below)
1. **Approve, edit or reject the 44 categories** (framework/STAGE1_REVIEW.md). Stage 2 starts only after this.
2. **Wine and spirits.** Kept in scope as B9 (your decision: wine cellars are in), now by object: every alcoholic drink in a sealed container that a person owns. AU2 suggests moving drink stock to the Culinary taxonomy and leaving B9 as Smoking & Vaping. Keep, or move?
3. **Cannabis and nicotine products** are in B9 alongside tobacco. Confirm.
4. **Accounts and currency:** game, social and email accounts are OUT, but items held in them are I1. Cryptocurrency holdings are OUT like a bank balance; NFTs are in. Confirm.
5. **Baby and child goods** have no category; the user's age is a modifier, and a generated 'baby & child' view could follow later. Confirm, or ask for a category.
6. **Stage-2 pilot.** Proposed: one study for A1 Clothing (with A2, A3 and A4 as neighbours) and one for D1 Computers & Components, using the memo template. Confirm the pair.

## Next (session 2)
After the owner's answers to the queue: apply any category edits to v0.3, re-run one blind round if anything structural changed, then run the stage-2 pilot memos for the two approved categories (template in framework/STAGE2_MEMO_TEMPLATE.md; web research agents, Opus reviewer per memo).

## Session 2 (2026-10-17) — Stage 2 pilot: A1 Clothing and D1 Computers & Components
Owner approved the 44 categories "as of now" and raised no objection to queue items 2–6 (defaults recorded in BRIEF.md).

| Phase | What | State |
|---|---|---|
| 0 | Research batches CL01–06 (clothing) and PC01–05 (computers) | done |
| 1 | Memo drafts (Opus writer per category, from research outputs only) | done; then extended to all 53 categories (see Stage 2 below) |
| 2 | Cold review of each memo (Opus), revisions | done as domain reviews and a conformance pass |
| 3 | Present memos and owner decisions | framework/structure/STAGE2_SUMMARY.md |

## Session 1, continued — owner scope decisions and rounds 4–5
Owner decisions (2026-10-17, BRIEF.md): groceries in as graded ingredients; software types in; media, games and subscriptions as objects and kinds of access, never by genre; subscriptions and streaming in; edge calls answered (pet food B10; supplements in; single tickets and one-off services out; crypto out, NFTs in; online services by utility vs entertainment, not price; overlapping foods link to Culinary; cannabis and nicotine with tobacco; baby goods distributed).

| Step | Result |
|---|---|
| Grocery harvest G01 (Google and COICOP food branches, 5 grocers, 29 grading schemes) and probe sets PG1 (120 sourced grocery items) and PS1 (39 software, media and staple items) | done |
| Framework v0.4: domain J Groceries & Cellar (J1–J7), domain I split into I1 Software, I2 Digital Media & Items, I3 Subscriptions & Memberships; B9 becomes Smoking & Vaping; boxed software moves to I1 | 53 categories |
| Round 4 (857 items, 3 placers) | 99.1 % unanimous, κ 0.994; 159 new items 100 % unanimous |
| Cold audit AU3 (Opus) on the new scope | 25 findings, 72 hard cases; 49 of 72 had more than one answer under v0.4 |
| Framework v0.5: closed definition of prepared food; S1b notes jump directly; I3 limited to five kinds of access (catalogues, online utilities, connectivity, member places, curated deliveries) with a bundle rule; services one-off or recurring OUT; in-game currencies OUT; live shellfish in J2; frozen and dried produce, plant milks and meat alternatives homed; B9 by substance in any form; animal food B10 everywhere | |
| Round 5 (953 items incl. 96 audit hard cases with intended homes) | 99.0 % unanimous, κ 0.993, no splits; 94 of 96 hard cases at their intended home (the two misses were the expectation: jarred pasta sauce is a sauce; a class card is a pass) |
| Framework v0.6: one precedence sentence for each round-5 doubt (heated tables B1, soban B1, EV chargers and bike locks G1, cap tassels A1, piñatas E1, health tonics H2, mixtapes F1, pass cards I3, jarred pasta sauce J5); header history corrected (v0.4 and v0.5 files had kept the v0.3 header line) | not re-tested |
| Round 6 (v0.6 frozen as audit/CATEGORIES_R6.md; same 953 items reshuffled; 3 fresh Sonnet placers) | 99.8 % unanimous (951/953), κ 0.999, no splits; 95 of 96 audit cases at their intended home (the miss is the known one: jarred pasta sauce is J5 by the v0.6 sentence, the old gold said OUT); 9 items moved from round 5, all as the v0.6 precedence sentences intended (kotatsu and korsi B1, workbench C1, fudepen C5, season ticket and class card I3, festival wristband OUT, piñata E1, survival kit B8). The two non-unanimous items (phone charger, emergency survival kit) are decided by K-3 and K-1. |

## Owner queue (stage 1, still open)
1. **Approve, edit or reject the 53 categories** (framework/STAGE1_REVIEW.md). Stage 2 starts after this.
2. **Phone and broadband plans** are in (I3, connectivity); home energy and water supply are out as services. Confirm.
3. **Recurring personal services** (a cleaner on contract, weekly lessons) are out like one-off services. Confirm.
4. **Commuter season tickets** are in I3 with other passes. Confirm.
5. **Vitamins, supplements and sports nutrition** sit under H2 Health. Keep there or move to groceries?
6. **Stage-2 pilot pair:** Clothing and Computers & Components proposed. Confirm or choose others.

## Stage 2 (2026-10-17, continued while the owner was away) — structure research for all 53 categories
Owner instruction: "continue everything you can". Everything below is research for owner review; nothing is approved.

| Phase | What | Result |
|---|---|---|
| Memos | One structure memo per category (framework/structure/<CODE>.md; Sonnet research and writing, template framework/STAGE2_MEMO_TEMPLATE.md incl. 4b choice level and a 20-object usability check); sources in verify/out/S2_<CODE>_sources.tsv | 53 memos, 3.9 MB |
| Reviews | Ten cold domain reviews (Opus), framework/structure/_review_A.md … _review_J.md; J also checks the Culinary boundary and links | verdicts: 1 ready (B10), 41 minor fixes, 11 rework (A2, B8, C1, D4, E1, F2, F4, G2, H2, I2, J5) |
| Conventions | Shared conventions C1–C17 adopted for drafting, plus proposed additions from reviews F, G, H, I and J (JC1–JC7) in _conventions.md | 46 convention questions (CV-1 … CV-46) |
| Framework conflicts | Top-level key problems logged per review, then a sweep of all reviews and memo sections 9–10 (_framework_conflicts.md) | 229 entries, merged to 196 questions (K-1 … K-196); 20 would move 24 round-5 probe objects |
| Conformance | Each memo revised to its review and the conventions (Sonnet; Opus for the 11 rework memos); owner-dependent items kept as the memo recommended and marked OWNER:, unsourced claims marked †; section 11 revision log in every memo | 53 of 53 done; 2,568 † and 1,925 OWNER marks (verify/out/S2_stats.tsv, tools/s2_stats.py) |
| Summary | Seven domain digests (verify/out/S2S_X*.md) and a cold Opus summary | framework/structure/STAGE2_SUMMARY.md (owner page) and STAGE2_OWNER_QUESTIONS.md (K-1…K-196, then A-1…J-17: 228 per-category questions) |

Known contradictions left open for the owner (summary §6): workbench B1/C1 (K-190), chainsaws C1/C2 (K-173), plants in pots (K-73), sets (K-1), labneh (K-44), Japanese lanterns (K-116), pencil cases (K-132), hard seltzer (K-24).
Not done: no web sourcing in the conformance pass (all † remain); no `fetch_status` column in the sources files (needs a tools/ script, CV-39); v0.6 and every stage-2 change untested blind.

## Owner queue (current)
1. Stage-1 queue above (approve the 53 categories of v0.6; items 2–5).
2. **Shared conventions:** CV-1 … CV-46 (STAGE2_SUMMARY.md §3), yes/no each.
3. **Framework changes:** the 25 consequential K items in STAGE2_SUMMARY.md §4a, then the rest (STAGE2_OWNER_QUESTIONS.md part 1).
4. **Per-category questions:** the 15 in STAGE2_SUMMARY.md §5a first, then domain by domain (STAGE2_OWNER_QUESTIONS.md part 2).
5. **Owner question from B10:** allow the kind of animal served as B10's first axis (an Appendix A exception, K-102).

## Session 2, continued — delegated decisions, v0.7 and v0.7.1, source census (2026-10-17)
Owner rulings this session (all in BRIEF.md, "Owner decisions on stage 2"): the stage-2 answers are delegated to Claude; no separate sourcing pass (the † claims are attested at stage-3 harvest); depth and breadth are the point (no caps on makers, lines or named forms); one fetched page proves existence (no two-source rule); use existing catalogues first; board, video and other game genres go to a future Interactive Entertainment taxonomy.

| Step | Result |
|---|---|
| Round 6: v0.6 blind (audit/CATEGORIES_R6.md, 953 items, 3 Sonnet placers) | 99.8 % unanimous, κ 0.999, no splits; 95/96 gold |
| Delegated decisions | framework/structure/decisions/: D1 (CV-1…46, K-1…196: 231 adopted, 11 departed), D2 (A–E, 160), D3 (F–J, 125; G-13 and H-2 corrected to object tests), D4_residual (R-0…R-57, including R-16 a–hh, the key amendments) |
| Framework v0.7, then v0.7.1 | framework/CATEGORIES_v0_7.md (196 K decisions), framework/CATEGORIES_v0_7_1.md (63 changes: R-16 amendments, residual key notes, 7 contradiction fixes). Neither is tested yet. |
| Conventions | framework/structure/CONVENTIONS_v1.md (final; _conventions.md superseded) |
| Memo decision pass | all 53 memos have section 12 "Decisions applied"; 0 open OWNER marks; 15 residual follow-ups (S2X); 3,600 † (attestation list for harvest) |
| Source census (stage 3 prep) | 937 existing catalogues for all 53 categories in data/source_catalogues.tsv (tools/build_source_plan.py), plus follow-ups for puzzles, fashion subcultures and Asian sources |
| Tools | tools/s2_stats.py, tools/add_fetch_status.py (fetch_status on all S2 source files; auto values, checked at harvest), tools/build_stage2_page.py (owner page, published at https://claude.ai/artifact/WrwQ9sYpZYYg6YCd3FFdkN), tools/add_probes_rg7.py (round-7 batch) |
| Round 7 prep | verify/out/RG7_candidates.tsv (493 regression objects for K-1…K-196 and R items, not yet cold-checked); kind-level test builders KL_<CODE> for the 11 rework categories (A2 B8 C1 D4 E1 F2 F4 G2 H2 I2 J5) write verify/out/KL_<CODE>_tree.md and _items.tsv |

Open: R-57(d) card-sleeve wording in the key (for v0.7.2); trading-card sleeves are E1 parts.

## Session 3 (2026-10-17) — kind-level test, round 7, owner page, stage-3 pilot
Worked on branch `claude/stoic-ptolemy-4nctsh` (the branch named in SESSION_3_PROMPT.md, `claude/adoring-gates-42vva3`, does not exist; this session's designated branch holds all session-2 work). Decisions R-58 to R-70 in framework/structure/decisions/D4_residual.md.

| Step | Result |
|---|---|
| 1. Kind-level test (A2 B8 C1 D4 E1 F2 F4 G2 H2 I2 J5) | Builder notes settled (R-58 to R-63): one tree-path id scheme (E1, F2, I2 converted, 223 ids, verify/out/KL_id_crosswalk.tsv); J5 splits adopted; tie rules for C1 tool storage, H2 commode chair and care pendant, F4 doorpost case; F2-26 "hand carved" confirmed on a fetched page; F2-22 Hummel is earthenware. Trees frozen to audit/KL_<CODE>_tree.md. 33 Sonnet placers: 327/330 unanimous, 329/330 majority-right (R-64; A2-07 was an item fault). Opus rework KLFIX1 of A2, B8, G2 (R-66; new kind A2.2.2.07 plain slip-on shoe), frozen as audit/KL_<CODE>_tree_v2.md; retest 90/90 unanimous and right (R-67). Kind ids written back to each memo as section 13. Tools: kl_prepare.py, score_kl.py, kl_memo_ids.py. |
| 2. v0.7.2 | R-57(d) card sleeves (trading-card sleeves and toploaders E1). Frozen as audit/CATEGORIES_R7.md. |
| 3. Round 7 | RG7V cold check of 493 candidates (R-65: 480 ok, 8 definitions, 1 expected, 4 dropped); 470 K probes, data/gold_RG7.tsv. 3 Sonnet placers on 1,423 items: 99.6 % unanimous (1,417), no splits, κ 0.997; gold RG7 470/470, RG2 95/96 (R-68). AU4 cold audit of the 7 cases (R-69) → framework/CATEGORIES_v0_7_3.md (I3 entitlement sentence, sport kite, game launchers OUT); probe definitions fixed and gold T0036 → J5 (tools/fix_probes.py). v0.7.3 not yet re-tested. |
| 4. Owner page | framework/structure/STAGE2_DECIDED.md (Opus S2D): 53 decided structures, main decisions, test results. tools/build_stage2_page.py renders it as the first tab "Decided"; republished to https://claude.ai/artifact/WrwQ9sYpZYYg6YCd3FFdkN (version 2). |
| 5. Stage 3 start | Tables designed from CONVENTIONS_v1 (tools/schema.py: 26 tables) with one validating writer (tools/data_write.py) and a tree loader (tools/load_tree.py). Structure of 13 categories in data/nodes.tsv. Pilot A1 + D1 (R-70): 209/209 kinds attested on fetched pages; after the Opus decision pass HVMK (270 named forms moved to lines, 71 dropped, 37 new kinds found) and batch HV_NK (all 37 new kinds attested): 246 kinds (A1 127, D1 119), 2,103 named forms, 262 lines, 1,378 makers; data_write.py check is clean. Plan for the other 51 categories: framework/structure/STAGE3_PLAN.md. |

## Session 3, continued — owner navigation decisions, D1 rebuild, regional coverage
Owner saw the pilot and decided (BRIEF.md): clothing is navigated scene first (clusters → brands → signature pieces); D1 is rebuilt to shopper paths; clothing brands must cover every world region. R-71 to R-76: D1 rebuilt into 10 sub-families and retested 40/40 (R-72, R-73); constructed Aesthetics Wiki URLs held, 134 scenes to re-locate (R-74); regional harvest across 12 UN M49 regions, tools/regions.py and tools/coverage.py (R-75); category-level ties and scene-proposal queue, tools/load_batch.py and tools/tidy_ties.py (R-76). A1 now has 9,484 brands with a country for all but 19; 96 scenes loaded, 88 proposed. The US (226) and UK are under-represented. Owner principle added (BRIEF.md): coverage of every category should be proportional to the world's distribution of brands.

## Session 4 (2026-10-17/18) — scenes, regional garments, proportional coverage, garment depth
Worked on branch `claude/stoic-ptolemy-4nctsh`. Decisions R-77 to R-95 in framework/structure/decisions/D4_residual.md.

| Step | Result |
|---|---|
| 1. Unfinished batches | verify/work/ had been lost with the old container (R-77). SC_A1R re-run in three parts: 133 of 134 held scenes re-located on search-found pages; SCB_1–7 (scene membership, split for speed) loaded: about 6,300 scene tags. Excerpt-only sources removed by tools/drop_excerpt_sources.py (R-78). |
| 2. Decision passes | DP_S4A (Opus): 105 scenes accepted, 84 merged, 32 rejected (R-81); DP_S4C: 5 more accepted (R-95); 206 scenes, 7,746 tags. DP_S4B (Opus): 11 new A1 kinds (bodysuit, bondage trousers, thobe, boubou, tunic suit, hanbok, wrap robe, track jacket, abaya, sherwani, headscarf), kurta reworded to the generic tunic shirt, 31 named forms, 184 re-ties, Alienware relation, open countries (R-84). HFB checked the 249 high-fashion names: 185 clothing (R-85). |
| 3. Proportional coverage | Reference distribution (R-80; tools/coverage_ref.py; verify/out/coverage_reference_A1.tsv) from market size, trademark filings by origin and Wikipedia brand counts. US/UK depth passes (9 batches) and country passes for DE, CN (4 rounds), IT, FR, ES, TR/IR (2), CH/NL, BR/BE, RU, AU/KR, IN, MX/AR/CO/CL, Nordics, TW/HK, plus country backfill and duplicate merges (R-86, R-89). A1 brands 9,484 → 28,445; no country below half its expected share (R-94; US 0.56, CN 0.53, GB 2.6×, IN 2.5×). Mixed fashion rankings held (R-87), factory directories kept as manufacturers but not counted as brands (R-91). Method written into STAGE3_PLAN.md step 2b (3d). |
| 4. Garment depth | GD batches (verify/in/GD_COMMON.txt) tie roster-only brands to garments: yields about 10 % for African fashion-week rosters, 40–50 % for US and Indian designer pages; the 2,897 held Pernia designer labels were checked page by page and 2,154 restored (GDP_1–10). Category-level ties left: about 12,000. |
| 5. Pilot page | https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk version 3: A1 opens "By scene", with "By garment" and a "Coverage" view (regions and countries against the reference); data shipped beside the page as pilot-data.json. |
| Tools | coverage_ref.py, coverage.py (ratios and flags), load_s4.py (one-step batch load), drop_excerpt_sources.py, defer_unknown_tags.py, merge_makers.py, hold_makers.py, gdp_makers.py, drop_cb_ties.py, apply_dp_s4b.py, apply_scene_decisions.py, normalise_countries.py, fix_backslashes.py; fixes to common.write_tsv (escape doubling, R-82), data_write.py (FK caching) and load_batch.py. |

Open: the remaining GD batches (verify/in/GD_*_prompt.txt without a verify/out/*_maker_kinds.tsv) and a REG_PKTR top-up were still running at the end of this log; kinds review for garments with no kind (scrubs, lab coats, wetsuits, furs, raincoats, pheran, co-ord set, Nehru/bandhgala jacket, Mandarin jacket); 103-group merge review done, homonyms kept apart; storefronts (department stores) counted as brands is an open call; Kenza Boutique's Dubai base needs a refetch; GANT (SE) and Reima (FI) country fixes need a source.

## Next (session 5)
See SESSION_5_PROMPT.md: (1) finish and load the running GD batches and REG_PKTR, re-run coverage; (2) kinds review for the garments with no kind; (3) step 6 of SESSION_4_PROMPT.md: the STAGE3_PLAN.md depth passes (D1 chip, card and laptop models; A1 signature pieces) and wave 1 (B10, C6, I1, D5, J4, J2, B3, J3), each with its reference distribution (step 2b) and the navigation rule.
