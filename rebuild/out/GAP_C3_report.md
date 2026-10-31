# GAP_C3 report: Plants & Living Cultures

Validator: OK (313 kinds, 3,829 archetypes; about 1,500 entries added over the two passes). Backups: rebuild/work/GAP_C3/bak/ and bak2/. Scripts: apply.py, apply2.py. Fetches: 46 of 60 (log: sources.tsv).

## Method
Wikidata SPARQL through WebFetch, one query per genus: every species with an English Wikipedia article, or every cultivar item with one. The Wikidata query URL is each new entry's source. Three-column tables from Wikipedia were used in pass one.

## Closed
- Loose models: none (0 `m`).
- Coverage line on every kind with entries (249 plus one new kind).
- Species added (entries before to after): Philodendron 7 to 111, Anthurium 6 to 196, Hoya 5 to 168, Mammillaria 5 to 85, Echeveria 17 to 41, Haworthia 6 to 71, Monstera 3 to 51, Alocasia 6 to 37, Goeppertia/Calathea 7 to 53, Begonia 4 to 206, Pelargonium 6 to 42, Fuchsia 5 to 57, Hosta 21 to 36, Paeonia 8 to 43, Hydrangea 4 to 53, Clematis 8 to 72, Lavandula 4 to 18, Camellia 1 to 41, Rhododendron 9 to 233, Magnolia 2 to 149, Tulipa 10 to 54, Narcissus 6 to 54, Iris 4 to 247, Dahlia 19 to 27.
- Cultivars added from Wikidata: apple 6, pear 2, plum 2, cherry 6, peach 2, citrus 5, fig, olive, strawberry 2, potato 24, tomato 2, daylily, and a few in Camellia, Clematis, Magnolia, Rhododendron.
- Earlier pass (kept): Astrophytum, Ariocarpus, Clivia, Miltoniopsis, Lithops, Epipremnum, Sarracenia, Heliamphora, Phragmipedium completed to their Wikipedia lists.
- Sections: 39 kinds over 12 entries with mixed name types now have `xg` and `g` (species, hybrid, cultivar or group, form).
- Roses: 235 rose cultivars have Wikidata articles; 57 were new and sit in a new kind "Rose cultivar (class not stated)", because Wikidata gives no class.

## Remaining
- Species without an English Wikipedia article are not listed (Philodendron, Anthurium, Hoya, Begonia, Rhododendron and Iris genera are far larger). No accepted-species register (POWO, WFO) was fetched. Counts are "Covers n", never "Complete", for these kinds.
- Not queried (budget): Citrus species, Acer palmatum (query returned no rows), Hippeastrum, Lilium, Sempervivum cultivars, Camellia/Hosta/Narcissus cultivar sets (Wikidata has only a few), orchid greges, RHS AGM lists.
- Cultivar kinds over 12 entries (tomato, beans, brassica, onion, rose classes, olive, apple) have no section axis in any source read; left unsectioned.
- Wikidata rows were returned through a summariser; large lists could have dropped rows (Hoya and Mammillaria counts matched the Wikidata counts).
- No market facts or roles added; no plant-breeder market list exists in fetched pages. Dried flowers and dwarf conifer not retried. Firecrawl not used.

# Round 3 (34 fetches; total 80 over three rounds incl. one timeout)
Validator: OK (313 kinds, 7,070 archetypes).

## Added (species and hybrids with an English Wikipedia article, from Wikidata, 2026-10-31)
- Succulents and houseplants: Aloe +156, Agave +76, Crassula +59, Dracaena (snake plant) +50, Ficus +232, Peperomia +457, Tillandsia +371, Sempervivum +6.
- Carnivorous: Nepenthes +198, Drosera +157.
- Bulbs and garden: Lilium +71, Hippeastrum +24, Salvia +349, Syringa +13, Buxus +16, Rosa species +125, Citrus species and hybrids +67 (Speciality citrus), Juniperus +66.
- Orchids: Phalaenopsis +70, Cattleya +46, Dendrobium +178, Paphiopedilum +58, Cymbidium +17, Oncidium +56, Vanda +26.
- Fruit and other cultivars, found by Wikidata cultivar-class labels: apple +228 (249 listed), pear +15, plum +2, peach 0 new, citrus (orange, mandarin, citron) +18, cherry +20 (sweet and sour), strawberry +4, tomato +8, olive +2. 56 kinds now carry `xg`/`g` sections.

## Not added, and why
- Ulmus and Acer species: the lists include fossil taxa and the target kinds are bonsai kinds; not added.
- Acer palmatum cultivars: three queries (cultivar rank, cultivar-of, title prefix) returned nothing or timed out. Dionaea has one species (already an entry). Carmona: no rows.
- Apricot, quince, fig, potato, grape, hosta and dahlia cultivar classes: no class label with articles in Wikidata; grape varieties belong with wine in the drinks taxonomy.
- Species without an English Wikipedia article are still not listed; no POWO or WFO register was fetched. Wikidata rows pass through a summariser and may drop rows.
- Cultivar kinds have no section axis in the sources, so apple, pear, cherry and the like stay unsectioned.
