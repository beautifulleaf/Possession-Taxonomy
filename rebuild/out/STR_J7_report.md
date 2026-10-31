# STR_J7 report: Wine, Beer & Spirits

**Before → after.** Departments 12 → 12. Shelves 38 → 45. Kinds 276 → 294. Archetypes 1,011 → 931. `validate.py --v3` prints OK. Backups are in rebuild/work/STR_J7/bak/; sources are logged in rebuild/work/STR_J7/sources.tsv.

**Category.** Added `ax` and a 12-step placement `key` with a precedence note. The lead is reworded slightly; nothing contradicted RULES.md.

**Departments and shelves.** Every department has `t` and `ax`; every shelf has `t` and `ax`. Kinds are ordered along the shelf axis.
- Red and white wine: the catch-all "More ... grapes" shelves are regrouped by home region (Central Europe/Balkans/Greece/Caucasus; Americas and southern Africa; French and Swiss regional). The grape tree was not re-levelled by appellation.
- Beer: new shelf "Amber, brown & strong ales" (Mild, Scottish ale, Old ale and Barleywine moved in). Beer now has 9 shelves, one over the target.
- Whisky: Scotch blends renamed "Blended & grain Scotch whisky"; Irish split out from "Irish, Japanese & world whisky" into two shelves.
- Liqueurs: one flat 10-kind shelf split into fruit and flower, herb and bitter, and cream, coffee and nut.

**Kinds.** All 198 flat `t` lists were rewritten by hand as `tt` with question-style group labels. No kinds merged, renamed or moved out (`J7_renames.json` is empty; `J7_moves.json` unchanged).

**Added (18), reference per shelf.** Wikipedia: List of grape varieties (Cinsault, Zweigelt); Sparkling wine (Cap Classique, Brachetto, Sparkling Shiraz); List of beer styles (Blonde ale, Amber & red ale, Brown ale, Rye beer); Whisky (Blended American whiskey); Distilled beverage (Aguardiente); List of liqueurs (Flower, Chocolate, Honey, Whisky liqueur); Sake (Kijōshu, Doburoku); Cider (Apfelwein & Most). Also checked with no further gaps: Fortified wine, Sake, Mead, Alcopop, Non-alcoholic drink.

**Generic archetypes demoted: 80.** They became `tt` members; 155 sourced versions were kept as models in `m`, and three brand ranges (Cantillon fruit lambics, Russian River, Jester King) went to `r`. Examples: mead variants, Cava grades, pisco categories, mezcal agave types, fruit-wine fruits, Chilean Carmenère. St-Germain and Drambuie moved to the new Flower and Whisky liqueur kinds.

**Cross-links: 12** `see` entries, all targets checked (J3 Pecorino, J5, J9, B5).

**Not done / caveats.**
- New kinds have no archetypes.
- Some `tt` members come from the existing data, not a fetched page.
- Carignan, Poitín and Kvass were not added; Kvass and Boza already sit in J9.
