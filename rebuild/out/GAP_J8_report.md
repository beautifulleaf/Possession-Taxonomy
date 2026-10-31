# GAP_J8 report (Bakery, Sweets & Snacks)

validate.py --v3 OK (142 kinds). Backups in work/GAP_J8/bak/. About 23 fetches; sources in work/GAP_J8/sources.tsv.

**1. Loose models.** None remain: J8.json has no `m` or `r` fields (the gap list's 56 predates the V4 passes). Nothing removed.

**2. Coverage lines.** All 114 kinds with entries now end with a standard line. "Complete: 219 of 219" for Artisan bakery (Loaf Mark list). "Covers n of about m" for Countline, Mithai, Wagashi, Halva, Marzipan, Nougat & turrón, Baklava & syrup pastries. "No complete list exists; follows ..." for every brand kind and for traditional forms with no reference.

**3. Partial coverage closed.**
- Mithai 9 -> 66 (Wikipedia List of Indian sweets and desserts, read to its end; puddings, drinks, flatbreads and biscuits left out).
- Wagashi 9 -> 33 (Wagashi article; Oshiruko, Kasutera, Aosashi and the classification groups not entered).
- Halva 7 -> 27; Marzipan 7 -> 20; Nougat & turrón 9 -> 15; Baklava & syrup pastries 9 -> 27 (each article read to its end of text; the remainder is references and navigation, checked at offset 100,000).
- Tasali (Saudi Arabia, 1989, PepsiCo 2001) added to Potato crisps and the brand register.
- Not re-read: List of confectionery brands and List of ice cream brands (the first calls itself never complete; ice cream stays at the earlier ~170-row read); chocolate and biscuit brand lists were already read to the end in V4.

**4. Gaps from the reports.** New market facts with years:
- Germany gummy sweets: Haribo 56.1%, Storck 11%, Katjes 9.6%, Trolli 4.7% (2023 report).
- France sweets: Haribo 37.7%, Carambar & Co 14.5%, Lutti 12.7% (article of 2018).
- Turkey/Saudi Arabia/Egypt: Ülker biscuits 33.3%, 18%, 11% and Turkish chocolate 42.1% (Nielsen, 2016).
- Germany bar chocolate: private label 34.5% (Circana, 2025).
- Brazil bread: Bimbo about 37% after Wickbold, Panco about 18% (2025).
- Middle East snack champion: Tasali (PepsiCo), second largest in Saudi Arabia.

**Remains (two attempts each).**
- UK biscuit shares: searched "UK biscuit market share 2024 McVitie's Pladis", "The Grocer biscuits top brands"; Grocery Gazette page fetched, no share stated.
- Japan ice cream and confectionery shares: searched English and Japanese queries; only paywalled reports and a Meiji sales figure (not fetched).
- France bread share, Brazil snack share, Germany biscuit share: not found.
- Saudi 2001 Tasali/PepsiCo 45% share: foodnavigator 404, Progressive Grocer 403; logged in firecrawl_deferred.md, as is lsa-conso.fr (French sweets).

**5. Sections.** Every entry in every kind with `xg` already has `g`; all kinds over 12 entries have `xg`. No change.
