# V4_E6 report: E6 Observing & Measuring, named-entry pass

Files changed: out/E6.json, out/E6_brands.json (60 maker names added, no country or year because no page was fetched for them). Renames and moves files untouched. validate.py --v3: OK (102 kinds, 364 entries). Backups and build script: rebuild/work/V4_E6/.

## Entries before -> after (x entries; all former models m now zero in touched kinds)
- Telescopes: Refractor 12 -> 9 (designs Galilean, Keplerian, aerial, achromatic, apochromatic, Petzval, superachromat, copyscope, unilens; the 11 former maker-line entries and 12 models became versions); Newtonian 1 -> 1 (design, 6 lines as versions); Dobsonian 2 -> 8; Cassegrain 3 -> 8; Gregorian & off-axis 4 -> 7; Schmidt-Cassegrain 3 -> 2; Maksutov 3 -> 3; Schmidt astrograph 2 -> 6; new kind Specialist catadioptric telescope 0 -> 6; Smart 6 -> 7; Solar telescope 2 -> 5; Solar filter 3 -> 5.
- Binoculars family: Binoculars 14 -> 37 (six prism-type entries from Wikipedia's Binoculars article, then maker lines); Opera 1 -> 6; Giant 1 -> 10; Monocular 0 -> 8; Spotting scope 4 -> 22; Night vision 1 -> 3; Thermal 4 -> 11.
- Microscopes: Compound 7 -> 17; Stereo 2 -> 18; Polarising 0 -> 7; Digital 0 -> 13.
- Weather: Weather station 3 -> 21; air thermometer, hygrometer, anemometer, rain gauge, barometer, barograph, Geiger counter each gain their former models as entries; new kinds Pyranometer (1), Wind vane & windsock, Disdrometer & ceilometer (no entries, commodity or professional).
- Sky and historic: Orrery 3 -> 5, Astrolabe 3 -> 4, Quadrant 1 -> 2, Sextant gains Octant, Armillary sphere and Nocturnal 1 each, Home planetarium 1 -> 5; new kinds Ancient & medieval calculating instrument (10), Sundial & gnomon (3), Early navigation aid (4). Sections by period.
- Every touched kind has nl, sel and, where useful, xg.

## References fetched (logged in work/V4_E6/sources.tsv)
Wikipedia: List of telescope types, Binoculars, Microscope, List of astronomical instruments, List of weather instruments. The Wikipedia list of historical scientific instruments returned 404; the astronomical-instruments list was used instead. The weather list has only 12 instruments, all covered as kinds.

## Disposition of former models
All m in touched kinds were turned into entries or versions. Removed as out of scope: Vaonis Atlas (a mount), Ecowitt GW1202 gateway (accessory), Meade glass solar filter, euro EMC SF100 and Artesky filters (no lineage). Apogee SP-110 moved to the new Pyranometer kind. Ranges r kept where a maker range spans many entries (weather, microscopes), removed from telescopes.

## Not done or not sourced
- Entry sources for converted models reuse the kind-level and entry source URLs from the earlier pass, not pages re-fetched this session. Models from that pass have a generic description ("model from X") and no year.
- Years and inventors on new design entries come only from the fetched pages or earlier-pass data; the telescope list gives none. Several professional designs (Wolter, Crossed Dragone, Pfund, Stevick–Paul) have only a one-line description.
- Maker lines as versions of Dobsonian designs are in separate maker entries, since no page names the line hierarchy.
- Prism type of most maker-line binoculars is not stated by a fetched page, so they sit under "Maker lines" rather than under a prism entry.
- Roles (origin/landmark) only for Galilean telescope and the Dobsonian design; no other page-backed badge was checked.
- Mounts & accessories, microscope parts, magnifiers and Home & hobby lab kinds were left as they were (commodity or out of the named levels); lab glassware stays a commodity kind. No market layer (ms, own, tier) was added: BRIEF.md does not list E6 for one.
