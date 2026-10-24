# DPW1_E1 report: E1 Toys & Games (wave 3, offline)

No DPMK_1_E1 file exists.

## Task 1: missing kinds (34 items; DPW1_E1_kinds.tsv)
new_kind 8, named_form 12, covered 6, attribute 3, other_category 5.

New kinds (next free id, checked against kinds.tsv and the map):
- E1.4.08 Plastic toy railway
- E1.7.1.06 Play food or cookware set
- E1.7.3.06 Activity table
- E1.8.08 Sandpit
- E1.8.09 Seesaw
- E1.9.09 Game clock
- E1.9.10 Model-railway decoder
- E1.9.11 Point motor

Named forms:
- Under the boxed board game: mancala, Chinese checkers, Halma, ludo.
- Under the chess set: xiangqi (region CN).
- Under the dexterity game: sjoelbak (NL), bagatelle, pucket.
- Under the mechanical puzzle: peg solitaire, tangram.
- Under the play kitchen: mud kitchen.
- Under E1.4.01: Mini 4WD, as a Tamiya lines row.

Other categories: kick scooter E2, teether H1, card binder and bulk card box B1, dress-up clothes A1.

## Task 2: named forms (29 flagged; DPW1_E1_moves.tsv)
to_line 24:
- Dolls: Barbie, Ken, Skipper, Licca-chan.
- Figures: Nendoroid (duplicate of its lines row), Dunny, Labbit, five Pop Mart characters (existing rows).
- Bobbleheads: Wacky Wobblers, Head Knockers, Cosbaby.
- Others: Hubelino Marble Run, six Scalextric set ranges, Wasgij, Puzzleball.

drop 5: Royal Bobbles (a maker name) and four TCG set names, which are C3 variants under memo section 4.

No move_kind.

## Task 3: navigation
I confirm R-116: the way in is by type (play family), with a brand and publisher tab beside it.

The data supports this:
- Named forms span all nine families (games 93, role play 55, dolls and figures 54).
- All 898 makers are tied at category level only. Brand-first would show brands without types.
- Lines cluster in construction (137, LEGO themes) and in figures and dolls (66). The brand tab and character view serve them.

Sketch:
1. **Level 1:** Dolls, figures & soft toys; Building & construction; Models, kits & railways; Play vehicles & ride-ons; Board, card & tabletop games; Puzzles; Pretend play & other toys; Outdoor play equipment; Parts & accessories.
2. **Level 2, the leaves.** For example, under Games: Board, Card, Tile & dice, TCG, Miniatures, Table & dexterity, Casino. Leafless families show kinds.
3. **Level 3, the kinds.** For example Chess set, Go set, Boxed board game. Named forms below by maker or line; age-band filter everywhere.

Side tabs: brands, game systems, characters.

## Rules applied
- C2(a), C2(b), C2(d)
- R-70(a): a series covering several models is a line
- C11 tie-break
- S3 and the E1.9 parts rule
- K-9, key steps 11 and 18, precedence 2 and 8, R-58 ids

Note: R-70(a) moves Ken, Skipper and Licca-chan to lines (the memo kept Blythe a named form).

## Decisions resting on † claims
- L-jumbo-wasgij: Jumbo is not on the fetched page.
- Seesaw and activity table: no page in the logs shows them, so source_url is empty and both go to HV_NK.
- Xiangqi and sjoelbak become kinds only if seller categories in two regions show them.
