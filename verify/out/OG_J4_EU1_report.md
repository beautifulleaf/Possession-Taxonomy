# OG_J4_EU1 report (designations only), revision 2

Output: verify/out/OG_J4_EU1_designations.tsv, 129 rows: IT 79, PT 18, ES 17, GR 11, HR 3, CY 1, MT 0. Fetch log: verify/work/OG_J4_EU1/fetched.tsv. Build scripts: verify/work/OG_J4_EU1/build.py, build2.py, build3.py. Rows replaced under their old designation_id; new rows added.

## Spelling pass (coordinator request)
- The 8 rows I had "restored" are rewritten from an Italian page: the national DOP/IGP/STG register extract (updated 23.03.2023) published by Regione Calabria. The same page now serves as the primary source for all 79 Italian rows, so every Italian name is spelled as that page spells it.
- Where the Wikipedia list spelled a name differently, the register spelling replaced it and the old spelling is kept in notes. The changes are: Cipolla Rossa di Tropea Calabria, Mela Alto Adige o Sudtiroler Apfel, Peperoni di Senise, Pescabivona, Pera mantovana.
- For Pera dell'Emilia Romagna, Pomodoro di Pachino, Pomodoro S. Marzano dell'Agro Sarnese-Nocerino and the two Radicchio rows, the extract shows an amending regulation. I kept the original regulation and date from Wikipedia and noted the amendment.
- Greek names are now in Greek, as spelled in the consolidated annex of Reg. 1107/96. Spanish and Portuguese names follow that annex or the Official Journal.
- Tomate La Cañada is now spelled as Reg. 487/2012 spells it. Wikipedia had "Tomate de La Cañada-Níjar".

## Gaps filled
- Italy after 2011: Anguria Reggiana, Asparago di Cantello, Carciofo Brindisino, Ciliegia di Bracigliano, Ciliegia di Vignola, Cipolla bianca di Margherita, Finocchio di Isola Capo Rizzuto, Limone di Rocca Imperiale, Mela Rossa Cuneo, Mele del Trentino, Melone Mantovano, Patata del Fucino, Patata novella di Galatina, Patata Rossa di Colfiorito, Rucola della Piana del Sele, Susina di Dro, Uva di Puglia, plus the Sicilian additions.
- Greece: 7 names in Greek from the 1107/96 annex, plus Κουμ Κουάτ Κέρκυρας and Σύκα Βραβρώνας Μαρκοπούλου Μεσογείων. Φιρίκι Πηλίου and Τοματάκι Σαντορίνης come from their regulations.
- Spain: Cerezas de la Montaña de Alicante, Espárrago de Navarra, Nísperos Callosa d'En Sarriá, Pimientos del Piquillo de Lodosa, Uva de mesa embolsada 'Vinalopó', Cereza del Jerte, Alcachofa de Tudela, Pimiento de Fresno-Benavente, Pimiento Riojano, Cebolla Fuentes de Ebro, Tomate La Cañada.
- Portugal: the 12 names also in 1107/96 now carry that regulation and date. Batata-Doce da Madeira (PDO, 2024-07-05) is added.
- Croatia: Neretvanska mandarina PDO (2015/1150, 2015-07-01), Lički krumpir PGI (2015/1738, 2015-09-21), Varaždinsko zelje PDO (2017/1900, 2017-10-18). The Wikipedia page showed no schemes.
- Cyprus: Kolokasi Sotiras now has the Greek name, PDO, and EU registration date 3 August 2016 (UK GI register page).

## Still open
- Spain remains incomplete. MAPA PDFs returned 503 on every attempt, and the boe.gob.es host returns only a redirect notice. Not written because I found no fetchable page for them: Cítricos Valencianos, Cebolla de la Mancha, Melón de La Mancha, Alcachofa de Benicarló, Nísperos/other Valencian names, Pera de Lleida, Manzana Reineta del Bierzo, Pera del Bierzo and others. Retry MAPA later.
- Malta: nothing in class 1.6. Search excerpts show only Ġbejna tan-nagħaġ (cheese) and wine, so zero rows.
- Cyprus: Kolokasi is the only fresh-produce name found.
- Portugal: Cebola da Madeira (PDO-PT-02800) and Alho da Graciosa were seen only in search excerpts, so they are not written.
- eAmbrosia is JavaScript-only. Parallel tools returned 402. The Greek ministry page returned 403. EUR-Lex pages return empty bodies, so the lexaris, legislation.gov.uk and inforlex mirrors were used instead.
- The 1107/96 annex, the Italian register and several lexaris pages are read through a summariser or a saved PDF, so those rows are marked partial where the text was summarised.

## Skips to other categories (about 65)
Italy: chestnuts and marroni, dried beans and lentils, rice, farro, flours, hazelnuts, pistachios, capers, table olives, dried figs (Fichi di Cosenza) and Brovada. Also Portugal rice, almond and chestnuts, Spanish pulses, rice and Pimiento Asado del Bierzo, the Greek table olives, pistachios, dried figs, beans and currants, and Croatian Brački varenik, Ogulinsko kiselo zelje and Komiški rogač.

## "missing kind?" rows (23)
All sources are in the sources column of the TSV; the main URLs are below.
- artichoke (Paestum, Romanesco, Spinoso di Sardegna, Brindisino, Alcachofa de Tudela): https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf and https://www.boe.es/doue/2001/269/L00005-00006.pdf
- prickly pear (2): the Calabria register above
- fig (Cilento): the Calabria register above
- fig (Vravronas Markopoulou Mesogion): https://www.legislation.gov.uk/eur/1996/1107/2008-11-20/data.xht
- radicchio/chicory (4): the Calabria register above
- salad leaf (Insalata di Lusia): the Calabria register above
- wild mushroom (Fungo di Borgotaro): the Calabria register above
- fennel (Isola Capo Rizzuto): the Calabria register above
- cherimoya: https://en.wikipedia.org/wiki/List_of_Andalusian_food_and_drink_products_with_protected_status
- anona, passion fruit: https://en.wikipedia.org/wiki/List_of_Portuguese_food_and_drink_products_with_protected_status (passion fruit also the 1107/96 annex above)
- Firiki Piliou (fruit type not stated): https://www.legislation.gov.uk/eur/2011/414/data.html
- kumquat, loquat: https://www.legislation.gov.uk/eur/1996/1107/2008-11-20/data.xht
- taro (Kolokasi): https://www.gov.uk/protected-food-drink-names/kolokasi-sotiras-slash-kolokasi-poulles-sotiras-slash-kolokasi-sotiras-slash-kolokasi-poulles-sotiras
