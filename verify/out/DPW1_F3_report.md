# DPW1_F3: F3 Coins, Stamps, Medals & Trading Cards decision pass (offline)

## Task 1: missing kinds (40 items)
The inputs were both HV_F3 "missing kind?" lists, split into single items, plus generic types named in the "gave" column of the fetch logs. There is no DPMK_1_F3 file.

Counts: covered 13, other_category 10, attribute 9, new_kind 6, named_form 2.

**New kinds.** Ids follow R-58 and are free in both data/kinds.tsv and TREE_F3_map.tsv. Every URL is logged as full.
- F3.5.3.03 Aerogram or letter sheet. Lettercards are included. Airmail stays a postal_service value (F3-O4). Source: Sri Lanka Post.
- F3.5.3.04 Newspaper wrapper. Source: Wikipedia, Postal stationery.
- F3.5.4.02 Philatelic numismatic cover. Source: IoM glossary. It is administration-issued, so it is F3 (K-118).
- F3.4.1.03 Vending or service-machine token. It covers dispenser, parking, car-wash, laundry and telephone tokens. Source: Numista.
- New leaf F3.4.5 Tokens for admission and record, holding F3.4.5.01 Admission, attendance or voting token. Communion tokens are included. Source: Numista.
- F3.9.1.03 Coin weight. Source: Numista.

**Other categories:**
- E1: arcade tokens, casino chips, play money.
- F4: devotional and luck tokens (K-117), religious medals (K-107).
- F5: postal orders, travellers cheques, ration coupons, trade vouchers, promissory notes (K-27).

**Attributes:**
- Presentation pack, year set and folder are `unit` = set. K-1 keeps the mint and proof set as the only set kind.
- Postal tax stamp is a postal_service value.
- Pane is a `unit` value.
- Definitive booklet is an issue_class value.
- Medal miniatures is the full-size or miniature attribute.
- The gavel sounding block is part of a set.
- Hobby box, blaster, hanger and fat pack are product_form values.

**Named forms:**
- Prestige booklet, under F3.5.2.02.
- USPS Digital Color Postmark FDC, under F3.5.4.01.

## Task 2: named forms (0 of 71 flagged)
I checked all 71 named forms and none needs an action:
- The 26 Topps Chrome insert, autograph and relic subsets are designs inside one kind, already tied to line L-topps-topps-chrome (C2(d)).
- Bullion coin designs, British orders and medals, and the holder and mount products are single designs or awards.
- No row is a maker, shop, colourway or size.

The moves file is header only.

Borderline rows, kept:
- "Topps Chrome Champion Refractors": refractor is otherwise a parallel (C3), but the checklist lists it as an insert set.
- "BCW toploaders": maker plus kind word, with sizes as variants.

## Task 3: navigation
This confirms R-116: the way in is **by collecting field, then the standing or form of the issue, then the named issue and grade**. The maker role stays "owner".

Evidence from the harvest:
- Numista's tree opens on object type, then standing (circulation, commemorative, non-circulating, emergency, pattern, copies).
- Bullion shops (APMEX, BullionByPost) open on bars against coins, then the mint.
- Baldwin and Noonans open medals by purpose (campaign, long service, gallantry, orders).
- Trophy shops open by form.
- The 71 named forms spread over 14 makers. Topps holds 26, all in one line, so no maker leads the category as a whole.

Sketch:
1. **Which field?** Coins · Bullion · Banknotes and paper money · Stamps and postal items · Trading cards and stickers · Medals, orders and insignia · Tokens and scrip · Trophies and awards · Holders, slabs and mounts.
2. **What standing or form?** For example, Stamps → Adhesive stamps · Stamp units · Postal stationery · Covers · Fiscal labels. Coins → Circulating · Collector · Local and emergency · Copies. Bullion has no leaf, so it goes straight to Bar · Round · Coin.
3. **Which kind?** For example, Postal stationery → Stamped envelope · Postal card · Aerogram or letter sheet · Newspaper wrapper. Bullion coin → Eagle, Maple Leaf, Krugerrand and the other designs.

After that come issue and grade on the field's scale. Side tabs: mint and refiner for bullion, card brand for cards. Issuer, era and theme are filters.

## Rules applied
R-58, R-70 a, R-116, R-118 a, R-122 c; C2(a)(b)(d), C3, C5(d), C11, S3; K-1, K-27, K-107, K-117, K-118, K-120; F-16, F3-O1, F3-O3, F3-O4; memo sections 4, 4b, 9, 14.

## Claims to check († and calls resting on reports)
- **E1 sentence and the service-machine token.** I read "a token made to be used up in one coin-operated game or machine is E1" as meaning game and amusement machines. Vending, parking and car-wash tokens therefore stay in F3. This should be confirmed when key v0.7.x is next revised.
- **Numista nodes known only from the harvester's summary.** The node names for dispenser, voting, coin weight and religious tokens come from the harvester's summary of the Numista index page, not from node pages.
- **Tree kinds still unattested:** F3.6.5.02 Crown of office † and F3.6.5.03 Chain of office †. The chain is shown in use on council pages, but no page shows one sold.
