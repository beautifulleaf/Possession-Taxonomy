# V4_B6 report (Cleaning & Laundry, light pass)

All 86 kinds are treated as commodity kinds. Entries before -> after:
- Loose models (m): 265 -> 0. Ranges (r): 62 -> 0. All removed as out of scope for commodity kinds.
- Named entries (x): 12 -> 0, in Cylinder, Upright, Robot and Handheld vacuum cleaners and Trouser press (including Henry and its versions). Removed because the brief says all kinds here are commodity; the makers stay in the brand register. If the owner wants Henry-type entries kept, they need a canon reference, which was not found in this pass.
- t, ax, tt and see untouched. No renames (B6_renames.json is empty) and no new moves.

Brand register: 58 makers and brands from the removed models added to B6_brands.json (88 -> 146). Country and founding year filled only for Procter & Gamble (US, 1837), Unilever (UK, 1930), Reckitt (UK, 1999, merger year) , Church & Dwight (US, 1847) and 3M (US, 1902), from fetched Wikipedia pages. The rest, and Henkel, have empty country and year and a placeholder description; they need a later sourcing pass.

Market panels (ms and msum), all from fetched pages:
- Vacuums & floor machines: Dyson over 15 % of household vacuums and top five 54.5 % (2025, Global Market Insights); robot vacuums Roborock 17.0 %, Ecovacs 11.5 %, SharkNinja 10.5 %, Dreame 7.5 % (2025, same publisher); smart-vacuum units Q1 2025 Roborock 19.3 %, Ecovacs 13.6 %, Dreame 11.3 %, Xiaomi 9.9 %, iRobot 9.3 % (IDC; WebFetch gave 403, so Firecrawl was used for one page).
- Washing machines & dryers: Haier 16.6 %, top five (Haier, Samsung, Whirlpool, LG, Midea) 38.1 % (2025, Global Market Insights; the page also says 38.2 %).
- Laundry products: Procter & Gamble 35.1 %, Unilever 15.0 %, Henkel 7.5 % (2025, Global Market Insights, laundry care).

Not sourced: dishwashing and general cleaning-product shares, regional market leaders, dryer and iron markets. Shares come from a commercial research publisher whose method the pages do not state; other search results gave conflicting figures and were not used because the pages were not fetched.

validate.py --v3 out/B6.json: OK (0 errors). Fetches: 11 (one via Firecrawl). Backups in rebuild/work/V4_B6/bak/.
