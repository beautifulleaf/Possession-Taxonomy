# V4_E3_GUITAR report (rounds one and two)

Part file rebuild/out/E3_parts/GUITAR.json, 468 KB. Replaces Guitars & basses, Guitar & bass parts, Amps & effects. Validates OK: 46 kinds, 961 entries (575 after round one). Builder in rebuild/work/V4_E3_GUITAR/ (build.py, adds.py, adds2.py); sources in sources.tsv. About 65 fetches in total.

## Entries, before -> after
Solid-body 16 -> 316; semi-hollow 6 -> 32; hollow-body 11 -> 37; steel-string 17 -> 107; archtop acoustic 1 -> 15; electric bass 11 -> 135; classical 3 -> 5; lap steel 2 -> 4; acoustic bass 2 -> 4. Combo amps 8 -> 77; heads 8 -> 74; cabinets 1 -> 12. Pickups 6 -> 20. Pedal kinds +1 to +6 each. Strings: origin entry only (Augustine nylon, 1947).

## References
Wikipedia: Gibson and Fender product lists, Ibanez (read to its end; the tail has no model rows), Epiphone, Rickenbacker, Gretsch, ESP, Jackson, Martin, Taylor, PRS, Guild, Ovation, Schecter, Music Man, Washburn, Takamine, Hofner, Danelectro, Squier, Warwick, Spector (company), Steinberger, Yamaha electric guitar models, Fender amplifier, Marshall, Vox, Mesa Boogie, Orange, Peavey, Ampeg, Boss, Effects unit, Seymour Duncan, DiMarzio, String (music). Also Yamaha Pacifica history, Premier Guitar, vintagemartin.com sizes, three Wikidata queries.

## Coverage
Each `sel` ends "Covers n entries (kept, added)". No kind is marked Complete: the pages are partial and the summariser drops rows, so Washburn, Schecter and Yamaha lists may be short. Gibson (86 rows) and Fender guitar, steel and bass rows are placed in full.

## Country in `g`
Now from fetched pages only: the maker pages above and two noisy Wikidata country queries, used only where rows agreed. About 50 makers (Ernie Ball, Celestion, EMG, Klon, Maestro, Tokai, Line 6, Kemper, Eventide and others) read "Country not stated on a fetched page".

## Loose models
Converted to entries or versions: Fender HM Strat, Mesa Mark VII, Marshall DSL, Boss BF/CS/NS-2/ME-5/HM-2, Fender volume pedal, Marshall ShredMaster. Removed as unsourced: Kramer Baretta, Dean Bel Aire, Gibson US-1, Warwick-style extras not on the page, other makers' acoustic basses, small parts brands, modeller and attenuator products, boutique pedals.

## Not sourced
- Spector_Bass_Guitars, Spector_Guitars and the Yamaha guitars article returned 404; no Wikipedia Martin full model list exists, so Martin comes from its article and the sizes page.
- Rickenbacker, Gretsch, ESP/LTD, Jackson, Epiphone, Fender, Vox and Mesa have only their Wikipedia pages; the makers' own archives were not fetched. Gibson's list has no years.
- No market fields or market summary (instruments decision). Roles only on the Seymour Duncan JB and the Augustine strings.
- Talk boxes, ring modulators and EBow had no kind.
