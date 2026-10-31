# V4_G1_BIKES report

Part: rebuild/out/G1_parts/BIKES.json (replaces Bicycles; Prams & strollers). Validates OK: 46 kinds, 277 entries, about 259 KB. About 65 fetches, logged in rebuild/work/V4_G1_BIKES/sources.tsv; built by build.py there.

## Entries before -> after
- Bicycles about 190 -> 258: Road bike 11 -> 34; Electric bike 2 -> 20 (five Riese & Müller lines added); Folding bike 5 -> 14; Cargo bike 4 -> 7; Groupset 6 -> 37 (Shimano 18 series including Tourney, Altus, Acera, Alivio, CUES; SRAM 9; Campagnolo 9; every generation named is a version); Trail mountain bike 5 -> 10.
- Prams & strollers 8 -> 19 (Kent's shell carriage 1733 as origin, Balmoral, Stokke Xplory, Trailz, Crusi, Scoot, Richardson stroller).
- Every entry has `g` (maker country, then maker); every kind with entries has `nl`, `sel` with a coverage line, `xg`; 8 role badges.

## References
Wikipedia pages of 20 makers (Trek, Specialized, Cannondale, Pinarello, Cervélo, Colnago, Bianchi, Santa Cruz, Canyon, Giant, Merida, Raleigh, Schwinn, Brompton, Dahon, Tern, Pashley, Surly, Gazelle, Riese & Müller), plus Strida, Moulton, Shimano, SRAM, Campagnolo, List of Shimano groupsets, Deore XT, Accell, Pon, Electric bicycle, Baby transport, Maclaren, Bugaboo, UPPAbaby, Silver Cross, Stokke, Goodbaby. Trade pages: MHW Bike (Tourney, read through Firecrawl after a 403), Cycling Industry News (Alivio, Acera, Altus, 2018), BikeRadar (CUES, 2022), tech.eu (Cowboy), two strollberry pages. The long Wikipedia pages were read to their ends; the tails held only reference lists and added a few versions (Synapse SmartSense, Dogma XC, Cervélo P2C and S5 Grand Tour Edition). No Wikidata: it does not model bicycle lines.

## Coverage
Groupset is complete for the lines on those pages. Other kinds say no total exists, so only lines on the pages read are covered.

## Market facts (with years)
Shimano about 85 % of components by value (2016 report), revenue US$2.872 bn (2024); SRAM about 15 % (2010 era); Giant US$1.9 bn (2017); Merida NT$29.39 bn (2021); Pon bicycles EUR 2.1 bn (2024); Accell EUR 1.294 bn (2023), insolvent August 2026; Riese & Müller EUR 350 m (2022); Cowboy $120 m raised (2022); Canyon EUR 738 m (2025); Brompton GBP 42 m (2019); EU e-bike sales over 5 m (2021). Prams: Maclaren 600,000 a year (1976), Fosun 87.23 % of Silver Cross (2017), Goodbaby bought Cybex and Evenflo (2014), Newell baby brands (2017), Stokke bought Babyzen (2021). Own, tier, cty, own_y set for 28 makers; 10 new brands; 28 brand_updates.

## Former models
All `m` and `r` removed. Attested ones became entries or versions; the rest were dropped as SKU-level or unattested (Domane, Aethos, Salsa, Bike Friday, Santana, Co-Motion, Burley trailers, RockShox and Fox sizes, Cybex, Chicco, Graco, Nuna, Evenflo, Bugaboo Butterfly and others).

## Not sourced
- Stroller market share: none. Tried: Global Market Insights (410), Goodbaby annual report and PDF (too large), Newell FY2017 10-K (no share stated), Dorel searches, Business Wire report (403), Bamboo Works Goodbaby (403). Search excerpts quote a 10-15 % top-eight share (2023) and a "one in three" Goodbaby claim; neither is on a fetched page, so neither is used.
- Cowboy has no Wikipedia page in search; no founding year or unit count fetched.
- Ownership of Maclaren, Tern, Strida, Moulton, Riese & Müller; Bugaboo Fox, Venge, Domane attestation.
