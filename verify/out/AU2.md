# AU2 — Cold audit of CATEGORIES_R2.md (top level only)

Auditor stance: independent classification designer (museum cataloguing, product taxonomy, thesaurus construction). Source read: `audit/CATEGORIES_R2.md` only. No other repository file, no web, no git.

**Notes before the findings**
- The brief speaks of "the catch-all step 27". In this draft step 27 is C2 Garden & Grounds. The broad tools step is **step 31 (C1)** and the holding bin is **step 32 (X0)**. I read "step 27" in the brief as meaning step 31/32 and audit those.
- The file header reads "v0.1 … revision 1", but the file is named R2. Fix the header so later audits cite the right revision.
- Count: 43 placing categories plus X0 = 44; 9 domains (A–I) plus the X holding domain.
- Severity: **high** = misfiles common objects or breaks a stated rule; **medium** = misfiles a recognisable class or leaves a reader with two answers; **low** = edge case or cosmetic.
- Every "Fix" gives exact wording. Text in quotes replaces the text named, or is added where stated.

---

## Part 1 — Key mechanics and wording that governs everything

### 1. Parenthetical notes have no stated status in the key
- **Type:** wording / rule contradiction · **Severity:** high
- **Examples:** greenhouse (step 3's lead claims it as "a building … made to be entered"; its note says C2); dried flowers (step 6's lead, "made by nature … prepared", claims them; step 5's note says B4); a stable block (step 3 lead claims it; note says animal housing is B11); a playhouse (step 3 vs note: E1).
- **Problem:** "The placement key is authoritative. Category descriptions and precedence notes restate the key." A reader can take the parentheticals as "precedence notes", which lose to the key, so the greenhouse lands in G2. The draft needs the notes to bind, but never says so.
- **Fix:** add after S1a: "**S1b Notes bind.** A note in brackets inside a step is part of the key. It takes the objects it names out of that step and sends them on to the step or category it names. Where a note and a lead question disagree, the note wins."

### 2. Step 15's lead question ("Worn on the body") leaves out its own A4 examples
- **Type:** wording / key-order trap · **Severity:** high
- **Examples:** suitcase, wheeled carry-on (step 10's note says A4), umbrella, wallet in a drawer, keyring, hand fan, shopping tote, briefcase.
- **Problem:** By S1a the lead question must be *yes* before a branch can apply. A suitcase is not worn, so it skips step 15. It then reaches step 29 / B7 ("carry household things"), and A4 loses the things it was built for.
- **Fix:** replace the step 15 lead with: "**Worn on the body, or carried on the person or in hand as a personal accessory** (bags and luggage of every kind, wallets, umbrellas, keyrings, hand fans)."

### 3. Step 22's lead question ("powered electronic device") leaves out its own D4 and D5 examples
- **Type:** wording / axis break (power source) · **Severity:** high
- **Examples:** tripod, roll of film, darkroom tray, manual film SLR, reflector, a video-game disc or cartridge.
- **Problem:** None of these is a powered electronic device, so the lead is *no* and the branches are never reached. The note "This branch also takes non-powered photographic equipment" contradicts S1a. The lead also files by technology, which Appendix A lists as a modifier.
- **Fix:** replace the step 22 lead with: "**An electronic device made for computing, communication, picture-taking, gaming, or playing or receiving sound and pictures; or any equipment for photography; or a video game on a physical carrier:**". Delete "(This branch also takes non-powered photographic equipment.)".

### 4. Other leads that fail their own examples under S1a
- **Type:** wording · **Severity:** medium
- **Examples by step:**
  - Step 16 (H1): pacifiers, teethers and "massagers for comfort" are not grooming, hygiene, cosmetics or fragrance.
  - Step 23 (E1): fireworks are not "made for play or for games".
  - Step 31 (C1): fuels, packing materials and household batteries are not "for building, repair and electrical work".
  - Step 29 B2: swaddling cloths do not "cover, soften or dress beds, floors, windows, seats and tables".
  - Step 29 B9: door stops do not "secure or protect".
  - Step 29 B1: playpens are not for sitting, lying, working at, display or storage.
  - Step 9 (E4): fencing foils and target bows are not "made to injure or kill".
- **Fix (exact replacements):**
  - Step 16: "Made to be used on the body for grooming, hygiene, cosmetics, fragrance **or bodily comfort and soothing** …"
  - Step 23: add "**and fireworks and other pyrotechnics for celebration**" after "Made for play or for games". Or, better, move fireworks to B4: add "fireworks, sparklers and party poppers" to the B4 branch and delete them from E1.
  - Step 31: "… or **materials, hardware and supplies for building, repair, electrical work, packing, or powering and fuelling household machines** …"
  - B2: "made to cover, soften or dress beds, floors, windows, seats and tables, **or to wrap or dry the body (towels, swaddling cloths)**".
  - B9: "made to secure or protect a home, its people and its contents, **or to hold doors and windows**, or to keep pests out".
  - B1: "furniture: made to sit, lie, work at, display or store things on or in, **or to hold a small child in place (cots, high chairs, playpens)**".
  - Step 9: see Finding 20.

### 5. Branch order inside step 29 is used but never declared
- **Type:** wording / overlap · **Severity:** medium
- **Examples:** plain candle (B3 "give light" comes before B4, which lists "candles"); fairy lights and Christmas string lights (B3 or B4); lava lamp and neon wall sign (B3 or B4); electric blanket (B8 "heat" comes before B2 "cover beds"); kettle and water-filter jug (B5 or B8: order happens to save them).
- **Fix:** add to S1a: "Branches are tried in the order printed; the first branch that fits wins." Then add to B3: "(Candles, string and fairy lights, lava lamps and neon signs made mainly as decoration are B4.)" and to B8: "(Electric blankets and heated throws are B2.)"

### 6. S2 wording invites "one-of-a-kind objects are out of scope"
- **Type:** wording / scope · **Severity:** low
- **Examples:** an original oil painting, a family letter, a meteorite, a hand-built house.
- **Fix:** replace "Unique individual items are out." with "**An individual item is never a kind; a one-of-a-kind object is filed under the generic type it belongs to (an original painting under 'painting').**" Replace "A kind is a generic type someone has one of" with "A kind is a generic type of object a person can own."

---

## Part 2 — Scope (step 1 and the scope lines)

### 7. Step 1 puts every licence OUT before step 4 can take digital licences IN
- **Type:** scope / rule contradiction · **Severity:** high
- **Examples:** a purchased e-book or film (a "licence entitlement"), a software licence key, a font licence, a domain-name registration, an in-game skin.
- **Problem:** Step 1 puts "a right, claim … licence to use a place … intellectual property" OUT, and step 1 comes first. A careful reader stops at step 1 for every licensed digital good, so I1 empties.
- **Fix:** add to the step 1 brackets: "**A digital item held as a file, licence entitlement or registered token (e-book, software, font, domain name, NFT) is not a right in itself: go to step 4.**"

### 8. Step 1 (food OUT) runs before step 5 (living cultures IN)
- **Type:** scope / key-order trap · **Severity:** medium
- **Examples:** sourdough starter, kombucha SCOBY, kefir grains, live yoghurt culture, brewer's and baker's yeast, fresh-cut culinary herbs (cut basil vs. cut tulips).
- **Problem:** A sourdough starter is "a substance made to be eaten", so it is OUT at step 1, against step 5's own example.
- **Fix:** add to the step 1 brackets: "**Living cultures kept to grow or propagate (sourdough starter, kombucha and kefir cultures, mushroom spawn) are step 5, even when what they make is eaten.**" Add to step 5: "(Cut herbs, sprouts and microgreens sold as food are OUT.)"

### 9. Land and the burial plot are IN, yet "licence to use a place" is OUT
- **Type:** scope inconsistency · **Severity:** medium
- **Examples:** a burial plot held as an exclusive right of burial (the common tenure in the UK and many other places), a cemetery niche, an allotment tenancy, a boat mooring, a leasehold flat, a beach hut on a licensed pitch, a timeshare.
- **Problem:** Whether something is "land" or "a right" depends on the legal form of tenure, which is not designed function. The draft rules in two of the examples above and out the rest without a principle.
- **Fix:** step 3: replace "a burial plot held as land" with "**a burial plot or niche, however it is held**". Step 1: replace "licence to use a place, timeshare" with "**a licence, tenancy or timeshare to use a place that the person does not hold as land, a building or a burial plot (allotment tenancy, mooring, timeshare week)**".

### 10. Physical tokens of OUT things have no home
- **Type:** scope / gap · **Severity:** medium
- **Examples:** plastic gift card, credit or debit card, transit smartcard, hotel keycard, membership card, a game-key card (a cartridge that holds only a download licence), a hardware crypto wallet, casino chips.
- **Problem:** Step 1 says physical tokens of rights are objects and names only share certificates, tickets, coins and banknotes. A gift card is neither "issued to prove identity, status, ownership or achievement" (F5) nor clearly "money … in physical form" (F3).
- **Fix:** add to step 17's lead: "… or a **card, pass or token issued to give access to an account, service, place or stored value (payment, gift, transit, membership and key cards)** …". Add to step 22 D1: "hardware wallets and security keys". Add to step 23: "casino and poker chips". Add to step 22 D5: "game-key cards (physical carriers that hold only a licence)".

### 11. The alcohol exception is filed by motive, and tobacco is called a food
- **Type:** scope / axis break (S5 motive) · **Severity:** medium
- **Examples:** a cellared Bordeaux (in) vs. aged pu-erh tea cakes, vintage balsamic vinegar or a collector's bottled water (out); non-alcoholic spirits (out); beer in a keg or cask, boxed wine, homebrew in a demijohn ("bottled"?); cannabis flower, herbal smoking blends, nicotine pouches (no home: step 25 names only "tobacco products").
- **Problem:** "kept as stock" is a motive test, which S5 forbids. "Food and drink are out … except … tobacco" implies tobacco is food.
- **Fix:** scope line: "Food and drink are out (the Culinary taxonomy covers them), except **alcoholic drinks in sealed containers kept for later use** (B10). **Tobacco, cannabis and other products made to be smoked, vaped, chewed or snuffed for their effect are in** (B10)." Step 25: replace "Bottled alcoholic drinks kept as stock" with "**Alcoholic drinks in sealed containers (bottle, can, keg, cask, box)**", and replace "tobacco products" with "**tobacco, cannabis, herbal and nicotine products made to be smoked, vaped, chewed or snuffed**". Medicinal nicotine (gum, patches) stays H2.

### 12. Body-derived keepsakes and human remains are not addressed
- **Type:** scope / gap / key-order trap · **Severity:** low
- **Examples:** cremated ashes, a lock of a child's hair, baby teeth, a keepsake umbilical cord, a saint's relic.
- **Problem:** By step 6 ("made by nature … kept as found") these become F6 Natural History, which is a surprising answer. The relic loses to F6 because step 6 runs before step 12.
- **Fix:** step 1: add "**human remains (ashes, bones, hair and teeth kept as remains)**" to OUT, with the bracket "(The urn, reliquary or keepsake box holding them is filed as that object: F4 or B7.)" If keepsakes must be in, add them instead to step 17: "**keepsakes of the owner's or family's body (locks of hair, baby teeth)**".

### 13. "Devices implanted in the body are H2" files by location, not function
- **Type:** scope / axis break · **Severity:** low
- **Examples:** cosmetic breast implants (cosmetic surgery is OUT, the implant is H2?), a hobbyist's RFID/NFC chip implant for door access, a pet microchip, a contraceptive implant (correctly H2).
- **Fix:** replace the bracket text with: "(Devices placed in the body to treat, monitor or compensate for a condition, or for contraception, are H2. Other implants are part of a change to the body and are OUT. Animal identification microchips are B11.)"

---

## Part 3 — Overlaps

### 14. S3 "made for one kind" vs "made for a class" has no working line
- **Type:** overlap / rule contradiction · **Severity:** high
- **Examples:**
  - Storage made for one kind of thing, which S3 sends with that thing: bookcase (books are one kind, yet B1 by fiat), wine rack (B1 by fiat), TV stand (S3 says "stands made to hold one kind of object are parts" → D3, though it is furniture), garment bags (S3 → A1, but B7 lists them).
  - Other storage S3 would also send with its contents: clothes hangers (→ A1), shoe rack (→ A2), coat hooks (→ A1), key hooks (→ B9), umbrella stand (→ A4), magazine rack and bookends (→ F1), CD/record crates (→ F1), jewellery box (→ A3), humidor (→ B10, but step 25's note says B1/B7), spice rack and knife block (→ B5), watch winder (→ A5).
- **Problem:** "One kind of object" vs. "a class of things" is not a decidable distinction: books are both. The key (step 7) also overrides the B7 description, which lists garment and shoe bags.
- **Fix:** replace S3's second and third sentences with: "**Cases, bags, covers and stands are parts only when they are made to hold, carry or protect one object at a time and travel or stand with it (a phone case, a guitar case or stand, a golf bag, a camera bag, a watch strap). Furniture, racks, shelves, hooks, hangers, boxes and other storage that hold several objects, or that stand in a room as a piece of furniture, are never parts, whatever they are made to hold: furniture is B1, containers and organisers are B7, safes are B9.** Anything for growing plants (pots, compost, plant food, grow lights) is C2." Then delete from step 25 "Wine racks and humidors are B1 or B7".

### 15. Step 7 (parts) catches worn protective gear before step 15
- **Type:** overlap / key-order trap · **Severity:** medium
- **Examples:**
  - Riding gear S3 calls "accessories for" a vehicle: motorcycle helmet, motorcycle jacket and boots, and a bicycle helmet, each → G1.
  - PPE S3 calls "accessories for" a machine or appliance: welding helmet (→ C1), chainsaw trousers (→ C1 or C2), oven gloves (→ B5), shooting ear defenders (→ E4).
  - Meanwhile, a hard hat and ear defenders for work go to A1 at step 15, and a riding helmet goes to E2.
- **Fix:** add to S3: "**Nothing worn on the body is a part: garments, footwear, helmets and personal protective equipment go to step 15, whatever object or activity they are made for.**" Extend the A1 branch: "… or **protective clothing, helmets and personal protective equipment made to protect the wearer from a hazard (hard hat, motorcycle and cycling helmets and riding gear, welding helmet, chainsaw trousers, safety glasses, respirator, ear defenders, hi-vis)**". Sport-specific protection still goes to E2 by the step 15 sport rule. Oven gloves stay B5: add to B5 "oven gloves and aprons".

### 16. Step 7 consumables split cleaning products and fuels
- **Type:** overlap · **Severity:** low
- **Examples:** dishwasher tablets, rinse aid and dishwasher salt (S3 → B5), but washing-up liquid → B6; barbecue charcoal (S3 → B5), but other fuels → C1; descaler for kettles (→ B5).
- **Fix:** add to S3: "**Cleaning products are B6 and fuels are C1, whatever they are used in.**"

### 17. Step 2 (health) is not limited to people, so veterinary goods leave B11
- **Type:** overlap / key-order trap · **Severity:** medium
- **Examples:** flea and worming treatments, a dog's cone (Elizabethan collar), horse leg wraps and poultices, a pet wheelchair, a pet first-aid kit, a livestock drench gun.
- **Problem:** Step 2 runs before step 11 and says only "an illness, injury or disability", so all of these go to H2 Health. B11's own list says "grooming and care equipment".
- **Fix:** step 2 lead: "Made to diagnose, treat, monitor or compensate for an illness, injury or disability **of a person**, …". Add to step 11: "**including veterinary medicines, treatments and care equipment**".

### 18. "Compensate for a disability" files adapted ordinary objects by user
- **Type:** overlap / axis break (user modifier) · **Severity:** medium
- **Examples:** braille book or large-print book (F1?), talking or braille watch (A5?), big-button phone (D2?), adapted cutlery (B5?), wheelchair-accessible car (G1?), vibrating alarm clock, closed-caption TV box.
- **Problem:** Step 2 runs first, so all of these go to H2. Yet Appendix A says the user is a modifier.
- **Fix:** add to step 2's brackets: "**An ordinary object made in an adapted form for a disabled user (large-print or braille book, talking watch, big-button phone, adapted cutlery, wheelchair-accessible vehicle) is filed as that object; 'adapted' is a modifier. H2 takes objects whose function exists only because of the condition (wheelchair, hearing aid, stairlift, grab bar, white cane).**"

### 19. Weapon test verbs catch pest tools and sport implements
- **Type:** overlap / wording · **Severity:** medium
- **Examples:**
  - Made to kill an animal by striking: fly swatter, electric bug zapper, mole trap (the step 9 note names only "pest traps").
  - Livestock and fishing tools: captive-bolt stunner for livestock (→ E4 by "firing"), speargun (E4 or E2 fishing?).
  - Not covered by the verbs: a taser and a contact stun gun (neither strikes, cuts nor shoots), though pepper spray, which sprays, is listed.
  - Tools that can be weapons: machete, felling axe.
- **Fix:** replace step 9's lead with: "**A weapon: made for fighting, self-defence or hunting, by striking, cutting, shooting, firing, spraying or electric shock (firearms, air guns, bows and crossbows, swords, fighting and hunting knives, martial-arts weapons, pepper spray, stun guns and tasers); armour made to protect against such weapons; ammunition?**" Add to its brackets: "Tools made to kill pests (swatters, zappers, traps, poisons) are B9; slaughter and stunning tools for livestock are C7; spearguns and other fishing tackle are E2; machetes and axes made for cutting wood or vegetation are C1 or C2."

### 20. Sport weapons and their armour are split between E4 and E2
- **Type:** overlap / granularity · **Severity:** medium
- **Examples:** fencing foil (E4 under "weapons made for … fencing") vs. fencing jacket and mask (E2 as "padded sport armour"); shinai and bokken (E4 as "martial-arts weapons") vs. kendo bogu (E2); target recurve bow (E4) vs. arm guard and target boss (E2?).
- **Problem:** The lead says "made to injure or kill", but foils and shinai are made not to. One sport's equipment is split across two categories.
- **Fix:** step 9: replace "including such weapons made for target shooting or fencing" with "**including firearms, air guns, bows and crossbows made for target shooting**". Add to the brackets: "**Blunted or padded implements made for a combat sport (fencing foils, épées and sabres, shinai, bokken, training weapons) and the protective gear for them are E2.**"

### 21. Step 10 transports "people or goods" only; "gliders made for a sport" is ambiguous
- **Type:** overlap / wording · **Severity:** medium
- **Examples:**
  - Animals are not "goods": horsebox and livestock trailer (G1 or B11 carrier?), dog bike trailer.
  - "Gliders made for a sport are E2" also catches a sailplane, which is a registered aircraft.
  - Unclear whether sport craft are boats (G1) or sport equipment (E2): racing kayak, rowing shell, racing dinghy, track bicycle, snowmobile, jet ski.
- **Fix:** step 10 lead: "Made mainly to transport people, **animals** or goods …". Replace "Unpowered boards, skates, skis, sledges and gliders made for a sport are E2" with "**Boards, skates, skis, sledges, hang gliders and paragliders made for a sport are E2. Every boat, canoe, kayak, bicycle and aircraft is G1, including those made for racing.**"

### 22. Step 12's "rite of passage" files by occasion, which Appendix A calls a modifier
- **Type:** axis break / overlap / key-order trap · **Severity:** high
- **Examples:**
  - Items step 12 claims before step 15: plain wedding ring (the brackets save only "jewellery in a religious form", so it goes to F4, not A3), wedding dress, christening gown, graduation gown and mortarboard, quinceañera dress (each F4, not A1: the brackets save only "religious dress").
  - Wedding paraphernalia that also goes to F4: wedding guest book, cake topper, ring pillow.
- **Problem:** Appendix A lists "occasion (wedding, festival, season)" as a modifier, and S5 says test the object. Step 12 contradicts both.
- **Fix:** replace step 12's lead with: "**Made for use in religious or spiritual practice, or to hold, mark or accompany the dead**: altars, shrines, icons, prayer beads, tefillin, ritual vessels, lamps, instruments and implements, religious festival objects used in worship (menorah, diya, Advent wreath, home nativity set), coffins and caskets, cremation urns, grave markers?" Add to the brackets: "**Objects for weddings, christenings, graduations and other occasions are filed as what they are: occasion is a modifier.**"

### 23. Step 12 vs B4: festival décor, incense, divination, worn amulets
- **Type:** overlap / wording · **Severity:** medium
- **Examples:**
  - Festival décor: Christmas tree and baubles (religious festival object or "secular seasonal decoration"?), Easter egg decorations, Diwali string lights, Hina dolls (listed F4) vs. Halloween décor (B4).
  - Incense: incense sticks bought as home fragrance (step 12 takes all incense before B4's "home fragrance").
  - Spiritual practice vs. ordinary objects: meditation cushion (F4 vs. B2), tarot deck (F4 divination, or E1, since tarot is also a card game), Ouija board (sold as a board game), healing crystals (F6 first, by step 6), smudge sticks.
  - Worn amulets: evil-eye pendant, St Christopher medal, Hamsa bracelet (F4 "amulets" vs. A3 "jewellery in a religious form").
- **Fix:**
  - Add to step 12's brackets: "**Decorations for any festival, religious or secular (Christmas trees and ornaments, Easter, Diwali and Halloween décor), are B4 unless made for use in worship. Incense and incense burners are F4 only when made for a rite; home-fragrance incense is B4. Anything worn as an ornament, including amulets worn as pendants, rings or bracelets, is A3. Tarot and oracle decks are F4; card and board games are E1.**"
  - Move "festival display dolls" to B4 unless they are used in a rite.

### 24. Figures, figurines, models and collectibles are claimed by four steps
- **Type:** overlap / axis break (acquisition, edition) · **Severity:** high
- **Examples:**
  - A Lladró or Hummel porcelain figurine: F3 (step 13, "made only to be collected"), E1 (step 13 note, "figures sold as collectible series"), or F2 (step 18, "figurines, whatever the edition")?
  - Funko Pop: E1 by note, but also F3.
  - A garden gnome or concrete garden Buddha: F2 "free-standing sculpture" (step 18) before B4 "garden ornaments" (step 29).
  - A commemorative plate: F3, though it is a plate.
  - A painted Warhammer miniature: E1 "figures" (step 23) or C4 "model kits (built or not)" (step 26).
  - A built Airfix Spitfire (C4) vs. a ready-made Corgi Spitfire (E1). This is the same kind of object split by how it was acquired, which the axis paragraph forbids.
- **Fix:**
  - Step 13: delete "or an object made only to be collected" and "commemorative series made for collecting". The test becomes "**Money, postage or an award in physical form**", plus "non-game trading cards" kept explicitly.
  - Step 18: replace "including figurines" with "**including ornamental figurines of people and animals made in ceramic, glass, metal, stone, wood or resin**", and extend its brackets: "**Figures of characters, action figures, vinyl and collectible-series figures, and bobbleheads are E1. Garden statues and gnomes are B4.**"
  - Step 23: add "**scale models, model kits and miniatures, built or not, ready-made or not**". Step 26: delete "model kits (built or not)" and add "**paints, glues and tools made for model-making**".
  - Add to S5: "**A commemorative plate is a plate; a commemorative coin is a coin.**"

### 25. Award vs. document: diplomas and award certificates
- **Type:** overlap · **Severity:** low
- **Examples:** a diploma, a framed award certificate, an engraved award plaque, a sports participation certificate.
- **Problem:** Step 13 ("an award in physical form") runs before step 17 ("certificate, diploma"), so diplomas become F3.
- **Fix:** step 13: "**an award made as a medal, decoration, trophy, cup, shield or plaque (paper certificates and diplomas are step 17)**".

### 26. Step 14 (timepieces) takes smart clocks and clock radios before step 22
- **Type:** overlap · **Severity:** low
- **Examples:** smart display clock with voice assistant, clock radio, sunrise alarm lamp, hybrid analogue smartwatch, kitchen timer, hourglass, sundial, sport stopwatch.
- **Fix:** step 14: "A **timepiece**: a watch or clock whose main function is to show the time, of any kind? (Smartwatches, hybrid smartwatches and smart displays are D2/D3. Clock radios are D3. Sunrise lamps are B3. Kitchen timers are B5. Sundials made as garden ornaments are B4. Stopwatches are A5.)"

### 27. E3 (music gear) vs. D3 (listening): one object, two homes
- **Type:** overlap / wording · **Severity:** medium
- **Examples:**
  - Studio monitor headphones: E3, though D3 says "headphones of any kind".
  - Studio monitor speakers.
  - Direct-drive turntable: DJ equipment (E3) or record player (D3)?
  - USB microphone bought for podcasts and video calls: E3, not D1.
  - Karaoke machine.
  - Music box, wind chimes (step 20 runs before B4).
- **Fix:** step 20's brackets: "(Toy instruments are E1. **Headphones, turntables and speakers are D3 unless sold as studio, stage or DJ equipment. Microphones made for speech, calls or streaming are D1. Karaoke machines are D3. Wind chimes are B4. Music boxes are E3.**)"

### 28. F5 vs. F2/C5: split by maker and by condition
- **Type:** overlap / axis break (maker, condition) · **Severity:** medium
- **Examples:**
  - Split by maker: a framed family photographic print (F5, "made by or for its owner") vs. a commissioned family portrait in oil (F2); a hand-drawn house plan (F5) vs. an architect's presentation drawing hung as art.
  - Split by condition: a written postcard (F5) vs. an unused vintage picture postcard bought for a collection (C5 Office & Stationery); a written diary (F5) vs. a blank diary (C5).
- **Problem:** Appendix A makes maker and condition modifiers.
- **Fix:**
  - Add to Appendix A, after "condition": "(**being written, drawn or recorded on is not condition: paper goods become records when used, see step 17**)".
  - Step 17: replace "personal photographic prints" with "**photographic prints and slides of the owner's own life, family and places (photographs made as art are F2)**".
  - Step 30: add "(**Picture postcards, used or not, are F5; postcards are collected as records.**)"

---

## Part 4 — Key-order traps

### 29. Step 6 ("made by nature") is far too broad for its early position
- **Type:** key-order trap / wording · **Severity:** high
- **Examples:**
  - Fuel and building or garden material: firewood and kindling (→ F6, not C1 fuels), river stones and pebbles for a garden, driftwood décor.
  - Natural objects used on the body: pumice stone, natural sea sponge, loofah (→ F6, not H1).
  - Animal equipment: antler dog chew, cuttlefish bone for a budgie (→ F6, not B11).
  - Craft materials: craft feathers, raw wool fleece for spinning, seashells bought for craft (→ F6, not C4).
  - Flowers and pictures: dried lavender bunch (step 5's note says B4, but step 6 runs first), pressed-flower picture.
  - Religious objects: rudraksha seeds, a relic.
- **Problem:** "Kept as found" covers almost any raw natural material.
- **Fix:** replace step 6 with: "**A natural object, not made or shaped by people beyond cleaning, cutting, polishing or preserving, kept as a specimen for study, display or collection**: minerals, rocks, fossils, meteorites, shells, unset gemstones, skeletal and taxidermy specimens, pinned insects, herbarium sheets? **F6** (**A natural material sold for a use is filed by that use: firewood C1, garden stone C2, sponges and pumice H1, animal chews B11, craft feathers, fleece and shells C4, dried flowers B4, religious relics and seeds made into beads F4.**)"

### 30. Step 6 splits identical loose gems by origin
- **Type:** axis break (maker/material) · **Severity:** medium
- **Examples:** a loose lab-grown diamond or cultured pearl ("made by people", so it skips F6 and falls to C4 beads or X0) vs. a natural loose diamond (F6). A faceted sapphire is shaped by people, yet is listed as F6.
- **Fix:** add to step 6's brackets: "**Unset gemstones and loose pearls are F6 whether natural, cultured or laboratory-grown, rough or cut: origin is a modifier.**"

### 31. Step 21 ("observe, magnify or measure") swallows household measuring tools
- **Type:** key-order trap · **Severity:** high
- **Examples:**
  - Kitchen: kitchen scales, measuring jugs and spoons, meat and sugar thermometers (→ C6, not B5).
  - Body: bathroom scales, body-fat scales, baby scales.
  - Desk and sewing: ruler (C5?), sewing tape measure (C4?), postal scale.
  - Garden and pool: pool and hot-tub test kits, soil pH meter (C2?).
  - Travel: luggage scale.
  - Step 21's note protects only "building and trade measuring tools".
- **Fix:** replace step 21's lead with: "Made to **observe, magnify or measure for observation, study or science**: binoculars, telescopes, microscopes, magnifiers and loupes, weather instruments, laboratory glassware and instruments, science-education kits? **C6** (**A measuring tool made for a task the key files elsewhere goes with that task: kitchen scales and thermometers B5, rulers and postal scales C5, sewing tape measures C4, pool and soil test kits C2, building and trade measuring tools C1. Bathroom and body scales are H1.**)" Then add "**bathroom and body scales**" to step 16's examples.

### 32. Step 23's "games" captures sports
- **Type:** key-order trap / wording · **Severity:** high
- **Examples:** a football (football is "a game"), tennis racket, cricket bat, golf club, darts and dartboard (listed in E2), pool table and cue, table-tennis table (listed in E2), bowling ball, croquet set, chess clock.
- **Problem:** Step 23 runs before step 24. A careful reader files every ball game in E1.
- **Fix:** replace step 23's lead with: "Made for play, or for **a game of skill or chance played at a table, on a board or floor, or with cards, dice, tiles or tokens**: …" and add the bracket: "(**Games that are sports, including ball, racket, bat, stick, cue and target games and darts, are E2. Chess, draughts, go and other board games are E1.**)"

### 33. Steps 27 and 11 empty C7 of farm equipment
- **Type:** key-order trap · **Severity:** high
- **Examples:**
  - Crop equipment step 27 ("growing plants … powered or not") takes as C2 Garden & Grounds: combine harvester, plough, seed drill, crop sprayer, hay baler, and a tractor (which "goes by that work").
  - Livestock and timber equipment step 11 takes as B11: milking machine, cattle crush, sheep shears, poultry incubator, electric fence energiser. A forestry forwarder would go to C2 if forestry counts as growing trees.
  - Left in C7: commercial catering, retail and signage.
- **Fix:** move the farm test **before step 11**, as new step 10a: "Made for **agricultural or forestry production**: tractors and anything made to be drawn by, mounted on or driven from a tractor; self-propelled farm and forestry machines; livestock handling, milking and shearing equipment for herds and flocks; commercial crop, poultry and dairy equipment? **C7 Farm & Forestry Equipment** (Equipment for a household garden, allotment, pets, horses or a few backyard hens or hives is C2 or B11.)" For the commercial half of C7, see Finding 37.

### 34. Step 29 B7 takes desk accessories before step 30 can
- **Type:** key-order trap · **Severity:** low
- **Examples:** desk organiser, pen pot, letter tray, magazine file, document box, cable tidy. The step 29 lead says "wherever it is used (home, office …)", and B7 "store, organise" fits all of these.
- **Fix:** add to B7: "(**Desk organisers, letter trays and filing supplies are C5.**)"

### 35. Step 3's building elements make installation a category boundary
- **Type:** axis break / rule contradiction · **Severity:** high
- **Examples:**
  - A box of floor tiles (C1) vs. the same tiles laid (G2).
  - A rug (B2) vs. fitted carpet (G2).
  - A wardrobe (B1) vs. a fitted wardrobe (G2).
  - A built-in bath (G2) vs. a freestanding roll-top bath (no step takes it, so X0).
  - Blinds and shutters (B2 "dress windows" or G2 windows?).
  - Wallpaper (G2 or B4?).
  - A built-in oven (B5, by the note) inside a fitted kitchen (G2).
- **Problem:** Appendix A lists "installation (freestanding, built-in, fitted)" as a modifier. Step 3's note says "'built-in' is a modifier", yet the step itself divides on it.
- **Fix:** replace step 3's building-element clause and its examples, so the step reads: "**Land; a building or other permanent structure made to be occupied, entered or enclosed (house, flat, garage, barn, shed, garden room, carport, in-ground pool); a vehicle or vessel made to stay in one place as a dwelling; a burial plot or niche?** **G2** (**A building is filed as a whole. Its elements and products, installed or not, are filed by what they are: structural, envelope and finishing products (bricks, timber, roofing, windows, doors, stairs, flooring, tiles, wallpaper, fixed plumbing and wiring, fencing) are C1; kitchen and wardrobe cabinetry is B1; carpets, blinds and curtains are B2; sanitaryware and hot tubs are B8; installed machines, lamps, safes and alarms keep their own category.** …)"
  - Add to S3: "**Building products are never parts of a building: they go where step 3's note sends them.**"
  - Add to step 31's examples: "**doors, windows, roofing, flooring, tiles, wall coverings, fencing and other building products**".
  - Add to the B8 branch, and rename B8 **Climate, Water & Sanitary**: "**or to supply water for bathing and washing, or take away waste: baths, showers, basins, toilets and bidets, fitted or freestanding, and hot tubs**". This puts sanitaryware next to the water heaters and softeners B8 already holds.
  - A floor tile, a door or a bath is then in one category before and after it is installed, as Appendix A requires.

### 36. Step 3 vs. notes: barns, stables, garden structures
- **Type:** overlap / wording · **Severity:** low
- **Examples:** a barn (G2) vs. a stable block or cattle shed ("animal housing is B11"); a summerhouse (G2) vs. a playhouse (E1) vs. a treehouse; a prefab sauna cabin (G2) vs. a portable sauna tent; a pergola, gazebo and decking (G2 or C2?).
- **Fix:** step 3's brackets: "(… Greenhouses and polytunnels are C2. **Animal housing that is not a building a person can stand in (hutches, coops, kennels, stalls inside a building) is B11; stable blocks and barns are G2.** Play structures, including treehouses, are E1. **Pergolas, gazebos, decking and patios are G2; pop-up gazebos are B1.**)"

---

## Part 5 — Axis breaks (against S4/S5 and the axis paragraph)

### 37. C7 "not for a household" files by market and setting
- **Type:** axis break · **Severity:** high
- **Examples:**
  - Catering: a commercial espresso machine owned by a home barista (C7) vs. a domestic one (B5); a commercial glass-door fridge in a home bar; a catering griddle.
  - Retail and signage: a vintage Coca-Cola vending machine kept by a collector; a cash register or card terminal; a shop neon sign hung in a games room (C7 "commercial signage" vs. B4 "wall signs").
- **Problem:** Appendix A lists setting and user as modifiers, and step 29 says "wherever it is used". "Not for a household" is a market-grade test. Catering kit has exactly B5's inner structure (cook, cool, store, serve).
- **Fix:** after Finding 33, C7 = farm and forestry only, by function. Then:
  - B5 branch: "… **of any capacity, domestic or commercial**".
  - Step 22 D1: "**point-of-sale terminals, card readers and cash registers**".
  - B4: "**flags and signs, including illuminated and shop signs**".
  - B1: "**display stands, counters and shop fittings**".
  - B5: "**vending machines for food and drink**".
  - Retitle C7 "**Farm & Forestry Equipment**" and replace its description with "tractors and their implements, self-propelled farm and forestry machines, livestock handling and milking equipment".

### 38. E2 "outdoor recreation" files camping kit by setting
- **Type:** axis break / granularity · **Severity:** medium
- **Examples:**
  - Furniture: folding camp chair (E2) vs. folding garden chair (B1); camping hammock (E2) vs. garden hammock (B1); inflatable camping mattress (E2) vs. guest air bed (B1).
  - Cooking and cooling: camping stove (E2) vs. portable gas hob (B5); camping kettle; cool box (E2 or B5?).
  - Light: camping lantern (E2) vs. lantern (B3).
  - Bags: hiking rucksack (A4 bag at step 15, or E2?).
- **Problem:** Appendix A lists "setting (indoor, outdoor, travel …)" as a modifier. E2 would also need two unrelated inner structures: equipment by sport, and camping kit by task (shelter, sleep, cook, light, carry).
- **Fix:**
  - Step 24: replace "tents, sleeping bags, camp furniture and stoves" with "**tents, shelters, sleeping bags and sleeping mats, and climbing, caving and navigation gear**".
  - Add to step 24's brackets: "(**Portable furniture, stoves, cookware, cool boxes and lanterns are filed by what they do, B1, B5 and B3, wherever they are used: 'camping' is a setting. Rucksacks and bags of every kind are A4.**)"

### 39. C4 vs. C5 divides drawing materials by user ("artists'")
- **Type:** axis break / wording · **Severity:** medium
- **Examples:** coloured pencils, sketchbooks, felt-tip and alcohol markers, crayons, fineliners, calligraphy pens, graphite drawing pencils (2B–8B), a children's colouring set (E1? C4? C5?).
- **Problem:** "artists' paints … artists' drawing materials" (C4) vs. "everyday drawing" (C5) is a user test, and user is a modifier. A related C4/C1 split puts silversmith's pliers (C1, "shaping metal") apart from beading pliers (C4), though they are the same tool form.
- **Fix:**
  - Step 26: replace "artists' paints, brushes, canvases and easels, artists' drawing materials" with "**paints, inks, pastels, charcoal, coloured pencils, crayons and markers made for making pictures, brushes, canvases, easels and sketchbooks**".
  - Step 30: replace "writing, everyday drawing" with "**writing**".
  - Add to step 26: "(**Pencils, pens and highlighters made for writing are C5. Tools for jewellery-making and beadwork are C4, including small pliers and cutters made for that craft.**)"

### 40. C5 files office machines by connectivity
- **Type:** axis break · **Severity:** low
- **Examples:** a label maker with a USB or Bluetooth link (D1 peripheral or C5?); a standalone copier (C5) vs. a multifunction printer-copier (D1); a fax machine.
- **Problem:** Connectivity is a modifier, and the D-branch note says so.
- **Fix:** step 30: replace "office machines that do not connect to a computer (copiers, shredders, laminators, label makers)" with "**office machines whose main function is not printing from or scanning to a computer (copiers, shredders, laminators, label makers, binding machines), connected or not. Printers, scanners and multifunction printers are D1.**"

### 41. D2 is a grab-bag list, and two-way radios have no branch
- **Type:** axis break / gap · **Severity:** medium
- **Examples:** walkie-talkies, CB and amateur-radio transceivers, baby monitors (D3? B9?), pagers, satellite messengers, electronic pocket translators, landline cordless phones, intercoms.
- **Problem:** D2 is a list ("phone, tablet … tracker, power banks"), not a function. A reader cannot tell whether a two-way radio is a "phone". Baby monitors fit D3 ("receiving sound and pictures") and B9.
- **Fix:** step 22 D2: "a **phone, two-way radio, pager or other device for personal communication**; a **tablet, e-reader, electronic organiser or translator**; a **smartwatch, fitness tracker, smart ring, smart glasses, GPS unit, satellite messenger or tracker**; and power banks?" Add to B9: "**baby and child monitors**".

### 42. "Made for one sport" (step 15) is unworkable at its edges
- **Type:** wording · **Severity:** medium
- **Examples:** ski jacket (made for skiing, but "outdoor jackets stay A1"), hiking boots (hiking is a recreation, not "one sport"), climbing harness, ballet shoes and tap shoes (is dance a sport?), running shoes ("general trainers"?), golf shoes, yoga leggings, a cycling commuter helmet.
- **Fix:** replace the step 15 sport bracket with: "(**Made for a sport means made for the demands of one sport, dance or outdoor activity and not suited to everyday wear: football boots, ski boots and ski jackets with powder skirts, climbing shoes and harnesses, ballet, tap and dance shoes, swimming costumes, wetsuits, padded cycling shorts, riding helmets, kendo uniform. These are not filed here: go to step 24. Running shoes, hiking boots, general trainers, leggings, team and fan jerseys, and outdoor jackets stay A1 and A2.**)" Add "**dance**" to step 24's lead.

### 43. A1 "PPE for work", costume vs. dress-up, badges and hair ties
- **Type:** wording / axis break (user) · **Severity:** low
- **Examples:** safety glasses for home DIY (not "work"); a respirator for painting a bedroom; a hi-vis vest for cycling; a child's Elsa costume (A1 "costume", or E1 "dress-up toys"?); a staff ID badge on a lanyard (A3 "badges" or F5 "proves identity"?); hair ties and plain hair clips ("ornament"?).
- **Fix:**
  - A1: replace "personal protective equipment for work" with the hazard wording in Finding 15.
  - E1: replace "dress-up toys" with "**dress-up accessories made as toys (toy crowns, wands, play make-up); costumes are A1**".
  - A3: "pins, badges and patches **worn as ornament (identity and access badges are F5)**".
  - H1: add "**hair ties, plain clips, grips and bands**".

### 44. "Clocks & Watches" sits in the "Worn" domain; domain labels imply an axis
- **Type:** axis break (presentation) · **Severity:** low
- **Examples:** a grandfather clock and a kitchen wall clock are in domain A "Worn".
- **Problem:** Domains are declared reading aids, but their names ("Worn", "Home", "Electronics") read as tests. Readers will use them.
- **Fix:** rename domain A "**Worn & Carried**", and add to "Levels in stage 1": "**Domain names describe most of their members, not all; they are never tests.**"

---

## Part 6 — Gaps (no test, or falls to step 31/32 though not a tool)

### 45. Bathing, water leisure and heat objects
- **Type:** gap · **Severity:** medium
- **Examples:**
  - Freestanding bath, washbasin on a stand, portable camping toilet (X0).
  - Hot tub or spa: B8 by the literal "heat … water", which is surprising.
  - Above-ground swimming pool (C2 "pools"? E1?) vs. inflatable paddling pool (E1).
  - Portable sauna tent.
  - Hot-water bottle, wheat heat pack, chemical hand warmers (H1? H2? B8?).
- **Fix:** sanitaryware and hot tubs as in Finding 35 (B8). Add to C2: "**above-ground and inflatable pools for swimming**". Add to E1: "paddling pools made for play". Add to H1's lead examples: "**hot-water bottles, heat packs and hand warmers for comfort**". Portable saunas go to B8.

### 46. Pregnancy, fertility, feeding and baby care
- **Type:** gap · **Severity:** medium
- **Examples:**
  - Pregnancy and fertility: pregnancy test, ovulation kit, fertility monitor (pregnancy is not "an illness"; they fall to C6 "measure" or X0).
  - Feeding: breast pump (X0), nursing pillow (B2?).
  - Bathing and changing: baby bath, baby changing mat, potty and toddler toilet seat (H1? X0?).
  - Child safety: stair gate and cupboard locks (B9 "protect a home and its contents", not people).
  - Sleep: baby sleeping bag (A1 or B2?).
- **Fix:**
  - Step 2 lead: add "**or for pregnancy, fertility or breastfeeding (tests, monitors, breast pumps, nursing pads)**".
  - H1: add "**baby baths, changing mats, potties and toilet-training seats**".
  - B9: as amended in Finding 4 ("its people"), plus "**stair gates and child-safety locks**".
  - A1: "**wearable baby sleeping bags**".

### 47. Home energy equipment has no clear home
- **Type:** gap / wording · **Severity:** medium
- **Examples:** rooftop solar panels, solar inverter, home battery wall, wind turbine (C1 "power"? installed, so its category is unclear); EV wall charger (G1 by S3, acceptable); heat pump (B8); smart energy meter.
- **Problem:** C1's "power" was written for generators and tools. A household's energy system is a domestic-services function, like heating and water.
- **Fix:** rename B8 **Climate, Water & Energy** (and, with Finding 35, "& Sanitary"). Add to its branch: "**or to generate, store or meter electricity for the home: solar panels and inverters, home battery storage, small wind turbines, energy meters**". Portable generators stay C1.

### 48. Other gaps and step-31/32 fallers that are not tools
- **Type:** gap · **Severity:** low
- **Examples and homes to add (exact text):**
  - Cannabis and herbal smoking products: see Finding 11 (B10).
  - Matches and utility lighters: add to C1 "**matches, firelighters and utility lighters**". Pipe and cigar lighters stay B10.
  - Freestanding letterbox and parcel box: add to B9 "**letterboxes and parcel boxes**".
  - Boxed software on disc or USB, which is neither F1 ("made to be read, viewed or listened to") nor I1 (physical): add to step 22 D1 "**software on a physical carrier**".
  - Shipping container used as a store: add to step 3 "**shipping containers and portable cabins kept in place as stores or rooms**".
  - Life jacket and buoyancy aid: A1 PPE by Finding 15's hazard wording; E2 if made for one water sport.
  - Metal detector: add to E2's lead "**metal detecting**"; detectors made for finding pipes and cables are C1.
  - Travel neck pillow: add to B2 "**travel pillows**".
  - Christmas crackers, party poppers, sparklers: B4 (see Finding 4).

---

## Part 7 — Granularity (no split or merge proposed for size alone)

### 49. Merge B7 Storage & Organisation into B1 Furniture
- **Type:** granularity (merge) · **Severity:** medium
- **Examples:**
  - Storage furniture vs. containers: storage ottoman, blanket chest, travel trunk, shoe cabinet (B1) vs. shoe rack and shoe box (B7?).
  - Shelving: wall shelf (B1) vs. shelving insert (B7).
  - Others on the line: under-bed drawer on castors, wall-mounted coat rack, cube storage unit with fabric bins.
- **Reason:** B1's lead already includes "store things on or in". The B1/B7 line is drawn only by size (a piece of furniture vs. a box), and the brief forbids splitting for size. Both would need the same inner facets: what is stored, form, and fixing.
- **Fix:** merge into "**B1 Furniture & Storage** — pieces and containers made to sit, lie, work at, or display, store and organise things on or in, indoor or outdoor, including mattresses." Delete the B7 branch, and send its examples (boxes, baskets, bins, hooks, shelving inserts, tool boxes) to B1. Garment and shoe bags also go to B1, by Finding 14. (If this merge is made, read "B7" in Findings 14 and 34 as B1.)

### 50. Split C1 into tools and building/repair materials
- **Type:** granularity (split) · **Severity:** medium
- **Examples:**
  - Tools, classified by action (cut, shape, join, measure, lift): hand saw, cordless drill, socket set, ladder, multimeter, workshop lathe.
  - Materials, classified by substance and building element: timber, bricks, tiles, paint, adhesives, fasteners, hinges, cables, fuses, fuels, batteries, packing materials, plus (after Finding 35) doors, windows and roofing.
- **Reason:** Not size. The two halves need different inner structures, in the way DIY retailers and construction classification systems separate "tools" from "building products". C1 is also the step-31 catch-all, so a mixed category makes misfiles invisible.
- **Fix:** step 31 becomes two branches:
  - "a **tool, instrument or machine made to cut, shape, join, measure, test, lift, power or repair**? **C1 Tools & Workshop Equipment**"
  - "**materials, building products, hardware and supplies** for building, repair, electrical work, packing and fuelling? **C8 Building Materials & Hardware**"
  - If this split is made, read "C1" for building products in Findings 35 and 48 as C8.

### 51. B10 Cellar & Smoking joins two unrelated inner structures
- **Type:** granularity · **Severity:** low
- **Examples:** a case of Rioja and a rack of single malts vs. a briar pipe, a vape pen, a hookah and an ashtray.
- **Reason:** Drink stock would be studied by drink type, origin and vintage (mirroring the Culinary taxonomy). Smoking goods would be studied by product and implement. Nothing inside is shared except "adult indulgence", which is a motive.
- **Fix:** keep B10 for now (no better home for either), but name it as two sub-trees in its description: "**B10 Cellar & Smoking — two independent parts: (a) alcoholic drinks in sealed containers; (b) tobacco and other smoking, vaping and chewing products and their implements.**" Revisit after stage 2. If the Culinary taxonomy can take sealed alcoholic drinks as owned stock, move (a) there and retitle B10 "Smoking & Vaping".

### 52. E2 is two categories in one
- **Type:** granularity · **Severity:** medium
- **Examples:** a tennis racket, a rowing machine and a dartboard (sport and fitness, structured by sport and exercise) vs. a tent, a sleeping bag and a climbing rope (outdoor activity).
- **Fix:** with Finding 38 applied (portable furniture, stoves and lanterns leave), what remains of outdoor gear is shelter, sleep and climbing/navigation. That is small and close enough to sport to stay. **No split**; Finding 38 is the fix. Record in E2's description: "**inner structure: by sport or activity first, then by equipment type**".

### 53. C7 becomes thin but coherent
- **Type:** granularity · **Severity:** low
- **Examples:** after Findings 33 and 37: tractor, baler, milking machine, forestry forwarder.
- **Fix:** keep as **C7 Farm & Forestry Equipment**. It has its own inner structure (tillage, planting, crop care, harvest, livestock, forestry) that does not match C2's garden structure.

### 54. H3 and I1: thin or derivative, but keep
- **Type:** granularity · **Severity:** low
- **Examples:**
  - H3: vibrator, dildo, restraints.
  - I1: an e-book, an MP3 album, a game download, a font, a domain name, an NFT. Its main kinds mirror F1, D5, F2 and F5.
- **Fix:**
  - Keep H3: a distinct function, a distinct register, and no other honest home.
  - Keep I1, but add to its description: "**inner structure mirrors the physical categories for the same works (F1, F2, F5, D5) plus data-only kinds (software, fonts, domain names, tokens); study I1 together with F1 and D5.**"

---

## Part 8 — Overall shape

### 55. Is a 44-category top level with 9 navigation domains a sound basis for per-category studies?
- **Type:** overall judgement · **Severity:** high (as a gate on stage 2)
- **Judgement:** **Yes in shape, not yet in boundaries.**
  - **The count is reasonable.** Forty-three placing categories (plus X0) is in the range of working top levels for product classification, and well within what a reader can scan. The nine domains are a sensible reading aid, and having one (I) or two (G) categories in a domain is harmless because domains are not tests.
  - **The axis statement is good and should be kept:** a status filter, then designed function, with an explicit modifier list.
  - **The weakness is that the key relies on dozens of bracketed exceptions** (Finding 1). About a dozen steps file by something Appendix A calls a modifier: setting (C7, E2), user (step 2, C4), occasion (step 12), installation (step 3), connectivity (C5), maker or condition (F5), acquisition (C4 vs. E1), origin (F6), and power or technology (step 22).
  - Stage 2 studies would inherit these contested boundaries, and two teams would study the same object (figurines, camp furniture, measuring tools, sanitaryware) from different categories.
- **Merges I would make because the inner structure is the same:** B1 + B7 (Finding 49). Commercial catering (now in C7) into B5 (Finding 37). Built model kits (C4) with models (E1) (Finding 24). I would *not* merge C4 with C5, A1 with A2, or D1 with D2. Each pair has different inner structures once the boundary wording is fixed.
- **Splits I would make because the inner structure differs:** C1 into tools vs. materials (Finding 50).
- **Tests I expect to fail in practice** (two careful placers will disagree):
  - S3 "one kind vs. a class" (Finding 14).
  - Step 6 "made by nature" (Finding 29).
  - Step 12 "rite of passage" and religious vs. secular festival (Findings 22–23).
  - Step 21 "measure" (Finding 31).
  - Step 23 "games" (Finding 32).
  - Step 15 "made for one sport" (Finding 42).
  - F2/F3/E1 for figures (Finding 24).
  - E3 vs. D3 for headphones, turntables and microphones (Finding 27).
  - B3 vs. B4 for decorative lighting (Finding 5).
  - D1 "convertible computer" vs. D2 "tablet": a detachable-keyboard tablet such as a Surface Pro or an iPad with a keyboard case. Fix: "**a device whose screen and keyboard can separate is D2 if it is sold as a tablet with an optional keyboard, and D1 if the keyboard is supplied with it**".
  - C7 "not for a household" (Finding 37).
- **Before stage 2:** apply the fixes, then rerun a blind placement round, seeded with the example objects in this audit, as the regression set.

---

## Top five changes, in priority order

1. **Make the key mechanically sound.**
   - Add S1b ("notes bind") and declare branch order (Findings 1, 5).
   - Rewrite the lead questions that exclude their own examples: step 15 "worn or carried", step 22 "electronic … or any photographic equipment … or a video game", and steps 16, 23, 31, B1, B2, B9 (Findings 2–4).
   - Until this is done, suitcases, umbrellas, tripods and game discs land in the wrong category under the draft's own S1a.
2. **Rewrite S3** so that only cases, bags, covers and stands for one object at a time are parts. Furniture, racks, hooks, hangers and boxes are never parts, and nothing worn is a part (Findings 14–16). This fixes bookcases, TV stands, garment bags, hangers, motorcycle helmets and welding masks in one move.
3. **Narrow the four over-broad early steps**, with the exact wording in Findings 29, 31, 32 and 22–23:
   - step 6, to natural objects kept as specimens;
   - step 21, to observation and science;
   - step 23, to table, board, card and dice games;
   - step 12, to religious practice and the dead, with occasion a modifier.
4. **Remove installation as a boundary.** G2 holds land and whole structures. Building products go to C1/C8 whether installed or not; cabinetry to B1; carpets and blinds to B2; sanitaryware and hot tubs to B8 (Findings 35, 45, 50).
5. **Remove the market and setting splits.**
   - Move the farm test ahead of steps 11 and 27 as C7 Farm & Forestry (Finding 33).
   - Send commercial catering, POS, signage and vending to their functional homes (Finding 37).
   - Send camp furniture, stoves and lanterns to B1/B5/B3 (Finding 38).
   - Replace C4's "artists'" with a picture-making vs. writing test (Finding 39).

*Next after these five: the figures, models and collectibles cluster (Finding 24) and the B1 + B7 merge (Finding 49).*
