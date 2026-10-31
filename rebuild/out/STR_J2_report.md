# STR_J2 report (Fish & Seafood)

**Counts before → after:** departments 7 → 7; shelves 24 → 32; kinds 154 → 171; archetypes 162 → 110. validate.py --v3: OK.

**Added:** category `ax` and `key` (7 steps plus a precedence note); `t` and `ax` on every department; `t` on every shelf, `ax` on every shelf over three kinds; hand-written `tt` (named axes: Species, Cut, Form, State, Packing medium, Cure and so on) on every kind, replacing the flat `t` lists.

**Regrouped:** Fresh fish now runs by family or water (salmon, cod family, oily and open-sea, flatfish/rays/sharks, coastal and reef, deep-sea, freshwater). Shellfish runs by animal (oysters, other bivalves, snails and abalone, crabs, lobsters and crayfish, prawns, squid and others). Smoked fish by fish group. Tinned fish by what is in the tin, with marinated fish on its own shelf. Roe by how it is sold. Salted/dried split into salted, fermented, dried fish, dried shellfish. Fish-paste split into cakes, sticks/balls, coated fish, patties and spreads.

**Split/renamed:** "Flatfish & skate" → Flatfish (+ new Skate & ray); recorded in J2_renames.json. No kinds merged or moved to other categories.

**Added kinds (reference: Wikipedia List of types of seafood, Smoked fish, Smoked sable, Himono, Bombay duck, Hanpen, Otah, marxfood roe guide, UCSB Olympia oyster page):** Skate & ray, Shad, Pacific saury, Lamprey, Olympia oyster, Barnacle, Jellyfish, Sea squirt, Smoked halibut, Smoked sable, Smoked whitefish, Smoked sturgeon, Whitefish roe, Himono, Bombay duck, Hanpen, Otak-otak. Eomuk added as an alias of Satsuma-age.

**Coverage references per department:** fresh fish and shellfish: List of types of seafood; smoked: Smoked fish; roe: marxfood guide; dried/salted: Himono, Bombay duck pages; fish cakes: Kamaboko, Hanpen, Satsuma-age, Otah; tinned: thetinnedfishmarket guides (no gaps it could confirm).

**Archetypes demoted (37 moved to `m` with maker):** producer or brand ranges (Rio Mare, John West, StarKist, Herpac, Ortiz, Olasagasti, Petrossian, Ummera, Burren, Belvelly, Severn & Wye, Connétable, King Oscar, Bevans and similar) and generic descriptions (West Coast Kumamoto, NSW estuary rock oyster, Creel-caught langoustine, Hybrid sturgeon, British potato fishcake, Scandinavian gravad lax, Galician mussels in escabeche). A further 15 that only restated an alias or a type (Red king crab, Ventresca, Honkarebushi, Arabushi, Karebushi, Hwangtae, Bugeo, Kanikama, Golbaengi and others) were removed because the name already sits in the kind's aliases or `tt`.

**Cross-links:** 59 `see` links, all targets checked (J2 internal; J5 Fish sauce and Dashi and dashi ingredients; H2 Omega-3 oil). STR_SEE.tsv has no J2 rows.

**Not done:** tinned shrimp, tinned cuttlefish and monkfish liver (ankimo) could not be sourced from a fetched page, so not added; the new-kind definitions for Lamprey, Jellyfish and Barnacle rest on the seafood list page only. Firecrawl and Parallel were out of credit; all pages via WebFetch. No brands file change needed.
