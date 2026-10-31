# CMP_WINE report

File edited: rebuild/out/J7.json (backup in rebuild/work/CMP_WINE/bak/). Scripts and progress.md in rebuild/work/CMP_WINE/. `validate.py --v3`: OK (0 errors, 391 kinds).

| List | Before → after | Reference total | Method |
|---|---|---|---|
| Italy DOCG / DOC / IGT | 76 / 330 / 113, unchanged | Wikipedia pages: 76 named (page says 77), 330, 113 distinct (117 rows) | Re-read pages; Wikidata has about 980 DOC items but they are typologies and sub-zones of the same appellations, so none added. |
| Spain DOP | 96 → 103 | 103 in the Ministry of Agriculture report for 2023/24 (2 DOCa, 69 DO, 7 VC, 25 VP) | Added Vinos de Pago Rosalejo, Chozas Carrascal, Bolandín, Abadía Retuerta, Dehesa Peñalba, Urueña and VC Cebreros (new kind for Castile and León pagos). Fetched with Firecrawl (WebFetch gave 503). |
| Spain IGP | unchanged | 43 IGP | Not found in a fetched register; stated in the coverage line. |
| Romania DOC | 42 vineyard entries → 54; 33 marked DOC | 33 DOC | Sommgeo table plus winebrotherhoods.org (32 DOC, 10 sparkling DOC); 12 added, rest marked in `d`. |
| Romania IG | 4 → 16 | 12 IG | Brotherhood list added; the four older names kept. |
| Bulgaria | 5 regions → plus 52 PDO | 52 PDO | New kind from the Sommgeo table. Official register not read. |
| Slovenia | 14 → 21 | 14 PDO | 7 PDO names that are not districts added. |
| Croatia | 12 → 18 | 18 PDO | 6 added (including Dingač). |
| Czechia | 6 → 11 | 11 PDO | 5 added (Čechy, Morava, Novosedelské Slámové víno, Šobes, Znojmo). |
| Chile | 20 → 24 | page read to its end | Added Atacama, Coquimbo, Austral, Central Valley. The page has no DO list. |
| Argentina | 27, unchanged | page read to its end | Nothing further after character 100,000. |
| New Zealand | 32 → 33 | page read to its end | Added Central Hawke's Bay. |
| Grape varieties | 849 → 866 | Wikipedia list read to its end | Added 17 wine grapes of American species (labrusca, muscadine, Black Spanish, Mustang) as a new kind. Hybrids from the list were already present. |

Coverage lines were appended to `sel` on the touched kinds (Spain, Italy, Romania, Bulgaria, Slovenia, Croatia, Czechia, Chile, Argentina, NZ, grapes). The "first part of the page only" notes were removed from South America and Australia/New Zealand kinds.

## Still short
- Italian DOC: no register count beyond Wikipedia's 330; the official register may be slightly different.
- Spanish IGP (43) and Portuguese IG lists not re-checked.
- Romania: 33 DOC reconciled across two sources; Bulgaria and Croatia PDO names rest on one trade source (Sommgeo), with no descriptions beyond "PDO".
- Czech municipalities, German Einzellagen, Chile and Argentina formal appellations: not covered.
- Grapes went through a page summariser; rosé rows look doubtful (Zinfandel Rose as Austrian, etc.) and were not changed. Completeness is not proven.
- Brazilian, Chinese and other Asian appellations untouched (outside the brief).
