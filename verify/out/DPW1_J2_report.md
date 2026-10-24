# DPW1_J2 report: J2 Fish & Seafood decision pass

Offline Opus pass on HV_J2_1 (the only J2 harvest report) and its missing-kinds TSV. No web, no git, no writes to data/.

## Task 1: missing kinds (94 single items)
new_kind 74, named_form 10, covered 7, attribute 2, other_category 1. Whole capelin was not found on sale, so it gets no row.

New kinds (R-58, next free number under the parent):
- J2.1.1.24–46 finfish (23): eel, sablefish, tilapia, pangasius, snakehead, pomfret, croaker, scad, milkfish, catfish, flounder, smelt, grouper, snapper, Dover sole, lemon sole, red mullet, gurnard, John Dory, zander, carp, turbot, Patagonian toothfish.
- J2.1.2.07–13 crustaceans: spot prawn, northern prawn, Argentine red shrimp, white shrimp, tiger prawn, giant freshwater prawn, crayfish.
- J2.1.3.07–15 molluscs: whelk, periwinkle, mud snail, apple snail, top shell, land snail (escargot), clam, razor clam, cockle.
- J2.2.08–09: smoked haddock, smoked sprats.
- J2.3.08–12: dried abalone, fish maw, dried shark fin, dried bonito (katsuobushi), cured salmon (gravlax).
- J2.4.05–19: tinned anchovies, marinated anchovies (boquerones), and tinned mackerel, herring, sprats, salmon, mussels, octopus, squid, clams, cockles, razor clams, scallops, eel, cod.
- J2.5.1.05–10: kaluga, Amur sturgeon, white sturgeon, sterlet, hackleback, paddlefish caviar.
- J2.5.3.03–08: capelin, herring, pollock, cod, bowfin and grey mullet roe.
- J2.6.07: fried fish cake (satsuma-age).

Named forms: mentaiko, bottarga, Arbroath smokie, finnan haddie, bonito del norte, tinned kipper, soft-shell, swimming and Dungeness crab, kikiam. Covered: bulot, tarako, smoked cod roe, swai, scampi, rock lobster, spiny lobster. Attributes: white tuna (species within tuna), salt-packed anchovies (pack medium). Other: kabayaki eel is OUT (sauced, so prepared).

## Task 2: named forms (38 reviewed)
2 drops: kanikama (an alias of J2.6.01) and Fuzhou fish ball (pork-filled, so OUT under K-45). There are no to_line or move_kind rows: the three lines already exist and their models are proper named forms. Grocery products with descriptive names (Regiis Ova Salmon Roe, Ichimasa Chikuwa) stay, because C2(e) makes a single product in one kind a maker-bound named form. Siberian osetra stays under osetra ("and related osetra sturgeon").

## Task 3: navigation, decided by shopper path
J2 is not scene-driven. No J2 scene has a definition source, and the tinned-fish scene is held back (memo §7). The 266 makers are tied only at category level. Kinds were harvested from retailer trees (Weee, Fish Society, Knuspr) that lead with form and then species, as memo §2 found. The only brand-led pockets are canneries (142 of 283 makers, from the AllTinned and Premium Sardines directories) and caviar houses.

View:
1. **How is it sold?** Fresh & frozen · Smoked · Salted, cured & dried · Tins & jars · Roe & caviar · Fish cakes & pâtés.
2. **Which animal?** For example, Fresh & frozen → Fish · Prawns, crabs & lobster · Shellfish, squid & snails · Sea urchin & sea cucumber · Mixed. Tins & jars → Fish · Shellfish & cephalopods, with a "by cannery" tab (by country). Roe → Sturgeon caviar (with a "by house" tab) · Salmon & trout · Other roe.
3. **Which species?** Kinds. Finfish (46 kinds) gets the generated `species_group` grouping (salmon & trout, white fish, flatfish, tuna & swordfish, oily fish). Below that, the filters are storage state, cut, wild or farmed, certification and origin.

## Rules applied
C2(a)/(c)/(e), C9, C11, P1, P3, P4b, P7, P8, K-26, K-45, K-47, R-54, R-58, R-96(c), J-4/J-5 (the caviar vocabulary), memo §4b.

## Structural notes
- J2.4 now holds 19 kinds and J2.3 holds 12, above the C5(b) "about 12" mark. I added no leaves, because ids are never renumbered (R-58) and J-4 is decided. Grouping by animal group can be a display view, or an OWNER QUEUE item.
- The kinds of L-ramon-pena-silver-line should add J2.4.01 (bonito del norte).
- There is no base "kipper" named form under J2.2.05.

## Decisions resting on † claims (need the attesting fetch)
Fuzhou fish ball filling; kabayaki glaze; kikiam wrapper; land snail (the listed item is sauced, so a plain-snail page is needed); boquerones (not on the harvester's page); finnan haddie; top-shell and mud-snail identity; Amur caviar possibly a hybrid; tinned cod possibly cod liver.
