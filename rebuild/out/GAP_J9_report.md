# GAP_J9 report (Soft Drinks & Water)

Files: J9.json, J9_brands.json (27 owners added), J9_renames.json (two emptied kinds mapped). Backups and scripts in rebuild/work/GAP_J9/. `validate.py --v3`: OK (104 kinds, 960 entries). About 56 fetches, logged in sources.tsv. Firecrawl not used.

## 1. Loose models
None in J9 (no kind keeps `m`); nothing removed.

## 2. Coverage line
All 106 kinds with entries now end `sel` with "No complete list exists; follows <the pages their entries cite>". No whole-space list of soft-drink, water, juice, syrup or energy brands exists, so no kind says "Complete" or "Covers n of m". Two kinds emptied by the owner pass were removed.

## 3. Partial coverage
None to extend, since no kind claims partial coverage of a reference. The Coca-Cola brand list was read A to S plus the tail in V4_J9 and was not re-read here.

## 4. Gaps closed
- Owners: 38 of the 387 ownerless brands now have an owner and `os` source (349 remain blank). Examples: Saratoga (BlueTriton Brands, 2021), Bionade (Hassia, 2018), La Colombe Draft Latte (Chobani, 2023), Cedevita (Atlantic Grupa, 2001), Cockta (Atlantic Grupa, 2010), Kola Real (Ajegroup), Bilz y Pap and Kem (CCU), Cristaline (Alma Group), Twizza (Varun Beverages, 2026), Dr. Brown's (Honickman Companies), Calpis (Asahi), Rose's and Ghost (Keurig Dr Pepper). 30 entries moved to the matching Independents kind, two (Ghost, Rose's) to the Keurig Dr Pepper kinds.
- National champions: Hamoud Boualem (Algeria, nearly 50 % of soft drinks per a family-business history) and Julmust (Sweden, outsells Coca-Cola at Christmas, about 50 % of December soft drink volume) set to National champion and landmark.
- Market facts added to `ms`: Nigeria carbonates, Coca-Cola leader 2017 (Euromonitor via Marketing Edge, no figure); China bottled water, Nongfu Spring top seller 2012 (Nielsen, no figure).

## What remains, with searches tried
- 349 brands without owner: pages fetched for the brand named no owner (Ramune is made by several firms; UCC, Guayakí, Thomas Henry, Belvoir, Q Mixers, Remedy, Fassbrause brands, Chinotto brands, Julmust makers other than Roberts). No ownership statement was found on a fetched page after two tries.
- Market shares: Brazil (2008 ABIR split only in a search excerpt; Mintel/Statista paywalled), Mexico (only reach rankings), Germany (Gerolsteiner release returned 404; Wikipedia page has no share), South Africa (Twizza 10 or 23 percent conflict in excerpts, no fetched page), UK, China beyond Nongfu (no fetched share), Nigeria beyond the 2017 ranking. Searches: "Brazil soft drink market share Coca-Cola Ambev...", "Mexico carbonated soft drinks market share...", "Germany soft drinks market share...", "Nigeria carbonated soft drink market share...", "China bottled water market share...", "South Africa soft drinks market share...".
- Not owner-resolved from the groups' own sites (Coca-Cola FEMSA, Arca Continental, Postobón, Polar, Uni-President, Lotte Chilsung): not fetched within budget.
- Step 5 (sections): entries in kinds with `xg` already carry `g`; no change.
