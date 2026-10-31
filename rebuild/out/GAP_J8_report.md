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

## Round 2
About 40 further fetches (13 MediaWiki extract calls, 4 list pages, 12 share pages). validate.py --v3 OK (142 kinds).

**Lists read to their end:** List of confectionery brands (286 rows), List of ice cream brands (150 rows), List of brand name breads (27 rows) and the snack, popcorn, nut and cracker rows of List of brand name food products. The separate "List of brand name snack foods" page could not be found by search (only an archive mirror, not used).
**Added 88 entries** under their flagship kind with owner, tier and country from the list or the brand's intro: sweets and chocolate 41 (Allen's, Brach's, Ferrero Rocher, Heath, Hot Tamales, Rowntree's Fruit Gums, Tootsie Pop family and others), ice cream 26 (Good Humor, Kibon, Paddle Pop, Ben & Jerry's, regional dairies), bread 14 (Wonder Bread, Tip Top, King's Hawaiian, Lender's, Wibs), snacks 15 (popcorn, Cheezies, San Nicasio, Twiglets, Nobby's). 52 owner stubs added to the register. Loaf & Bundt cake gained its first entry (Entenmann's).
**Left out:** company names with no product brand (Arcor, Storck, Ferrara, Tangerine, Froneri), parlour and shop chains, defunct brands (Hippy Sippy, Ipso, Milkfuls, McCowan's, Texan, Tudor Crisps), generic sweet names (Humbugs, Wine gum), and items without a kind (Peperami, Slim Jim: no meat-snack kind; Nutella: J5).

**Share markets, second attempt**
- Germany biscuits: Bahlsen market leader with rising share, 2015 (Lebensmittelzeitung, no figure); the 11.7 % excerpt came from a PDF that now redirects.
- UK biscuits, France bread (Harrys about 36 % volume, Jacquet about 15 %, seen only in a search excerpt), Brazil snacks, Japan (Meiji 10 %, Lotte 9 % in 2021, seen only in a Statista excerpt): no fetched page states a figure. Pladis, Meiji, Barilla and Bimbo annual reports were searched for; none was found with a share. Blocked pages are in firecrawl_deferred.md.
