# STR_B2 Soft Furnishings: structure report

**Counts (before → after):** departments 6 → 6; shelves 18 → 20; kinds 78 → 84; archetypes 165 → 151. validate.py --v3 prints OK.

**Category:** added `ax` (floor, bed, seats, windows, bath or table) and a 6-step `key` with a precedence note. Lead unchanged (it already says "organised by use").

**Departments and shelves:** every department has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than 3 kinds. Towels split into "Bath & body towels" and "Flat-woven & wrap cloths". Table & kitchen linen split into "Dressing the table" and "Kitchen cloth". Other shelves kept; kinds reordered along each shelf's axis.

**Kinds:** all flat `t` lists replaced by hand-written `tt` (one question per group). Body pillow moved from a type of Bed pillow to its own kind. Types merged out: weighted blanket (now a `see` to H2), panel track (now the Panel blind kind).

**Added (reference per shelf, all fetched):** Comforter, Coverlet (Wikipedia Bedding, duvets shelf); Afghan, Sleeved blanket, Baby blanket (Wikipedia Blanket); Body pillow (Wikipedia Pillow), Bolster (Wikipedia Bedding); Panel blind (Wikipedia Window blind); Pelmet and valance (Wikipedia Window covering); Poncho towel, Sports towel, Baby towel (Wikipedia Towel); Doily, Table protector (Wikipedia Tablecloth). Rugs and mats: no whole-space reference could be fetched (Wikipedia Doormat lists no kinds; Firecrawl ran out of credits before the rug category page), so rug shelves are unchanged apart from structure.

**Generic archetypes demoted (carried into types or ranges):** Terry towel; Damask and Indian block-print tablecloth; Irish linen tea towel; Matelassé, Candlewick, Chenille and Indian block-printed bedspreads; Cowhide and Sheepskin rug; Braided rug, Proggy mat; Latch-hook and Stamped-pattern rug; the four Designer rug maker lines moved to `r`.

**Cross-links (`see`):** 24 across 23 kinds, e.g. Quilt → F2 Art quilt / E2 Backpacking quilt, Blanket → H2 Weighted blanket, Persian rug → F4 Prayer rug, Towel → G3 Heated towel rail. All targets checked against rebuild/reader. No B2 pairs were in STR_SEE.tsv.

**Moves:** none new; B2_moves.json untouched. **Brands file:** untouched.

**Not sourced / left:** no models or archetypes added; Eiderdown and net curtain not added (no fetched source). Sources logged in rebuild/work/STR_B2/sources.tsv.
