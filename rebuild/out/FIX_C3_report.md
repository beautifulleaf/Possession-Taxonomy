# FIX_C3 report

Kinds 229 -> 257; archetypes 824 -> 1429; brands 49 -> 49 (Tantau merged out, Sensi Seeds added). validate.py OK. Backups in work/FIX_C3/bak/.

## Coordinator task (J4 RHS cultivars)
The file holds 453 records, not 461. 445 were adopted with their RHS source; 8 duplicated existing archetypes and were skipped (Stella, Czar, Cambridge Favourite, Symphony, Jonkheer van Tets, White Grape, Connover's Colossal, Gijnlim). They went into existing fruit/seed/plant kinds (Apple tree, Plum tree, Tomato seed, Seed potato, Root & brassica seed and others). 17 new seed kinds were created where the hobby compares cultivars (Cabbage, Cauliflower, Broccoli, Brussels sprout, Carrot, Beetroot, Leek, Onion, Lettuce, Cucumber, Green bean, Broad bean, Sweetcorn, Aubergine, Melon, Celery & fennel seed), plus Oregano & marjoram plant and Medlar tree.

## Findings
- C3-1 partly: added Hellebore, Agapanthus, Auricula, Garden chrysanthemum, Bougainvillea, Mandevilla, Hedging & topiary plant, Tree fern, Hardy palm, Clivia, Fritillaria, Gladiolus, Ranunculus, Freesia (Wikipedia sources). Auricula and chrysanthemum have only the species or no archetypes (groups and cultivars not attested). Dwarf conifer not added (page 404). Society registers not fetched.
- C3-2 partly: added Skunk archetype and Sensi Seeds. Northern Lights, OG Kush and Dutch Passion could not be sourced (no page or 404). Landraces not added.
- C3-3 skipped: a POWO/WFO species register needs a bulk dataset and a new file outside the files I may edit.
- C3-4 done: 87 named cultivars lifted out of the "Other ..." and vague bucket archetypes, buckets removed.
- C3-5 done: bonsai styles moved to the department note; shared seed packet types moved to the seed department note; five Christmas tree kinds merged into one with species as archetypes.
- C3-6 done: roses are now named cultivars; classes are types only.
- C3-7 partly: duplicate tomato and chilli cultivars removed from the plant kinds. Camellia cultivars stay in `m`: the fetched Camellia pages do not name them.
- C3-8 done: Tantau merged into Rosen Tantau.

No moves added (C3_moves.json unchanged).
