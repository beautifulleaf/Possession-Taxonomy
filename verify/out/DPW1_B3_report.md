# DPW1_B3: B3 Lighting decision pass

Offline pass over TREE_B3, the memo, HV_B3_1 and the B3 rows in data/ (50 kinds, 681 named forms, 73 lines).

## Missing kinds (6 items, 8 rows)
"Daylight lamp" and "ring lamp" each name two objects, so each has two rows.
- **new_kind 1:** B3.1.3.04 Under-cabinet light (puck or bar). Source: IKEA integrated-lighting page. It is made only for a furniture mount (C12 M(a)) and is rigid, so it is not the strip light.
- **other_category 5:**
  - B4: string lights (K-181), stone lantern (K-116).
  - D4: studio light (K-17), photo ring light (step 24).
  - H2: daylight lamp sold for light therapy (step 2).
- **attribute 1:** a daylight-spectrum task lamp (light colour, C10).
- **covered 1:** a ring-headed work lamp is the desk lamp B3.2.1.02.
- **named_form:** none.

## Named forms (53 flagged)
- **to_line 14:**
  - Families: PH lamps, Mirror Ball, Tolomeo, Lumiere, Nanoleaf Essentials, ColorSource, Selecon Pacific, Radium HRI, GE Mazda, Coleman Lantern.
  - Olight series: ArkPro, Javelot, Warrior X, Array.
- **drop 22:**
  - B4: six stone dōrō, two lava lamps, the candle sconce and three IKEA standing candle lanterns (K-116, K-180).
  - F4: Obon chochin.
  - E4: TLR-8, Valkyrie and Odin (weapon lights, K-162).
  - Not named forms: an alias pair (drop light, torchiere), a restated kind (collapsible chochin), Strauss chandelier, "Philips Sunrise Alarm Clock", and a duplicate ACTIK CORE.
- **move_kind 17:**
  - Nine Adesso floor lamps leave the uplighter kind. "Torchiere" is only the seller's word (R-64).
  - Briloner GRIP and Flos Kelvin LED become desk lamps.
  - Ledlenser NEO5R becomes a headlamp.
  - Five rigid IKEA bars go to B3.1.3.04 once it is attested.

**Follow-ups:**
- Set line_id on the members of PH, Lumiere, PILSKOTT, KABOMBA and SKURUP.
- Add B3.1.3.04 to the MITTLED and KÖLVATTEN lines.
- L-flos-castiglioni groups one designer's work and includes a Stilnovo piece. It should become designer relations (R-24).
- The SureFire M6 Guardian note says weapon-mounted. From memory, unchecked, it is a handheld light, so the note needs a recheck.

## Navigation: shopper path
Lighting is not scene-driven:
- The biggest makers are house and retailer brands: IKEA 103 forms, Lindby 37, Paulmann 22, Lucande 21, Adesso 19.
- Every kind source is a retailer placement page.
- B3 makers carry only two scene tags.
- Memo section 2 makes placement, cap or carry the first choice.

Brand leads only for design classics and torches, which become side tabs.

View sketch (levels 1 > 2 > 3):
1. Ceiling and wall > ceiling / wall / spots, track and cabinet > kinds, then makers
2. Lamps > table and desk / floor / night and wake-up > kinds, then makers
3. Outdoor > lanterns and floodlights / path and post / spike and plinth > kinds
4. Torches and lanterns > hand / head / lanterns / work > brands, then models
5. Bulbs and strips > cap (E27, E14, B22, GU10, G9, from C13) > shape kind
6. Stage > fixture types > makers
7. Shades and parts > part kinds

Side tabs: Design houses (signature pieces, era tags) and Torch makers.

## Rules applied
C2(a)(b)(d), R-70(a) (a series of models is a line), C9, C10, C12, R-58, R-64, R-71, K-17, K-116, K-162, K-180, K-181, B4-O2, memo 9.1–9.13.

## † dependence
- Some moves rest on product facts from my own knowledge, not on the row notes. Recheck each against a fetched page when it is applied:
  - Odin and Valkyrie are weapon lights.
  - NEO5R is a headlamp.
  - Kelvin LED has an arm.
  - The IKEA bars are rigid.
  - ColorSource and Coleman Lantern are families.
- I did not refetch the pages behind the daylight and ring-lamp splits.
- B3.1.3.04 enters the data only when a fetched page shows the type.
