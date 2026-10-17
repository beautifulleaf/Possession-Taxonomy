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
