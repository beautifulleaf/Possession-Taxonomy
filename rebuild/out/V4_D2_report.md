# V4_D2 report: named-entry pass, D2 Phones, Tablets & Personal Devices

Result: python3 validate.py --v3 out/D2.json is OK (78 kinds, 342 entries). Files edited: D2.json, D2_brands.json, D2_renames.json (backups in work/V4_D2/bak/). D2_moves.json unchanged.

## Entries before -> after (by department)
- Phones: 69 -> 94. Smartphone lines, folding phones, feature phones, collector handsets and vintage telephones.
- Tablets & e-readers: 20 -> 43. Rebuilt iPad (iPad, mini, Air, Pro as four entries), Galaxy Tab (S, A, Active, early lines) and Kindle (Kindle, DX, Paperwhite, Voyage, Oasis, Colorsoft) from the fetched tables.
- Wearables, PDAs, Navigation, Radio: former models (`m`) and ranges (`r`) became entries or versions of one. Totals now 54, 24, 36 and 91.
- Power & charging and Cases & accessories: commodity, so 0 entries; all models and ranges removed.
- Corded, cordless and IP phones, and four station-equipment kinds: commodity, no entries.
- Every kind with entries now has `nl`, `sel` and `xg` (maker); each entry has `g` (maker), sorted by the maker's earliest year, then year, then name.
- "Android E Ink tablet" merged into "E-paper writing tablet" (D2_renames.json).

## References fetched (rebuild/work/V4_D2/sources.tsv)
Wikipedia: List of iPhone models, Samsung Galaxy S series, IPad, Samsung Galaxy Tab series, Amazon Kindle, Apple Watch, List of Nokia products, Mobile phone. Market pages: GSMArena (IDC) and Counterpoint.

## Market facts (Phones department, `ms`)
- Global smartphones 2025 (IDC): Apple 19.7 %, Samsung 19.1 %, Xiaomi 13.1 %, vivo 8.2 %, Oppo 8.1 %.
- US smartphones (Counterpoint): Q4 2025 and Q2 2026 for Apple (67 %, 54 %), Samsung (17 %, 30 %), Motorola (10 %, 11 %), Google (3 %, 3 %).
- Global mobile phones 2022 top five (Wikipedia citing Counterpoint): Samsung 21 %, Apple 16 %, Xiaomi 13 %, Oppo 10 %, Vivo 9 %.

## Not done or not sourced
- Several fetch summaries were partial (page text over 100,000 characters; the Nokia, Kindle, iPad and Apple Watch pages were read only to character 100,000). Wikipedia's Google Pixel list returned 404, so Pixel keeps its earlier versions. Pixel, Nexus, Surface, Fire and Wear OS lines were not re-checked.
- Entries made from former models (OnePlus, Xiaomi, Garmin eTrex and others) keep the kind's earlier cited page as `s`; I did not fetch those pages in this pass. Their versions have no years.
- The Kobo, Fitbit, Galaxy Watch, BlackBerry, Motorola RAZR and ham-radio maker lists were not re-fetched; their entries and versions are as before.
- No `role` badges were set, as no fetched page named a best-seller or first of kind.
- `own`, `tier`, `cty` and `own_y` were not added; no fetched ownership pages. Wearable and tablet market shares were not found.
- 46 makers added to D2_brands.json by name only (country and year blank, segment "Specialist" as a placeholder).
- Removed models are listed in work/V4_D2/removed.json (62 items: commodity models and ranges, plus models already present as versions).
