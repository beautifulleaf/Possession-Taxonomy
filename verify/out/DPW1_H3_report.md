# DPW1_H3 report (H3 Adult Objects, offline)

Inputs: HV_H3_1 report, fetch log and rows (57 kinds, 91 named forms, 5 lines), TREE_H3 and map, memo sections 3, 4b, 9, 14, proposals.tsv, maker_roles.tsv (owner). No DPMK_1_H3 file or H3 groups.tsv rows exist.

## Task 1, missing kinds (15 candidates: 7 from the report, 8 from shop categories in the fetch log)
- Counts: new_kind 2, attribute 7, covered 4, other_category 2, named_form 0.
- New kinds, both on harvester URLs logged full:
  - **H3.1.1.09 Vibrating cushion**: a cushion with a built-in vibrator, sat or lain on (Orion Sexmöbel). A cushion that only positions the body stays B2.
  - **H3.5.4.02 Labia spreader**: holds the labia apart (Orion Ketten und Klemmen).
- Attributes:
  - strap-on dildo (`harness_compatible`, already decided)
  - Pumpdildo (inflatable)
  - clitoral clamp (the target of a clamp; widen the H3.5.3.05 definition to "nipples or genitals")
  - bondage kits (mixed sets, K-1)
  - mini (a size), app (control mode), glass (a material)
- Covered: nipple sucker H3.1.1.08, lay-on vibrator H3.1.1.02, hogtie H3.5.1.01, position restraint H3.5.1.07.
- Other category: anal douche → H1 (K-33); Liberator positioning cushions → B2 (K-82).

## Task 2, named forms (11 of 91 flagged)
- Drop (10):
  - Hitachi Magic Wand: an alias of Magic Wand Original.
  - Inner Goddess Mini: a size variant.
  - KlicLok: a C13 platform row.
  - Seven names that only restate the kind, a material or the set's contents: Love Swing, Sex Swing, Leather Flogger, Furry Handcuffs, Under The Mattress Restraint System, Collar with Nipple Clamps, Double-sided Fucking Machine.
- move_kind (1): Hismith Capsule → H3.1.2.03.
- to_line: none. The existing lines already hold the multi-kind ranges.
- Maker point, outside the moves file: M-fifty-shades-of-grey is a licensed range, not a maker. It needs a licensor or licensee row once a page names one.

## Task 3, navigation
**Confirmed: by type of product** (R-116), with brand as a filter and tab.
- Every harvested retailer tree splits by type first (Orion alone attested about 35 kinds; Babeland, Passionbugs, Bondara and NLS do the same).
- Makers cluster inside one group (Hismith, TENGA, Mystim, the doll makers). Only The One, Fifty Shades and Lovense cross groups.
- No scene source was loaded, so H3 is not scene-driven.

Sketch:
1. **Level 1**: 8 groups (Vibrators and suction stimulators; Dildos and non-powered insertables; Anal products; Penile products; Restraint, impact and sensation gear; Machines; Dolls and body replicas; Parts and accessories). Beside them sit a Brand tab and the linked view "Condoms, lubricants and sexual-health products".
2. **Level 2**:
   - Vibrators: External / Internal / Dual-contact.
   - Penile products: Enclosing / Rings and sleeves / Pumps.
   - Restraint gear: Restraints / Deprivation and gags / Impact and sensation / Chastity and genital restraint / Electro-stimulation.
   - The other groups list their kinds directly.
3. **Level 3**: kinds (for example External: wand, palm, bullet … vibrating cushion), then models filtered by material (`body_safe_class`), size, power and connectivity.

## Rules applied
C2(a)(b)(d), C3, C6, C9, C10 (rule T and retail facets), C13, K-1, K-33, K-81, K-82, R-58 (the last ids used were H3.1.1.08 and H3.5.4.01), R-70 b, R-116, memo 4b.

## Calls resting on † claims
- **Capsule**: memo usability row 2 (†). No fetched page shows a C13 connector. It goes back to H3.6.01 if a page shows KlicLok on it.
- **Not moved**: The Cowgirl Premium and Sit-On-Climaxer may be riding saddle machines, but H3.6.02 is unattested and the harvest page shows no saddle.
- **Kept as they are**: Pocket Rocket stays a non-maker form (a Babeland branch spans several makers). The memo's maker-bound call (†) is still open. The Magic Wand home (K-32) stays provisional.
- **Still unattested**: H3.4.1.01, H3.5.1.08, H3.5.1.09, H3.5.3.01 and H3.6.02. They go with the two new kinds to an HV_H3_NK batch.
