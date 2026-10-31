# VERIFY H4 Fragrance (Opus verifier)

Inputs: H4.json (924) + H4_countries.json (187) harvest rows, AUDIT_H4.json (90 drops, 64 relabels, 15 homonyms, 29 add_brands, 5 add_regions). Worked by script (VERIFY_H4_tmp/build.py) from the audit's saved raw pages (dir_*.md, dir_UAE.json, ao.md, ao_check.json, fifi/, add/, des/) plus pages re-fetched raw here (VERIFY_H4_tmp/pages/).

## Result

- Rows: 1055 (harvest 1016 after 90 drops and 5 merges; 29 audit adds; 7 register brands given rows from audit relabel evidence; 3 Brazil region brands).
- By tier: listed 789, cultural 46, quality 220; not shown: 0.
- Scenes (owner divisions): Middle Eastern perfumery 728, South Asian attar houses 72. Every Fragrantica country-directory row keeps its scene (Gulf, Iraq, Jordan, Lebanon, Iran, Egypt, Turkey -> Middle Eastern perfumery; India, Pakistan -> South Asian attar houses); other rows whose name is in a country section also get the scene.
- Homonyms: 19 (audit 15 + 4 found here: Bohémia, S''Ram, PourMoi, B.ATES). Same-company rows (Raymond, Junaid Jamshed, Huda Beauty, Mauzan, Vakko, Mavi, Koton, LC Waikiki, DeFacto, Flormar, Atelier Rebul, Valentino Beauty, Prada Beauty, Rare Beauty) unflagged, noted "cross-tag H4". QIUHAO (A&O) left unflagged: creative direction by Qiu Hao, likely the A1 designer.

## Decisions

- Fragrantica directory rows: listed (existence) with scene. UAE rows checked against the 417-name UAE section (counts from the list, fixing the 11 sidebar counts); 43 sidebar rows dropped; Amouage moved to the Oman page (156 perfumes); Nishane stays via the Turkey page. Hope Istanbul by Serimu Kozmetik matches (page uses a Cyrillic k).
- Art and Olfaction (Wikipedia, blind-judged): quality; each note gives category, winner/finalist/honourable mention and years from ao_check; 27 rows are honourable mention only and say so. 39 Sadakichi art entrants dropped. Samar = 2024 Artisan winner; Aether Arts 2014 winner. Oneiros (2026 Sadakichi winner, perfume by IFF perfumer) kept as quality with a caveat.
- FiFi (TFF Awards, US): tiered cultural, not quality. The TFF FAQ (search excerpt, fragrance.org/faqs) says categories are voted by members, an expert panel for some categories, or consumers; no page states which categories are expert-judged, so TRADE VOTES applies. YSL, Guerlain, Tom Ford, Jo Malone: country/scene cleared. Robertet, Mane, Symrise, Scents of Wood, A Lab On Fire, Perfume Calligraphy, Odin New York, Veronique Gabai and FiFi notes for Amouage, Arquiste, BDK, Zoologist, Bond No. 9, Byredo, Kilian Paris: cultural.
- Juried quality: Marie Claire Türkiye 2026 (jury, blind smelling; re-fetched raw): OJUVI, Soul of Caria, Positive Zero, Atelier Rebul, Puzzle Parfum, Parfümane, Imprime, Mad Parfumeur. Fragrance Foundation France 2025 niche prize (jury, raw): Une Nuit Nomade, Chambre52. Asia Perfume Awards 2025 (expert judges, raw): Wren Atelier, Liberta, d'Annam. Enio Bonchev (gold medal for rose-oil quality, festival history page).
- Excerpt-mode audit pages re-fetched raw and names confirmed: LSM (Dzintars), mos.ru and Krasnaya Moskva (Novaya Zarya), BeautyMatter (White Label Fragrances, Saint d'Ici), Scented Salamander (Bint el Sudan), Premium Beauty News (Scent of Africa), Asia Perfume Foundation, Business Times (Maison de L'Asie), WhatScent Latin (Phebo, Yanbal, Natura, O Boticário, Granado), Fragrantica atomiser history (Marcel Franck). All shown.
- Albert Vieille: Givaudan's own acquisition release -> cultural at most (cultural). Phebo, Yanbal and the WhatScent Middle Eastern list: listed (weak app magazine with buy-links). Ajmal (CEO interview in a business supplement) and Shaikh Mohd Saeed / Al Hunaidi (unbylined advertorial): listed. Swiss Arabian: cultural (bylined Khaleej Times 2014, "the UAE's pioneer group in the perfume industry"). Arabian Oud, Abdul Samad Al Qurashi, Almajed Oud, Deraah: cultural (AlJazira Capital research).
- M.L. Ramnarain: own site only and its raw text does not even show the name; src2 Fortune India (bylined 2024, re-fetched raw: "200-year-old perfume distillery") -> cultural, Kannauj region, South Asian scene. Gulab Singh Johrimal: src2 AFP/Taipei Times -> cultural, South Asian scene, not in the Kannauj region (Old Delhi house).
- Atelier Rebul / Eyüp Sabri Tuncer: BBC and Business Insider give no raw text on re-fetch (excerpt only), so they are kept only as src2; Rebul rests on Marie Claire (quality), Tuncer on the Turkey directory (listed).

## Regions

- Grasse, France: renown True ("so many iconic fragrances were born in the international perfume capital (France.fr)"); brands ['Fragonard', 'Molinard', 'Galimard']. designation: UNESCO Representative List 2018 (skills related to perfume in Pays de Grasse); UNESCO page names no houses, brands from src2 (France.fr). Robertet, Mane, Albert Vieille not named on either page: not in the region
- Kannauj, India (attar): renown True ("Kannauj is to India what Grasse is to France. Here perfume-making is art. (AFP)"); brands ['Pragati Aroma Oil Distillers', 'M.L. Ramnarain Perfumers']. designation: Kannauj Perfume GI (Wikipedia page); GI page names no houses; brands from AFP/Taipei Times. M.L. Ramnarain is placed via Fortune India (src3, bylined, "ancient town known for its perfumery"). Gulab Singh Johrimal is named on the same AFP page but is an Old Delhi house: South Asian attar scene, not the Kannauj region
- Turkey (kolonya): renown False; brands none. BBC and Business Insider return no raw text (full_content empty on re-fetch); excerpts name Eyüp Sabri Tuncer and Atelier Rebul but state no regional renown. Both houses keep the Middle Eastern perfumery scene via the Fragrantica Turkey directory; Atelier Rebul has quality via Marie Claire Türkiye 2026
- Gulf / Arabian Peninsula (oud, attar, incense perfumery): renown False; brands ['Amouage', 'Ajmal', 'Al Haramain', 'Swiss Arabian', 'Rasasi', 'Arabian Oud', 'Lattafa', 'Armaf', 'Afnan']. WhatScent app magazine (weak, buy-links); its raw text names all nine houses but states no regional renown (only "heritage houses built on oud rose saffron and amber"). The Middle Eastern perfumery scene carries these houses
- Italy (Florence herbal perfumery, Parma cologne): renown False; brands ['Santa Maria Novella']. rests only on Santa Maria Novella's own site: own-site renown not allowed; no independent page found by the audit
- Bulgarian Rose Valley (Kazanlak/Karlovo) rose oil: renown True; brands ['Enio Bonchev']. designation: EU PGI Bulgarsko rozovo maslo (gov.uk register page); producers from src2 (Kazanlak rose festival history)
- Taif, Saudi Arabia (Taif rose oil): renown True ("Taif roses, renowned for their exceptional aroma ... among the Kingdom's most valuable natural perfume products"); brands ['Al-Kamal (Taif rose factory)']. SPA (state news agency, independent of makers); Al-Kamal named on src2 (Arab News)
- Bohemia, Czech Republic (crystal perfume bottles): renown True ("Bohemian Crystal and Czech art glass have long been revered internationally for their workmanship and beauty."); brands none. museum collection page (Czech Center Museum Houston); names no makers; a dealer page naming Hoffmann/Schlevogt is a seller page, not used
- Brazil (perfume and cologne houses): renown True ("Brazil has the strongest home-grown perfume industry in the region."); brands ['Natura', 'O Boticário', 'Granado', 'Phebo']. WhatScent app magazine: weak source, but the quote states the regional strength; Granado is register H1 only - this page shows colognes/EDPs (cross-tag H4)

Removed: Japan (Kyoto/Awaji incense) region and its 8 houses (incense is B4/F4).

## Index cleanup (for review)

- Shoyeido and Nippon Kodo carry an H4 code in the register (with B4/F4); incense houses: review whether H4 should be removed.

## Not done / notes

- Directory rows missing from the harvest (India 1, Saudi 2 names in the section but not in the harvest) were not added.
- Kannauj houses Raahi Perfumes and PKAPO are named on the Fortune India page but were not added (outside the audit list).
- FiFi tier is cultural by the TRADE VOTES rule; if the coordinator rules TFF categories (e.g. Indie, Perfume Extraordinaire) expert-judged, those rows rise to quality.
