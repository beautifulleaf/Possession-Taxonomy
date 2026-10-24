# DPW1_J4 report (J4 Fruit & Vegetables; offline Opus pass)

Inputs: the COMMON reading list plus J4 rows in data/ (69 kinds, 2,045 named forms, no lines). Fetch logs are lost, so I worked from the report and rows.

## Task 1: missing kinds (15 candidates)
- **new_kind 14** (R-58, next free number under the parent): J4.1.2.05 Apricot; J4.1.3.08 Mandarin [tangerine]; J4.1.3.09 Lime; J4.2.2.03 Cauliflower; J4.2.3.06 Radish; J4.2.4.05 Leek; J4.2.5.10 Okra; J4.2.5.11 Pumpkin and winter squash; J4.2.6.03 Green bean; J4.2.7.04 Rhubarb; J4.4.06 Oyster mushroom; J4.4.07 Enoki; J4.4.08 Morel; J4.4.09 Cep.
- **covered 1:** squash. A hard-rind squash goes to J4.2.5.11, a soft-skinned one to J4.2.5.07 Courgette.

Tree lines to add:
- Rhubarb is tart as sold, so it is a vegetable under stems and shoots (J-9).
- Mandarins other than clementine and satsuma are J4.1.3.08.
- J4.4 now has 9 kinds, so it stays leafless (C5(b)).

## Task 2: named forms (11 of 2,045 flagged)
- **move_kind 4:**
  - Chinese Yali → Asian pear
  - Nagpur and Coorg → Mandarin
  - Ney Poovan → Banana
- **drop 7:**
  - Duplicates: Ya Li, Doyenne du Comice
  - Trade-mark aliases (C9): Jaffa, Sharon fruit
  - Dried products (J5): Peperone crusco, Guajillo
  - Not food: Amflora, an industrial starch potato
- **to_line 0:** Del Monte's "glow" pineapples and NatureSweet's tomatoes each stay inside one kind, so they remain maker-bound named forms (C2(d)).

Open, with no home and so not moved: Pepino melon, Seville orange, Issai (a kiwiberry).

Maker pass: five club cultivars (Zespri RubyRed, Hort16A, EnzaRed, Tasti-Lee, Kumato) lack maker_bound = yes.

## Task 3: navigation, by shopper path
Why:
- There are no scene tags.
- Only 15 named forms are maker-bound (6 makers); 28 makers have only a category-level tie.
- The depth is in cultivars (potato 269, strawberry 159, pear 158, mango 148).
- Retailer trees open with fruit or vegetable, then crop group.

View:
1. **What are you buying?** Fruit; Vegetables; Herbs; Mushrooms & seaweed; Mixed packs. Generated side entries: In season, Organic, Frozen, By tradition.
2. **Which group?** Fruit: Apples & pears, Stone, Citrus, Berries, Grapes & kiwi, Melons, Tropical, Other. Vegetables: Leafy, Cabbage family, Roots, Onions & garlic, Fruiting, Peas & beans, Stems.
3. **Which produce?** Kind pages filter by state, origin, organic; varieties list protected and traditional names first, then club cultivars by maker (C7).

## Rules applied
J-9; memo 4b (citrus by heading, mushrooms by market type); C2(a), C2(b), C2(d); C5(b); C9; JC4 and boundary 1 (dried goes to J5); R-18; R-58; R-96(c).

## Resting on † or unattested claims
- Six new kinds have no URL in the report: apricot, lime, cauliflower, leek, radish, green bean. Each enters only when HV_NK fetches a page showing it.
- From botanical knowledge, not a fetched page: okra as a fruiting vegetable; Nagpur and Coorg as mandarins; Ney Poovan as a dessert banana; Jaffa and Sharon fruit as trade marks; Amflora as industrial; Guajillo and Peperone crusco as dried products.
- Memo-provisional: plantain kind; sea vegetables folded into fungi.
