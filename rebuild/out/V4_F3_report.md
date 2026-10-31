# V4_F3 report: Coins, Stamps, Medals & Trading Cards

Validation OK (108 kinds, 1,046 entries). Backups, scripts and sources.tsv are in rebuild/work/V4_F3/.

## Per kind, entries before -> after (references)
- Bullion coin 16 -> 62: every series in Wikipedia's List of bullion coins (gold, palladium, platinum, rhodium, annual and limited silver), by country; metals as versions. Bars 5 -> 7, rounds 3 -> 5 (no whole-space reference).
- Circulation coin 20 -> 63; commemorative 9 -> 25: series by issuer from Wikipedia coin and currency articles for the US, UK, euro area, Canada, Australia, Japan, Mexico, Brazil, Russia, South Africa, India, China, Switzerland.
- Circulation banknote 11 -> 41: adds South Africa, Russia, Brazil, India series; commemorative 2 -> 6, collector 0 -> 5.
- Definitive stamp 23 -> 75, error and variety 7 -> 24, commemorative 2 -> 9, revenue 5 -> 12, official 2 -> 3: Wikipedia's List of notable postage stamps, all rows placed by type.
- Orders 16 -> 61, gallantry and merit 17 -> 63, campaign 12 -> 31, long-service 4 -> 6: UK, US, France, Soviet Union and Japan lists; Germany's page is only an index (two entries).
- Cards: Base card 16 -> 45, tobacco/candy renamed "Vintage tobacco, candy and food card" 3 -> 14 (Wikipedia Baseball card article); new kind "Trading-card game set" 211 entries (Pokémon sets by generation from the first to Mega Evolution; Magic core sets and 250-card-plus expansions); singles 6 -> 3 (sets moved).
- Grading services stay in the register (already in F3_brands.json).

## Loose models (m)
All m lists are now empty. Maker-named models were promoted to entries (about 110, sourced to the kind's earlier catalogue page); unnamed generic ones were dropped as out of scope (about 70, e.g. "Siege notes", "Casino chip (cheque)", "Gold Swan", 12 unlisted British campaign medals such as Afghanistan Medal).

## Market layer
Not applied: F3 is canon-led, not market-shaped; no `ms`, `own` or `tier` fields were added. New issuers and publishers (about 26) were added to F3_brands.json; one rename in F3_renames.json; F3_moves.json unchanged.

## Could not be sourced or not covered
- Beckett's Topps history gave 403 and a 404 on Firecrawl, so the full Topps year-by-year run is missing.
- Circulating coins and banknotes cover 13 issuers (not 20); the Middle East, other Africa, Korea, Turkey and the rest of South America are missing.
- The UK and US medals pages were truncated at 100,000 characters; UK campaign medals and US foreign awards were not read. Medals of Germany, Italy, Austria and others are not covered.
- Definitive series beyond the earlier pass were not fetched; some entries lack years the page did not give.
- Pokémon HeartGold/SoulSilver sets lack years; Magic sets under 250 cards are out of scope.
