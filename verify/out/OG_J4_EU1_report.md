# OG_J4_EU1 report (designations only)

Output: verify/out/OG_J4_EU1_designations.tsv, 99 rows: IT 62, PT 17, GR 9, ES 7, HR 3, CY 1, MT 0. Fetch log: verify/work/OG_J4_EU1/fetched.tsv. Build script: verify/work/OG_J4_EU1/build.py.

Coverage is partial. This is not a full class 1.6 harvest.

Sources that served:
- Wikipedia IT and PT lists, via WebFetch summaries (rows marked partial).
- Wikipedia Andalusian and Croatian lists.
- OJ regulations 245/2002, 547/2000, 905/2002, 1491/2003, 1665/2003 and 417/2006 (BOE PDFs, read locally with pdftotext). These are the full-status rows.
- legislation.gov.uk for Firiki Piliou (414/2011) and Tomataki Santorinis (1400/2013).
- Sicily regional list (post-2011 Sicilian additions) and Lazio list.
- Taste of Cyprus; greeknewsagenda.gr (Greece).

Sources that failed:
- eAmbrosia: JavaScript-only app, loads a title and nothing else.
- Parallel tools: HTTP 402, no credit. Only WebSearch and WebFetch were used.
- Greek ministry (minagric.gr): HTTP 403.
- MAPA Spain: 503 or 404 on the DOP/IGP annual reports.
- visitgreece.gr: empty body.
- eur-lex 2023/691: empty.
- MASAF: not reached.

Gaps (all need a retry):
- Spain is badly under-covered: only 7 rows, and the major fruit and vegetable names are absent.
- Italy: the Wikipedia table stops at 2011 and the Sicilian list adds only Sicilian names. Other post-2011 Italian names are missing.
- Greece: names are English renderings from a news page, not the registered Greek names, except the two taken from regulations.
- Portugal: Batata-Doce da Madeira, Cebola da Madeira and Alho da Graciosa appeared only in a search excerpt (Aldeias Portuguesas), not a fetched page, so they are not written.
- Cyprus: one row.
- Malta: nothing found.
- Croatia: schemes and dates are not shown on the fetched page.

Quality notes:
- Italian "del/della/dell'" forms were garbled to "of" in the Wikipedia summariser output. I restored them from Italian grammar. Each affected row says so in notes and needs a register check.
- One mistake: early on I typed an eAmbrosia URL from memory instead of taking it from a search result. It failed and was not used as a source.
- Pesca Bivona has no scheme on its page, so the scheme is blank.
- Citrinos do Algarve (PGI) is a tag row. Its kinds_served is assumed from the word "citrus".

Skips to other categories (about 48):
- Italy 35: chestnuts and marroni 12, dried beans 6, rice 3, hazelnuts 3, table olives 3, farro 2, lentil 1, chestnut flour 1, pistachio 1, caper 1, plus Pistacchio di Raffadali and Cappero delle Isole Eolie.
- Portugal 6: rice, almond, 4 chestnuts.
- Spain 4: Pimiento Asado del Bierzo, Aceituna Aloreña, Pasas de Málaga, Garbanzo de Escacena.
- Croatia 3: Brački varenik, Ogulinsko kiselo zelje (sauerkraut), Komiški rogač (carob).

"missing kind?" rows (17), by type, with source URL:
- artichoke, 3 rows (Paestum, Romanesco, Spinoso di Sardegna): https://en.wikipedia.org/wiki/List_of_Italian_food_and_drink_products_with_protected_status
- prickly pear, 2 rows: the same Wikipedia page for Ficodindia dell'Etna (also Reg. 1491/2003, https://www.boe.es/doue/2003/214/L00006-00007.pdf), and for Ficodindia di San Cono https://svilupporurale.regione.sicilia.it/storage/2026/03/SRG-10-All.-5-Elenco-prodotti-agricoli-e-alimentari-rientranti-nei-regimi-di-qualita.pdf
- fig, 1 row (Fico Bianco del Cilento): the Wikipedia page above (also https://boe.es/doue/2006/072/L00008-00009.pdf)
- wild mushroom, 1 row (Fungo di Borgotaro): the Wikipedia page above
- salad leaf or chicory, 1 row (Insalata di Lusia): the Wikipedia page above
- radicchio or chicory, 4 rows: the Wikipedia page above
- cherimoya, 1 row (Chirimoya de la Costa Tropical): https://en.wikipedia.org/wiki/List_of_Andalusian_food_and_drink_products_with_protected_status
- anona (custard apple), 1 row (Anona da Madeira): https://en.wikipedia.org/wiki/List_of_Portuguese_food_and_drink_products_with_protected_status
- passion fruit, 1 row (Maracujá dos Açores/S. Miguel): the Portuguese Wikipedia page above
- Firiki (Pelion), 1 row, fruit type unconfirmed: https://www.legislation.gov.uk/eur/2011/414/data.html
- taro (kolokasi), 1 row: https://tastecyprus.com.cy/en/cypriot-products/
