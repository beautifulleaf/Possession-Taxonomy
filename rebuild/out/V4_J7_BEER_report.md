# V4_J7_BEER report: Beer, market-first

File: rebuild/out/J7_parts/BEER.json (1 department "Beer", mode tier; 29 kinds; 464 entries, 537 versions; 99 owners added to the brand register; 0 moves). `validate.py --v3` on the wrapped part: OK. Build script, backup and sources.tsv are in rebuild/work/V4_J7_BEER/.

## Structure
Shelves: Global groups (AB InBev 72 entries, Heineken 48, Snow 16, Carlsberg 37, Molson Coors 48, Tsingtao 1, Asahi 19, Kirin 7); National & regional (8 world regions, 52); Independents (Europe, Americas, Asia/Africa/Oceania, 50); Craft & indie (US 62 = the whole Brewers Association 2024 top 50 plus earlier craft entries, Belgium 18, Britain and Ireland 19); Own label (Aldi, Josephsbrau, Kirkland Signature, Mountain Brew); plus the six traditional-brew kinds kept as a last shelf (Sorghum, Millet, Maize, Banana, Rye, Sahti).
Every old style kind is in `renames` (77 kinds) or kept; none dropped. Style canon: BJCP style on each carried version and in `tt` of each kind. Before: 157 entries and about 250 loose models; after: 464 entries.

## References (fetched 2026-10-31; full list in sources.tsv)
VinePair top-40 brewers 2024, Brewers Association 2024 lists, 24/7 Wall St AB list, Punch own-label article, and about 30 Wikipedia pages (group brand lists and Beer in <country>).

## Market facts (`ms`, 35 rows)
Group volumes 2024; shares for India, Brazil, China, Vietnam, Thailand, Philippines, Australia, Canada, Asahi in four European markets (2005 to 2023); US as Brewers Association ranks.

## Alcohol-free versions (coordinator request), `alc` set from fetched pages
alcohol-free: Heineken 0.0, Guinness 0.0, Bavaria 0.0, Beck's Blue (0.05 %), Peroni Libera and Nastro Azzurro 0.0, Corona Cero, Budweiser Zero (0.00 %), Asahi Super Dry 0.0 and Asahi Dry Zero (0.00 %), Kirin Zero ICHI (0.00 %), Carlsberg 0.0, San Miguel 0,0, Stella Artois 0.0, San Mig Zero. De-alcoholised: Erdinger Alkoholfrei (under 0.5 %), Clausthaler Classic (0.45 %, SRF report). Low: Budvar Free, Sapporo Super Clear (as old/page text says).
Not stated by their pages: Corona Cero, Budweiser Zero (Fox), Heineken 0.0 on Wikipedia; levels came from the other fetched pages listed in sources.tsv. The SRF page names Heineken as Clausthaler's maker; the earlier record and my entry say Radeberger Gruppe, so check.

## Could not be sourced / caveats
- Many German, Belgian and British carried entries keep sources from earlier passes; owner and tier left blank where no fetched page states them (national shelf and British kind).
- Only the US has a ranked craft list; Belgian and British craft kinds are the earlier selection, tier set to "Craft & indie" by judgement.
- Not reached: Lidl and Tesco own label, Japanese and Korean market shares, Mexico 90 % duopoly (no year), Carlsberg page tail, Nigeria (404), Brewbound and Aldi pages (403).
- Alkoholfrei versions of Reissdorf, Früh, Bitburger, Augustiner, Paulaner, Jever carried without `alc` (no page states a level).
- Kona is under AB InBev per the AB list but ranked in the BA craft list; kept in craft with own AB InBev.
- 214 loose models (and 3 ranges) whose brewery has no entry were removed as out of scope (list: rebuild/work/V4_J7_BEER/dropped_models.json); 135 became versions of their brewery's entry.
