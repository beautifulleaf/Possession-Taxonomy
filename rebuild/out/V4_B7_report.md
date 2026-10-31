# V4_B7 report: Portable Climate & Air (light pass)

Files edited: B7.json, B7_brands.json; B7_renames.json created empty ({}); B7_moves.json unchanged. Backups in rebuild/work/V4_B7/bak/. validate --v3: OK (29 kinds).

## Kinds
All 28 commodity kinds had their loose models (m) and ranges (r) removed as out of scope (the kind is the end). Counts removed per kind:
Fan heater 8, Convector heater 8, Oil-filled radiator 8, Radiant heater 5, Infrared panel heater 9, Electric fireplace 4, Kerosene heater 10, Portable gas heater 5, Window air conditioner 11, Portable air conditioner 15, Evaporative cooler 5, Desk fan 5, Box fan 2, Pedestal fan 9, Tower fan 7, Air circulator 8, Window fan 2, Wall or clip fan 5, Handheld fan 6, Neck fan 2, Air purifier 18, Replacement air filter 2, Indoor air quality monitor 30 (plus empty r and x), Humidifier 14, Dehumidifier 13, Desiccant moisture absorber 5. Misting fan and Floor fan had none.
Their t, ax, tt and see are unchanged.

Electric fan (design & vintage): kept its 4 entries (4 -> 4), because they are named lines, not loose models. Added nl, sel, xg ("Era"), g per entry, and role "origin" on Emerson Northwind (Emerson Electric page: first to sell electric fans in the US, 1892). No whole-space reference exists; sel says so and names the maker pages used. No landmark badges, as no fetched page names best-sellers.

## Brand register
71 -> 105. 34 makers from the removed models were added by name only (no country or year, since no fetched page gave them): AEG, AirGradient, Aqara, Atmotube, Belaco, Beldray, Bionaire, Bresser, Bromic, Cürv, Davis Instruments, Devola, Dr. Infrared, Elpine, Friedrich, Heat Storm, Igenix, Kero-World, Kiasa, Klarstein, Mirrorstone, Momcozy, Nielsen-Kellerman, PurpleAir, Russell Hobbs, Sengoku, Skip Hop, Soleus Air, Supawarm, Swan, Temtop, VonHaus, Warmlite, Zanussi. Existing entries were not changed (Balmuda, Vornado and Emerson facts were already present and agree with the fetched pages).

## Market panels (ms and msum added; all estimates from market-research vendors)
- Air cleaning & monitoring: global air purifiers 2025 (gminsights.com): Honeywell over 4.5 %, Coway 4.0 %, Dyson 3.8 %, top five 17.3 %.
- Air conditioners & coolers: global portable air conditioners (verifiedmarketresearch.com, Q1 2026 report, basis not stated): LG 18.2 %, Haier 15.8 %, Midea 13.9 %, Daikin 11.5 %.
- Fans: global bladeless fans 2025 (dataintelo.com): Dyson 28.5 %, top five 57.3 %.
- Humidity control: portable dehumidifiers (businessresearchinsights.com, 2025 base year, unit shipments): Midea about 15 %, Haier about 13 %, top five about 54 %.

## Not sourced
Portable heating has no panel: no ranking found. No share found for fans overall, humidifiers, or any national champions, so no own/tier/cty fields were added (no entries are branded). Other search results gave conflicting vendor figures and were not used (De'Longhi 8-22 % in different reports).

Fetches: about 9 (logged in rebuild/work/V4_B7/sources.tsv).
