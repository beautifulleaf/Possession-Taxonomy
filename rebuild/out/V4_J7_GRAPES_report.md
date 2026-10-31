# V4_J7_GRAPES report (step complete-list)

Part file: rebuild/out/J7_parts/GRAPES.json. It adds one department, "Grape varieties". It replaces nothing, so there are no renames, moves or drops. The brand register is empty. The wrapped --v3 check passes: 24 kinds, 849 entries.

Shelves and entries:
- Red varieties: 421.
- White varieties: 344.
- Pink and grey varieties: 8.
- Hybrid varieties: 76.

Kinds are by home region of the variety (for example "French red varieties"). Entries are sectioned by `g` = country of origin, with synonyms in `a`. The list gives no country for 46 whites and 2 reds, so they sit in "unstated origin" kinds.

Method: WebFetch windows at offsets 0, 40000, 80000, 120000, 160000, 180000, 200000 and 260000. The tool refused to reproduce rows verbatim and always reads about 100,000 characters from the offset. I therefore asked for short rows (name, country, at most two synonyms). Rows are merged from all windows, deduplicated by name and colour. The build is work/V4_J7_GRAPES/build2.py, from data.txt, new_white.txt, new_pink.txt and new_hybrid.txt.

Caveats:
- The data passed through a page summariser. It is not checked row by row against the page, and some synonyms or countries may be wrong.
- Completeness is not proven. Reds past about 180,000 characters and whites after Žilavka were not seen. Characters 280000 to 350000 were never read: the 260000 call returned no vinifera rows, only headings and the hybrid tables.
- The earlier six pink rows (for example "Zinfandel Rose") looked doubtful and are replaced by the eight rosé rows from the later window. The rosé section's start may be missing.
- Hybrids: the list states no colour for them, so they are not placed in red or white. They have their own shelf, and the d text says "hybrid". Hybrids the page also files under red or white (Baco Noir, Chambourcin, Chancellor, Chelois, Cabernet Cortis, Cascade, Alexander, Orion, Flora) stay in their colour with "Hybrid." in d. The non-vinifera "table and wine" hybrids are included.
- Cereza and Arnsburger appear in both red and white, as the page lists them.
- Appellations in `d`, `role`, `v`, and market fields are not filled. Grape varieties are not brands.
- Out of scope: table-only varieties, labrusca-only and other single-species wild-grape sections, and rootstocks.

Files: rebuild/work/V4_J7_GRAPES/{progress.md, sources.tsv, data.txt, new_*.txt, build.py, build2.py}.
