# GAP_J10 report: Smoking & Vaping

Edited J10.json and J10_brands.json (+30 makers and owners). Validator OK (133 kinds, 367 archetypes). Backups, scripts and removed-model list: rebuild/work/GAP_J10/. About 22 fetches.

## Closed
1. **Loose models:** all 98 `m` items removed (list in rebuild/work/GAP_J10/removed_models.json). They were commodity SKUs (humidors, cutters, cases, rolling machines, snuff bottles, hookah bowls, glass bongs, grinders, lighter and vaporiser models) or maker/pipe-blend lines with no fetched page. Velo, General Onyx and Ettan came back as entries from fetched pages.
2. **Coverage lines:** every kind with entries now has `nl` and `sel` ending "Complete", "Covers" or "No complete list exists; follows ...".
3. **Cigars:** Wikipedia List of cigar brands re-read (compact rows A to Z, about 170). Added Aristoff, Star Cigar, 777, 1881, 1881 Perique, La Flor de la Isabela, Sancti Spiritus, Lars Tetens, Propio, and a new kind "Cigar marque, country not stated" (46 rows with no country, owner as listed). All five country kinds now say Complete. Wikidata (Q110684031) has only 33 items, almost none with country, so was not used further.
4. **Heated tobacco:** page read to its end (226,066 characters); Revo added; Complete 14. Marlboro HeatSticks, iSENZIA, CK33 excluded.
5. **Vaping:** Electronic cigarette read to its end (234,450). New kind "Vape brand, form not stated" with Vype, Logic, Green Smoke, Nicocigs, Voke, QMOS, eTron 3T, BLOW. The four kit kinds say Complete for the page.
6. **Pouches, snus:** nicotine pouch (+9 brands: Zonnic, Epok, LYFT, Velo, ZZU, Nordic Spirit, Zone, Garant, Engu) and portion snus (+Blue Ocean, Grovsnus Svart, General Onyx), Makla El Hilal under Dipping tobacco.
7. **Empty pipe kinds:** Oriental blend (4 TobaccoReviews pages) and Kizami (Koiki, Takarabune, Yamabuki, Kikyo, one hobbyist page).
8. **Sections:** missing `g` filled on Freehand, Box mod, RTA, RDA.

## Remains
- **Dokha:** still empty. Searched: Wikipedia Dokha (retailers only).
- **Vape hardware makers** (SMOK, Vaporesso, VooPoo, OXVA, Geek Bar): no fetched reference. Searched: "list of e-cigarette brands Wikipedia", Wikidata class query (empty).
- **Storz and Bickel vaporisers:** only search excerpts found, so not entered.
- **Oriental blends:** covers 4 only; Kizami owners unstated.
- **Not attempted (budget and sources):** pipe-blend target of 40 to 60, cannabis strain lineage (Leafly/Seedfinder), Kaywoodie, Vauen, Ascorti, Radice, Bo Nordh (earlier 404/403), 11 Habanos marques without vitola lists, individual PMI/BAT/JT shares (chart only).
- **Dissolvable nicotine:** page names none; kind stays empty.

# Second round (coordinator items 1 to 5)
About 40 more fetches. Validator OK (133 kinds, 457 archetypes).
1. **Habanos vitolas:** added for Vegueros, Diplomaticos, La Gloria Cubana (Wikipedia), Por Larranaga (Wikipedia), Rafael Gonzalez (Chaveta). Still none: Jose L. Piedra, Quintero, Fonseca, Vegas Robaina, El Rey del Mundo, Juan Lopez, La Flor de Cano, Saint Luis Rey. Their Wikipedia pages carry no vitola list; cubancigarwebsite.com gave 403 and Firecrawl is out of credits. Searched: Habanos brand vitola lists, per-marque pages.
2. **Pipe blends:** TobaccoReviews brand pages read for Samuel Gawith (122 blends), Peterson (82), Mac Baren (131), Cornell and Diehl (386; first 100,000 of 165,159 characters). About 90 blends with many reviews added across the five blend kinds; mis-typed Cornell and Diehl rows (Billy Budd, Epiphany, Bayou Night: types the kinds do not hold) were left out. Not done: Gawith Hoggarth, G.L. Pease, Sutliff, Davidoff, Orlik, Captain Black (brand page IDs not found in budget); C&D remainder.
3. **Pipe makers:** Peterson (1865, Ireland, Laudisi Enterprises since 2018) and Savinelli (1876, Italy) registered from Wikipedia. Kaywoodie, Vauen, Stanwell, Dunhill: Wikipedia has no usable page, Pipedia returned 403; search excerpts only, so not registered.
4. **Vaporisers:** Storz and Bickel redirects to Electronic cigarette on Wikipedia with no company facts; official site not found by search. SMOK, Vaporesso, VooPoo, Geek Bar: no trade-press page fetched (budget). Searched: "Storz Bickel Volcano Wikipedia", vape brand lists.
5. **Shares:** PMI FY2024 10-K added to the cigarette market panel: international share 28.7 % (cigarettes 23.5 %, heated tobacco 5.2 %), cigarette-over-cigarette 25.3 %, Marlboro 10.1 %, all 2024, excluding China and the US. BAT and JT annual-report shares not fetched.
