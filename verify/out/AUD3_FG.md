# AUD3_FG — cold audit of F1–F6, G1, G2 (2026-10-28)

Counts are computed from rebuild/reader/<CODE>.json and its registers. "Absent everywhere" means a case-insensitive grep of all rebuild/reader/*.json files found nothing. Facts from my own knowledge are marked (to verify).

---

## F1 Media & Publications
**Brand mode:** mixed. Tier for everyday books, current maps and storage; variety for fine and early books, records, film and video, comics, sheet-music editions, and antique maps and globes.
127 kinds, 308 archetypes, 43 kinds with no archetype.

**Gaps for hobbyists**
- **F1-1 Comics are lumped.** *Single-issue comic* has 12 types but only one archetype, "CGC-graded comic". That is a grading holder, which belongs with the F3 slab and grading register, not a comic archetype. *Bande dessinée album* has one generic archetype ("Standard 48-page album"), and its `m` entry "Album (bande dessinée)" repeats it. **Fix:** give each format its own archetypes: standard US comic book (newsstand and direct versions), Giant-Size and annual, treasury edition, Prestige format, digest, Italian Bonelli-format albo (to verify). Organise BD by publisher line (Dupuis, Dargaud, Casterman, Le Lombard, Glénat), with édition originale and tirage de tête as versions. Move CGC to F3.
- **F1-2 Missing carriers.** Piano roll, wire recording, Dictabelt and PlayTape are absent everywhere. Test pressing is not even a type. The 4-track cartridge is filed as the archetype "Stereo-Pak" under *8-track cartridge*, although its own alias says "4-track cartridge". **Fix:** add a *Piano roll* kind (Ampico, Duo-Art, QRS; to verify) and a *Dictation and wire recording* kind. Rename the cartridge kind to "Tape cartridge (4- and 8-track)", and add "test pressing" to the LP types.
- **F1-3 Missing book formats.** Dime novel, penny dreadful, yellowback, Big Little Book, children's annual and the "Real Book" fake book are absent everywhere. Photobook exists only as an archetype under *Artist's book*. **Fix:** add a "Popular & cheap fiction formats" shelf, plus a *Photobook* kind and an *Exhibition catalogue* kind.

**Too much detail**
- **F1-4 Thin videotape and tape kinds.** The Videotape shelf has 8 kinds but 4 archetypes. S-VHS, VHS-C, W-VHS, Video 2000, 8 mm and MiniDV each have 0 archetypes and 2–4 types. DAT, DCC and Elcaset also have 0 archetypes, and Elcaset's types are just "blank; tape type". **Fix:** merge into one *Camcorder cassette* kind (types: VHS-C, Video8/Hi8/Digital8, MiniDV), make S-VHS and W-VHS types of VHS, and make one *Digital & late analogue cassette* kind (DAT, DCC, Elcaset).
- **F1-5 Storage is a SKU list.** The Storage dept has 29 `m` rows, 13 of them BCW, e.g. three backing boards that differ only by Golden/Silver/Current size. CD-R has 9 dye-chemistry types. **Fix:** keep brands only (BCW, Ultra PRO, E. Gerber, Nagaoka, MoFi), make sizes into types, and cut CD-R to about 4 types.

**Confusing organisation**
- **F1-6 Urtext editions sit under *Songbook*.** The *Songbook* kind holds Henle, Bärenreiter and Wiener Urtext, Peters and Kalmus. Those are classical performing editions, and nobody looks for them under "Songbook". **Fix:** create *Performing edition (urtext / practical)* and keep *Songbook* for PVG and fake books.
- **F1-7 Carriers are duplicated in F5.** F5 *Home film reel* and *Home videotape* repeat F1's film-print and videotape carriers. **Fix:** keep the carriers here and make "home-made" a content view in F5.

**What it would look like (Comics)**
```
Comics & manga
└ Single-issue comic
  ├ US standard comic book → newsstand / direct / variant cover → grade, label
  ├ Giant-Size, annual & treasury edition
  ├ Prestige-format book (1980s–)
  ├ Digest comic
  └ Bonelli-format albo (Italy)
└ Bande dessinée album
  ├ Dupuis · Dargaud · Casterman · Le Lombard lines → édition originale → tirage de tête
```
Priority: medium
Fix size: medium

---

## F2 Art
**Brand mode:** variety. Figurines are variety by house; the framed-art-print kind is tier.
118 kinds, 331 archetypes.

**Gaps for hobbyists**
- **F2-1 Figurines are lumped and skewed.** The dept has 6 kinds and 25 archetypes.
  - *Porcelain and bone china figurine* puts Meissen, Doulton, Lladró, Hummel and Precious Moments into one kind (9 archetypes), plus 23 flat named pieces (17 Royal Doulton, 5 Lladró).
  - 6 of the 8 crystal archetypes are Swarovski. *Resin figurine* has one archetype (Willow Tree).
  - Lilliput Lane, David Winter, Border Fine Arts, Boyds, Lomonosov, Hutschenreuther and Jim Shore are absent everywhere. Royal Copenhagen and Bing & Grøndahl appear only as plates in B5.

  **Fix:** split the porcelain kind into three:
  - *Continental porcelain figure*: Meissen, Nymphenburg, Royal Copenhagen, B&G, Lomonosov, Herend, Capodimonte.
  - *English bone-china figure*: Doulton HN, Royal Worcester, Beswick, Coalport, Wade.
  - *Collectible giftware figurine*: Hummel, Lladró, Precious Moments.

  Also add a *Miniature cottage* kind (Lilliput Lane, David Winter, cross-linked to Department 56 in B4), fold the named Doulton and Lladró pieces into versions, and add Baccarat, Daum, Waterford and Orrefors/Kosta animals to the crystal kind.
- **F2-2 Missing processes.** Carbon print, gum bichromate, bromoil and Woodburytype are absent everywhere. Editioned art multiples (Fluxus, Beuys; to verify) are also absent. **Fix:** add these as process kinds under Photographs and add a *Multiple* kind under Sculpture.

**Too much detail**
- **F2-3 Monoprint repeats Monotype.** *Monoprint* has 0 archetypes and overlaps *Monotype*. **Fix:** make it a type of Monotype.

**Confusing organisation**
- **F2-4 Paintings mixes axes.** The 23 kinds mix media (oil, acrylic, watercolour) with traditions and a status:
  - Traditions: Tingatinga (1 archetype), Nihonga (1), Korean folk, Indian folk, Aboriginal.
  - Status: *Outsider art*, whose types include sculpture and collage.

  The traditions register already holds Tingatinga, Mithila, Minhwa and Western Desert painting. **Fix:** keep medium and format kinds, make the traditions into register entries tagged onto the medium kinds, and make "outsider" a view tag.
- **F2-5 Photo kinds duplicated in F5.** Daguerreotype, Ambrotype, Tintype and Instant print are kinds in both F2 (with archetypes) and F5 (mostly without). **Fix:** keep one home per process here, and give F5 a "vernacular & family" view over it.
- **F2-6 Artists are filed as brands.** The lead promises a ULAN-keyed artist register. Instead, artists sit in the brand register (204 entries, 132 with segment "Artisan & independent"), and ULAN appears 0 times. **Fix:** create a separate artist register with ULAN IDs, and keep houses and studios (Meissen, Daum, Mourlot) as brands.

**What it would look like (Collectible figurines)**
```
Collectible figurines
├ Continental porcelain figure → Meissen Kändler · Nymphenburg commedia · Royal Copenhagen · Lomonosov
├ English bone-china figure → Royal Doulton HN (versions: HN numbers) · Beswick animals · Royal Worcester
├ Collectible giftware figurine → M.I. Hummel · Lladró · Precious Moments
├ Crystal & glass figurine → Swarovski SCS · Baccarat · Lalique · Daum · Murano
└ Miniature cottage & village → Lilliput Lane · David Winter · (Dept 56 in B4)
```
Priority: medium
Fix size: medium

---

## F3 Coins, Stamps, Medals & Trading Cards
**Brand mode:** variety (issuers, card makers); tier for holders, albums and trophies.
112 kinds, 405 archetypes, 9 kinds fully empty.

**Gaps for hobbyists**
- **F3-1 Coins lean on the US.** Of the 121 Coins archetypes, 24 are United States Mint, plus 13 of the US `m` rows. All 6 mint-error archetypes are US. **Fix:** add issuer-first archetypes for about 10 major issuers: euro definitives, British pre-decimal silver, French Semeuse, German mark, Swiss Helvetia, Indian rupee (all to verify). Add non-US errors and mules.
- **F3-2 Trading cards lean on Topps.** Topps has 14 of 46 archetypes plus 14 `m` rows. All 8 *Insert card* rows and all 5 *Autograph card* rows are Topps SKUs. *Box card* is empty, and soccer, F1 and American football barely appear. **Fix:** add flagship sets per maker (Panini Prizm, Select and National Treasures; Upper Deck Series 1; Leaf; Topps Chrome F1), and turn the insert and autograph SKUs into versions of their sets.
- **F3-3 Missing collectables.** Hobo nickel is absent everywhere. Signed or game-worn memorabilia appears only as relic cards. *Championship ring* and *belt* are empty, although replica belts and rings are collected. **Fix:** add hobo nickel as a type of love token and give the ring and belt kinds archetypes. Memorabilia goes to F5 (see F5-1).

**Too much detail**
- **F3-4 Empty kinds.** 9 kinds are fully empty: Maximum card, Philatelic numismatic cover, Box card, Medal case, Trophy cup, Upright award, Bowl/tankard/salver, Rosette, and Championship ring. **Fix:** collapse the Trophies dept into one *Trophy or award* kind with form types, make Maximum card a type of First-day cover, and fill or drop the rest.
- **F3-5 Thin token kinds.** Tokens have 11 kinds and only 14 archetypes, and 7 kinds have at most one archetype. **Fix:** merge transit, vending, locker/trolley and tax tokens into one *Service token* kind.

**Confusing organisation**
- **F3-6 Orders use mixed axes.** British awards get 4 kinds by award type and the US gets 2. France, Germany, Russia and Japan get one kind each, and "other states" has 2 archetypes. **Fix:** make kinds by award type, and make the issuing state a view through the issuer register, as for coins and stamps.

**What it would look like (Orders, decorations & medals)**
```
Orders, decorations & medals   (issuing state = issuer view)
├ Order of chivalry → Garter · Bath · Legion of Honour · Rising Sun · Order of Lenin → class (collar, star, badge)
├ Gallantry decoration → Victoria Cross · Medal of Honor · Iron Cross · Hero of the Soviet Union
├ Campaign medal → Waterloo · QSA · WWI trio · Vietnam Service → clasps, naming
├ Long-service & good-conduct medal
└ Mounting, ribbon & case
```
Priority: medium
Fix size: medium

---

## F4 Religious & Spiritual Objects (form-first structure audited as given)
**Brand mode:** variety for images, prayer aids and tarot; tier for candles and funeral goods.
131 kinds, 120 archetypes. 65 kinds have no archetype, and 44 of those have at most 3 types.

**Gaps for hobbyists**
- **F4-1 No sacred texts as objects.** The Scriptures dept holds only Jewish and Islamic holders. "Mushaf", "siddur" and "megillah" are absent everywhere, and a Bible appears only as F1 incunable or private-press archetypes. **Fix:** add a *Sacred text copy* kind tagged by tradition, with archetypes: family Bible, mushaf, gutka, orihon sutra book, Megillat Esther. Text editions cross-link to Literature.
- **F4-2 Missing common objects.** Sri Yantra, Ganesha, pysanka, palm cross, gau box and dreamcatcher are absent everywhere. The *Murti* kind has only Nataraja, linga and shaligram. "Ritual-magic tools" has 2 kinds and 0 archetypes. **Fix:** add deity archetypes to Murti, add *Yantra* (Sri Yantra plus the Jain Siddhachakra), and add *Wand*, *Cauldron* and *Book of Shadows*.
- **F4-3 Tarot is a title list.** *Tarot deck* has 5 archetypes plus 10 decks with no maker. *Oracle deck* has 1 generic archetype plus 7 decks. U.S. Games, Llewellyn, Lo Scarabeo and Grimaud are in the register but linked from nothing. **Fix:** see the tree below, with publisher `mk` on each version. Hay House oracle lines should be added (to verify).

**Too much detail**
- **F4-4 Too many thin kinds.** Single-object kinds with 1–3 types and no archetype include Kara, Kanga, Kirpan, Tingsha, Kalash, Etrog box, Paschal, Havdalah and Yahrzeit candles, Holy-water bottle, Aspergillum, pendulum and dowsing rod. **Fix:** merge by form:
  - *Altar bell & chime* (with Standing bowl bell)
  - *Holy-water vessel*
  - *Ritual candle* (with types)
  - *Worn article of faith*
  - *Dowsing tool*
- **F4-5 Junk `m` rows.** 47 `m` rows have no maker. Many just repeat the kind (Tasbih, Juzu, Mokugyo, Kartika, Omamori, Ihai), and some duplicate an archetype (Yemenite shofar, Elder Futhark rune set). **Fix:** delete them.

**Confusing organisation**
- **F4-6 Ceremonial regalia is out of place.** "Ceremonial regalia & office insignia" holds 4 fully empty institutional kinds (Mace, Gavel, Chain of office, Crown of office). These are not worship objects and fail the scope rule. **Fix:** drop them, or move Gavel to office goods.
- **F4-7 Duplicates in F2.** *Calligraphy wall panel* (hilya) repeats F2 *Islamic calligraphy* and its "Hilye panel" archetype. Thangka is in both the F4 and F2 traditions registers. **Fix:** give each one home and cross-link the other.

**What it would look like (Tarot & divination)**
```
Tarot deck
├ Tarot de Marseille → Conver (to verify 1760) · Grimaud Ancien Tarot · Camoin–Jodorowsky
├ Rider–Waite–Smith (Rider, 1909) → U.S. Games editions · Smith–Waite Centennial · RWS-system clones
├ Thoth (Crowley–Harris) → AGM / U.S. Games editions
├ Visconti–Sforza → Lo Scarabeo / U.S. Games reproductions
└ Independent artist deck → publisher line (Wild Unknown, Modern Witch …)
Detail: size, gilt edges, box, edition
```
Priority: medium
Fix size: medium

---

## F5 Papers, Cards & Ephemera
**Brand mode:** variety for postcards, ephemera, scripophily, and transit and phone cards; tier for identity, certificates and gift or membership cards.
84 kinds, 98 archetypes, 16 kinds fully empty.

**Gaps for hobbyists**
- **F5-1 Autographs and memorabilia are missing.** *Autograph*, the largest hobby here, has 0 archetypes. Signed and game-worn memorabilia has no kind. PSA/DNA, JSA and Beckett Authentication are in the register but link to nothing. **Fix:** add autograph archetypes (signed photo, index card, cut signature, White House card, signed FDC cross-linked to F3) and a new *Signed & game-used memorabilia* kind (signed ball, jersey, bat), with the authenticators as versions or labels.
- **F5-2 Ephemera hobbies are missing.** Beer mats, cigar bands, sugar packets, pinback buttons, and lobby cards or press kits are absent everywhere. *Matchbox label* (phillumeny) has 0 archetypes. **Fix:** add these kinds, with maker or issuer archetypes.

**Too much detail**
- **F5-3 Empty kinds.** 16 kinds are fully empty: 6 of the 9 identity kinds, plus Gift card, Gift certificate, Membership card, Will, Tax paper, House plans, School report, Snapshot, Scrapbook and Promissory note. **Fix:** merge into fewer kinds:
  - *Identity document* (with types), keeping *Passport* separate.
  - *Gift & membership card*, taking in the *Loyalty card* kind and its one Duane Reade row.
  - *Household & legal papers*.
- **F5-4 Transit issuers swamp the register.** 237 of the 289 register entries are transit-card issuers (kf "transit card"), from a Colnect harvest, against 14 transit archetypes. **Fix:** keep them as stubs but out of the default brand view, and raise postcard and ephemera publishers instead.

**Confusing organisation**
- **F5-5 Duplicates across categories.** The same items live in F2, F3, F1 or twice in F5:
  - Daguerreotype, Ambrotype, Tintype and Instant print repeat F2.
  - *Posted envelope* (censored, crash, airmail) and the Aerogramme archetype repeat F3 covers and F3 *Aerogram*.
  - Home film and video repeat F1 carriers.
  - Stevengraph is an archetype twice in F5 (Novelty postcard and Bookmark).
  - Commonplace book is in both F1 and F5.

  **Fix:** give each one home and cross-link the others.

**What it would look like (Letters, autographs & memorabilia)**
```
Letters, autographs & memorabilia
├ Autograph → signed photograph · index card · cut signature · White House card → authenticator (PSA/DNA, JSA, Beckett)
├ Signed & game-used memorabilia → signed ball · game-worn jersey · bat → photo-match, LOA
├ Letter → ALS · TLS · V-mail · airgraph
├ Autograph album → album amicorum · Victorian friendship album · yosegaki
└ Diary · manuscript document · written-in notebook
```
Priority: medium
Fix size: medium

---

## F6 Natural History & Specimens
**Brand mode:** variety (dealers, labs, preparators); tier for display.
299 kinds, 1,184 archetypes. The mineral tree (169 species kinds) follows Nickel–Strunz well.

**Gaps for hobbyists**
- **F6-1 Popular minerals are missing.** Bornite, molybdenite, atacamite, boleite, witherite, hanksite, chalcanthite, aegirine, astrophyllite, zincite, anatase and creedite are absent everywhere, including species/F6. Bornite ("peacock ore") and boleite are shop and collector staples (to verify). **Fix:** add them to the tree, or at least to the species register.
- **F6-2 Dinosaurs are lumped.** *Dinosaur fossil* is one kind with 5 archetypes that mix parts (Spinosaurus tooth, Carcharodontosaurus tooth, egg) and taxa (Triceratops, hadrosaur). T. rex, Allosaurus and raptor claws are absent. Ichthyosaur is only named in a definition. **Fix:** split by specimen type (tooth, claw, bone or vertebra, egg or eggshell, skin impression) with taxa as archetypes, and add an Ichthyosaur archetype (Lyme Regis).
- **F6-3 Missing dealers and viewing stones.** The 24-entry register holds labs and taxidermists, but no mineral or fossil dealers, although the lead promises them (e.g. Collector's Edge, Kristalle; to verify). Suiseki, gongshi and viewing stones are absent everywhere. **Fix:** add the dealers, a *Viewing stone* kind, and two tradition entries.

**Too much detail**
- **F6-4 Taxidermy and skulls mix attributes into archetypes.** "Full mount", "Shoulder mount" and "Skull mount" are mount types, not archetypes. "Dermestid-cleaned skull" is an archetype under both mammal and bird skulls. *Reptile skull* and *Fish skull* have 0 archetypes and list species as types (alligator, piranha). **Fix:** merge into one *Animal skull* kind with the animal group as a type, make preparation a detail, and send species to the species register.
- **F6-5 Display kinds are empty.** The Display dept has 4 kinds, 3 fully empty. *Insect in resin* is also empty. **Fix:** merge into one *Specimen display* kind (dome, riser, frame case, thumbnail box).

**Confusing organisation**
- **F6-6 Fossil insect is misplaced.** Its own definition says it means insects preserved in rock, yet it sits on the "Amber & copal" shelf. **Fix:** move it to "Trilobites & arthropods", renamed "Arthropods & insects".

**What it would look like (Vertebrate fossils)**
```
Vertebrate fossils
├ Dinosaur tooth → Spinosaurus · Carcharodontosaurus · T. rex · raptor (Kem Kem, Hell Creek)
├ Dinosaur claw & bone → Allosaurus · hadrosaur vertebra · Triceratops horn/frill
├ Dinosaur egg & eggshell → Hypselosaurus · oviraptorid
├ Marine reptile → Mosasaur · Plesiosaur · Ichthyosaur (Lyme Regis)
└ Fossil shark tooth · fossil fish · fossil mammal
Detail: restoration %, composite, locality, formation
```
Priority: low
Fix size: medium

---

## G1 Vehicles
**Brand mode:** variety for cars, motorcycles, boats, aircraft, rail and classic bikes; mixed for bicycles, caravans and riding gear; tier for prams, trailers and vehicle care.
237 kinds, 840 archetypes. Car icon coverage is strong.

**Gaps for hobbyists**
- **G1-1 Preserved buses and taxis are missing.** *Bus or coach* and *Tractor unit* are fully empty, treated as trade vehicles. Yet bus and lorry preservation is a large owner hobby, and Routemaster and the London taxi FX4 are absent everywhere. **Fix:** add archetypes for preserved buses (AEC Routemaster, Bristol Lodekka) and a *Taxi* kind (Austin FX4, Checker Marathon). Vintage tractors and traction engines already live in C7, so cross-link them.
- **G1-2 Icon gaps.** Citroën DS, Toyota AE86, Brough Superior SS100, Suzuki GSX-R, Yamaha XT500 and Tiger Moth are absent (to verify). **Fix:** add them as archetypes.

**Too much detail**
- **G1-3 Helmet catch-all.** *Other motorcycle helmets* is a catch-all whose 15 `m` rows duplicate every row in Full-face (7), Modular (1) and Open-face (2). **Fix:** delete it. Move the retro icons (Bell Bullitt, Bell Custom 500, AGV X3000, Biltwell Gringo) into archetypes of the open-face and full-face kinds.
- **G1-4 Vehicle care is a retail harvest.** It has 145 `m` rows against 18 archetypes, with Chain cleaner 14, Snow foam 11 and Interior cleaner 11. The lists show a UK retail skew (Halfords, CarPlan, Autoglym, Bilt Hamber recur). **Fix:** cut to market coverage plus test winners, 5–8 per kind.
- **G1-5 Empty kinds.** 11 kinds are fully empty, including 4 trailer kinds and 5 lifting kinds. **Fix:** make one *Utility trailer* kind with types.

**Confusing organisation**
- **G1-6 Misplaced kinds.** Jacks, axle stands and the engine hoist and stand sit on the "Washing & decontamination" shelf, and chain lube sits on "Interior, trim & tyres". *Motorcycle boot* is on the Helmets shelf, although the dept note says boots stay in Footwear, and no Footwear file has it. **Fix:** move the lifting gear to Tools or a "Garage equipment" shelf, give chain care its own shelf, and either fix the note or move the boot.
- **G1-7 Bicycle lists are skewed.** BMX's 5 `m` rows are all Mongoose, Electric bike's 5 are all Riese & Müller, and Canyon fills 5 MTB kinds. *Gravel bike* has 1 archetype plus 11 `m` rows. **Fix:** re-harvest from independent reviews.

**What it would look like (Motorcycle helmets)**
```
Motorcycle helmets
├ Full-face → Shoei X-Fourteen line · Arai RX-7 · Bell Star → Bell Bullitt (retro) → generations
├ Open-face → Bell Custom 500 (1954) · Biltwell Gringo
├ Modular → Schuberth C-series · Shoei Neotec
├ Off-road & dual-sport → Bell Moto line · Arai VX
└ Detail: shell sizes, homologation (ECE 22.06, DOT, Snell), graphics
```
(model names to verify)
Priority: medium
Fix size: medium

---

## G2 Real Estate & Property
**Brand mode:** tier for houses, land and burial places; mixed for prefab and branded residences.
85 kinds, 172 archetypes, 8 kinds fully empty.

**Gaps for hobbyists**
- **G2-1 Thin prefab and branded-residence coverage.** *Kit & prefab house* has 3 archetypes, and the register has no large Japanese prefab makers (Sekisui House, Daiwa House; to verify). Branded residences have only Four Seasons and Aman. Beach hut and timeshare are absent everywhere. **Fix:** add makers and branded lines, plus *Beach hut* and a *Fractional & timeshare* kind.

**Too much detail**
- **G2-2 Over-split burial and farm kinds.** Burial places has 8 kinds, 5 fully empty. Farm & estate buildings has 6 kinds (Cart shed empty, Granary and Field shelter with 2 types each). *Arable land* is empty. **Fix:** cut to 3 burial kinds (burial plot, crypt or mausoleum, cremation plot or niche), one *Farm building* kind with types, and make arable a type of Farm.

**Confusing organisation**
- **G2-3 Style and tradition are built as kinds.** The shelves "Architectural styles (view)" (5 kinds, 36 archetypes) and "Regional house traditions" (5 kinds, 52 archetypes) put style and tradition into the kind tree. That breaks the rule that period and style are an attribute and a view, and their type lists come out inverted ("villa; terrace; detached"). The 29-entry traditions register repeats them and duplicates itself ("Yaodong" and "Loess yaodong"). Items recur across the tree:
  - Cortijo, Finca and Pazo are under both Hacienda and Mediterranean.
  - Yaodong is under both Asian and Earth-sheltered.
  - Cape Cod and Saltbox are under both Colonial styles and Americas.
  - Ansitz, Pazo and Bastide are both types and archetypes of *Country house*.

  **Fix:** make style an attribute view, move the traditions to the register, and place vernacular forms as archetypes under the property-type kinds (Machiya under Townhouse, Trullo under Cottage).
- **G2-4 Single properties used as archetypes.** Necker Island, Skorpios, Lānaʻi, Balmoral Estate, Claiborne Farm, Château Lafite Rothschild, King Ranch and House in the Clouds are unique properties, not patterns. **Fix:** make them examples under pattern archetypes, e.g. "Caribbean private cay" or "Highland sporting estate".

**What it would look like (Houses)**
```
Houses   (views: architectural style · regional tradition)
├ Terraced house → Georgian terrace · Victorian terrace · back-to-back · brownstone → listed/unlisted
├ Townhouse → Kyoto machiya · Dutch canal house · Charleston single house
├ Cottage → thatched cob cottage · trullo · Creole cottage · blackhouse
├ Country house → manor house · Palladian · Scots baronial · pazo · bastide · Ansitz
└ Farmhouse → Low German hall house · Black Forest house · longère · masía
```
Priority: medium
Fix size: medium
