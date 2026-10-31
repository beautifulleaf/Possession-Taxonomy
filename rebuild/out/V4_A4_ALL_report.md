# V4_A4_ALL report (A4, part ALL)

Part file: rebuild/out/A4_parts/ALL.json (272 KB). Replaces all nine A4 departments. Validated: OK, 105 kinds, 388 entries (237 before). Renames none, moves none.

## Entries before -> after, by department
- Handbags 105 -> about 190: houses' own pages (Louis Vuitton, Hermès, Chanel, Dior, Celine, Prada, Loewe, Fendi) plus Wikipedia (Handbag, Gucci, Bottega Veneta, Longchamp, Louis Vuitton). Sections by house country, then house.
- Eyewear: added Ray-Ban Olympian/Outdoorsman/Erika, Moscot Nebb/Grunya/Mulholland Drive, Oakley O-Frame; The General as a version of Aviator. Sections by owner group.
- Backpacks & belt bags: Osprey (15 lines), Gregory (12), Deuter Aircontact and Futura Air Trek, Kånken range, Eastpak, JanSport, Herschel Little America, from the makers' range pages. Generations and litre sizes are versions.
- Luggage: Rimowa lines, Samsonite Streamlite, Hartmann, American Tourister, LV Steamer Bag.
- Umbrellas: Jean Marius folding umbrella (origin badge). Baby carriers: BabyBjörn Baby Carrier (1973 to 2021 versions), Ergobaby carrier. Other departments unchanged apart from owner fields.

## Loose models (`m`)
All 140-plus loose models were removed as out of scope (retailer SKUs without a line page). Only those the pages now attest became entries or versions (for example Madeleine, Liv Pochette, Distinct, Eva). Packing cubes, locks, hip seats and changing bags stay commodity kinds with no entries.

## Market fields
Every entry whose maker is in the owner map carries own, tier, cty and own_y. Years from fetched pages: Louis Vuitton 1987, Dior 2017, Loewe 1996, Rimowa 2016, Gucci and Saint Laurent 1999, Bottega Veneta 2001, Tumi 2016, Hartmann 2012, Gregory 2014, Ray-Ban 1999, Oakley 2007, Persol 1995. Panels (ms) on Handbags (group revenue of Kering EUR 14,675m 2025, Tapestry US$7.01bn, Capri US$4.4bn, Richemont EUR 21.4bn, H51 66.72 % of Hermès 2025), Eyewear (Safilo EUR 983.4m 2025, Marcolin EUR 547m 2022, Kering Eyewear about EUR 1.5bn 2023, Sunglass Hut 3,131 stores) and Luggage (CVC 2007 US$1.7bn, Tumi 2016, Rimowa 2016). Twelve owner companies added to the register; 6 makers added; brand_updates for 30 existing brands.

## Coverage (stated in each kind's `sel`)
No whole-space list exists, so every `sel` ends "Covers n lines; ..." with what is missing. Where I stopped: house pages stop at the lines the pages showed (Louis Vuitton page showed about 25 lines; Fendi page showed only Baguette, Baguette Soft, Croissant, Peekaboo).

## Not sourced
- Gucci, Saint Laurent, Bottega Veneta, Goyard, Mulberry, Coach, Longchamp model pages (blocked or unfound); Gucci and Saint Laurent crawler-blocked in search.
- Globe-Trotter page (404); no luggage market shares (only search excerpts, not fetched). Ergobaby company page unreachable; Highlander ownership unsourced.
- Owners for Osprey, Fjällräven, Eastpak, JanSport, Herschel, Bellroy and others not fetched, so own/tier left empty.
- Kind placement of Dior, Celine, Prada and Loewe lines is by usual shape; the pages give names only. LV URL and Rebag URL were tried unsearched at the start (Rebag gave a redirect page, unused).
