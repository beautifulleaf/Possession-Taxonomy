# STR_A5 report: Clocks & Watches

Before: 6 departments, 17 shelves, 71 kinds, 261 archetypes. After: 6 departments, 19 shelves, 78 kinds, 242 archetypes. Validates OK (--v3).

**Structure.** Category `ax` and 6-step `key` added (parts first, then wrist, pocket, timers, collectible, everyday). Every department and shelf has `t` and `ax`. Wristwatches now split by what sets the watch apart: Tool & sports, Style & dress, Electronic, Complication & precision. Pocket watches by era, grade and special form. Collectible clocks by placement (floor and wall, table and mantel) plus Precision and Electric & design shelves; the old Regional & period shelf was dissolved. Everyday clocks: bedside, room. Timers: interval timers, sundials. Straps chain moved to the strap shelf.

**Kinds moved.** Integrated-bracelet sports watch to Style & dress; Chronometer watch and Jumping-hours watch to Complication & precision; Watch chain to Straps; Wadokei, American shelf clock to Table & mantel; Wall regulator to Precision.

**Renamed.** Split-flap clock to Flip clock (Plato clock archetype added).

**Added kinds (reference):** Skeleton watch, Quartz watch, Solar-powered watch, Radio-controlled watch (Wikipedia Watch, Skeleton watch); Trench watch, Nuremberg egg (Wikipedia Pocket watch); Cartel clock (Wikipedia Cartel clock). Coverage references: Wikipedia Watch, Clock, Pocket watch, Timer, Flip clock.

**Archetype changes.** Eco-Drive moved to Solar-powered watch, Wave Ceptor to Radio-controlled watch, Terry thirty-hour shelf clock to American shelf clock, pendule cartel to Cartel clock. Duplicate Vienna regulator merged. Maker ranges moved to `r`: Telechron, Ulysse Nardin marine chronometers, Daniels co-axial. Generic archetypes demoted to types in `tt`: English longcase, English lantern clock, English bracket clock, French carriage clock, English and French skeleton clocks, English box chronometer, Dress leather strap, Aviator rivet, Rubber dive and Sailcloth straps, Verge and Cylinder pocket watch, English lever pocket watch, Carved and Chalet cuckoo clocks (their sub-versions were not carried over). Named-product "types" (Submariner-style and GS-style cases) dropped from Watch case types.

**tt.** Hand-written for all 36 kinds that had flat types, plus main kinds (dive, chronograph, longcase, etc.).

**Cross-links (`see`):** D2 Smartwatch, Multisport GPS watch, Watch strap; B4 Garden sundial; B5 Kitchen timer; D3 Clock radio; E1 Game clock; plus internal pairs (skeleton watch/clock, bracket/cartel, carriage/travel, chronometer watch/marine chronometer). All targets checked to exist. Watch strap kept in both A5 and D2 (different objects) with see.

**Not done.** Firecrawl was out of credits, so only WebFetch was used. No retailer category page was fetched for Everyday clocks, Timers, Straps or Watch modding parts, so their coverage rests on Wikipedia only and no kinds were added there. Differently sourced archetype `s` values from earlier sessions were kept as they were. Chess clock move already in A5_moves.json is unchanged.
