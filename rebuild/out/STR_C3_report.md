# STR_C3 structure report (Plants & Living Cultures)

**Counts, before to after:** departments 11 to 11; shelves 28 to 48; kinds 257 to 312; archetypes 1429 to 1429 (none dropped). Validator: OK.

**Category.** Added `ax` and an 11-step `key` (specific groups before houseplants and garden plants, with a precedence note). Lead kept; it does not conflict with RULES.md.

**Departments and shelves.** Every department now has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than 3 kinds.
- Aroids: climbing, upright, tuberous.
- Orchids: single-stem, clump-forming, slipper and jewel.
- Carnivorous plants: four shelves by trap type.
- Garden plants: Shrubs, Trees, Climbers and Perennials split out of one 16-kind shelf.
- Grow your own: orchard, warm-climate, nut, soft fruit, herbs, vegetables.
- Seeds: eight shelves by crop group or planting material.
- Bonsai: conifer, broadleaf, flowering and tropical, miniature plantings.
- Cut flowers: stems, bouquets and wreaths, trees.

**Types.** All 312 kinds now have hand-written `tt` (old flat `t` removed).

**Merged or renamed** (in `C3_renames.json`): Bean & pea seed and Green bean seed to Runner & French bean seed; Root & brassica seed to Radish seed; Celery & fennel seed to Celery, celeriac & fennel seed. Salad & leaf seed kept, narrowed to non-lettuce leaves.

**Archetypes redistributed by their own descriptions (none lost):** peas to Pea seed; radish, parsnip, turnip and swede, kale, kohlrabi and pak choi cultivars to their own new seed kinds; celeriac to the celery kind; lettuces to Lettuce seed; spinach and chard to Spinach & chard seed; radicchio and endive to Chicory & endive seed. No generic archetypes were found; all are named cultivars or species.

**Added (57 kinds)**, each sourced to a fetched Wikipedia page. The coverage references were Araceae (aroids), Orchidaceae, Carnivorous plant (trap types), Succulent plant, Bonsai, Mushroom cultivation and Cut flowers. Coverage for other shelves (garden plants, fruit, vegetables, seeds, bulbs, ferment cultures) comes from the per-kind pages, not a full list.
- Aroids: Homalomena, Calla lily, Arisaema, Amorphophallus.
- Houseplants: Schefflera, Aspidistra, Croton, Money tree, English ivy, Gloxinia, Chinese hibiscus.
- Orchids: Masdevallia, Bulbophyllum, Catasetum, Lycaste.
- Carnivorous: Waterwheel plant, Dewy pine, Corkscrew plant.
- Garden: Buddleja, Viburnum, Hebe, Lupin, Phlox, Echinacea, Marigold, Pansy & viola.
- Grow your own: Sage, Parsley plant, Chives plant, Coriander plant, Courgette & squash plant, Cucumber plant, Aubergine plant, Globe artichoke plant, Avocado tree.
- Seeds: Pea, Radish, Parsnip, Turnip & swede, Kale, Kohlrabi, Pak choi, Spinach & chard, Chicory & endive.
- Bonsai: Cypress & cedar, Hornbeam, Kusamono, Saikei.
- Cut: Cut gerbera, Cut alstroemeria, Cut foliage.
- Cultures: King oyster, Enoki and Shimeji spawn; Tempeh starter, Natto starter, Cheese starter culture.

**Moved.** Thaumatophyllum moved from climbing to upright aroids. No kinds went to other categories; `C3_moves.json` is unchanged.

**Cross-links.** 40 `see` links, each target checked in the reader files. They include the required pairs: Prickly pear, Salvia, Rosemary and Thyme.

**Not done.** Dried flowers (Wikipedia 404, so no kind added). Several `tt` members, such as bulb sale forms and seed types, rest on general horticultural knowledge rather than a fetched page. Archetypes were not re-sourced. Several garden-plant kinds were added without a page listing the whole shelf.
