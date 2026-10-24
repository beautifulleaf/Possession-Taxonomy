# DPW1_H3 report (H3 Adult Objects, wave-3 decision pass, offline)

Inputs: HV_H3_1 report, its fetch log and rows (57 kinds, 91 named forms, 5 lines, 27 makers in data/), TREE_H3 and map, memo H3 sections 3, 4b, 9, 13 and 14, proposals.tsv H3 row, maker_roles.tsv (owner, provisional). No DPMK_1_H3 file and no H3 groups.tsv rows exist.

## Task 1, missing kinds (15 candidates: 7 from the report, 8 from shop categories in the fetch log)
- new_kind 2, attribute 7, covered 4, other_category 2 (anal douche to H1, Liberator positioning cushions to B2), named_form 0.
- **New kinds** (both on a harvester URL logged full):
  - **H3.1.1.09 Vibrating cushion**: a cushion or pad with a built-in vibrator that the user sits or lies on (Orion Sexmöbel). A cushion that only positions the body stays B2.
  - **H3.5.4.02 Labia spreader**: straps or a frame that hold the labia apart (Orion Ketten und Klemmen).
- Attributes: strap-on dildo (`harness_compatible`, already decided), Pumpdildo (inflatable), clitoral clamp (clamp target; the H3.5.3.05 definition should read "nipples or genitals"), bondage kits (mixed sets, K-1), mini size, app control, glass/metal/stone material.
- Covered: nipple sucker (H3.1.1.08), lay-on vibrator (H3.1.1.02), hogtie (H3.5.1.01), sex position restraint (H3.5.1.07).

## Task 2, named forms (11 flagged of 91)
- drop 10:
  - Hitachi Magic Wand: an alias of Magic Wand Original.
  - Inner Goddess Mini: a size variant.
  - KlicLok: a C13 platform.
  - 7 names that only restate the kind, a material or the set's contents: Love Swing, Sex Swing, Leather Flogger, Furry Handcuffs, Under The Mattress Restraint System, Collar with Nipple Clamps, Double-sided Fucking Machine.
- move_kind 1: Hismith Capsule to H3.1.2.03.
- to_line 0: the 5 harvested lines already hold the multi-kind ranges.
- Maker-level point (not a move): M-fifty-shades-of-grey is a licensed range brand, not a maker. A maker-relations or licensor row is needed when a page names the licensee.

## Task 3, navigation
**Confirmed: by type of product** (R-116, proposals.tsv), with brand as a filter and tab.
- Every harvested retailer tree splits by type first (Orion attested about 35 kinds from its type branches; also Babeland, Passionbugs, Bondara and NLS).
- Makers cluster inside one sub-family: Hismith (machines), TENGA (masturbators), Mystim (e-stim), the doll makers. Only The One, Fifty Shades and Lovense cross groups.
- No scene source was loaded, and the BDSM tag is still provisional. So H3 is not scene-driven, and the owner maker role holds.

View sketch:
1. Level 1, the 8 groups: Vibrators and suction stimulators; Dildos and non-powered insertables; Anal products; Penile products; Restraint, impact and sensation gear; Machines; Dolls and body replicas; Parts and accessories. Beside them: the linked view "Condoms, lubricants and sexual-health products" (H1, H2) and a Brand tab.
2. Level 2, the leaves where they exist:
   - Vibrators: External / Internal / Dual-contact.
   - Penile products: Enclosing / Rings and sleeves / Pumps.
   - Restraint gear: Restraints / Deprivation and gags / Impact and sensation / Chastity and genital restraint / Electro-stimulation.
   - Groups without leaves list their kinds directly (for example dildo, double-ended dildo, dilator, kegel balls, urethral sound).
3. Level 3, kinds, then models filtered by material (`body_safe_class`), size, power and connectivity, for example External → wand, palm, bullet, … vibrating cushion.

## Rules applied
C2(a), (b), (d); C3; C6; C9; C10 rule T and retail facets; C13; K-1 (S3a); K-33; K-81; K-82; H-14; R-58 (next free id: H3.1.1.08 and H3.5.4.01 are the last used); R-70 b (drop restatements); R-116; memo 4b and the section 3 usability rows.

## Decisions resting on † or unverified claims
- **Capsule move**: rests on memo usability row 2 (†). No fetched page shows a C13 connector. If a page shows KlicLok on the Capsule, it goes back to H3.6.01.
- **Not moved**: The Cowgirl Premium and Sit-On-Climaxer may be riding saddle machines, but H3.6.02 is unattested and the harvest page shows no saddle. They should be checked when H3.6.02 is attested.
- **Pocket Rocket** stays a non-maker form, because a Babeland branch holds several makers. The memo's maker-bound, genericised-name call (†) is still open.
- **Magic Wand home** (K-32, maker wording not fetched) stays provisional.
- **Still needing attestation**: H3.4.1.01, H3.5.1.08, H3.5.1.09, H3.5.3.01 and H3.6.02 remain unattested. They and the two new kinds go to an HV_H3_NK batch.
