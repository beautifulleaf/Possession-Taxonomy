# DPH_E report: E1 Toys & Games, E2 Sports, E3 Music, E4 Weapons & Armour

Offline Opus pass (SESSION_7 step 1). None of the four is built (E1 has nodes, no kinds), so DPH_E_kinds.tsv, DPH_E_moves.tsv and DPH_E_groups_changes.tsv hold only their headers. Every decision is a build note in DPH_E_memo_notes.md, which becomes memo section 14.

## Points decided (28)

- E1 (7): 4 attribute, 1 covered, 1 display_only, 1 noted.
- E2 (5): 1 new_kind, 1 split, 1 display_only, 2 noted.
- E3 (7): 2 attribute, 1 named_form, 1 new_kind, 1 other_category, 1 display_only, 1 noted.
- E4 (9): 3 attribute, 1 named_form, 1 covered, 3 other_category, 1 noted.

## New kinds
No ids yet: the builder assigns them under R-58.
- E2 Cardio: spin bike and recumbent exercise bike. The memo's exercise bike becomes upright exercise bike.
- E2, new leaves:
  - Padel: padel racket, padel ball.
  - Pickleball: pickleball paddle, pickleball ball.
  - HEMA: HEMA training sword, HEMA fencing jacket, HEMA protective gloves.
- E3: groovebox. "Keyboard synthesizer" is renamed "synthesizer", with `form_factor` as an attribute.
- E1: none. Diorama kits are covered by E1.3.1.01 with subject "structure, terrain or diorama".

There are no merges.

## Attributes (50 rows)
- **E1 (12).** player_count, playing_time_min and min_age are a partial revision of E-9: genre, mechanic, theme and weight stay out. Also faction and the kit and figure facets.
- **E2 (11).** Fitness-machine, racket, boot, ski and wetsuit specs.
- **E3 (13).** Guitar, synth, keyboard and interface specs; hs_class on kinds.
- **E4 (14).** steel, HRC, blade shape, gut hook, tang, protection_level (both NIJ editions held), bow and firearm specs, quarry size, nihonto period.

## Needs (47 rows)
14 standards (one is a knife-steel reference table), 16 schemes, 4 grading scales and 13 C13 platforms.

Schema calls for the caller:
- Four new `platform_type` values: toy construction or track system; model scale and gauge; card or miniatures game system; module format.
- A C4 subject_type "steel", for the Outdoor Life steel scores.
- A rescoping of the E4 rows in maker_roles.tsv:
  - way in: swords, knives, polearms, historical armour and blade fittings;
  - owner: modern ballistic armour and everything else.

## Other categories
- EDC and bushcraft knives are C1 (K-83). The C decision pass should give C1 kinds for both.
- HEMA trainers are E2.
- Fishing tackle is E2.
- Thomann's non-music shelves go to I1, F1, B3/B4, D3/D4 as cross-links.

## Provisional calls (thin evidence)
- The E-9 revision, and faction treated as a tag.
- The exercise-bike split; the air bike is left as a harvest question.
- The padel, pickleball, HEMA and groovebox kinds.
- Skinning and caping knife as named forms.
- Guitar body designs beyond Thomann's groups.
- Unfetched standard and scale names (EN PPE, ISO 20957, Gunpla, BGG, grading scales).
- HEMA maker reputation, which rests on one source.
- E2 display order, E3 guitar ladder, E4 quality orders (US-heavy vendor evidence).
- The E4 maker-role scopes.
