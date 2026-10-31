# GAP_D2 report (Phones, Tablets & Personal Devices)

Validator: OK (78 kinds, 365 archetypes). About 49 fetches/searches, logged in rebuild/work/GAP_D2/sources.tsv. Only D2.json edited (backups in work/GAP_D2/bak/). No Firecrawl calls; no pages deferred.

## Closed
1. Loose models: none remain (no kind has `m` or `r`; checked).
2. Coverage lines: all 54 kinds with entries now end "No complete list exists; follows <Wikipedia pages and maker/retail pages cited on the entries>". No kind has a single whole-space reference, so none says "Complete" or "Covers". Nokia note corrected: List of Nokia products now read to character 350,000 of 351,327 (rest is footer).
3. Partial coverage: Pixel confirmed complete (Wikipedia, phone table); Nokia list finished (added N-Gage, Nokia 225/230/235/301/515); Kobo (25 models), Razr (to Razr 70/Fold), Fitbit (to Air), Forerunner (all 50), fenix, Galaxy Watch/Gear, Galaxy Tab S and A, Surface (RT, Pro, Go), Fire (2014-2024 generations), BlackBerry (Pearl, Storm, Z10, Classic, Q5, Z30, Leap, Priv, DTEK, Motion), LG G Watch, Asus ZenWatch added from fetched pages.
4. Version years filled where a fetched page gave them: OnePlus (36 versions), Xiaomi Mi/Xiaomi/MIX, Poco, Garmin eTrex/GPSMAP/Oregon/Montana, inReach, Thuraya, AirTag, TomTom, Yaesu FT-817/857/991A. Weak entries (OnePlus, Xiaomi, Poco) now cite Wikipedia instead of a Kimovil comparison.
5. Market facts: new `ms` for Tablets & e-readers (IDC Q3 2025 shipments via FoneArena: Apple 13.2 m, Samsung 6.9 m, Lenovo 3.7 m, Huawei 3.4 m, Xiaomi 2.5 m of 38 m) and Wearables (IDC Q2 2026 shares: Apple 15.5 %, Xiaomi 11.7 %, Huawei 10.9 %, Samsung 6.8 %, Imagine Marketing 4.9 %).
6. Sections: every entry already has `g` (maker); nothing missing.

## Remains
- No wikidata SPARQL was attempted; Wikipedia pages were used.
- `own`, `tier`, `cty`, `own_y`: no ownership pages fetched; searched only for market and release facts.
- Years still empty: Mi Band 3-10 (page gives none), Tile, Rino, Foretrex, Montana 710i, Magellan, SPOT, ham handhelds added without year (Baofeng, Quansheng, Alinco, Wouxun), Icom IC-7700/7000/7100/9100. Searched: "Samsung Galaxy Tab series", Mi Band, Tile, Garmin eTrex (found via gpstraining.co.uk). Wikipedia pages for Icom IC-7300, Garmin eTrex, Xiaomi Mi, BlackBerry (smartphone), SPOT returned 404.
- Pages read only to their first 100,000 characters: Fitbit, Fitbit products, Surface, Wear OS (tail also read, no years), OnePlus (Redmi/Nord later sections), Poco, AirTag, TomTom, Xiaomi products (to 200,000 of 285,183; Redmi Note not reached).
- Firecrawl-deferred list unchanged.
- Smart ring (Amazfit, Circular, RingConn), kids' watches, rugged phones, e-paper tablets (Supernote, MobiScribe) still rest on retail pages without years.
- Tablet/wearable full-year 2025 shares not found on a fetched page (IDC page shows latest quarter only).

## Round 2
Validator OK (78 kinds, 366 archetypes). About 42 further fetches.
- Owners: Wikidata SPARQL (chunk 1 of 3) came back ambiguous (Apple, Amazon), truncated and with almost no P749 parents, so I used MediaWiki API intro extracts for 8 batches of makers instead. Set `cty` on 273 entries, `own` (and `own_y` where stated) for Apple, Casio, Asus, Meta, Microsoft, Nokia, OnePlus (Oppo), Poco (Xiaomi), iQOO (Vivo), Kenwood (JVCKenwood), iriver (Dreamus), TAG Heuer (LVMH, 1999), T-Mobile (Deutsche Telekom), Timex (Timex Group B.V., 2008), Western Electric (AT&T), Sony Ericsson (Sony, 2012), SPOT (Globalstar). `tier`: "Global group" for makers in the fetched IDC top-five tables or owned by one; "Independent" for makers a fetched page describes as a standalone company; others left empty. Not done: no owner or country for makers whose pages were missing (4O3A, Ameritron, AnyTone, Quansheng, Wouxun, Xiegu, Retevis, RingConn and others). D2_brands.json unchanged.
- Tails: Fitbit, Fitbit products (to 200,000 of 231,636), Surface (to 200,000), OnePlus (to 200,000), Poco, AirTag, TomTom, Xiaomi products (read from 200,000 to the end of the 285,183). Added Surface Pro/Go generations with years, Xiaomi 13 to 17, Redmi Note/K and Mix Flip names, Poco and OnePlus names, OnePlus Pad. The pages give names without dates, so these versions have no year.
- Years: Mi Band 3 to Smart Band 8 (2018-2023), Rino 750/755t (2016), Icom IC-718, 7000, 7200, 7600, 7700, 7800, 9100, Tile (2019), SPOT X (2018), Baofeng UV-5R (2012).
- Full-year shares: IDC tablets 2025 total 151.9 million (+5 %) and Q4 vendor figures; Counterpoint smartphones 2025 total 1,255 million (+3 %). Vendor shares for the full year were not on any readable page (IDC blog, Counterpoint page); AppleInsider and SammyFans returned 403 (logged in firecrawl_deferred.md). No full-year wearable table found.
- Still blank: IC-7100/7300/7610/705, Foretrex, Montana 710i, SPOT Gen3, Quansheng, Wouxun, Alinco years (searched: release-year queries for each; no fetched page).
