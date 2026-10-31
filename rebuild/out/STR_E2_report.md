# STR_E2 report (Sports, Fitness & Recreation)

**Counts, before to after:** departments 14 to 12; shelves 51 to 62; kinds 374 to 404; archetypes 632 to 593. Validator: OK (--v3). File 427 KB.

**Category:** `lead` rewritten (equipment organised by object; a pursuit groups kit only where owners shop that way). Added `ax` and a 12-step `key` with a precedence note.

**Departments regrouped:** Team sports split into Team sports (balls, bats and sticks, gloves, ground kit) and Protective gear (by body part: head and neck; torso, arms and hands; hips and legs). Cycling kit became a shelf of Snow, ice & wheels (with skateboards, skates, scooters). Air sports became two shelves of Water, wind & air sports. Athletics & dance and Combat sports merged. Climbing and Fishing re-cut by job; Camping gained Camp living.

**Kinds:** merged HEMA jacket, gloves, chest protector and trousers into the Fencing kinds; renamed HEMA gorget to Fencing gorget and Terminal tackle to Fishing hook (split into hook, float, sinker, swivel and snap); Fingerboard moved to E1 (E2_moves.json). 387 kinds now have hand-written `tt`; the other 17 have no sensible attribute types.
**Added (37, all sourced):** among them Release aid, Billiard ball set, Mölkky set, four ice-fishing kinds, Tricam, Climbing hold, Portaledge, Drysuit, Dive light, Skimboard, Variometer, Pole vault pole, Irish dance shoe, Baseball, Racquetball. New archetypes: Wilson T2000, Spalding Smasher, Head Competition, Yonex R-7, Sherrin football, Mölkky, Tricam. Brands added: Sherrin, Lahden Paikka.

**Generic archetypes demoted to types (41):** lacrosse head and stick forms, surfboard shapes, fencing grips and blades, goalie mask styles, target faces, pup tent, bridge hammock, figure of eight, and similar. List: `rebuild/work/STR_E2/demoted.json`.

**Coverage references (24 Wikipedia pages, fetched):** Exercise machine (cardio, strength), Tennis racket, Golf equipment, Fishing tackle, Ice fishing, Lawn game, Diving equipment, Pole vault, Irish dance and others. Log: `work/STR_E2/sources.tsv`.

**Cross-links (23):** required Hakama to A1, Camp bed to B1, Trail camera to D4, plus E1, E4, G1, A2, B5 and in-category pairs; all targets checked.

**Not done:** no fetched whole-space reference for Strength equipment, Protective gear, Skateboards or Cycling kit (no new kinds added there); medicine ball, battle rope and similar left out as unsourced. Fetches were Wikipedia summaries via WebFetch, so quotes are paraphrases. `mk` of a few older archetypes (Steve Lis, Don Gapen and other individuals) are not in the brand index.
