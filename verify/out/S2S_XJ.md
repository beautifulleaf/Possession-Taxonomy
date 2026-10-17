## Domain J
Groceries & Cellar, seven memos (J1 to J7). Review: `_review_J.md`. Section numbers cited as "memo §n" are those of each memo; "R7-n" is the number in the review's section 7. Statuses of JC1 to JC7 (proposed domain-J conventions) are all "owner approval pending".

### Table
| code | name | sub-families | choice level | tier type | maker centrality | review verdict | kinds | daggers | OWNER marks |
|---|---|---|---|---|---|---|---|---|---|
| J1 | Meat & Poultry | Fresh & frozen meat; Cured, smoked & dried; Sausages; Cooked, tinned & potted meats (leaf = animal in the first only) | Named retail cut for beef and pork; one kind per species for other meat; cured piece; sausage type | mixed (carcass standards, rule classes, preference) | medium (origin and scheme led) | minor fixes | 76 (58 attested, 18 pending) | 64 | 47 |
| J2 | Fish & Seafood | Fresh, frozen & live; Smoked; Salted, cured, dried & fermented; Tinned, jarred & marinated; Roe & caviar | Species for finfish; animal type for shellfish; fish-and-process for smoked and tinned; source species for roe | preference | low (one identity pocket: caviar, smoking) | minor fixes | 62 | 25 | 33 |
| J3 | Dairy, Eggs & Alternatives | Milk; Cream & butter; Yoghurt & fermented milks; Cheese (9 leaves); Eggs; Milk powders & infant formula; Plant-based alternatives (5 leaves) | Variety for cheese; product type, species or stage elsewhere; plant base for plant drinks | preference (statutory grades as attributes) | medium (identity for cheese, butter, egg lines) | minor fixes | 61 | 27 | 54 |
| J4 | Fruit & Vegetables | Fruit; Vegetables; Herbs; Edible fungi; Sea vegetables (crop-group leaves in the first two, each ending in Mixed) | Species or commodity; cultivar is a non-maker named form | ladder (published grade standards, as attributes) | low | minor fixes | 60 | 22 | 39 |
| J5 | Pantry Staples | 12: rice/grains/flours; pasta/noodles; pulses; nuts/seeds; oils/fats/vinegars; spices/salt; sugars/honey; spreads/dips; sauces/stocks; preserved produce; baking; tofu/analogues | Variety or type in crop families; product type in condiments; JAS type for soy sauce | mixed (legal ladders, two consensus rankings, preference) | low (identity in a few leaves) | needs rework (sub-family level and rice kinds) | 115 numbered (about 550 to 650 est.) | 63 | 62 |
| J6 | Coffee, Tea & Cocoa | Coffee; Tea (ISO leaves); Cocoa; Herbal & other infusions (plant-part leaves) | Coffee product or machine system; tea type by process; cocoa product; herb identity | mixed (lot-level scores as attributes, preference at kind) | low (platform case: capsules) | minor fixes | 40 | 32 | 37 |
| J7 | Wine, Beer & Spirits | Wine; Beer; Cider, perry & mead; Sake & rice wines; Spirits; Liqueurs; Mixed drinks | Grape or blend type; BJCP style; sake composition; legal or production type of spirit | mixed (spec ladders, fine-wine consensus, preference) | high | minor fixes (one high finding) | 59 (17 regional-name kinds) | 46 | 31 |

### What conformance changed
- J1: Plain-cooked and tinned meat got a home (J1-D renamed); rillettes moved to J5 by the key; kind rule set to cut or "species, whole or jointed"; ledgers replaced by `standard` and `designation` tables (§11).
- J2: Caviar grades became attributes or producer tier entries; Matjes and wet cures got J2.3 (renamed); mixed-seafood leaf removed; snails placed in molluscs; formed fish left to owner (§11).
- J3: Rule P rewritten as an objective test (protected names bound to one kind become named forms); cheese first-yes key written; plant cream and egg leaves added; ordering made reproducible (§11).
- J4: "Mixed packs" sub-family removed (final Mixed kinds instead); Cripps Pink made non-maker-bound with Pink Lady as a trade-mark alias; fruit-or-vegetable rule set by sweetness; PLU moved to `external_codes` (§11).
- J5: Level-1 axis stated as "what it is made from"; J5.10 became Preserved fruit & vegetables on a process leaf axis; rice kinds redefined by grain type with milling as attribute; designations split from standards (§11).
- J6: Culinary link plan written; drip bags and tea bags made `pack_form`, capsules one machine-system kind; green-tea kinds redrawn by process; lot scores dropped under C16 (§11).
- J7: Country-only whisky kinds removed; sake designations became an attribute (kinds: junmai against added alcohol); sweet-wine leaf and first-yes wine key added; `bottler_role` dropped for `built_by_maker_id` (§11).

### Owner questions (merged)
Shared conventions
1. ★ Designated names (Champagne, Port, Cognac, Parmigiano Reggiano, Parma ham, Stilton, Feta). (a) JC1(c) with no exception, (b) exception for wine and spirit names, (c) J3 Rule P for cheese. [(b) for wine and spirits, (a) elsewhere] J1, J3, J5, J7.
2. Adopt JC1: one `standard` table and one `designation` table in place of five memo ledgers; consortia held as `authority`. [Yes] J1 to J7.
3. Legal or measured ladders (olive-oil categories, Ibérico sale names, caviar grades, sake polishing classes) are attributes; only names fixing a different composition are kinds. [Yes] J1, J2, J5, J7.
4. ★ Cuts. (a) cut is the kind for meat and pasta, (b) cut for meat, shape family for pasta, (c) cuts are named forms everywhere (literal BRIEF wording). [(b)] J1, J5, J2 (tuna cuts).
5. One `unit_price_band` (USD per kg or litre) for J1 to J6; J7 keeps the item band per bottle too. [Yes] J1 to J7.
6. One `supply_role` column (JC3); consortia are designation authorities, not makers. J5 adds "vinegar maker" and "soy brewery". [Yes] J1 to J7.
7. Minced, shaped or formed one-ingredient products (sausage, raw burger, kamaboko, fish sausage, plant burger) stay groceries in the source category; coated, filled or sauced ones are prepared. [Yes] J1, J2, J5.
8. Spreads, pastes and dips of any origin (rillettes, jar pâté, potted shrimp, taramasalata, hummus, pesto) are J5; sliceable pâté and terrine stay J1-D or J2. Pesto: J5.8 or J5.9? [Yes; pesto J5.9] J1, J2, J5.
9. Mixed products: half by weight decides, else a final "mixed" kind; no sub-family by pack composition. [Yes] J2, J4, J5, J7.
10. One J `tradition` vocabulary with a source per value, no `cuisine` tag, Culinary links that may start from designation and variety rows. J5 would keep `cuisine`. [Yes, no cuisine tag] J1 to J7.
11. One shared variety table (breeds, cultivars, rice, coffee varietals, tea cultivars, grapes). [Yes] J1, J4, J5, J6, J7.
12. New C9 relation value `trade mark` (Pink Lady as an alias of Cripps Pink). [Yes] J4.
13. Allow `variant_type` vintage and bottler edition in C3, and a tier entry on a variant, so critic scores attach to a vintage. [Yes for C3; tier on variant needs thought] J7.
Framework changes
14. Extend the J1 branch to "meat, poultry, game and other land animals eaten (frogs, insects)", snails as J2 molluscs. Without it, insects run to X0. [Yes] J1, J2.
15. Reword the J6 test to "other plant parts brewed as infusions (leaves, flowers, fruit, roots, bark, roasted grains)" and add kava to the J6 line. This settles chicory and barley in J6.4. [Yes] J6, J5.
16. Reword step 1 as "alcohol-free versions of beer, wine and spirits". [Yes] J6, J7.
17. Cocoa butter and cocoa paste: J6 cocoa products or J5 fats and baking chocolate? Couverture and baking chocolate stay J5? [Cocoa butter and paste J6; chocolate J5] J5, J6.
18. A dry drink mix (3-in-1, milk tea, drinking chocolate) is J6 when coffee, tea or cocoa leads by weight, otherwise prepared. J3 must align. [Yes] J3, J6.
19. Plain fermented milk drinks (kefir, drinking yoghurt, buttermilk) are J3; sweetened or flavoured ones OUT. Ayran and plain lassi: J3 or OUT? [Ayran and plain lassi J3] J3.
20. Plain-cooked and tinned plain meat go to J1-D "Cooked, tinned & potted meats"; pastrami and corned brisket pieces to J1-B. [Yes] J1.
21. Margarine and plant-only fat spreads J5; spreads containing butter J3. [Yes] J3, J5.
22. Hard-boiled, pickled and preserved eggs are J3 (plain cooking or curing of one ingredient). [Yes] J3.
23. Par-fried and coated frozen vegetables (chips, hash browns) are prepared (OUT). Sprouting seed sold to eat is J5. [Yes to both] J4, J5.
24. Instant noodles: a dry brick with sachet J5, a cup or pot a ready meal (log as a Culinary gap). [Yes] J5.
25. Casks, futures and en primeur offers are OUT until delivered; a delivered cask is J7. [Yes] J7.
26. Sealed ready-to-drink cocktails and hard seltzer go to J7.7. [Yes] J7.
27. Home-brewing and winemaking ingredients J5, equipment B5. Bitters: by the dash J5, to drink by the glass J7. [Yes to both] J5, J7.
28. Live fish sold to eat are OUT (as the key reads); protected-species goods (shark fin) carry a flag attribute. [Both yes] J2.
Per-category structure
29. ★ J1 first axis: state of preparation or the animal (the literal "divided by species")? Candidate A needs a non-species sub-family. [State of preparation, with a generated by-animal view] J1.
30. J1 veal as its own leaf or inside Beef; offal under each animal or one cross-species leaf; primals and sides kept as kinds after the retail cuts. [Veal own leaf; offal under each animal; keep primals] J1.
31. ★ J2 first axis: form first (recommended) or animal group first. Evidence splits across source families. [Form first] J2.
32. J2 details: storage state as one attribute; fresh seaweed J4 and dried J5; whole salted-fermented seafood J2.3 and sauces J5; "caviar" only for sturgeon and paddlefish roe, uni in J2.1; scientific name required. [Yes to each] J2.
33. J3 plant alternatives as their own sub-family (against folding into each family). [Own sub-family] J3.
34. J3 details: evaporated and condensed milk in Milk; growing-up milk J3 but condition-labelled ranges H2; tenth cheese leaf for dried dairy once sourced; skyr and labneh as yoghurt, quark as cheese. [Yes to each] J3.
35. J3 further: egg class, grade, size and farming code as attributes; salted and unsalted as attribute; cheese leaf key (first-yes) as drafted rather than a pure moisture ladder. [Yes to each] J3.
36. J4 fruit-or-vegetable rule by sweetness as sold (avocado, tomato in Fruiting vegetables); cherry in Stone fruit; commercial types (cherry tomato, new potato) as named forms. [Confirm all] J4.
37. J4 details: load only cultivars attested as sold; frozen as an attribute; keep or fold the small sea-vegetable sub-family. [Attested only; attribute; fold] J4.
38. ★ J5 level-1 restructure (one sub-family axis, Preserved fruit & vegetables, tinned pulses with pulses) and the rice kinds by grain type. Confirm or return to shelf families. [Confirm] J5.
39. J5 details: flour with grains; honey with sweeteners; roasted and salted nuts J5 with a rule for coated nuts and trail mix; cake mixes J5.11, sprinkles OUT. [Yes to each] J5.
40. J5 soy sauce: the five JAS types as kinds (grades as attributes), and olive oil as one kind with legal category an attribute. [Approve both] J5.
41. J6 pack forms: drip bags and tea bags are `pack_form`; machine capsules and pods one kind (system in C13); tea capsules need a home once sourced. [Yes] J6.
42. J6 details: herb identity as kind; whole bean and ground one kind; matcha under Green tea; raw and ripe pu-erh as attribute; green-tea kinds by process. [Yes to each] J6.
43. J7 wine kind is grape or blend type (appellation a tag); sake kinds by composition; whisky kinds by production type with country a tag. [Confirm] J7.
44. J7 coverage: authorise a second pass (East Asian drinks, vermouth, EU wine and spirit rules) before approval; seed makers only from attested lists, at a stated cap. [Yes] J7.

### Shared-rule questions raised in this domain
- JC1: one `standard` and one `designation` table, and the placement rule for designated names (needs the wine-and-spirit exception decision against C11 and Culinary's s14 rule). Used by J1, J3, J5, J7, and in part J2, J4, J6.
- C11 (regional names) with C2(c): country-only kinds removed in J7; J3 Rule P rewritten to match.
- C4(a) to (e) and C16: ladders as attributes, tier entries only on makers, lines and named forms, no lot scores or batch certificates. J7 asks for tier on a variant (C4(a) extension).
- JC2 against the C4(d) item band: J1 to J6 all propose a per-kg or per-litre unit band; egg unit still unset.
- JC3 against C1: `maker_class` keeps C1 values and `supply_role` carries roles; `built_by_maker_id` (the C1 addition from the E and G reviews) is used by J1, J7.
- JC4 (state, process and pack): storage state an attribute; preservation process a level only on its stated axis (J5.10); machine capsules a kind with C13 ledger (J6).
- JC5(a), (b), (c) = `_framework_conflicts.md` entries "Formed products", "Spreads, pastes and dips" and "Mixed products" (J1, J2, J4, J5, J7).
- JC6 and C8: `tradition` vocabulary without a `cuisine` tag, and Culinary links from any row (all seven memos).
- JC7: shared variety table (J1, J4, J5, J6, J7).
- C3 variant types: J7 vintage and bottler edition; J6 vintage year and recipe code for pu-erh.
- C5(b) and (c): leaf skipped under about 12 kinds; first-yes keys for J1 level 1, J3 cheese, J5 rice, J7 wine. C5(d) (parts sub-family) does not apply to J (review X12).
- C9 alias table: new `trade mark` relation (J4); "caviar", "pancetta/panceta" and "pickle" homonym rows.
- C13 compatibility ledger (J6 capsules); C14 multi-use kinds (J1 offal); C17 jurisdiction ledger (J7, nothing fetched).
- `_framework_conflicts.md` J entries: edible insects, par-fried vegetables, bitters, packaged prepared kinds Culinary lacks; step 1 wording of "alcohol-free" (J6 and J7); sprouting seed (J4, J5).
END J
