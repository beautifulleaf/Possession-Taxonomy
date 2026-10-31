# STR_E1 report (Toys & Games)

**Counts, before to after:** departments 12 to 12; shelves 31 to 42; kinds 180 to 197; archetypes 519 to 451. Validator: OK (--v3).

**Category:** added `ax`, a 12-step `key` and a precedence note. `lead` unchanged.

**Showcase, Puzzles, fidgets & desk toys:** the department opens with the goal test (puzzle = goal; fidget = none, held; desk toy = set down). Fidgets are now 14 kinds ordered by hand action: Spinner, Clicker & switch, Popper, Slider & haptic, Squeeze toy, Squishy, Stretch fidget, Flippy chain, Twist (Tangle), Fold (Infinity cube), Baoding balls, Worry stone, Worry beads, Begleri.
- Split: Clicker & button fidget into Clicker and Popper; Worry & hand-rolling object into four kinds; Flip & twist fidget into three; Squeeze toy and Squishy.
- Merged: Speedcube and Smart cube into Cube twisty puzzle; Poker table into Casino gaming table.
- Renamed: Bandaged & shape-mod puzzle to Modified cube puzzle.
- Moved: Rubik's Snake to new kind Chain twisty puzzle.
- Added: Stretch fidget, Flippy chain, Begleri, Pin art, Useless machine, Magic 8 Ball, Chain twisty puzzle, Rag doll, Paper doll, Fingerboard, Paddleball, Clackers, Model engine, Spring rider, Roundabout. Also archetypes Pavelsky patent, QiYi Haptic Coin, NeeDoh (Schylling 2017), Sudoku Cube, Alexander's Star, Minsky ultimate machine, Magic 8 Ball.
- Shelves renamed or regrouped: Mechanical puzzles by family to Mechanical puzzles; Circus & juggling props to Juggling props. Big shelves split in Building, Dolls, Action figures, Board games, Pretend, Baby, Skill, Vehicles and Outdoor.

**Demoted generic archetypes (73, kept as types under "Named forms"):** Three-lobed bearing spinner, Magnetic push slider, Stress ball, the burr, bottle, kite, draughts, xiangqi, domino and miniature-scale entries, controller, decoder and point-motor entries, juggling and poi generics, and similar. Squishy archetype became a kind. Full list: `rebuild/work/STR_E1/log.json`.

**Types (tt-fix):** every `tt` is now written by hand (rebuild/work/STR_E1/tt_data.py); each group label is one question (Material, Scale, Power source, Frame...), and the vague labels are gone. Restored from backup as sourced archetypes: Six-piece, High-level and Diagonal burr; Ship and Fruit in a bottle; eight kite patterns; five draughts variants; Chinese domino set; two marble types. Other demoted generics (for example Reborn doll, Steelie, sock poi, DCC decoders) stay only as plain types or were dropped. Brand ranges moved to `r`: all 9 kit makers, 4 die-cast, Axial and Mini-Z, Carrera, Ninco, Mega, COBI, BlueBrixx, 3 sleeve and 3 binder ranges (their versions were not kept). Dropped from types: Spirit board.

**References fetched (coverage):** Wikipedia Fidget toy, Pop it, Begleri, Infinity cube, NeeDoh, Worry stone, Baoding balls, Komboloi, Desk toy, Mechanical puzzle, Combination puzzle, Jigsaw puzzle, Skill toy, Tabletop game, Doll, Action figure, Scale model, Model railway, Playground, Toy; retailer: specialneedstoys.com fidget page, thecubicle.com haptic coin. Search-only (not fetched): fidget-retailer pages.

**Cross-links added:** Piñata to B4, Marble to F6, Trading card packs to F3, Game clock to A5 Hourglass, Electronic handheld toy to E5, Slime and Stretch fidget, Squishy and Plush toy, Dexterity puzzle and Dexterity game, Dolls' pram and Baby doll. All targets checked.

**Moves:** none. Brand added: Schylling.

**Could not source:** fidget pad (no page found), Torqbar and haptic-coin makers or years, Nice Cube year, Umburry coin (search excerpt only). Retailer fidget pages for Fiddlers Green (503) and Therapy Shoppe (403) failed. Tamiya Hornet-type single RC models stay as archetypes. No fetched coverage reference for Pretend play, Baby toys or Science kits.

## Brief notes
- The "no curl" rule and the Parallel tools: Parallel_Auth returned 402 (no credit); WebFetch worked but is a summariser, so quotes are paraphrases.
- Brief needs a rule for what counts as a generic archetype versus a brand range; I demoted descriptions but kept ranges.
- Dept `t` and shelf `t` use "→ Shelf name" for same-department neighbours, and category codes for others; confirm this is wanted.
- Auto-grouped `tt` is mediocre; give a per-kind hand pass or accept.
- Shelf axes within a department differ when a department mixes object and use (for example railways); say whether that is allowed.
- Schema has no section field for grouping kinds; only `ax` and order express it.
