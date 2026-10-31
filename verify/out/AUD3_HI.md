# AUD3_HI — cold audit: H1 H2 H3 H4 I1 I2 I3

Auditor: cold (Opus), 2026-10-28. Inputs: rebuild/reader/<CODE>.json, brands/<CODE>.json, traditions/<CODE>.json. All counts were computed from the JSON with helper scripts in verify/work/AUD3_HI/. A fact marked "to verify" comes from my own knowledge and has not been checked.

---

## H1 Personal care

**Brand mode:** mixed. Tier for everyday basics, oral care, hair removal and appliances; variety for wet shaving, K-beauty and J-beauty, icon make-up and nail polish.

The file has 153 kinds and 349 archetypes, 195 of which have versions. The brand register holds 1,026 brands. Only 307 of them are linked to an item, and 785 have no lines and no signature archetypes.

**Gaps for hobbyists**
- **H1-1 Clippers and electric shavers have no archetypes.** Hair clipper (9 m), Electric shaver (11 m) and Beard trimmer (11 m) have x=0. Barbering and vintage-shaver enthusiasts recognise named families: Wahl Magic Clip, Andis Master, Oster Classic 76, Braun Series and Sixtant, Philips/Norelco rotary, Panasonic Arc (to verify). **Fix:** promote those m entries to archetypes, with generations as versions.
- **H1-2 Nail polish is thin for a collecting community.** It has 8 archetypes but 16 `t`, so finish types carry the structure. Indie polish is a real collecting scene. **Fix:** add archetype lines (for example OPI collections and Essie icon shades) and give indie makers register entries (to verify).
- **H1-3 Archetype–register mismatches.** Three archetypes have an empty `mk` although the brand is in the register: Clinique Almost Lipstick Black Honey, Maybelline SuperStay Matte Ink and Laneige Lip Sleeping Mask. Another 14 makers used as `mk` are missing from the register (Parker, Omega, Williams, Astra, Trim, Nizoral and others). **Fix:** fill `mk` and add the missing register entries.

**Too much detail**
- **H1-4 SKU lists without archetypes.** Examples: Styling cream (8 m, x=0), Heat protectant (7 m), Face powder (6 m) and Lip liner (7 m). Period underwear lists "Period underwear" three times and Menstrual cup lists "Period cup" twice. **Fix:** cut each to 5–8 market-covering or test-winner makers and remove the duplicates.
- **H1-5 Near-duplicate kinds:** Scalp scrub / Scalp treatment, Pimple patch / Acne spot treatment, Hair mousse / Volumising spray. **Fix:** merge each pair and keep the variants as `t`.
- **H1-6 Brand register bloat.** 719 of the 1,026 brands are unlinked. In a mostly tier category this works as a retail directory. **Fix:** keep linked brands, test winners and variety-area brands; drop the rest or reduce them to stubs.

**Confusing organisation**
- **H1-7 Orphan department and bare kinds.** The department "Hair care tools & accessories" holds a single kind, Hair towel; it belongs in Hair › Brushes & accessories. Changing mat, Baby bath, Potty, Toilet-training seat, Dummy and Anal douche are bare (no t, m or x). Baby care is a view, not a shelf. **Fix:** move the nursery items to the Home or Baby view by tag, and give Anal douche `t` or merge it into Intimate care.
- **H1-8 Duplicate archetypes across kinds.** Eight Hour Cream sits under both Body lotion and Lip balm, and Kajal under both Eyeliner and Kohl & surma. **Fix:** keep one home for each and cross-link.
- **H1-9 Overlap with H2 and H3.** Hot-water bottle and Heat pack (H1) duplicate Heat & cold pack (H2). Personal lubricant sits in H1 while condoms are in H2 and toys in H3. **Fix:** assign one owner for each kind.

**What it would look like (Shaving › Electric shavers & clippers)**
```
Hair clipper (kind)
├─ Oster Classic 76 [Oster] — 1950s–; v: Classic 76, 76 Turbo  (to verify)
├─ Andis Master [Andis] — v: Master, Master Cordless
├─ Wahl Magic Clip [Wahl] — v: corded, cordless, 5 Star line
└─ dt: motor (magnetic/pivot/rotary) · blade · guards
Electric shaver (kind)
├─ Braun Sixtant → Series 9 [Braun] — foil lineage
└─ Philips/Norelco rotary [Philips] — v: Series 9000, S9000 Prestige
```
**Priority:** medium · **Fix size:** medium

---

## H2 Health & medical

**Brand mode:** tier throughout. The two exceptions are low-vision and Braille aids, which have one archetype each. The file has 174 kinds, 2 archetypes and a register of 191 brands (188 linked). The traditions view lists 5 healing traditions.

**Gaps for hobbyists**
- **H2-1 Walking sticks as collectibles are absent everywhere.** A grep of all reader files finds only H2 "Walking stick" (8 t, 4 m), filed as a mobility aid. Antique, system and gadget canes are an established collecting field, as are Malacca and silver-topped sticks. Swaine Adeney Brigg and Fayet are known makers (to verify). **Fix:** add a "Canes & walking sticks" kind with archetypes, in A-domain accessories or here with a collector shelf, and cross-link it.
- **H2-2 Active-user wheelchairs are flattened.** Manual wheelchair has 12 m, 3 r and x=0. Active users compare frames such as Quickie, TiLite and Küschall (to verify) much as cyclists compare bikes. **Fix:** add 3–5 archetypes under mode "mixed" for that shelf only.

**Too much detail**
- **H2-3 Attribute-only kinds.** There are four hearing-aid kinds by form factor (RIC, BTE, ITE, ITC) carrying 4–10 r each. There are six support kinds split only by body part (knee, ankle, back, wrist, elbow, neck). **Fix:** use one "Hearing aid" kind with form factor as `t`, and one "Joint support / brace" kind with body part as `t`.
- **H2-4 SKU depth in prescribed and clinical items.** Leg prosthesis has 9 m, Arm prosthesis 6 m, Implant sound processor 11 m plus 5 r, Spectacle lens 13 t plus 11 m plus 8 r, and Patient lift 10 m. These are fitted by clinicians, not chosen by owners. **Fix:** keep these at kind level with `t` only, per the scope rule.
- **H2-5 Maker skew in the m lists.** Portable ramp is 5 of 9 EZ-ACCESS, Alerting system 5 of 7 Bellman & Symfon, Pregnancy test 5 of 10 Clearblue, and Nicotine replacement 5 of 9 Nicorette. **Fix:** cut each to one product per maker.

**Confusing organisation**
- **H2-6 Orphan department.** "Medical supplies & first aid" holds a single bare kind, Medical face mask, beside an existing "First aid & supports" department. **Fix:** merge them.
- **H2-7 Misplaced kinds.**
  - Grab bar is a built-in fixture, so it moves to Home Fixtures.
  - Medical app is software, so it moves to I1 or I3.
  - Delay spray sits under "Contraception & barriers" and belongs with intimate devices.
  - The shelf "Quit smoking & traditional remedies" mixes nicotine replacement with homeopathy.
  - Sleep aid sits on the Pain shelf.
  **Fix:** re-shelve each one.
- **H2-8 Cross-category duplicates.** Pelvic-floor trainer duplicates H3 Kegel balls. Vaginal dilator duplicates H3 Dilator. Vacuum erection device duplicates H3 Penis pump. Erection ring duplicates H3 Penis ring. Heat & cold pack duplicates H1. **Fix:** give each kind one home. Medical-use devices stay in H2 and cross-link to H3.

**What it would look like (First aid & supports › Braces & supports)**
```
Joint support / brace (kind)
  t: knee · ankle · back · wrist & hand · elbow · neck
  t: sleeve · strap · hinged brace · splint
  m: Futuro, Bauerfeind, McDavid, DonJoy, Aircast  (≤6, to verify)
Hearing aid (kind)
  t: RIC · BTE · ITE · ITC · CIC · OTC
  r: Phonak, Oticon, Signia, ReSound, Widex, Starkey
```
**Priority:** medium · **Fix size:** small–medium

---

## H3 Sexual wellness

**Brand mode:** tier on paper. I recommend mixed, because icon products and a fantasy-silicone collector niche exist. The file has 58 kinds and **0 archetypes**. The register holds 34 brands, and none of them has lines or signature archetypes.

**Gaps for hobbyists**
- **H3-1 No archetypes, although the field has documented icons.** Each of the following has a Wikipedia or maker record: Hitachi/Vibratex Magic Wand (1968), Rabbit Pearl, Fleshlight, Tenga Egg/Cup, Sybian, RealDoll, Womanizer and Satisfyer Pro 2, and We-Vibe. Today they sit as flat m entries; Wand vibrator alone has 12 m including three Magic Wand variants. **Fix:** promote them to archetypes, with generations as versions (for example Magic Wand Original → Rechargeable → Mini).
- **H3-2 Missing kinds.**
  - Strap-on harness: a grep of all files finds none, although Dildo has the `t` "Harness-compatible".
  - Positioning wedge or cushion: Liberator is in the register but no kind exists.
  - Fantasy silicone toys: Bad Dragon is absent from all files.
  - Fetish wear: latex lives in A1, so cross-link it.
  **Fix:** add the three kinds and the cross-link.

**Too much detail**
- **H3-3 SKU lists in care items.** Toy cleaner has 15 m; Automatic masturbator has 8 m, one of them an all-caps product string. **Fix:** cut each to about 5.
- **H3-4 Attribute-only kinds.** Palm, Flicking, Bullet and Glans vibrator, Wearable panty vibrator and Vibrating cushion are form variants of "External vibrator". Spreader bar and Labia spreader are bare. Urethral sound lists 5 medical sound shapes as `t`. **Fix:** fold the vibrator forms into one kind with `t`, and reduce the sound shapes to a single detail line.

**Confusing organisation**
- **H3-5 Mechanism and anatomy axes collide.** "Masturbators, sleeves & rings" holds the shelf "Body-form toys & dolls". Thrusting vibrator sits under Machines while Rabbit sits under Insertable. Intimate oil sits in "Impact & sensation". **Fix:** split dolls into their own department, and move oils into Care, alongside lubricant from H1 (see H1-9).
- **H3-6 Overlap with H2.** This is the same overlap as H2-8 (dilator, kegel, pump, ring). **Fix:** cross-link, with H3 as the consumer home.

**What it would look like (Vibrators)**
```
Wand vibrator (kind)
├─ Magic Wand [Vibratex/Hitachi] 1968 — v: Original (corded), Rechargeable, Mini, Plus
├─ Doxy [Doxy] — v: Original, Die Cast, 3R
└─ Le Wand [Le Wand] — v: Original, Petite
Air-pulse stimulator (kind)
├─ Womanizer [Womanizer] 2014 — v: W100, Premium, OG
└─ Satisfyer Pro 2 [Satisfyer]
```
**Priority:** medium · **Fix size:** small

---

## H4 Fragrance

**Brand mode:** variety for perfume, bottles and materials; mixed for samples and gift sets. The file has 44 kinds and 190 archetypes (141 with versions). The register holds 566 brands, 486 of them unlinked. There are 5 traditions.

**Gaps for hobbyists**
- **H4-1 The niche and modern-cult canon is missing.** All of the following are absent from H4.json (grep): Amouage (Interlude, Gold), Creed's Green Irish Tweed, Xerjoff, Parfums de Marly, Nishane, Tom Ford Tobacco Vanille and Tuscan Leather, and Dior Homme. The classics are also absent: Guerlain Vol de Nuit, Caron Habanita, Calvin Klein Eternity and Geoffrey Beene Grey Flannel. Most of these houses are in the register, but none has a signature archetype. **Fix:** add about 30 archetypes from Fragrantica's most-reviewed and "classic" lists.
- **H4-2 Middle-Eastern and inspired-by houses are unrepresented.** Lattafa, Armaf, Rasasi and Ajmal are in the register, but there is no archetype for the clone or "dupe" phenomenon (for example Club de Nuit Intense Man → Aventus). It is a major hobbyist axis. **Fix:** add a `t` "inspired-by (clone)" on family kinds, with archetypes and a cross-link to the original.
- **H4-3 Perfumers are filed as brands.** About 20 noses sit in the brand register (Jean-Claude Ellena, Germaine Cellier, Ernest Beaux, Sophia Grojsman and others). **Fix:** create a perfumer register, parallel to the artist register, and link archetypes to it.

**Too much detail**
- **H4-4 Catch-all SKU kind.** "Alcohol-based perfume" has t=0, **70 m** and 8 r. 25 of the 70 m (36%) are Diptyque, a retail-harvest skew, and the kind duplicates m entries from the family kinds. Floral fragrance has 14 m, 3 of which are repeated in its own r. **Fix:** dissolve the kind and distribute its scents by family; the rule says scent is the archetype.
- **H4-5 Body mist** has 11 m, 8 of them Bath & Body Works (skew). **Fix:** reduce to the 4 existing archetypes plus about 4 makers.

**Confusing organisation**
- **H4-6 Inconsistent register names.** Fabergé, Rabanne, Gisou and Pfizer are used as `mk` but are not register names. "By Kilian" appears as a maker while the register has no Kilian. Knize Ten and Jovan Musk have an empty `mk`. Deer musk appears both as an oil archetype and as a raw material. **Fix:** reconcile the names and keep one home for Deer musk.
- **H4-7 The "Oud fragrance (Western niche)" label is confusing**, and the kind has only 2 archetypes. **Fix:** rename it "Oud fragrance" and include Arabian houses' alcohol-based ouds.

**What it would look like (Perfume › Fine fragrance by family)**
```
Fougère fragrance (kind)
├─ Fougère Royale [Houbigant] 1882 — v: original, 2010 re-creation
├─ Jicky [Guerlain] 1889
├─ Green Irish Tweed [Creed] 1985 — v: EDP; clones: Cool Water (lineage)
├─ Azzaro pour Homme · Kouros · Drakkar Noir · Le Male
├─ Sauvage [Dior] 2015 — v: EDT, EDP, Parfum, Elixir
└─ dt: concentration · reformulation year · batch code
```
**Priority:** high · **Fix size:** medium

---

## I1 Software

**Brand mode:** mixed. Tier for utilities, security and office; variety for Linux distributions, emulators, creative tools, DAWs and plug-ins. The file has 138 kinds and 382 archetypes (380 with versions). The register holds 103 developers, and **97 archetype makers are missing from it**.

**Gaps for hobbyists**
- **I1-1 Missing hobby kinds** (all absent from all files on grep):
  - Self-hosting and home-server software: Home Assistant, TrueNAS, Unraid, Plex or Jellyfin media servers. Only Kodi sits in Media player.
  - Modular and visual audio environments: VCV Rack, Max, Pure Data.
  - SDR software. SDR hardware is in D2, but no SDR software exists.
  - Desktop customisation: Rainmeter, Wallpaper Engine, AutoHotkey.
  - Long-form writing apps: Scrivener.
  - Music trackers: Renoise sits only as an m entry; OpenMPT and FastTracker (to verify).

  **Fix:** add these kinds with archetypes.
- **I1-2 The developer register is incomplete.** 97 `mk` values are missing, including Debian Project, GNU Project, Image-Line (FL Studio), Cockos (Reaper), Figma and Anthropic. **Fix:** add a register entry for each archetype maker.

**Too much detail**
- **I1-3 Catch-all archetypes.** The following are groups, not icons: "Independent distributions", "Other saturators", "Other repair tools", "Mastering chains from other makers", "Modular and AI strips", "Vocal effects and suites", "Tape plug-ins", "Character delays", "Dynamic EQ plug-ins", "Single-game mod managers", "Multi-network clients", and per-platform "… emulators" buckets. **Fix:** dissolve them into named archetypes or `m`.
- **I1-4 SKU lists on utility kinds.** File manager has 20 m, Terminal emulator 20 m (18 with no maker), AI coding assistant 18, Code editor plug-in 17, Media player 17, and Backup 15. Many entries have an empty maker; 39 kinds have m lists whose largest maker group is "empty". **Fix:** cut to 6–10 market or test leaders and fill the makers.
- **I1-5 Near-duplicate and out-of-scope kinds.**
  - Word processor, Spreadsheet and Presentation software sit beside Office suite.
  - Media player sits beside Music player, and Screenshot tool beside Screen recorder.
  - Online whiteboard (3 m) sits beside Diagramming.
  - Out of scope as institutional or trade software: Computer-assisted translation tool, Show-control software (QLab), Accounting software, Survey and form software, SPSS and Stata.

  **Fix:** merge the duplicates; drop the trade software or keep it as a bare kind.

**Confusing organisation**
- **I1-6 Overlap with I2 and I3.**
  - Orchestral sample library and Sampler (I1) duplicate I2 Virtual instrument library. Spitfire BBC SO and Kontakt appear in both.
  - VPN, AI assistant and Language-learning appear as software here and as plans in I3.

  **Fix:** product → I1, content → I2, plan → I3, with cross-links.
- **I1-7 Linux archetypes are "lineages".** That is defensible, because DistroWatch organises by base. Arch and Mandriva lack `mk`. **Fix:** make sure Ubuntu, Mint and Fedora appear as versions.

**What it would look like (Audio plug-ins › Saturation & distortion)**
```
Saturation & distortion plug-in (kind)
├─ Studer A800 [Studer] — v: UA Studer A800, … (hardware emulation)
├─ Ampex ATR-102 [Ampex] — v: UA ATR-102
├─ Decapitator [Soundtoys] 2009 — v: v5
├─ Saturn [FabFilter] — v: Saturn, Saturn 2
└─ (no "Other saturators" bucket; long tail → m)
```
**Priority:** medium · **Fix size:** medium

---

## I2 Digital content & assets

**Brand mode:** variety for typefaces, game items and NFTs; tier for templates and media files. The file has 76 kinds and 117 archetypes. The register holds 63 brands; 11 foundries in it are unlinked, and 24 `mk` values are missing from it.

**Gaps for hobbyists**
- **I2-1 The typeface canon is thin.** The nine classification kinds hold 23 archetypes; Serif has 5, Display 1, Blackletter 1 and Monospace 1. Absent on grep: Didot, Optima, Palatino, DIN, Johnston, Franklin Gothic, Avenir, Cooper Black, Trajan and Arial. Foundries in the register (Klim, Commercial Type, Emigre, Grilli Type, House Industries) have no signature faces. **Fix:** add about 40 archetypes using Vox-ATypI groups as `t`.
- **I2-2 Trading-community game-item icons are missing.** The following are absent: RuneScape partyhats, TF2 Unusual hats, Dota 2 couriers and arcanas, Roblox Limiteds (only a generic "Limited item" exists), and Fortnite Black Knight (to verify). **Fix:** add 6–10 archetypes beyond Valve.

**Too much detail**
- **I2-3 Platform-profile shelf.** Its 7 kinds are mostly Steam attributes: Loading screen, Chat emoticon, Profile background, Avatar or frame, Badge, Trading card and Sticker pack. **Fix:** make one "Platform profile item" kind with `t`, and keep Steam trading card as an archetype.
- **I2-4 Format lists posing as types.** Digital photo `t` lists 14 raw formats by camera maker. Domain name has 16 TLDs with registry operators as m. **Fix:** cut each to the main classes.
- **I2-5 Valve skew.** 26 of the 117 archetypes are Valve, and all 5 Loot-case m entries are Valve. **Fix:** rebalance through I2-2.

**Confusing organisation**
- **I2-6 Mixed maker axis for typefaces.** `mk` mixes designers (Claude Garamond, Hermann Zapf), historic foundries (Bauersche Gießerei) and companies (Google), none of them in the register. **Fix:** use a foundry register plus a designer register, as for perfumers.
- **I2-7 Duplicate archetypes.** Poly Haven is filed under three kinds and Quixel Megascans under two; both are platforms, not assets. Kontakt is a player, not a library. **Fix:** move the platforms into the brand register.

**What it would look like (Fonts › Serif typeface)**
```
Serif typeface (kind)  t: Venetian · Garalde · Transitional · Didone
├─ Jenson → Centaur [Bruce Rogers]  (to verify)
├─ Garamond [Claude Garamond] — v: Stempel, Adobe, EB Garamond
├─ Caslon · Baskerville
├─ Bodoni · Didot [Firmin Didot]
├─ Times New Roman [Monotype] 1932 — v: Times, Times Ten
└─ Palatino [Hermann Zapf] 1949 — v: Palatino Linotype, Nova
```
**Priority:** medium · **Fix size:** medium

---

## I3 Subscriptions, memberships & services

**Brand mode:** tier for streaming, telecoms, online services, boxes and home contracts; variety for clubs, status, staff and private aviation. The file has 79 kinds and 24 archetypes, with 180 brands in the register.

**Gaps for hobbyists (the luxury and status end)**
- **I3-1 Status programmes lack their icons.**
  - Airline status has x=0 and 11 programme m. FlyerTalk-level readers expect the invitation-only tiers: Lufthansa HON Circle, AA Concierge Key, United Global Services and BA Premier (to verify). None is in any file.
  - Hotel status also has x=0.
  - Ski passes (Epic, Ikon) are absent from Season ticket.

  **Fix:** add archetypes.
- **I3-2 The private-club list is short.** It has 9 archetypes. Garrick, Brooks's, Boodle's, the Knickerbocker and 5 Hertford Street are absent (to verify), and there are no Asian clubs. Jet card (NetJets, VistaJet) and concierge (Quintessentially) stay as m. **Fix:** promote these to archetypes, with versions for the card and programme tiers.

**Too much detail**
- **I3-3 Operator lists by country.** Mobile phone plan has 12 m plus **57 r**. Video streaming has 10 m plus 30 r. Broadband has 12 m plus 11 r. Gym has 20 m. **Fix:** cap each kind at the global leaders plus about 1–2 per major market, and move the per-country lists into the brand register as a "market" view.
- **I3-4 Duplicate model.** Personal stylist lists "Personal shopping" twice. **Fix:** remove one.

**Confusing organisation**
- **I3-5 Product, plan and content blur with I1 and I2.**
  - VPN service, AI assistant subscription, Language-learning plan and Cloud storage mirror I1 software kinds.
  - Stock library subscription mirrors I2 Stock photo.
  - The domain-name `t` in hosting mirrors I2 Domain name.
  - Season or battle pass mirrors I2 game items.

  **Fix:** adopt the rule "plan here, product or asset there" and cross-link.
- **I3-6 Pursuit delineation is creeping in.** The `t` lists of "Sports, hobby or social club" and "Gym" enumerate sports and disciplines (tennis, rowing, yoga, boxing). **Fix:** keep the membership form as `t` (club, multi-sport, supporters') and cross-link the sport to the pursuit taxonomy.
- **I3-7 Label.** "Multi-site membership", "Multi-venue pass" and "Annual pass" are hard to tell apart. **Fix:** rename them "Heritage & parks membership", "City & museum pass" and "Single-venue annual pass".

**What it would look like (Memberships › Clubs & status)**
```
Airline status (kind)  t: alliance tier · qualification basis
├─ Lufthansa HON Circle [Lufthansa] — invitation by miles  (to verify)
├─ AA Concierge Key [American Airlines] — invitation only
├─ United Global Services [United] — invitation only
├─ BA Premier [British Airways] — invitation only
└─ m: AAdvantage, Flying Blue, Miles & More, KrisFlyer …
Private members' club (kind)
├─ White's 1693 · Athenaeum · Garrick · Brooks's · Soho House (v: houses)
```
**Priority:** low–medium · **Fix size:** small
