# VERIFY D2 Phones, Tablets & Personal Devices

Raw fetch (mcp__Parallel__web_fetch, full_content) of all 17 harvest and 28 audit source URLs plus 4 region pages and 10 src2/cross-tag pages. Pages in VERIFY_D2_tmp/pages/ (index.json maps URL to file; the Wikipedia list and category pages are kept as condensed extracts of the rows checked). Blocked or partial: nytimes.com Wirecutter (excerpt only, so Mujjo and Smartish needed src2), eham.net product 14741 (403), pcmag.com (verdict excerpt only).

Brands checked: 179 (harvest 167 minus 7 drops/merges and 27 moved rows, plus 45 audit adds, plus Lava International given its own row). Not shown: 0. By tier: {"cultural": 135, "quality": 32, "listed": 12}. Homonyms: 2. Regions: 17 (0 with renown). Moves: 28 names (29 rows) in MOVES_D2.json.

## Coordinator rulings applied
- (1) Tier rule: every Wikipedia list or category row linking to the brand's own article is cultural (all 94 list rows checked against the raw link targets). Exceptions: Avio links to the Italian aerospace company Avio, so it is listed; Nextbit links to Nextbit_Robin, the article on its one phone (cultural); VinSmart links to its own vi-Wikipedia article (cultural). The 13 obscure budget names (Gfive, Vsun, Wasam, Technology Happy Life, InfoSonics, iDroid USA, Jeotex, Verzo, Vitelcom, New Generation Mobile, Onda Mobile Communication, DBTel, X-tigi) are all blue links to their own en-articles, so they are kept as cultural. The audit's drop of them is reversed.
- (2) Moves to MOVES_D2.json as {"to":{CODE:[rows]}} with the same row fields. D3 gets 26 rows: the broadcast radio/TV makers, Blaupunkt (home radios), Metz (note: flashes belong to D4), Stromberg-Carlson (radios), and GoldStar with merge_into LG. G1 gets Blaupunkt (car radios). D1 gets Packard Bell. A5 gets Oregon Scientific. All of them are members of Category:Radio_manufacturers, checked on the raw page (cultural). Stromberg-Carlson stays in D2 for telephones. Renamed to the page form: Panda Electronics, and Thorn Electrical Industries, flagged as a homonym guard against the register's Thorn Lighting (alias Thorn).
- (3) Drops: Zetron, Telit, Medion, Kogan. Merges: JVCKenwood into the register's Kenwood Corporation; harvest Boox and Onyx Boox into the register's Onyx (aliases Boox, Onyx Boox; ZDNet expert-tested pick, so quality); Cybook into the register's Bookeen.
- (4) GRE: the fetched en-Wikipedia GRE (company) page says "General Research of Electronics, Inc. was a Japan-based multinational manufacturer" (Tokyo, 1961; scanners, transceivers). The country is corrected from Italy to Japan and the row renamed GRE (General Research of Electronics).
- (5) The 45 audit additions were re-tiered by rule. Own website only gives listed: Codan, GME, Sepura (and harvest Mudita, Punkt.). Not independent gives listed: Findmykids, which sells its own Pingo watch (Xplora, imoo, Gabb), and the Vodafone Turkey operator-retail blog (General Mobile, Casper, Reeder). Lab tests and independent reviews give quality: the Sherwood tables (Hilberling, Apache Labs, Expert Electronics, Ten-Tec, Lowe Electronics, Racal, Watkins-Johnson), ARRL guide (Begali, Schuenemann, N3ZN, K8RA), eHam owner reviews (Optibeam), OutdoorGearLab, Wareable, CHIP Testcenter (Tolino), Good e-Reader (Bigme, iReader, Hyread), Wearify (iFLYTEK), CES Innovation Awards (OtterBox, Littlebird), GLOMO (Well Being Digital), AppleInsider (Mujjo) and Wirecutter (Smartish). Some names are not on the src page in full form, so src2 was used: Apache Labs (eHam ANAN-100 page), Expert Electronics (DXZone), Lowe Electronics (Medium Wave Circle HF-225 review), Watkins-Johnson (the src page says only "WJ"; Medium Wave Circle HF-1000 review), Mujjo (AppleInsider), Smartish (Wirecutter Gripmunk page). Wenquxing appears only as 文曲星 (alias). Besta and Wenquxing rows in the ja-Wikipedia maker table link to their own zh-Wikipedia articles (cultural).

## Homonyms
- Casper (phones): Turkish phone brand, HOMONYM of the register's Casper (B1 foam mattresses).
- Lava International (phones): the harvest region brand "Lava", given its own row (list row links to Lava_International). HOMONYM of the register's Lava (H1).
- Not homonyms: Bush (no plain Bush in the register; moved to D3), Panda (moved as Panda Electronics; register Panda Pops/Security/Supplements are other names), Polar (register Polar is the same company, Polar Electro; region member only), Light Phone (no "Light" brand in the register), Tolino (not in the register).

## cross_tag
- Starlink (+D2): PCMag review of the Starlink Mini, a portable satellite-internet dish ("A Fantastic Way to Access Starlink on the Go", travel-friendly), i.e. D2 Satellite hotspot.
- Vestel (+D2): the fetched Vodafone Turkey page lists "Vestel Telefonlar" among domestic phone brands.

## Kinds note
- D2.kinds.txt lists "Car sat-nav" under Navigation > Navigators, but mounted car sat-navs belong to G1 (framework). The kinds file should drop it, keeping Handheld GPS only.

## Regions
| Region | Renown | Note | Brands kept | Removed (not on page) |
|---|---|---|---|---|
| China (Shenzhen/Dongguan/Beijing) | no | list/category page: no renown statement | Huawei, Xiaomi, Oppo, Vivo, Honor, OnePlus, Realme, Itel, Infinix, Tecno, Ulefone, Oukitel, Cubot, Umidigi, Unihertz |  |
| Finland / Nordics | no | list/category page: no renown statement | Nokia, HMD Global, Jolla, Bittium, Doro, Ericsson |  |
| Japan | no | Amateur radio companies category names Icom Incorporated, Yaesu (brand), Kenwood Corporation, AOR (company), Alinco; Sony/Sharp/Kyocera/Fujitsu/Panasonic are not in it | Icom, Yaesu, Kenwood Corporation, AOR, Alinco | Sony, Sharp, Kyocera, Fujitsu, Panasonic, JVCKenwood (dropped: merged) |
| France / Western Europe | no | list/category page: no renown statement | Alcatel, Wiko, MobiWire, Archos, Gigaset, Fairphone, SHIFT | Medion (dropped: store label) |
| Russia / Eastern Europe | no | list/category page: no renown statement | Yotaphone, teXet, Allview, Evolveo |  |
| South Asia | no | two harvest South Asia entries merged; all 8 names are on the list page (Lava_International page names only Lava, Micromax, Karbonn, Xolo) | Lava International (phones), Xolo, Karbonn, Micromax, Intex Technologies, Symphony, Walton, QMobile |  |
| Southeast Asia | no | list/category page: no renown statement | Cherry Mobile, Starmobile, MyPhone, I-Mobile, VinSmart, Nexian |  |
| Africa | no | list/category page: no renown statement | Condor Electronics, SICO Technology, Mobicel, EvertekTunisie, GTel, Tecno, Infinix, Itel |  |
| Latin America | no | list/category page: no renown statement | Positivo, Multilaser, Gradiente, Lanix, Zonda, Kyoto Electronics |  |
| United States | no | list/category page: no renown statement | Elecraft, Heathkit, MFJ Enterprises, Hallicrafters, Hammarlund, Vibroplex | Purism, Caterpillar |
| Sub-Saharan Africa | no | page says Transsion "was the largest smartphone manufacturer by sales in Africa": a company statement, not regional renown | Tecno, Itel, Infinix, Transsion | Mara Phones |
| Northern Europe (Finland) | no | Polar is the register brand Polar (A5/J8/J9/D2), same company: unflagged | Suunto, Polar | Nokia |
| Oceania (Australia / New Zealand) | no | GME own site: own-site renown never counts | GME | Codan, Tait Communications, Uniden |
| Japan and Greater China | no | page names カシオ/Casio, シャープ/Sharp, キヤノン (Canon), セイコー(インスツル) (Seiko), 快譯通 (Instant-Dict), Besta, 文曲星 (Wenquxing); a maker table, no renown statement | Casio, Sharp, Canon, Seiko, Instant-Dict, Besta, Wenquxing |  |
| Turkey | no | operator-retailer blog: lists "tamamen yerli" (fully domestic) brands; no renown | Vestel, General Mobile, Casper (phones), Reeder |  |
| Indonesia | no | IDN Times: market "didominasi merek internasional"; local brands "sempat ikut bersaing" (no renown) | Advan, Andromax, Evercross, Mito, Polytron |  |
| Italy / Germany / Eastern Europe | no | "finest Morse keys in the world are made by Pietro Begali" in Cellatica: a maker statement, not regional renown; the other five are not on this page | Begali | Optibeam, Hilberling, RigExpert, Expert Electronics, Acom |

No region has a renown statement on an independent fetched page. The harvest regions rest on the Wikipedia country list or the amateur-radio category (bare listings). The Oceania entry rests on GME's own site, which cannot establish renown. Turkey rests on an operator-retail blog; Indonesia (IDN Times) says the market is dominated by international brands. The ARRL guide's praise is for Begali, the maker, not for a region. The two South Asia entries are merged.
