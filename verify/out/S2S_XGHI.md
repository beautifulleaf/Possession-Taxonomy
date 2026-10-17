# S2S_XGHI: stage-2 summary digest, domains G, H, I

## Domain G
### Table
| code | name | sub-families | choice level | tier type | maker centrality | review verdict | kinds | daggers | OWNER marks |
|---|---|---|---|---|---|---|---|---|---|
| G1 | Vehicles | Land vehicles, Rail vehicles, Watercraft, Aircraft, Parts and accessories made for one vehicle | Body style, discipline or class within a vehicle class; model line is the named form | preference (price band; legal classes to C17, standards as attributes) | high | minor fixes | about 150 (71 in the worked tree) | 52 | 48 |
| G2 | Property & Structures | Land, Dwellings, Other buildings & structures, Burial places | Where sources' search filters and census categories stop; unique objects sold by place | preference (spec facets such as alc_grade, standard_met) | low | needs rework (Land sub-family; house and flat kinds) | 53 | 27 | 37 |

### What conformance changed
- G1: Cut the tree to one named-form level (body sub-styles became `body_substyle`), made motorhome layouts kinds, and moved legal classes (kei, UNECE, EPAC) to the C17 ledger.
- G1: Split animal-drawn from hand-pushed carriers, merged vans, trucks and buses into one leaf by body, and added a parts skeleton with a C13 ledger (all dagger-marked).
- G2: Rebuilt Land by land cover and principal use, merging smallholding with lifestyle block and hobby farm; buildings became the facet `improvements`.
- G2: Cut house kinds to detached, semi-detached and terraced (bungalow, riad, castle to `house_form`) and flats to flat and maisonette; dwellings kept in place re-cut by physical form.
- G2: Withdrew use tests (S5) and the market sub-family option; houseboat and non-residential buildings are left to the owner (O1, O2).

### Owner questions (merged)
1. ★ [G1] Mode as first inner axis: sub-families Land, Rail, Watercraft, Aircraft, Parts; Rail skips the leaf level. [yes]
2. [G1] Motorsailer: a kind in sailing craft, with `propulsion` = wind + combustion engine and a primary flag. [yes]
3. ★ [G1] Legal classes (kei, UNECE and EU L/M/N/O, EPAC, FAA) go to C17; design standards are attributes; trucks and buses stay kinds despite "market". [yes]
4. [G1] Speed pedelec and throttle e-bike: a bicycle by form with legal class in C17, or a moped over the local limit. [bicycle by form]
5. [G1] Body sub-styles (roadster, targa, crossover, coupé SUV): `body_substyle` attribute, kinds, or non-maker named forms. [attribute with generated view]
6. [G1] Low-profile, overcab and A-class motorhomes, campervan, fifth-wheel and truck camper as separate kinds in one caravans leaf; UK/US alias. [yes]
7. [G1] Mountain-bike disciplines as kinds; road and gravel gradients as a `geometry` attribute or non-maker named forms. [MTB kinds; attribute]
8. [G1] Inflatable against rigid (kayaks, boats): two kinds now, or a kind only where two regions' retailers split. [attribute until second-region source]
9. [G1] Vans, pickups, trucks and buses: one leaf by body with mass and seats as attributes, or two leaves split at 3.5 t. [one leaf]
10. [G1] Prams, strollers and pet strollers in a "hand-pushed carriers" leaf apart from animal-drawn vehicles. [yes]
11. ★ [G1, E2] Racing and off-road sport machines (racing cars, karts, motocross bikes, dune buggies) are G1, filed by body. [yes]
12. [G1, E2] Edge small vehicles: children's pedal bicycles G1 (balance bikes, tricycles E1); unicycles, hoverboards, eFoils, e-scooters outside L classes open. [bikes yes; rest open]
13. [G1, E2] A horse-drawn or machine-drawn sleigh is G1; a play or sport sledge is E2. [yes]
14. [G1] Parts sub-family: skeleton by vehicle system with C13 compatibility ledger, and roof boxes and bike racks as parts. [yes]
15. [G1; D4 and C7 memos] Vehicle-mounted electronics (car audio, dashcam, mounted sat-nav, bike computer) are G1 parts; Unimog-type carriers are G1. [yes]
16. [G1] Named forms at model-line depth, with generation, trim, model year and engine as variants. [yes]
17. ★ [G1, G2] Houseboats: every houseboat G2 (G2 memo O1), or a navigating hull (narrowboat, cruising houseboat) G1 and a moored dwelling G2; narrowboat G1? [navigating G1]
18. [G2] Tiny house on wheels: always G2 as step 4 names it, or G2/G1 by use. [always G2]
19. ★ [G2] Non-residential buildings: in G2 by function as a leaf of Other buildings, or out of scope. [no recommendation; by function if admitted]
20. [G2] Choice-level rule for unique objects sold by place: kind stops where filters and census categories stop; a legal class never alone makes a kind. [yes]
21. [G2] Land by principal use with `improvements` facet; merge smallholding, lifestyle block, hobby farm; keep or merge smallholding and mixed farm (O14). [yes; keep both]
22. [G2] Bungalow, courtyard house, cave dwelling, castle, barndominium as `house_form` values with named forms, not kinds. [yes]
23. [G2] Flat and maisonette the only flat kinds; penthouse, loft, studio named forms. [yes]
24. [G2] Dwellings kept in place by physical form; licences in C17; factory-built home on permanent foundation filed as a house. [yes]
25. [G2] Annexe or ADU meeting the dwelling test (own sink, toilet, entrance) is a detached house, otherwise a garden room. [yes]
26. [G2, B7] Sauna cabin a person can enter that stands as a building is G2; portable sauna is B7. [yes]
27. [G2, E2] Tents, yurts and tipis: always E2, or G2 on a permanent platform as a dwelling. [no recommendation]
28. [G2] In-ground pools: one kind with `construction` attribute, or three kinds (fibreglass, vinyl-liner, gunite; US sources only). [one kind unless non-US source]
29. [G2] "However it is held" covers German Reihengräber and Japanese perpetual-care graves; a share granting only use of a slip or pitch is OUT. [yes]
30. [G1, G2] Extend domain-wide C4(d) price bands above 15,000 USD to over 5,000,000 USD. [yes]
31. [G1, G2] Add maker classes builder, converter, kit supplier and `base_named_form_id` to C1, with one domain-wide maker ledger; G2 lines table only if wanted (O18). [yes; no G2 lines]
32. [G1, G2] Amend C7: non-maker named forms first, by year then alphabetically; adopt the domain-G `propulsion` list and the four new C3 variant types. [yes]

### Shared-rule questions raised in this domain
- C4(d) amendment (price bands above 15,000 USD): both memos depend on it; houses, plots and graves carry no list price (C16).
- C1 amendment (maker classes, `base_named_form_id`, one domain-wide maker ledger) and C3 amendment (variant types generation, trim, model_year, engine).
- C7 amendment (named-form order) and the domain-G `propulsion` attribute (proposed additions from the domain G review).
- C17 clarification: design standards as `standard_met` against jurisdiction classes in the ledger; used for kei, UNECE, EN 15194, BS 3632, HUD code.
- C5(a)/(b)/(c)/(d): one named-form level; Rail and Burial places skip the leaf; per-sub-family leaf axes; G2 has no Parts sub-family.
- C10(b) / Rule T for watercraft propulsion leaves and airplane engine classes; C2 non-maker named forms (one-design classes, mamachari, riad); C13 open ledger for parts fit; C15 toy-or-real for children's bicycles.
- _framework_conflicts.md entries from the domain G review: houseboats, narrowboats and tiny houses on wheels (X-1); park model RV (X-2); vehicle-mounted electronics (X-10a); carriers that power implements (X-10b); commercial buildings scope.
END G

## Domain H
### Table
| code | name | sub-families | choice level | tier type | maker centrality | review verdict | kinds | daggers | OWNER marks |
|---|---|---|---|---|---|---|---|---|---|
| H1 | Personal Care & Beauty | Skin care, Makeup, Hair care and styling, Fragrance, Shaving and hair removal, Body bath and hygiene, Oral care, Grooming implements mirrors and scales, Comfort warmth and massage | Retail product type that retailers filter and review sites rank; fragrance by strength class (OWNER) | preference (price band; SPF and PA as attributes) | high | minor fixes | 82 (31 marked dagger) | 56 | 27 |
| H2 | Health, Medical & Mobility | Monitoring and testing, Therapy devices, Mobility and transfer, Daily-living and care, Sensory and communication, Medicines, Supplements, Sports meal and medical nutrition, Contraception barriers and breastfeeding, First aid and wound care, Supports braces and prostheses, Parts | Devices by physical or functional type; medicines by OTC use class; supplements by ingredient | mixed (spec attributes, legal classes in C17, sparse maker-line rankings) | medium | needs rework (Vision, Medicines, testing sub-families only) | 124 (87 attested) | 76 | 37 |
| H3 | Adult Objects | Vibrators and suction stimulators, Dildos and non-powered insertables, Anal toys, Penis toys, Restraint impact and sensation gear, Sex machines, Dolls and body replicas, Parts | The type buyers compare within an action family; masturbators by form factor | preference (consensus material class; maker value tiers held back) | high | minor fixes | 53 (52 attested) | 40 | 29 |

### What conformance changed
- H1: Deleted the user-based "Baby hygiene" leaf for a function leaf; merged hair-tool leaves and face/body care; dropped the `segment` maker column. Fragrance strength left to the owner.
- H2: Level 1 recast as two ordered tests (substance, then function); all tests in H2.1; spectacles added to Vision; legal classes moved to C17; brand products to lines table.
- H3: Level 1 recast as one ordered placement test with a motor rule; sex machines redefined; "strap-on dildo" kind dropped; collars and cuffs with fixing points placed in H3.

### Owner questions (merged)
1. [H1] Everyday used-up toiletries (toothpaste, shampoo, soap) in scope, as step 18 says, although BRIEF names consumables "kept or collected". [yes]
2. ★ [H2] Prescription-only medicines in scope: none, only classes kept at home (insulin, inhalers, antibiotics, pills), or all. [only home-kept classes]
3. [H1, H2, H3] Named-form admission: only attested, iconic, rated or ledgered named forms with a cap per category; supplement kinds from the NIH list plus volume sellers. [cap; yes]
4. ★ [H1] Fragrance kind: strength class as kind (memo), one format kind with strength as C3 `concentration` variant (review), or one kind with plain attribute; store each source's percent range. [format kind with variant; store ranges]
5. [H1, B4] One fragrance family list shared with B4: Edwards wheel, SFP seven groups, or Perfume Society eight. [Edwards wheel]
6. [H1] Sun care as a leaf of Skin care covering every area, or its own sub-family. [leaf in Skin care]
7. [H1] Tools by area (a tools leaf per area sub-family, multi-area tools in sub-family 8), or one tools sub-family. [by area]
8. ★ [H1, H2, H3] Parts: a final "Parts and accessories made for one object" sub-family in all three categories (extends C5(d) to domain H), or parts beside the device. [sub-family]
9. ★ [H2] Medicines depth: kind at OTC use class, active ingredient an attribute with ATC code, only brand products as named forms; or ingredient as named form (memo). [attribute plus ATC]
10. [H2] Level 1 as two ordered tests (substances by what they are, then devices by function), with every test and monitor, pregnancy and fertility included, in H2.1. [yes; applied]
11. [H1, H2] Adopt the shared H1/H2 sentence (labelled purpose decides; cosmetic purposes H1; legal status to C17). [yes]
12. [H1, H2, H3] Massagers: ordered test (maker names sexual use or specialist retailer lists it: H3; treatment: H2; comfort: H1). [yes]
13. [H1, H2, H3] Lubricants, massage oil, anal douches, intimate washes H1; condoms and dental dams H2; toy cleaners B6. [H1; H2; B6]
14. [H2, H3] Medical-purpose sexual-health items (ED rings and pumps, pelvic-floor trainers, vaginal dilators): H2 when the maker states a medical purpose, otherwise H3. [yes]
15. [H1, H2, H3] Wigs, breast forms and packers: all H1, all H2, or wigs H1 and the rest H2. [wigs H1, rest H2]
16. [H3, A1, A3] Harnesses, hoods, corsets, fetish clothing A1; collars, cuffs, armbinders with fixing points H3; ornamental collars A3; leash kind open. [confirm]
17. [H3, B2] Sex furniture made to restrain or suspend is H3; positioning cushions B2. [yes]
18. [H1, H2, H3] Adopt the shared set and kit rule (X11): one kind, else item of greatest value, standard kits as kinds. [yes]
19. [H1, H2] Items the key does not name: nappies, menstrual products, baby wipes, cotton pads H1; incontinence products H2. [confirm]
20. [H1] "Baby" is a user tag only; "Baby hygiene" leaf replaced by function leaf "Toileting and nappy changing". [yes; applied]
21. [H2, B1] Care beds, pressure-relief mattresses, lift recliners: H2 when made for care, or B1. [H2 when made for care]
22. [H2, B6] Contact-lens solution: H2 under S3, or B6. [H2]
23. [H1, H2, A3] Coloured non-corrective contact lenses: H2 with `corrective: no` (needs key note), H1 cosmetic, or A3. [H2]
24. [H2, A4] Add prescription spectacles, reading glasses, prescription sunglasses to H2.5 Vision, frames and lenses as parts, plano fashion frames A4. [yes; applied]
25. [H2, A2] Therapeutic and diabetic footwear: A2 or H2. [A2]
26. [H2, B8] Personal alarms, fall detectors, wandering detectors: H2.4 or B8. [no recommendation]
27. [H2, A1] Medical and surgical face masks: A1 as PPE or H2. [A1]
28. [H2] Medical-condition infant formula as its own kind in H2.8 or H2.7. [no recommendation]
29. [H2, G1] First-aid kits made for a vehicle are H2 whatever they are made for (needs key note against S3). [yes]
30. [H1, H2, H3] Legal classes (supply class, device class, cosmetic or drug status, scooter class) in the C17 ledger, voluntary standards as attributes. [yes]
31. [H2, H3] Tier entries from maker schemes (hearing-aid levels) and reviewer grades enter only with a second source from another region; record `iso_3533_declared` per named form. [yes; optional]
32. [H1, H2, H3] One domain-H user list (women, men, unisex, couples, baby, child, bariatric, adapted; "gay men" open) with generated department views. [yes]
33. [H1, H2, H3] Fetch the missing sources (appliance and baby-care retailers, optician and second-region pharmacy trees, restraint, machine and doll catalogues) before approval, or after. [before]
34. [H3] Unfetched edge items (dilators, electro-stimulation kits, urethral sounds, inflatable furniture, leashes) and proposals: C9 relation `genericised name`, `licensor_id` on lines. [decide at approval]

### Shared-rule questions raised in this domain
- C5(d) extension: a Parts sub-family in every domain H category (H2.12 already conforms).
- C17 extension: every legal class in the ledger; voluntary standards (SPF, PA, first-aid kit class, ISO 3533) as attributes.
- C1 amendment from the domain H review: maker classes pharmaceutical company, medical-device manufacturer, supplement brand.
- Named-form test and retail-facet test (C10(b) generalised); C2(b) for measuring modes, load classes and sub-styles.
- User vocabulary (C6 detail), app ecosystems as C13 rows (C13 detail), and maker tier ladders (C4 detail with C4(e)).
- _framework_conflicts.md, domain H review entries: sets and kits (X11); H1/H2 line (X3); massagers (X4); intimate, menstrual and body-replacement goods (X5).
- H2 conformance entries: car first-aid kit against S3; coloured plano contact lenses and step 2.
- Domain G C7 amendment (non-maker named forms first) is adopted in H2; C3 amendment for fragrance `concentration` variant if the owner chooses option (b).
END H
