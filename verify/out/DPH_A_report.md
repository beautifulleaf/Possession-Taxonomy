# DPH_A report: structure points of domain A (A1–A5)

Offline Opus pass under DPH_COMMON: no web, no git, nothing written to data/ or framework/. Outputs in verify/out/DPH_A_*: kinds (7 rows, A1), moves (empty), attributes (67), needs (58), groups_changes (1), scene_changes (72), memo_notes (all five categories).

## Decisions: 26 points

| Code | Points | Decisions |
|---|---|---|
| A1 (built) | 7 | display_only 5, noted 2 |
| A2 | 5 | display_only 2, noted 1, other 2 (load the 63 memo kinds before groups; the default tab is decided, not queued) |
| A3 | 5 | noted 3, display_only 1, other_category 1 (loose diamonds go to F6 as a cross-link) |
| A4 | 4 | new_kind 1, display_only 1, noted 2 |
| A5 | 5 | attribute 2 (design_family; seals as standards), display_only 1, noted 2 |

**New kind** (an A4 build note, not data): School satchel (rigid school backpack) under A4.2, at the next free id. Randoseru becomes a named form; Schulranzen and cartable become aliases; the lycée sac stays under satchel. Provisional: the only evidence is the Markenkoffer School tab and customs heading 4202.

**Merges and splits:** none, and no named form moves. A1 is split for display only: the 69 Traditional & regional dress scenes go into six "Traditional dress:" clusters by dress form. No scene is invented, and nothing is grouped by country. SC-old-money moves to Tailoring & classic. Couture and luxury houses become "Designer houses & couture", shown as the Designer edit. tools/apply_scene_changes.py also expects a DPH_A_scenes.tsv file: give it an empty one.

**Groups:** G-A1-9 is renamed "Workwear and safety". A2 safety footwear (`protection_class`) joins it as a generated cross-link once A2 kinds load. The group plans for A2, A3 and A4 are in the memo notes.

**Attributes:** A1 has 19 (user, denim_oz, selvedge, sanforized, loom_type, fill_power, wool_super_s, membrane, protection_class and others); A2 9, A3 11, A4 14, A5 14.

**Needs:** 34 standards, 14 schemes, 8 grading scales and 2 platforms (Pandora Moments; watch movement calibres).

## Thin evidence (provisional)
- The school satchel kind, and DIN 58124 as its standard.
- The PPE EN/ISO standards, EN ISO 12312-1, ISO 22810, ISO 764, Qualité Fleurier, the Patek Philippe Seal and the Grand Seiko Standard are named from the memos or general knowledge. Each needs a fetched page.
- The fill_power test methods are not attested.
- A5 has no scene domain until a collector community has a fetched definition page. The A2 scene door and the A3 style door wait for sourced tags or scenes.
- Clock calls rest on the memo alone.
- The markers for A4 handbags, umbrellas, baby carriers and sunglasses stay unset; the sunglasses attributes are provisional.
- The jewellery fine/demi-fine/fashion scheme has no attested mapping to tiers.
- Two scene placements are judgement calls: modest fashion with robes; Habesha kemis, Algerian and Kurdish dress under dresses and sets.
