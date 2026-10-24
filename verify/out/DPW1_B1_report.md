# DPW1_B1: B1 Furniture & Storage decision pass (offline)

## Task 1: missing kinds (71 items)
Harvest lists split into single items, plus 4 "gave"-column categories; no DPMK_1_B1 file.

Decisions: covered 34, new_kind 17, attribute 13, other_category 5, named_form 2.

**New kinds.** Next free ids (R-58, data and tree map checked); URLs logged full or partial.
- Seating: B1.1.2.07 Chair bed; .08 Slipper chair; B1.1.3.04 Booster seat.
- Beds: B1.2.1.08 Bed frame (the panel bed of memo §4b); .09 Loft bed; .10 Bassinet (cradle); .11 Hammock.
- Tables: B1.3.1.03 Bar table; B1.3.2.05 Game table; B1.3.3.05 Drafting table.
- Storage: B1.4.2.09 Bar cabinet; .10 Shoe cabinet; .11 Storage cabinet.
- Containers: B1.5.1.04 Hanging organiser; B1.5.2.07 Umbrella stand; .08 Clothes rail.
- Division: B1.6.07 Desk screen.

**Other categories:** topper → B2, massage chair → H1, laptop stand → D1 (K-8), ironing center → B6, coin capsule → F3 (S3).

**Named forms:** wing chair, bistro chair.

## Task 2: named forms (24 of 396 flagged)
- **drop 1:** LURÖY under bed slats duplicates the slatted base.
- **move_kind 20:**
  - 12 IKEA bed frames → B1.2.1.08 (pending until it loads);
  - lap tray → lap desk;
  - 4801 and Safari → armchair;
  - IVAR → modular shelving.
- **to_line 3:** Leuchtturm NUMIS, KASKADE and VISTA, which are album ranges (R-70 a).

**Line gaps.** No move action can set a line_id, so these are listed in verify/work/DPW1_B1/line_fixes.tsv:
- Set line_id on 4 rows.
- 6 new IKEA lines (MACKAPÄR, NÄMMARÖ, STEGESUND, STOCKHOLM 2025, TOLKNING, BILLY).
- Kind updates on lines; MALM, BRIMNES, VIHALS, SONGESAND and TONSTAD should list B1.2.1.08.

## Task 3: navigation
This confirms R-116: the way in is **by type of object**, as a shopper path.
- IKEA holds 255 of the 396 named forms; 60 makers in all.
- Every catalogue harvested opens on piece type: IKEA in 15 markets, Google, Wayfair, Chairish, 1stDibs.
- About 50 designer-classic rows are served by the "Design houses & designers" side tab.
- The maker role stays owner.

Sketch:
1. **What piece?** Sofas & armchairs · Chairs, stools & benches · Beds & mattresses · Tables & desks · Storage furniture · Boxes, racks & organisers · Screens, stands & shelters · Replacement parts. Albums are shown apart.
2. **Which family?** For example, Beds & mattresses → Beds & cots · Mattresses (by construction) · Bed bases.
3. **Which type?** For example, Beds & cots → Bed frame, Platform, Bunk, Loft, Daybed, Four-poster, Cot, Bassinet, Camp bed, Playpen, Hammock.

Then named forms; room view generated.

## Rules applied
R-58, R-64, R-70 a, R-116, R-118 a; C2, C3, C6, C11, C15; K-1, K-8, K-9, K-172, K-184, K-190; B-2, B-12, B-14; S3; memo §4b; TREE_B1 precedence.

## † and weak evidence
- **Product knowledge (†):**
  - 4801 and Safari are lounge chairs.
  - IVAR is a system.
  - IKEA frames need a separate base.
  - NUMIS and KASKADE are ranges.
- **Partial Google excerpts:** slipper chair, booster seat, drafting table, game table, umbrella stand.
- **Storage cabinet:** rests on the IKEA "storage cabinets" page by its name alone.
- **HOLMERUD:** left as filed.
