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

## Market layer
`own`, `tier` and `cty` are on 452 and 486 and 1,151 entries respectively. Owner names come from the list pages where stated (Scotland, Ireland, bourbon, Canada, rum notes). Others (for example Four Roses to Kirin, Amarula to Distell, Kahlúa to Pernod Ricard) are from general knowledge in ownmap.txt and need audit. No `own_y` (no fetched page gives acquisition years). Craft & indie is applied to independent distilleries opened from 2000, a rule of mine, not a fetched craft overview. Department `ms`: one fact only (Soju: HiteJinro almost half, October 2023). No Alexandria or share data found for the other departments. One `role`: Jinro as landmark (page: best-selling branded spirit, 2019). No `alc` set (no alcohol-free items in scope).

## Gaps
- Not found (404 on guessed URLs): Irish brands list, Japanese distillery list, Cognac houses list, absinthe brands list, Canadian distilleries list. Substitutes used. The NOM tequila register, Armagnac, Calvados and Cognac producer lists, pastis, ouzo and aquavit brands were not fetched; those kinds keep the old sourced entries.
- Unmatched old models (194) were dropped as bottling-level SKUs without sources (list in dropped_models.json); 40 became versions of matching distilleries and brands; 41 old entries became versions of list entries.
- Versions are only those already in the previous edition or named on fetched pages; core expressions of the new distilleries are not added.
- Blended Scotch, American subtypes, world whisky, grappa, fruit brandy, anise, cachaça: previous-edition entries only, no whole-space list.
- Armagnac and Calvados kinds hold areas and AOCs as entries; old producer entries kept.
