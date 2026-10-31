# STR_E3 report (Musical Instruments & Music Gear)

**Counts, before to after:** departments 10 to 10; shelves 36 to 47; kinds 210 to 237; archetypes 691 to 570. Validator: OK (--v3).

**Category:** added `ax` and a 10-step `key` with a precedence note. `lead` unchanged. Every department has `t` and `ax`; every shelf has `t` and `ax`; all 237 kinds carry a hand-written `tt` (work/STR_E3/tt_data.py).

**Department change:** "Pianos & keyboards" renamed "Keyboards & electronic instruments" (it holds drum machines and controllers). Other department names kept.

**Regrouped shelves:**
- Guitar parts split into Bodies & necks, Pickups & wiring, Bridges/tuners/hardware, Strings.
- Keyboards: digital and electric pianos, early and unusual electronic instruments split out.
- Percussion: Hand & world percussion and Tuned & orchestral percussion rebuilt as Hand drums, Cymbals/gongs/chimes, Shakers/scrapers, Tuned percussion.
- Orchestral: Clarinets & double reeds split into single-reed and double-reed shelves (saxophone joins single reeds); Early & period instruments added.
- Folk: shelves now follow how the sound is made (lutes, zithers, bowed, free reeds, pipes, mechanical).
- Pedals: re-cut into drive (ordered by clipping), time/modulation, filter/pitch/dynamics, multi-effects.
- Recording: by signal-chain stage. DJ: Decks & players, Mixers & controllers.

**Added kinds (27, each sourced from a fetched page):** Archtop acoustic guitar, Portable keyboard, Celesta, Udu, Tambourine, Gong and tam-tam, Shaker and maraca, Güiro and scraper, Cowbell and block, Triangle, Castanets, Tubular bells, Lute, Viola da gamba, Sackbut, Cornett, Serpent, Baritone horn, Cavaquinho, Bağlama (saz), Kora, Sheng, Native American flute, Dizi, Duduk, Microphone stand, Timecode vinyl. Coverage references: Wikipedia List of musical instruments (three parts) and Thomann UK category navigation. Sweetwater returned 403; Monitor controller (404) and Guitar strap (no definition) were not added.

**Archetypes:** 108 generic ones demoted to types (e.g. Superstrat, Flamenco blanca, steelpan voices, concertina systems, ocarina forms, ney styles); 20 maker ranges or makers moved to `r` (five flute makers, Bösendorfer and Fazioli ranges, Boss series, LP congas). Six sourced named classics added: Gretsch Duo Jet, Fender Mustang, Yamaha CS-80, Roland D-50, Casio CZ-101, EMS VCS 3, plus Gibson L-5 (acoustic).

**Cross-links:** about 45 `see` entries; targets checked in D1, D3, E1, E5, F1, F4, I1. Required pairs done: In-ear monitors (D3), DJ turntable and Turntable (D3), Dynamic microphone and Microphone (D1; D3 has no microphone kind).

**Merged/renamed kinds:** none (E3_renames.json is empty). **Moves:** none. Cable moves from D1 kept; the shelf name "Picks, sticks, reeds & cables" is unchanged because the placement table points at it.

**Not done:** shelf coverage was checked against list pages only, not per-shelf retailer pages, so pedals, amps and studio gear were not extended with new named classics; new kinds lack archetypes except the Archtop L-5; some `tt` values for pedals and studio gear rest on the existing data and general knowledge, not fetched pages.
