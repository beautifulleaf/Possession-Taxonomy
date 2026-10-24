# DPW1_A4: decision pass, A4 Bags & Accessories (wave 2, offline)

Inputs: BRIEF.md, CONVENTIONS_v1, memo A4 (§3, §10, §14), D4_residual (R-58, R-70, R-71, R-119, R-121), TREE_A4.md, data rows (71 kinds, all attested; 175 named forms; 6 lines; 158 makers tied at category level), verify/work/HV_A4_1/fetched.tsv. No HV report was saved, so candidates come from the session-7 list (parasol, umbrella types), the harvested "gave" column, memo §3/§10 and the proposals row. Every tree kind is attested, so there are no keep or merge calls.

## Task 1: candidates (39)
new_kind 4 · covered 18 · attribute 12 · named_form 2 · other_category 2.

New kinds (the next free id under each parent, R-58):
- **A4.7.07 Parasol**: a hand-held sun umbrella whose canopy is not made for rain (Kohl's "Sun Parasol", fetched). A UV-coated rain umbrella keeps its mechanism kind and takes the attribute `uv_protection`.
- **A4.7.08 Inverted umbrella**: a double canopy that closes inside out. This is a different mechanism, which is the sub-family axis (besttravelumbrella.com).
- **A4.3.07 Packing cube**: a zipped case for clothes packed inside luggage (Wikipedia Baggage). It is not made for one bag, so it does not go in A4.10.
- **A4.10.04 Luggage tag**: no harvester page for a plain tag, so source_url is left empty. It is attested in HV_A4_NK.

All four go to HV_A4_NK before they enter the data.

Other calls:
- Vented, flat and automatic umbrellas, compact wallets, mini/nano bags, the underseater, the business trolley, and carry positions of holsters and quivers are attributes (C2(b), C6, memo §14 `wheel_count`, `size_class`).
- Folding, compact, golf, stick and bubble umbrellas are already in the tree.
- The gate-check bag goes to G1 (S3: made for a stroller). Clip-on sunglasses go to H2 (memo F30).
- Wallet band and breast wallet become non-maker named forms (A4.5.05, A4.5.03).

## Task 2: named forms (11 flagged)
- **to_line 8.** Samsonite Silhouette (a series running over several generations). Rimowa Original, Classic and Essential (collections that span suitcase and travel trunk; Original Pilot joins L-rimowa-original). Tumi 19 Degree (listed among Tumi's lines by the harvester; holds 19 Degree Aluminum). Fashionable Canes StyleStix, FashionStix and Pearlz (ranges of many cane designs).
- **drop 3.** Rimowa "Cross-body shoulder strap" and LAVA "Purse Organizer Insert" (category names that only restate the kind). "East-west bag" (an orientation attribute).
- **Not flagged.** Scout and Step by Step school-satchel models (one model in many colourways; a set is a bundle variant), Bearpaw quivers and the other Samsonite collections (sizes are attributes, C6). No named form is really a maker.

## Task 3: navigation
**Decision: shopper path, with a house view as the second tab.**
- Seven of the ten sub-families are chosen by function. maker_roles.tsv sets them to "owner only" for A4.7 to A4.10, and the proposals row gives "type of object, grouped by what it carries".
- The harvest holds no A4 scene evidence: 1 stray scene tag, and 158 makers tied only at category level.
- The maker leads only for luxury handbags, small leather goods and sunglasses (Hermès, Louis Vuitton, Chanel, Ray-Ban icon models). That is served by a house tab, not by scenes. The owner's scene-first rule covers scene-driven categories, and A4 is not one.

View:
1. **What do you need to carry?** Luggage & travel · Backpacks & packs · Handbags & shoulder bags · Work cases · Wallets & small leather goods · Sunglasses · Umbrellas, parasols & fans · Baby carriers · Small accessories & bag parts.
2. **Which type?**
   - Luggage: suitcase by `size_class` and shell, trunk, duffels, garment bag, packing cube.
   - Packs: use groups Everyday & school / Travel / Outdoor (memo §14 flag 3).
   - Handbags: by silhouette.
   - Wallets: by format.
   - Sunglasses: by frame shape.
   - Umbrellas: by mechanism.
3. **Which one is best?** Quality markers (fabric, construction, zippers and wheels, warranty), then lines and models: Rimowa, Samsonite and Tumi collections; house → icon models (Birkin, Kelly, 2.55).

Side tab: **By house** (house → its icon models), for handbags, small leather goods and sunglasses.

## Rules applied
C2(a)/(b), C2(d) and R-70(a) (lines), C3, C6, C10 (retail facets), C11, C14, S3, R-58, R-121; memo §14 attributes.

## Decisions resting on † claims (from knowledge, offline)
- Rimowa Original, Classic and Essential each include a trunk model. The harvested pages show Rimowa trunks, but not which collection each belongs to.
- Tumi 19 Degree spans several models.
- The inverted umbrella is sold under its own name in shops. The guide page shows the type, and the NK pass should fetch a shop page.
- The parasol line between "sun only" and "rain and sun" is a definition call. It needs a fetched seller page that shows parasols as their own category.
