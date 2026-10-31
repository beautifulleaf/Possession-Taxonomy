# V4_J7_GRAPES report

Part file: rebuild/out/J7_parts/GRAPES.json. Validates (23 kinds, 560 entries). It adds one department, "Grape varieties". It replaces nothing, so there are no renames, moves or drops. The brand register is empty.

Structure: three shelves (red, white, pink and grey). Kinds are by home region (for example "French red varieties"). Entries are sectioned by `g` = country of origin, with synonyms in `a`.

**This part is incomplete.** The brief asks for every variety the reference lists. WebFetch returns a summary of the page, not its rows, and the page is 350,000 characters.
- Red: the list runs from Abbuoto to Zweigelt, but the summariser dropped rows. Only about 480 of the page's red varieties are present, and the 100,000-200,000 window began mid-list.
- White: Addoraca to Grechetto only. Whites from H to Z are missing.
- Pink: six rows, copied from the page's "Rose grapes" section.
- Not fetched: characters 300,000 onwards, and a clean pass over whites H to Z.
- A fuller list needs Firecrawl scrape of the page, read in pieces, or a rerun with smaller windows.

Data quality:
- Synonyms and countries are as returned by the summariser, with at most two or three synonyms per row. Spot checks matched the page's known pattern, for example Bovale Sardo and Cagnulari both listing Graciano. Some rows may be wrong. Examples: "Zinfandel | Croatia" and "Zinfandel Rose | Austria".
- Colour follows the page's section. Arinto de Bucelas was listed under red; I left it out as probably white. It is not placed under white either.
- Entry `s` is the list page, which was fetched.

Not done, for lack of sourcing:
- `d` appellations (up to five per variety): none. No page was fetched per variety, so every `d` is a plain one-line description.
- `role` badges, `v` versions, `own`, `tier`, `cty` and `ms`/`msum`: none. Grape varieties are not brands, so market fields do not apply.
- Hybrids (Baco Noir and similar), which the page lists in a separate section, are only present where the summariser placed them under the red vinifera section (Baco Noir, Chambourcin, Chancellor and others). Whether they belong needs checking.

Files: rebuild/work/V4_J7_GRAPES/{data.txt, build.py, sources.tsv, progress.md}.
