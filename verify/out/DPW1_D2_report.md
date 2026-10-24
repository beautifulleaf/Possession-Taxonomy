# DPW1_D2 report: D2 Phones, Tablets & Personal Devices

Inputs: as COMMON and W3_ADD. Memo D2 has no section 13, so ids come from TREE_D2_map.tsv. There is no DPMK_1_D2 file and no D2 groups. Maker role: owner only.

## Task 1: missing kinds (13 candidates)
11 come from the harvest list and 2 from the fetch log's "gave" column.
- new_kind 5:
  - D2.1.1.05 Dual-screen smartphone
  - D2.4.3.03 Translator earbuds (the key names translators in D2; form differs from the handheld translator)
  - D2.6.2.03 Satellite hotspot
  - D2.8.14 Smartphone microphone
  - D2.8.15 DECT repeater (source_url empty: attest in HV_NK)
- attribute 7: satellite PTT radio (radio_service), brick, phablet, multi-screen, rollable (form or size), kids smartwatch, kids tablet (user = child).
- other_category 1: cycling computer goes to G1 (S3b).
- named_form 0, covered 0.
Ids are the next free number, checked against data/kinds.tsv and the tree map.

## Task 2: named forms (4 flags)
- to_line 3: mophie Juice Pack (Juice Pack Access should join that line), OtterBox Commuter Series and OtterBox Symmetry Series. Each is a series covering several models (R-70).
- move_kind 1: Kenwood Viking VP8000 moves from D2.2.03 to D2.2.01.
- drop 0.
Noted, not flagged: the HyperJuice puck stand fits D2.8.05 weakly (generic Qi2 pad plus a watch puck), and Sidekick II has the wrong maker (Danger built it, T-Mobile sold it).

## Task 3: navigation
**Confirmed: shopper path, type of object first** (R-116).
- The maker role is owner only, with makers clustered in a few platform houses, so brand is not the way in. There are no scenes.
- Fetched retailer trees open on device type (Coolblue, Harvey Norman, B&H, Garmin).
- Best Buy's second step (iPhone, Android, BlackBerry, Feature phones) makes platform the first filter, with price band beside it.

Sketch:
1. Phones · Tablets · Wearables · E-readers and pocket devices · GPS, trackers and safety · Power banks · Two-way radios and pagers · Accessories.
2. Leaves: Smartphones, Feature, Satellite and Landline phones; Reading and writing, Organisers and PDAs, Language devices; GPS units, Satellite communicators, Trackers. Groups without leaves show their kinds here.
3. Kinds, for example Bar, Keyboard-bar, Flip foldable, Book foldable and Dual-screen smartphones. Models sit below them, grouped by line. Platform and price are filters. A By platform view and a brand tab come second.

## Rules applied
C2(b), C2(d), C3, C6, C10, R-58, R-70, S3 and S3b, D-12, and D2.2 "form, not service".

## Resting on † or unverified claims
- **VP8000 is a handheld:** outside knowledge, not a fetched page. Check before applying.
- **Thin pages:** dual-screen phone (Wikipedia section), DECT repeater (named only as a feature), translator earbuds (the B&H fetch named only handhelds). HV_NK attests all three.
- **Unchanged:** the C10(b) comparison sources for D2.7.02 and D2.6.3.02 are still missing.
