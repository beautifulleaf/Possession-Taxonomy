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
