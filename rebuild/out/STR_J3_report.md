# STR_J3 report: Dairy, Eggs & Alternatives

**Before to after:** departments 8 to 10 (Cheese split into three by how the curd is made: Fresh, soft & blue; Pressed & hard; Stretched, brined & dried); shelves 26 to 26; kinds 157 to 164; archetypes 435 to 405 (33 demoted, 3 added). Validator: OK.

**Added to the category:** `ax`, a 10-step placement `key` (with precedence note), lead updated for the three cheese departments, `t` and `ax` for every department, `t` for every shelf and `ax` for every shelf over three kinds. Kinds reordered along the shelf axis in Milk, Cream, Fresh cheese, Washed-rind, Fermented drinks, Sheep's-milk and Plant drinks.

**Kinds:** every kind with types now has hand-written `tt` (142 kinds; the rest have no types). No kinds merged. One renamed: Flavoured milk drink to Flavoured milk (`J3_renames.json`). Shelf renamed: Tinned & dried milk to Concentrated & dried milk; Pressed uncooked sheep cheese to Sheep's-milk pressed cheese. Nothing moved out (`J3_moves.json` unchanged).

**Added kinds (all sourced from fetched pages):** Horse, donkey & yak milk; Half-and-half & light cream; Khoa & mawa; Cheese curds; Crescenza & stracchino; Muenster (American); Grain, tuber & fruit drink. Added archetypes: Smen, Shrikhand, Leben.

**Generic archetypes demoted to models in `m` (versions kept):** Greek yoghurt, Labneh, Grain kefir, Cultured and Traditional buttermilk, Kumis, Ryazhenka, Quark, Fromage blanc, Queso fresco / queso blanco, Farmer cheese, Dairy brie, British and Irish farmhouse brie, Dairy camembert, Generic gruyere, Artisan Somerset / Clothbound farmhouse / Creamery block cheddar, Crumbly Lancashire, Washed-curd longhorn Colby, Monterey Jack, Queso ibérico, Mexican manchego, Danish/Swedish/US fontina, Low-moisture mozzarella, Aged and Goat's-milk Gouda, Edam ball, Feta-style white cheese, Hard and Soft chhurpi, Soy tempe, Oat tempeh. Where they described a variant they now also appear as a type.

**Cross-links:** `see` added on 61 kinds, including Pecorino to J7 Pecorino, Plant cream and Coconut drink to J5 Coconut milk and cream, Spreadable butter to J5 Margarine, Yoghurt to J8 Frozen yogurt, Kefir to J9 Water kefir. All targets checked to exist.

**References (Wikipedia, fetched 2026-10-31, logged in work/STR_J3/sources.tsv):** cheese shelves: List of cheeses (read in three chunks; the page is truncated near France) and Types of cheese; Milk shelf, Butter, Concentrated milk: List of dairy products; Cream: Cream; Yoghurt and fermented drinks: List of fermented milk products; Eggs: Eggs as food; Plant drinks and alternatives: Plant milk; Tofu shelf: List of soy-based foods. Baby formula shelf had no reference fetched (three age-based kinds, complete by definition).

**Not done / caveats:** the cheese list could not confirm every regional cheese (WebFetch truncation), so cheese shelf coverage was checked mainly for gaps in kinds, not every PDO. Some `tt` values (for example Gouda age bands, Appenzeller colours) come from the earlier data, not new fetches. No new brands were needed.
