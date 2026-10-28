# FIX_B6 report (Cleaning & laundry)

Counts before -> after: kinds 83 -> 76 · archetypes 1 -> 12 · flat models 359 -> 266 (max 6 per kind; was 12) · brand register 85 -> 88.

- **B6-1 done.** Added 11 archetypes with fetched Wikipedia sources (Roomba, Dyson DC01, Hoover Model O, Dustbuster, Numatic Henry, Electrolux Trilobite, Kirby, Vorwerk Kobold, Rainbow, Hoover Constellation, Hoover Dustette). Versions only where the page gave them. Their models left `m`. Brands Kirby, Vorwerk, Rexair added to the register. Not sourced and left out: Henry HVR160 (stays in `m`), Kobold generations after Model 30, Dustette versions, Kirby founding detail beyond the page, founding years for Vorwerk and Rexair.
- **B6-2 done (mechanical).** `m` capped at 6 per kind, one model per maker first. Range entries dropped where they repeated a retained model or only the brand name. No independent-test winners were re-sourced, so the cap kept the existing order rather than picking test winners.
- **B6-3 done.** Rinse aid and salt folded into Dishwasher detergent, Spin mop system and Dust mop into Wet mop, Waste-paper basket into Kitchen bin (as types and aliases); trade Hard-floor scrubber-polisher dropped.
- **B6-4 partly.** Pedestal and stacking kit moved to Front-load washing machine as a type. Integrated washer, built-under dryer and under-counter compactor kept as types: G3 has no compactor or integrated washer kind to link to, and the schema has no cross-link field.
- **B6-5 skipped.** Vacuum storage bags, shoe-care kit and clothing-care cabinet: the finding asks for cross-links only, which the schema cannot hold, and adding kinds would conflict with the restraint rule. Left for a later cross-link pass.

Moves file and traditions file unchanged. Backups in rebuild/work/FIX_B6/bak/. validate.py: OK.
