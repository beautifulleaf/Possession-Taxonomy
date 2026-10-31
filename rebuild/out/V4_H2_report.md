# V4_H2 report: Health, Medical & Mobility (light pass)

validate.py --v3: OK (192 kinds, 19 archetypes). Backups in rebuild/work/V4_H2/bak/. Fetches: 5 (4 WebFetch, 1 Firecrawl for the Omron page, which WebFetch got as 403).

## Per kind (entries before -> after)
- Collector cane: 6 -> 14 named entries. Reference: Wikipedia "Walking stick" (every named type) plus the Swordstick article. Sections by what the stick is known for (wood or plant, regional, fitted). Shillelagh merged with Blackthorn stick; added Ashplant, Malacca, Supplejack, Kebbie, Waddy, Dress cane, Retractable cane, Tippling cane. Shooting stick, alpenstock, pike staff and scout staff left out as tools. nl, sel, xg and g set. The maker range (Swaine Adeney Brigg) was removed.
- Manual wheelchair: 4 -> 4 entries, now with nl, sel, xg, g; Everest & Jennings badged "origin" (first mass-market wheelchair, Wheelchair page). No whole-space reference exists, said in sel. 11 models and 3 ranges removed.
- Braille device: 1 -> 1 entry (Perkins Brailler), nl, sel, xg, g added. Three models (HumanWare, Freedom Scientific) removed.
- All other kinds (commodity): no named entries; 851 loose models (m) and ranges (r) removed in total across all kinds.

## Brand register
237 makers and brands added to rebuild/out/H2_brands.json, taken from the removed models and ranges (models kept as signature entries, ranges as lines). Country and founding year are blank for all of them because no page was fetched for them. Includes owner groups Sonova, Demant, GN Store Nord, Sivantos and Haleon (also blank). Existing entries unchanged. rebuild/out/H2_renames.json is {}. H2_moves.json unchanged.

## Market panels (ms and msum)
- Monitors, tests & dosing: Omron about 46 % of world home blood-pressure monitors by value, FY2015 (Omron press release, 5 Dec 2016; company's own research).
- Hearing: 2012 unit shares, Bernstein as reported by Hearing Health & Technology Matters (2013): Sonova 24, Demant 23, Sivantos 17, GN 16, Starkey 9, Widex 9 %. Old; WS Audiology has no separate figure.
- Supplements & nutrition: Haleon largest vitamins, minerals and supplements player, about 3 % (2023, Haleon 20-F).

## Not sourced
- Over-the-counter medicines panel (Haleon, Kenvue, Bayer, Sanofi): no fetched page gives a comparable ranking. Haleon's 20-F states "third largest player, approximately 11 %" under an oral-health heading, so it was not used; Kenvue's 10-K names competitors without shares.
- A current hearing-aid share (WS Audiology) and any blood-pressure share by maker other than Omron.
- own, tier, cty and own_y on the wheelchair entries; country and founding year for new register brands.
