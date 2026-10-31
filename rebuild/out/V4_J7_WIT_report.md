# V4_J7_WIT report: wine of Italy

Part file: rebuild/out/J7_parts/WIT.json (validates OK: 1 department, 53 kinds, 519 entries).

**Structure.** One department, "Wine of Italy" (mode tier). 20 shelves, one per region. Kinds are the appellation tier per region ("Tuscany: DOCG appellations", "...: DOC appellations", "...: IGT appellations"); Piedmont and Aosta Valley have no IGT kind (the IGT page states none are produced there). Entries are appellations only; no producers.

**Sources (all fetched).** Wikipedia List of Italian DOCG wines (76 listed, page says 77), List of Italian DOC wines, List of Italian IGT wines, Barolo DOCG, Italian wine. Logged in rebuild/work/V4_J7_WIT/sources.tsv.

**Counts.** Entries: DOCG and DOC and IGT kinds together 519. Appellations that are in both the DOCG and DOC lists appear once, under DOCG. Cross-region zones (delle Venezie, Valdadige, Lugana, Orvieto and others) appear once, with the span noted.

**Versions.** Only those a fetched page names: Chianti sub-zones, Valtellina Superiore sub-zones, Asti styles, Barbera d'Asti sub-zones, riserva/superiore/classico forms, and Barolo's traditional crus by commune (stated as unofficial; the page says there is no official classification).

**Market.** One sourced fact in `ms`: Italy produced 49.8 million hl in 2022, 19.3 % of world output (Italian wine, Wikipedia).

**Renames (old grape kinds to appellation kinds).** Sangiovese to Tuscany DOCG; Nebbiolo, Arneis, Cortese to Piedmont DOCG; Dolcetto, Barbera to Piedmont DOC; Lagrein to Trentino-Alto Adige DOC; Refosco to Friuli-Venezia Giulia DOC; Friulano likewise; Sagrantino to Umbria DOCG; Montepulciano and Pecorino to Marche DOCG; Aglianico, Greco, Fiano to Campania DOCG; Nero d'Avola, Nerello Mascalese, Carricante, Malvasia to Sicily DOC; Garganega to Veneto DOC; Vermentino to Sardinia DOC; Verdicchio to Marche DOC; Trebbiano to Abruzzo DOC; Falanghina to Campania DOC. Ties were broken by the larger tier; Falanghina, Malvasia and Refosco kinds also hold non-Italian wines, which the GRAPES part should relocate.

**Dropped/moved.** None. Italian wines in style kinds (Prosecco, Franciacorta, Lambrusco, Marsala, vermouth, Super Tuscan) and multi-country grapes were left to their own parts.

**Not sourced.**
- The Wikipedia DOC list is shorter than the official register (about 330 names; some newer DOCs are missing).
- Colours and grapes per appellation are given only where the DOCG page states them (`dt`); other entries rely on the kind-level `tt`.
- The Barolo and Barbaresco MGA lists (181 and 66) could not be fetched in full, so they are not versions; the Barbaresco page returned 404.
- No `role` badges: no fetched page names a top-ranked appellation.
- No Italian brand owners or tiers (appellations are not brands); the `brands` list is empty.
