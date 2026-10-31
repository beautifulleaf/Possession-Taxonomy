# STR_C3 structure report (Plants & Living Cultures)

**Counts, before to after:** departments 11 to 11; shelves 28 to 48; kinds 257 to 312; archetypes 1429 to 1429 (none dropped). Validator: OK.

**Category.** Added `ax` and an 11-step `key` (specific groups before houseplants and garden plants, with a precedence note). Lead kept; it does not conflict with RULES.md.

**Departments and shelves.** Every department has `t` and `ax`; every shelf has `t`, plus `ax` where it holds more than 3 kinds. Shelves now follow one axis per department (growth habit, trap type, crop group, planting material). The old 16-kind garden shrub shelf became Shrubs, Trees and Climbers, and the 2-shelf seeds department became 8 shelves.

**Types.** All 312 kinds now have hand-written `tt` (old flat `t` removed).

**Merged or renamed** (in `C3_renames.json`): Bean & pea seed and Green bean seed to Runner & French bean seed; Root & brassica seed to Radish seed; Celery & fennel seed to Celery, celeriac & fennel seed. Salad & leaf seed kept, narrowed to non-lettuce leaves.

**Archetypes redistributed by their own descriptions (none lost):** cultivars from the dissolved seed kinds went to the new crop kinds (peas, radish, parsnip, turnip, kale, kohlrabi, pak choi, spinach and chard, chicory) or to Lettuce seed and the celery kind. No generic archetypes found.

**Added (57 kinds)**, each sourced to a fetched Wikipedia page. Coverage references: Araceae, Orchidaceae, Carnivorous plant, Succulent plant, Bonsai, Mushroom cultivation, Cut flowers. By department: aroids 4 (Calla lily, Arisaema, Amorphophallus, Homalomena); houseplants 7; orchids 4 (Masdevallia, Bulbophyllum, Catasetum, Lycaste); carnivorous 3; garden 8 (Buddleja to Pansy & viola); herbs and vegetables 9; seeds 9 (Pea, Radish, Parsnip, Turnip & swede, Kale, Kohlrabi, Pak choi, Spinach & chard, Chicory & endive); bonsai 4; cut 3; cultures 6.

**Moved.** Thaumatophyllum moved from climbing to upright aroids. No kinds went to other categories; `C3_moves.json` is unchanged.

**Cross-links.** 40 `see` links, each target checked in the reader files. They include the required pairs: Prickly pear, Salvia, Rosemary and Thyme.

**Not done.** Dried flowers (page 404, no kind added). Some `tt` members rest on general horticultural knowledge, and several garden-plant shelves lack a full-list reference. Archetypes were not re-sourced.
