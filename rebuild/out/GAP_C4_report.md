# GAP_C4 report: Craft & Art Supplies

validate.py --v3 OK (316 kinds, 483 entries). Backups in work/GAP_C4/bak/; fetches in work/GAP_C4/sources.tsv (about 14 fetches, 3 searches).

## Closed
1. Loose models: none remained (0 kinds with `m`); nothing removed.
2. Coverage lines: all 132 kinds with entries now end `sel` with one. Yarn weight class: "Complete: 8 of 8 in Wikipedia's Yarn article". Artists' pigment: "Covers" the whole Wikipedia List of inorganic pigments, organic part partial. The other 130 kinds: "No complete list exists; follows <three most-cited source sites> and the makers' ranges", because product-range kinds have no whole-space reference.
3. Sections: every kind with `xg` already has `g` on all entries (0 missing); the 26 entries in kinds without `xg` are small kinds (1 to 4 entries) and need no axis. Artists' pigment (130) and Watercolour paint (14) are sectioned by `g`.
4. Market facts, now fetched: F.I.L.A. S.p.A. owns Lyra (2008), Daler-Rowney (2016), St Cuthberts Mill (2016), Canson (2016, already set), Pacon with Strathmore and Princeton (2018), Arches (2019). Sakura Color Products owns Royal Talens (1991). Lion Capital bought DMC (2019). Faber-Castell AG (family), Staedtler SE, Janome Corporation, Bernina International, Brother Industries and Tamiya Corporation are private or listed independents. `own` and `tier` set on 38 more entries, `own_y` where the page gives a year. Three owners added to C4_brands.json (F.I.L.A., Sakura Color Products, Lion Capital).

## Remains
- Organic pigment canon: Wikidata class query returned 0 rows; searched "list of organic pigments Colour Index PR PY PB PV generic names"; only partial artist tables found. Not complete.
- Arches and Fabriano family lists: searched "Arches watercolour paper range ... Huile Platine Cover"; only retailer pages for the Aquarelle surfaces, not fetched as attestation. Not added.
- Owners not found: Sizzix (Wikipedia names only "Ellison"), Derwent (Wikipedia page 404), Sculpey/Polyform, Cricut, Singer-line others, Lion Brand, Hobbs, Spellbinders, Clover, Olfa, Iwata, Holbein, Kuretake, Schmincke, Sennelier, Pebeo. Left empty; no second attempt made within budget.
- Colart sub-brands (Reeves, Lefranc & Bourgeois, Letraset) were sourced but no entry carries them as `mk`, so none were set.
- No department `ms` market summary: no share figures were fetched (none searched for beyond the owner pages).
- Firecrawl not used; no deferred pages.


## Round 2 (45-fetch pass)
- **Organic pigments:** added 124 Pigment Red organics (PR1 to PR288) from The Color of Art Pigment Database red page, read to its end; Artists' pigment is now larger and `sel` says so. Not read: its Yellow, Orange, Violet, Blue, Green and Brown pages (names in the database are partly scrambled by the page summariser; the code and the page's common name are kept as given). No Wikipedia list of organic pigments exists; the Wikidata class query returned 0 rows; Handprint and ColourLex were not returned by search.
- **Fabriano:** 10 lines added (Studio Watercolour, 1264 Sketch, 1264 Bristol, Studio Mixed Media, Artistico Pittura, Tela, Black Black, Toned, Classic Journal, Venezia) from the Aboveground overview, read in full. Arches: the Cornelissen page names only Aquarelle, with 185/300/640/850 gsm and three surfaces, noted on the entry; Huile, Platine and Cover not found on a fetched page.
- **Owners set:** Derwent (ACCO Brands, 1980), Sizzix (Ellison), Schmincke (family-owned H. Schmincke & Co. GmbH & Co. KG), Kuretake, OLFA, Cricut, Lion Brand (Blumenthal family): 27 entries. Not found: Polyform (LLCP held it Dec 2013 to Feb 2018; later owner unstated), Anest Iwata (page does not mention the airbrushes), Sennelier (private, owner unstated), Pebeo (family link only), Holbein (403 from Jackson's; searches gave only retailer text; deferred).
- **Colart sub-brands:** Reeves, Lefranc & Bourgeois, Charbonnel, Letraset, Snazaroo, Elephant Art added to the brand register; no entry has any of them as maker, so none set on entries.
- **Market facts (`ms`):** F.I.L.A. EUR 612.6 million revenue 2024; Faber-Castell EUR 618.4 million turnover 2023/24; Cricut USD 709 million 2025. These are company revenues, not shares. Colart: intranet host blocked and no total found (search only gives 2023 growth of 4.1 %). Cricut annual report itself not fetched (Wikipedia figure used).
