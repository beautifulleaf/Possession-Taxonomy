# GAP_B5 report (Kitchen & Dining)

Validator: OK (--v3), 277 kinds, 737 entries. About 58 fetches used. Backups in rebuild/work/GAP_B5/bak/; sources in rebuild/work/GAP_B5/sources.tsv.

## Closed
1. **Loose models.** None left: rebuild/out/B5.json holds no `m` on any kind (the "84 kinds" in gaps.md counted the older reader file). Nothing removed in this pass.
2. **Coverage lines.** All 100 kinds with entries now end in a "Complete:" or "No complete list exists; follows ..." sentence (90 rewritten by rebuild/work/GAP_B5/cov.py from the old "Covers n lines" wording; no kind claims a total it lacks).
3. **Partial coverage.** Glassware house 101 to 107. Read Category:Glassmaking_companies, its by-country subcategory and the Belgian, Swiss, Slovak, Turkish, Indian, Chinese and Maltese pages. Added Val Saint Lambert, Glasi Hergiswil, Rona, Paşabahçe, Borosil, Mdina Glass. Left out as out of scope: Liuli Gongfang (art studio, visual art), Hindustan National Glass, Vetropack, AGC, Chinese flat-glass firms, Bodum (already an entry). The Azerbaijan and Bangladesh categories were not read. Tableware house was already complete against both Wikipedia lists.
4. **Owners and market facts (fetched Wikipedia pages).** Added owner, tier and year to Anova (Electrolux 2017), Blendtec (Wasatch Group 2021), AeroPress (Tiny Capital 2021, tier changed from Craft to Independent), Instant Pot (Centre Lane Partners 2023), La Marzocco (De'Longhi S.p.A., majority by late 2023), Rancilio Silvia (Ali Group 2013), SodaStream (PepsiCo 2018), CamelBak (Vista Outdoor 2015, as the page states), Viking (Middleby 2013), AGA, Rangemaster, Falcon and La Cornue (Middleby; AGA group 2015), Cuisinart (Conair 1989), Waring (Conair 1998), Hamilton Beach, Sunbeam Mixmaster (Newell Brands), Russell Hobbs K2 (Spectrum Brands 2010), Bodum, Melitta. Paşabahçe owner Şişecam. Meissen already held Free State of Saxony.

## Remains (two attempts each)
- Owner not stated on fetched pages: Chemex, Dualit (family-run, no owner named), Oster and Osterizer (page says Sunbeam bought Oster in 1960; no current owner), Hario (company page names none), Richard-Ginori, Narumi (searched "Narumi porcelain company Nagoya founded 1946 owner"; Wikipedia 404), Moser (Wikipedia title 404; searched "Moser Karlovy Vary glassworks current owner"), Zalto, Glasi Hergiswil, Rona, Mdina.
- Bialetti: page reports only an April 2025 agreement with Nuo Capital for 78.567 %, so no owner entered.
- La Cornue and Falcon own_y not given by the group page.
- Eureka Mignon owner: the Wikipedia "Eureka" page is the US vacuum maker; not used.
- Market shares for small appliances, coffee machines and kettles; Samsung and LG panels; Euromonitor percentages: not searched in this pass (budget went to owners).
- Section axis (step 5): Cutlery set (17 entries) and the other tableware kinds (Plate, Steak knife, Serving, Butter dish etc.) still have no `g`; maker countries are not on the cited pages and the brand register lacks them. Cocktail shaker and Corkscrew have `xg` but no `g`.
- Not touched: Susie Cooper and Pyrex patterns, Ninja Foodi 2018 source, Misono and Tojiro founding years, Kai and Lodge Wikipedia 404s.
- Not attempted: Wikidata SPARQL for glassware makers; Firecrawl (none needed, nothing deferred).
