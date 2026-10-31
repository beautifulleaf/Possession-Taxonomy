# V4_E3_GUITAR report

Part file: rebuild/out/E3_parts/GUITAR.json (352 KB; replaces Guitars & basses, Guitar & bass parts, Amps & effects). Validates OK: 46 kinds, 575 entries. Builder: rebuild/work/V4_E3_GUITAR/build.py, adds.py.

## Entries before -> after (kinds with entries)
- Solid-body 16 -> 153; Semi-hollow 6 -> 26; Hollow-body 11 -> 35; Steel-string acoustic 17 -> 51; Classical 3 -> 5; Archtop acoustic 1 -> 5; Lap steel 2 -> 4; Pedal steel 4 -> 5; Electric bass 11 -> 64; Acoustic bass 2 -> 4.
- Pickups 6 -> 20; Strings 3 + 1 -> 1 (origin only); Bridge, tuners, cabinets and speakers unchanged.
- Combo amps 8 -> 51; Amp heads 8 -> 34; Cabinets 1 -> 3.
- Pedals: Tremolo/vibe 2 -> 7, Wah 3 -> 9, Delay 9 -> 12, EQ 1 -> 4, Multi-effects 1 -> 4, others +1 to +2 each.

## References (56 fetches counting Wikidata)
Wikipedia: Gibson and Fender product lists (read whole), Ibanez (first 100,000 of 130,308 characters), Epiphone, Rickenbacker, Gretsch, ESP, Jackson, C. F. Martin, Fender amplifier, Marshall, Vox, Mesa Boogie, Boss Corporation, Effects unit (both windows), Seymour Duncan, DiMarzio, String (music); Yamaha Pacifica history and Premier Guitar SG2000; one Wikidata SPARQL query (109 guitar rows, many unlabelled or without maker detail). See sources.tsv.

## Coverage
Each kind's `sel` ends "Covers n entries (kept, added)"; I did not claim "Complete" because the Wikipedia pages are partial: they do not list every model of each maker. Gibson's list is placed in full (86 rows; duplicates merged into existing entries or versions). Fender guitar, steel and bass rows are placed in full. Not placed: Gibson mandolin, banjo and amplifier rows and the P-90 and PAF rows (pickups are covered elsewhere), Fender amplifier navigation names not in a kind, Epiphone Gibson-equivalent models.

## Loose models (`m`)
All removed or converted. Converted to entries or versions: Fender HM Strat, Mesa Mark VII, Marshall DSL, Boss BF-1/BF-2/BF-3, CS-1/CS-3, NS-2, ME-5, HM-2, Fender volume pedal, Marshall ShredMaster. Removed as unsourced (no fetched page): Kramer Baretta, Dean Bel Aire, Gibson US-1, Fender Contemporary Strat, Gibson double-neck lap steel, Warwick Streamer/Corvette/Star, acoustic basses of Taylor, Martin B65E, Ibanez, Harptone, Lace Sensor, EMG SA, Hipshot, Graph Tech, Mojotone, CTS and Switchcraft parts, modeller and attenuator products, Line 6/Roland/Yamaha amps, and boutique pedals (JHS, Wampler, Revv and others). Their kinds that now hold no entries are parts or commodity kinds.

## Not sourced
- No Yamaha, Taylor, PRS, Guild or Ovation catalogue: Wikipedia's Yamaha guitars page returned 404; Yamaha shows only Pacifica, SG and Wikidata rows. Martin, Fender and Gibson signature and era models appear as versions only where the earlier pass had them.
- Descriptions for many rows are minimal because the source lists give names, not facts.
- No `own`, `tier`, `cty` market fields and no department market summary, as the owner decision for instruments says.
- Maker countries in `g` are general knowledge, not fetched; to verify.
- Roles: only the Seymour Duncan JB (landmark, best-selling per its page) and Augustine nylon strings (origin).
- Talk boxes, ring modulators, EBow and Korg Kaoss Pad (Effects unit page) had no kind and were left out.
- Amp makers beyond Fender, Marshall, Vox, Mesa (Orange, Peavey, Ampeg and others) have only their earlier entries.
- Brand register not extended.

## Round two (coordinator request)
Part file now 468 KB, 46 kinds, 961 entries (from 575). About 38 more fetches. Validates OK.
- Ibanez read from offset 100000 to its end (page ends at 130,308): no model rows there, only navigation; nothing added.
- Pages read and placed: Taylor, PRS, Guild, Ovation, Schecter, Music Man, Washburn, Takamine, Hofner, Danelectro, Squier, Warwick (guitar manufacturer), Spector (company), Steinberger, Yamaha electric guitar models, Pacifica history, Martin body sizes (vintagemartin.com), Orange, Peavey, Ampeg. Marshall history and Fender company pages re-read for dates and country; no new Marshall lines beyond round one.
- Entries now: solid-body 316, semi-hollow 32, hollow-body 37, steel-string 107, archtop acoustic 15, electric bass 135, combo amps 77, heads 74, cabinets 12.
- Country in `g`: now from fetched pages only (maker pages above, plus two Wikidata country queries of 32 and 95 rows, noisy). Makers with no fetched country read "Country not stated on a fetched page" (about 50 makers, e.g. Ernie Ball, Celestion, EMG, Klon, Maestro, Tokai, Line 6, Kemper, Neural DSP, DOD, Eventide). Wikidata country rows were used only where they agreed; ambiguous ones (Kemper, Selmer, Maestro, Eventide, Line 6, Strymon, Steinberger) were not used.
- Not reachable: Wikipedia pages Spector_Bass_Guitars and Spector_Guitars (404; Spector (company) used), Yamaha guitars article (404; Yamaha electric guitar models used), no Wikipedia Martin full model list exists (404 or absent; Martin lines come from the Martin article and vintagemartin.com sizes). Rickenbacker, Gretsch, ESP/LTD, Jackson, Epiphone, Fender, Vox and Mesa have only the round-one pages: their own model archives were not fetched, so their lists are not complete. Taylor, PRS and Guild rows are series and models the Wikipedia pages name; the pages date few of them.
- Several pages were summarised, which drops rows: the Washburn, Schecter and Yamaha lists may be partial.
- Fender amplifier list: all dated rows plus navigation names placed; Princeton Reverb added.
