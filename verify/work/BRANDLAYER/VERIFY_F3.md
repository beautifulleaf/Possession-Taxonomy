# VERIFY F3 Coins, Stamps, Medals & Trading Cards (brand layer, 2026-10-31)

Every distinct harvest and audit source URL, plus the src2 pages, was fetched raw once with mcp__Parallel__web_fetch (full_content). That is 55 pages, saved in VERIFY_F3_tmp/pages/ (index.json maps each URL to its file) and parsed with VERIFY_F3_tmp/build.py. The Borsa Istanbul PDF and List of bullion dealers came back inline, so their name sections were saved verbatim (pages/borsa.txt, pages/bullion.txt). No URL was guessed: every src2 page came from a search result.

Brands checked: 307. Not shown: 0. By tier: quality 121, cultural 102, listed 84 (the seller tier is not used; dealers carry role "seller"). Homonyms: 3. Cross-tags: 13. Deferred: 10 (in DEFER_F3.json). Regions: 22, with 2 showing renown and 20 without.

Row count: harvest 263, minus 1 drop (The Mint, Carlingford), minus 6 deferred game publishers, minus 6 duplicates merged in, plus 48 audit additions and 9 cross-tag rows (De La Rue, Waterlow & Sons, Tiffany & Co., Jostens, Calbee, Mitsubishi Materials, Heritage Auctions, In the Game Trading Cards, Dart Flipcards).

## Coordinator rulings applied
- **LBMA:** all 52 LBMA rows were re-sourced to the Borsa Istanbul PDF, which reproduces the LBMA Good Delivery gold and silver lists under licence (last update 02/10/2026). All 52 are shown there, in some cases under the PDF's spelling (Tanaka Kikinzoku Kogyo, Shenzen Cuilu, Aneka Tambang, CCR Refinery). Tier is quality, as an accreditation standard. Today's raw LBMA fetch does show some names, but the src was re-sourced anyway.
- **Shandong Gold Smelting:** cultural. It is kept as a former Good Delivery refiner (the PDF's former group: "Unlisted Date: 05.08.2026").
- **29 silver-list additions:** quality on the same PDF. Note: most of them are base-metal smelters (the audit's flag).
- **Stamp printers and trading-card rows:** the Colnect-only printers and the trading-card table rows without their own article are kept as listed (existence only). That covers 48 Colnect rows, and 33 table rows: the 31, plus Action Packed with rel Donruss and Maxx with rel Upper Deck. Select Australia is listed even though the page calls it the largest producer of Australian rules football cards; it has no article of its own. Press Pass links to "Press Pass, Inc.", so it is cultural.
- **British American Bank Note Co.** is cultural, not listed: the Bank of Canada Museum page says BABN designed and printed the Bank of Canada's first notes in 1935, and holds its models and proofs in the National Currency Collection.
- **Security Printing Press Nashik** is cultural, not listed: it has its own Wikipedia article under the name India Security Press (alias), which prints postage stamps.
- **Re-sourced printers:**
  - Joh. Enschedé: quality. Its own article calls it "Royal Joh. Enschedé" (stamps, banknotes).
  - Harrison & Sons: cultural. Grace's Guide records the 1914 Royal Warrant "Printers-in-Ordinary to H.M. the King".
  - Cartor: quality. Merged with Walsall and ISP. The Åland stamp it printed won the World's Best Stamp 2025, praised for its "meticulous print quality".
  - Bundesdruckerei: quality. Winner of the IACA 2026 Best New House Note (STELLA).
- **Coin of the Year upgrades:** the 9 mints were raised to quality, each confirmed on the raw COTY page: IPZS (Italian Mint), Kremnica, Pobjoy, Staatliche Münze Berlin, SMBW (Karlsruhe), Hamburgische Münze, St Petersburg, Moscow and CBPMC. Mennica Polska is also quality (COTY). Shenzhen Guobao Mint is quality as the 2026 COTY Best Crown mint (Numismatic News).
- **Duplicates merged, with aliases:**
  - Bavarian State Mint (+ Bavarian Central Mint)
  - SkyBox (+ SkyBox International)
  - Tristar (+ Tristar Productions)
  - Mennica Polska (+ Polish Mint (Mennica Polska))
  - Cartor (+ Walsall Security Printers, International Security Printers)
  - Pinnacle Brands, renamed "Pinnacle" so that the merge folds it into the existing F3 row
- **Central Mint:** renamed "Central Mint (Taiwan)".
- **SEGS:** row kept, tier listed. The Coin World directory row is the src; src2 is Wikipedia Third-party grading, where the PNG survey lists SEGS as "Poor".
- **The Mint (Carlingford):** dropped.
- **Central banks:** dept "issuer" for Costa Rica, Cyprus, Fiji, Iceland, Iraq, Jordan, Lesotho, Sierra Leone, Greece, Latvia, the NBU, the Kazakhstan NB mint and Bangko Sentral.
  - Bangko Sentral is also a refiner (LBMA gold list on the Borsa PDF, as src2): quality.
  - The Kazakhstan NB mint and the NBU are also makers.
- **Bullion dealers:** role seller for DGSE, Goldline, Monex, Texas Precious Metals, Chards, Sharps Pixley, Pallion, Emirates Gold and Garfield (the last two also refine).
- **India Government Mint:** src2 is the MoSPI Statistical Year Book ("a long tradition of craftsmanship"). It stays cultural.
- **Defer:** the 10 game publishers went to DEFER_F3.json, each with a fetched source and shown true: Wizards of the Coast, The Pokémon Company, Konami, Media Factory, AEG, Bushiroad, Chaosium, Cryptozoic, Decipher (as "Decipher, Inc.") and Renegade. Konami and Bushiroad were also removed from the "Japan (cards)" region.

## Additions (48): tier rulings
- **Quality:**
  - Thomas Fattorini: BAMS President's Medal and Marsh Award for medallic art, 2011.
  - Crane Currency: IBNS Bank Note of the Year 2025.
  - Note Printing Australia: IBNS Bank Note of the Year 2022.
  - Orell Füssli: IBNS Bank Note of the Year 2016 and 2017, "Printed by Orell Fussli".
  - The 29 LBMA silver-list refiners.
- **Cultural:**
  - GDE Bertoni (own it.wikipedia article; no independent craft statement).
  - Thomas Lyte (own article and Royal Warrant; famous trophies are standing, not a craft test).
  - Hélio Courvoisier (stamps). Its "Master Stamp-Printers" is the printer's own legend reproduced in a philatelic study, so the audit's premium was lowered.
  - Yvert et Tellier, Michel, Vaughtons, Osborne Coinage, Northwest Territorial Mint.
  - Sellers (role seller): Noonans, Stephen Album, Ginza Coins, Taisei Coins, Sekiguchi and Champion Auctions. The Japanese names are matched raw in kana and kanji on WealthAtlas.
- **Listed:** Baldwin's (coins). A Numista shop-directory row is its only source; role seller.
- **Own-site sources with an independent src2 (cultural, role seller):** Stack's Bowers (CoinWeek: "the current official house for the American Numismatic Association") and Künker (CoinsWeekly who's who).

## Homonyms and cross-tags
- **Homonym true:**
  - Hélio Courvoisier (stamps), vs Courvoisier cognac (J7).
  - Baldwin's (coins), vs Baldwin locks (B8).
  - Crane Currency, vs Crane inhalers (H2/C5).
- **Same companies:**
  - Leaf, Merlin and Score are the register's own F3 rows (no new rows).
  - Pacific Trading Cards keeps its full name. No register namesake exists in F3; the register's "Pacific …" rows are unrelated fashion and beauty firms.
- **Cross-tags (13), each with an F3 product confirmed on a fetched page:**
  - Mennica Polska (F5)
  - Mitsubishi Materials (C4): LBMA gold and silver lists
  - Bradbury Wilkinson (F5): Colnect stamp printer, listed
  - Waterlow & Sons (F5): Colnect, listed
  - De La Rue (E1): stamps from 1855; IBNS 2023 makes it quality
  - Thomas Fattorini (A3)
  - Thomas Lyte (A3)
  - Tiffany & Co.: the Super Bowl trophy since 1967 (ABC); cultural
  - Jostens (A3): Super Bowl rings (NYT, partly rendered); cultural
  - Calbee (J8): its own PR TIMES release for the プロ野球チップス cards; listed
  - Heritage Auctions (F2): began as a rare-coin firm; cultural, role seller
  - In the Game Trading Cards (E1): Category member
  - Dart Flipcards (E1): Category member
  - Cartamundi is left in E1, as the audit advised. Parkhurst Products was not found on the fetched Category page, so it gets no cross-tag.

## Regions
- **With renown:**
  - Ticino. BBC: "Four of the world's biggest gold refineries are in Switzerland, three of them in the southern canton of Ticino". Only PAMP is shown on the page (in the related links); Argor-Heraeus, Valcambi and Metalor were removed from the region.
  - Kremnica. Wikipedia: "the site of the oldest still-working mint in the world". Kremnica Mint is shown.
- **Pforzheim:** renown false. Wikipedia's "known for its jewelry and watch-making industry ... Goldstadt" is renown for A3/A5 goods, not for refining or bullion. The refiners are named only on the ESG buying page, which is a refiner's own site, so no brands are kept.
- **Kongsberg and Llantrisant:** not added. Only the mints' own sites exist, which do not count for renown.
- **Harvest regions (19):** renown false for all. They rest on list pages (LBMA, now the Borsa PDF by country; COTY; Colnect; the Category page; the bullion list), on one company page (Royal Warrant), or on makers' own sites (Monnaie de Paris, Künker). Brands not shown on a region's page were removed:
  - Italy: Chimet, Italpreziosi, TCA
  - Australia: Royal Australian Mint, ABC Refinery
  - UK medals: Spink, Toye Kenning & Spencer
  - US grading: Beckett Grading Services
