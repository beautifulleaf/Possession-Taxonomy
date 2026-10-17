# AU1 — Cold audit of CATEGORIES_R1.md (top level only)

Source audited: `audit/CATEGORIES_R1.md` (Top-Level Categories v0). No other repository file was opened. Offline; no web, no git.

Conventions: "Step n" = placement key step n. "→ X" = where the key as written sends the object. Severity reflects how many common objects are misfiled and how hard the fix becomes once stage 2 builds on the top level.

---

## Findings

### 1. Step 2 "protect" captures most protective gear, armour, sport helmets and safety objects
- **Type:** Key-order trap / Overlap / Wording
- **Severity:** High
- **Examples:** cycling helmet, motorcycle helmet, riding hat (E2 claims "protective gear made for one sport"; step 2 runs first → H2); bulletproof vest, stab vest, medieval armour (step 8 claims "armour of any use"; step 2 first → H2); hi-vis vest, hard hat, safety boots, welding mask (A1 claims "protective clothing"; → H2); sunglasses (A4 says "sunglasses stay here"; they protect the eyes → H2); life jacket (E2 water sports → H2); child car seat (S3 example sends it to Vehicles; step 2 precedes step 6 → H2); condoms (H3 → H2); sunscreen, insect repellent (H1 → H2); smoke alarm, fire extinguisher, air purifier, mosquito net (B6/B4 → H2 on a literal reading).
- **Also "monitor":** fitness tracker, smartwatch with heart-rate or ECG, smart ring, bathroom scale. D2 lists fitness trackers and smartwatches, but step 2 runs before steps 11/15 → H2.
- **Problem:** Step 2 is the first function step, and "protect … the body's health or function" covers nearly everything worn for safety. Seven category texts are contradicted by it.
- **Fix (replace step 2):** "2. Made to **diagnose, treat, monitor or compensate for an illness, injury or disability**, or for first aid: medical devices and monitors, medicines and medical supplies, mobility and assistive aids (including ones installed in a home, such as a stairlift), hearing aids, spectacles and contact lenses that correct vision, first-aid kits? **H2 Health, Medical & Mobility**. (Protective gear goes by what it is: gear made for one sport → E2; armour → E4; other protective garments → A1, footwear → A2, eyewear → A4. A device that counts steps or heart rate for fitness is not a medical monitor: step 15.)"

### 2. Step 15 sends music electronics to D3, and has no exit when no branch fits
- **Type:** Overlap / Key-order trap / Wording
- **Severity:** High
- **Examples:** guitar amplifier, effects pedal, mixing desk, studio monitor speakers, microphone, audio interface, DJ controller (step 15, branch "audio equipment … speakers" → D3, although E3 lists "amplifiers, effects, DJ and studio equipment" and E3's own precedence keeps only "hi-fi for listening" in D3); digital piano, synthesiser, drum machine, electronic drum kit (powered electronic devices; no branch fits).
- **No-exit cases:** power bank, electric torch, heated jacket and light-up trainers (step 11 sends any powered worn or carried device to 15), vape (also sent from step 11), electronic calculator (C5 lists it), label maker, shredder, GPS unit, robot toy, RC car, pinball machine. The step's question is answered *yes*, so S1 ("stop at the first yes") stops the key with no category.
- **Problem:** Step 15 runs before step 16, and its trigger ("a powered electronic device") is broader than its branches.
- **Fix:** (a) Move the current step 16 (music) so it runs **before** the current step 15. (b) Replace the step 15 lead line with: "15. A **powered electronic device whose main function is computing, communication, picture-taking, gaming, or playing or receiving sound and pictures**:" (c) Add as the last line of step 15: "(A powered device that fits none of these branches is not filed here: continue to step 16.)" (d) Add a general rule after S1: "**S1a Branches.** When a step's lead question is *yes* but none of its branches fits, the answer is *no*: continue to the next step."

### 3. Step 15 branch order: tablets and phones are "computers"; earbuds are "wearables"
- **Type:** Wording / Overlap
- **Severity:** Medium
- **Examples:** iPad, Android tablet, 2-in-1 convertible laptop, smartphone (all general-purpose computers → branch 1, D1, before branch 2, D2 is tested); wireless earbuds and over-ear Bluetooth headphones (worn → "wearable", branch 2, D2, although D3 lists "headphones and earbuds").
- **Fix:** Branch 1: "a **desktop, laptop or convertible computer**, its components, peripherals, storage or networking? **D1**". Branch 2: "a **phone, tablet, e-reader, smartwatch, fitness tracker or smart glasses**? **D2**". Branch 3: add "headphones and earbuds of every kind (they are D3, not wearables)".

### 4. Step 11 "or other personal accessory carried" swallows portable objects
- **Type:** Key-order trap / Wording
- **Severity:** High
- **Examples:** pocket knife, multi-tool (E4 precedence sends utility knives to C1 → A4); lighter, cigarette case (B7 → A4); water bottle, vacuum flask, lunchbox (B3 → A4); pen, pocket notebook (C5 → A4); hiking backpack, camping water bladder (E2 → A4 as "bag"); hand-held torch (no-exit case of finding 2, or A4); walking stick (A4 lists it, but step 2 "mobility aids" takes it first → H2).
- **Problem:** Almost anything small is "carried". The intended category is personal accessories by type, not portable things.
- **Fix (replace the last branch of step 11):** "- a **bag, luggage, wallet or purse, umbrella, sunglasses or non-corrective eyewear, hand fan, keyring, or fashion cane**? **A4 Bags & Accessories** (an object that is only portable, such as a pocket knife, lighter, pen or water bottle, is filed by what it does)." In A4, replace "walking sticks" with "fashion canes (walking aids made for support are H2)".

### 5. Step 11 "ornament worn on the body or hair" captures cosmetics, and the jump to step 15 captures heated garments
- **Type:** Key-order trap / Overlap
- **Severity:** Medium
- **Examples:** false eyelashes, press-on nails, hair extensions, body glitter, temporary tattoos (H1 cosmetics; step 11 runs before step 12 → A3); wig (headwear A1, ornament A3, or H1?); heated jacket, heated gloves, LED costume (A1 says "heated or lit garments stay here", but step 11's first line sends every powered worn device to step 15).
- **Fix:** Step 11 first line: "A **powered electronic device** worn or carried whose main function is computing, communication, sensing or media (smartphone, smartwatch, fitness tracker, earbuds, e-reader)? Go to step 15. (A garment, shoe or accessory with heating or lights is not such a device: continue below.)" Third branch: "an **ornament** worn on the body, hair or clothing (rings, necklaces, body jewellery, brooches, hair ornaments, cufflinks), or a watch? **A3**". Add to step 12: "including cosmetics applied to or attached to the body (false eyelashes, artificial nails, hair extensions, wigs and hairpieces)".

