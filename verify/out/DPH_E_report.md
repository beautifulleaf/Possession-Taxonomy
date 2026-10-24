# DPH_E report: E1 Toys & Games, E2 Sports, E3 Music, E4 Weapons & Armour

Offline Opus pass (SESSION_7 step 1; R-116 d, R-118 a). None of the four is built (E1 has nodes and adopted ids but no kinds), so DPH_E_kinds.tsv, DPH_E_moves.tsv and DPH_E_groups_changes.tsv are header-only; every decision is a build note in DPH_E_memo_notes.md (section 14 via tools/append_memo_notes.py).

## Points decided (28)

| Code | attribute | named_form | new_kind | split | covered | other_category | display_only | noted |
|---|---|---|---|---|---|---|---|---|
| E1 | 4 | | | | 1 | | 1 | 1 |
| E2 | | | 1 | 1 | | | 1 | 2 |
| E3 | 2 | 1 | 1 | | | 1 | 1 | 1 |
| E4 | 3 | 1 | | | 1 | 3 | | 1 |

## New kinds (no ids: E2 and E3 trees not built; the builder assigns ids under R-58)
- E2 Cardio: spin bike, recumbent exercise bike (the memo's exercise bike becomes upright exercise bike).
- E2 new leaves Padel (padel racket, padel ball) and Pickleball (pickleball paddle, pickleball ball).
- E2 new leaf HEMA, from E4-3: HEMA training sword, HEMA fencing jacket, HEMA protective gloves.
- E3: groovebox.
- E1 gets no new kind. Diorama kits are E1.3.1.01 with subject "structure, terrain or diorama"; E1.3.2.05 is not widened.

## Splits, merges and renames
- Exercise bike split into three kinds.
- E3 "keyboard synthesizer" renamed "synthesizer", with `form_factor` as an attribute.
- No merges.

## Attributes (50 rows)
- E1 (12): player_count, playing_time_min and min_age, a partial revision of E-9 (genre, mechanic, theme and weight stay in the IE link field); faction; scale; assembly; subject; material; power_type; piece_count; product_form; sales_channel.
- E2 (11): resistance_type, flywheel weight, user weight, racket specs, U-weight, ground code, court surface, ski specs, flex, wetsuit thickness, comfort temperature.
- E3 (13): pickup configuration, string count, scale class, handedness, body wood, sound engine, polyphony, form factor, keys, grand size, interface specs, hs_class (on kinds), country of build (view only).
- E4 (14): steel, HRC, blade shape, gut hook, tang, blade length, handle material, protection_level (both NIJ editions), plate cut, bow specs, firearm specs, muzzle energy, quarry size, nihonto period.

## Needs (47 rows)
- 14 standards, including a knife-steel reference table.
- 16 schemes.
- 4 grading scales.
- 13 C13 platforms.

Schema calls for the caller:
- New `platform_type` values: toy construction or track system; model scale and gauge; card or miniatures game system; module format.
- C4 subject_type "steel", so Outdoor Life steel scores can sit on steel rows.
- A maker_roles.tsv rescoping for E4: way in for swords, knives, polearms, historical armour and blade fittings; owner for modern ballistic armour and the rest.

## Other categories
- EDC and locking pocket knives, and bushcraft knives, go to C1 under K-83. The C decision pass should give C1 kinds for both.
- HEMA trainers go to E2.
- 4komma5's fishing shelf is E2 Angling.
- Thomann's software, sheet-music, lighting and video shelves are I1, F1, B3/B4 and D3/D4, shown as cross-links.

## Provisional calls (thin evidence)
- Partial revision of E-9 (player count, time, age as facets); faction as a franchise-like tag rather than an IE link field.
- Exercise bike split: two retailer guides; air bike left as a harvest question.
- Pickleball and padel kinds: one partial page plus shop shelves.
- HEMA kinds: Academie Duello guide only.
- Groovebox: one guide; desktop module as an attribute.
- Skinning and caping knife as named forms of hunting knife.
- Guitar body designs beyond Thomann's five groups (superstrat, offset, SG, V, Explorer).
- EN PPE standard numbers, ISO 20957, EN ISO 23537, Gunpla grades, BGG rank, TCG and Reverb grading-scale names: from memory or memo, unfetched.
- HEMA maker reputation (one source).
- E2 level-1 display order; E3 guitar ladder; all E4 quality orders (US-heavy, vendor-written).
- E4 maker-role scopes.
