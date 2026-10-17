## Domain A
Worn & Carried. Memos A1 to A5, conformance pass applied. Source: framework/structure/A1..A5.md and _review_A.md. Section marks (§) are memo sections. "Review 5A/5B/5C" are the parts of _review_A.md section 5.

### Table
| code | name | sub-families | choice level | tier type | maker centrality | review verdict | kinds | daggers | OWNER marks |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Clothing | Tops; Bottoms; Dresses, one-piece garments and sets; Outerwear; Underwear, hosiery and sleepwear; Headwear and head protection; Hands, neck and waist wear; Parts | Kind = cut buyers compare: deep in outerwear, shallow in tops; named form below | mixed | high | minor fixes | 98 | 65 | 18 |
| A2 | Footwear | Sneakers; Shoes; Boots; Sandals; Slippers; Over-footwear; Parts | Generic type buyers compare (Oxford, Chelsea); deeper for boots and dress shoes | mixed | high | needs rework (levels 1 and 2 only) | 61 | 44 | 30 |
| A3 | Jewellery | Head and hair; Ear; Body and facial piercing; Neck and chest; Arm and wrist; Hand and finger; Torso, waist and clothing; Leg and foot; Parts | Form buyers name (hoop earring, tennis bracelet); metal, stone, chain pattern are attributes | mixed | high | minor fixes | 56 (+3 parts) | 39 | 24 |
| A4 | Bags & Accessories | Handbags and shoulder bags; Backpacks; Luggage; Work cases; Wallets; Non-corrective eyewear; Umbrellas and fans; Baby carriers; Small carried accessories; Parts | Silhouette or format; no leaf level (depth 3); luggage size class is an open OWNER point | preference (no tier stored) | medium | minor fixes | 69 | 55 | 18 |
| A5 | Clocks & Watches | Wristwatches; Carried watches; Clocks; Timing instruments; Parts | Wristwatch: defining complication or certified function; clocks: case or placement form | mixed | high | minor fixes | 52 | 31 | 14 |

Notes. Tier: A1, A2, A3, A5 are consensus-ranked at maker, line and named-form level plus spec-ranked attributes (denim ounces, EN ISO 20345, fineness, COSC); no tier on a kind (C4). A4 has no fetched tier source, so none is stored. Maker centrality: every memo classes makers as "identity"; A4 is rated medium because that holds for handbags, small leather goods, luggage collections and sunglasses only. Depth: A4 uses three levels below the category; the others use four. A3 and A4 fail the two-region tier test (C4(e)).

### What conformance changed
- A1: Deleted the role-based uniforms and costumes leaf; added a written coverage-and-layer tie-break, homes for protective gear (leaf 6.2), kinds renamed by form not material, and a parts sub-family (§11 F1 to F4).
- A2: Dropped the work-and-safety sub-family (now an attribute plus view); boot leaves rebuilt on shaft height only; shoe leaves cut to one axis; over-footwear and parts sub-families added (§11 F11 to F13).
- A3: Piercing jewellery became a sub-family defined by fitting (nose pin and nath share one home); tier moved off kinds to ledger entries; regional types and kihei demoted to named forms or attributes (§11 F19 to F22).
- A4: Overlapping bag kinds got form tests; sling moved to handbags, shopper and sports bag became aliases; the catch-all split into baby carriers and small accessories; the withdrawn tier left empty (§11 F26 to F28).
- A5: Wristwatch leaves rebuilt on defining complication (environment-first rule kept only as Candidate A'); style and decoration kinds became tags and attributes; border-case kinds added; watch chain moved to parts (§11 F33 to F35).

### Owner questions (merged)
Shared conventions (review 5A)
1. ★ Levels (C5): at most four below the category with the named form as one; leaf optional per sub-family; "one axis per level" read within each sub-family. [approve] A1 to A5
2. ★ Kind against named form (C2): the choice-level test decides; named forms are maker-bound or not; specs, sizes, prints, colourways are never named forms. [approve] A1 to A5
3. Traditional and regional forms: kinds only when sold as their own category, else non-maker named forms with a region tag and a "by tradition" view; never a sub-family or leaf. [approve] A1 to A4 (A3 §10.3: chandbali, haath phool)
4. Historical-only styles (poulaine, chopine, caliga, cartel and tavern clocks, trench watch): kinds or named forms when owned, or only a "historical" tag? [none given] A2 §10.9, A5 §10.10
5. Variant ledger (C3) for colourways, references, prints, collaborations, editions. [approve] A1, A2, A5
6. Tier storage (C4 a to c): never on kinds; entries per source with a disputed flag; spec ladders as attributes; platform segments as dated tags. [approve] A1, A3, A5
7. Tier vocabulary and price band: one tier scale or one per category; one USD band scheme (C4(d)) or per category. Also A5: which tier lists count, and are dealer labels tiers or platform tags? [tier per category, stored per source; band domain-wide] A1 to A5
8. Maker ledger (C1): core schema with category extensions; lines, tier entries, named forms, variants as separate tables. [approve] A1 to A5
9. Maker-ledger seed: makers named in owner-emphasis scenes, or crawl retailer brand lists (Musinsa lists 3,708)? Include retailers' own labels (Uniqlo, ZARA) as makers? [none given] A1 §10.10
10. Scene vocabulary (C8): one sourced list, core or adjacent strength, tagged at maker, kind, named form, no inheritance; unsourced tags (skate, techwear, lolita, Y2K, archive) held back. [approve] A1 to A5
11. Alias table (C9): English label plus native-script label; homonyms with two targets (coverall, wristlet, sling, chain wallet, trench watch). [approve] A1, A4, A5
12. User and department: gender, child, baby are tags with generated department views in every A category, including children's clothing in A1. [confirm] A1 §10.12, A5 §10.8
13. Parts sub-family (C5(d)) in every A category; boxes and rolls holding several items stay B1 (Chrono24 files them with watches); A3 may keep its parts sub-family empty or omit it. [approve] A1 §10.13, A3 §10.10, A5 §10.3

Framework changes (review 5B)
14. Swimwear: does the key's E2 "swimming costumes" mean competition and sport swimwear only, with bikinis, trunks and beachwear staying A1? [yes] A1 §10.5
15. Equestrian and cycling gear: all riding and cycling helmets A1, or equestrian helmets and tall riding boots E2 with cycling helmets A1 (the key's current split)? [none given; memos apply the key] A1 §10.5, A2 §10.6
16. Watch chains and fobs (W1): chains made for a pocket watch A5 under S3, fobs worn without a watch A3; add the crown sentence. [adopt] A3 §10.11, A5 §10.3
17. Head ornaments (H1) and buckles (K1): banded headwear incl. fascinators A1, pinned or clipped ornaments A3, plain clips H1; loose buckles follow the belt to A1. Stick-on bindi: A3 or H1? [adopt H1 and K1; bindi none] A3 §10.9
18. Furoshiki and carry cloths: bag (A4) or wrapping textile (B2)? [B2 with A4 cross-reference] A4 O5
19. Insulated lunch and cool bags to B5 (already in _framework_conflicts.md)? [yes] A4 O6
20. Pencil cases and toiletry bags: A4 by step 17, or C5 and H1? [A4] A4 §10
21. Powered handheld fans: A4 or B7? Beach and patio umbrellas: B1 or C2? [none given] A4 O6
22. Prescription sunglasses are H2 because they correct vision? [confirm] A4 O8
23. Prayer-bead necklaces and malas: F4 if sold as prayer beads, A3 if sold as a necklace, or always F4? [by how sold (A3 if necklace)] A3 §10.6
24. Gold-ingot pendants and coin jewellery: A3 with a bail or loop, F3 as bullion or coin without a mount (form test)? [form test (review); memo wording differs] A3 §10.7
25. Sensor-led outdoor watches (Rangeman, Mudmaster): A5 when time is the main display, D2 when sensing is? [yes] A5 §10.4
26. Performance basketball and tennis shoes: E2 only when sold as performance models with sport-specific soles, A2 for lifestyle retros? [yes] A2 §10.7
27. Shoe waterproofing sprays: B6 (care products) or C8 (not a cleaning product, used on many objects)? [memo B6; review leans C8] A2 §10.8

Per category (review 5C plus memo additions)
28. A1: adopt form-first Candidate A, seven sub-families plus parts, with the coverage-and-layer tie-break. [yes; Candidate B breaks Appendix A] A1 §10.1
29. A1: "Draped and wrapped garments" leaf; kurta in Shirts, lehenga choli in Dresses, hakama in Trousers; kimono types as named forms, or as kinds (Google lists them as nodes)? [named forms] A1 §10.2
30. A1: protective gear filed by body zone and form with hazard_rating, no protective sub-family; keep leaf 6.2 (head, eye, ear, face protection) or fold into hats by zone? [yes; leaf none given] A1 §10.3
31. A1: delete the uniforms and costumes leaf; file by form with a uniform tag; one kind "costume". [yes] A1 §10.4
32. A1: gaiters, leg warmers, obi, dupatta stay in A1; arm sleeves are not placed and need a ruling. [yes] A1 §10.6
33. ★ A2: level 1 as form families (sneakers, shoes, boots, sandals, slippers, over-footwear), safety footwear as attribute `protection_class` plus view, not a sub-family. [yes] A2 §10.1
34. A2: dress-shoe kinds by lacing and cut (oxford, derby, monk, loafer) with broguing an attribute, or toe-cap patterns as kinds (ABC-MART)? [lacing and cut] A2 §10.2
35. A2: mules and clogs as kinds under Shoes, or with sandals? [under Shoes] A2 §10.3
36. A2: minimalist and barefoot shoes as a kind in Sneakers, or an attribute? [kind] A2 §10.4
37. A2: Ugg-type sheepskin-lined pull-on boot in Boots, or slipper boot in Slippers? [Boots] A2 §10.5
38. ★ A3: two-step top (site, then form family) or flat form leaves (Candidate B)? [two-step] A3 §10.1
39. A3: piercing rule by fitting, not sales channel (second exception to C5(d)); decide the edge of a ring or stud sold "for the ear". [yes] A3 §10.2
40. A3: wedding and engagement rings as occasion tags on band and solitaire rings, or as kinds? [tags] A3 §10.4
41. A3: jewellery sets filed under the principal piece with contents recorded, or a kind "jewellery set"? [principal piece] A3 §10.5
42. A4: hardside and softside as an attribute or as kinds (Samsonite, Tumi split them)? [attribute] A4 O1
43. A4: luggage size class (cabin, check-in) as kinds (memo, a stated exception to C6) or an attribute with a "carry-on" view? [attribute (review)] A4 O2
44. A4: eyewear frame shape as a kind, shared by name with H2 frames, which are filed by whether they correct vision. [yes] A4 O3
45. A4: a named form that sources place under two kinds (Birkin, Kelly, Speedy) goes under the kind the maker uses, read from a fetched maker page. [yes] A4 O4
46. A4: one home for the wristlet (card slots and no compartment: wallet; else bag) and for the two chain wallets as drawn. [yes] A4 O7
47. A4: rare silhouettes (Modalina's 104) are named forms unless a source compares them as kinds. [yes] A4 O10
48. A4: split baby carriers from small carried accessories (applied); A4.1 holds 14 kinds with leaf null against the "about 12" limit. [yes] A4 O9
49. A5: movement and power are attributes only, no horology exception. [yes] A5 §10.1
50. ★ A5: wristwatch level 2 by defining complication or function, with pilot, field, racing, sailing, dress as tags (Candidate A), or environment-first A' with tests; confirm order across functions and "display is the form" rule. [Candidate A] A5 §10.2
51. A5: fashion watches and tie-in editions as maker-class and variant tags, not kinds. [yes] A5 §10.7
52. A5: skeleton clock stays a kind (a dealer counts 44) while the skeleton watch is an attribute, or both attributes? [none given] A5 §10.11
53. A5: Swiss Made as an attribute or an entry in the C17 jurisdiction ledger? [attribute] A5 §10.12

### Shared-rule questions raised in this domain
- All five memos are written to the draft conventions C1 to C9 (maker ledger, kind against named form, variant ledger, tier and price band, levels and axes, size and user, order, scene vocabulary, alias table); none is owner-approved yet.
- C5(c) and C5(d): the leaf axis is stated per sub-family, and the parts sub-family is the one exempt from the level-1 axis. A3 adds a second exception (fitting-defined piercing sub-family).
- C4(d) and C4(e): the domain-wide USD price band, and the two-region rule for tier sources (A3 and A4 fail it today; A5's three tier lists are all English dealer blogs).
- C6 exception: luggage size class (A4) is the one proposed departure from "size is an attribute".
- C10 (rule T: power source and technology), C11 (rule R: regional names), C12 (rule M: mounting, for clock kinds) and C13 (compatibility ledger: Pandora Moments, watch movement supply) are applied in A2 to A5.
- C14 (multi-use kinds: the charm), C15 (toy or real: toy crown), C16 (no individual-item facts), C17 (jurisdiction ledger: hallmarking, Swiss Made) are applied or raised in A3 and A5.
- Framework conflicts touching A: lunch bags (A4 against B5), worn optical instruments (loupes against the A4 branch), and sport helmets, goggles and swimwear (A1 protective list against the E2 "made for a sport" note).
- Precedence sentences proposed for the key: W1 (watch chains), H1 (head ornaments), K1 (loose buckles), and the crown sentence; plus decided-by-key records for shoe horns, waders, game and attendance clocks, tower and atomic clocks, pulse watches, bag charms, clip-on lenses, loose belt buckles.
- Appendix A and S3 are relied on throughout: user, occasion, region, scene, tier are modifiers and never levels; parts follow the whole object.
END A
