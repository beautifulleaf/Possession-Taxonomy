# V4_J9c report: owners for J9 brands

Backups: rebuild/work/V4_J9c/bak/. Script: rebuild/work/V4_J9c/apply.py. `validate.py --v3`: OK (106 kinds, 960 entries).

**Result: 45 of the 432 ownerless brands now have an owner (387 remain blank).** Each filled entry carries its owner source in a new field `os`. Owners new to the register were added to J9_brands.json.

## Fetches: about 33 (budget 35)
- Wikidata SPARQL (P127 owned by, P176 manufacturer, P749 parent), 9 queries covering all brand labels (names under 48 per query because longer URLs were rejected). The yield was low: most small national brands have no ownership statements and common names matched unrelated items (ships, towns, bands), which were rejected by type and country.
- Portfolio and brand pages (Wikipedia): Spendrups, Pripps, Coca-Cola HBC, Britvic, Keurig Dr Pepper, Monster Beverage, Royal Unibrew, Carlsberg Group, Celsius Holdings, Kofola, Asahi Soft Drinks, Osotspa, Pakola, Innocent Drinks, V8, Vita Cola, Afri-Cola, Fritz-Kola, Olipop, Fever-Tree. Suntory, AJE Group, Kirin Beverage and Ocean Spray pages returned 404. Spendrups, Pripps, Coca-Cola HBC, Monster, Royal Unibrew and Celsius gave none of the target brands.

## Owners found
- Wikidata (35): Baikal (PepsiCo), Oasis, Bikkle, Iyemon (Suntory), Roots (Suntory Foods), Big Cola (AJE Group), Apotekarnes Cola (Pripps), XL Cola (Falcon Brewery), Club, MiWadi (Britvic), Cola Turka, Çamlıca (Ülker), Elmer Citro (Ramseier Suisse), Ifri Gazouz (Ifri Group), Hell Energy Drink (Hell Energy Hungary), Kool-Aid, Crystal Light, MiO (Kraft Heinz), Kia-Ora (The Coca-Cola Company), Laranjada (Madeira Brewery), Jupiña, Materva (Cawy Bottling Company), Nesbitt's (Monarch Beverage Company), Milaf Cola (Al Madinah Heritage), Mozell, Villa (Ringnes), Natakhtari (Efes Beverage Group), Tang (Mondelez International), Sukita (Ambev), Wonda (Asahi Soft Drinks, also page), Vitasoy (Vitasoy International Holdings), Vivi Kola (ViCOLLECTIVE AG), Vichy Catalan (Sociedad anónima Vichy Catalan), Vinea (Kofola ČeskoSlovensko).
- Portfolio and brand pages (10): Semtex (Kofola, acquired Pinelli 2009), Solo (Norway) (Carlsberg Group), Cidona (Britvic), Pakola (Mehran Bottlers), M-150 and Shark (Osotspa), Innocent Smoothies (The Coca-Cola Company, 2013), V8 (Campbell Soup Company, 1948), Vita Cola (Thüringer Waldquell), Afri-Cola (Mineralbrunnen Überkingen-Teinach AG), Fever-Tree (Fevertree Drinks plc, taken from the article lead).

Rejected matches: Chupa Chups, Cadet, Cool, Royal Club, Premium-Cola, Clipper, Elbrus, Duchess, Ghost, Henry Weinhard's (wrong item type or country); Sinalco and Solo/Villa multi-owner statements for Sinalco; Sunkist (Indonesia entry, KDP page is for the US); Kola Román (Wikidata gives Panamco, a conflict with the Colombian entry); Murree Brewery, Olipop (the brand is the company).

## Shelf moves (45)
- To Global groups: Oasis, Bikkle, Iyemon, Roots (Suntory), Baikal (PepsiCo), Innocent Smoothies, Kia-Ora (Coca-Cola). New kind "Suntory fermented drink brands".
- To Independents (existing regional kinds; new kind "Independent soda brands: Africa"): the other 38.
- The kind "National syrup and cordial brands: North America" emptied; recorded in J9_renames.json as renamed to "Independent syrup and cordial brands".
- National & regional brands lost the 45, so the 387 remaining ownerless brands stay there.

## Still without owner
387 brands, mostly small national sodas, water brands, energy drinks and US craft sodas, with no Wikidata ownership statement and no fetched portfolio naming them. Larger groups' own sites (Coca-Cola FEMSA, Arca Continental, Ambev, Postobón, Polar, Uni-President, Kirin, Sapporo, Lotte Chilsung and others) were not fetched within the budget.
