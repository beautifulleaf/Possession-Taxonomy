# V4_I1_CREATIVE report

Part file: rebuild/out/I1_parts/CREATIVE.json (439 KB; validates, 0 errors; 67 kinds, 1,010 entries). Replaces the five departments by exact name. Builder: rebuild/work/V4_I1_CREATIVE/build.py and data.py; sources.tsv logs the pages fetched (about 38 fetches).

Method: every former model (`m`) became an entry (sourced at kind level to the old kind page); entries from fetched list pages were added; dedupe by name and alias across all five departments; `g` is the maker; order is maker, year, name. Kinds with entries now carry `nl`, `sel` (with the "Covers n of about m" line) and `xg`.

Entries before -> after (named + former models -> total), main kinds: Image editor 6+15 -> 40; Photo manager 5+14 -> 23; Vector 7+7 -> 29; CAD 7+12 -> 39; 3D modelling 7+19 -> 40; new 3D renderer 12; Circuit design 4+12 -> 27; Video editor 7+13 -> 33; DAW 11+14 -> 37; Notation 6+10 -> 32; Media player 0+12 -> 60; Software synthesiser 16+16 -> 55; Genealogy 5+3 -> 26; new Online family-tree service 13; Planetarium 5+5 -> 26; GIS 4+8 -> 21; Science and statistics 5+14 -> 44; new Plug-in format 13 and Instrument & effect bundle 2.

References fetched (Wikipedia): comparisons of raster editors, vector editors, video editing, audio editors (DAW table), scorewriters, GIS, CAD (all but the first row of the tail), EDA, screencasting, audio and video players, statistical packages (first 100,000 characters; the tail held only four already-listed names); lists of 3D software and screenwriting software; Planetarium software, Software synthesizer, Virtual Studio Technology, Audio plug-in, Genealogy software, Text-to-image model; company pages for Native Instruments, Waves Audio, FabFilter, Universal Audio, Spectrasonics, Xfer Records.

Removed as out of scope: Quad Cortex (hardware), Gardena, duplicate range-like models (Neural DSP plug-ins, Valhalla reverbs, Lexicon 224 and 480L, Tokyo Dawn free dynamics, Mastering The Mix metering), DNA-testing services, server and trade GIS products, discontinued products. ShareX and Snagit sit under Screenshot tool only.

Not done or not sourced:
- No market figures (`ms`/`msum`): no fetched page gave shares for these departments. `tier` and `cty` are not set; `own` equals the maker named on the fetched page. `own_y` not set.
- Roles: only Neon and VST (first VST instrument and plug-ins, per the VST page); older roles kept.
- New entries have no versions (the product history pages were not fetched); old versions are kept. Serum 2 (2025) added to Serum from the Xfer page.
- Not completed: Wikipedia list of music software (DJ, wave editors, trackers, VST hosts) was only summarised by the fetch tool; the music tracker, DJ, audio editor and orchestral/drum/amp kinds stay at previous-edition entries. Notation tablature, slicers, photogrammetry, laser, ham radio, SDR, astrophotography and home-design kinds have no complete reference read. Their `sel` says so.
- AAX, TDM and RTAS appear on the Audio plug-in page without years; CLAP has no maker there.
- Brand register: 356 makers added to `brands` with name only; country and founding year were not on the fetched pages.
- Entry descriptions for converted and new rows are templated (maker, year), not hand-written.
