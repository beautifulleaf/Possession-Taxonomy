# DPH_C report: domain C structure decisions (session 7, R-118 a)

Offline pass over the C structure_flags (split into single points) and the prompt's items. C6 is built (kinds, groups files); C1–C5, C7, C8 get memo notes. No named form moves (moves file header only).

## Counts per category (points decided)
- **C1 (5):** new_kind 1, display_only 2, noted 1, needs 1.
- **C2 (5):** attribute 3, new_kind 1, noted 1.
- **C3 (4):** attribute 1 (place and light tags), new_kind 1, noted 2.
- **C4 (5):** other_category 2 (craft storage B1 by K-172; Hobbies & Games E1, Kids a user tag), new_kind 1 point (3 kit kinds), covered 1 (yarn maker-role row exists), noted 1.
- **C5 (14):** build instruction 1, paper stock as lines plus attribute 1, maker role 1, retailer collections 6 (3 attributes, 3 tags or platform_tags), alias 1, variant 1, attribute 1, new_kind 1.
- **C6 (13 rows):** named_form 1, attribute 4, new_kind 6, noted 2.
- **C7 (5):** other_category 1, display_only 1, covered 2, noted 1.
- **C8 (12):** covered 6, new_kind 2, display_only 1 (clip, with 2 new kinds), attribute 1, noted 2.

## New kinds (17)
- C6, ids issued: C6.1.3.08 Schmidt astrograph; C6.5.1.13 Telescope finder; C6.5.1.14 Barlow lens; C6.5.1.15 Astronomical filter; C6.5.2.04 Microscope objective; C6.5.2.05 Microscope eyepiece. All go to attestation (HV_C6_NK); groups G-C6-8, -12, -13, -22 extended, three renamed.
- C1: C1.4.1.04 Demolition hammer (breaker), the next free id in the frozen section 13 tree; group G-C1-4-1 renamed.
- Build notes (ids at build): C2 garden multi-tool; C3 mushroom grow kit; C4 paint-by-numbers kit, diamond-painting kit, needlecraft kit (each the last kind of its sub-family, leaf 0); C5 label tape cassette (new leaf "For label makers"); C8 dowel, packer (shim), cable clip, pipe clip.

## Merges and splits
None. The Dobsonian stays a non-maker named form (C-18): the same Newtonian tube is sold on several mount types, so C12(a) fails. It gets a `mount` facet and is shown first in the Reflectors group. The C8 "clip" shelf is split by the object held, not made a kind.

## Attributes and needs
37 attribute rows (DPH_C_attributes.tsv), among them C2 lawn_area_suited, hand_size, spare_battery_available; C3 light_need, setting, hardiness_rating; C5 paper_stock and the collection attributes; C6 sold_as, mount, designed_for, area_of_application, objective_class, filter_type; C7 size_class; C8 strength_class and tile ratings. 52 needs rows (DPH_C_needs.tsv): schemes for QS_ (Consumer Reports, CHOICE, Stiftung Warentest, Which?, RHS AGM, Nebraska, BirdForum alpha and others), standards (ASTM D4303, CYC, EN 13300, EN 338, PEI and others) and platforms for PF_ (battery and split-shaft systems, SDS holders under a new "tool-holder system" type, finder shoe, filter and microscope threads, pen cartridges, label tape, hitch categories).

## Maker role
C5: scoped way_in for fountain pens, fountain-pen ink, notebooks, planners and paper stocks. Everything else in C5 stays owner. The proposed row for maker_roles.tsv is in the memo notes; this pass did not write it.

## Provisional calls (thin evidence)
- C6.1.3.08 Schmidt astrograph: from memory; no evidence row names RASA.
- C6 finder and Barlow lens: no evidence URL (memo attestation list only).
- C6 filter, objective, eyepiece: evidence names the parts, not sold apart.
- C1 demolition hammer placed in the hammers leaf, not drills.
- C2 garden multi-tool (B&Q class, memo S3), C3 grow kit (one North Spore facet), C4 kit kinds, C5 label tape, C8 dowel, packer, cable clip and pipe clip: each waits for its page.
- C5 way-in role.
- BirdForum alpha (excerpt only); KWF mark; EN 338, EN 335, DIN 51130, ANSI A326.3 values named from memory; ASTM D4303 from an excerpt.
