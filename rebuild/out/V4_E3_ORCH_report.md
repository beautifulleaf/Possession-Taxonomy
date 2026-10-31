# V4_E3_ORCH report

Part file: rebuild/out/E3_parts/ORCH.json (217 KB; validates OK, 124 kinds, 419 entries). Replaces Orchestral & band instruments, Folk & world instruments, Cases, stands & accessories.

## Orchestral & band instruments
- Loose models: 67 became entries (maker model lines, e.g. Haynes, Powell, Muramatsu, Yamaha, Selmer, Buffet, Heckel); 6 retailer own-label models (Thomann, Startone) were removed as out of scope.
- Violin: Stradivari pattern became "Antonio Stradivari" with 116 named violins as versions; Guarneri del Gesù (4 named violins), Amati (6 named instruments), plus new entries Jacob Stainer and Jean-Baptiste Vuillaume (Il Cannone and Messiah copies). Viola: 10 Stradivari violas; Cello: 29 Stradivari cellos. Vuillaume octobass added under Double bass.
- Reference: Wikipedia List of Stradivarius instruments plus the maker pages. Coverage is partial: the page is about 216,000 characters, WebFetch's summariser drops rows, and Firecrawl JSON extraction returned only part of the 1703-1731 golden-period rows (Messiah, Lady Blunt, Titian and others were recovered by a targeted pass). The Strad guitars, harp and bow rows were returned but guitars/harp/bow were not placed (no E3 kind in this part); the three mandolins went under Mandolin.
- Roles: Stradivari and Amati origin, Selmer Mark VI landmark.

## Folk & world instruments
- 6 shelves kept; 12 new kinds added from Wikipedia's Hornbostel-Sachs lists (32 lutes, 31 zithers, 421 flutes, aerophones, Reed aerophone, chordophones hub): European and Asian lutes, African lutes, lyres, tube/raft/board zithers, musical bows, world harps, spike fiddles, European bowed lutes, free-reed pipes, end-blown/transverse/fipple flutes, double- and single-reed folk pipes, natural horns, stringed novelties. About 197 entries added; all entries sectioned by world region.
- Region labels for list rows are mine (the lists give none); "Region not stated" where unsure. Percussion families belong to Drums & percussion and were not added.
- 35 loose maker models removed as non-defining (e.g. Overton whistles, Dunlop-type retail lines, Kyser-type); historic defining makers (Wheatstone, Lachenal, Soprani, Hohner, Seydel, Donati, Symphonion, Reuge) kept as entries.
- Not fetched: H-S pages 422 and 423 do not exist (404); plucked-instruments list URL did not exist (404, its extracted rows discarded). The 32, 31 and 421 lists were read by extraction only, so coverage lines say "Covers n", not "Complete".

## Cases, stands & accessories
- Commodity; all 74 loose models and 6 entries (DW 5000, Iron Cobra, Eliminator, Tortex, Jazz III, 351 shape) removed: none is a first of its kind or a design-collection landmark on a fetched page. Kinds keep attributes only.

## Market fields
None (E3 has no market panel). New register entry: Jacob Stainer (Austria).

## Not done
Exact totals for the lists; Strad guitars/harp/bow; icon-rule entries for accessories (no fetched design-collection page).
