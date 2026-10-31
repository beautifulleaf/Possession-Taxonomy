# STR_F1 report (Media & Publications)

Counts before -> after: departments 8 -> 8; shelves 20 -> 35; kinds 132 -> 159; archetypes 339 -> 178; models in `m` 51 -> 164 (demoted archetypes' versions kept here); ranges in `r` 89 (maker ranges moved out of archetypes).

Added: category `ax` and `key`; `t`/`ax` on every department and shelf; `tt` axis groups on kinds; `see` cross-links (24).

Shelf changes: mixed shelves split by one axis per department (for example Books into Everyday, Children's, Publisher special editions, Hand-crafted, Illustrated & catalogue, Cheap serial print, Manuscripts & early printed, Traditional Asian; Sheet music into Scores, Parts & choral, Songs & hymns, Editions & tuition; Globes into Globes, Specialist globes, Globe fittings).

Kinds merged/renamed (in F1_renames.json): Dictation and wire recording -> Wire recording; Digital and late analogue cassette -> Digital Audio Tape (DAT); Camcorder cassette -> VHS-C cassette; Score and parts -> Performance parts.

Kinds added (32, each with `s`): Book club edition, Coffee table book, Armed Services Edition, Scroll, Pothi, Extended play (EP), X-ray record (ribs), DualDisc, Wire recording, Elcaset, DAT, DCC, Music box disc, Dictabelt, VHD videodisc, U-matic, Cartrivision, VHS-C, Video8/Hi8, MiniDV, Digital8, 28 mm print, Graphic novel, Vocal selections, Hymnal, Tablature book, Raised-relief map, Portolan chart, Lunar and planetary globe, DVD keep case, Digipak, Disc sleeve.

Moved (F1_moves.json, appended): Sewing or knitting pattern -> C4 (Fabric, thread & sewing machines). The existing Graded comic slab -> F3 entry is kept.

Archetypes: generic descriptions (for example Big-box VHS, Punk zine, Hero and detective pulp, Book of hours, Oil-company road map) were removed as archetypes; their sourced versions were kept as models in `m` (the archetype itself if it had no versions). Maker or imprint archetypes (Kelmscott, Doves, Folio Society, Rivière, Moleiro, Aldine and similar) became ranges in `r`. No sourced item was dropped.

References used for coverage: Wikipedia tape cartridge and cassette formats list, video format timeline, 8 mm video format, plus the 25 specialist and reference pages logged in work/STR_F1/sources.tsv (Kelmscott Chaucer and Doves Bible pages fetched; two alternates returned 503/403).

Not sourced / gaps: Fitzwilliam and Britannica alternates failed to load; their facts rest on the other fetched pages.

validate.py --v3 out/F1.json: OK (0 errors, 159 kinds, 178 archetypes).
