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

## Session 4, continued (2026-10-18/20) — garment depth, D1 models, wave 1
Decisions R-96 to R-100 in framework/structure/decisions/D4_residual.md.

| Work | Result |
|---|---|
| A1 garment depth | GD_WEU2_6–8, GD_LAC2_2–4, GD_EEU2_1–3, GD_SAS2_2–3, GD_MENA2_1, GD_SEA2_1 and REG_PKTR (PK 212, TR 160 brands) loaded; duplicate makers merged (auto 17; Farm/Farm Rio, Hering, Akhmadullina, Cojocaru by hand). A1 holds about 28,800 brands; category-level ties 12,000 → 11,101; no country flagged (CN 0.52, IR 0.54, CH 0.55, US 0.56). |
| D1 models | MOD_D1_1–4: about 7,000 chip, card and laptop models as named forms under the 244 D1 lines (R-70). Line and kind problems for the D1 review in verify/out/MOD_D1_*_report.md and MOD_D1_1_problems.txt. |
| A1 signature pieces | SIG_A1_1–11 over 1,281 houses: rate limits cut most batches short; about 230 named forms and 23 lines loaded so far; the batches resume from verify/work/SIG_A1_n/done.tsv. |
| Wave 1 trees | B10, C6, I1, D5, J4, J2, B3, J3 built offline and loaded (nodes; R-96 for open kinds). |
| Wave 1 harvests | HV_<CODE>_n for all eight: every worklist kind attested (B10 98, C6 63, I1 68, D5 51, J4 69, J2 70, B3 50, J3 69); named forms B10 386, C6 248, I1 1,266, D5 953, J4 2,045 (varieties), J2 38, B3 681, J3 109; about 1,900 new makers. Loader takes the category code (R-97). Missing-kind lists in verify/out/HV_<CODE>_n_report.md. Guessed URLs removed where found (J4: 19 makers set aside for the maker harvest). |
| Wave 1 references | coverage_reference_<CODE>.tsv for all eight (R-98 exports are not a market; R-99 production in tonnes is its own family; R-100 summary). |
| Wave 1 decision passes | DPW1_<CODE> (Opus, offline): B10, B3, I1, J2, J3 finished (verify/out/DPW1_<CODE>_report.md, _kinds.tsv, _moves.tsv), not yet applied; C6, D5, J4 stopped by a container restart (partial files). tools/apply_dp.py applies them. |
| Maker harvest by region | MKH_<CODE>_<NAO/EUR/ASIA/GS> prompts for all eight (verify/in/MKH_COMMON.txt); MKH_B10_NAO, MKH_C6_NAO, MKH_B3_NAO started and were stopped by the restart (partial C6 output). |

## Session 5 (2026-10-24) — wave-1 decisions, owner rulings on countries and makers, regional and clothing depth
Worked on branch `claude/stoic-ptolemy-4nctsh`. Decisions R-101 to R-110 in framework/structure/decisions/D4_residual.md.

Owner rulings this session (BRIEF.md, 2026-10-24): no country backfill, and countries never divide a category (navigation is by object type and, where scenes exist, by genre); regional maker harvests stay but per-country balancing passes go; regional harvests only where shoppers choose by maker; **maker roles** per category (way in / owner only / none, framework/structure/maker_roles.tsv): video games keep hardware makers only, groceries lead with origin and grade and show makers only through branded products.

| Step | Result |
|---|---|
| 1. Wave-1 decision passes | DPW1_C6, D5, J4 re-run; all eight applied (tools/apply_dp.py, fixed to keep existing lines and hold moves to unattested kinds). 58 lines, about 127 named forms out, 164 new kinds, all attested by HV_<CODE>_NK and loaded (B10 28 with 7 new leaves, B3 1, C6 13, D5 10, I1 10, J2 74, J3 14, J4 14). All eight chose a shopper path (R-104). |
| 2. Makers by region | Country backfill CBF_1–5 stopped by the owner (254 countries kept, R-103). Regional harvests: North America for all eight, Europe for I1, C6, D5, B3, J2, J3, Asia for I1, D5, J2, J3, plus partial runs stopped under the maker roles (B10 Europe, Asia and rest of world; B3 and C6 Asia; J4 Europe and Asia). Rest-of-world batches dropped or narrowed (R-108, R-109); J2_GS and J3_GS rewritten as branded-product harvests. About 18,500 makers added; ledger 51,198. Branded grocery products: 147 + 25 + 125 tins and caviars (J2), 88 + 96 + 385 dairy products (J3). |
| 3. Clothing | DP_A1K kinds review: 9 new kinds (scrub top, team jersey, co-ord set, firefighter suit, casual jacket, raincoat, fur coat, lab coat, braces), four wordings widened, 196 re-ties, storefront rule (100 storefronts out of the brand count) (R-105). SIG_A1_1–11 all done: about 170 new signature pieces and 20 lines. GD3 lists (15, the 1,754 never-tried category-level brands): about 1,100 brands tied at garment level; category-level-only brands 11,101 → 9,902. |
| 4. D1 review | Line kind lists rebuilt from their models (tools/fix_lines.py), L-xpg-levante, three new kinds (desktop-case PC, rack-mount server, detachable 2-in-1) with 223 models and 10 lines (R-102). |
| 5. Pilot page | tools/build_pilot_page.py covers all ten categories with their way-in questions and maker roles; A1's coverage view kept as an information report. |
| Safeguards | tools/check_batch.py (unlogged sources, reused maker ids) now runs inside tools/load_s4.py; load refused until a batch with reused ids is reviewed (verify/out/reviewed_batches.txt); tools/fix_batch_ids.py and tools/split_homonym.py for same-name makers (about 25 split: Trimble, Fig, Exact, Tekla, Esko, Lemaire, Milestone, IKA and others); id-collision guard in data_write.py (R-107); source-separator repair (R-110); fetch logs and done lists are now committed (R-101 f). |

Open: M-nika conflates three Russian firms (verify/out/open_maker_splits.tsv); 69 storefront-class makers with vague notes; clothing kinds still missing (gharara, sharara, anarkali, changing robe, cagoule, tracksuit as a set); second decision passes for the wave-1 "missing kind?" lists (MKH_*_report.md); D5 regional names owed as aliases; D5 platform rows; one D5 move waits for a B1 kind.

## Session 6 (2026-10-24) — origin and grade, second decision passes, owner rulings on busy work and "buy the best", holistic organisation of all 53 categories, clothing genres
Worked on branch `claude/blissful-hopper-oyzk13` (fast-forwarded from `claude/stoic-ptolemy-4nctsh`). Decisions R-112 to R-117 in framework/structure/decisions/D4_residual.md.

Owner rulings this session (BRIEF.md, session 6): no busy work on clothing retries, genre framing first; groceries organised around buying the best; every category re-evaluated for its best holistic organisation; decisions delegated to Claude while the owner sleeps.

| Step | Result |
|---|---|
| 1. Grocery origin and grade | Tables widened (R-112). OG_J3_EU/ROW, OG_J2, OG_J4_EU1/EU2/ROW1/ROW2, VR_J3, VR_J3_2, VR_J4_1–3, GR_J3, GR_J4 (tools/load_og.py): 973 protected designations (EU, UK, CH, TR, GE, IN, CN, JP, KR, VN, LatAm), 988 varieties and breeds, 62 grading scales; designations binding one kind became non-maker named forms (renamed with the register spelling where corrected). eAmbrosia is JavaScript-only and the Parallel tools are out of credit, so coverage outside Europe, Japan, Korea, India and China is thin. |
| 2. Second decision passes | DPW2_B3, B10, C6, D5, I1, J2, J3, J4 and DPOG_J2 applied; attestation HV_J2_NK3/NK4, HV_J3_NK2, HV_J4_NK2, HV_D5_NK2 (14 aliases), HV_I1_NK2 (25 kinds, 185 products). Kinds 1,048 → 1,178 (J4 +69 fruit and vegetables, I1 +42 incl. word processor and spreadsheet, J3 +28 incl. brined white cheese, J2 +29, C6 +21, B10 +11, D5 +6, B3 +3). Not attested for want of a seller page: oscypek, tench, stockfish, lamprey, smoked shad. 16 duplicate named forms dropped. |
| 3. Clothing | Changing robe kind (HV_A1_NK2), sharara, gharara, anarkali suit, tracksuit, shell suit as named forms, cagoule alias (R-113); M-nika split in three; SF_A1: 78 own-label, 10 storefronts, 72 unclear. RT_A1 retry stopped by the owner (R-114). Genre first: SCV_1–2 → SCV_DP added 34 genres (238 scenes), SCF_1–11 filled thin and new genres (scene tags 7,765 → about 8,700). |
| 4. Holistic organisation | HOL_EV_1–12 (evidence from retailers, specialist shops, buying guides, quality signals) and HOL_DP_1–12 (Opus) for all 53 categories; applied by tools/apply_hol.py to framework/structure/navigation/ (proposals, display groups for every built category, 125 grocery and cellar quality markers); scoped maker roles (R-116). |
| 5. Pilot page | Version 6 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk). Groups as the tree, ladder as the way in, "What makes the best" / "Who vouches" boxes, origin-and-grade panels on grocery kinds, "All 53 categories" tab. |

Open: model depth for owner-only categories (SESSION_6 step 4) and wave 2 (step 5) not started; structure flags from the proposals (R-116 d); platform rows; award and rating schemes; season attribute; SF_A1 unclear makers; the 5 unattested grocery kinds.

## Session 7 (2026-10-24) — structure decisions, quality signals, platforms, genre placement, model depth, wave 2
Worked on branch `claude/blissful-hopper-oyzk13`. Decisions R-118 to R-121 in framework/structure/decisions/D4_residual.md. The owner delegated all decisions.

| Step | Result |
|---|---|
| 1. Structure points (R-118 a, R-119) | DPH_A–J (Opus, one per domain) decided every structure_flags point of proposals.tsv: 31 new kinds in built categories, all attested (B10 9 with two new leaves, C6 6, D1 desk mat, D5 flight yoke, throttle and sim cockpit, I1 firewall, J2 anchovy and cuttlefish, J3 eight kinds split from J3.4.6.08 with 15 moves and 17 designations re-pointed, J4 dill, rosemary, sage, chives); decisions for unbuilt categories appended to each memo as section 14; traditional dress regrouped into six dress-form clusters and a "Designer houses & couture" cluster; maker roles for C5 and E4 refined; display groups updated (tools/apply_groups_changes.py). Attribute definitions (≈400) and needs (≈380 schemes, standards, platforms, scales) are in verify/out/DPH_*_attributes.tsv and _needs.tsv. |
| 2. Quality signals (R-118 b, c) | New table `attributes`. 16 schemes, 1,667 tier entries: Seafood Watch (838) and MCS Good Fish Guide (369) on J2 kinds by source and method, MSC and ASC, World Cheese Awards, Great Taste, ICDA, Slow Food Presidia (188 as non-maker named forms), AV-TEST and AV-Comparatives (130), Stiftung Warentest (32); 80 PLUS on 33 PSUs (standards); 360 season rows (UK, US, NZ, AU, JP). Blocked or thin: Guild of Fine Food lists (form-driven), CLEAResult and Cybenetics (JavaScript), Which? (paywall), part of the Slow Food site (throttled). |
| 3. Platforms (R-118 d) | 289 platforms (CPU sockets, chipsets, memory, buses, form factors, ports; 70 consoles; lamp caps and smart-lighting protocols; telescope and microscope standards; 32 lens mounts, 3 flash shoes, 26 tool battery platforms for D4 and C1) and 293 compatibility rows. |
| 4. Clothing (R-118 f, R-120) | PL_A1_1–13: about 2,600 unscened English-Wikipedia brands placed, about 15 % into genres (scene tags 8,700 → 9,334); the rest recorded as no-genre with a class (verify/out/PL_A1_*_nogenre.tsv). PL_A1_14–24 not run (R-120). Not done: re-sourcing shibu-kaji, stilyagi, sukeban, peeps, oshare kei, girly kei; genre candidates; signature pieces. |
| 5. Model depth (owner-only categories) | MODK by kind: B3 1,377 models, B10 1,643 (lists 1–3), C6 908 (lists 1–3), D5 hardware 515, I1 2,130 (lists 1–2). MODK_B10_4–5 and I1_3–4 not started. |
| 6. Wave 2 | Trees for A3, A4, A5, H1, E3, J7, B9 (TREE_<CODE>.md; R-121 adds grape brandy and molasses rum), A2 from its frozen tree; harvests HV_<CODE>_1–2: 18 categories now have kinds: 1,847 kinds (A2 63, A3 57, A4 71, A5 53, H1 102, E3 97, J7 90 of 97, B9 102 of 105), 26,187 named forms (after model depth), 1,035 lines, 57,974 makers. Same-name makers of other trades split by id at review (Omega, Sessions, Globe-Trotter, Fulton, Sons, Baccarat, Diesel, Fonseca, Toscano, Windsor, Richmond, Gravis, Moonstar); ESP duplicate merged. |
| Pilot page | Version 7 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk): 18 categories, 1,847 kinds, 26,187 named forms; makers ship in pilot-makers.json beside pilot-data.json (each under the 16 MB limit). |
| Tools | load_qs.py (QS_, PF_, PL_, MODK_ batches), split_dph.py, retire_kinds.py, append_memo_notes.py, apply_groups_changes.py, sync_designation_kinds.py, fix_node_markdown.py, fix_fetch_log_header.py (adds missing headers and moves "(Parallel)" notes out of logged URLs; run it before every load). |

Lessons: the authenticated Parallel web_fetch works (search does not) and renders JavaScript and 403 pages; agents often write fetch logs without a header or with notes after the URL (run tools/fix_fetch_log_header.py); check_batch reviews catch same-name makers of other trades; at most 20 agents run at once.

## Session 8 (2026-10-24) — model depth done, wave-2 decisions, clothing genres, quality signals, platforms, wave 3 (all 53 trees)
Worked on branch `claude/blissful-hopper-oyzk13`. Decisions R-122 in framework/structure/decisions/D4_residual.md. The owner delegated all decisions.

| Step | Result |
|---|---|
| 1. Model depth | MODK_B10_4 (431), B10_5 (123), I1_3 (526), I1_4 (638) loaded: step done. |
| 2. Wave-2 decisions | DPW1_A2, A3, A4, A5, H1, E3, J7, B9 applied (new kinds, 100+ lines, drops and moves; A5.5 leaves; six beer leaves); HV_W2_NK1–3 attested 73 of 76 new and tree kinds (not attested: maize beer, strong cider, palm or sap wine). HOLW_1: display groups and quality markers for A2, A3, A4, A5, B9, E3, H1, J7, J1, J5, J6 (J7.3.1.06, J7.4.04, J7.4.06 not yet in a group). DPMK_1 (missing kinds named by the MODK, QS and wave-3 reports): 127 kinds added, 54 to attest; 13 microscope objective series as lines (R-122 g). |
| 3. Clothing | SCR_1–2: 11 genres added (scenes 239 → 249), 152 brand tags (9,486). |
| 4. Quality signals | QS_J7_1 (1855 Médoc and Sauternes, Saint-Émilion 2022, Graves, Cru Bourgeois 2025: 359 entries; 33 Burgundy grands crus as designations), QS_J7_2 (DWWA, IWC, IWSC, SFWSC, WWA, World Beer Cup, European Beer Star, IWC Sake, Kura Master: 178), QS_J2_3 (17 Seafood Watch changes since Feb 2024), QS_J3_3 (113 World Cheese Awards, partial: gff.co.uk blocked), QS_W2_1 (FiFi, Art and Olfaction, Allure, GPHG, Red Dot, TEC, SOS: 114), QS_SEASON_2 (48 season rows; none for South Africa or Brazil). Schemes 17 → 36, tier entries 1,667 → 2,448. |
| 5. Platforms | PF_5 (OS, app stores, hive systems, heated-tobacco systems), PF_6 (razor, brush-head and shaver systems, Eurorack, MIDI, 500-series, watch calibres, string gauges), PF_7 (129 compatibility rows for D5, B3, C6 models): platforms 289 → 378, compatibility 293 → 454: step done. |
| 6. Wave 3 | Trees for all 35 remaining categories (TREE_<CODE>.md, loaded with tools/load_tree.py): every category now has nodes. Harvested and loaded: J1, J5, J6, I2, I3, C2, C3, C4, D2, D3, B6, B7 (12 categories). Harvest prompts written, not run: B1, B2, B4, B5, B8, C1, C5, C7, C8, D4, E1, E2, E4, F1–F6, G1, G2, H2, H3 (verify/in/HV_<CODE>_<n>.prompt.txt, from tools/hv_prompt.py). |
| 7. Pilot page | Version 8 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk): every category with kinds (2,937 at publish). |

Totals now: 30 categories with kinds, 3,099 kinds, 32,164 named forms, 1,415 lines, 60,305 makers, 1,006 designations, 36 schemes, 2,448 tier entries, 378 platforms, 454 compatibility rows, 414 attributes, 249 scenes, 9,486 scene tags.

Tools: tools/hv_prompt.py (wave-3 harvest prompts), tools/drop_stored_makers.py (run before every load). Lessons: harvest reports must be saved as files (the wave-3 prompts require it); agents still guess URLs now and then (logged as failed, unused); a maker id reused from another trade must be split before load (check_batch).

## Session 9 (2026-10-24) — wave-3 harvests done, decision passes for every wave-3 category, display groups for 52 categories
Worked on branch `claude/blissful-hopper-oyzk13`. Decisions R-123 in framework/structure/decisions/D4_residual.md. The owner delegated all decisions.

| Step | Result |
|---|---|
| 1. DPMK_1 kinds | HV_MK_NK1–3: 51 of 54 attested (snoek and komatsuna not; wreckfish later). Pending moves re-applied (DPMK_1_C6 done after B8; DPW1_B9 keeps 5 to_line moves waiting for owner-maker rows). J2.1.1 closed to new finfish: six family leaves J2.1.5–J2.1.10 (R-123 b). |
| 2. Wave-3 harvests | All 43 HV_<CODE>_n run and loaded (B1 B2 B4 B5 B8 C1 C5 C7 C8 D4 E1 E2 E4 F1–F6 G1 G2 H2 H3): every one of the 53 categories now has attested kinds. |
| 3. Decision passes | DPW1_<CODE> with verify/in/DPW1_W3_ADD.txt for 34 wave-3 categories (all but F5), applied with tools/apply_dp.py; new leaves via tools/add_leaf_nodes.py; kinds held for a page check when the only evidence was a harvester note. Attestation HV_W3_NK1–4 (26 + 19 + 25 + 18). Display groups and markers HOLW_2A–D for 38 categories (B1 B2 B4–B8, C1–C5 C7 C8, D2–D4, E1 E2 E4, F1–F4 F6, G1 G2, H2 H3, I2 I3) applied with tools/apply_hol.py; 33 J7 kinds placed in J7 groups (incl. J7.3.1.06, J7.4.04, J7.4.06); late kinds placed with their leaf siblings (GRP_S9_1–5). |
| 4. Left from session 8 | Not started except maize beer, strong cider and palm wine attestation (strong cider attested; maize beer no seller page; palm wine source not usable). |
| 5. Pilot page | Version 9 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk): all 53 categories, 5,992 kinds. |

Totals now: 53 categories with kinds, 5,992 kinds, 39,153 named forms, 2,330 lines, 63,510 makers, 1,006 designations, 36 schemes with 2,448 tier entries, 378 platforms, 454 compatibility rows, 414 attributes, 249 scenes, 9,486 scene tags; display groups for 52 categories (F5 has none yet).

Lessons: a batch that reuses a stored line id with another name made the whole lines write fail, so the loader helper now drops such rows before load (the stored row is kept); batches named HV_W3_* or HV_MK_* get a bogus category-level tie and their maker_kinds must be loaded with tools/data_write.py directly; agents sometimes claim to reuse a maker id that does not exist (add the row); decision-pass new leaves need the parent column "<id> <name> (new leaf)" before apply_dp.py and add_leaf_nodes.py.

## Session 10 (2026-10-24) — F5 finished, clean-up, depth (coins, notes, stamps, minerals, climbing, hockey), signature pieces, quality signals and platforms for wave 3
Worked on branch `claude/blissful-hopper-oyzk13`. Decisions R-124 in framework/structure/decisions/D4_residual.md. The owner delegated all decisions.

| Step | Result |
|---|---|
| 1. F5 | DPW1_F5 applied (7 new kinds, 6 e-money cards moved, NCMC line); 212 transit, bank, telecom and retail "makers" moved to the issuer ledger (tools/makers_to_issuers.py, R-124 a); HV_F5_NK1 attested 2 of 3 (social security card not); display groups and markers HOLW_F5 (25 groups, 20 markers): every category now has display groups. |
| 2. Clean-up | 16 maker merges, 4 line twins (tools/merge_lines.py), IKEA line gaps and 61 same-name line links (tools/link_line_names.py, tools/fix_lines.py), 40 single-kind lines to named forms (tools/lines_to_named_forms.py), 23 VALORANT bundle lines dropped, Fifty Shades (Lovehoney, licence) and Colt Defender (Umarex, licence), B9 owner lines TEREA, LEVIA, Copenhagen, Grizzly, Skoal (MK_S10), five definition widenings, scheme kinds_served synced (tools/sync_scheme_kinds.py). |
| 3. Depth | DEP_F3_1–4: 341 coin, bullion, banknote and stamp issues as non-maker named forms with 338 issuers; DEP_F6_1–2: 334 mineral species kinds (Strunz leaves); D4 camera battery platforms (PF_8; lens-hood mounts not attestable); DEP_E2_1: 26 caving and climbing kinds, 96 models; DEP_E2_2: new leaf E2.14.5 hockey, 15 kinds, 52 models; HV_W3_NK5 attested 19 of 24 retry kinds; DPS10 + HV_S10_NK1: 29 more kinds (R-124 k). |
| 4. Left from session 8 | SIG_A1_12–27 (646 scene-core brands): about 130 signature pieces, 20 scene tags (low yield, R-124 j); WCA (QS_J3_4, 16 entries), Allure 2026 (QS_W2_2, 28), DWWA Platinum and IWSC Gold 2026 (QS_J7_3, 186): partial (R-124 m); seasons for South Africa and Brazil (QS_SEASON_3, 110 fruit and vegetable rows; no fish calendars found); wave-3 needs: QS_W3_1–6 (45 schemes, 87 standards rows incl. supplement and safety seals, 56 grading scales, 95 tier entries, 41 standard values) and PF_8–9 (242 platforms, 72 compatibility rows). |
| 5. Pilot page | Version 10 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk): 6,421 kinds, 40,174 named forms; issued named forms show "Issued by". |

Totals now: 53 categories with kinds and display groups, 6,421 kinds, 40,174 named forms, 2,293 lines, 63,544 makers, 338 issuers, 1,006 designations, 988 varieties, 119 grading scales, 81 schemes with 2,768 tier entries, 90 standards with 74 values, 620 platforms, 526 compatibility rows, 524 attributes, 249 scenes, 9,506 scene tags.

Lessons: Sonnet agents given 160-brand lists stop after 10–30 brands; lists of 40 finish. Batches that add kinds and named forms together need the loader to re-read kinds (fixed in tools/load_qs.py, which now also loads kinds, issuers and grading scales). Parallel fetch hit its free-tier rate limit late in the session.

Still unattested: two-wheel tractor, crown of office, home audio recording, restraint furniture, riding saddle machine, social security card.

## Next (session 11)
See SESSION_11_PROMPT.md (the last hand-off: when its steps are done, hand-offs stop).

## Session 11 (2026-10-24) — last hand-off list: award results, last attestation attempt, last signature pass, pilot page version 11
Worked on branch `claude/blissful-hopper-oyzk13`. Decisions R-125 in framework/structure/decisions/D4_residual.md. The owner delegated all decisions.

| Step | Result |
|---|---|
| 1. Award results (R-124 m) | DWWA 2026 Platinum: QS_J7_4 placed 52 more and HV_S11_NK3 14 more on fourteen new single-grape kinds (Blaufränkisch, País, Prokupac, Refošk, Aleksandrouli, Altesse, Kisi, Albillo Mayor, Petite Arvine, Savagnin (Heida), Loureiro, Friulano, Falanghina, Pecorino): 165 of 196 stored; the other 31 have no colour or grape on Decanter's page (R-125 b). M&S own labels are issuer-owned (I-marks-and-spencer, R-125 a). Allure Best of Beauty 2026: one batch per category page (QS_W2_3–8) plus HV_S11_NK2: 145 of 319 winners stored (was 28); Allure's pages give only fragments through the Parallel fetch and K-beauty, nails and under-$24 gave nothing. Eighteen new kinds attested for the skipped winners (face mist, acne spot treatment, pimple patch, facial skin-care device, facial razor, highlighter, contour, makeup sponge, leave-in conditioner, detangling spray, scalp scrub, scalp treatment, dry shampoo, hair mousse, hair gel, texturizing spray, volumizing spray; B2.6.09 hair towel; R-125 f). World Cheese Awards: QS_J3_5 found two more levels (Cypress Grove 2024); no page lists levels, so the item is closed. |
| 2. Unattested kinds (R-125 c) | HV_S11_NK1 attested crown of office, restraint furniture, riding saddle machine and social security card (issuer: Social Security Administration). Two-wheel tractor (no page shows a Category 1 three-point hitch) and home audio recording (every listing fetch failed) are retired: framework/structure/retired_tree_kinds.tsv. |
| 3. Signature pieces (R-125 d) | SIG_A1_28, 40 weak negatives with their own sites fetched: 10 signature pieces (Polo Ralph Lauren polo shirt, Thom Browne 4-Bar cardigan, True Religion Ricky and Billy jeans, Westwood Mini-Crini, Mary Quant Georgie dress, Angelic Pretty Milky Way JSK, BABY Waist Ribbon JSK, Tommy Hilfiger flag denim jacket, Charles Tyrwhitt non-iron twill shirt) and the Trapstar Irongate line; 30 brands none found. The clothing signature pass is closed. |
| 4. Pilot page | Version 11 published (https://claude.ai/artifact/69ipGh4sxukS45bxkDoSEk): 6,457 kinds, 40,389 named forms; pilot-data.json 15.6 MB (under the 16 MB limit). |

Totals now: 53 categories with kinds and display groups, 6,457 kinds, 40,389 named forms, 2,294 lines, 63,647 makers, 340 issuers, 1,006 designations, 988 varieties, 119 grading scales, 81 schemes with 2,953 tier entries, 90 standards with 74 values, 620 platforms, 526 compatibility rows, 524 attributes, 249 scenes, 9,506 scene tags.

Left open, not planned (no busy work): Allure winners beyond what the JavaScript pages yield (Odele Air Dry Styler unplaced: a gel-serum styler between kinds); 31 DWWA Platinums without a stated type; Rogaine (a medicine, out of H1).

## Hand-offs stop
Every step of SESSION_11_PROMPT.md is done; no SESSION_12_PROMPT.md is written and no new session is started. The next session starts only when the owner asks for one (owner queue: review R-120 to R-125, the delegated decisions).

## Session 12 (2026-10-24) — readability: shop departments, plain names and a reader page for all 53 categories
Owner: "the challenges now are in fact readability and that it's organized how it should be"; a sidebar within categories and the categories as top navigation, as the Culinary and Pleasure pages; no sideways scrolling; "delegate to other models if you think it's ok for less usage". Decisions R-126 and R-127.

| Step | Result |
|---|---|
| Rules | framework/structure/navigation/READABILITY_RULES.md: one shop name per kind (synonyms to also_called), sentence case, departments as the category's shops split them (checked on fetched retailer pages), five to nine departments, no shelf of one, plain reader descriptions where a definition cites codes or working terms. The display layer never changes the tree: framework/structure/navigation/display.tsv (new), groups.tsv and markers.tsv, written only by tools/apply_readable.py (checks every kind sits in exactly one group). |
| C1 exemplar | Tools rebuilt on nine shop departments led by power tools, hand tools and workshop machinery (Toolstation, Bunnings), replacing job-based groups that mixed hand saws with table saws. |
| Rollout | 52 categories reviewed by Sonnet agents (verify/in/RD_COMMON.txt; outputs verify/out/RD_<CODE>_*), each checked and applied; every category now has 5–9 departments and every kind a shelf. Markers may now serve several departments or a whole category. |
| Test | Blind findability test (Haiku request writers and finders, names only, two shelves at most): 620 of 636 requests found (97.5 %), 549 on the first shelf; three shelving faults fixed. C1 old-versus-new test with Sonnet finders: both layouts found 59–60 of 60, so agent finders guard against regressions rather than prove a gain. |
| Reader page | https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n (tools/build_reader_page.py, tools/reader_template.html; pages/reader.html with pages/reader/<CODE>.json): domain row and category row at the top, departments and shelves in a sidebar, search across all categories, "What makes a good one" per department or category. The stage-3 pilot page stays as the working view with sources. |

## Owner queue (session 12)
verify/out/RD_decision_queue.md: items that may belong in another category (holster, replica weapons, kratom and other non-tobacco plant products in Smoking & Vaping, eFoils and hoverboards in Vehicles, casino machines in Toys & Games, and others), possible duplicates, five categories without quality markers (Clothing, Lighting, Animal Equipment, Optical & Scientific Instruments, Video Games), loose-fit placements and categories whose departments rest on no fetched shop page.

## Next
Owner reads the reader page and the queue; moves between categories change the tree and go through a decision pass (R-item) before the display layer follows. The Clothing scene view (genre first, R-71) is not yet on the reader page.

## Session 12, continued — decision queue, clothing scenes, final page, main
| Step | Result |
|---|---|
| Queue | R-128: three kinds moved to their shops' category (holster, studio backdrop, cabinet humidor; tools/move_kinds.py), one duplicate merged (CO2 launcher into pepper-ball launcher; tools/merge_kinds.py), 71 plain-word quality markers for Clothing, Lighting, Animal Equipment, Optical & Scientific Instruments and Video Games; the other flags stand where stage-2 boundary rules put them. |
| Scenes | Clothing opens by scene on the reader page (20 groups, 233 scenes, 9,486 brand placements, signature pieces), by garment on a toggle. |
| Final page | The Possession Taxonomy: https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n (6,456 kinds in 53 categories). |
| Branches | main now holds everything: this branch merged with main, claude/stoic-ptolemy-4nctsh and claude/adoring-gates-42vva3 (their files are all present here in later versions; histories kept, nothing rewritten). |

## Session 12, continued — granularity (R-129)
| Step | Result |
|---|---|
| Splits | GR_<CODE> reviews for all 53 categories: 286 new kinds, each attested on a fetched shop page (fidget toys into spinners, pop-its, cubes, squishies and the rest; lettuce, onion, tomato, cabbage; crab species; rigid trucks). Named forms re-filed; old kinds kept as "Other …" or the general type. |
| Cards | GC_<CODE> card passes for all 53: 81 cards over 207 kinds that shops sell as one item with options (table saw, bench plane, mattress, kitchen bin, baler…), shown as one card with a "Types" line. 5 proposed cards dropped at integration (hot tub, vaporizer, toy train, accordion, sake). |
| Page | "Where this was checked" and "Where this scene is described" links removed. Reader republished: 6,742 kinds; every live kind on one shelf with a display row. |
| Open | Undecided splits the reviewers left for lack of a fetched shop page are listed in verify/out/GR_<CODE>_report.md (e.g. makeup and hair brushes, melons, potatoes, special-purpose vehicles). |

## Session 13 (2026-10-31) — one line of work: the rebuild joins main
- The live artifact (https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n, v28) was built from branch `claude/toy-organization-system-mapqhu`, whose history is unrelated to main's. Merged into main keeping main's files and adding `rebuild/` (all of it), the AUD3 audits and FIX/E1PZ prompts, and the 2026-10-28 owner decisions in BRIEF.md. Both histories are kept; nothing rewritten.
- From here the live taxonomy is `rebuild/` (57 categories, 7,811 kinds at v28): start with rebuild/HANDOVER.md, rebuild/RULES.md (binding owner rules), SCHEMA.md, FINDINGS.md. CLAUDE.md updated to say so. data/*.tsv and tools/ are the frozen stage-3 pipeline.
- Framework v0.8 (framework/CATEGORIES_v0_8.md, framework/key_v0_8.json): the 57 rebuild categories, each with a membership test and precedence sentences, a 62-question placement key and a change table against v0.7.1. The reader page shows it under "How to place" and on each category ("Belongs here", "Key to this category").
- Structure pass STR (verify/in/STR_COMMON.txt, owner: a shelf should read like Culinary's Stews): every department gets a test and an axis, every shelf a definition and an axis, types grouped by named axes (`tt`), generic archetypes demoted, missing kinds added against a fetched reference per shelf, cross-links (`see`). Pilot E1 done (fidgets by what the hand does); rollout to the other 56 categories running.

## Owner queue (session 13, from framework v0.8)
1. BRIEF.md scope still says all animals are out; RULES.md makes living animals possessions via a breeds register. v0.8 follows RULES. Confirm the BRIEF line is superseded.
2. With titles out, I2 has no shelf for bought e-books, music, film or game downloads: out entirely, or format-only kinds?
3. Meat alternatives: FINDINGS says J3, the data keeps a J1 department. v0.8 follows the data. Which?
4. Single trading cards sit in both E1 and F3 (two views by rule). Which is the home?
5. Archery: bows and accessories in E4, quivers and bow slings in E2. Which?
6. Duplicates across categories (trail camera D4/E2, pond pump B10/C2, toiletry bag A4/H1, brewing yeast C3/J5, charcoal C2/C8, magnifiers E6/H2): apply v0.8's proposed precedence and keep one home each?
7. Portable power station has no home (B7 is air only, home battery is G3): C1 or D2?
8. Portable saunas and inflatable hot tubs in G3 (built-in rule) although movable: keep?
9. Fresh ready-to-eat food (sandwiches, salads, takeaway): in J5, or out as dishes?

## Session 13, continued — structure pass STR done for all 57 categories (artifact v30)
| Step | Result |
|---|---|
| STR pass | One Sonnet agent per category (verify/in/STR_<CODE>.prompt.txt over STR_COMMON.txt; reports rebuild/out/STR_<CODE>_report.md). Every category has `ax` and a placement `key`; every department `t` and `ax`; every shelf `t` (and `ax` above 3 kinds); 7,892 kinds have hand-written type groups (`tt`). All 57 files pass `validate.py --v3`. |
| Totals (v28 → v30) | departments 488 → 503; shelves 1,362 → 1,819; kinds 7,811 → 8,892; archetypes 18,649 → 16,758 (generic ones demoted to types, models or ranges); models 17,313 → 20,702; cross-links 0 → 1,823. |
| Restore pass | The agents dropped versions of demoted archetypes; tools/restore_lost.py put 1,685 concrete names back as models from the pre-pass backups. 58 could not be placed and 831 maker-less generic patterns were left out on purpose (rebuild/work/_restore/<CODE>.tsv). |
| Coordinator fixes | In-game currency kind removed from I2 (stored value is out); 16 cross-links retargeted after renames (tools/see_check.py, fix_see_links.py); 6 same-name different objects renamed apart and 4 same-object pairs linked (tools/fix_homonyms.py); merge.py folds moved-in kinds into kinds an agent merged or renamed (out/<CODE>_renames.json). |
| Page | Codes on departments, shelves and kinds; "Belongs here", "How it splits" and "Order" lines; grouped types; See-also links; per-category key; "How to place" view (framework v0.8); models are searchable. https://claude.ai/artifact/C1cQq1ygVd7bWfw7Duem6n v30. |

Known weak spots (from the reports): Firecrawl and Parallel ran out of credit, so coverage checks used WebFetch summaries, mostly Wikipedia; many shelves have no whole-space reference (listed per category in the STR reports); some type lists come from general knowledge; producer houses in J2 went to models instead of ranges; Strunz placements of four F6 minerals to spot-check; jacks and hoists (G1) may belong in C1.

## Next
Owner reads v30 and the session-13 owner queue above. Suggested follow-ups: retailer-page coverage checks for the shelves the reports list as unchecked once a fetch tool has credit; place the 58 unplaced restored names; a blind findability test on the new structure.

## Session 13, continued — named-entry standard (owner discussion)
Owner decisions recorded in BRIEF.md ("Owner decisions 2026-10-31"). Pilot ARC_E5 (video game consoles) published as artifact v31–v32.
Next: write the v4 brief (named-entry standard + market layer + No & low), then pilots in this order: J9 Soft Drinks & Water (market layer), J7 Wine, Beer & Spirits (appellations, styles, distilleries, No & low), A1 Clothing (patterns + brand market), then roll out by treatment group.
