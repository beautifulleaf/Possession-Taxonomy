# FIX_A1 report (A1 Clothing)

Counts before → after: kinds 210 → 227, archetypes 730 → 759, brands 2,530 → 2,531 (Levi's merged, Orchard Corset and Fanatics added), traditions 96 → 92, moves 21 → 22. validate.py: OK.

- **A1-1 done.** "Traditional, ceremonial & uniform headwear" split into Skullcap (faith tags), Fez & brimless cap, Turban & head-wrap, Conical & woven sun hat, Folk felt hat, Academic cap, Uniform headwear, plus Clerical hat, Court & official hat and Historical hat & bonnet so no type was lost. Deerstalker and sou'wester are in the new Country & weather hat. Novelty hats go to E1 via moves. Uniform headwear points to Militaria (E4) in its definition. Zanzibar kofia and a Bukhara tubeteika were not confirmed, so left out.
- **A1-2 done.** New Football shirt, Basketball jersey, Ice-hockey jersey and Baseball jersey with sourced archetypes; "Team jersey" kept as the catch-all for other sports. Not sourced, so omitted: Umbro 1990s templates, Swingman, authentic/replica versions per template. Team lists kept out.
- **A1-3 done.** Added Sporran, Kilt pin, Sgian-dubh, Smoking jacket, Plus fours & breeks, Mackinaw.
- **A1-4 done.** Collar stay and Cummerbund folded into Formal accessories; the detachable lining kind became a type on Overcoat. Leg warmers left (the finding gave no fix).
- **A1-5 done.** Corset top merged into Corset; the shapewear bodysuit type folded into Bodysuit.
- **A1-6 done.** Bisht stays under Abaya; Beckenbauer and Firebird stay under Tracksuit (versions merged); the sari cloths stay under Sari with notes on the cloth kinds.
- **A1-7 done.** Tracksuit moved to Casual jackets. Rain, army and cycling ponchos became Raincoat types. LZR Racer, Fastskin and related racing models and ranges were removed from Swimsuit, with a pointer to Sports. Glen plaid and houndstooth became types of Tweed cloth.
- **A1-8 partly.** Levi's and Levi Strauss & Co. merged and 'Adidas', 'André Courrèges' normalised; four tradition pairs merged. About 30 further archetype `mk` values still lack register entries (e.g. Worth London, Chapal, Trần Kim) or are multi-name strings; they need sourcing, so were not guessed.
