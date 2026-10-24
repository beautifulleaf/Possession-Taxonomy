# DPH_A report: structure points of domain A (A1–A5)

Offline Opus pass under DPH_COMMON. No web, no git, nothing written to data/ or framework/. Outputs are in verify/out/: DPH_A_kinds.tsv (A1, 7 rows), DPH_A_moves.tsv (header only), DPH_A_attributes.tsv (67), DPH_A_needs.tsv (58), DPH_A_groups_changes.tsv (1), DPH_A_scene_changes.tsv (72) and DPH_A_memo_notes.md (all five categories).

## Decisions: 26 points

| Code | Points | Decisions |
|---|---|---|
| A1 (built) | 7 | display_only 5, noted 2 |
| A2 | 5 | display_only 2, noted 1, other 2 (load the 63 memo kinds before groups; the default tab is decided, not queued) |
| A3 | 5 | noted 3, display_only 1, other_category 1 (loose diamonds go to F6 as a cross-link) |
| A4 | 4 | new_kind 1 (school bag), display_only 1, noted 2 |
| A5 | 5 | attribute 2 (design_family; seals as standards), display_only 1, noted 2 |

**New kinds:** one, for the A4 build (not data): **School satchel (rigid school backpack)** under A4.2, taking the next free id there. Randoseru becomes a non-maker named form; Schulranzen and cartable become aliases; the lycée sac stays under satchel. **Provisional:** the only evidence is the Markenkoffer "School" tab plus customs heading 4202. A fetched page must show rigid school satchels sold as their own category.

**Merges and splits:** none, and no named form moves. A1 is split only for display: the Traditional & regional dress cluster's 69 scenes go into six "Traditional dress:" clusters by dress form (draped and wrapped; kimono, robes and over-garments; dresses, suits and sets; shirts and tunics; handwoven, printed and embroidered cloth; folk costume and heritage revival). No scene is invented or merged, and nothing is grouped by country.

**Other scene changes:** SC-old-money moves to Tailoring & classic. Couture and luxury houses move to "Designer houses & couture", which the page shows as the Designer edit beside the genre door. Apply with tools/apply_scene_changes.py. That needs an empty DPH_A_scenes.tsv, or a version of the tool that runs the changes file alone.

**Display groups:** G-A1-9 is renamed "Workwear and safety". A2 safety footwear (named forms with `protection_class`) joins as a generated cross-link once A2 kinds load. The A2 (boots by style; lifestyle against performance), A3 (shop names for the piece types; body chains) and A4 (use groups) plans are in the memo notes, because groups.tsv can only hold loaded kinds.

**Attributes:** A1 has 19, including user (for the department toggle), denim_oz, selvedge, sanforized, loom_type, fill_power, fill_type, wool_super_s, membrane and protection_class. The memo's hazard_rating is renamed to match A2. A2 has 9, A3 11, A4 14 and A5 14 (design_family is the watch-family door). The value lists come from memos and fetched evidence; the rows are filled later from sources.

**Needs:** 35 standards (GOTS, OEKO-TEX, the PPE EN/ISO set, EN ISO 20345, hallmarking, DIN 58124, COSC, METAS, the Geneva Seal, maker-owned seals and others), 14 schemes, 8 grading scales and 2 platforms (Pandora Moments; watch movement calibres).

## Thin evidence (provisional calls)
- The school satchel kind (above), and DIN 58124 as its standard.
- The PPE standards for A1 and EN ISO 12312-1, ISO 22810, ISO 764, Qualité Fleurier, the Patek Philippe Seal and the Grand Seiko Standard come from the memos or general knowledge, not from fetched pages. Each must be fetched before it enters.
- fill_power test methods (IDFB, EN 12130) are not attested.
- No A5 scene domain: the watch families stay design_family values and maker classes until a collector community has a fetched definition page.
- The A2 scene door waits for A2-specific maker tags. The A3 style door stays off until an A3 scene has a defining page.
- Clock calls rest on the memo alone (no HOL_EV clock evidence).
- The A4 handbag, umbrella, baby-carrier and sunglasses markers stay unset. The sunglasses attributes are provisional.
- The fine/demi-fine/fashion jewellery scheme lacks its attribute-to-tier mapping.
- Two scene placements are judgement calls: modest fashion with robes (it is a contemporary industry, not traditional dress), and Habesha kemis, Algerian couture and Kurdish dress under dresses and sets.
