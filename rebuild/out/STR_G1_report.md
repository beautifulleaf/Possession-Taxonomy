# STR_G1 Vehicles - structure pass report

**Counts (before -> after):** departments 12 -> 12 · shelves 37 -> 52 · kinds 233 -> 240 · archetypes 851 -> 814 (37 demoted). Category ax and key (12 steps plus precedence) written; lead reworded. Every department and shelf has t and ax; every kind has `tt` (hand-written, no `t` left). Validates OK (--v3).

**Reshaped shelves:** Cars (4 -> 7: Everyday, Luxury, Sports & open, Performance, Off-roaders & pickups, Tiny, Built & custom); Motorcycles (4 -> 6: road, retro, three-wheelers, off-road, scooters, electric); riding gear (2 -> 3, by body part; boot moved out of helmets); Bicycles (6 -> 7, historic cycles split out); Boats (5 -> 7: living afloat and inflatables split from cruisers); Off-road (1 -> 3); Aircraft (3 -> 6); Vehicle care (jacks, stands, hoists moved out of Washing into Lifting & workshop support).

**Merged/renamed (G1_renames.json):** Expandable-end trailer -> Folding camper; Sport utility RV -> Toy hauler.

**Added (sourced, fetched Wikipedia):** Utility coupe (Car body style); Dual-sport motorcycle (Types of motorcycles); Cruiser bicycle (List of bicycle types); Inflatable boat, Drift boat, Ice boat, Airboat, Hovercraft (List of boat types).

**References per space:** Types of motorcycles; List of bicycle types; List of boat types; Car body style; Unicycle (checked, E2 holds Unicycle). Vans, caravans, aircraft, rail, prams and vehicle care were not checked against a whole-space reference (not fetched this session). Heritage streetcar was fetched but trams stay out per the department note.

**Generic archetypes demoted** (versions kept as models in `m`; ranges to `r`): Street rod, Rat rod, Lowrider, Bob-job, Sandrail, Dutch roadster, Longtail, Long John, Sociable, Birch-bark canoe, Dugout canoe, Inflatable tender with outboard, Dutch barge, Hot-air airship, Pump handcar, Coach (to types); ranges to `r`: Pashley traditional roadsters, Dahon, Tern, Bike Friday, Santana tandems, Co-Motion tandems, Burley child trailer, Old Town wood-canvas canoe, Perception kayak, Sea-Doo, Lagoon, Fountaine Pajot, J/Boats racer-cruisers, Turtle Wax, Funco sand cars, Ski-Doo, Arctic Cat, Lynx, Tony Kart, CRG, Birel.

**Cross-links:** `see` on about 90 kinds, all targets checked to exist, including the required Glass cleaner (B6), Headset (D3), Jet (F6), Houseboat (G2), plus E1, E2, C1, C2, C7, C8, A1, A4, D4, H2 and I3 links.

**Not done:** no new kinds for vans, trucks, caravans, aircraft or prams (no reference fetched); archetype Kawasaki KLR650 left under Adventure motorcycle although it is dual-sport; jacks and hoists stay in G1 but may belong in C1. G1_moves.json unchanged; brands file unchanged.
