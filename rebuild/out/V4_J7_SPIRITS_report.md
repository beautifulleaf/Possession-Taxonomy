# V4_J7_SPIRITS report

Part file: rebuild/out/J7_parts/SPIRITS.json (validates: 0 errors, 71 kinds, 1,400 entries; about 700 KB, so trim if J7 must stay near 400 KB). Build script and logs: rebuild/work/V4_J7_SPIRITS/ (build_part.py, sources.tsv, progress.md, dropped_models.json).

## Structure
Old departments Whisky, Spirits and Liqueurs become eight: Whisky; Brandy; Rum & cane spirits; Agave; Gin, vodka & aquavit; Anise & absinthe; Asian spirits; Liqueurs. Every old kind survives under its own name, so `renames` and `moves` are empty. Nothing dropped at kind level.

## Entries by department and reference (all fetched)
- Whisky 413: Scotch malt distilleries by region and Scotch grain distilleries (Wikipedia, List of whisky distilleries in Scotland, 158 malt, 8 grain); bourbon brands by distillery (List of bourbon brands, first 100,000 characters); Irish distilleries, 47 operating and 22 closed; Japanese distilleries (Japanese whisky article); Canadian distilleries with brands as versions.
- Brandy 66: Cognac houses and crus; Armagnac areas; Calvados AOCs; pisco types (Cognac, Armagnac, Calvados, Pisco articles; whisky.fr houses).
- Rum 361: List of rum producers by region and country, Martinique and Guadeloupe under Rhum agricole.
- Agave 57: List of tequilas; Mezcal categories and agave types.
- Gin, vodka & aquavit 201: lists of vodkas and gins by country.
- Asian 62: baijiu aroma types and brands; shōchū regional types; soju brands.
- Liqueurs 224: List of liqueurs sections mapped to kinds.
- Anise & absinthe 16: old entries only.

## Market layer (after audit)
Owners are kept only where a fetched record states them; each such entry carries `os` (source URL) and, where the page gives a year, `own_y`. Records used: the list pages themselves (Scotland, bourbon, Irish, Canadian, rum, Soju, Cognac), the owner groups' Wikipedia pages (Diageo, Pernod Ricard, Bacardi, Campari, Rémy Cointreau, Brown-Forman, Beam Suntory, LVMH) and three Wikidata SPARQL rows (Amrut, Monkey Shoulder, O.P. Anderson). Wikidata bulk queries returned mostly label collisions (ships, schools), so the group pages carry most checks. Result: 400 entries have `own` with `os`, 53 have `own_y`, 1,151 have `cty`. Owner names not found in any fetched record were removed (for example Famous Grouse, Hendrick's, Jose Cuervo, Hine, Kahlúa excepted, Bols, Disaronno, Drambuie, Amarula, Moutai). Finlandia now shows its 2023 sale (Coca-Cola Hellenic) per the Brown-Forman page. Belvedere is LVMH per the LVMH page, not the stale Wikidata owner.
Tiers: Global group (181) only where `own` is one of the eight groups and sourced; Independent (33) only for Irish distilleries the list calls independent; National champion only for Jinro (Soju page: largest maker). All Craft & indie tiers were removed (no fetched craft overview). Entries with a sourced non-group owner carry no tier. Department `ms`: Soju only. One `role`: Jinro.

## Gaps
- Not found (404 on guessed URLs): Irish brands list, Japanese distillery list, Cognac houses list, absinthe brands list, Canadian distilleries list. Substitutes used. The NOM tequila register, Armagnac, Calvados and Cognac producer lists, pastis, ouzo and aquavit brands were not fetched; those kinds keep the old sourced entries.
- Old models: 194 had no match in the first pass. In the audit 32 more were restored as versions (d 'bottling') because their maker matches an existing entry; 162 remain dropped as unsourced bottlings with no matching entry (list in rebuild/work/V4_J7_SPIRITS/still_dropped.json). 40 models became versions earlier and 41 old entries became versions of list entries.
- Versions are only those already in the previous edition or named on fetched pages; core expressions of the new distilleries are not added.
- Blended Scotch, American subtypes, world whisky, grappa, fruit brandy, anise, cachaça: previous-edition entries only, no whole-space list.
- Armagnac and Calvados kinds hold areas and AOCs as entries; old producer entries kept.
