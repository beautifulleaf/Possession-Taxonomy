# OG_J2 report

Rows: designations 86, varieties 14, grading_scales 9. Helper files and the fetch log: verify/work/OG_J2/ (fetched.tsv, r*.py).

Designations by country: JP 19, CN 12, GB 11, FR 7, KR 7, IT 5, DE 5, ES 3, HU 3, LV 2, HR 2, SE 2, NO, PT, PL, CZ, IE, FI, RO, TH 1 each. By scheme: GI 39, PGI 33, PDO 12, TSG 2.
Varieties: 11 oyster strains/names (Kumamoto, Olympia, Belon, Sydney rock, Bluff, Kiwa, Shigoku, Beausoleil, Wellfleet, Misty Point, Kumiai) and 3 tilapia strains (GIFT, Chitralada, GESIT). No mussel strains found.
Grading scales: EU freshness categories (Extra/A/B), EU size categories (stub, Annex II steps not on any fetched page), Norwegian salmon grades, French cupped-oyster numbers, French claire classes, shrimp count bands, scallop count bands (partial), Japanese-market tuna number grades, Codex 70 canned tuna presentations. Caviar grades not written (only retailer pages, no body or trade standard named). USDA/NOAA fillet grades not written: no fetched page gave the grade names (50 CFR 261.103 gives none; NOAA Part 5 PDF over 10 MB).

Sources that served: lexaris.de/lawplayer/legislation.gov.uk copies of the OJ regulations, boe.es OJ PDFs (read from the saved PDF copies), MAFF GI register index and pages, NFQS list page 1, CNIPA crab page, Defra specification PDFs, Wikipedia.
Failed: Parallel_Auth tools (402 no credit, so WebFetch/WebSearch only); eur-lex.europa.eu (empty pages); agriculture.gouv.fr and inao.gouv.fr (503); IP India GI registry (503); op.europa.eu and romania-insider (429); khaosodenglish (403); deccanherald (403); NFQS list pages 2-3 (JavaScript pagination, so 14 Korean rows not reachable); eAmbrosia (scanned PDF, unreadable). India: no fish GI found in the Wikipedia table. Note: WebFetch returns model summaries, not raw pages; fields such as class and country were taken from those summaries.

Skips to other categories: 6 (Phu Quoc fish sauce, Japan いしり, Korean laver 무안돌김, 고흥김, 해남김, plus Colatura-type sauces not searched). Non-fish regulations met and ignored: Queso Camerano, Brački varenik, Paška janjetina, Stafida Ilias, Melekouni.

Not found / not attested (no fetched page): Coquille Saint-Jacques des Côtes d'Armor, Lieu jaune de l'Île d'Yeu, Avgotaracho Messolongiou (503), Pohořelický kapr, Lausitzer Karpfen, Caviar de Riofrío, Shengsi portunus (no registration details), Wando gim, Yeonggwang gulbi, Vietnam/Indonesia/Türkiye/Brazil/Mexico/Peru/Chile/Colombia/Africa fish GIs, Whitstable oysters.

"missing kind?" rows (kind_id blank, URL = first source):
- salted anchovy: DS-it-acciughe-sotto-sale-del-mar-ligure, DS-fr-anchois-de-collioure (https://en.wikipedia.org/wiki/List_of_Italian_food_and_drink_products_with_protected_status ; https://www.reussir.fr/lesmarches/melon-du-quercy-et-anchois-de-collioure-sur-la-liste-des-igp)
- tench: DS-it-tinca-gobba-dorata-del-pianalto-di-poirino (Wikipedia Italian list)
- pufferfish (fugu): DS-jp-shimonoseki-fuku (https://www.maff.go.jp/j/shokusan/gi_act/register/0019/index.html), DS-jp-awajishima-3nen-torafugu (https://www.maff.go.jp/j/shokusan/gi_act/register/index.html)
- stockfish: DS-no-torrfisk-fra-lofoten (https://lexaris.de/book/version/documentflat/head/2116589)
- sea trout: DS-gb-west-wales-coracle-caught-sewin (https://www.legislation.gov.uk/eur/2017/596/data.html)
- trout species unspecified: DS-hu-szilvasvaradi-pisztrang (https://www.lexaris.de/book/version/documentflat/head/2064057)
- mixed freshwater fish: DS-hu-balatoni-hal (https://www.lexaris.de/book/version/documentflat/head/2063656)
- lamprey: DS-lv-carnikavas-negi (https://www.legislation.gov.uk/eur/2015/269/data.html), DS-lv-salacgrivas-negi (https://www.lexaris.de/book/version/documentflat/head/2062870)
- vendace/whitefish: DS-fi-puruveden-muikku (https://www.legislation.gov.uk/eur/2013/1262/data.html)
- vendace roe: DS-se-kalix-lojrom (https://www.boe.es/doue/2010/296/L00009-00010.pdf), DS-se-vanerlojrom (https://lawplayer.com/eu/act/32021R2004)
- Siberian sturgeon caviar: DS-fr-caviar-d-aquitaine (https://www.lexaris.de/book/version/documentflat/head/7773378)
- smoked shad: DS-ro-scrumbie-de-dunare-afumata (https://www.digi24.ro/stiri/economie/comisia-europeana-scrumbia-afumata-de-dunare-a-devenit-al-cincilea-produs-recunoscut-oficial-1042255)
- pollan: DS-gb-lough-neah-pollan (https://www.boe.es/doue/2018/098/L00017-00017.pdf)
- whitebait (shirasu), marinated sea bream, cutlassfish: DS-jp-tagonoura-shirasu, DS-jp-wakasa-obama-kodai-sasazuke, DS-jp-toyoshima-tachiuo (https://www.maff.go.jp/j/shokusan/gi_act/register/index.html)
- dried rockfish: DS-kr-sinan-geonureok (https://www.nfqs.go.kr/hpmg/data/actionMarineGeographicForm.do?menuId=M0000230)

Caveats: "Lough Neah Pollan" is spelled as in the Spanish OJ text I read (likely slip for Neagh). Kind choices marked "approximate" (shijimi/ark shell as clam, Melva as tinned mackerel) need review. Miyagi Salmon kind (coho) is a guess.
