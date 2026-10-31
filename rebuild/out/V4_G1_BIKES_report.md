# V4_G1_BIKES report

Part file: rebuild/out/G1_parts/BIKES.json (replaces Bicycles; Prams & strollers). Validates OK: 46 kinds, 266 entries, about 249 KB. About 50 fetches; all logged in rebuild/work/V4_G1_BIKES/sources.tsv. Built by rebuild/work/V4_G1_BIKES/build.py.

## Entries before -> after
- Bicycles: about 190 -> 247 named entries. Road bike 11 -> 34; Electric bike 2 -> 15; Folding bike 5 -> 14; Cargo bike 4 -> 7; Groupset 6 -> 32 (Shimano 13 series, SRAM 9, Campagnolo 9, each with every generation the pages name as versions); Trail mountain bike 5 -> 10; Suspension fork 7 -> 8. Other kinds gained 1-4 each.
- Prams & strollers: 8 -> 19 (Pram 1 -> 3, Stroller 6 -> 11). Added Kent's shell carriage (1733, origin), Silver Cross Balmoral, Richardson reversible stroller, Stokke Xplory, Trailz, Crusi, Scoot. Maclaren, YOYO, Frog and UPPAbaby entries corrected from the fetched pages.
- Every entry has `g` (maker country, then maker). Every kind with entries has `nl`, `sel` with a coverage line, `xg`. Roles: 8 in 266.

## References
Wikipedia pages of Trek, Specialized, Cannondale (first 100,000 characters of 149,601), Pinarello (first 100,000 of 140,035), Cervélo (first 100,000 of 151,232), Colnago, Bianchi, Santa Cruz, Canyon, Giant, Merida, Raleigh, Schwinn, Brompton, Dahon, Tern, Pashley, Surly, Gazelle, Strida, Moulton; List of Shimano groupsets, Shimano Deore XT, SRAM, Campagnolo, Shimano; Accell, Pon; Electric bicycle (first 100,000 of 193,372); Baby transport, Owen Finlay Maclaren, Bugaboo, UPPAbaby, Silver Cross (company), Stokke AS; two strollberry retailer pages. No Wikidata query: Wikidata does not model bicycle model lines, so the maker pages were used.

## Coverage
Groupset: complete for the lines named on the Shimano, SRAM and Campagnolo pages; the Shimano list was read through a summariser (Tourney, Altus, Acera not named). Other kinds: the coverage line says no reference gives a total, so only the lines on the pages read are covered. The three long pages were read to 100,000 characters only (tails not read).

## Market facts (ms, with years)
Shimano about 85 % of components by value (2016 report) and revenue US$2.872 bn (2024); SRAM about 15 % (2010 era); Giant US$1.9 bn (2017), e-bikes 30 % of sales (2021); Merida NT$29.39 bn (2021); Pon bicycle revenue EUR 2.1 bn (2024); Accell EUR 1.294 bn (2023), insolvency August 2026; Specialized about US$500 m (2011); Trek US$1.0 bn (undated); Canyon EUR 738 m (2025); Brompton GBP 42 m (2019); Gazelle 300,000 a year; EU e-bike sales over 5 m (2021); Netherlands e-bike share 57 % (2022); Japan 350,000 (2023). Prams: Maclaren 600,000 a year (1976), Fosun 87.23 % of Silver Cross (2017), Bugaboo and UPPAbaby country reach, Stokke bought Babyzen (2021). Own, tier, cty and own_y are set for 26 makers; 8 new brands (Pon Holdings, Accell Group, Giant Manufacturing, Merida, Quality Bicycle Products, Fosun International, Bain Capital, Cycleurope) and 26 brand_updates are in the part.

## Former models (`m`) and ranges (`r`)
All `m` and `r` were removed. Attested ones became entries or versions: Soloist, 5500, Tallboy, Big Dummy, Boardwalk, Curl, EEZZ, K-Feather, Verge/Link/eLink/BYB, GSD/HSD/NBD/Quick Haul, Force, Apex, Rival, Chorus, Potenza, Veloce, Claris, Treadwell Neo, Compact Neo, Chamonix. The rest were dropped as SKU-level or unattested on any fetched page: Domane, Aethos, Roadeo, Vincitore, track-bike Cinelli and Look models, gravel models of other makers, Salsa, Bike Friday, Santana, Co-Motion, Top End, Burley trailers, RockShox and Fox fork sizes, DT Swiss, Hutchinson, Tufo, Brooks saddles, all Cybex, Chicco, Graco, Nuna, Evenflo, Mockingbird, Bugaboo Butterfly/Dragonfly/Donkey, Silver Cross Reef/Wave, Petique.

## Not sourced
- Stroller market shares: the Global Market Insights page returned HTTP 410; no figure is given.
- Riese & Müller and Cowboy Wikipedia pages returned 404; their existing entries keep earlier sources.
- Stokke's own history and blog pages failed (parse error); Xplory rests on a retailer page.
- Bugaboo Fox, Specialized Venge/Turbo, Trek Domane, Maclaren's Volo/Triumph lines had no fetched attestation.
- Tern, Strida and Moulton ownership, and Maclaren ownership, are not stated on fetched pages.
- Pinarello, Cervélo and Cannondale pages: the unread tails may hold more lines.
