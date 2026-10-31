# V4_J7_WFR report

File: rebuild/out/J7_parts/WFR.json (validates OK: 1 department, 34 kinds, 460 entries; builder and sources in rebuild/work/V4_J7_WFR/).

## Structure
Department "Wine of France" (mode mixed), 11 shelves (regions), 35 kinds (districts or appellation tiers, e.g. "Bordeaux: Left Bank appellations"), entries = appellations.
- Reference: Wikipedia, List of Appellation d'Origine Contrôlée wines (every row, duplicates merged, spellings repaired), plus appellations named in the Languedoc-Roussillon list (Pic Saint-Loup, Terrasses du Larzac, La Clape, Berlou, Roquebrun, Roussillon Villages sub-names) and the vin doux naturel article (Rasteau, Muscat du Cap Corse).
- Versions: 1855 classification (Pauillac, Margaux, Saint-Julien, Saint-Estèphe, Haut-Médoc, Sauternes, Barsac; rank in `d`), Graves 1953/1959 classified estates and Haut-Brion (Pessac-Léognan), Saint-Émilion 2022 premiers grands crus classés A and B (Saint-Émilion Grand Cru), the 17 Champagne grand cru villages (Champagne). Burgundy grands crus are appellations, in a "Grands crus" section.
- Kind `tt`: colour/style and main grapes per kind (grape lists are general knowledge, not page-sourced).
- Languedoc-Roussillon also has an IGP kind (57 zones from the Wikipedia list).
- Department `ms`: three sourced figures from Wikipedia "French wine" (2005 AOC 53.4 %, Vin de Pays 33.9 %; 2007 area 861,075 ha).
- Brands: none added. Moves: none.

## Renames (old kind to new kind)
Bordeaux red blend, Merlot, Sauternes & Barsac, White blend, Pinot Noir, Chardonnay, Crémant, Gamay, Viognier, Cabernet Franc, Chenin Blanc, Melon de Bourgogne, Sauvignon Blanc, Muscat, Savagnin, Altesse, Pétillant naturel, Vin doux naturel, and the four Champagne kinds (now renamed to "Champagne houses"). Only kinds with a French majority were renamed.

## Not done or not sourced
- Non-French entries in renamed kinds are lost unless other parts take them: Masseto; Central Otago, Willamette Pinot Noir; California Chardonnay; Marlborough Sauvignon Blanc; South African Chenin; Heida; Col Fondo; Gemischter Satz, Edelzwicker; Sassicaia, Ornellaia, Opus One, Meritage, Ridge Monte Bello; non-French models `m`.
- Mixed kinds left alone (French share at most half): Syrah, Grenache, Rosé, Red blend, Riesling, Pinot Blanc, Pinot Grigio, Gewürztraminer, Late-harvest wine, Regional fortified wine (Pineau des Charentes, Floc de Gascogne, Macvin du Jura have no appellation page fetched). Nothing dropped otherwise.
- Old French entries absent from the AOC list were dropped: Pétrus, Le Pin, Coche-Dury, Leflaive, Cheval Blanc, Cru Bourgeois, Beaujolais nouveau, Southern Rhône blend, vin jaune, Vendanges Tardives (producers or styles).
- That list is dated and incomplete: e.g. Jurançon sec, Muscat d'Alsace sub-names, Floc, Pineau and several newer appellations are absent. Only Languedoc-Roussillon IGPs were found on a fetched list (France has 75 IGPs); other IGPs missing.
- No `role` badges: no fetched page named a top rank for an appellation. No Alsace Grand Cru vineyards or Burgundy premiers crus. Appellation of Graves estates is inferred as Pessac-Léognan; the page names Graves only. Wikipedia region labels kept as given.

## Added: houses and estates (step houses-estates)
- New kind "Champagne houses": all 49 houses in Wikipedia's List of Champagne houses (UMC members, then other major houses), each with `own`, `tier`, `cty`=France and the page's cuvées as versions (Dom Pérignon, Cristal, La Grande Dame...). Tier: LVMH and Pernod Ricard = Global group, all others Independent (no national-champion or craft overview fetched). `own_y` not given by the page. Owner not stated for Delbeck, Pannier, Paul Goerg, Francis Pétret (blank). Gosset's owner kept as the page spells it, "Renaud-Cointreau". Growers' Champagne: not on that page, no section.
- 62 brand-register entries added (49 houses with country and year, 13 owner groups).
- No Champagne market shares by group: two sources failed (403, redirect) and search excerpts are not fetched pages, so department `ms` is unchanged.
- Estate versions, each naming Wikipedia's page: Pomerol (Pétrus, Lafleur, Trotanoy, L'Évangile, La Fleur-Pétrus, Latour à Pomerol, Vieux Château Certan, Le Pin, Certan de May, Clinet, La Conseillante, Clos l'Église, La Fleur-de-Gay, Gazin; from Clive Coates 2001 as quoted there), Châteauneuf-du-Pape (Vieux Télégraphe, Rayas, Beaucastel), Hermitage (Chave, Chapoutier, Jaboulet, Delas). The Gevrey-Chambertin, Meursault and Puligny-Montrachet pages name no estates; Vosne-Romanée and Chablis pages returned 404; no other estates added.
