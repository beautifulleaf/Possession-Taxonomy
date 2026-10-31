# V4 J7 WCE report

Part file: rebuild/out/J7_parts/WCE.json. Validates OK (27 kinds, 378 entries; only the wrapper check was used). Sources are in rebuild/work/V4_J7_WCE/sources.tsv; the build script is rebuild/work/V4_J7_WCE/build.py. Fetched only with WebFetch (no Firecrawl).

## Departments (6) and kinds
- Germany, Austria & Switzerland: Anbaugebiete (13), Bereiche (40, with ~150 Grosslagen as versions), Landwein regions (19); Austria Weinbaugebiete (5) and DACs (18, Wachau grades as versions; Weinviertel marked origin as "first DAC"); Swiss regions (6) and Vaud AOCs (6 + Dézaley Grand Cru).
- Hungary & Central Europe: 22 Hungarian regions (Tokaj styles and the 1730 classes as versions); Czech sub-regions (6, VOC as versions); Slovak regions (6, Slovak Tokaj styles); Polish areas (5).
- Balkans: Slovenia (14 districts), Croatia (12 sub-regions, Dingač/Postup as versions), Serbia (22), Southern Balkans (12).
- Eastern Europe: Romania (43 vineyards), Bulgaria (5), Moldova (6), Ukraine (4), Russia (4 regions + 11 appellations).
- Greece & Cyprus: Greece 19 PDOs, Cyprus 5.
- Turkey, Caucasus & Levant: Turkey (6), Georgia (5 regions + 46 named wines by colour), Armenia (8), Lebanon (5), Israel (5).

## Renames (old grape kinds)
Blaufränkisch, Zweigelt -> Austria DACs; Kadarka, Furmint, Tokaji -> Hungary; Plavac Mali -> Croatia; Prokupac -> Serbia; Mavrud -> Bulgaria; Xinomavro, Agiorgitiko, Assyrtiko, Moschofilero -> Greece; Saperavi, Aleksandrouli, Rkatsiteli, Kisi -> Georgia; Müller-Thurgau, Sylvaner, Kerner -> Germany.
Old entries are covered: Mittelburgenland, Leithaberg, Eisenberg, Egri Bikavér (Eger version), Dingač, Postup, Naoussa, Amyntaio, Goumenissa, Mukuzani, Napareuli, Kindzmarauli, Akhasheni, Khvanchkara, Tsinandali, Dry Tokaji Furmint, Santorini/Nykteri/Vinsanto, Tokaji styles. Somló Furmint is covered by the Nagy-Somló region; Šipon is a Slovenian grape synonym and not an entry. Not carried: Washington Lemberger (US part), Alto Adige Kerner (Italy part), Greek Messenikola and Zitsa-type names not on fetched pages.

## Dropped or left
No kind dropped. Left for other parts: Riesling, Grüner Veltliner, Chasselas, Petite Arvine, Savagnin (Heida), Sekt, Retsina, Gemischter Satz, Commandaria entry in the passito kind (now also in Cyprus), Georgian qvevri amber wine entry. Brands: none added (no classified producers used). Moves: none.

## Gaps (honest)
- The EU register (eAmbrosia) and national lists were not retrievable; WebFetch summaries of Wikipedia were the canon. Greece lists only the 19 PDOs named on fetched pages (33 PDOs and 114 PGIs exist), Swiss cantonal AOCs (62) are missing apart from Vaud, Hungarian PDO sub-districts and Czech/Slovak districts are missing, Austrian ÖTW Erste Lage, German VDP Grosse Lage and Tokaj named first-growth vineyards are not on fetched pages, so no landmark badges beyond Weinviertel (origin).
- Armenian Artsakh was left out. Pages for the Georgian list were read to 100,000 characters only. Alcohol field not needed (no alcohol-free items). No department market summary (`ms`) was added: no share figures were fetched.
