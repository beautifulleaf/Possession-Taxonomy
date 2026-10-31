# STR_C8 report: Building Materials & Hardware

Validate (--v3): OK. File 97 KB to 173 KB.

**Counts before to after:** departments 14 to 11; shelves 35 to 38; kinds 147 to 185; archetypes 120 to 95 (25 demoted or moved, 1 added).

**Structure.** Category `ax` and `key` (11 steps plus precedence note) written. Every department has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than three kinds. All flat types became grouped `tt`. Electrical supplies merged into "Plumbing, drainage & electrical" (axis: what it carries). Fuel and Batteries merged into "Batteries, fuel & firelighting". Shelves regrouped: timber by form, fencing by barrier type, ironmongery by job, fixings by how they hold.

**Split or renamed** (in C8_renames.json): Insulation to Mineral wool insulation (plus Rigid foam, Natural fibre, Loose-fill, Reflective foil); Engineered board to MDF (plus Chipboard, OSB, Hardboard); Screw to Wood screw (plus Drywall, Self-tapping, Machine, Coach); Nail to Wire nail (plus Finishing pin, Clout, Masonry, Ring-shank, Tack); Bolt, nut, washer and rivet to Bolt and nut (plus Washer, Rivet). 

**Added (each sourced from a fetched page):** Engineered structural timber, Cement board, Roofing lead and flashing, İznik tile, Cuerda seca tile, Fence rail, Trellis, Screening roll and hurdle, Chain-link fencing, Shellac, Lining paper, Wallpaper border, Wall mural, Downpipe and rainwater fitting, Cabinet hinge, Cabin hook, Toggle catch, Superglue, Epoxy adhesive, Hot-melt glue stick.

**Generic archetypes demoted to types:** five hinge patterns, lion-head and Hamsa knockers, Cottage latch, Haired lime plaster, Heart pine, Barn wood, Pea gravel, Golden gravel, Welsh slate chippings, Scottish pebbles, Indian sandstone colourways, Sett, Cobblestone, Marabú, Quebracho, Oak and hickory lump, pillow, sawdust and extruded briquettes. Montana GOLD and BLACK moved to `r`. Added archetype: Ogatan.

**Coverage references (Wikipedia, fetched 2026-10-31, one per shelf group):** Engineered wood, Roof shingle, Building insulation materials, Mortar, Tile, Paver, Fence, Wood finishing, Paint, Wallpaper, Piping and plumbing fitting, Electrical cable, Rain gutter, Hinge, Latch, Screw, Nail, Adhesive, List of battery sizes, Charcoal, Firelighter. Logged in work/STR_C8/sources.tsv.

**Cross-links:** Sandpaper to C1 Sanding sheet or disc; Plaster to H2 Plaster; Door bolt to B8 Door bolt; Battery charger to C1 Battery charger; Lump charcoal and Charcoal briquettes to C2 Barbecue fuel. All targets checked.

**Not done:** no moves added. Architectural salvage page was a 404, so salvage and aggregate shelves have no list reference. Pipe-fitting shapes and valve types stay as types of one kind each. New kinds' types come from general knowledge where no fetched page lists them.
