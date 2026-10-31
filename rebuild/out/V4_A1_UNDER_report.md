# V4_A1_UNDER report

Part file: rebuild/out/A1_parts/UNDER.json (replaces Underwear, nightwear & swim; Hats & headwear; Scarves, gloves & belts). Validates OK: 63 kinds, 170 entries (131 before, +39 new). 43 Wikipedia pages fetched (list in rebuild/work/V4_A1_UNDER/sources.tsv).

Method: read the whole register (2,531 brands) by script and took every `sig` and `lines` item matching these garments; most were already entries or versions. Added the rest, with the brand's register `s` page as source. Read the garment articles for originators. Fields added to all entries: `g` (brand country, forms without a brand last), `cty`, `own`/`own_y` only where a fetched page states them (Spanx: Blackstone 2021; Jantzen: Jantzen Brands Corporation 2019; Hanes/Maidenform: Hanesbrands; '47: New Era 2024), `nl`, `sel` with a coverage line, `xg`. Origin roles (7): Jockey Y-front, Boss of the Plains, Panti-Legs, Hermès carré, Réard bikini, Union suit, Coke hat. Landmark: Spanx OnCore (MoMA collection since 2017). Removed the mistaken "Hat body" buying-order block from Scarves, gloves & belts.

New entries by kind: Bra +4 (Jacob backless brassiere, Frederick's padded bra, Playtex 18 Hour, Triumph Doreen); Men's underwear +1; Undershirt +1; Shapewear +1; Corset +1; Tights +1; Thermal +2; Socks +1; Swimsuit +8 (five Speedo lines, Eres Aquarelle, Jantzen, Burkini); Bikini +2; Cover-up +1; Homburg +1; Top hat +4; Fedora +1; Baseball cap +2; Headband +1; Headscarf +2; Cloche +1; Neck gaiter +1; Shawl +2; Belt +1.

Loose models `m`: 134 removed. Kept as versions where the maker had an entry (Jockey Low Rise/Midway, Orlebar Brown fits, Hunza G cuts, Birdwell, Seafolly kaftans, Buff, Smartwool, Icebreaker, Onia not kept, M-Pact, Rapha Tom Simpson). The rest were retailer SKU lines (Wolford, Falke, Disturbia, Darn Tough, Hestra extra models, Lewis Leathers, Levi's belts and others) with no attesting page: removed as out of scope.

Not finished (stated plainly):
- List of hat styles (about 168 entries) was read only for its first 100,000 of about 194,500 characters, and only to check existing names; the full list is not imported as entries. Kinds with named forms (Dastar, Pagri, Imama, Kavuk, Tagelmust, Mob cap, Carlsbad, Ten-gallon) are not in that list's first window; they stay on earlier sources.
- Register lines not placed (garment unclear): Kangol Spitfire/Tropic/Furgora, Lock & Co. Whitebridge, Heat Holders Alta/Jordan, Resistol, Akubra range lines, Vilebrequin Mahina, Albert Thurston and Trafalgar braces (no kind for braces here).
- Regional forms named in the Scarf, Sock, Glove and Mitten articles (dupatta, khata, tabi, beoseon, Latvian mittens) not added: traditional dress is tentative (BRIEF 2026-10-31).
- Cowboy kinds' own Wikipedia article not re-fetched; existing entries keep earlier sources.
- Market fields: `tier` and department `ms` not set; the tiers are defined for groceries and no fetched page gives clothing market shares. Alexander McQueen and Triangl have no country in the register.
- No new brand register entries or brand_updates written (arrays empty).
