# FIX_J4 report

Counts: kinds 208 -> 200; archetypes 1,078 -> 621; departments 5 -> 4; brands 33 -> 37. validate.py: OK.

- **J4-1 partly.** Removed 461 RHS garden-cultivar archetypes (24 retained that are sold by name, e.g. Discovery, Concorde, Crown Prince, Hispi, Marmande). No living-plants category exists to receive them, so they are dropped, not moved. 621 remain, above the ~400 target: the rest are Wikipedia-sourced and were not pruned.
- **J4-2 done, partly.** Echo archetypes for Clementine, Yuzu, Sudachi and Kabosu deleted; Clementine's versions (Clemenules, Fina, the PGIs) promoted to archetypes. Yuzu, Sudachi and Kabosu merged into "Japanese aromatic citrus" (the finding's name "Koji citrus" is not a recognised term), keeping the two GI entries as archetypes. Enoki, Shimeji, Maitake, Lion's mane and Wood ear merged into "Speciality cultivated mushrooms" with types. Mixed packs department dissolved: Fruit gift box moved to a new "Premium & gift fruit" shelf (type: mixed fruit pack); mixed berries became a type of Blueberry; mixed vegetables and fruit-and-veg trays became types of Mixed salad leaves. Other empty kinds (Cloudberry, Mangosteen, Kiwano, Sage, Chives and others) left: valid product kinds the finding did not ask to merge.
- **J4-3 done, partly.** Added Shizuoka Crown melon (archetype under Melon, fetched ikigaifruits page), brands VOG, Marlene, Val Venosta, Melinda (producereport and Fruitnet pages fetched), and fresh Dulse and Sea lettuce kinds (Wikipedia). Fresh nori not added: Wikipedia confirms only iwanori (rock nori) as fresh, not a retail product.
- **J4-4 done.** Shelves merged: Pome fruit (Apple lead), Soft fruit (Strawberry lead), Mangoes with bananas, pineapples and papayas, Potatoes with sweet potatoes and tropical roots.

Moves: none (J4_moves.json unchanged). Unsourced and not added: Melinda founding year, Marlene and Val Venosta founding years. Sources log: rebuild/work/FIX_J4/sources.tsv. Backups: rebuild/work/FIX_J4/bak/.
