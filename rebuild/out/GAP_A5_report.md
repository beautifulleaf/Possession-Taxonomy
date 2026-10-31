# GAP_A5 report: Clocks & Watches

Result: validator OK (87 kinds, 903 entries, up from 863 and 85 kinds). Backups in rebuild/work/GAP_A5/bak/; sources in rebuild/work/GAP_A5/sources.tsv. About 55 fetches and searches. The gap list's counts (33 loose-model kinds, 50 without coverage) were stale: they described the pre-merge file.

## Closed
1. **Loose models:** none remain (0 `m` in A5.json). The `r` ranges left are makers' ranges spanning many entries (Seiko Prospex, TAG Heuer Aquaracer and similar). No removals this pass.
2. **Coverage lines:** all 28 wristwatch kinds and the Design clock, Watch movement and Railroad kinds now end with a recognised coverage sentence. Wristwatch kinds say "No complete list exists; follows Wikipedia's Category:Watch models (38 pages and four subcategories, read in full), maker pages, Wikidata Q178794 and Watchbase for nine makers".
3. **Partial coverage:** Wikidata Q178794 has 246 items, mostly museum objects; every in-scope wristwatch was already an entry except Amfibia (Vostok, 1967) and Movado Ermeto (new kind "Purse watch"). Category:Watch models is now complete. Added 29 entries from the Wikipedia pages of Seiko, Citizen, Tissot, Hamilton, Longines and Vacheron Constantin (Parawater, Goldfeather, Twin Quartz, Credor Fugaku, Kodo, Tour de l'Île, Kallista, Solaria Ultra, Hybris Mechanica and others). Seth Thomas railroad grades: 8 entries from Rails West, so Railroad-grade is now 189.
4. **Owners:** set from fetched pages for Chopard (Scheufele family, 1963), Girard-Perregaux (Sowind Group), Doxa (Jenny family, 1997), Glycine (Invicta, 2016), Universal Genève (Breitling SA, 2023), Waltham (2011), Greubel Forsey, Christopher Ward (2014), Vostok, Baltic, Philippe Dufour, Sinclair Radionics, Lorier (Worn & Wound, 2026), Chanel (Wertheimer family). Sunrise alarm clock now has its origin entry (1890 patent, Wikipedia Dawn simulation).
5. **Sections:** every entry in kinds with `xg` has `g`; new entries carry it.

## Remains
- Owner not stated after two attempts: Nomos (searched "Nomos Glashütte owner Roland Schwertner"; Wikipedia silent), Tutima, Urwerk (worldtempus page and urwerk.com silent), Sellita (Wikipedia silent; search found only one blog for García 2003), Poljot (Volmax and Pugachev claims conflict), Gallet.
- Watchbase family lists for other makers: blocked; logged in firecrawl_deferred.md. Seiko, Tudor, Zenith, Panerai and others rest on Wikipedia.
- Omega 8500, Rolex 3235, Sellita SW500 and Seiko 6R calibre pages (403/404) not listed. Star Caliber 2000 skipped (maker not stated on the page).
- Own-year gaps remain for Omega, Tissot, Hamilton, Panerai, Cartier and Swatch brands.
- Searched "list of complicated watches Wikipedia": none exists; the Complication (horology) list was used.
