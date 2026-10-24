# DPW1_C6: C6 decision pass

Offline pass over TREE_C6, the memo, HV_C6_1 and the C6 rows in data/: 63 kinds, 248 named forms, 10 lines. The fetch logs are lost, so decisions use the report's URLs and the row notes.

## Missing kinds (24 rows)
- **new_kind 13:**
  - C6.1.3.07 Cassegrain reflector telescope
  - C6.1.6.05 Eye loupe
  - C6.5.1.06–.10: telescope tripod, mount counterweight, tube rings, polar scope, equatorial wedge
  - C6.3.2.08–.13: condenser, autoclave, shaker, rotary evaporator, laminar-flow cabinet, biosafety cabinet
- **named_form 4:**
  - Ritchey-Chrétien and Klevtsov go under C6.1.3.07.
  - Maksutov-Newtonian and Schmidt-Newtonian go under C6.1.3.02.
- **attribute 3:** astrograph, image-stabilised binoculars, rangefinder binoculars.
- **covered 2:** workstation magnifier (C6.1.6.03); flasks (C6.3.1.02–.04).
- **other_category 2:** electronic vision aid goes to H2 (K-38); storm glass goes to B4 (memo 9.10).

## Named forms (9 flagged)
- **to_line 6:**
  - Span two kinds: NexStar SE, ETX, ToupCam, Panthera.
  - Cover several models: Megrez, Televid.
- **drop 1:** Dino-Lite, a brand.
- **move_kind 2:**
  - Star Adventurer moves to the equatorial mount.
  - LumiLoupe moves to the stand magnifier.

A row whose members differ only in size or magnification stays a named form (C3, C2(b)). Only a family of differently named models is a line (R-70(a)).

**Follow-ups:**
- Lines to add, with line_id on the members:
  - FirstLight (Explore Scientific)
  - Tech-Line (Schweizer)
  - the cross-kind Vortex, Nikon, Leupold and Hawke series
- maker_bound fixes:
  - PVS-14 should be "no".
  - Galileoscope should be "yes".
- Rows to recheck:
  - Baader "Planetarium NV 110/220"
  - banjo barometer as aneroid
  - Mobilux and varioPLUS as low-vision aids (H2)

## Navigation: shopper path
C6 is not scene-driven:
- No C6 maker has a scene tag.
- The top makers are generalist and retailer brands: Omegon 19, Celestron 18, Bresser 14, Sky-Watcher 12.
- Every kind source is a retailer category page.
- Memo section 2: buyers choose type, then design, then spec, then maker; use is a second filter.

Brand leads only for alpha binoculars, which become a side tab.

View sketch (levels 1 > 2 > 3):
1. Binoculars > prism design / giant / opera / monocular > series by maker
2. Telescopes > optical design (with solar and smart) > series by maker
3. Mounts & accessories > mounts / tripods and mount parts / eyepieces / filters / cameras > models
4. Spotting, night & thermal > the three kinds > models
5. Microscopes & magnifiers > types / forms / parts > models
6. Weather & air > stations / instruments by quantity / air quality > models
7. Lab > vessels / sample handling > kinds, then makers
8. Science kits > discipline > kits
9. Sky models & solar viewing > kinds > models

Side tabs: scenes (astronomy, birding, home weather, antiques) and alpha binoculars.

## Rules applied
C2(a)(b)(d), C3, C10, R-58, R-70(a), R-71, K-15, K-38, K-148, S3, memo precedence, 9.5, 9.10.

## † dependence
- **New kinds:** each enters the data only on a fetched page (R-70(d)).
- **Moves from my own knowledge, to recheck against a page:**
  - NexStar 4SE is a Maksutov.
  - ETX includes refractors.
  - Panthera DL is digital.
  - Star Adventurer is equatorial.
  - LumiLoupe stands on the object.
  - Televid HD 65 and Televid 82 are separate models.
- **Storm glass:** "gives no reading of any quantity" is unattested.
