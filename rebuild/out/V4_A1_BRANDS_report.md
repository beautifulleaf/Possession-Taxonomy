# V4_A1_BRANDS report

Part file: rebuild/out/A1_parts/BRANDS.json (replaces [], depts []). Check passed: loads under python3 -I and every brand_updates key exists in A1_brands.json. Builder: rebuild/work/V4_A1_BRANDS/build.py.

## Brands updated
172 existing register brands got own, tier and (where a page states it) own_y. 137 brands not in the register were added as new entries (name, segment, own, tier, source; no country or founding year, none fetched). Sources are Wikipedia company articles plus Inditex's own brands page; the owners' own brand pages were mostly unavailable (LVMH 404, Kering blocked, H&M 404), so Wikipedia stands in.

Per owner (updated + new): LVMH 23, Kering 11, Richemont 14, Inditex 8, H&M Group 9, Fast Retailing 7, Gap 6, PVH 2, Tapestry 2, Capri 2, Prada Group 4, VF 10 (Lee and Wrangler under Kontoor 2), Levi's 3, Moncler Group 2, Nike 2, Adidas 2, Puma 2, Under Armour 1, Anta 5, Li-Ning 1, Amer 7, Gildan (incl. Hanesbrands brands) 14, Authentic Brands 35, WHP 12, Marquee 3, ABFRL 10, Reliance 5, Shein 4, Primark/ABF 2, Next 7, M&S 5, Tendam 6, LPP 5, Bestseller 9, Boohoo 11, ASOS 4, Aritzia 5, lululemon 1, AEO 3, A&F 3, URBN 4, Pentland 9, Sanyo Shokai 4, Itochu 2, Mr Price 3, Cotton On 5, LC Waikiki 1, Landmark Group 1, Bosideng 4, Ralph Lauren 5, Hugo Boss 3, Burberry 1.
Tiers: Global group for multi-brand multinationals; National champion only where a fetched page gives a leading rank (Primark, Next, M&S in the UK per GlobalData; Anta and Li-Ning in China per Euromonitor; Bosideng in China down wear; Mr Price on the JSE); Independent for the rest. No Craft & indie or Own label tier set.

## Market facts (dept_ms)
Tops: UK apparel shares for 2025 (GlobalData, 10 retailers, Primark 6.0 %); China sportswear shares (Euromonitor via China Daily, Anta 23 %, Nike 20.7 %; the article gives no year, so yr is null); Shein 28 % of US fast fashion (2022, Shein's own claim); 36 group revenues with year (2018 to 2026, in the note, not as share). Coats & jackets: Bosideng group 36.7 % of China down clothing (2010). Underwear, nightwear & swim: Hanesbrands revenue USD 3.51 billion (2024).

## Not sourced
- Not done: OTB (page 404), Heilan, Semir, Youngone (404/disambiguation), Shimamura (surname page), Onward, World Co., Trent, Mango (404), Lojas Renner (redirect, not refetched), EssilorLuxottica (skipped as instructed). Supreme and Stuart Weitzman skipped (sold to non-apparel or footwear owners).
- No fetched group-level market shares for US, Japan, India, Brazil, Germany, France; no UK share for Inditex group. Paid sources (GlobalData, Statista, Euromonitor) blocked.
- National champions cover UK, China, South Africa only as tiered; Poland, India, Japan, Turkey, UAE, Australia, Korea, Spain brands recorded without a leader claim (Independent). Africa, Middle East, South Asia and Oceania appear only through Mr Price, LC Waikiki, Landmark, ABFRL/Reliance and Cotton On.
- Craft and indie lists not fetched. Gildan's ownership of Hanesbrands brands (2025) is from a page saying the deal was agreed; closing is inferred from a later mention. M&S revenue (GBP 17,273.6 m) and Capri revenue conflict within their pages.
- About 70 fetches used; the target of about 20 markets was not reached.

# Round 2 update (continuation)

Part file rebuilt by rebuild/work/V4_A1_BRANDS/build.py (first version kept as build_v1.py). Check passed: loads under python3 -I; all 229 brand_updates keys exist in A1_brands.json; 205 new register entries. Tiers on updates: Global group 117, Independent 104, National champion 8. About 62 further fetches; every page found by WebSearch first (the earlier guessed-URL fetches stay logged in sources.tsv).

## Changes
- Gildan correction: the Hanesbrands brands (Hanes, Playtex, Bali, L'eggs, Just My Size, Barely There, Wonderbra, Maidenform, Berlei, Bonds) now sit under Hanesbrands, no own_y. No fetched page states the Gildan deal closed.
- Newly sourced portfolios: OTB Group (Diesel, Maison Margiela 2002, Viktor & Rolf 2008, Marni 2012, Jil Sander 2021, Amiri 2019 as page text), Mango, Trent, Lojas Renner, Arvind, Benetton, Oniverse (ex Calzedonia), Max Mara, Esprit, s.Oliver, C&A (Cofra), Zalando own labels, Muji, Canada Goose, Columbia (Sorel 2000, Mountain Hardwear 2003, prAna 2014), Patagonia, HLA/Heilan Home, Samsung C&T Fashion, Gloria Jeans, Koton, Mavi, Country Road Group, Pepkor, Lindex, Mulliez (Kiabi), El Puerto de Liverpool (Suburbia 2016), Hering/Reserva (Soma/Azzas 2154), Shimamura.
- 26 register brands got an owner from their own entry's cited page (Lacoste, DAKS, Spanx, Wolford, Fjällräven etc.); that text and page were fetched in an earlier stage, not this session.

## Markets with a leader claim from a fetched page
UK (Primark, Next, M&S; GlobalData 2025), China (Anta, Li-Ning, Euromonitor figure, no year; Bosideng), South Africa (Mr Price 9 % 2014; Pepkor largest by store count 2025), Japan (Uniqlo 6.5 %, no year; Shimamura second among specialty chains), Brazil (Renner 7.2 % 2021; Hering), Russia (Gloria Jeans, 2009 rank), Latin America (Azzas 2154 claimed largest). Regions with only owner records and no leader claim: Turkey (Koton, Mavi, LC Waikiki), UAE (Max), Korea (Samsung C&T), Mexico (Liverpool), Chile (Falabella not entered), Australia (Cotton On, Country Road Group), Sweden (Lindex), France (Kiabi), Italy (Benetton, Oniverse, Max Mara), Spain (Mango, Tendam), India (Trent, ABFRL, Arvind, Reliance), Germany (s.Oliver, C&A, Zalando).

## New market facts
GlobalData 2024 global shares (Nike 2.85 %, Adidas 1.79 %, Shein 1.53 %, Zara 1.24 %, H&M 1.06 %, Uniqlo 0.92 %); US apparel (Nike 4.9 % 2021, 4.3 % 2022); US clothing spending (Amazon 17.8 %, Walmart 6.0 %, Macy's 3.1 %, 2026); Germany 2023 sales ranking (Otto, H&M, Zalando, Shein); top-six concentration South Africa 47 %, Egypt 4 %, Nigeria under 2 % (2012); revenues for 20 more groups.

## Still not sourced
- Onward Holdings, World Co., Youngone, Semir, Heilan beyond HLA, Itochu brand list: pages lacked brand lists (no portfolio entered). EssilorLuxottica skipped as instructed.
- Market shares for India, France and Germany as shares: only a French spending ranking by rank (no figures), German sales not shares; no Indian share beyond a brokerage excerpt not fetched. Indonesia, Nigeria, Kenya, Saudi Arabia, Argentina, Egypt: no fetched page names a leader or owner, so no brand got a tier there.
- Craft & indie: the register's own pages are not overviews of the scene; no brand was given that tier.
- Own label tier unused. Kontoor's tier and Stuart Weitzman, Supreme, Club Monaco left unset.
- Budget: first-round and second-round fetches together exceed the 70 allowed; the coordinator granted 80 more.
