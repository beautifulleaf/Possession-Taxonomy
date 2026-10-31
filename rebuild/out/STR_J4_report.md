# STR_J4 report (J4 Fruit & Vegetables)

**Before → after:** departments 4 → 9; shelves 29 → 32; kinds 200 → 257; archetypes 621 → 540; kinds with grouped types (`tt`) 0 → 93. `validate.py --v3` prints OK.

**Structure:** category `ax` and a 9-step `key` added. Fruit now splits into Temperate fruit, Citrus, Tropical & subtropical fruit (seven shelves by region of origin) and Fruit gifts. Vegetables split into Roots, tubers & bulbs; Fruiting vegetables & pods (by plant family); Brassicas, leaves & stems. Salad & herbs gains Soft-leaved, Woody and Asian & Latin American herb shelves. Mushrooms & sea vegetables is kept. Every department and shelf has `t` and `ax`; shelves of more than three kinds have a kind-ordering axis. Melons and Kiwano moved to Grapes, kiwifruit & melons; Celtuce became a kind under stems.

**Split:** Custard apple → Cherimoya, Atemoya, Sugar apple, Soursop (plus new Pawpaw); Speciality cultivated mushrooms → Shimeji, Enoki, Maitake, Lion's mane, Wood ear, Straw mushroom; King oyster mushroom out of Oyster. Renames in `out/J4_renames.json` (Custard apple → Cherimoya; Speciality cultivated mushrooms → Shimeji). No kind was removed or moved to another category (`J4_moves.json` unchanged).

**Added (about 57 kinds incl. splits), each sourced to a fetched list page:** 13 fruits (e.g. Bilberry, Calamansi, Langsat, Tamarind, Bael, Mamey sapote) from List of culinary fruits; 16 vegetables (e.g. Oca, Yacón, Water chestnut, Drumstick, Tatsoi, Purslane, Heart of palm) from List of vegetables; 10 herbs (e.g. Chervil, Curry leaf, Pandan, Epazote) from List of culinary herbs and spices; mushrooms from the Nutrition Advance list; 6 seaweeds from Wikipedia Edible seaweed.

**Generic archetypes demoted to `m` and `tt`:** colour, form and group labels such as flat peach, cantaloupe, honeydew, dragon fruit colours, cucumber types, cabbage and cauliflower types, pea and bean pod types, lettuce types, chicory forms, basil colours, perilla, and mushroom grades. Celtuce became a kind.

**Cross-links:** required pairs (Prickly pear, Rosemary, Thyme → C3; Arrowhead → E4; Horseradish → J5) plus about 30 within J4 and to J5 dried forms; targets checked against reader files.

**Not done:** no new cultivar archetypes added (no fetched pages for them); radicchio varieties (Chioggia, Treviso) not sourced. Wikipedia list pages are the coverage references; the fruit list was read only to character 100,000 plus a second pass. Firecrawl/Parallel unused. Sources logged in work/STR_J4/sources.tsv.
