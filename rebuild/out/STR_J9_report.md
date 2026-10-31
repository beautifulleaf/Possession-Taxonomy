# STR_J9 report (Soft Drinks & Water)

**Before -> after:** departments 8 -> 8; shelves 10 -> 28; kinds 84 -> 91; archetypes 192 -> 169. Validator: OK (--v3).

**Category and departments:** added `ax` and an 8-step `key`; every department has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than 3 kinds. All 91 kinds now carry hand-written `tt` (no flat `t`).

**Reshelved:** Sodas cut by flavour family (cola and spice, citrus, fruit and sweet, root/cream/herbal); Tonic and mixers by taste added; Juices by raw material and dilution; Syrups by use; Fermented drinks by what ferments; Energy and sports by purpose; Water by source, gas, additive, ice; Ready-to-drink split into coffee and tea.

**Merged or renamed** (in J9_renames.json): Mexican & Latin American soda -> Fruit soda; Cordial-based soda -> Mixed-fruit soda; Craft & prebiotic soda -> Prebiotic & functional soda; Grenadine & cocktail syrup -> Grenadine. Tango, Sinalco, Mirinda moved to Orange soda, Ting to Citrus soda, Jarritos to Fruit soda, Cheerwine to Cherry soda, Sidral Mundet and Manzana Postobon to Apple soda. Nothing moved to other categories (J9_moves.json unchanged).

**Added kinds** (source in brackets, all fetched): Cherry soda and Apple soda (Soft drink; Sidral page), Grapefruit & citrus juice (Juice), Mageu and Kanji & vegetable ferments (Fermented drink), Simple & gomme syrup (Simple syrup), Orgeat and Falernum (split from Grenadine, existing sources).

**References used per shelf:** Wikipedia Bottled water (Water shelves), Soft drink (all soda shelves), Juice (juice shelves), Fermented drink (fermented shelves), Simple syrup (bar syrups). Tonic, energy, sports and ready-to-drink shelves were checked against the existing kind lists only; no further reference was fetched (Firecrawl and Parallel out of credit), so coverage there is unverified beyond the previous pass.

**Demoted archetypes (22):** Golden ginger ale, Grape soda, Vanilla cream soda, Red/pink cream soda, Birch beer (to types), Sarsaparilla, Dandelion & Burdock, Apfelschorle and Sour mix (to types), Canned oolong tea, Orgeat/Falernum/Grenadine (became kinds); ranges moved to `r` with versions kept as models in `m`: Crush fruit flavours, Fanta flavours, Fanta Guarana, Teisseire sirop, Monin sirop, Torani syrup, Monin coffee syrup, SodaStream syrups, Perrier flavoured, Bundaberg brewed soft drinks.

**Cross-links:** 31 `see` links, mostly within J9; external to B5 (Soda maker, Kombucha and kefir vessel), C3 (Kombucha SCOBY, Water kefir grains), J3 (Kefir, Drinking yoghurt & ayran, Coconut drink), J6 (Cold brew & coffee concentrate, Iced tea mixes & tea concentrates, Yerba mate). All targets verified.

**Not done:** no new archetypes added (Tier juice and mixer shelves); no new brands needed; sources log at work/STR_J9/sources.tsv.
