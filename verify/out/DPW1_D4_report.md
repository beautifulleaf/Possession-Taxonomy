# DPW1_D4: D4 Cameras & Photography decision pass (offline)

## Task 1: missing kinds (43 items)
Items: the HV_D4 lists, split, plus shop categories from fetched.tsv. No DPMK_1_D4 file. Ids checked against data/kinds.tsv and TREE_D4_map.tsv.

Counts: new_kind 25, covered 8, attribute 6, named_form 4.

**New kinds:**
- D4.1.1.14 Digital back; D4.1.2.09 Panoramic film camera.
- D4.2.14 Extension tube.
- D4.3.2.05 LED tube light; .06 Tungsten light; .07 HMI light.
- D4.3.3.11 Flag or net; .12 Overhead frame; .13 Speed ring.
- D4.4.10 Camera dolly; .11 Slider; .12 Crane or jib; .13 Pedestal or studio column stand; .14 Body-worn support.
- D4.5.07 Black-and-white reversal film.
- D4.6.1.04 Film dryer; D4.6.2.07 Negative carrier; .08 Contact printing frame; D4.6.3.04 Print washer; .05 Print tongs; D4.6.4.03 Thermometer; .04 Graduate.
- D4.7.14 Screen protector; .15 Focusing screen; .16 Dry cabinet.

10 have a logged page that shows the type. The other 15 have an empty source_url and go to HV_NK.

**Other decisions:**
- Named forms: bellows (extension tube); tilt-shift adapter and reverse ring (mount adapter); cucoloris (gobo).
- Attributes: subminiature, underwater, medium-format digital, telephoto, film gauges, legs-only tripods.
- Covered: strip LED, scrim, optical spot, diffusion, enlarger head, body cap (widen the lens cap definition), eyecup, insert bag.

**Flag:** D4.4 now holds 14 kinds, above the "about 12" of C5(b). The build could group static and moving-camera support. Ids unchanged.

## Task 2: named forms (19 of 603 flagged)
- **to_line 17:**
  - Rows repeating a stored line: Land Camera 100 series, Fun Saver, QuickSnap.
  - New lines: Brownie, Nikkormat, Exa, the Variable Prime sets of ARRI, Schneider and ISCO, Pan-Cinor (cine).
  - Jobo 1500 and 2500: tank-and-reel systems over two kinds.
  - Bag ranges: Think Tank Retrospective and DarkLight, Tenba DNA and Roadie, Vanguard VEO (bags and tripods).
- **move_kind 2:** MiNT Instantflex TL70 to D4.1.3.01 (instant precedence); Cooke Varotal III to cine lens.
- **No drops.** Ranges that differ only by size stay named forms with size variants (C3).
- **Open:** four photo-booth rows have brands but maker_bound = no; the ATA line is a whole catalogue.

## Task 3: navigation
Confirms R-116: **type of object** first, system (mount, film format) as filter and side view. Maker role stays owner.
- Every harvested catalogue opens on product type: KEH, B&H, Adorama, Freestyle, MPB, Camera Store.
- 603 named forms over 171 makers and 92 kinds; top maker Godox at 41 (7%, lighting only).
- The By-system view waits for the PF_4 rows.

Sketch:
1. Cameras · Lenses and attachments · Lighting · Support · Film and instant film · Darkroom · Accessories. The intro asks "is a phone enough?" and links to D2.
2. For example, Cameras → Digital · Film · Instant; Lighting → Flash · Continuous · Modifiers · Stands. Lenses, support, film and accessories show kinds directly.
3. For example, Digital → Mirrorless · DSLR · Rangefinder · Compact · Bridge · Camcorder · Cinema · Action · 360 · Pocket gimbal · Trail · Booth · Drone · Digital back.

Then filters (sensor, mount, film format and process, ISO), then maker and model.

## Rules applied
R-58, R-70 a, R-116, R-118 a, R-122 c; C2, C3, C5(b), C10(b), C13, C14(c); D-19, D-20; S3; tree precedence; memo §14.

## † claims
- **Model knowledge, not on a fetched page:** the ranges behind Nikkormat, Exa, Variable Prime, Pan-Cinor, the bags and Jobo; Varotal as a cine zoom.
- **Harvester's word or no page:** the 15 kinds without a URL; HMI's ballast claim (C10(b)).
