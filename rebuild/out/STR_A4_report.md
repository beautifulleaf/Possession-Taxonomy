# STR_A4 report (A4 Bags & Accessories)

Before → after: departments 9 → 9; shelves 22 → 24; kinds 97 → 105; archetypes 241 → 237. Validator: OK (--v3). File 251 KB.

**Structure.** Category `ax` and 9-step `key` written. Every department has `t` and `ax`; every shelf has `t`, and `ax` where it holds more than 3 kinds. Handbags now split by how the bag is carried (handles, shoulder, crossbody, hand). Wallets split by what they hold. Eyewear split into frames by shape, sunglasses for a purpose, prescription and reading, antique, accessories. "Umbrellas & fans" became "Umbrellas, fans & canes" (fashion cane joins). Shopping trolley moved to Luggage soft bags. Every kind has hand-written `tt` (no flat `t` left).

**Merged.** Canvas tote into Tote bag; Wheeled duffel into Duffel bag (archetype and model carried); Prescription sunglasses and Spectacle frame into Prescription glasses (lens types, not kinds).

**Added (source).** Barrel bag, Wristlet bag, Gladstone & doctor's bag (Gladstone archetype moved from Top-handle bag), Travel wallet, Fashion backpack (Prada nylon backpack, 1979), Rolling backpack, Oversized & bug-eye frames, Rivet spectacles, Scissors glasses, Lens cloth & cleaning kit, Pouch sling, Onbuhimo; archetypes Rollaboard, Tessen, Mai ogi, Kawahori-ogi.

**References checked per shelf (fetched):** Wikipedia Handbag (handbag shelves), Wallet (wallet shelves), Glasses (eyewear), Backpack, Luggage, Umbrella, Hand fan, Briefcase, Baby sling (carriers), Prada. Changing bags and bag accessories: no reference fetched.

**Generic archetypes demoted to types:** Solid-stick umbrella, School satchel, Steamer trunk, Wardrobe trunk, Dome-top trunk, Train case (now an alias of Vanity case), Half-moon bag, Palm-leaf fan, Feather fan.

**Cross-links added:** 31 `see` entries (e.g. Fashion cane to Walking stick and Collector cane; Laptop backpack to Camera backpack; Lorgnette to Opera glasses; Folding fan to Handheld fan; Toiletry bag to Toiletry & make-up bag). All targets checked to exist. No STR_SEE.tsv pairs involve A4.

**Moves:** none new; existing A4_moves.json untouched.

**Not done / caveats:** Firecrawl and Parallel were out of credit, so all pages came through WebFetch (long pages read to about 100,000 characters). Famous archetypes were not added beyond those above; shelf-level coverage of Eyewear frame shapes relied on the Glasses page only. Brand file unchanged (Prada already present).
