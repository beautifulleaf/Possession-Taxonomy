# DPW1_E1 report: E1 Toys & Games decision pass (wave 3, offline)

Inputs: HV_E1_1 and HV_E1_2 reports, their fetch logs ("gave" column), TREE_E1 and its map, memo sections 13 and 14, 298 E1 named forms, 227 E1 lines, 898 E1 makers (all tied at category level only). No DPMK_1_E1 file exists.

## Task 1: missing kinds (34 items; verify/out/DPW1_E1_kinds.tsv)
- new_kind 8, named_form 12, covered 6, attribute 3, other_category 5.
- New kinds. Next free id under each parent, checked against data/kinds.tsv and the map:
  - E1.4.08 Plastic toy railway (Plarail).
  - E1.7.1.06 Play food or cookware set.
  - E1.7.3.06 Activity table (no source_url).
  - E1.8.08 Sandpit.
  - E1.8.09 Seesaw (no source_url).
  - E1.9.09 Game clock.
  - E1.9.10 Model-railway decoder.
  - E1.9.11 Point motor.
- Named forms:
  - Mancala, Chinese checkers, Halma and ludo go under the boxed board game (precedence 2).
  - Xiangqi goes under the chess set, tagged region CN.
  - Sjoelbak (region NL), bagatelle and pucket go under the dexterity game.
  - Peg solitaire and tangram go under the mechanical puzzle.
  - The mud kitchen goes under the play kitchen.
  - Mini 4WD goes under E1.4.01 as a Tamiya lines row.
- Other categories: kick scooter E2, teether H1, card binder and bulk card storage box B1 (K-9), dress-up clothes A1.

## Task 2: named forms (29 flagged; verify/out/DPW1_E1_moves.tsv)
- to_line 24:
  - Barbie, Ken, Skipper and Licca-chan.
  - Nendoroid, which duplicates its existing lines row.
  - Dunny and Labbit.
  - Five Pop Mart characters, using the existing L-pop-mart-* rows that span E1.1.2.04 and E1.1.3.01.
  - Wacky Wobblers, Head Knockers and Cosbaby.
  - Hubelino Marble Run.
  - Six Scalextric set ranges.
  - Wasgij and Puzzleball.
- drop 5:
  - Royal Bobbles, which is a maker name.
  - Four TCG set names (three Pokémon, one Magic). The memo makes card sets C3 variants.
- No move_kind. The Melissa & Doug salon set stays a play make-up set, because the fetched page calls it pretend makeup.

## Task 3: navigation
I confirm the way in that R-116 set: type of object (play family), with the maker as way in shown as a brand and publisher tab beside it (maker_roles E1 way_in).

The harvested data supports this. The 298 named forms spread over all nine families (games 93, role play and other toys 55, dolls and figures 54, play vehicles 27, play equipment 24). All 898 makers are tied only at category level, so a brand-first page would open on brands that cannot yet be shown under any type. Brand lines cluster in construction (137, mostly LEGO themes) and figures and dolls (66). Those collector shelves are better served by the brand tab and the character and franchise view than by a brand-first root. No country or scene way in fits.

Sketch:
1. Level 1 is the nine groups: Dolls, figures & soft toys; Building & construction; Models, kits & model railways; Play vehicles, RC & ride-ons; Board, card & tabletop games; Puzzles; Pretend play & other toys; Outdoor play equipment; Parts & accessories.
2. Level 2 is the leaves. For example, Games opens on Board games, Card games, Tile & dice, Trading card games, Miniatures games, Table & dexterity, and Casino. Leafless families show their kinds directly.
3. Level 3 is the kinds, for example Chess set, Go set, Mancala-type named forms under Boxed board game, and Game clock in Parts. Under each kind sit named forms grouped by maker or line, with an age-band filter everywhere.
4. Side tabs: brands and publishers; game systems (TCG, Warhammer); characters and franchises.

## Rules applied
C2(a), (b) and (d); R-70(a) (a series covering several models is a lines row); C11 tie-break; S3 and the E1.9 parts rule; K-9; key steps 11 and 18; precedence 2 and 8; memo section 4 (sets and editions are C3 variants); R-58 ids. One reading to check: R-70(a) moves the Ken, Skipper and Licca-chan character ranges to lines, although the memo's older reading kept Blythe as a named form.

## Decisions resting on † claims
- L-jumbo-wasgij: the maker Jumbo is not on the fetched page.
- Seesaw and activity table: the logged page summaries do not show them, so source_url is left empty and they are to be attested in an HV_NK batch.
- The provisional status of go and shogi as kinds is unchanged. Xiangqi and sjoelbak become kinds only if seller categories in two regions show them.
