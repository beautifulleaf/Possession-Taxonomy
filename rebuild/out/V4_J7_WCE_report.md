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

## Complete-lists pass (step "complete-lists")
Firecrawl was used only for eAmbrosia-related pages WebFetch could not read (JS lists). The eAmbrosia register itself is a JavaScript app and was not readable; national and trade lists stand in.
- Greece: all 33 PDOs and the full PGI list (114 names, matching the stated count, incl. retsina and Verdea) from the Wines of Greece appellations page (Firecrawl). Old Retsina kind merged into "Greece: PGI wines".
- Switzerland: new kind of cantonal wine areas with communes (German Wikipedia); the 62-AOC federal list was not found.
- Hungary: 22 regions plus 9 sub-region/large-area PDOs and 6 PGIs (Taste Hungary, 2023: 31 PDOs, 6 PGIs). Kőszeg, Füred and Mura PDOs (2025-26 news) not added.
- Slovakia: all 40 districts; Czechia: six sub-regions only (municipalities sit in decree 254/2010, not fetched).
- Cyprus: 5 PDOs and 4 PGIs (government Labels of Taste); Romania: 4 IGP regions added.
- VDP Grosse Lage: only 5 sites on a fetched page (as versions); OeTW Erste Lage not fetchable (401).
- Still missing: Bulgarian PDO/PGI (page 503/404), Romanian 33 DOC and 8 other IGP names, Slovenian and Croatian PDO lists, German Einzellagen. Totals: 33 kinds, 587 entries; check OK.

## Remaining gaps
