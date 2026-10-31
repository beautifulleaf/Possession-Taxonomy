# STR_B4 report (B4 Decor)

**Counts, before to after:** departments 8 to 8; shelves 19 to 27; kinds 94 to 107; archetypes 166 to 148. validate.py --v3 prints OK.

**Structure:** category `ax` and 8-step `key` added; every department has `t` and `ax`; every shelf has `t` (and `ax` above 3 kinds); every kind has hand-written `tt`. Lead unchanged.

**Reshaped**
- Vases: one "Vase" kind split by material into Glass, Porcelain, Earthenware & stoneware, Metal vase. Shelves now Vases, Jars & bottles, Bowls & urns, Glass paperweights.
- Candles: "Free-standing candle" keeps pillar, taper and tealight as shapes. Incense rebuilt by form: Stick, Cone, Coil, Rope & paper, Loose, Paste, Smudge; burners get their own shelf.
- Seasonal: shelves by festival (Christmas split three ways, Halloween, Easter, East Asian festival decor) plus Folk dolls & figures. Ore Mountains pieces moved out of the mixed collectibles shelf; Snow globe sits with Christmas.
- Fireworks: "Ground firework" split into Fountain & wheel and Firecracker & banger.
- Garden: shelves Statues & figures, Focal pieces, Wind & water features. Flamingo moved to the new Lawn ornament kind.
- Artificial plants split into Imitation and Dried & preserved shelves.

**Renamed:** Entrance decoration to New Year entrance decoration; Stick and cone incense to Stick incense.
**Merged:** Ground firework into the two new kinds; Ultrafragola moved to Floor mirror.

**Added kinds (reference):** Wick trimmer, Scented beads & gel, Moravian star, Cone incense, Incense rope & paper, Paste incense, Smoke & novelty firework, Lawn ornament, Rain chain, and the four vase kinds. References fetched: Wikipedia Vase, Garden ornament, Candle, Incense, Christmas decoration, Fireworks, Paperweight, Mirror, Artificial flower, Party popper, Air freshener, Picture frame, Flag. Added archetype: Millville rose.

**Generic archetypes demoted (19):** to types: Overmantel mirror, Millefiori, Lampwork and Sulphide paperweights, Bohemian cut-glass vase, West German pottery vase, Iznik-style vessel, Masala agarbatti, Dhoop. To ranges `r`: Moser coloured crystal vase, Textured range, Carnaby series, Blenko designer vase, Shoyeido Daily and Premium, Nippon Kodo Traditional Series, Seiun, Morning Star, 3-Wick Candle. Named scents under the five incense ranges were not kept.

**Cross-links:** about 45 `see` entries, all targets checked to exist (F2 Art glass and Art pottery, F4 Incense burner, E1 Piñata, B3 Hurricane lantern and others).

**Not done:** no new sources for Halloween, Easter, Lunar New Year and folk-craft shelves (Halloween and collector-plate pages gave 404); existing coverage kept. Firecrawl was out of credits, so WebFetch was used. Note F2 also holds "Venini Fazzoletto vase", a duplicate of the B4 Fazzoletto archetype. No moves added.
