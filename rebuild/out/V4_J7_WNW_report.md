# V4_J7_WNW report: wine of the Americas, southern hemisphere and Asia

Part file: rebuild/out/J7_parts/WNW.json (7 departments, 52 kinds, 664 entries). `validate.py --v3` on the wrapped file: OK. Build script, sources.tsv and progress.md are in rebuild/work/V4_J7_WNW/. J7.json was read only.

## Departments (entries)
- Wine of the United States: 280 AVAs, 6 California kinds by the list's own regions, then Pacific Northwest, Southwest, Midwest, South, Northeast. Multi-state AVAs are filed once, under the first state that lists them. Reference: Wikipedia List of American Viticultural Areas.
- Wine of Canada & Mexico: 56. Ontario and British Columbia VQA areas with sub-appellations (Wikipedia Vintners Quality Alliance); Mexican valleys by state (Wikipedia Mexican wine).
- Wine of South America: 68. Chile by macro-region, Argentina by province, Uruguay by department (2013 hectares), Brazil by region.
- Wine of South Africa: 89 districts and wards by region (Wikipedia Wine regions of South Africa).
- Wine of Australia & New Zealand: 142. Wine Australia's GI register (official) split into zones and regions by state; New Zealand regions and sub-regions with GI years 2017, 2018, 2020 where the page gives them.
- Wine of England & Wales: 5 PDO and PGI names. Wine of China, Japan & India: 24 (10 Chinese areas, 5 NTA wine GIs with dates, 9 Indian areas including the Nashik Valley GI).

## Renames (old grape kind to new kind)
Zinfandel to California: Central Valley AVAs; Malbec to Argentina: Cuyo; Carmenère and País to Chile: Central Valley; Tannat to Uruguay wine departments (its Madiran and Irouléguy entries are French, so the GRAPES or French part should decide); Pinotage to Coastal Region districts and wards.

## Not done or not sourced
- No classified producers or vineyards exist in this scope, so no versions and no `role` badges (no fetched page names a top rank). Colour, style and grapes are in `d` where the page gave them; `tt` is the generic colour and labelling attribute set.
- No market layer: no fetched share figures, so no `ms`/`msum`, `own`, `tier` or brand-register additions (brands list empty).
- Sources are Wikipedia pages rather than official registers, except Wine Australia and the Japanese NTA. The Chile, Argentina and NZ pages were read only for their first 100,000 characters. The Chile and Argentina pages and Brazil give no formal appellation lists (Brazil IP/DO, Chile coastal/andean subdivisions and Argentine GIs not covered). Nova Scotia and Quebec: page names no designation, so no kind. English Quality Sparkling Wine, Darnibole and Westerhill not on the fetched page. China has no GI list from a fetched page (Helan Mountain East and Yantai GIs appeared only in search excerpts). Nashik Valley GI year conflicts between sources, so it is omitted. AVA approval years are not on the page, so `y` is blank.
- Old grape kinds not renamed (Cabernet Sauvignon, Pinot Noir, Syrah, Petite Sirah, Cap Classique, Sparkling Shiraz, Ice wine, etc.) hold mostly or no wines of this scope and are left to the GRAPES and other parts. Dropped: Boberg (repealed fortified designation).
