# BRANDLAYER VERIFY: A1 Clothing

Opus verifier, 2026-10-31. Input: A1.json (323 harvest brands, 22 regions) minus 1 audit drop (AYA), plus AUDIT_A1.json add_brands (71) and add_regions (13): 393 brand rows, 35 regions. Every source URL was fetched raw with mcp__Parallel__web_fetch (session c0f3a7e2...); large results were saved and parsed with python (VERIFY_A1_tmp/p_*.txt, chk2.py, rchk.py, decisions in dec.json). For the four big Wikipedia list pages (US category page 1, LVMH Prize, The Fashion Awards, CFDA Fashion Awards, High fashion brands, ja shinise list) Parallel excerpt mode (verbatim page passages) was used with the names as queries, and a second pass was run for every name not returned; the ja list and US pages were also fetched in full.

## Counts

- Brands checked: 393 of 393; shown false: 0; rows needing src2: 25
- By tier: {"cultural": 144, "quality": 120, "listed": 90, "seller": 39}
- Regions: 19 with renown, 16 without; 17 brand rows carry a region
- No duplicate rows found to merge (normalised-name check).

## Points for the merge

- Harvest layer "premium" splits into quality 108 / listed 69 / cultural 18 / seller 4; harvest "cultural" into cultural 126 / seller 35 / listed 21 / quality 12.
- Directory rule: all 46 British Made Clothing rows (skirts, dresses) are "listed".
- Own-website rule: makers' own sites give "listed", or "seller" when the site sells a traditional item (thobes, sarees, barong, caftan, kilt, safa ...). Regions whose only renown text is on a maker's or seller's own site (Millau, Saint-Junien, Shiromeda, Bavaria, Varanasi, Shetland, Montecristi, Béarn, Arequipa) are renown false.
- Forum posts and reader comments are not editorial evidence: Himel Bros., Good Wear Leather, Lost Worlds, Brimaco, Dave Sheeley, Thedi, Southcombe, Restelli, Hamerli are "listed". Tripulse sits under "Brands I'd Like To Test" with AYA, so it is "listed" (the audit dropped AYA for the same reason).
- ja.wikipedia shinise list: rows linking to their own article (福助, オーベクス, 竺仙, 冨田屋) are cultural; red-link or unlinked rows (長谷川染物店, 銀座越後屋, とみひろ, 柴田音吉洋服店, 堀内洋服店, 高橋洋服店) are listed.
- src2 used for: 13 US category names on the continuation page, 4 royal-warrant names on its continuation page, Sindiso Khumalo (lvmhprize.com), 6 Woolmark names (M.PATMOS, Teatum Jones, Bodice, Suket Dhir, Qiu Hao, DYNE; woolmarkprize.com history page), Angels (BBC; The Times is paywalled and returned no text).
- Region brand lists cut to names on the raw page: Savile Row keeps 11 houses, all named on the harvest also_src Savile Row article (the Hong Kong tailors src names none); Paris 10 of 17; Italy 17 of 21; India 3 of 10; Turkey 6 of 9; Bavaria 5 of 6; Varanasi 1 of 6; Aran 1 of 3; Shetland 1 of 3; Montecristi 1 of 3; Chiapas/Oaxaca 1 of 3; Yucatán 2 of 3; Uzbekistan 2 of 3; Iseyin 1 of 2; Ethiopia 2 of 3; Moroccan caftan couture 1 of 6; Ghana Ashanti 1 of 2; West Africa 0 of 1.
- Kyrgyzstan: the page backs Kyrgyz felt craft and the UNESCO felt rugs, not the ak-kalpak named in the harvest speciality. Panama Las Tablas: renown rests on a ministry page that celebrates the town's pollera artisans; it does not use the word "renowned". The Hungary (Pécs) quote comes from a reader comment.

## Regions

- RENOWN | England (Savile Row, London) | 11 brands | London's Savile Row, until then the undisputed international center of bespoke tailoring — src (Hong Kong tailors) names none of the houses; these 11 are named on the harvest's also_src https://en.wikipedia.org/wiki/Savile_Row (fetched raw); Dege & Skinner, Norton & Sons, Maurice Sedwell, Kathryn Sargent, Chittleborough & Morgan, Henry Herbert, Cad and the Dandy, Chester Barrie not on either page
- RENOWN | Scotland (Outer Hebrides) | 3 brands | This definition, quality standards and protection of the Harris tweed name are enshrined in the Harris Tweed Act 1993. — protected designation (Act of Parliament, Orb stamp)
- RENOWN | Hong Kong | 3 brands | The Hong Kong tailors are well-known for producing bespoke men's clothing 
- no renown | Ghana (Ashanti Region) | 1 brands | According to Asante oral tradition, it originated from Bonwire in the Ashanti Region — origin statement only, no renown wording; Vlisco (Dutch) is the only listed name on the page; Akosombo Textiles not on page
- no renown | Netherlands and West Africa | 6 brands |  — all six named; the article describes the industry but has no renown statement for the region
- RENOWN | France (Paris) | 10 brands | Beginning in the mid-nineteenth century, Paris became the centre of a growing industry — Hermès, Charvet, Berluti, Isabel Marant, Sonia Rykiel, Cacharel, Kenzo not on page
- RENOWN | Italy (Milan, Florence) | 17 brands | Milan, Italy's centre of design, was ranked the top fashion capital of the world — Isaia, Caraceni, Rubinacci, Borsalino not on page
- RENOWN | India | 3 brands | A famous Indian fashion trademark is embroidery — Fabindia, Anokhi, Sabyasachi, Rohit Bal, JJ Valaya, Falguni Shane Peacock, Raymond not on page
- RENOWN | Iceland / Northern Europe | 2 brands | The most iconic piece of Icelandic wool clothing is undoubtedly the lopapeysa. 
- RENOWN | Norway | 6 brands | Norway's rich knitting heritage lives on through a mix of brands with centuries of history 
- no renown | Ireland (Aran Islands) | 1 brands |  — GQ describes Inis Meáin's factory on the Aran islands but does not say the islands are renowned; Aran Crafts and Aran Sweater Market not on page
- no renown | Scotland (Shetland, Edinburgh) | 1 brands |  — src is Jamieson's own website; Kinloch Anderson and William Lockie not on page
- RENOWN | Japan (Okayama, Kojima) | 6 brands | Especially in the Okayama prefecture, where a cache of denim factories have been turning out high-quality selvedge denim 
- RENOWN | Japan (Kyoto) | 5 brands | Kyoto's kimono are also regarded to be among Japan's finest specimen. 
- no renown | India (Varanasi, Kanchipuram) | 1 brands |  — src is a seller's own About page (Varanasi heritage claimed by the seller); other listed sellers not on this page
- RENOWN | Turkey (Istanbul) | 6 brands | Over the years, Istanbul has made its mark as a new fashion capital. — Mavi Jeans, Ipekyol, Faik Sonmez not on this page
- RENOWN | Morocco / North Africa | 1 brands | The garment [the caftan] recently made it onto the UNESCO list of Intangible Cultural Heritage. 
- no renown | West Africa (Nigeria, Senegal, Mali) | 0 brands |  — UNESCO report lists aso-oke, bogolan and other textiles but has no renown wording for the region; Kankou Elegance not in report
- no renown | Germany / Bavaria (Munich) | 5 brands | Die Tracht ist nicht nur in Bayern mehr als beliebt — retailer's own website; says Tracht is popular in Bavaria, not that the region is renowned; Stockerpoint not on page
- no renown | Australia | 7 brands |  — src is a Wikipedia category page: all seven are members, but a category page states no renown
- no renown | Ecuador (Montecristi) | 1 brands |  — src is Lock & Co.'s own shop page (hand-woven in Ecuador from the finest toquilla straw); Brent Black and Panama Hatters not on page
- no renown | France (Béarn, Oloron-Sainte-Marie) | 1 brands |  — src is Laulhère's own website ('Made in Oloron-Sainte-Marie since 1840')
- no renown | France (Millau, Aveyron) | 1 brands | In Millau, known as the 'Glove Capital' — statement is on the maker's own website (not independent); owner rule 2026-10-31 bars it from placing a regional division [audit add]
- no renown | France (Saint-Junien, Limousin) | 1 brands | Saint-Junien, also known as “The City of the Leather Glove” — statement is on the maker's own website (not independent) [audit add]
- RENOWN | Hungary (Pécs) | 1 brands | the city of Pécs — has a rich history of producing high-quality gloves, dating back to the 18th century — quote is from a reader comment on the Permanent Style glove guide [audit add]
- RENOWN | Mexico (Kimbilá and Mérida, Yucatán) | 2 brands | Kimbilá has earned a reputation as one of Yucatán's best places to shop for handcrafted clothing — Guayaberas Cab not on this page [audit add]
- no renown | Peru (Arequipa) | 2 brands |  — src is the owner group's own website; no statement that Arequipa is renowned [audit add]
- RENOWN | Uzbekistan (Margilan, Fergana Valley) | 2 brands | Margilan ... It is considered a center of silk production and silk goods. — Dildora Kasimova not on this page [audit add]
- RENOWN | Kyrgyzstan | 1 brands | ala-kiyiz and shyrdak rugs ... inscribed into the UNESCO List of Intangible Cultural Heritage in 2012 — page states Kyrgyz felt craft revival and UNESCO felt rugs; it does not mention the ak-kalpak named in the harvest speciality [audit add]
- RENOWN | Nigeria (Iseyin, Oyo State) | 1 brands | Iseyin is considered the home of aso-oke. — Clairla not on this page [audit add]
- no renown | Ethiopia (Shiromeda, Addis Ababa) | 2 brands | Shiromeda, one of Addis Ababa's most recognized destinations for Ethiopian clothing — statement is on the seller's own website (not independent); Mafi Mafi not on this page [audit add]
- RENOWN | Panama (Las Tablas, Los Santos) | 1 brands | San José de Las Tablas celebra con orgullo el talento de sus artesanos (Festival del Tambor y la Pollera) — ministry page celebrates the town's pollera artisans; no explicit 'renowned' wording [audit add]
- no renown | Mexico (Chiapas highlands and Oaxaca) | 1 brands |  — page describes highland backstrap-loom cloth sold through cooperatives but no renown statement; Remigio Mestas and Khadi Oaxaca not on this page [audit add]
- no renown | Morocco (Casablanca, Marrakech) - caftan couture | 1 brands |  — museum page profiles Tamy Tazi; it does not say the region is renowned for caftan couture; other designers not on this page [audit add]
- RENOWN | Ghana (Bonwire and Adanwomase, Ashanti) - kente sellers | 1 brands | Bonwire – now the leading centre of kente weaving in Ashanti —  [audit add]
