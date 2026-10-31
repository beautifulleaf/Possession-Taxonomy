# GAP_E3 report (Musical Instruments & Music Gear)

Validates OK (0 errors, 260 kinds). About 52 fetches; log in rebuild/work/GAP_E3/sources.tsv; backups in rebuild/work/GAP_E3/bak/; scripts adds.py and cov.py in rebuild/work/GAP_E3/.

## Closed
1. Loose models: no kind holds `m` any more (checked: 0). The 61 kinds with maker ranges `r` were kept; no fetched page names their members.
2. Coverage line: all 181 kinds with entries now end "No complete list exists; follows <pages> (n entries)". No kind has a whole-space reference, so no "Complete" or "Covers n of about m" claim is made. Old "Covers n entries" sentences were replaced with current counts.
3. Stradivari guitars: one entry "Stradivari guitar" in Classical guitar, with versions Hill 1688, Sabionari 1679, Rawlins 1700, Vuillaume 1711. Holders come from the Stradivarius list (window 100000; windows 150000 and 200000 hold references only). Country Italy from the Antonio Stradivari page ("Italian luthier", Cremona). The list summary gave Hill's former name garbled, so it is omitted.
4. Maker archives, 108 entries added (all with g):
 - Rickenbacker 45 (products list and the maker's legacy page: 200, 300, 400, 600, 700, 800/900, Rose Morris, 2000, 3000, 4000 series).
 - Gretsch 5 (6128 and 6136 pages: Silver Jet, Round Up, Thunder Jet bass, Black Falcon, Silver Falcon); the 6120 variants were already present.
 - Epiphone about 40 (Epiphone article: archtops, FT flat-tops, nylon, basses, amps, Gibson-pattern solids).
 - Fender 5 (Esquire 1950, Hot Rod DeVille 1996, Bandmaster Reverb, Vibrosonic Reverb; Marauder already present). The Fender categories show the guitar range was otherwise complete.
 - Vox 6 (AC30 timeline: AC4 1962, Twin, Super Twin, T60 Bass, Super Transonic, AC30 Bass).
5. Country in `g`, from fetched pages: Celestion (UK), Eventide, Line 6, Ernie Ball, DOD, DigiTech, Strymon, Morley (US), Tokai, Shin-ei (Japan), Lowden (UK).
6. Sections: every kind with `xg` has `g` on every entry; no kind over 12 entries lacks `xg`.

## Remains (searched)
- Mesa/Boogie: maker site redirects to gibson.com (no model text); americanmusical 403; only a retailer list found, not used. Searches: "Mesa/Boogie amplifier models list Mark I ...". Deferred in firecrawl_deferred.md.
- Jackson, ESP/LTD: Wikipedia categories 404, official sites give labels or collaborations only. Searches: "Jackson Guitars Soloist Dinky ... history models". Deferred.
- Gretsch: tonewolf guide gave eras, no rows. Vox: Wikipedia category 404; AC10 absent from timeline.
- Epiphone: Granada, Professional, Espana, Barcelona, Bard, Serenader, Folkster, Cortez, Caballero, Caiola, Howard Roberts, Monticello not placed because the page gives no type.
- Countries still empty: Bigsby, Maestro (pages give none) and about 36 minor makers; 282 folk-instrument entries read "Region not stated".
- 23 kinds still have no entries (Clavichord, Pipe organ, Conga, Bongos, Xylophone, Guzheng, Sarangi, Ney and others).
