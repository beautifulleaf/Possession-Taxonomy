# V4_J7_WFR report

File: rebuild/out/J7_parts/WFR.json (validates OK: 1 department, 34 kinds, 411 entries; builder and sources in rebuild/work/V4_J7_WFR/).

## Structure
Department "Wine of France" (mode mixed), 11 shelves (regions), 34 kinds (districts or appellation tiers, e.g. "Bordeaux: Left Bank appellations"), entries = appellations.
- Reference: Wikipedia, List of Appellation d'Origine Contrôlée wines (every row, duplicates merged, spellings repaired), plus appellations named in the Languedoc-Roussillon list (Pic Saint-Loup, Terrasses du Larzac, La Clape, Berlou, Roquebrun, Roussillon Villages sub-names) and the vin doux naturel article (Rasteau, Muscat du Cap Corse).
- Versions: 1855 classification (Pauillac, Margaux, Saint-Julien, Saint-Estèphe, Haut-Médoc, Sauternes, Barsac; rank in `d`), Graves 1953/1959 classified estates and Haut-Brion (Pessac-Léognan), Saint-Émilion 2022 premiers grands crus classés A and B (Saint-Émilion Grand Cru), the 17 Champagne grand cru villages (Champagne). Burgundy grands crus are appellations, in a "Grands crus" section.
- Kind `tt`: colour/style and main grapes per kind (grape lists are general knowledge, not page-sourced).
- Languedoc-Roussillon also has an IGP kind (57 zones from the Wikipedia list).
- Department `ms`: three sourced figures from Wikipedia "French wine" (2005 AOC 53.4 %, Vin de Pays 33.9 %; 2007 area 861,075 ha).
- Brands: none added. Moves: none.

## Renames (old kind to new kind)
Bordeaux red blend, Merlot, Sauternes & Barsac, White blend, Pinot Noir, Chardonnay, Crémant, Gamay, Viognier, Cabernet Franc, Chenin Blanc, Melon de Bourgogne, Sauvignon Blanc, Muscat, Savagnin, Altesse, Pétillant naturel, Vin doux naturel, and the four Champagne kinds. Only kinds with a French majority were renamed.

## Not done or not sourced
- Non-French entries that sat in renamed kinds are lost unless the other parts take them: Masseto (Merlot); Central Otago and Willamette Pinot Noir; California Chardonnay; Marlborough Sauvignon Blanc; South African Chenin; Heida (Savagnin); Col Fondo; Gemischter Satz and Edelzwicker (White blend); Sassicaia, Ornellaia, Opus One, Meritage, Ridge Monte Bello (Bordeaux red blend); Cabernet Franc/Merlot models `m` of other countries.
- Mixed kinds left alone (French share at most half): Syrah, Grenache, Rosé, Red blend, Riesling, Pinot Blanc, Pinot Grigio, Gewürztraminer, Late-harvest wine, Regional fortified wine (Pineau des Charentes, Floc de Gascogne, Macvin du Jura have no appellation page fetched). Nothing dropped otherwise.
- Champagne houses and cuvées (Moët, Dom Pérignon etc.) are no longer entries (producers outside a classification); they belong in the brand register if already there.
- Old French entries not in the Wikipedia AOC list were dropped: Pétrus, Le Pin, Domaine Coche-Dury, Domaine Leflaive (producers), Château Cheval Blanc, Cru Bourgeois du Médoc, Beaujolais nouveau, Southern Rhône blend, vin jaune, Vendanges Tardives (styles within appellations).
- That list is dated and incomplete: e.g. Jurançon sec, Muscat d'Alsace sub-names, Floc, Pineau and several newer appellations are absent. Only Languedoc-Roussillon IGPs were found on a fetched list (France has 75 IGPs); other IGPs missing.
- No `role` badges: no fetched page named a top rank for an appellation. No Alsace Grand Cru vineyards or Burgundy premiers crus. Appellation of Graves estates is inferred as Pessac-Léognan; the page names Graves only. Wikipedia region labels kept as given.
- Champagne village districts and premier cru count not on the pages fetched in full (enviedechamp states 44 premier cru communes, 11 Montagne de Reims and 6 Côte des Blancs grand crus; not placed).
