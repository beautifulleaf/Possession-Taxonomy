# VERIFY E2 Sports, Fitness & Recreation

Raw fetch (mcp__Parallel__web_fetch, full_content) of every distinct harvest and audit source URL (36 harvest, 47 audit) plus src2 / cross-tag pages: 100 pages in VERIFY_E2_tmp/pages/ (index.json maps URL to file), parsed with VERIFY_E2_tmp/build.py. No URL was guessed: ISPO paginated pages (?start=20/40/60) come from page links in the audit's raw fetch, other src2 pages from search results.

Brands checked: 310 (harvest 262 minus 10 drops, 17 moves and 2 rows collapsed in the SS/SG triplicates, plus 82 audit adds minus 5 turned into cross_tag). Not shown: 0. By tier: {"cultural": 218, "quality": 50, "listed": 42}. Homonyms flagged: 10. Regions: 29 (7 with renown). Moves: 17 rows in MOVES_E2.json. Cross-tags: 9.

## How each audit "drop" item was handled

- Drops (no row): Resurfice Corporation (ice resurfacers, rink plant (audit)); Zamboni Company (ice resurfacing machines (rink plant), not personal sports equipment (audit)); Buggies Unlimited (golf-cart parts retailer, no E2 kind (audit)); Fanttik (tyre inflators/gadgets, not a tent maker (audit)); Arthur Beale (London yacht chandlery shop, not a maker (audit)); Avon Technologies (military/CBRN respirators, not sport diving gear (audit); register has Avon Protection (C1)); Divex (commercial/military diving systems (audit)); Drass-Galeazzi (hyperbaric chambers, commercial diving systems (audit)); Interspiro (firefighting/military breathing apparatus (audit)); Nuytco Research (industrial submersibles / atmospheric diving suits (audit)).
- Moves (real brands of another category, each shown on its fetched src or src2; rows in MOVES_E2.json): A1: Antigua Apparel, SBENU, Luanvi, Grand Sport Group, Real United, Warrix Sports, Keuka, Pelliot, Zhongqiao, Impetus, Outopia, Gore Wear; E4: Morini; A4: Boblbee; G1: Sugino, Smittybilt; A2: EDV. SBENU goes to A1 as the coordinator ruled (audit said A2). Zhongqiao and Gore Wear are ISPO apparel winners not named in the audit drop list but covered by the ISPO apparel rule. Tokio Sports (ISPO 2024 women's football boot) stays in E2: football boots are an E2 kind (Boots, goals & fixtures). Antigua Apparel moves to A1 (audit: golf apparel).
- Merges (row renamed to the register name with aliases, so merge.py adds evidence to the existing brand): Callaway Golf Company -> Callaway Golf Company; Ping -> Ping (Karsten Manufacturing); CCM -> CCM Hockey; Penn Reels -> Penn Fishing; Penn Racquet Sports -> Penn; Scott Sports -> Scott; Shakespeare Fishing Tackle -> Shakespeare; Shearwater Research -> Shearwater; Mikasa Sports -> Mikasa; Sherwood Hockey -> Sherwood Hockey; Prince Sports -> Prince; Mountain Safety Research -> MSR; Wilson Staff -> Wilson Sporting Goods; New Balance Cricket -> New Balance; Adidas Terrex -> Adidas; Nikolay (Grishko) -> Grishko; SS (Sareen Sports) + Sareen Sports Industries -> SS; SG (Sanspareils Greenlands) + Sanspareils Greenlands -> SG. SS and SG triplicates collapsed: each keeps the Wikipedia category row (cultural) with the harvest and directory names as aliases. Scott: merge adds E2 to the register Scott (A2/G1) row. Adidas Terrex: not on the paginated src page now, shown on ispo.com/news/promotion; its awards are for jackets, so the row only carries the alias.
- Rename: Payne Rod Company -> James Arthur Payne (aliases Payne Rod Company, E.F. Payne Rod Company): the category lists the person; his fetched article says he owned the E.F. Payne Rod Company.
- Src fix: Simond src2 = https://www.ispo.com/award-winner?start=60 (MT900 backpack and Single Wall Trekking Tent shown). The other 2025 ISPO winners also moved off page 1: Acemate, Robens, Vitbio, Zhongqiao on ?start=20; EGGspander, Impetus, Outopia on ?start=40; EDV on ?start=60. 2024 winners no longer on promotion?start=80: Tokio Sports, Raide, Ruroc have src2 on their own ISPO award articles. Ocun src2 = OutdoorGearLab Bullit review (no longer on the best-shoes page). Kosa src2 = Category:Sporting goods manufacturers of Sweden ("Kosa (sports manufacturer)"; not on the ice-hockey category).
- Retiers: Irish Guild of Hurley Makers members (32) premium -> cultural; cricketbats.com rows (Spartan, DSC, Woodworm) and tenkarabum rows (Tenryu, Suntech, Nissin) -> listed.
- Homonyms kept apart (homonym: true, qualifier in the name): Victor Barton, Cosco (India), CORE (tents), Gazelle (tents), Viking (dry suits), Faber (diving), Nissin (tenkara), Mitsuboshi (kendo bogu), Burley (Burley-Sekem), Faber (snowshoes). Victor Barton: fetched article is a Hampshire cricketer who ran a Southampton sports outfitters and "was also briefly involved in the manufacture of cricket bats": kept as a cultural category member, weak as a brand. Mitsuboshi (kendo bogu) is not the B5 cutlery Mitsuboshi. Nissin (tenkara) is not the D4 flash maker; Burley (Burley-Sekem) is not the G1 bike-trailer Burley; Gazelle (tents) is not the G1 Gazelle bikes. Same-company names left unflagged so the merge adds E2: Hobie (register A1), Ferrino, De Marchi, Santini, Sting Sports (register A1).
- Register errors: listed under "Index cleanup" below, not added as rows.

## Tier rulings

- Wikipedia category members are own articles: cultural (all category rows checked against the raw page text).
- quality only where an independent fetched page states craft, an award, a federation standard or a test: ISPO winners (juried award), OutdoorGearLab awards (hands-on test), GearJunkie report of ISPO 2022 winners, IWF-certified bar makers (Uesaka, Werksan, Zhangkong), FIPJP competition-approved boule labels (federation standard), GR8 Sports (ICC approval), Sting Sports (official AIBA glove), Anwar Khawaja (Olympic balls), Kays Curling (BBC: hand-crafted, only stones used by the World Curling Federation), De Marchi (Wikipedia: "superior quality of the wool"), Miura, Kubota Slugger, Megabass (Red Dot / iF awards), R-Class and Suffolk (handcrafted pointe shoes), Field Mag best-brand picks (Gentemstick, Korua) and WEST, Top King (glove test), Auchterlonie (R&A: "first and foremost a clubmaker"), Lewis Mitchell (hand-carved hickory sticks), Suzuki Kendogu (hand-stitched Takeya-ryu) and Umezawa Kendogu (Contemporary Master Craftsman, Yellow Ribbon Medal).
- SELLER PRAISE -> listed: Eiko Budogu, Matsukan Kogyo, Mitsuboshi (kendo shops that stock them), the six tt-spin.com table-tennis brands (shop-affiliated), tenkarabum names. Suzuki and Umezawa rest on the honours and craft facts of a kendo retailer's guide to other shops (not brands it is shown to stock); flag if the coordinator prefers listed.
- Maker's own page = existence only: Sanpuku Shoji (listed). Directory or brand-list mentions with no quality statement: listed (BDM, FC Sondhi, Roundpoint, Traditional Lacrosse, Hatakeyama, Zett, SSK, Neve Gear, Kiwi Ultralight, Chacott, Grishko/Nikolay, Moss, Bataleon, Lobster, Äsmo, Hirano, Tokyo Seibudo, Iizuka, Kenbudo, Windy, Thaismai, Raja, Boon Sport, Sandee, Ona Pilota).
- Heritage: Chistera Gonzalez (French ICH inventory) cultural; Benedict Lacrosse Factory (Smithsonian collection) and Faber (snowshoes) (Wooden Canoe Museum record) cultural; Shibata Kanjuro cultural (official bowmaker to the Emperor, stated on an association page of his own school, so not independent enough for quality); Alfie Jacques cultural (USA Lacrosse museum, Hall of Famer).
- Black Crows: "high end" is price wording, cultural on its article only.

## Cross-tag (register brands that gain E2; E2 product confirmed on a fetched page)

- Kelme: Wikipedia: produces sportswear and athletic shoes for football and futsal (football/futsal boots = E2 Boots, goals & fixtures). Register Kelme (A1/A2) is the same company. (https://en.wikipedia.org/wiki/Kelme_(company))
- Penalty: Wikipedia: makes kit and balls; "In the 1980s, Penalty became the largest Brazilian manufacturer of soccer balls". Register Penalty (A1/A2) same company. (https://en.wikipedia.org/wiki/Penalty_(sports_manufacturer))
- Uhlsport: Wikipedia infobox products: Goalkeeper gloves, Balls. Register Uhlsport (A1) same company. (https://en.wikipedia.org/wiki/Uhlsport)
- Mitre: Wikipedia infobox products: Football balls. Register Mitre (A1/A2) same company. (https://en.wikipedia.org/wiki/Mitre_Sports_International)
- Zoggs: Wikipedia: "a brand of swimming goggles, training aids, swimwear". Register Zoggs (A1) same company. (https://en.wikipedia.org/wiki/Zoggs)
- Asics: Wikipedia infobox: Industry "Sports equipment"; Products "Footwear, apparel, sports equipment". Register Asics (A1/A2) same company. (https://en.wikipedia.org/wiki/Asics)
- Umbro: Wikipedia infobox products: Footballs. Register Umbro (A1/A4/A2) same company. (https://en.wikipedia.org/wiki/Umbro)
- Diadora: Wikipedia: "Diadora produces football boots". Register Diadora (A1/A2) same company. (https://en.wikipedia.org/wiki/Diadora)
- Joma: PadelVerdict (independent racket reviews) tests the Joma Slam Pro Iconic 2026 padel racket (E2 racket sports). The Joma Wikipedia article lists only sportswear and footwear, so a second page was used. Register Joma (A1/A2) same company. (https://padelverdict.com/rackets/joma-slam-pro-iconic-white-gold-2026)

## Regions

| region | renown | quote | brands kept | not on page |
|---|---|---|---|---|
| Scotland | no | - | Forgan of St Andrews, Hugh Philp, Ben Sayers | - |
| Nordic countries / Norway | no | - | Madshus, Rottefella, Swix, Rønning Treski, Karhu, Peltonen | - |
| Austria / Alps | no | - | Atomic, Fischer, Kneissl, Völkl, Head, Elan | - |
| South Asia (India) | no | - | SG, SS, MRF | - |
| England / Australia | no | - | Gray-Nicolls, Gunn & Moore, Kookaburra, Stuart Surridge, Duncan Fearnley | - |
| Canada / Quebec | no | - | Bauer, CCM Hockey, Cooper Canada, Sherwood Hockey, Victoriaville, Warrior | - |
| Japan | no | - | Mizuno, Molten Corporation, Mikasa, Shimano, Snow Peak, Butterfly, Yonex, Descente, Shoei, Gosen, Globeride | - |
| Ireland | no | - | Camán, Martin Hurls, Denis Ahern Hurleys, Fitzgerald Hurleys, Liam Walsh Hurleys, O'Connor Hurleys, 65 Hurls, Farrell Hurls, H Sports, O'Dea Hurls, Tom Murphy Hurleys, Aylward Hurleys, O'Neills, Mycro Sportsgear | - |
| Sialkot, Pakistan | yes | Sialkot city, known as the world's football manufacturing capital | Forward Sports, CA Sports | Anwar Khawaja Industries |
| Thailand (Bangkok and surroundings) | yes | the best Muay Thai brands come from Thailand where the sport originates and continues to thrive | Fairtex, Twins Special, Yokkao, Top King, Windy, Thaismai, Raja Boxing, Boon Sport, Sandee | - |
| Finland | no | - | Suunto, Karhu, Koho, Titan | - |
| India | no | - | Cosco (India), Nivia Sports, SS, TYKA Sports | - |
| Mexico (Latin America) | no | - | Atletica, Charly, Voit | - |
| New Zealand / Oceania | no | - | Canterbury of New Zealand, Macpac, Bliss-stick | - |
| Switzerland | no | - | Katadyn, YES. Snowboards | - |
| Scotland (curling) | yes | all the stones used by the competitors originate from an uninhabited Scottish island | Kays Curling | - |
| Japan (kyudo) | no | - | Shibata Kanjuro | - |
| Hawaii/California/Australia (surfing) | no | - | Hobie, Haydenshapes, Bob McTavish | - |
| Italy (diving, climbing) | no | - | Cressi, Mares, Technisub, CAMP, La Sportiva, Scarpa | - |
| France (alpine, diving) | no | - | Petzl, Millet, Beuchat, Aqua Lung | - |
| Haudenosaunee nations (Akwesasne Mohawk, Onondaga) | no | - | Roundpoint Lacrosse Stick Factory, Alfie Jacques | Traditional Lacrosse, Lewis Mitchell (Mohawk stickmaker), Benedict Lacrosse Factory |
| Japan (tenkara) | no | - | Tenryu (tenkara rods), Suntech, Nissin (tenkara) | - |
| Saitama Prefecture, Japan | yes | headquarters of major nationally known kendo equipment manufacturers ... are concentrated here ... home to the Takeya-ryu kendo equipment craftsmen's shops | Suzuki Kendogu (Takeya-ryu), Umezawa Kendogu, Eiko Budogu, Matsukan Kogyo | - |
| Meerut and Jalandhar, India | yes | Jalandhar and Meerut ... are the nerve centres of India's cricket equipment industry | SG, SS, BDM (BD Mahajan & Sons), FC Sondhi & Co | - |
| Kashmir valley (Sangam/Bijbehara, Anantnag), India | yes | Known for their durability and affordability, Kashmir's bats give English willows ... a run for their money | GR8 Sports | - |
| St Andrews, Scotland | yes | St Andrews was always well known as a golf-ball manufacturing centre | Hugh Philp | Forgan of St Andrews, Auchterlonie (D. & W. Auchterlonie, St Andrews) |
| Basque Country (Iparralde and Hegoalde) | no | - | Chistera Gonzalez | Ona Pilota |
| Himeji / Ichikawa, Hyogo, Japan | no | - | Miura Golf | - |
| Saint-Bonnet-le-Château and Saint-Étienne (Loire), France | no | - | Obut, JB (Boule J.B.), La Boule Noire, Boule l'Artisanale, La Boule Bleue | - |

Region notes: duplicate harvest/audit entries merged (Japan x2, Ireland x2, Sialkot, Thailand, Haudenosaunee). Renown is never taken from a maker's own site. Without renown: all Wikipedia category regions; Haudenosaunee (only company shares and the origin of the game are stated); Basque Country (ICH sheet makes no renown statement); Himeji (renowned for swords, not golf irons); Loire boules (FIPJP list only); Japan (kyudo) and Japan (tenkara) (one-maker / seller pages). Brands not on the region page were left out of the region (e.g. Anwar Khawaja is on Dawn, not the ADB page; Forgan and Auchterlonie are not on the St Andrews history page; Lewis Mitchell, Traditional Lacrosse and Benedict are on other pages).

## Index cleanup (register errors; not added here)

- Fischer (register dept "wood screw", C8/E6/E2): the fischer fixings company carries E2; E2 needs Fischer Sports (skis) as its own row.
- Bell (dept "helicopters", G1/E2): Bell helicopters carries E2; split from Bell Sports (helmets).
- Fox (dept "confectionery", J8/I3/E2): Fox's sweets carries E2; remove E2 (Fox Racing is its own row).
- Stiga (dept "powered garden equipment", C2/E2): Stiga garden machinery vs Stiga Sports (table tennis): split.
- Castellani (dept "archaeological revival", A3/E2): jewellery house tagged E2: remove E2.
- eB (dept "transit card", F5/E2): not sports equipment: remove E2.
- Kirkland Signature (B6/J9/J1/E2): private label with no E2 footprint: remove E2.
- Select (dept "Australian team sets", F3/E2): mixed row of Select trading cards and Select Sport (Danish footballs): split.
- Mongoose (bmx bikes) and Lynx (snowmobiles) carry E2: they are G1.
- Adidas (dept "sports watches") and Nike (dept "digital watches") E2 rows: dept text describes A5 lines; E2 rows should say football boots, balls, track spikes.

## Not done / caveats

- Kosa, Payne, Haydenshapes, Hobie, Victor Barton and Charles Ritz are category members that are people or minor makers; kept as cultural per the encyclopedia rule.
- ISPO list pages ?start=10/30/50 were not fetched (not linked from fetched pages); every ISPO name was found on a fetched page anyway.
- Jackson Kayak was never in the harvest (audit note only).
