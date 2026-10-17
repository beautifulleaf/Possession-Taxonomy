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
