# VERIFY J2 Fish & Seafood (lean mode)

Rows checked: 228 (+ Abba alias row for Kalles). By tier: {'quality': 62, 'cultural': 107, 'listed': 38, 'seller': 21}. Not shown: 22 (15 with no saved page; 7 Serious Eats/F&W rows whose raw page is truncated). Deferred to DEFER_J2.json: 7 (oishii-desu blog, New Worlder podcast). CITES flagged: 11. Regions: 37, renown 18.

Fetches: 1 call, 3 URLs (Merimbula News Weekly, oishii-desu, Scotsman stub). No new research.

## Audit fixes applied
- Serious Eats contenders (Bar Harbor, Gonsalves, Henry & Lisa's, Maria (Conservas), Brunswick (sardines)) and Bacalalo-ranking names (Lemberg Kaviar, Nacarii), Armatore: listed.
- GFA rows: tier quality; years from gfa_year_map.json in notes; "2026" labels removed.
- Aliases: Ati Manal -> Ati Manel; Matiz España -> Matiz (F&W favourite -> quality, src2); Kaluga Queen -> Hangzhou Qiandaohu Xunlong; Kalles -> Abba.
- Homonym:true: Fukusaya (mentaiko), Minerva (conservas), Scout (tinned seafood), Brunswick (sardines); Tetsujin (katsuobushi) and Yamaki (bonito flakes) are in DEFER.
- Miss Can country Portugal. Maine Coast Fishermen's Association and Armatore kept in J2 with a note (J5 already merged).
- Same-company register matches (merge adds J2): Cure Cooking, Island Trollers, Fish (Sausalito) ~ FISH. (J1). Patagonia Provisions rel Patagonia.

## Accuracy sample (seed 7, 15 rows)

| brand | shown | tier |
|---|---|---|
| Sea Sisters | False | quality |
| Pacific Andes | True | cultural |
| Alex Spink & Sons | True | cultural |
| Loja das Conservas | True | seller |
| Lox, Box and Barrel | True | quality |
| Pure Alaska Salmon Company | True | quality |
| Hazelgrove Oysters | True | quality |
| Conservas El Capricho | True | cultural |
| Vital Choice | True | quality |
| Conservas Lago Paganini | False | listed |
| Röda Ulven | True | cultural |
| Maine Coast Fishermen's Association | True | quality |
| Dunns of Dublin | True | cultural |
| Pacific Seafood | True | cultural |
| Gulf of Maine Conservas | True | quality |

## Regions

| region | renown | quote / note | brands |
|---|---|---|---|
| Scotland (Arbroath, Angus) | True | The Smokie has a protected status under European law (PGI Status) | 11 |
| Italy (Cetara, Amalfi coast) | False | seller praise cannot establish renown | 1 |
| United States (Pacific Northwest, Alaska, California) | False | no renown statement on src page | 5 |
| Spain / Portugal (Galicia, Cantabria, Matosinhos) | False | no renown statement on src page | 7 |
| France (Marennes-Oléron, Atlantic coast) | False | PGI holder own site; page not saved | 0 |
| Latvia (Riga, Salacgrīva) | False | own site; page not saved | 0 |
| France (Paris) | False | own site | 0 |
| Japan (Makurazaki, Kagoshima) | False | own site | 0 |
| New Zealand | False | own site | 0 |
| Italy (Lombardy) | False | own site | 0 |
| England (Whitstable, Kent) | True | The Whitstable area is renowned for the quality of its oysters | 3 |
| Norway (Lofoten) | True | Tørrfisk fra Lofoten AS manages both the Norwegian and European Protected Geographical Indication (PGI) for stockfish | 1 |
| Cantabrian coast anchovies (Santoña, Laredo, Castro Urdiales) | False | no renown statement on src page | 12 |
| Basque coast (Bermeo, Ondarroa) | False | no renown statement on src page | 5 |
| Japan (Fukuoka / Hakata mentaiko) | True | Fukuoka Prefecture is the place for enjoying the best mentaiko! | 6 |
| Japan (Lake Hamana unagi) | True | Registration No.177 浜名湖うなぎ（Lake Hamanako Unagi） | 1 |
| Japan (Kagoshima katsuobushi: Makurazaki, Ibusuki) | True | The region continues to preserve the traditional method of Honkare Honbushi | 1 |
| Japan (Shimonoseki fugu) | True | Registration No.19 Shimonoseki Fuku (GI register page) | 1 |
| Japan (Echizen snow crab, Fukui) | True | the area has been traditionally known as a production site of snow crabs | 1 |
| Japan (Wakasa Obama) | True | Registration No.45 若狭小浜小鯛ささ漬（Wakasa Obama Kodai Sasazuke） | 1 |
| Japan (Miyagi Sanriku salmon) | True | MIYAGI SALMON is a high qua[lity]... Miyagi Prefecture is suitable for coho salmon production | 1 |
| South Korea (Yeonggwang, Beopseongpo) | True | 2015 국가브랜드대상 ... 영광굴비 - 연 매출 3500억 올리는 지역 대표 브랜드 | 0 |
| South Korea (Ganggyeong, Nonsan) | True | 강경 젓갈시장은 자타가 공인하는 전국 최대의 젓갈 집산지이자 공급지 | 2 |
| Malaysia (Melaka, Penang, Kedah, Sabah) | True | Melaka, Penang, Kedah, and Sabah are renowned for producing high-quality belacan | 0 |
| Portugal (Lisbon conservas) | False | no renown statement on src page | 4 |
| United States (New York appetizing) | False | no renown statement on src page | 2 |
| Sweden (Bohuslän herring coast) | True | Klädesholmen ... The center for herring | 1 |
| England (London fishmongers) | False | no renown statement on src page | 6 |
| Australia (NSW Sapphire Coast oysters) | True | the Sapphire Coast region has an exceptional reputation in the culinary world | 3 |
| Italy (Sardinia, Cabras bottarga) | True | Cabras, per la bottarga arriva il Presidio Slow Food | 1 |
| Thailand (Bang Bo, Samut Prakan) | True | the most famous of them all is Pla Salid Bangbo, or Bangbo Snakeskin Gourami | 1 |
| Hong Kong (Sheung Wan dried seafood street) | True | Hong Kong has been one of the main centres of the trade for years | 0 |
| Ireland (Carlingford Lough) | False | no renown statement on src page | 2 |
| Iran (Caspian caviar) | False | src page not saved | 0 |
| Iceland (harðfiskur, Westfjords) | False | src page not saved | 0 |
| Netherlands (Hollandse Nieuwe herring) | False | no renown statement on src page | 1 |
| Japan (kamaboko: Odawara, Niigata, Nanao, Nagato) | False | no renown statement on src page | 3 |

## Not shown

- Bar Harbor: https://www.seriouseats.com/best-canned-sardines-taste-test-11791642
- Gonsalves: https://www.seriouseats.com/best-canned-sardines-taste-test-11791642
- Henry & Lisa's: https://www.seriouseats.com/best-canned-sardines-taste-test-11791642
- Maria (Conservas): https://www.seriouseats.com/best-canned-sardines-taste-test-11791642
- Siesta Co.: https://www.foodandwine.com/this-tasting-put-the-time-old-saying-there-s-plenty-
- Sea Sisters: https://www.independent.co.uk/extras/indybest/food-drink/best-tinned-fish-sardin
- Brīvais Vilnis: https://brivaisvilnis.lv/en/about-the-company
- Groupement Qualité Huîtres Marennes Oléron: https://www.huitresmarennesoleron.info/UK-info.html
- Nishimura Asamori Shoten: https://n-asamori.jp/english
- Marumo (Makurazaki katsuobushi): https://kk-marumo.co.jp/wp/wp-content/uploads/2021/06/marumo_brochure_en.pdf
- Tateaki Suisan: https://tateaki.co.jp/en
- Makurazaki Marine Products Processing Industries Cooperative: https://www.maff.go.jp/e/policies/intel/gi_act/register/250715_3.html
- Sanford (New Zealand): https://www.sanford.co.nz/operations/aquaculture/mussels
- Talley's: https://www.talleys.co.nz/
- Conservas Lago Paganini: https://conservaslagopaganini.com/en
- Australia's Oyster Coast: https://www.begadistrictnews.com.au/story/7706716/far-south-coast-oyster-produce
- Dornika Caspian: https://hongkong.mfa.gov.ir/en/newsview/760813
- Scout (tinned seafood): https://www.foodandwine.com/this-tasting-put-the-time-old-saying-there-s-plenty-
- Brunswick (sardines): https://www.seriouseats.com/best-canned-sardines-taste-test-11791642
- Von Iceland: https://grapevine.is/mag/2023/02/15/how-its-made-hardfiskur/
- Harðfiskverkun Finnboga: https://icelandmonitor.mbl.is/news/eat_and_drink/2019/06/12/how_dried_fish_is_ma
- Breki: https://icelandmonitor.mbl.is/news/culture_and_living/2015/01/21/dried_fish_rece
