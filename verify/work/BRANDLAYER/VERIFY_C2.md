# VERIFY C2 Garden & Grounds

Raw fetch (Parallel free-tier web_fetch, full_content) of all 124 distinct source URLs (harvest and audit brands and regions), plus src2 pages found by search: substack secateurs test (Alpen), ZDNET (Navimow), Gardeners' World review URLs (Maze, Kent & Stowe, Harcostar), The Spruce Eats (Good Charcoal), Bob Vila wood-chipper test (Earthquake), IGCA 2026 sponsor page (Esschert Design), and the cross-tag pages (Oase, Morsø, Poterie Ravel). Pages in VERIFY_C2_tmp/pages/. Firecrawl was out of credits; several Gardeners' World, Telegraph, Independent, BHG, Real Simple and Serious Eats pages came back as excerpts only (noted per row). Seven excerpt-only src2 fetches returned inline and were saved by hand from the tool output.

Brands checked: 211 (harvest 156 minus 2 audit drops, plus 59 audit adds, minus 2 merges). Not shown: 1 (Wildwood Ovens: page text has only "Wildwoods" and the domain). By tier: {"cultural": 54, "quality": 30, "listed": 120, "seller": 7}. src2 used: 8. Homonyms flagged: 4.

## Tier rules applied
- cultural: Wikipedia category members (Garden tool, Lawn mower, Irrigation companies) and Masport article; Royal Warrant register (as in B1/B2/B6/B10); Marchio Storico register (Antonio Carraro); Consejo Regulador Talavera producer list (Talavera de la Luz); Black Country local-history museum page (Chillington); Suzu City traditional-products page (Noto Nenshoki Kogyo); RHS Chelsea tradestand medals and non-product RHS awards (standing, not quality, per coordinator).
- quality: independent tests and awards: CNET, Pool Nerd, ZDNET, Reviewed, GearLab, Bob Vila, BBC Gardeners' World Best Buys, BHG, Spruce Eats, testberichte.de, welt.de editorial verdict (Kränzle), RHS product awards (HOTBIN, Gaze Burvill, Twool's award-winning twine), EPV label (Krampouz, Serres et Ferronneries d'Antan, as in B1/B2), Spokesman-Review craft article (Guy Wolff), Uriarte (independent guide plus DO certification).
- seller: specialist sellers of traditional items (Tokoname bonsai pots, shichirin, Impruneta terracotta, scythes, clay tandoors).
- listed: own websites, directories (Metoree, Made in Britain), retailer catalogues and retailer praise, affiliate blogs, brand round-ups without tests, press features without quality claims, tested-but-no-result mentions (Wybot, Troy-Bilt, Que Choisir planchas), and RHS Product of the Year finalists that never won (precedent: CDA finalists in B-batches).

## Audit items applied
- Drops: BDT Capital Partners, The Middleby Corporation, Angus Chain Saw Service, John Miller (Corsham) (only the last two were harvest rows), plus the wrong-sense C2 tags on the register rows Halls (cough drops) and Viking (Viking Range): both listed under coordinator_flags for removal of C2 from those rows.
- Downgraded to listed: In The Swim set (Kokido, Pleatco, Jandy, Waterway, SmartPool, Water Tech, Intermatic, Baracuda, Kreepy Krauly); Rain Bird, Weathermatic, Netafim; Clementi; Bigei; swimmingpool.com set (Hayward, Fluidra, Natural Chemistry, Latham, Wilbar Group); affiliate pond-pump names (Pondmaster, Tetra Pond, Alpine Corporation); Polish retailer-filter names (Cellfast, Prosperplast, Walkiewicz) and Esschert Design; Tower kamado.
- Earthquake restored to quality: Bob Vila test page fetched (K33 best overall wood chipper; separate hands-on review also fetched).
- 59 additions all checked; RHS tradestand medallists tiered cultural; kazany.ru tandyr ranking names listed; finalists of RHS Garden Product of the Year 2019 listed; HOTBIN (winner) quality.
- Qualified names: Rover Mowers, Hunter Industries, Polaris (pool cleaners) (all homonym: true) and Chillington (Crocodile) (homonym: register Crocodile is a polo-shirt label). Uriarte Talavera is the same company as the register row (C8, B4): unflagged, dept "talavera planters (macetas)", C2 for planters only.
- Merges: Segway Navimow + Navimow; Maytronics + Dolphin (its brand). True Temper kept separate from Ames True Temper (product brand vs company), noted.

## cross_tag (existing register rows that also get C2)
- Oase (B10) -> C2, garden pond pumps and filters: https://www.oase.com/en/pond-and-water-garden/pond-pumps (fetched, own site): pond pumps, filters, UVC clarifiers for ponds and water gardens
- Bestway (G3) -> C2, above-ground pools: https://www.reviewed.com/home-outdoors/best-right-now/best-above-ground-pools (fetched): Bestway Power Steel above-ground pool, one of the two leading above-ground pool brands
- Poterie Ravel (B4) -> C2, garden terracotta pots and jars: http://poterie-ravel.com/ (fetched, own site): garden vases 20-120 cm, jars, basins; "Since 1803 ... part of a French ornamental garden tradition"
- Morsø (G3) -> C2, outdoor ovens: https://morsoe.com/us/product/outdoor/fireplaces/forno_us (fetched, own site): Morsø Forno cast-iron outdoor oven

## For the coordinator (not cross-tagged here)
- Kingsford and Big K (C8): overlap with C2 barbecue fuel.
- Kubota and BCS (C7), also Gravely and Pellenc: overlap with C2 garden machinery.
- Keter (G3): planters and raised beds overlap.
- Bartram Mowers (Royal Warrant, cultural) is a machinery dealer, the same profile as the two dealers the audit dropped; consider dropping it.
- Tower assumed to be the same company as register Tower (B6); left unflagged.

## Regions
- Japan (Seki/Gifu, Tokoname/Aichi): renown True ("Tokoname is a largest area to producing them [bonsai pots] in Japan"); brands kept 0, not on page 6
- United Kingdom: renown False (maker own site; no regional renown); brands kept 1, not on page 1
- Australia: renown False (maker own site); brands kept 1, not on page 4
- Germany: renown False (maker own site); brands kept 1, not on page 4
- South Africa: renown False (maker own site); brands kept 1, not on page 2
- Argentina / Brazil / South America: renown False (UK member directory; says nothing of South America); brands kept 1, not on page 2
- Japan: renown True ("The original Konro Grill is manufactured in Japan and is rooted in a centuries-old tradition"); brands kept 2, not on page 0
- England (Warwickshire): renown False (firm is "world renowned", not the region); brands kept 1, not on page 0
- Italy (Impruneta, Siena): renown False (seller page; no renown statement for the region); brands kept 1, not on page 0
- Netherlands: renown False (maker own site); brands kept 1, not on page 0
- Israel: renown False (maker press release); brands kept 1, not on page 2
- India: renown False (maker own site); brands kept 1, not on page 0
- Sweden: renown False (maker own site); brands kept 1, not on page 2
- South Korea (Yeongju): renown True ("Inspired by the traditional Korean hand tool, the Homi"); brands kept 1, not on page 0
- China (Shenzhen/Beijing): renown True ("Chinese Brands Drive Global Lawn Mower Revolution"); brands kept 4, not on page 2
- Malaysia: renown False (maker own site ("largest exporter" is about the firm)); brands kept 1, not on page 0
- Tunisia (Nabeul) / Morocco (Safi, Fes): renown True ("The pottery of Nabeul, Tunisia has achieved widespread international acclaim (Morocco not covered)"); brands kept 0, not on page 1
- India (Delhi): renown False (maker own site); brands kept 1, not on page 0
- Italy (Impruneta, Tuscany): renown True ("The most frost resistant terracotta in the world"); brands kept 3, not on page 3
- Puebla and Tlaxcala, Mexico: renown True ("Puebla becoming the most important earthenware production center in the New World"); brands kept 9, not on page 0
- Russia (Rostov, Tver) and CIS: renown False (retailer ranking; tandyr tradition attributed to Asian peoples, not Russia); brands kept 3, not on page 0
- Noto peninsula (Suzu), Ishikawa, Japan: renown False (maker own site; Edo-period method and municipal folk-property designation stated, but no renown statement); brands kept 1, not on page 3

Audit regions: Puebla renown accepted (the "internationally renowned" line on the page is about Talavera de la Reina in Spain, so the Puebla quote is used instead); Russia tandyr no renown (retailer ranking); Noto/Suzu no renown on the src (maker's own site, which names only itself).
