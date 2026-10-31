# V4_J9 report: Soft Drinks & Water, market layer pilot

Files changed: rebuild/out/J9.json, J9_brands.json (160 -> 1,170 brands and owners). J9_renames.json and J9_moves.json unchanged (no kinds merged, none moved to another category). Backups and the build script are in rebuild/work/V4_J9/. `validate.py --v3`: OK (91 kinds, 973 entries). Entries went from 169 to 973.

## Entries per kind (before -> after)
Waters: natural mineral 12 -> 77, spring 5 -> 18, artesian and glacier 2 -> 3, purified 3 -> 13, sparkling mineral 14 -> 19, flavoured sparkling 3 -> 10, flavoured still 0 -> 4, alkaline and functional 1 -> 2.
Sodas: cola 7 -> 97, fruit soda 2 -> 283, orange 7 -> 39, lemon-lime 3 -> 21, citrus 2 -> 8, root beer 3 -> 18, ginger ale 5 -> 15, guaraná 1 -> 11, sparkling lemonade 4 -> 13, apple 2 -> 9, cream soda 0 -> 3, others smaller.
Other: juice drink 3 -> 44, energy drink 7 -> 77, sports 6 -> 13, functional 1 -> 18, iced tea 3 -> 18, canned coffee 3 -> 13, kvass 2 -> 8, malta 3 -> 7, lactic 2 -> 7.
Four existing entries moved kind to follow the flagship product named on the fetched list (Irn-Bru to citrus soda; Inca Kola, Colombiana, Big Red to fruit soda). No former models existed in J9.

## References (all fetched 2026-10-31, logged in sources.tsv)
Wikipedia: List of soft drinks by country (whole page, three reads), List of bottled water brands, List of Coca-Cola brands (A to S plus tail), List of PepsiCo brands, Keurig Dr Pepper, List of brand name soft drink products, Craft soda; The Daily Meal craft-soda list. "List of cola brands" returned 404, so cola follows the other lists. Each kind with entries carries `nl`, `sel`, `xg` (country); each entry carries `g`, `own`, `cty`, and `tier` where an owner is stated.

## Market facts (department `ms`, with `msum`)
- US soft drinks 2008: Coca-Cola 42.7 %, PepsiCo 30.8 % (Pepsi page, quoting Beverage Digest).
- US 2024: only share changes were on a fetched page (Coca-Cola +0.4, PepsiCo -0.7 volume points, nine months); Dr Pepper tied Pepsi for second in regular soda (June 2024).
- India: Thums Up 85 % (1993), Pepsi about 15 % (2012). Peru: Inca Kola 26 % against Coca-Cola 25.5 % (2012); 32.9 % in 1995. Russia 2005: Coca-Cola 19.4 %. Japan: Coca-Cola 22.4 %, Suntory 17.1 % (2018 article). Middle East about 2003: Pepsi about 75 %. Scotland: Irn-Bru ranking, no figure.
- Craft soda: 1 % of US soda in 2015; world value USD 537.9 million in 2016.
- Energy: Red Bull 13 % global (2023); Monster 39 % (2020, conflicting definition); US convenience/gas, four weeks to 20 July 2024: Monster 34.7 % (36.7 % with Bang), Red Bull 35.9 %, Celsius 7.9 %.
- Water: bottled water about 25 % of US consumption (2022); Primo Brands "number one" (2024, no figure); India top five 67 % (2013).

## Could not be sourced
- Owner's figure not used: no fetched page states a current US company share for Coca-Cola, PepsiCo or Keurig Dr Pepper (Beverage Digest text is paywalled; Visual Capitalist returned 403). The 2024 levels (about 40, 27, 24.5) appear only in search excerpts, so they are not recorded.
- Markets covered: about 8, not 20; no fetched share figures for Brazil, Mexico, Germany, UK, China, Nigeria, South Africa.
- Tier is blank on 429 entries where the list names no owner (own and tier left empty rather than guessed). National champion is set only for Irn-Bru, Inca Kola and Thums Up, where fetched pages support it.
- Entry `y` (year) is blank for new entries; founding years were not on the lists. `own_y` only for Thums Up, Inca Kola (stake), Big Red, CORE, Innocent, Ghost, Green River.
- Coca-Cola brand list was read A to S plus the tail, so its portfolio is partial. Fruit soda (283) is the default kind for unspecified national sodas and should be split later. Placement of brands with no stated type is a judgement.
- Syrup, cordial, squash and fermented kinds gained few entries (no list covers them); kombucha brands barely appear.
