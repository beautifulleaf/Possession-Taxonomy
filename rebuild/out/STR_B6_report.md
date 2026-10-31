# STR_B6 report: Cleaning & Laundry

Validated with `validate.py --v3`: OK.

**Counts before to after.** Departments 8 to 8. Shelves 17 to 26. Kinds 76 to 86. Archetypes 12 to 12 (all kept, none added: tier category).

**Category.** Added `ax` and an 8-step `key` with a precedence note. Rewrote `lead` to say "organised by the job the object does". Every department has `t` and `ax`, every shelf has `t`, and every shelf of more than 3 kinds has `ax`. Every kind has a hand-written `tt`; the old flat `t` is gone.

**Regrouped.**
- Vacuums: now shelves Vacuum cleaners, Shop & ash vacuums, Floor washers/carpet/steam cleaners, and Window machines (window vacuum and robot moved in from Mops).
- Mops, brooms & cloths: split by what the tool does to dirt (wet mop, dry sweep, scrub, wipe).
- Cleaning products: split by what is cleaned.
- Washing machines & dryers: split into wash, dry, and both.
- Laundry products: split by "in the wash" versus "after the wash".
- Ironing & drying: split into pressing, drying, and carrying/hand washing.
- Bins: 4 shelves.

**Kinds split.**
- Fabric waterproofing and technical wash became Technical fabric wash and Fabric waterproofer (models and ranges divided between them).
- Dishwasher detergent gave Dishwasher rinse aid and salt.
- Clothes airer gave Washing line.
- Kitchen bin gave Waste-paper basket.

**Kinds added (each with a fetched source).** Hand brush, Metal polish, Laundry bleach and whitener, Laundry starch, Drying cabinet, Flatiron (sad iron).

**Merged, moved, demoted.** None merged or moved; `_moves.json` is unchanged. No archetypes were demoted: the 12 existing ones are real named models (Henry, Hoover Constellation, Rainbow, Hoover Model O, Dyson DC01, Kirby, Vorwerk Kobold, Electrolux Trilobite, Roomba, Dustbuster, Hoover Dustette, Corby trouser press). The old "pedestal and stacking kit" type moved into Washing machine spare parts.

**Coverage references (fetched, one or more per shelf).** The references are Wikipedia pages: Vacuum cleaner, Broom, Mop, Sponge (tool), Cleaning agent, Dishwasher detergent, Washing machine, Clothes dryer, Laundry detergent, Fabric softener, Clothes iron, Clothes line and Waste container. They cover every shelf. Window machines had no dedicated reference and relies on the Vacuum cleaner page. No kinds were skipped for being trade-only (backpack vacuum, floor buffer, skip and dumpster).

**Cross-links.** 24 kinds carry `see` entries, all targets checked to exist. Cross-category links: G1 Glass cleaner, Car vacuum cleaner, Car-wash shampoo, Upholstery and carpet cleaner, Leather cleaner and conditioner; G3 Central vacuum system, Bathroom clothes dryer, Waste disposal unit; A2 Shoe cleaner, Shoe polish and waterproofing; B1 Clothes hanger; B5 Dishwasher; C2 Pressure washer; H3 Toy cleaner. Within B6: Wet mop/Spray mop, Tumble dryer/Drying cabinet, Clothes airer/Washing line, and others.

**Not done.**
- Firecrawl ran out of credit midway, so Dishwasher detergent was checked with WebFetch. It names rinse aid but not dishwasher salt, so salt rests on the page only for the product group.
- H3's kind is "Toy cleaner", not the "Sex-toy cleaner" in STR_SEE.tsv; I linked to the actual name.
- No retailer category page was fetched; all references are Wikipedia.

Files: `work/STR_B6/build.py`, `sources.tsv`, `progress.md`, `bak/`.
