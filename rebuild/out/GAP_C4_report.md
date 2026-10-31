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
