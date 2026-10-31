# STR_C2 structure pass: Garden & Grounds

**Before → after:** departments 11 → 11; shelves 29 → 40; kinds 131 → 166; archetypes 210 → 154; kinds with grouped types (`tt`) 0 → 163; cross-links 0 → 53. Validator: OK. Category `ax` and a 11-step `key` added; every department has `t` and `ax`, every shelf `t` (and `ax`).

**Reorganised:** every department's shelves now answer one question (e.g. Lawn care: mowers / edging / treatment; Outdoor cooking: lidded grills / open and portable / ovens / fire and heating / fuel and accessories). Bonsai split into four shelves; Pools gained a cleaning shelf.

**Split / merged / renamed** (all in C2_renames.json): Plant support → Plant stake & cane (+ Trellis, Garden arch & obelisk); Plant tie & label → Plant tie (+ Plant label); Potting compost, soil & mulch → Potting compost (+ Topsoil, Soil improver, Mulch, Grow bag); Bonsai wire & wire cutter → Bonsai wire (+ Bonsai wire cutter); Root hook & rake → Root hook (+ Root rake); Barbecue grill merged into Kettle grill (models carried over). Riding mower split into Riding mower, Lawn tractor, Zero-turn mower (models divided). Garden sieve and Soil test kit moved to Composting & soil testing. No kinds moved to other categories; C2_moves.json unchanged.

**Added (35 kinds), with references:** Lawn tractor, Zero-turn mower (Wikipedia Lawn mower); Lawn sweeper, Powered lawn edger, Pickaxe, Post-hole digger (Wikipedia Garden tool and own pages); bonsai kinds (Wikipedia Bonsai, Bonsai Empire tool guide); Hose nozzle & spray gun (Wikipedia Garden hose); Mulch, Slug pellets (Wikipedia); Window box, Trellis, Garden arch & obelisk; Seed tray, Greenhouse heater, shading, Capillary matting (Gardeners' World); pool ladder, brush, net, vacuum head, thermometer (Inyo Pools category page); Electric grill, Tandoor, Outdoor fireplace, Dakota fire pit (Wikipedia Barbecue grill, Tandoor, Fire pit). Topsoil, Soil improver and Grow bag reuse the old kind's source.

**Generic archetypes demoted to types (56):** e.g. Digging/Border/Transplanting spade, Dutch/Draw/Swan-neck/Oscillating hoe, bow/stone rakes, mattock pick/cutter, serrated sickle, dibbers, bonsai wire/cutter/turntable/root-tool entries, six Tokoname kiln pots (already versions of the Tokoname archetype), upright drum smoker, masonry oven.

**Cross-links:** required pairs done (Pond pump with B10, Insecticide with B8, Barbecue fuel with C8 charcoal); all targets checked to exist.

**Caveats:** Harrod Horticultural pages returned 403, so plant-support and greenhouse shelves were checked against other pages. WebFetch summaries were the fetched evidence. Some types (e.g. Grow tent size) are hand-written from shop practice. Sources: work/STR_C2/sources.tsv.
