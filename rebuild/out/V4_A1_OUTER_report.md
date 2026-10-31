# V4_A1_OUTER report

Part file: rebuild/out/A1_parts/OUTER.json. Replaces Coats & jackets; Suits & formalwear; Workwear & uniform clothing (54 kinds). Validates OK (0 errors, 291 archetypes). Nothing renamed or moved. Scenes untouched.

## Entries
Before 154 -> after 291 across 54 kinds. Biggest: Overcoat 8->17, Business suit 8->17, Tie 6->15, Cape 5->12, Raincoat 4->11, Biker jacket 7->12, Puffer jacket 8->12, Shell jacket 8->11. Kinds still empty: Coach jacket, Cut-off vest, Chef's jacket, Scrub top (no fetched garment article names a brand or type list; no register piece matches).
Every entry has `g`: brand home country, then brand, then year; "Named forms without a brand" last (103 forms, 188 brand pieces). 18 `role` origin badges, each per a fetched page (Burberry, Aquascutum, Mackintosh, Levi's Type I, Baracuta G9, Eddie Bauer Skyliner, PolarFleece, Peter Storm cagoule, Castell & Son necktie, Brooks Brothers ready-to-wear suit, Lady Margaret Boat Club jacket, Henry Poole dinner jacket, others). Each kind has `nl`, `sel` with coverage line, `xg`.

## References
43 Wikipedia articles fetched (list in rebuild/work/V4_A1_OUTER/sources.tsv), e.g. Trench coat, Overcoat, Parka, Flight jacket, Raincoat, Down jacket, Polar fleece, Suit, Tuxedo, Necktie, Overalls, Boilersuit, Chore jacket, Donkey jacket, Mackinaw coat. Plus the register (2,531 brands): every sig/lines piece whose garment matches a kind.
Not read in full: Suit (read 100,000 of 168,380 characters), Tuxedo (of 190,725), Necktie (of 157,287), Morning dress (of 142,835), Waistcoat (of 110,474), Mackinaw coat (of 106,937). Those kinds' `sel` say so. Where I stopped: after these six first windows and the garments listed; no offset windows were fetched (about 43 fetches used of 60).

## Loose models (`m`): 145 removed or folded
27 register-confirmed models became entries (e.g. Arctic Parka, Roadmaster, Dominator, Service Pant). 116 retailer-page SKUs with no register signature piece were removed as out of scope (Gloverall, Aspesi, REI, Ellesse, Sergio Tacchini track tops, coach jackets, etc.). Schott 613/618/118 and the Jacquard jacket became versions.

## Sourcing caveat
Entries from the register carry the brand page (`s`) from the earlier brand pass; I did not re-fetch those pages, and many have empty `d` (51 entries) because no fetched fact names the piece. Military forms (A-2, G-1, M-65 etc.) are kept as named forms; E4 see-notes added on Flight, Field and Deck jackets.

## Market
`cty` on all 188 brand entries. `own`, `tier`, `own_y` only for 12 brands whose register description states the owner (VF Corporation/The North Face 2000, Napapijri 2004, Moncler/Stone Island 2020, Amer Sports/Arc'teryx, Shandong Ruyi/Aquascutum, Yagi Tsusho/Mackintosh, DAKS/Sankyo Seiko 1991, etc.). No fetched market-share figure for outerwear, tailoring or workwear: no `ms`; `msum` says so.

## Not sourced
Fur clothing, Leather jacket, Deck jacket, Quilted jacket and Tie-brand articles were not fetched; Norfolk/Harrington etc. have no brand beyond those listed. 7 new brands to add to the register (Castell & Son, Gannex, Hudson's Bay Company, Blue Bell, One-In-Hand Tie Company, Jesse Langsdorf, George Key).
