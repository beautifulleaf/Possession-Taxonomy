# DPW1_F3: F3 Coins, Stamps, Medals & Trading Cards decision pass (offline)

## Task 1: missing kinds (40 items)
Inputs: both HV_F3 "missing kind?" lists, split into single items, plus generic types from the fetch logs' "gave" column. There is no DPMK_1_F3 file.

Counts: covered 13, other_category 10, attribute 9, new_kind 6, named_form 2.

**New kinds** (R-58 ids, free in data and the map; every URL logged full):
- F3.5.3.03 Aerogram or letter sheet, lettercards included. Airmail stays a postal_service value (F3-O4).
- F3.5.3.04 Newspaper wrapper.
- F3.5.4.02 Philatelic numismatic cover. It is administration-issued, so it is F3 (K-118).
- F3.4.1.03 Vending or service-machine token (dispenser, parking, car wash, laundry, telephone).
- New leaf F3.4.5 Tokens for admission and record: F3.4.5.01 Admission, attendance or voting token, communion tokens included.
- F3.9.1.03 Coin weight.

**Other categories:**
- E1: arcade tokens, casino chips, play money.
- F4: devotional and luck tokens, religious medals.
- F5: postal orders, travellers cheques, ration coupons, trade vouchers, promissory notes.

**Attributes:**
- Presentation pack, year set and folder are `unit` = set (K-1).
- Postal tax stamp, pane, definitive booklet, medal miniatures, the gavel sounding block, and the sealed card forms (hobby box, blaster, hanger, fat pack).

**Named forms:** Prestige booklet; the USPS Digital Color Postmark first-day cover.

## Task 2: named forms (0 of 71 flagged)
None of the 71 named forms needs an action, so the moves file is header only.
- The 26 Topps Chrome subsets are designs inside one kind, already tied to line L-topps-topps-chrome.
- The bullion designs, British orders and medals, and the holder products are single designs.
- No row is a maker, shop, colourway or size.
- Borderline rows kept: "Topps Chrome Champion Refractors" and "BCW toploaders".

## Task 3: navigation
This confirms R-116: the way in is **by collecting field, then the standing or form of the issue, then the named issue and grade**. The maker role stays "owner".

Evidence from the harvested sources:
- Numista opens on object type, then standing.
- Bullion shops open on bar against coin, then the mint.
- Baldwin and Noonans open medals by purpose; trophy shops open by form.
- The 71 named forms spread over 14 makers. Topps holds 26 of them, all in one line.

Sketch:
1. **Which field?** Coins · Bullion · Banknotes · Stamps and postal items · Trading cards and stickers · Medals, orders and insignia · Tokens and scrip · Trophies and awards · Holders, slabs and mounts.
2. **What standing or form?** For example, Stamps → Adhesive stamps · Stamp units · Postal stationery · Covers · Fiscal labels. Bullion has no leaf, so it opens directly on Bar · Round · Coin.
3. **Which kind?** For example, Postal stationery → Stamped envelope · Postal card · Aerogram or letter sheet · Newspaper wrapper.

After that come issue and grade. There are side tabs for mint or refiner and for card brand. Issuer and era are filters.

## Rules applied
R-58, R-70 a, R-116, R-118 a, R-122 c; C2, C3, C5(d), S3; K-1, K-27, K-107, K-117, K-118, K-120; F-16, F3-O3, F3-O4; memo sections 4, 4b, 9, 14.

## Claims to check
- **My reading of the E1 sentence.** "A token made to be used up in one coin-operated game or machine" is read as game machines only. Vending, parking and car-wash tokens therefore stay F3. This needs confirming at the next key revision.
- **Numista detail.** Dispenser, voting, coin-weight and religious nodes rest on the harvester's summary of the Numista index page.
- **Unattested tree kinds:** Crown of office † and Chain of office †.
