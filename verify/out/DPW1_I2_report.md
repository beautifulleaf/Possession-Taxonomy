# DPW1_I2 report: I2 Digital Media & Items (offline decision pass)

## Task 1: missing kinds (25 candidates)
Sources: the HV_I2_1 lists, split into single items, and the shop types in the "gave" column of fetched.tsv. There is no DPMK_1_I2 file, so nothing was skipped.

Result: **covered 16, new_kind 4, other_category 3, attribute 2, named_form 0.**

New kinds take the next free id under their parent (R-58). I checked data/kinds.tsv and TREE_I2_map.tsv; both end at .03 in these leaves.
- **I2.6.2.04 Vehicle skin** (Fortnite car bodies and wheels). The leaf is named for vehicles but had no vehicle kind. Source: the Epic cosmetic-types page.
- **I2.6.5.04 Profile avatar** (Steam Points Shop avatars). Source: Steam partner doc.
- **I2.6.5.05 Avatar frame** (Steam Points Shop). Source: Steam partner doc.
- **I2.6.5.06 Loading screen** (Fortnite). Source: Epic page.

All four source pages were logged as full (Parallel fetches), so none needs an empty source_url. They still go to HV_NK for attestation as rows.

Other calls:
- **other_category, D5:** Fortnite Jam Tracks (songs you play in the rhythm mode) and LEGO Kits (buildable structures). Both are add-ons that change play.
- **other_category, OUT:** .arpa, which nobody can register.
- **attribute (C3 bundle):** the Steam Game Profile bundle and shop skin bundles.
- **covered**, mostly by memo section 13's own lists:
  - Banner, aura and kicks go to I2.6.1.02.
  - CS2 gloves go to I2.6.1.02.
  - Instrument and boost go to I2.6.2.02. Pickaxe, glider and contrail stay together there.
  - Car decal goes to I2.6.2.03.
  - Patch and gun buddy go to I2.6.3.03.
  - Steam chat sticker goes to I2.6.3.04.
  - Mini-profile background and VALORANT player card go to I2.6.5.02.
  - Digital paper and frame or overlay packs go to I2.5.2.03.
  - Social-media template packs go to I2.5.2.01.

## Task 2: named forms (414 reviewed, 11 flagged)
- **move_kind 5:** the CS2 glove finishes (NF-I2.6.2.01-027 to -031) move to I2.6.1.02. Memo section 13 files CS2 Gloves under Avatar accessory.
- **to_line 1:** Noto, which is a superfamily, becomes L-google-noto. This follows memo section 12, which keeps superfamilies as lines rows; the point is still in the owner queue.
- **drop 5:** Poly Haven materials, ambientCG materials, FreePBR, Poly Haven HDRIs and OpenHDRI. These are asset libraries or sites (makers or shops under the owner role), not named products.

Left as they are:
- Formats, TLDs, CS2, Fortnite and VALORANT item designs, sample, MIDI and preset packs, and NFT collections.
- The ERC-1155 game collections (Age of Rust and others). Each is a token collection named after its game, not the game itself.

**Open point, no action:** about 38 VALORANT skins have line_ids that point to store re-run bundles ("Run It Back", "Give Back") rather than design collections (Elderflame, Prime, Oni). A line fix pass should re-point them; I did not do that offline.

## Task 3: navigation
**I confirm R-116's way in: by shopper path, "what will you do with it?"**
- Brand cannot lead. 52 of 414 named forms have no maker, and 49 of 61 makers have only one named form.
- Valve, Riot and Epic hold 274 forms (66 %), all inside I2.6, where the game (C13) is the natural second view.
- No scene membership has been harvested.

View:
1. **Purpose:** Read; Listen; Watch; View and keep images; Create with; Use in a game or platform; Register.
2. **Leaf or kind.** For example, under "Use in a game or platform": character and avatar wear; tools, weapons and vehicles; expression; containers and unlocks; collectibles and profile items. Under "Read": reflowable e-book, fixed-layout, comic or manga.
3. **Named forms**, filtered by rights state and format (media), by game (C13) and rarity tag (items), and by foundry (fonts).

## Rules applied
- C2(a), C2(b) and C2(d), C3 (bundle), and the C13 game rule (I-14).
- The maker role is owner only (maker_roles.tsv), so asset sites are dropped.
- R-58 ids, memo sections 12 to 14, and the D5 boundary sentence (add-ons that change play).

## Decisions resting on a † or unverified claim
None rests on a † kind; all 49 tree kinds are attested. The aura and LEGO-kit calls rest on my reading of what those Fortnite types are, because the fetched page names them without describing them. HV_NK should confirm both.
