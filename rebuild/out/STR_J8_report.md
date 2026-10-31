# STR_J8 report: Bakery, Sweets & Snacks

validate.py --v3 prints OK (141 kinds, 509 archetypes, file 356 KB).

**Counts before to after:** departments 7 to 7; shelves 11 to 24; kinds 123 to 141; archetypes 524 to 509 (15 demoted to ranges or models net of 29 added).

**Category:** wrote `ax` and a 7-step placement `key` with a precedence note. Lead unchanged (it already respects the object rule).

**Shelves regrouped, each with one stated axis:**
- Bread & bakery: Loaves; Rolls, flatbreads & enriched breads; Pastries; Festive & spiced bakes; Cakes.
- Biscuits: unchanged two shelves, reordered.
- Chocolate: Bars & blocks; Filled pieces & boxes; Countlines & bars; Seasonal & novelty chocolate.
- Sweets: Hard, fizzy & novelty; Soft & chewy; World confectionery traditions (now ordered by main ingredient).
- Crisps: Potato crisps; Corn snacks; Baked & puffed snacks; Meat, seaweed & spiced snacks.
- Nuts & bars: Bars; Plain nuts; Seasoned nuts & mixes (22 kinds had been one flat shelf).
- Ice cream: Tubs & scoop; Water ices; Single-serve & shaped.

**Merged or renamed** (in J8_renames.json): Gluten-free bread into Sliced & tin loaf; Dairy-free ice cream into Ice cream tub (models and archetypes carried over); Countline & chocolate bar snack to Countline; Cone to Ice cream cone.

**Added kinds (18, all sourced and with archetypes):** Quick bread & cornbread, English muffin & crumpet, Puff pastry, Choux pastry, Turnover & strudel, Tart & shortcrust pastry, Cupcake & muffin, Madeleine & financier, Loaf & Bundt cake, Cheesecake, Cheese cracker, Graham cracker, Oyster & animal cracker, Aerated chocolate bar, Coconut bar, Candy floss, Novelty sweets, Fruit snack, Frozen custard, Shaved ice.

**Reference per shelf (fetched Wikipedia lists):** breads (Loaves, Rolls); pastries (Pastries); cakes (Cakes); cookies (Sweet biscuits); crackers (Crackers); chocolate bar brands (all Chocolate shelves); confectionery brands (Sweets); frozen desserts (Ice cream); snack foods (Crisps, Nuts & bars, no new kinds found: the fetched page was truncated before its savoury section).

**Types:** every kind now has `tt` written by hand, with one question per group. Old flat `t` removed.

**Archetypes demoted (63 entries):** 25 generic ones (Birthday cake, Pork rinds, Chocolate bunny and similar) went to models in `m` with their versions; 38 maker ranges (single-origin bar ranges, crisp brands, Ben & Jerry's pints, crispbread brands and similar) went to `r`, versions to `m`. Soda bread, Fortune cookie and Pez were moved to better kinds.

**Cross-links:** 30 `see` entries, targets checked (J5 Hazelnut-chocolate spread, Granola, Popcorn kernels, Dried seaweed, Cake and baking mixes, Ready-made pastry; J6 Drinking chocolate, Cocoa powder; the rest within J8). STR_SEE.tsv has no J8 row.

**Not done:** no moves file entries (nothing left the category); new archetypes have no maker or year where the fetched list did not give one; Nuts & bars is a tier department so no archetypes were added there.

Backups: work/STR_J8/bak/. Build script: work/STR_J8/build.py.
