# V4_F2 report: Art named-entry pass (medium group)

Validated with validate.py --v3: OK (141 kinds, 418 entries). Files edited: out/F2.json, out/F2_brands.json. F2_moves.json and F2_renames.json unchanged (no kind moved or merged). Backups, edit scripts, sources.tsv and ve_names.json are in work/V4_F2/.

**Counts (entries before -> after):** 296 -> 418 entries; 119 loose models (m) -> 0; kinds 138 -> 141 (new: Collodion photograph, Rarely met named process, Precious and soft-metal sculpture). Brand register 213 -> 95 (artists removed; Hummel Manufaktur, Fiskars, PHI Industrial Acquisitions, Free State of Saxony added).

**Artists, works, movements removed** (about 85 entries, all loose models, and artist-made versions): moved to a `ve` list on each kind (names for the Visual Entertainment taxonomy; the schema's `see` accepts only A-J codes). Generic forms kept under neutral names (Mobile, Stabile, Machine sculpture, Welded-steel sculpture, Bozzetto, Animalier bronze, Chryselephantine figure, Bizarre ware, Foundational hand, Papier collé). Dept notes say so.

**Processes (from fetched lists):**
- Photographs: Wikipedia List of photographic processes (about 250 names, read as name lists through the summariser; Wikidata class Q172839 holds only 22 mixed items, so not used). 118 process entries added across kinds, including the new "Rarely met named process" kind. Covers 118 of about 250; film stocks, negatives, papers and darkroom steps left out. Dates only where the page gave them.
- Prints: Wikipedia Printmaking plus Boston Printmakers glossary: 34 of 37 terms (not paper marbling, direct-to-garment, collage). Edition structure added as type "Edition" on every print, photograph and cast-sculpture kind.
- Painting and drawing media: List of art media: 8 of 8 painting media and 9 of 9 drawing materials are kinds or entries; supports are attributes. Fresco techniques from the Fresco article.
- Sculpture: casting methods from Lost-wax casting; materials from the Sculpture article, read only to 100,000 of 407,686 characters.

**Figurines:** maker lines with named series as entries, grouped by house: Lladró (2), Hummel (5), Meissen (8). Owner facts from fetched pages (Lladró PHI 2016, Hummel Foertsch 2017, Meissen Saxony).

**Not sourced:** Royal Copenhagen and Royal Doulton pages name patterns and numbering, not figurine series, so no series entries (Royal Doulton keeps its HN entry). Stacco a massello dropped (no fetched page). Hauser & Wirth glossary returned 429. Summariser would not return the photograph list verbatim with descriptions, so process entries carry templated one-line definitions. Market layer not applicable to Art. About 15 fetches used.
