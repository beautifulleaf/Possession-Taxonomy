# AUDIT J2 Fish & Seafood (cold audit + retry round)

## Accuracy

25/25 shown on their src pages (Gonsalves and Siesta Co. only via excerpt fetch: raw full_content of Serious Eats/F&W/Wirecutter is truncated to a few lines). 3 substantive tier errors (Gonsalves contender tiered premium; Armatore and Lemberg rest on seller praise). 8 of 10 sampled Good Food Award rows say '2026' but the src page aggregates all years 2017-2026; only Fishpatricks and Cure Cooking won in 2026. Error rate 3/25 = 12% substantive; 11/25 = 44% counting the year mislabels.

| brand | shown | claim | note |
|---|---|---|---|
| Lerøy | True | True | list row links to own article |
| Young's Seafood | True | True | list row links to own article |
| Pescanova | True | True | list row links to own article |
| Rappahannock Oyster Co. | True | True | list row links to own article |
| Handy Seafood | True | True | list row links to own article |
| Clean Seas Seafood | True | True | list row links to own article |
| Pacific Seafood | True | True | list row links to own article |
| Regalis Foods | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2017 (not 2026) |
| Cure Cooking | True | yes | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2022-2026 incl. 2026 |
| Gulf of Maine Conservas | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2023 (not 2026) |
| Lox, Box and Barrel | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2017-2018 (not 2026) |
| Fishpatricks | True | yes | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2026 ok |
| Ekone Oyster Co | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2017 (not 2026) |
| California Caviar Company | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2021-2022 (not 2026) |
| Louisiana Caviar Company | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2019 (not 2026) |
| Fishpeople | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2019 (not 2026) |
| OneForNeptune | True | partial | juried Good Food Award winner confirmed; the /winners/fish page aggregates 2017-2026, year pages show 2020 (not 2026) |
| Gonsalves | True | partial | shown only as one of 17 contenders (raw full_content truncated; excerpt fetch lists it). Contender, not winner: layer 'premium' wrong -> listed/cultural at most |
| Matiz | True | True | #18 TasteAtlas; duplicate of harvest 'Matiz España' |
| Conservas Braseadas Güeyu Mar | True | True | #9, Ribadesella |
| Armatore | True | partial | 'Spitzenproduzent' is a retailer's product-page praise (SELLER PRAISE) -> listed, not premium; colatura is a fish-sauce-like condiment, borderline J5 |
| Siesta Co. | True | True | named favourite (mussels); raw fetch truncated, excerpt fetch confirms |
| Lemberg Kaviar | True | partial | ranked #2 in a ranking by a caviar seller that says it is not neutral -> listed |
| Bacalalo | True | True | own page: Mercat del Ninot seller since 1990; seller role, own site only |
| Caputo's | True | True | named as US distributor of tinned fish brands (seller) |

## Additions: 135 brands ({'cultural': 111, 'premium': 24}; 22 sellers), 28 regions

By country: UK 31, Japan 20, Spain 16, Portugal 10, US 8, Germany 6, Italy 5, Ireland 4, Australia 4, Norway 3, Iceland 3, Sweden 2, South Korea 2, France 2, Maldives 2, Iran 2, Netherlands 2, Canada 2, China 1, Russia 1, Philippines 1, Switzerland 1, South Africa 1, Brazil 1, Finland 1, Thailand 1, Hong Kong 1, Lithuania 1, Morocco 1

| brand | layer | country | dept | region | says |
|---|---|---|---|---|---|
| José Peña Conservas | cultural | Spain | tinned fish | Galicia | #12 in TasteAtlas best canned sardines in the world (audience-rated); Pontevedra |
| La Gondola | cultural | Portugal | tinned fish | Northern Portugal (Matosinhos) | #14 in TasteAtlas best canned sardines in the world (audience-rated); Matosinhos |
| South Bay Wild | premium | US | smoked fish |  | Good Food Award winner (juried blind tasting): Smoked Black Cod; Morro Bay, California |
| Wooden Spoons | premium | US | fish pâté & rillettes |  | Good Food Award winner (juried): Salmon Rillettes; Berkeley, California |
| Fish (Sausalito) | premium | US | fish sausage |  | Good Food Award 2024 winner (juried): McFarland Springs Trout Dog; Sausalito, California |
| EPIC Provisions | premium | US | fish jerky |  | Good Food Award winner (juried): Smoked Salmon Strips / Maple Glazed & Smoked Tender Salmon Bites; Austin, Texas |
| Bon Appétit Management Company (Abbey Kitchen) | premium | US | smoked salmon |  | Good Food Award 2018 (juried): Hardwood Hot Smoked Columbia River Chinook Salmon; Saint Benedict, Oregon |
| Alex Spink & Sons | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: where to buy authentic Arbroath Smokies made using the traditional method (PGI) |
| Arbroath Fisheries (seller) | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: seller/maker of authentic Arbroath Smokies |
| Arbroath Smokies Direct (seller) | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: seller of authentic Arbroath Smokies |
| B. Swankie Fishmongers (seller) | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: authentic Arbroath Smokies; Swankie a traditional smokie family name (List) |
| David Cargill Fishmongers (seller) | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: authentic Arbroath Smokies |
| Derek Spink Fishmerchants | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail; also named by The List among remaining Fit o' the Toon producers |
| E & O Fish | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: authentic Arbroath Smokies |
| M & M Smith | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: authentic Arbroath Smokies |
| M & M Spink | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail; named by The List among remaining smokie producers |
| Stuart's Fresh Fish (seller) | cultural | UK | smoked haddock | Scotland (Arbroath, Angus) | VisitScotland Arbroath Smokie Trail: authentic Arbroath Smokies |
| Kaluga Queen | cultural | China | caviar | China (Qiandao Lake, Zhejiang) | own Wikipedia article: largest caviar producer in the world (~60% of world production), Qiandao Lake; supplies 21 of 26 Paris 3-star restaurants. SAME company as register 'Hangzhou Qiandaohu Xunlong' (merge as alias). CITES flag |
| Russian Caviar House | cultural | Russia | caviar |  | own Wikipedia article: Russian black caviar producer founded 1978 (aquaculture), Cherepovets. CITES flag |
| Conservas Ramirez | cultural | Portugal | tinned fish | Northern Portugal (Matosinhos) | own Wikipedia article: Portuguese canned fish producer created 1853 (oldest active cannery), 16 brands incl. Cocagne, Tomé, Al-Fares, Gabriel |
| Cofaco | cultural | Portugal | tinned tuna | Azores | own Wikipedia article: Portuguese tuna canner (Azores); main brands Bom Petisco, Pitéu, Líder, Ás do Mar, Santamaria |
| Bom Petisco | cultural | Portugal | tinned tuna | Azores | main Cofaco brand of tinned tuna, Portuguese everyday icon (brand row in Cofaco article) |
| Seasalter Shellfish (Whitstable) | cultural | UK | oysters | England (Whitstable, Kent) | named in the UK Protected Food Name (PGI) application for Whitstable Oysters: only company farming oysters on its Pollard Ground beds, descendant of the 1893 Seasalter & Ham Oyster Fishery Co |
| The Whitstable Oyster Fishery Company | cultural | UK | oysters | England (Whitstable, Kent) | named in Whitstable Oysters PGI application: incorporated by Act of Parliament 1793 as Company of Free Fishers and Dredgers of Whitstable |
| The Faversham Oyster Fishery Company | cultural | UK | shellfish | England (Whitstable, Kent) | named in Whitstable Oysters PGI application; cited as oldest existing company in the world (Guinness) |
| Tørrfisk fra Lofoten AS | cultural | Norway | stockfish | Norway (Lofoten) | alliance of Lofoten stockfish producers holding the PGI 'Tørrfisk fra Lofoten' (Norway 2007, first Norwegian EU PGI 2014) |
| Lofoten Fisk AS | cultural | Norway | stockfish | Norway (Lofoten) | stockfish company presenting the PGI Tørrfisk fra Lofoten at the FHF stockfish conference 2016 (thin: presenter's company) |
| Russ & Daughters (seller) | cultural | US | smoked fish | United States (New York appetizing) | #1 TasteAtlas best-rated smoked fish in USA (Gaspe Nova smoked salmon); New York appetizing shop |
| Barney Greengrass (seller) | cultural | US | smoked sturgeon | United States (New York appetizing) | #2 TasteAtlas best-rated smoked fish in USA (smoked sturgeon); New York |
| A Passion for Seafood | cultural | US | smoked fish |  | TasteAtlas US smoked fish list #6: Ness Point Smokehouse cold smoked wild bass |
| Macneil's Smokehouse | cultural | UK | smoked salmon |  | #2 TasteAtlas best-rated smoked salmons in Europe (beechwood hot kiln smoked salmon), Rushock, England |
| Ahumados Domínguez | cultural | Spain | smoked salmon |  | #4 TasteAtlas best-rated smoked salmons in Europe (Salmón Ahumado Suprême), Alcorcón |
| East Neuk Kilnhouse | cultural | UK | smoked salmon | Scotland | #5 TasteAtlas best-rated smoked salmons in Europe (hot smoked salmon), Anstruther |
| Secret Smokehouse | premium | UK | smoked salmon | England (London cure smoked salmon PGI) | olive magazine smoked salmon taste test 8/10 (London cure, PGI); also #6 TasteAtlas Europe smoked salmon |
| Kish Fish | cultural | Ireland | smoked salmon |  | #8 TasteAtlas best-rated smoked salmons in Europe (Baily & Kish), Dublin |
| Dunns of Dublin | cultural | Ireland | smoked salmon |  | #9 TasteAtlas best-rated smoked salmons in Europe, Dublin |
| Staithe Smokehouse | cultural | UK | smoked salmon |  | #10 TasteAtlas best-rated smoked salmons in Europe, Brancaster Staithe, Norfolk |
| Bleikers Smokehouse | premium | UK | smoked salmon |  | winner (10/10) olive magazine smoked salmon taste test: oak smoked salmon |
| John Ross Jr | premium | UK | smoked salmon | Scotland | olive magazine smoked salmon taste test 7/10: traditional Scottish smoked salmon (Aberdeen) |
| Anchoas Hazas | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #1 TasteAtlas best-rated preserved anchovies in Europe and #1 canned fish in Spain; Lastres |
| La Castreña | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #2 TasteAtlas preserved anchovies in Europe; Sámano (Castro Urdiales) |
| Conservas Codesa | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #3 TasteAtlas preserved anchovies in Europe; Laredo |
| Conservas Catalina | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #4 TasteAtlas preserved anchovies in Europe; Santoña |
| Conservas El Capricho | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #5 TasteAtlas preserved anchovies in Europe, #2 canned fish in Spain; Santoña |
| Rosalita | cultural | Spain | tinned anchovies |  | #8 TasteAtlas preserved anchovies in Europe (Anchoas Suaves XL); Las Rozas |
| Conservas Mª Asun Velar | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #9 TasteAtlas preserved anchovies in Europe; Castro Urdiales |
| Magno Food | cultural | Italy | tinned anchovies |  | #11 TasteAtlas preserved anchovies in Europe (Cantabrian anchovies in Beppino Occelli butter); Naples |
| Nettuno | cultural | Italy | salted anchovies | Italy (Cetara, Amalfi coast) | #14 TasteAtlas preserved anchovies in Europe: alici salate, Cetara |
| Fredo La Estrella del Norte | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #15 TasteAtlas preserved anchovies in Europe; Santoña |
| Conservas M.A. Revilla | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #17 TasteAtlas preserved anchovies in Europe; Santoña |
| Conservas Emilia | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #18 TasteAtlas preserved anchovies in Europe; Santoña |
| Anchoas La Capitana | cultural | Spain | tinned anchovies | Cantabrian coast anchovies | #19 TasteAtlas preserved anchovies in Europe; Laredo |
| Agromar | cultural | Spain | tinned fish |  | #20 TasteAtlas preserved anchovies in Europe; Gijón |
| Conservas Serrats | cultural | Spain | tinned tuna | Basque coast (Bermeo) | #12 TasteAtlas canned fish in Spain (ventresca de bonito del norte); Bermeo |
| Arroyabe | cultural | Spain | tinned tuna | Basque coast (Bermeo) | #16 TasteAtlas canned fish in Spain (bonito del norte); Bermeo |
| Röda Ulven | cultural | Sweden | fermented herring | Sweden (Höga Kusten surströmming) | #2 TasteAtlas best-rated preserved fish in Northern Europe: surströmming, Skagshamn |
| Delicius | premium | Italy | tinned anchovies |  | olive magazine anchovies taste test 8/10 (Superior anchovy fillets in olive oil); Italian brand |
| Alfred Enderby | premium | UK | smoked haddock | England (Grimsby traditional smoked fish PGI) | Falstaff (Sudi Pigott 2021): 'for the best smoked haddock, head to Aldred [sic] Enderby in Grimsby', traditional smokehouse since 1918, PGI |
| J. Laurie & Sons | premium | UK | kippers | Scotland | Falstaff 2021: family company in the Scottish Highlands, numerous awards for Jaffys Mallaig kippers |
| Rock-a-Nore fishmongers (seller) | cultural | UK | smoked fish | England (Hastings) | Falstaff 2021: Hastings fishmonger selling freshly smoked anchovies |
| Kanefuku | cultural | Japan | pollock roe (mentaiko) | Japan (Fukuoka / Hakata mentaiko) | Fukuoka Prefecture tourism guide: one of the karashi mentaiko makers of Fukuoka (in-house roe sourcing, twice-pickling); Just One Cookbook: 'one of the most famous brands of mentaiko' |
| Fukusaya (mentaiko) | cultural | Japan | pollock roe (mentaiko) | Japan (Fukuoka / Hakata mentaiko) | Fukuoka Prefecture tourism guide: karashi mentaiko maker of Fukuoka. HOMONYM CHECK: not the Nagasaki castella house Fukusaya |
| Kabata | cultural | Japan | pollock roe (mentaiko) | Japan (Fukuoka / Hakata mentaiko) | Fukuoka Prefecture tourism guide: founded 1921 as a pickle shop, now a karashi mentaiko maker |
| Fukutaro | cultural | Japan | pollock roe (mentaiko) | Japan (Fukuoka / Hakata mentaiko) | Fukuoka Prefecture tourism guide: karashi mentaiko maker using only selected Alaska pollock roe |
| Barrio Fiesta | cultural | Philippines | salted fermented shrimp (bagoong) |  | Malaya Business Insight 2020: Prime Global Corp's Barrio Fiesta, the only bagoong brand produced and distributed at scale in local and international markets (Filipino household name) |
| Hyeongje Sanghoe (Ganggyeong jeotgal) (seller) | cultural | South Korea | salted fermented seafood (jeotgal) | South Korea (Ganggyeong, Nonsan) | Seoul Shinmun 1996: Ganggyeong jeotgal merchant (Park Cheong-su, 30+ years) at Korea's largest salted-seafood market |
| Sinjin Sanghoe (Ganggyeong jeotgal) (seller) | cultural | South Korea | salted fermented seafood (jeotgal) | South Korea (Ganggyeong, Nonsan) | Seoul Shinmun 1996: Ganggyeong jeotgal market merchant (secretary of the market's merchants' association) |
| Caviar Kaspia | cultural | France | caviar | France (Paris caviar houses) | Falstaff: 'cult status, almost 100 years of Caviar Kaspia' - Paris caviar house founded 1927 by Arcady Fixon, Place de la Madeleine; Groupe Caviar Kaspia took over La Maison du Caviar 2018 (lesrestos). CITES flag |
| La Maison du Caviar | cultural | France | caviar | France (Paris caviar houses) | historic Paris caviar house, taken over by Groupe Caviar Kaspia 2018 ('deux maisons historiques'). CITES flag |
| Balik | premium | Switzerland | smoked salmon |  | Worldcrunch (from Le Temps) 2012: Balik farm, Ebersol (Toggenburg), the 'world's best smoked salmon', Tsar-era recipe; FürSie: 'der beste Räucherfisch der Welt' |
| Conserveira de Lisboa | cultural | Portugal | tinned fish | Portugal (Lisbon conservas) | Lojas com História (Lisbon municipal heritage-shop register): canned fish shop opened 1930, own brands Tricana, Minor and Prata do Mar; Prior: oldest canned fish shop in Lisbon |
| Tricana | cultural | Portugal | tinned fish | Portugal (Lisbon conservas) | Conserveira de Lisboa house brand for larger northern fish (heritage-shop register page) |
| Loja das Conservas (seller) | cultural | Portugal | tinned fish | Portugal (Lisbon conservas) | Prior 'Tin Town' (Lisbon's top purveyors of tinned fish): walk-in shop where every major Portuguese tinned fish manufacturer is represented |
| A Vida Portuguesa (seller) | cultural | Portugal | tinned fish | Portugal (Lisbon conservas) | Prior 'Tin Town': Catarina Portas' shops selling Portuguese conservas (José Gourmet, Tricana, Minerva, Tenório) |
| Dois Dedos de Conserva (seller) | cultural | Portugal | tinned fish | Portugal (Lisbon conservas) | Prior 'Tin Town': Alvalade shop for conservas (Naval, Cocagne, Minerva, Pescarias do Algarve) |
| Minerva (conservas) | cultural | Portugal | tinned sardines |  | Portuguese conservas brand named by Prior among brands stocked by Lisbon's top tinned-fish purveyors (listed only) |
| Klädesholmen Seafood | cultural | Sweden | marinated herring | Sweden (Bohuslän herring coast) | West Sweden tourism: Klädesholmen 'the center for herring'; Klädesholmen Seafood with Salt & Sill appoints the expert jury for Sweden's herring dish of the year |
| Lucky Star | cultural | South Africa | tinned pilchards |  | BusinessTech 2026: 'one of South Africa's most iconic brands' (Oceana's canned pilchards) |
| Gomes da Costa | cultural | Brazil | tinned sardines & tuna |  | Brazilian tinned sardine and tuna brand celebrating 70 years (2026), market leader in canned fish (Nauterra); trade press |
| Rahameeru | cultural | Maldives | tinned tuna |  | Hotelier Maldives 2019: Horizon Fisheries' 'genuinely Maldivian' tuna brand (Maandhoo complex, Laamu), sold in Asian markets (thin; trade press) |
| Carlingford Oyster Company | premium | Ireland | oysters | Ireland (Carlingford Lough) | Great Taste 2021 3-star (Golden Fork shortlist): Louet Feisser Select Carlingford Oysters |
| Rooney Fish | premium | UK | oysters | Ireland (Carlingford Lough) | Great Taste 2021 3-star: Millbay Oysters; Newry, Co. Down |
| The Scottish Salmon Company | premium | UK | smoked salmon | Scotland | Great Taste 2021 3-star: Harris and Lewis Smoked Scottish Salmon (now Bakkafrost Scotland) |
| Goatsbridge Fish Processors | premium | Ireland | smoked trout |  | Great Taste 2025 Golden Fork from Ireland nominee (3-star): Hot Smoked Rainbow Trout Fillets |
| Kuopion Perinnetuote | premium | Finland | smoked trout |  | Great Taste 2026 Golden Fork nominee (3-star): Stone Kiln Cold Smoked Rainbow Trout Fillet |
| Sublime Butter | premium | UK | seafood spread |  | Great Taste 2021 3-star: Ridiculous No55 Lobster & Crab Butter (borderline: seafood spread) |
| Lake Hamanako Aquaculture Fisheries Cooperative | cultural | Japan | eel | Japan (Lake Hamana unagi) | Registered group of Japan GI No.177 Lake Hamanako Unagi (Hamamatsu, Kosai), valued for high fat content, commands higher prices |
| Life of Fish (seller) | cultural | UK | fresh fish | England (London fishmongers) | SheerLuxe directory of the best fishmongers in London: David Palmer's shop (ex-Selfridges fish concession) |
| Moxon's (seller) | cultural | UK | fresh & smoked fish | England (London fishmongers) | SheerLuxe best fishmongers in London: Robin Moxon, with own smokehouse in Wimbledon (salmon, cod, haddock, kippers) |
| Fin & Flounder (seller) | cultural | UK | fresh fish | England (London fishmongers) | SheerLuxe best fishmongers in London: family-run fishmonger at Broadway Market, Hackney |
| The Sea, The Sea (seller) | cultural | UK | fresh fish | England (London fishmongers) | SheerLuxe best fishmongers in London: chef-led fish shop, dry-aged fish, supplies 100+ restaurants |
| The Chelsea Fishmonger (seller) | cultural | UK | fresh fish | England (London fishmongers) | SheerLuxe best fishmongers in London: Rex Goldsmith, hyper-seasonal UK fish |
| La Petite Poissonnerie (seller) | cultural | UK | fresh fish | England (London fishmongers) | SheerLuxe best fishmongers in London: Primrose Hill, day-boat fish (Theo Randall's supplier) |
| Yamakawa Marine Products Processing Industries Cooperative | cultural | Japan | katsuobushi | Japan (Kagoshima katsuobushi: Makurazaki, Ibusuki) | Registered group of Japan GI Ibusuki Katsuobushi (Ibusuki, Kagoshima) |
| Shimonoseki Karato Fish Market Intermediate Wholesaler Cooperative | cultural | Japan | puffer fish (fugu) | Japan (Shimonoseki fugu) | Registered group of Japan GI No.19 Shimonoseki Fuku (puffer fish) |
| Fukui Prefecture Fisheries Cooperative Association | cultural | Japan | snow crab | Japan (Echizen snow crab, Fukui) | Registered group of Japan GI No.69 Echizen Gani (snow crab, incl. boiled) |
| Miyagi Salmon Promotion Association | cultural | Japan | coho salmon | Japan (Miyagi Sanriku salmon) | Registered group of Japan GI No.31 Miyagi Salmon (farmed coho, Sanriku coast) |
| Nodamura Fisheries Cooperative | cultural | Japan | scallop |  | Registered group of Japan GI No.47 Iwate Nodamura Araumi Hotate (scallop) |
| Hamanaka Fishery Products Promotion Council | cultural | Japan | sea urchin |  | Registered group of Japan GI No.135 Hamanaka Youshoku Uni (farmed sea urchin, Hokkaido) |
| Cooperative of Obama Sasazuke Association | cultural | Japan | vinegar-marinated sea bream | Japan (Wakasa Obama) | Registered group of Japan GI No.45 Wakasa Obama Kodai Sasazuke (vinegar-pickled small sea bream) |
| Fukura Fisheries Cooperative | cultural | Japan | puffer fish (fugu) |  | Registered group of Japan GI No.144 Awajishima 3nen Torafugu (three-year tiger puffer, Awaji) |
| Kure Toyoshima Fisheries Cooperative | cultural | Japan | cutlassfish |  | Registered group of Japan GI No.84 Toyoshima Tachiuo (cutlassfish) |
| Jusan Fisheries Cooperative | cultural | Japan | clam |  | Registered group (with Shariki FC) of Japan GI No.23 Jusanko-san Yamato Shijimi (brackish-water clam) |
| Nuovo Consorzio Cooperative Pontis | cultural | Italy | bottarga | Italy (Sardinia, Cabras bottarga) | L'Unione Sarda 2025: Slow Food Presidio for Cabras lagoon bottarga; only Consorzio Pontis may sell bottarga fished in the stagno; Gambero Rosso: consortium of ~130 fishermen |
| L'Oro di Cabras (Fratelli Manca) | cultural | Italy | bottarga | Italy (Sardinia, Cabras bottarga) | Gustiamo (importer page): Fratelli Manca cooperative in Cabras, traditional bottarga process (seller page: listed unless Katie Parla 'one of the best producers' page fetches) |
| Mae Amnuay Bang Bo Gourami | cultural | Thailand | dried & salted fish (pla salid) | Thailand (Bang Bo, Samut Prakan) | Michelin Guide Thailand 2023: well-known three-generation Bang Bo (Samut Prakan) salted gourami (pla salid) producer, OTOP products |
| Shing Lung Hong Company (seller) | cultural | Hong Kong | Chinese mitten crab & dried seafood | Hong Kong (Sheung Wan dried seafood street) | Hong Kong Tourism Board QTS-accredited shop: over half a century, own Tai Lake (Suzhou) farm, high quality hairy crabs and dried seafood (Wing Lok Street, Sheung Wan) |
| Deutsche See | cultural | Germany | fresh & chilled fish |  | Bremen company portrait 2012: Bremerhaven fish and seafood company (founded 1939), Germany's market leader for fish and seafood; owns delicatessen brand BEECK |
| Appel Feinkost | cultural | Germany | tinned herring & mackerel |  | Undercurrent News 2022: market leader in Germany for canned pelagic fish and tuna ('the brand with the lobster', 135+ years per LebensmittelPraxis) |
| Hawesta | cultural | Germany | tinned herring & mackerel |  | Food Chain Magazine: over 100 years of canned fish loved in Germany (Lübeck; Rügen Fisch / Thai Union group) |
| Rügen Fisch | cultural | Germany | tinned fish |  | German fish canner (Sassnitz, Rügen), Thai Union subsidiary owning Hawesta and Ostsee Fisch (trade press) |
| Gottfried Friedrichs | cultural | Germany | smoked salmon |  | LebensmittelPraxis brand portrait: Hamburg fish delicatessen (smoked salmon) 'aus Tradition' (brand directory: listed) |
| Krone Fisch | cultural | Germany | smoked & marinated fish |  | LebensmittelPraxis brand portrait: smoked and marinated salmon, trout, mackerel and herring specialities (brand directory: listed) |
| Vičiūnai Group | cultural | Lithuania | surimi & crab sticks |  | own article in the Lithuanian Universal Encyclopedia (VLE): Kaunas food group, ~158,000 t a year mostly under the Viči brand (surimi crab sticks, fish) |
| Tathra Oysters | premium | Australia | oysters (Sydney rock) | Australia (NSW Sapphire Coast oysters) | Sydney Royal Fine Food Show (juried): champion Sydney rock oyster 2018, 2019, 2021 and 2023, champion aquaculture product 2021 (Nelson Lagoon) |
| Australia's Oyster Coast | premium | Australia | oysters (Sydney rock) | Australia (NSW Sapphire Coast oysters) | Sydney Royal Fine Food Show 2022 (juried): Annual Trophy for Champion Sydney Rock Oyster (Merimbula Bistro Appellation Oyster) and two golds; brand 'Appellation Oysters' |
| Hazelgrove Oysters | premium | Australia | oysters (Sydney rock) | Australia (NSW Sapphire Coast oysters) | Sydney Royal Fine Food Show 2023 Sydney rock oyster medallist |
| Wapengo Rocks Wild Organic Oysters | premium | Australia | oysters (Sydney rock) | Australia (NSW Sapphire Coast oysters) | Sydney Royal Fine Food Show 2023: one gold and two silver medals |
| Caspian Monarque | cultural | Iran | caviar | Iran (Caspian caviar) | New Worlder (Nicholas Gill, James Beard-nominated food writer) 2024: Iranian caviar producer with Caspian sturgeon farms; 'indeed the great stuff'. CITES flag |
| Dornika Caspian | cultural | Iran | caviar | Iran (Caspian caviar) | Iranian consulate Hong Kong announcement: organic caviar company, CITES member, investing in Iranian sturgeon farms (official promotion; listed). CITES flag |
| Stabburet | cultural | Norway | tinned mackerel |  | Store norske leksikon article (and own Wikipedia article): Norwegian food maker (1943, Orkla); section on Stabbur-Makrell, its iconic tinned mackerel in tomato (yellow-and-red tin) |
| Maldives Industrial Fisheries Company | cultural | Maldives | tinned tuna & Maldive fish (smoked dried tuna) |  | own Wikipedia article: state-owned Maldivian fish processor (MIFCO, 1993): canned and frozen tuna, katsuobushi similar to traditional Maldive fish |
| Vishandel Gebroeders Simonis (seller) | premium | Netherlands | Hollandse Nieuwe herring | Netherlands (Hollandse Nieuwe herring) | AD Haringtest (jury of keurmeesters) 2016 winner with a 10, also winner 2015 and second the two years before: best Hollandse Nieuwe herring, The Hague/Scheveningen |
| Vishandel Arenthals (seller) | premium | Netherlands | Hollandse Nieuwe herring | Netherlands (Hollandse Nieuwe herring) | NH Nieuws: best herring of Noord-Holland in the Nationale Haringtest (score 9.5), Alkmaar fish kiosk |
| Nouvelle Aveiro Maroc | cultural | Morocco | tinned sardines |  | OU Kosher certified company page: founded 1946, tinned sardines and mackerel from Moroccan coasts (directory: listed) |
| Scout (tinned seafood) | cultural | Canada | tinned fish |  | Food & Wine 2022 tasting of 20+ tinned fish: 'we also really enjoyed the offerings from ... Scout' (Canadian tinned seafood). HOMONYM: register 'Scout' is a luggage brand (A4), different company |
| Brunswick (sardines) | cultural | Canada | tinned sardines |  | one of 17 contenders in Serious Eats 2025 sardine test (contender only: listed); Connors Bros./Bumble Bee brand. HOMONYM: register 'Brunswick' (E1/E2) is a different company |
| Kibun Foods | cultural | Japan | kamaboko & surimi |  | SeafoodSource market report (FY2018 ranking): Japan's largest fish-paste (kamaboko, chikuwa, crab stick) maker by sales, JPY 46bn; known for 'chi-chiku' |
| Ichimasa Kamaboko | cultural | Japan | kamaboko & surimi |  | SeafoodSource market report (FY2018): Niigata kamaboko maker, second in Japanese fish-paste sales (JPY 35bn) |
| Sugiyo | cultural | Japan | crab stick (surimi) |  | SeafoodSource market report (FY2018): Nanao, Ishikawa; third in Japanese fishcake sales; claims to be the originator of crab-flavoured surimi sticks |
| Fujimitsu Corporation | cultural | Japan | kamaboko |  | own Wikipedia article: kamaboko maker founded 1887 in Senzaki (Nagato, Yamaguchi) |
| Maruha Nichiro (Umios) | cultural | Japan | seafood (frozen, tinned, surimi) |  | own Wikipedia article: major Japanese seafood company (origins 1880, Osaka; merged with Nichiro 2007), renamed Umios March 2026; main competitors Nissui and Kyokuyo |
| Von Iceland | cultural | Iceland | dried fish (harðfiskur) | Iceland (harðfiskur, Westfjords) | Reykjavík Grapevine 2023: Hafnarfjörður family firm making harðfiskur (Icelandic dried fish, sold in almost every Icelandic shop) and Crunchy Fish |
| Harðfiskverkun Finnboga | cultural | Iceland | dried fish (harðfiskur) | Iceland (harðfiskur, Westfjords) | Iceland Monitor (Morgunblaðið) 2019: Ísafjörður harðfiskur maker drying fish the old-fashioned way in a shed, since the mid-1980s |
| Breki | cultural | Iceland | dried fish (harðfiskur) | Iceland (harðfiskur, Westfjords) | Iceland Monitor 2015: Icelandic company relaunching harðfiskur as 80%-protein flakes and fish jerky |

## Regions

| region | speciality | brands |
|---|---|---|
| Scotland (Arbroath, Angus) | Arbroath Smokies PGI hot-smoked haddock; VisitScotland Smokie Trail | Alex Spink & Sons, Arbroath Fisheries, Arbroath Smokies Direct, B. Swankie Fishmongers, David Cargill Fishmongers, Derek Spink Fishmerchants, E & O Fish, M & M Smith, M & M Spink, Stuart's Fresh Fish, Iain R. Spink |
| England (Whitstable, Kent) | Whitstable oysters (UK protected food name application); designation | Seasalter Shellfish (Whitstable), The Whitstable Oyster Fishery Company, The Faversham Oyster Fishery Company |
| Norway (Lofoten) | Tørrfisk fra Lofoten stockfish, PGI (Norway 2007, EU 2014); designation | Tørrfisk fra Lofoten AS, Lofoten Fisk AS |
| Cantabrian coast anchovies (Santoña, Laredo, Castro Urdiales) | hand-filleted Cantabrian anchovies; TasteAtlas Europe anchovy ranking dominated by Santoña/Laredo makers | Conservas Catalina, Conservas El Capricho, Don Bocarte, Fredo La Estrella del Norte, Conservas Angelachu, Conservas M.A. Revilla, Conservas Emilia, Conservas Codesa, Anchoas La Capitana, Conservas Mª Asun Velar, La Castreña, Anchoas Hazas |
| Basque coast (Bermeo, Ondarroa) | bonito del norte and anchovy conservas | Conservas Serrats, Arroyabe, Conservas Zallo, Ortiz, Olasagasti |
| Japan (Fukuoka / Hakata mentaiko) | karashi mentaiko: 200+ makers in Fukuoka Prefecture (Fukuoka tourism) | Fukuya, Yamaya, Kanefuku, Fukusaya (mentaiko), Kabata, Fukutaro |
| Japan (Lake Hamana unagi) | Lake Hamanako Unagi, Japan GI No.177; designation | Lake Hamanako Aquaculture Fisheries Cooperative |
| Japan (Kagoshima katsuobushi: Makurazaki, Ibusuki) | Makurazaki and Ibusuki Katsuobushi, Japan GIs 168/169; designation | Yamakawa Marine Products Processing Industries Cooperative, Makurazaki Marine Products Processing Industries Cooperative |
| Japan (Shimonoseki fugu) | Shimonoseki Fuku, Japan GI No.19; designation | Shimonoseki Karato Fish Market Intermediate Wholesaler Cooperative |
| Japan (Echizen snow crab, Fukui) | Echizen Gani, Japan GI No.69; designation | Fukui Prefecture Fisheries Cooperative Association |
| Japan (Wakasa Obama) | Wakasa Obama Kodai Sasazuke, Japan GI No.45; designation | Cooperative of Obama Sasazuke Association |
| Japan (Miyagi Sanriku salmon) | Miyagi Salmon, Japan GI No.31; designation | Miyagi Salmon Promotion Association |
| South Korea (Yeonggwang, Beopseongpo) | Yeonggwang gulbi (dried yellow croaker), 2015 National Brand Award regional brand, KRW 350bn annual sales |  |
| South Korea (Ganggyeong, Nonsan) | jeotgal (salted fermented seafood): Korea's largest salted-seafood market | Hyeongje Sanghoe (Ganggyeong jeotgal), Sinjin Sanghoe (Ganggyeong jeotgal) |
| Malaysia (Melaka, Penang, Kedah, Sabah) | belacan (fermented shrimp paste); official cultural gateway: areas 'renowned for producing high-quality belacan' |  |
| Portugal (Lisbon conservas) | historic tinned-fish shops and purveyors | Conserveira de Lisboa, Loja das Conservas, A Vida Portuguesa, Dois Dedos de Conserva |
| United States (New York appetizing) | smoked fish appetizing shops; TasteAtlas US smoked fish #1/#2 | Russ & Daughters, Barney Greengrass |
| Sweden (Bohuslän herring coast) | Klädesholmen, 'the center for herring' | Klädesholmen Seafood |
| England (London fishmongers) | specialist fishmongers (SheerLuxe directory) | Life of Fish, Moxon's, Fin & Flounder, The Sea, The Sea, The Chelsea Fishmonger, La Petite Poissonnerie |
| Australia (NSW Sapphire Coast oysters) | Sydney rock oysters; 'the Sapphire Coast region has an exceptional reputation in the culinary world' (industry officer, Merimbula News Weekly) | Tathra Oysters, Australia's Oyster Coast, Hazelgrove Oysters, Wapengo Rocks Wild Organic Oysters |
| Italy (Sardinia, Cabras bottarga) | bottarga di muggine of the Cabras lagoon; Slow Food Presidio 2025 | Nuovo Consorzio Cooperative Pontis, L'Oro di Cabras (Fratelli Manca) |
| Thailand (Bang Bo, Samut Prakan) | salted dried gourami (pla salid), OTOP | Mae Amnuay Bang Bo Gourami |
| Hong Kong (Sheung Wan dried seafood street) | dried seafood trade (abalone, sea cucumber, fish maw, conpoy) | Shing Lung Hong Company |
| Ireland (Carlingford Lough) | oysters; Great Taste 3-star 2021 | Carlingford Oyster Company, Rooney Fish |
| Iran (Caspian caviar) | Caspian sturgeon caviar (Gilan, Mazandaran, Golestan) | Caspian Monarque, Dornika Caspian |
| Iceland (harðfiskur, Westfjords) | harðfiskur wind-dried fish; Visit Westfjords: 'part of Iceland's rich culinary heritage', racks across the Westfjords | Harðfiskverkun Finnboga, Von Iceland, Breki |
| Netherlands (Hollandse Nieuwe herring) | Hollandse Nieuwe herring; AD national herring test | Vishandel Gebroeders Simonis, Vishandel Arenthals |
| Japan (kamaboko: Odawara, Niigata, Nanao, Nagato) | fish-paste products; FY2018 top makers | Kibun Foods, Ichimasa Kamaboko, Sugiyo, Fujimitsu Corporation, Suzuhiro Kamaboko |

## Drops / moves

- Ati Manal: misspelling (Serious Eats' spelling) of register brand 'Ati Manel' (J2): merge into it, do not create a new row; tier listed (contender only)
- Matiz España: duplicate of harvest 'Matiz' (same Spanish brand): merge as alias
- Tetsujin: rename 'Tetsujin (katsuobushi)': register has 'Tetsujin Hamono' (knives, B5); not a drop, a qualifier
- Maine Coast Fishermen's Association: its Good Food Award product is a monkfish stew (packaged prepared food = J5), MOVE to J5 unless a J2 product is sourced
- Armatore: not a drop: tier 'listed' (seller praise) and its product colatura di alici is a fish-sauce-type condiment (J5 per owner's fish-sauce rule) - consider MOVE to J5

## Tier fixes

- ['Gonsalves', 'Bar Harbor', "Henry & Lisa's", 'Maria (Conservas)', 'Ati Manal']: Serious Eats contenders only (winner not visible in fetch): listed/cultural, not premium
- ['Lemberg Kaviar', 'Nacarii']: seller's (Bacalalo) self-declared non-neutral ranking: listed
- ['Armatore']: retailer praise only: listed
- all Good Food Awards rows: '2026' label wrong for most: the /winners/fish page aggregates 2017-2026. Only Copper River Fish Market, Cure Cooking, Fishpatricks, Lummi Island Wild Co-op, Oro Pacific Provisions and Tsar Nicoulai are 2026 winners. Approximate year map in AUDIT_J2_tmp/gfa_year_map.json (prefix-matched; 'Fish' rows of 2019/2024 belong to 'Fish (Sausalito)', 'Cure' 2023/2024 to the same Omaha maker). Tier stays quality (juried).
- Miss Can: country Portugal (Lisbon), not Spain
- Kaluga Queen (audit add): same company as register 'Hangzhou Qiandaohu Xunlong': merge as alias
- Ekone Seafood (TasteAtlas US #5): same as harvest 'Ekone Oyster Co' - not added separately
- Kalles: decided J2 (smoked cod roe spread = roe / fish spread); already covered by register row 'Abba' (desc 'Kalles Kaviar'): add 'Kalles' as alias/sub-brand of Abba, no new row
- ['Marumo (Makurazaki katsuobushi)', 'Sanford (New Zealand)']: homonym check: no 'Marumo' or 'Sanford' row exists in the register, so the qualifiers are harmless but not required; keep
- Patagonia Provisions: subsidiary of register 'Patagonia' (A1/A4): add rel link, keep its own row
- Fukusaya (mentaiko) (audit add): HOMONYM: register 'Fukusaya' is the Nagasaki castella house (J8), different company; qualifier kept

## Notes

Retry round focused on additions from fetched raw pages (Parallel web_fetch full_content, saved to AUDIT_J2_tmp/pages and parsed with python). Sources added: VisitScotland Arbroath Smokie Trail (10 producers), UK PFN Whitstable oysters application, Visit Lofoten + FHF (Tørrfisk fra Lofoten AS), TasteAtlas US smoked fish / Europe smoked salmon / Europe anchovies / Spain canned fish / Northern Europe preserved fish, olive magazine smoked salmon and anchovy taste tests, Falstaff smoked fish, Great Taste 3-star 2021 + Golden Fork nominees 2025/2026, Good Food Award year pages 2017-2026, Fukuoka tourism mentaiko makers, MAFF Japan GI register (fish GIs and registered groups), SeafoodSource kamaboko market ranking, Wikipedia (Kaluga Queen, Russian Caviar House, Conservas Ramirez, Cofaco, MIFCO, Fujimitsu, Maruha Nichiro, Stabburet), SNL, VLE (Vičiūnai), Lojas com História (Conserveira de Lisboa), Prior 'Tin Town', SheerLuxe London fishmongers, Sydney Royal oyster results, Michelin Thailand (Bang Bo gourami), HKTB QTS (Shing Lung Hong), Slow Food Presidio Cabras bottarga, AD Haringtest, Iceland Monitor/Grapevine harðfiskur. Region designations (DESIGNATION AS RENOWN): Arbroath Smokies PGI, Whitstable oysters PFN, Tørrfisk fra Lofoten PGI, London cure smoked salmon PGI and Grimsby traditional smoked fish PGI (named on pages), Japan GIs: Lake Hamanako Unagi, Makurazaki/Ibusuki Katsuobushi, Shimonoseki Fuku, Echizen Gani, Wakasa Obama Kodai Sasazuke, Miyagi Salmon, Iwate Nodamura Araumi Hotate, Hamanaka Youshoku Uni, Awajishima 3nen Torafugu, Toyoshima Tachiuo, Jusanko Yamato Shijimi (further fish GIs on the MAFF list without fetched group pages: Lake Ogawara and Lake Shinji clams, Abashiri clams, Hirotawan Ishikagegai, Tanoura Gindachi, Ono Asari). Owner decision applied: Kalles = J2 (via register row Abba). Sea vegetables (Good Food Award kelp/seaweed winners: Atlantic Sea Farms, Barnacle Foods, Daybreak Seaweed, Kelpful, Maine Coast Sea Vegetables, Smithereen Farm, Soba Mill furikake) deliberately NOT added. Blind spots after this round: West African smoked/dried fish (only FAO/NGO pages, no named makers or sellers: artisanal women processors, REGIONS ARE NOT QUOTAS); Peru/Chile (industry is fishmeal and commodity canning; Florida/Compass brands only in food-safety news, Camanchaca/Austral trade press only - not added); Russia (Russian Caviar House only); Poland (Koral, Suempol located only in directories, not added); Korea (Yeonggwang gulbi and Ganggyeong jeotgal regions confirmed, but only two 1996 market merchants named; no maker page fetched); Philippines (Barrio Fiesta only; Cebu Taboan danggit sellers located in travel pages not fetched); Indonesia terasi, Vietnam, India (Bombay duck), China mainland (Zhoushan, Dalian sea cucumber), Turkey (lakerda), Greece, Mexico (Dolores is a redlink in Wikipedia's Mexilink article), Morocco (one directory row), Chile; Great Taste full winners table (official site not fetched; only 2021 3-star and Golden Fork nominee lists); Serious Eats winner not visible in raw fetch (truncated to 9 contenders); Gambero Rosso bottarga ranking blocked (403). Fetch caveat: Parallel raw full_content for Serious Eats, Food & Wine and Wirecutter returns only a few lines; those names were confirmed with excerpt-mode fetches. Firecrawl credits exhausted during this run.