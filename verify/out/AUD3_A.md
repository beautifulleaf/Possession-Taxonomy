# AUD3_A — cold audit of A1–A5 (2026-10-28)

All counts come from rebuild/reader/<CODE>.json and its brand and tradition registers, read on 2026-10-28. Facts from my own knowledge are marked "to verify". I checked every claimed absence with a grep across all rebuild/reader/*.json.

---

## A1 Clothing

**Brand mode:** mixed. Tops, trousers, underwear and nightwear are tier at the basics end. Coats, suits, dresses, hats and traditional dress are variety.

Size: 9 departments, 210 kinds, 730 archetypes, 1,071 versions; 2,530 brands (2,045 are stubs); 96 traditions.

### Gaps for hobbyists
- **A1-1 Lumped headwear kind.** "Traditional, ceremonial & uniform headwear" holds 65 `t` types and 0 archetypes. It mixes faith skullcaps, military headwear (bearskin, shako, kepi), East Asian court hats, folk caps, historical bonnets and novelty party hats. This is the E1 "Mechanical puzzle" case again. **Fix:** split it by object form into these kinds: Skullcap (kippah, taqiyah, zucchetto, kufi, tubeteika); Fez & brimless cap; Turban & head-wrap; Conical & woven sun hat (nón lá, salakot, kasa, sombrero vueltiao); Folk felt hat (Tyrolean, kalpak, qeleshe); Academic cap; Uniform headwear, cross-linked to the militaria shelf in Weapons. Put the faith tradition on each kind as a tag (rule of 2026-10-28). Move deerstalker and sou'wester to the country hats. Send novelty hats to Costume.
- **A1-2 Football shirts and team jerseys have no archetypes.** "Team jersey" has 0 archetypes and 7 `r` ranges. Retro football shirts are a large collecting field (Classic Football Shirts, Score Draw and COPA are already in the ranges). **Fix:** create kinds for Football shirt, Basketball jersey, Ice-hockey jersey and Baseball jersey. Use maker template families and eras as archetypes, e.g. adidas Equipment 1990–92 and Umbro 1990s templates (to verify). Versions are authentic or replica and home or away. Keep team lists out.
- **A1-3 Missing kinds:** sporran, kilt pin and sgian-dubh (Highland dress; "Kilt" only names them in a `t` string), smoking jacket, shooting breeks and plus-fours, Mackinaw. A grep across all files found none of these.

### Too much detail
- **A1-4** "Collar stay" (6 material types), "Cummerbund", "Detachable lining or hood" (a spare-part list) and "Leg warmers" all have 0 archetypes. **Fix:** fold collar stay and cummerbund into a "Formal accessories" kind. Turn the detachable liner into a `t` type on Coats.
- **A1-5 Near-duplicates:** "Corset top" (Tops) and "Corset" (Underwear); "Bodysuit" and the shapewear bodysuit. **Fix:** merge each pair.

### Confusing organisation
- **A1-6 Duplicate archetypes across kinds.** Bisht appears under both Cape and Abaya. The Beckenbauer and Firebird archetypes appear under both Tracksuit and Track jacket. Patola, Pochampally, Jamdani and Chanderi appear as both sari archetypes and "Named cloths". **Fix:** give each archetype one home and cross-link.
- **A1-7 Misplaced items.** Tracksuit sits in "Dresses, skirts & sets". The rain, army and cycling ponchos are `t` types under the traditional Poncho kind. LZR Racer and Fastskin racing suits are in Swimsuit and also in E2; under the sport rule they belong only in Sports. Glen plaid and houndstooth are patterns, so they belong as attributes, not archetypes under "Tweed cloth".
- **A1-8 Register hygiene.** "Levi's" and "Levi Strauss & Co." are two separate register entries, and archetype `mk` fields use both names. There are 7 `mk` values with no register entry, e.g. "adidas" where the register has "Adidas". The traditions register has duplicate pairs: Donegal tweed / Donegal tweed weaving, Loden / Loden cloth, Shemma / Ethiopian shemma, Bisht / Hasawi bisht. **Fix:** merge the pairs and normalise the maker names.

### What it would look like (Hats › brimless and faith caps)
```
Skullcap [tag: faith]
  Kippah (Judaism) → crocheted · velvet · suede
  Taqiyah (Islam) → crochet · Pakistani Sindhi cap
  Zucchetto (Catholic clergy) → colour by rank
Fez & brimless cap
  Fez (Ottoman/Moroccan) → tasselled · Zanzibar kofia
  Tubeteika (Central Asia) → Chust · Bukhara
Uniform headwear → link Weapons › Militaria
```
Priority: high
Fix size: medium

---

## A2 Footwear

**Brand mode:** variety for sneakers, dress shoes, boots and traditional footwear. Mixed for running/outdoor, sandals and heels. Tier for slippers and care.

Size: 10 departments, 84 kinds, 275 archetypes, 378 versions; 848 brands; 13 traditions.

### Gaps for hobbyists
- **A2-1 Air Jordan line squashed into one archetype.** "Air Jordan III", "IV" and "XI" are stored as versions of the Air Jordan 1 archetype. Basketball sneaker has only 8 archetypes. There is no Foamposite or Air More Uptempo, and no "Air Jordan 3" or "11" anywhere in the data. **Fix:** create an Air Jordan kind (or shelf) with one archetype per numbered model (AJ1–AJ14 at least, to verify). Add Foamposite, adidas Forum and Kobe/LeBron signature lines.
- **A2-2 Missing lifestyle icons.** These have no archetypes anywhere: Yeezy Boost 350 (it appears only in brand registers), Air Huarache, Air Presto, New Balance 550 and 2002R, Salomon XT-6, Gel-Kayano 14 retro, brothel creeper, Buffalo platform (to verify). **Fix:** add them under Heritage running, Chunky/tech and a new "Subculture shoes" shelf (creepers, Dr. Martens 1461, Rocking Horse).
- **A2-3 Catch-all archetypes.** "Air Max family (other models)" holds 11 versions and "99X numbered models" holds 9. These are SKU lists dressed as archetypes. Air Max 1/90/95/97/Plus have 0 versions each. **Fix:** promote BW, 180, 93 and VaporMax to archetypes, and give each Air Max OG colourways by style code.

### Too much detail
- **A2-4 Kinds with no archetypes and no types:** Walking shoe, Insole, Heel grip, and Shoe polish and waterproofing. "Peep-toe shoe", "Bootie" and "Heeled sandal" have 0 archetypes and are really attribute kinds. **Fix:** make peep-toe a `t` of Court shoe. Merge insole and heel grip into one "Fit aids" kind.

### Confusing organisation
- **A2-5 Duplicate department.** There are two departments: "Shoe care & accessories" and a second "Shoe care" whose single kind, "Shoe polish and waterproofing", duplicates "Shoe polish and conditioner". **Fix:** delete the second department and merge its models.
- **A2-6 Duplicate archetypes.** Triple S appears under both Chunky sneaker and Designer sneaker. "Rubber-soled jika-tabi" appears under both Jika-tabi and Split-toe work boot. Margiela Tabi sits under traditional Jika-tabi. The Vans Classic Slip-On is a one-archetype kind next to Skate shoe. **Fix:** make Chunky a `t` of Designer/Running, merge Split-toe into Jika-tabi, move Margiela Tabi to Designer, and fold Slip-on into Skate shoe.
- **A2-7 Register errors.** The Adidas brand entry carries seg "Designer" and kf "sports watches" because it was first registered from A5. Archetype `mk` uses "adidas" and "ASICS", which do not match the register names "Adidas" and "Asics". Tradition groups use both "Footwear & leather" and "Leather & footwear". **Fix:** correct the Adidas entry and unify the names.

### What it would look like (Sneakers › Basketball)
```
Air Jordan (Nike/Jordan Brand)
  Air Jordan 1 → High OG 1985 · Mid · Low · retro 1994/2001+ → colourway by style code
  Air Jordan 3 → 1988 OG · retro → Black Cement, White Cement…
  Air Jordan 4 / 11 / … → same pattern
Air Force 1 → Low · Mid · High → collabs
Dunk → Low · High · SB
Foamposite One → 1997 OG · retro
```
Priority: high
Fix size: medium

---

## A3 Jewellery

**Brand mode:** variety. Mixed for piercing jewellery, which is bought on material grade. Tier for parts.

Size: 11 departments, 99 kinds, 197 archetypes, 175 versions; 455 brands; 18 traditions.

### Gaps for hobbyists
- **A3-1 Earrings are thin.** 10 kinds hold only 9 archetypes. Six kinds are completely empty: Huggie, Chandelier, Threader, Ear jacket, Ear climber, Ear cuff. Stackable ring is empty too. **Fix:** turn the six into `t` types of Stud/Hoop/Drop. Add archetypes such as Dior Tribales ear jacket, Maria Tash ear stacking, Chanel CC hoops, and vintage clip-ons by Haskell and Trifari (to verify).
- **A3-2 Versions are sparse.** 108 of 197 archetypes have no versions. Love, Alhambra, Juste un Clou and Serpenti need sizes, materials and the original-versus-current split (e.g. Love bracelet 1969 screwdriver versus small model, to verify).
- **A3-3 Missing forms.** A grep across all files found none of these: jade bangle (a major Chinese tradition), class/college ring, mood ring, poison ring, memento mori ring, evil-eye and cornicello amulets, Hawaiian heirloom jewellery. There are no tradition entries for Chinese jade, Taxco silver or Scandinavian modernist silver. Religious pendants live in F4, so cross-link rather than duplicate them. **Fix:** add the missing kinds and archetypes, plus Chinese jade and Taxco traditions.

### Too much detail
- **A3-4 Repeated shape lists.** Solitaire (17 types), Halo (14) and Three-stone (15) each repeat the same 10 "shape:" types. **Fix:** declare stone shape once at department level as a detail axis.
- **A3-5 Piercing near-duplicates.** Seamless ring, Captive bead ring, Clicker ring and Nose ring overlap: Nose ring's types are exactly seamless, captive and clicker. **Fix:** make one "Piercing ring" kind with fastening as `t`, and treat placement (nose, septum, daith) as a tag.
- **A3-6 Parts.** "Jewellery parts" has 3 kinds (earring back, chain extender, ring guard). **Fix:** replace them with one "Spare parts" entry.

### Confusing organisation
- **A3-7 Mixed axes.** Most departments are by body location, but "Hip-hop jewellery" is a scene department and "Traditional & regional" is a tradition department. As a result, Cuban and rope chains are separate from "Necklace chain", and tennis chains are split. **Fix:** move Cuban, rope and grillz into their location kinds and expose hip-hop as a By-scene view.
- **A3-8 Brand lines scattered.** Juste un Clou appears 3 times (ring, stud, bangle). Serpenti appears twice (pendant, cuff) plus a watch in A5. Alhambra appears 3 times. **Fix:** keep each range once as a register line, with the per-kind entries pointing to it.

### What it would look like (Earrings)
```
Stud → Diamond solitaire (martini/basket) · Pearl · Alhambra · Juste un Clou
Hoop → Creole · Sleeper · Huggie [t] · Chanel CC hoop
Drop → Teardrop · Chandelier [t] · Threader [t] · Jhumka (→ South Asian)
Ear cuff & jacket → Dior Tribales · Maria Tash cuff
Clip-on → Haskell, Trifari vintage (period view)
```
Priority: medium
Fix size: medium

---

## A4 Bags & Accessories

**Brand mode:** variety for handbags, wallets, trunks and fans. Mixed for eyewear, backpacks, luggage and umbrellas. Tier for baby carriers.

Size: 9 departments, 95 kinds, 226 archetypes, 407 versions; 616 brands; 11 traditions.

### Gaps for hobbyists
- **A4-1 Hermès and resale icons missing.** Hermès has Birkin, Kelly, Bolide, Garden Party and Twilly. Evelyne, Picotin, Lindy, Herbag and the Constance bag appear only in brand-register text. Balenciaga City, YSL Loulou and Sac de Jour, Celine Luggage, Gucci Dionysus and Telfar Shopping Bag have no archetypes. **Fix:** add them as archetypes, with versions by size and leather.
- **A4-2 No basket or straw bags.** There is no basket or straw bag kind, and no bag-craft traditions: Wayuu mochila, PNG bilum and Kenyan kiondo all return no hits. Only 2 of the 11 traditions concern bags. **Fix:** add a "Basket & woven bag" kind and these traditions.
- **A4-3 Eyewear is thin and skewed to one maker.** 17 kinds hold 27 archetypes. "Trapezoid frames" has only the Wayfarer. Ray-Ban is `mk` on 6 archetypes and owns all 3 Geometric models. Cazal, Mykita and Gentle Monster exist only as brands. There is no monocle, pince-nez or lorgnette for antique eyewear. **Fix:** add Cazal 607, Ray-Ban Olympian/Round and Persol 714 versions (to verify), plus an antique-eyewear shelf.

### Too much detail
- **A4-4 Boilerplate and empty kinds.** 10 frame kinds repeat the same 5 lens types. "Prescription sunglasses", "Spectacle frame" and "Wristlet bag" are empty. Fashion cane, Shopping trolley and Crossbody bag have no types or archetypes. **Fix:** declare lens type once at department level and delete the empty kinds.
- **A4-5 Retail skew.** Prescription glasses list 3 Warby Parker models, and its `r` lists brands as "ranges" of EssilorLuxottica. Reading glasses are 4 Foster Grant models. **Fix:** tier these to market-covering brands plus test winners.

### Confusing organisation
- **A4-6 Inconsistent bag axis.** Doctor, Barrel, Baguette and Saddle bag are kinds with 1 archetype and 0 types each, while Shoulder bag lumps 13 icons. **Fix:** use shape kinds throughout (Flap, Hobo, Baguette/east-west, Saddle/half-moon, Bowling/Boston, Box/vanity). Move icons such as 2.55, Boy and 19 to Flap.
- **A4-7 Confusing labels.** "Wallet on chain" and "Chain wallet" are different objects but read alike. "Trapezoid frames" would not be guessed for Wayfarers. **Fix:** rename them "Wallet on chain (bag)", "Biker chain wallet" and "Wayfarer-style frames".

### What it would look like (Handbags › Flap & shoulder)
```
Flap bag
  Chanel 2.55 → 1955/1990s reissue → mini · small · medium · jumbo → lambskin/caviar → hardware
  Chanel Classic Flap (11.12) · Boy · 19
  Gucci Horsebit 1955 · Celine Triomphe
Hobo → Gucci Jackie 1961 · Bottega Jodie · Balenciaga City
Saddle / half-moon → Dior Saddle · Coach Tabby
```
Priority: high
Fix size: medium

---

## A5 Clocks & Watches

**Brand mode:** variety for wristwatches, pocket watches, collectible clocks and modding parts. Tier for everyday clocks, timers and storage.

Size: 7 departments, 74 kinds, 247 archetypes, 668 versions; 397 brands; 6 traditions.

### Gaps for hobbyists
- **A5-1 Detail axis missing.** 183 of 247 archetypes have no `dt`, and every wristwatch kind has 0 `t`. Seiko 62MAS, the Tuna and the C60 have no case size, material or dial axis. **Fix:** add `dt` (case mm · material · dial · bezel · bracelet) to every archetype, copying Watchbase's reference fields.
- **A5-2 Missing icons:** Tissot PRX, Seiko Alpinist, Bulova Lunar Pilot, Heuer Camaro, Rolex Cellini and IWC Portofino have no A5 hits (to verify each is not elsewhere under another name). Collectible clocks are missing Japanese wadokei, American ogee/steeple shelf clocks, Telechron electrics and flip/Solari clocks (Solari is only in D3). **Fix:** add the watches as archetypes. Add a "Collectible electric & design clocks" shelf and wadokei.
- **A5-3 Only 6 traditions.** Missing: Japanese wadokei, Vienna clockmaking, the American clock industry (Connecticut) and Russian/Soviet watchmaking (to verify).

### Too much detail
- **A5-4 Empty kinds (0/0/0):** Dial clock, Tower clock, Travel clock, Time clock, Watch clasp, Watch spring bar, Watch crown. Tower and time clocks are institutional, so the scope rule drops them. **Fix:** remove tower and time clocks. Merge clasp, spring bar and crown into one "Small watch parts" kind.
- **A5-5 Complications as kinds.** "Moon-phase", "Minute-repeater" and "One-hand" have 0 archetypes each, and "Perpetual-calendar" and "World-time" have 1. **Fix:** make complications a `t`/filter view. Keep only Chronograph and Calendar & chiming as shelves with archetypes.

### Confusing organisation
- **A5-6 Catch-all kinds.** "Dress watch" (33 archetypes) and "Everyday watch" (13) are catch-alls. Day-Date, Lange 1 and Ballon Bleu are not dress watches in the narrow sense, and Yacht-Master and Milgauss are sports watches filed under "Everyday". **Fix:** split into "Dress watch" (thin, time-only), "Prestige everyday" (Datejust, Day-Date, Oyster Perpetual) and "Shaped watch" (Tank, Reverso, Crash, Tonneau). Move Yacht-Master to Dive and Milgauss to Field.
- **A5-7 Duplicate Submariner names.** Rolex "Submariner" and Tudor "Oyster Prince Submariner" sit side by side, as do "Seamaster 300" and "Seamaster Diver 300M". This works, but the labels confuse. **Fix:** label each archetype with its maker, e.g. "Tudor Submariner".

### What it would look like (Wristwatches › Dive watch, Rolex lineage)
```
Submariner (Rolex, 1953)
  6204/6205 → 6536/6538 "Big Crown" → 5512/5513 → 1680 → 16610 → 116610 → 126610
  dt: case 37–41 mm · steel/gold · black/blue dial · Oyster bracelet
Sea-Dweller → 1665 "Double Red" → 16600 → 126600
Tudor Submariner → 7922 … 9411/0 "Snowflake" → Black Bay (homage line)
```
Priority: medium
Fix size: medium
