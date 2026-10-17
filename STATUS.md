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

## OWNER QUEUE
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
| 0 | Research batches CL01–06 (clothing) and PC01–05 (computers) | running |
| 1 | Memo drafts (Opus writer per category, from research outputs only) | |
| 2 | Cold review of each memo (Opus), revisions | |
| 3 | Present memos and owner decisions | |
