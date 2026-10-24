# DPW1_J7 report (J7 Wine, Beer & Spirits; offline Opus decision pass, wave 2)

Inputs: BRIEF, CONVENTIONS_v1, memo J7 (with section 14), D4 R-items, TREE_J7, the J7 rows in data/ (87 kinds, 463 named forms, 2 lines, 629 maker ties), and the "gave" column of HV_J7_1 and HV_J7_2.

## Task 1: candidates (68)
- new_kind: 49 (42 new kinds, plus 7 failed tree kinds kept for attestation)
- named_form: 12
- attribute: 4
- covered: 3
- other_category: 0

New kinds (R-58 ids):
- **Wine:** J7.1.1.07 Merlot, .08 Malbec, .09 Zinfandel/Primitivo, .10 Tempranillo, .11 Grenache/Garnacha, .12 Other red blend; J7.1.2.04 Riesling, .05 Chenin Blanc, .06 Gewürztraminer, .07 White blend; J7.1.5.05 Other sparkling wine; J7.1.6.04 Ice wine, .05 Dried-grape wine; J7.1.7.04 Other fortified wine.
- **Beer:** J7.2.1.05 German Pils; J7.2.3.02 Weissbier, .03 Witbier. Six new leaves:
  - J7.2.5 Amber lager: .01 Märzen, .02 Vienna Lager
  - J7.2.6 Bock: .01 Doppelbock
  - J7.2.7 Pale ale: .01 Best Bitter, .02 American Pale Ale
  - J7.2.8 IPA: .01–.04 (English, American, Hazy, Double)
  - J7.2.9 Porter: .01–.02 (English, American)
  - J7.2.10 Stout: .01–.03 (Irish, Sweet, Imperial)
- **Cider and mead:** J7.3.1.06 Fruit cider; J7.3.3.02 Fruit mead, .03 Spice mead.
- **Spirits:** J7.5.4.02 Distilled and compound gin; J7.5.5.03 Sotol; J7.5.9.04 Absinthe.
- **Liqueurs:** J7.6.08 Nut liqueur, .09 Coffee liqueur, .10 Spiced rum, .11 Flavoured vodka. J7.6 now has 11 kinds, still under the 12 that would need a leaf.
- **Ready-to-drink:** J7.7.05 Radler and shandy.

The seven failed tree kinds are all kept and go to HV_J7_NK: maize beer, strong cider, palm wine, futsūshu, cheongju, blended grain whisky and mixed spirits. None is merged.

Source URLs: the 27 kinds that have a harvester URL load at once under apply_dp. These are radler, sotol, absinthe, gin, spiced rum, flavoured vodka, nut liqueur, the two meads and the 17 BJCP beer styles. The other 15 new kinds have no URL and go to HV_J7_NK.

Edits that follow:
- J7.5.9.01 drops "absinthe" from its examples.
- The J7.7.01 definition should read "spirit, wine or malt base", as the J7.7 heading does (K-24).
- The six new beer leaves need node rows (tools/add_leaf_nodes.py).

## Task 2: named forms (41 flagged of 463)
- **to_line 34.** These are 26 blended-Scotch brands and 8 tequila brands whose row only repeats the maker's name. Each brand's bottlings are kept as a range (`L-<maker>-blended-scotch-range` / `-tequila-range`, R-70). Teacher's Highland Cream and Don Julio 1942 are products and stay named forms.
- **drop 1.** White Claw Variety #3 is a bundle variant.
- **move_kind 6:**
  - Royal Tokaji Late Harvest → Tokaj
  - TinShing Umeshu (26%) → Fruit liqueur
  - Kilbeggan Rye (30% rye) → Pot still whisky
  - Zoumot Arak → Anise spirit
  - Branca Menta → Bitter liqueur
  - Masseto → Merlot (pending until Merlot is attested)

Notes for the maker pass (no action here): about 70 brand-only rows have `maker_bound = no` and no maker_id. They are bourbon, rye and corn brands, vodka, cachaça, Redbreast, Green Spot and Powers. They should become makers or ranges once a maker row exists, since a line needs its maker (C1). Age-statement rows (Redbreast 18, Scapa 16) are kept as named forms; the memo (section 8) orders ages inside a named form, which points to a later variant pass.

## Task 3: navigation, by shopper path
Reasons:
- J7 has no scene tags.
- Every shop opens by drink family, then colour, style or spirit type (memo section 2; proposals.tsv).
- The depth sits under kinds: 171 wine and 214 spirit named forms.
- The 629 maker ties are category-level only, so a brand-first page would be a flat list.
- The maker stays the way in at the last step (maker_roles way_in), with a producer tab beside the path.

View sketch:
1. **Wine, beer, cider and mead, spirits and liqueurs, sake and rice wines, or ready-to-drink?** (G-J7-1 to 6)
2. **Which style?** Wine: red, white, rosé and orange, sparkling, sweet, fortified. Beer: lager, wheat, pale ale and IPA, porter and stout, traditional. Spirits: whisky, brandy, rum, gin, agave, vodka, other spirits, liqueurs.
3. **Which grape, designation or type?** This is the kind level: Pinot Noir, Champagne, American IPA, Bourbon. Kind pages filter by region, age, vintage and price. Below them come the named best by estate, house, distillery or bottler. The side tabs are Producers and By origin.

## Rules applied
C2(a)–(d), C3, C11, JC1, the CV-40 designation-kind exception, J-16, K-24, K-46, R-58, R-70, R-121, the tree's precedence rules and the memo's section 14.

## Decisions resting on † claims
- The BJCP 2021 codes and family tags of the 17 beer styles are from my own knowledge.
- Masseto being a single-variety Merlot.
- Kilbeggan Rye being pot-distilled.
- Sotol shelved with the agave spirits.
- The grape, sweet, sparkling, fortified, fruit-cider and coffee-liqueur kinds wait for a seller page.
