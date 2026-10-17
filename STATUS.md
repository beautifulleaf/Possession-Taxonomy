# Possession taxonomy — status

## Session 1 (2026-10-17) — Stage 1: top-level categories
Search cap: `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` = 100000. Test WebFetch (Google Product Taxonomy file) and Parallel web_search (Getty AAT) both work.

| Phase | What | State |
|---|---|---|
| 0 | Scaffold repo (CLAUDE, BRIEF, settings, layout) | done |
| 1 | Harvest source classifications H01–H06; collect probe items P01–P04 | done: 4,007 source nodes (data/source_nodes.tsv); 438 probe items (data/probes.tsv: 300 round 1, 138 round 2) |
| 2 | Draft category framework v0 | done: framework/CATEGORIES_v0.md (9 domains, 37 categories, 27-step key); frozen copy audit/CATEGORIES_R1.md |
| 3 | Blind placement round 1 (BP1 A–C), source crosswalk (CW01–04), cold audit (AU1); fixes; round 2 on fresh items | running |
| 4 | Close: results, owner queue, stage-2 memo template | |

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
