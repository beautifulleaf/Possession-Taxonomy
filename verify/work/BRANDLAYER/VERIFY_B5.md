# VERIFY B5 (Kitchen & Dining), brand layer

Checked 451 brands: 404 from the harvest, minus 16 audit drops, plus 64 audit additions, minus 1 merge (Lomonosov Porcelain into Imperial Porcelain Factory). Each source page was fetched raw once (Parallel web_fetch, full_content) on 2026-10-31; the pages are in VERIFY_B5_tmp/pages/ (index.json maps URL to file).

## Tiers
- cultural: 191
- listed: 215
- quality: 38
- seller: 7

## Not shown: 1
- L'hirondelle: not on the Japan Objects Nambu page; no other page found.

## Re-sourced (src2): 74
- 49 IVSH names now point to the paginated member pages (?tx_ivsh_member[currentPage]=N, Schneidwaren pages 2-8 and Haushaltwaren pages 2-3), as the audit found. The page links were taken from the fetched page 1 (never guessed).
- 15 Knifewear names point to brands page 1 or page 3 instead of page 2.
- Kahla, Bauscher, Lichte Porzellan and KPM Berlin point to Wikipedia 'Porcelain manufacturing companies in Europe'. KPM is the row 'Royal Porcelain Manufacture Berlin (abbreviated KPM)', which links its article; Kahla's and Bauscher's rows link no company article, so both are listed.
- Au Sabot (Franceclat, EPV and quality statement), Kamasada (Japan Guide), Oitomi (Kiriko Made), Suzuki Morihisa (Nihonmono), Unilloy (Red Dot Design Museum), Usmanov (International Folk Art Market), Hirota Glass (Tokyo Teshigoto).
- Names printed differently on the page are recorded as aliases: Carl Schmidt Sohn ('Schmidt Sohn GmbH, Carl'), Friedr. Herder Abr. Sohn, Otto Rüttgers, STUR (STUR GmbH), Notban ('Nobban'), Blichmann, Spike, Anvil, Pérez Pamatz, Zebra Head, Rosti.

## Merges and aliases
- Merged: Lomonosov Porcelain into Imperial Porcelain Factory (Europe table: "Formerly Lomonosov").
- Alias rows: Royal Delft = De Koninklijke Porceleyne Fles; Hartkopf = Julius Kirschner & Sohn; KPM = Königliche Porzellan-Manufaktur = Royal Porcelain Manufacture Berlin; Verbilki = Gardner Manufacture.
- Register merges listed in "alias_merges" (these names are not harvest rows): Moccamaster -> Technivorm; Kai Europe -> Kai Group (IVSH lists Kai Europe GmbH, Solingen); Kenwood Chef -> Kenwood; Instant Pot / Instant Brands (register: "Instant Pot Brands"); Lomonosov Porcelain Factory (F2) = Imperial Porcelain Factory.

## cross_tag (known brands that should also carry B5)
- OXO (register: OXO, now B6, J5): Wikipedia Category:Kitchenware brands and Category:Home appliance brands (OXO kitchen utensils brand), both fetched; also on Good Housekeeping 2027 Kitchen Awards page.
- Lobmeyr (register: J. & L. Lobmeyr, now B3): audit note (drinking glasses); not re-fetched in this pass.
- Holmegaard (register: Holmegaard Glasværk, now B4): audit note (drinking glasses/tableware); Holmegaard Glassworks appears in the Category:Glassmaking companies navbox on the fetched Borosil article.
- Kähler (register: Kähler, now B4): audit note (tableware); not re-fetched.
- Bitossi (register: Bitossi Ceramiche, now B4): audit note (tableware); not re-fetched.
- Gaggenau (register: Gaggenau, now G3): Wikipedia Category:Home appliance brands (fetched).
- Wolf (register: Wolf, now G3): audit note (ranges/cooking appliances); not on fetched pages.
- Officine Gullo (register: Officine Gullo, now G3): audit note (cooking units); not re-fetched.

## Tier rules applied
- cultural: Wikipedia category members; porcelain-list rows whose company cell links the brand's own article (any language Wikipedia); own articles (Zhang Xiaoquan, Borosil, Paşabahçe, Crown Lynn, Shtamp, Punzo family); Bat Trang Museum page; NGV; Tokyo Teshigoto; China Time-Honored Brand (Wangmazi); Royal Warrant (Caverswall, William Yeoward).
- quality: Red Dot, Good Housekeeping awards, SCA and World of Coffee awards, Stiftung Warentest, EPV label, Homo Faber, Saveur test pick, and independent press that states craft or materials (Kwangjuyo, Skeppshult, Bordallo Pinheiro, Carrol Boyes, Mahlkönig, Suzuki Morihisa, Odate Kogeisha, Zhangqiu woks, Santa Clara and San Lucas workshops, Murano furnaces on the Spinzi dealer page, Home & Decor workshops).
- listed: IVSH, Knifewear, Seisuke, Chubo, Riess shop, Whole Latte Love, Takefu member list, KOCCA directory, Japan Craft Expo exhibitor rows; red-link or unlinked list rows (incl. Royal Fernwood -> Dankotuwa article, Pentik -> founder article); own and parent-company sites; retailer pages (Manufaktum, Butch, Musubi Kiln, importfood); a readers' popularity survey (Ss Brewtech, Blichmann, Spike, Anvil); business press without quality claims (Preethi, Sumeet, Essen).
- seller: Moroccan Tagines, Page of Tea, SiYuTao Teapot, Usta & Co., Verve Culture, Yoshien, Almohite Cooperative (Safi).

## Regions (64: renown 15, no renown 49)
- Czechia / Bohemia: renown=False; brands kept 3. Encyclopedia list or category page; states no regional renown.
- Hungary: renown=False; brands kept 4. Encyclopedia list or category page; states no regional renown.
- Denmark / Norway / Finland / Sweden (Nordic): renown=False; brands kept 8. Encyclopedia list or category page; states no regional renown.
- Portugal: renown=False; brands kept 3. Encyclopedia list or category page; states no regional renown.
- Russia: renown=False; brands kept 5. Encyclopedia list or category page; states no regional renown.
- Poland: renown=False; brands kept 3. Encyclopedia list or category page; states no regional renown.
- Turkey: renown=False; brands kept 5. Encyclopedia list or category page; states no regional renown.
- Iran (Middle East): renown=False; brands kept 2. Encyclopedia list or category page; states no regional renown.
- United Arab Emirates (Middle East): renown=False; brands kept 1. Encyclopedia list or category page; states no regional renown.
- Japan: renown=False; brands kept 5. Encyclopedia list or category page; states no regional renown.
- South Korea / Taiwan / Vietnam / Sri Lanka (Asia): renown=False; brands kept 5. Encyclopedia list or category page; states no regional renown.
- India / South Asia: renown=False; brands kept 3. Encyclopedia list or category page; states no regional renown.
- South Africa (Sub-Saharan Africa): renown=False; brands kept 1. Encyclopedia list or category page; states no regional renown.
- Brazil / Colombia (Latin America): renown=False; brands kept 3. Encyclopedia list or category page; states no regional renown.
- United Kingdom / Ireland: renown=False; brands kept 8. Encyclopedia list or category page; states no regional renown.
- France: renown=False; brands kept 3; dropped (not shown) ['Bernardaud']. Encyclopedia list or category page; states no regional renown.
- Italy: renown=False; brands kept 1. Encyclopedia list or category page; states no regional renown.
- United States: renown=False; brands kept 4. Encyclopedia list or category page; states no regional renown.
- Japan - Echizen / Takefu (Fukui): renown=False; brands kept 3; dropped (not shown) ['Takefu Knife Village members', 'Masakage', 'Ryusen', 'Masutani Hamono']. Cooperative member page; no renown statement.
- Japan - Sakai (Osaka): renown=False; brands kept 3; dropped (not shown) ['Kagekiyo', 'Hado Sakai', 'Touroku Sakai', 'Aritsugu']. Retailer brand list giving locations only.
- Japan - Seki (Gifu): renown=False; brands kept 8; dropped (not shown) ['Misono', 'Kai Group']. Retailer brand list giving locations only.
- Japan - Sanjo / Tsubame (Niigata): renown=False; brands kept 2; dropped (not shown) ['Fujimoto', 'Yoshikane', 'Tojiro', 'Glestain']. Retailer brand list giving locations only.
- Japan - Tosa (Kochi): renown=False; brands kept 0; dropped (not shown) ['Haruyuki', 'Tetsujin Hamono']. Retailer brand list giving locations only.
- Hong Kong / Taiwan (East Asia): renown=False; brands kept 2. Retailer brand list giving locations only.
- Germany - Solingen: renown=False; brands kept 5; dropped (not shown) ['Zwilling J. A. Henckels', 'Wüsthof', 'Güde', 'Böker', 'Burgvogel', 'Teckel Messer (Manufaktur Solinger Kotten)', 'Herbertz', 'Giesen & Forsthoff', 'F. Dick']. Trade-association member directory; no renown statement.
- France - Thiers: renown=False; brands kept 1; dropped (not shown) ['K Sabatier', 'Sabatier Diamant', 'Forge de Laguiole', 'Laguiole en Aubrac', 'Opinel']. Maker's own site (Thiers-Issard); no independent renown statement.
- United Kingdom - Sheffield: renown=False; brands kept 0; dropped (not shown) ['Viners', 'Arthur Price', 'David Mellor', 'Richardson Sheffield', 'Robert Welch']. Cutlers' Company page speaks of "Sheffield's proud heritage" and standards, not renown; no named brands on it.
- Italy - Lombardy/Piedmont/Marche: renown=False; brands kept 15. Encyclopedia list or category page; states no regional renown.
- Germany - appliances: renown=False; brands kept 11. Encyclopedia list or category page; states no regional renown.
- Turkey (Middle East/Europe): renown=False; brands kept 4; dropped (not shown) ['Kütahya Porselen', 'Bonna Porselen']. Encyclopedia list or category page; states no regional renown.
- China / East Asia: renown=False; brands kept 6; dropped (not shown) ['Gongniu']. Encyclopedia list or category page; states no regional renown.
- Japan - rice cookers and appliances: renown=False; brands kept 7. Encyclopedia list or category page; states no regional renown.
- Latin America: renown=False; brands kept 2; dropped (not shown) ['Tramontina']. Encyclopedia list or category page; states no regional renown.
- Sub-Saharan Africa / South Africa: renown=False; brands kept 1; dropped (not shown) ['Aboso Glass Factory']. Encyclopedia list or category page; states no regional renown.
- South Asia: renown=False; brands kept 6; dropped (not shown) ['Vinod Intelligent Cookware', 'TTK Prestige', 'Hawkins']. Encyclopedia list or category page; states no regional renown.
- Southeast Asia: renown=False; brands kept 2; dropped (not shown) ['Chue Chin Hua', 'Royal Selangor']. Encyclopedia list or category page; states no regional renown.
- Oceania: renown=False; brands kept 6. Encyclopedia list or category page; states no regional renown.
- Japan - Morioka/Oshu (Iwate): renown=True ("Why is Nambu Ironware Considered the Best Japanese Cast Iron Kettles?"); brands kept 3; dropped (not shown) ['Suzuki Morihisa', 'Oitomi', 'Kamasada']
- Austria: renown=False; brands kept 2. Riess brand shop (own site).
- Italy - Murano: renown=True ("the Venetian island has been home to the most respected makers on the planet"); brands kept 4; dropped (not shown) ['Barovier & Toso', 'Moser']
- Czechia / Bohemia - glass: renown=False; brands kept 1; dropped (not shown) ['Moser']. Encyclopedia list or category page; states no regional renown.
- China - Hangzhou: renown=False; brands kept 1. Article on one shop; no regional renown.
- Mexico - Puebla: renown=True ("By the mid-1600s, Puebla had become the most important center for earthenware in New Spain."); brands kept 1; dropped (not shown) ['Talavera Armando']
- South Korea - bangjja brassware: renown=False; brands kept 0. Museum page on bangjja yugi; no regional renown statement and no makers named.
- Italy - Deruta (Umbria): renown=True ("Deruta is a hilltop town in Umbria that has been synonymous with Italian Renaissance maiolica ceramics since the 13th century."); brands kept 1
- Central Asia - Uzbekistan (Rishtan, Fergana): renown=True ("Rishtan continues to live up to its legacy as the home of traditional Rishtan ceramics"); brands kept 1; dropped (not shown) ['Usta & Co.']
- Southeast Asia - Vietnam (Bat Trang): renown=True ("its small workshops pack a serious pottery punch"); brands kept 0; dropped (not shown) ['Soul of Vietnam (Vu Duc Thang)', 'Bat Trang Museum Atelier']. No named makers on the page.
- South Asia - India (Bidar, Moradabad, Swamimalai): renown=False; brands kept 0. IBEF product page states Bidri originated in Bidar, not renown; no makers named.
- China - Yixing (Jiangsu): renown=True ("The pottery made from the clay is named Zisha ware, among which the best known is Zisha teapot"); brands kept 0; dropped (not shown) ['Yixing Zisha Factory No. 1', 'Yoshien', 'Page of Tea', 'SiYuTao Teapot']. CNIPA geographical-indication document; no makers named.
- Morocco: renown=True ("Salé potters, today gathered at the Oulja complex, are known for green-glazed ware"); brands kept 0; dropped (not shown) ['Moroccan Tagines', 'Verve Culture']. Tour-operator craft page; no named sellers.
- Mexico - Santa Clara del Cobre (Michoacán): renown=True ("Santa Clara del Cobre best known as the town of coppersmiths"); brands kept 1; dropped (not shown) ['Punzo family workshop (Santa Clara del Cobre)']. Quoted from a link caption in the article.
- China - Zhangqiu (Shandong): renown=True ("a model of national intangible cultural heritage"); brands kept 1
- Japan - Tokyo (Edo Kiriko): renown=True ("In Tokyo, the local government recognises two classes of traditional crafts in glass: Edo Kiriko and Edo Glass."); brands kept 3; dropped (not shown) ['Kagami Crystal']
- Japan - Odate (Akita): renown=True ("Magewappa craft is a specialty of the little Odate city"); brands kept 1
- Japan - Tokoname (Aichi): renown=True ("the town is known for its rich pottery heritage and masterful craftsmanship"); brands kept 1. Retailer page.
- Japan - Takaoka (Toyama): renown=False; brands kept 1. Exhibitor's own blurb ("Carrying the legacy of Takaoka copperware"); no renown statement.
- Spain - Albacete: renown=False; brands kept 1. Arcos's own history page.
- Poland - Bolesławiec: renown=False; brands kept 1. Company profile (self-description).
- Portugal - Caldas da Rainha: renown=False; brands kept 1. Press feature on the brand; no regional renown statement.
- Russia - Tula: renown=False; brands kept 1. Company article lists samovars among products; no regional renown.
- India - Odisha (kansa): renown=False; brands kept 1. Zishta's own shop page.
- Sub-Saharan Africa - recycled handblown glass (Eswatini, Kenya): renown=False; brands kept 1; dropped (not shown) ['Kitengela Glass']. Homo Faber maker page; no regional renown statement.
- Mexico - San Lucas Evangelista, Tlajomulco (Jalisco): renown=True ("los famosos metates y molcajetes que le han valido el nombre de “Tierra del molcajete”"); brands kept 3
- Turkey - Gaziantep (Bakırcılar Çarşısı): renown=True ("Why is Gaziantep so famous for copper?"); brands kept 0. No named makers on the page.

## Caveats
- The 18 porcelain and 10 appliance-category "regions" are country groupings built from encyclopedia lists; none states renown. They work as browse groupings but not as renowned divisions.
- Knifewear regions (Sakai, Seki, Sanjo, Tosa) are kept only for names on page 2 (the cited page); Kagekiyo, Hado, Touroku Sakai, Fujimoto, Glestain and Tetsujin are on pages 1 and 3. Region renown for the Japanese knife towns needs an independent page.
- Murano quality rests on a dealer's editorial (Spinzi), and Bat Trang's renown on a light phrase in The Kitchn. Both are worth a second look.
- Lobmeyr, Kähler, Bitossi, Wolf and Officine Gullo cross-tags come from the audit's notes; this pass fetched no page for them.
