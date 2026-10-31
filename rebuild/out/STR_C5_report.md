# STR_C5 report (Office & Stationery)

Before -> after: departments 6 -> 6 (same names); shelves 20 -> 24; kinds 96 -> 112; archetypes 244 -> 245. validate.py --v3 prints OK. Category `ax` and a 6-step `key` added; every department has `t` and `ax`, every shelf `t` (and `ax` above 3 kinds), every kind `tt` (no `t` left).

Shelves: Fountain pens (calligraphy fountain pen moved in from the dip shelf); Dip pens & glass pens; Brush calligraphy tools; Notebooks & journals / Planners & calendars / Pads, loose paper & notes / Letters, post & wrapping (was two mixed shelves); East Asian seals & paste / Wax seals & embossers / Ink stamps (was one); Calculators / Calculating antiques & collectables / Typewriters / Office machines.

Kinds split: Typewriter -> Manual, Electric, Electronic; Rubber stamp -> Rubber, Self-inking, Pre-inked, Stamp ink pad (dater is a type); Clips, pins & fasteners -> Clips, Pins bands & tags; Basic calculator -> Basic, Printing calculator; Notebook -> Notebook, Composition book, Reporter's notebook, Lab & field notebook.
Renamed (C5_renames.json): Typewriter -> Manual typewriter; Clips, pins & fasteners -> Clips; Planner or notebook cover, refills & inserts -> Notebook & planner covers, refills & inserts.
Added (source): Quill & reed pen (Quill, Pen), Pencil extender (Pencil), Legal pad (Notebook), Adhesive label (Office supplies), Artist's & collector's seal (Seal East Asia), Embossing seal (notary embosser page), Electric and Electronic typewriter, Printing calculator (Calculator). New archetypes: Hansen Writing Ball, Hammond Typewriter, IBM Electromatic 04, Coronamatic, Olivetti Tes 501, Canon Typestar 110, Silver City Writing Tablet. Brands added: Malling-Hansen, Hammond.
Nothing moved to other categories (C5_moves.json unchanged). No kinds dropped.

Generic archetypes demoted: Oblique pen holder and Coloured ink stick (now types), Waterman ink and J. Herbin Encre (-> ranges), Herbin brass wax seal and J. Herbin sealing wax (-> ranges). Disc-bound notebook renamed Atoma disc-bound system. Field Notes and Rite in the Rain moved to new notebook kinds; Trodat Printy and COLOP models moved to Self-inking stamp.

Coverage references (fetched, Wikipedia unless stated): Fountain pens and ink & parts: Fountain pen; Dip pens: Pen, Quill; Brush calligraphy: Four Treasures of the Study; Everyday pens and markers: Pen; Pencils: Pencil; Erasers, desk, files, post: Office supplies; Notebooks and pads: Notebook; Seals: Seal (East Asia), Rubber stamp, engineersealstamps.com notary page; Calculators and antiques: Calculator; Typewriters: Typewriter, Hansen Writing Ball.

Cross-links: 37 `see` entries, all targets checked in reader files, including required Inkstone (C4) and Highlighter (H1).

Not done: JetPens category page returned 403 and the Filofax page 404, so no retailer check of pen shelves; dictation machines fetched but not added (carriers sit in Media & Publications). Some types (wide-ruled, tape widths) are from common knowledge.
