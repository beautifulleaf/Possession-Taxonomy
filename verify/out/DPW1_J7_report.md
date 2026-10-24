# DPW1_J7 report (J7 Wine, Beer & Spirits; offline Opus pass, wave 2)

## Task 1: 68 candidates
new_kind 49 (42 new, 7 failed tree kinds kept), named_form 12, attribute 4, covered 3, other_category 0.

New kinds (R-58):
- Wine: J7.1.1.07–.12 Merlot, Malbec, Zinfandel/Primitivo, Tempranillo, Grenache/Garnacha, Other red blend; J7.1.2.04–.07 Riesling, Chenin Blanc, Gewürztraminer, White blend; J7.1.5.05 Other sparkling; J7.1.6.04 Ice wine, .05 Dried-grape wine; J7.1.7.04 Other fortified.
- Beer (BJCP 2021): J7.2.1.05 German Pils; J7.2.3.02 Weissbier, .03 Witbier; new leaves J7.2.5 Amber lager (Märzen, Vienna), J7.2.6 Bock (Doppelbock), J7.2.7 Pale ale (Best Bitter, American Pale Ale), J7.2.8 IPA (English, American, Hazy, Double), J7.2.9 Porter (English, American), J7.2.10 Stout (Irish, Sweet, Imperial).
- J7.3.1.06 Fruit cider; J7.3.3.02 Fruit mead, .03 Spice mead.
- J7.5.4.02 Distilled and compound gin; J7.5.5.03 Sotol; J7.5.9.04 Absinthe.
- J7.6.08 Nut liqueur, .09 Coffee liqueur, .10 Spiced rum, .11 Flavoured vodka.
- J7.7.05 Radler and shandy.

26 carry a fetched harvester URL; 16 go to HV_J7_NK. All seven failed kinds are kept for HV_J7_NK: maize beer, strong cider, palm wine, futsūshu, cheongju, blended grain whisky, mixed spirits.

Follow-ups:
- J7.5.9.01 drops "absinthe" from its examples.
- J7.7.01 should read "spirit, wine or malt base" (K-24).
- The six beer leaves need node rows.

## Task 2: 41 of 463 flagged
- to_line 34: 26 blended-Scotch and 8 tequila brand rows that only repeat the maker name become brand ranges (R-70).
- drop 1: White Claw Variety #3, a bundle variant.
- move_kind 6:
  - Royal Tokaji Late Harvest → Tokaj
  - TinShing Umeshu → Fruit liqueur
  - Kilbeggan Rye → Pot still
  - Zoumot Arak → Anise spirit
  - Branca Menta → Bitter liqueur
  - Masseto → Merlot (pending)

Maker-pass note: about 70 brand-only rows have maker_bound = no and no maker_id (bourbon, rye, corn, vodka, cachaça, Redbreast, Green Spot, Powers). They can become ranges only once makers exist (C1).

## Task 3: navigation by shopper path
Reasons:
- J7 has no scene tags.
- Shops open by drink family, then style or type (memo §2, proposals.tsv).
- The depth is in named forms under kinds (wine 171, spirits 214).
- The 629 maker ties are category-level only.
- Makers stay the way in at the last step, with a Producers tab.

View:
1. Wine · Beer · Cider & mead · Spirits & liqueurs · Sake & rice wines · Ready-to-drink.
2. Style: red, white, rosé/orange, sparkling, sweet, fortified; lager, wheat, pale ale/IPA, porter/stout; whisky, brandy, rum, gin, agave, vodka, other, liqueurs.
3. Grape, designation or type (Pinot Noir, Champagne, American IPA, Bourbon). Filters: region, age, vintage, price. Then the named best by estate, distillery or bottler.

## Rules
C2(a)–(d), C3, C11, JC1, CV-40, J-16, K-24, K-46, R-58, R-70, R-121, tree precedence, memo §14.

## Resting on † claims
- The BJCP codes and family tags (my own knowledge).
- Masseto being single-variety Merlot.
- Kilbeggan Rye being pot-distilled.
- Sotol shelved with agave spirits.
- The 16 kinds without a URL.
