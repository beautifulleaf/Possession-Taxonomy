# GAP_D1 report (Computers & Components)

Files changed: rebuild/out/D1.json and D1_brands.json (backups in rebuild/work/GAP_D1/bak/; script apply.py; sources in sources.tsv). validate.py --v3: OK, 110 kinds, 458 entries (was 385). About 45 fetches and searches; no Firecrawl.

## 1. Loose models
None remained (kinds with `m`: 0).

## 2. Coverage lines
Every kind with entries now ends its `sel` with a Complete, Covers or "No complete list exists" line (46 kinds). Kinds with no whole-space list (laptops, desktops, vintage kinds, cases, coolers, keyboards, switches, printers, security keys, hardware wallets and others) say so and name the overviews followed. Laptop: Wikipedia's List of laptops does not exist (404); List of laptop brands and manufacturers lists brands, not models.

## 3. Partial coverage closed
- Graphics card: now "Complete: 27 of 27" generations. Added GTX 1660 Ti and Super (2019) and GeForce 9400 and 9500 GT (2008) as versions from their series articles.
- Processor: "Covers 63 of about 74" rows of the Intel and AMD microarchitecture lists. Added Westmere, Nova Lake, four Atom cores (Saltwell, Airmont, Goldmont Plus, Darkmont). Years filled from article pages: Bobcat 2011, Jaguar 2013, Puma 2014, Zen 6 2026, Bulldozer 2011, K6-2 1998, Phenom II 2008. Left out and named in `sel`: 80186, Palm Cove, Family 11h, Llano, K9 (never released), and unreleased designs from Cougar Cove on. Piledriver, Steamroller, Excavator, K6-III and Athlon II have no year on any fetched page.
- Home computer: re-read the whole List of home computers; "Complete: 146 of 146" main-table machines (the row "Various models" names none). Added BBC Master and nine school computers (makers left blank). Cardboard demonstrators out of scope.
- Trainer & single-board kit: added 23 hobby and kit rows from that list and five early boards (Intel SIM4-01, SIM8-01, MYCRO-1, SDK-80, Motorola MEK6800D1); sections added.
- Single-board computer: 17 more families from the Single-board computer article (27 of 27 named, Arduino and Nvidia Drive handled elsewhere); sections by maker.
- Microcontroller board: 27 of 27 official Arduino boards on Wikipedia's Arduino list (read to 200,000 of 210,594 characters; clone section out of scope), plus STM32 Nucleo; sections by maker.

## 4. Other gaps
- Market: added AMD desktop 34.9, notebook 28.9, server 34.5 % (Mercury, Q2 2026); JPR AIB 12.5 million units; US PC shipments by vendor (Omdia, Q2 2026); Ethernet switch and router shares (IDC, Q2 2026); enterprise SSD revenue top five (TrendForce, Q2 2026).
- Brands: country and founding year filled for 12 brands from Wikidata where the result was plausible (the rest of the roughly 100 blank brands, and values that looked wrong such as Philips, Sony, Glorious, were left blank).

## Remains (searched)
- Intel segment shares, GPU vendor shares from JPR primary text (chart only): searched "Jon Peddie Research add-in board GPU market share Q2 2026", "Mercury Research x86 CPU market share Q2 2026".
- Printer vendor shares: IDC Q2 2026 page has totals only; searched "IDC worldwide hardcopy peripherals ... share".
- Europe and other regional PC shares, consumer SSD vendor shares, monitor and keyboard markets: no fetched source found.
- Cables, hubs and power: no kind has entries; no listing page found ("list of computer connectors" search).
- Years for hobby kits, school computers and most SBC families: not on fetched pages.
