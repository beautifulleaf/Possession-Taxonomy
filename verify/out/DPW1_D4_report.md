# DPW1_D4: D4 Cameras & Photography decision pass (offline)

## Task 1: missing kinds (43 items)
Sources: the two HV_D4 "missing kind?" lists, split into single items, plus shop categories from the fetched.tsv "gave" column. No DPMK_1_D4 file exists. Each id is the next free one under its parent, checked against data/kinds.tsv and TREE_D4_map.tsv.

Counts: new_kind 25, covered 8, attribute 6, named_form 4.

**New kinds:**
- **Cameras:** D4.1.1.14 Digital back; D4.1.2.09 Panoramic film camera (swing-lens or rotating).
- **Lenses:** D4.2.14 Extension tube.
- **Continuous light:** D4.3.2.05 LED tube light; .06 Tungsten light; .07 HMI light.
- **Modifiers:** D4.3.3.11 Flag or net; .12 Overhead frame (butterfly); .13 Speed ring.
- **Support:** D4.4.10 Camera dolly; .11 Camera slider; .12 Camera crane or jib; .13 Camera pedestal or studio column stand; .14 Body-worn camera support.
- **Film:** D4.5.07 Black-and-white reversal film.
- **Darkroom:** D4.6.1.04 Film dryer; D4.6.2.07 Negative carrier; D4.6.2.08 Contact printing frame; D4.6.3.04 Print washer; D4.6.3.05 Print tongs; D4.6.4.03 Darkroom thermometer; D4.6.4.04 Darkroom graduate.
- **Accessories:** D4.7.14 Camera screen protector; D4.7.15 Focusing screen; D4.7.16 Camera dry cabinet.

Ten of these have a logged fetch whose summary shows the type: panoramic, extension tube, tube light, flag, overhead frame, speed ring, body-worn support, print washer, negative carrier and proof printer. The other 15 have an empty source_url and go to HV_NK.

**Named forms, attributes and covered items:**
- Named forms: bellows goes under the extension tube; the tilt-shift adapter and reverse ring go under the mount adapter; the cucoloris goes under the gobo.
- Attributes: subminiature (film format), underwater (setting tag), medium-format digital, telephoto, sheet and cine gauges, and tripod legs sold alone.
- Covered: strip LED, scrim, optical spot, diffusion sheet, enlarger head, body cap (the lens cap definition should be widened to include it), eyecup and insert bag.

**Structure flag:** D4.4 now holds 14 kinds, more than the "about 12" of C5(b). The build may want two display groups there: static support, and moving-camera support (dolly, slider, crane, pedestal, body-worn). The ids stay as they are.

## Task 2: named forms (19 of 603 flagged)
- **to_line (17):**
  - 3 rows repeat a line that is already stored: Land Camera 100 series, Fun Saver and QuickSnap.
  - New lines: Kodak Brownie, Nikon Nikkormat, Ihagee Exa, the three Variable Prime sets (ARRI, Schneider, ISCO) and Pan-Cinor (filed as cine).
  - Jobo 1500 and 2500 are tank-and-reel systems that span two kinds.
  - Bag ranges: Think Tank Retrospective and DarkLight, Tenba DNA and Roadie, Vanguard VEO (bags and tripods).
- **move_kind (2):** the MiNT Instantflex TL70 goes to D4.1.3.01 (instant cameras come first in the precedence), and the Cooke Varotal III goes to the cine lens kind.
- **No drops.** No named form is a maker, a shop, a colourway or a size. Ranges that differ only by size, such as tripod series and Shimoda sizes, stay as named forms with size variants (C3).
- **Not actionable here:**
  - The four photo-booth rows have a brand but carry maker_bound = no.
  - L-ata-photobooths-ata-photo-booth-range is the maker's whole catalogue.

## Task 3: navigation
This confirms R-116: the way in is **type of object**, with the system (mount or film format) as a filter and side view. The maker role stays "owner".
- Every catalogue that was harvested opens on product type: KEH, B&H, Adorama, Freestyle, MPB and Camera Store.
- The 603 named forms spread over 171 makers and 92 kinds. Godox leads with 41 (7%, all lighting), and no maker dominates.
- The By-system view still waits for the PF_4 platform rows.

Sketch:
1. **What are you buying?** Cameras · Lenses and attachments · Lighting · Tripods, gimbals and support · Film and instant film · Darkroom · Camera accessories. The page intro asks "is a phone enough?" and links to D2.
2. **Which family?** For example, Cameras → Digital · Film · Instant; Lighting → Flash · Continuous · Modifiers · Stands. Lenses, support, film and accessories show their kinds directly.
3. **Which type?** For example, Digital → Mirrorless · DSLR · Rangefinder · Compact · Bridge · Camcorder · Cinema · Action · 360 · Pocket gimbal · Trail · Booth · Drone · Digital back.

After that come the filters (sensor format, mount, film format and process, ISO), then the maker and model.

## Rules applied
R-58, R-70 a, R-116, R-118 a, R-122 c; C2(b, d), C3, C5(b), C10(b), C13, C14(c), C16; D-19, D-20; S3; TREE_D4 precedence (instant cameras, cine lens); memo §14.

## † claims
- **Model knowledge, not on a fetched page:**
  - the Nikkormat, Exa, Variable Prime and Pan-Cinor ranges;
  - Varotal as a cine zoom;
  - the bag ranges and Jobo systems spanning several models or kinds.
- **Resting on the harvester's report only:** the 15 new kinds without a URL. The HMI kind's C10(b) claim (it needs a ballast) also waits for attestation.
