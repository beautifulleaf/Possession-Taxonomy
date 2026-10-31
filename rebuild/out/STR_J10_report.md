# STR_J10 report: Smoking & Vaping

Before: 9 departments, 23 shelves, 122 kinds, 209 archetypes. After: 9 departments, 30 shelves, 130 kinds, 202 archetypes (net of 16 added and 23 demoted). validate --v3: OK.

**Added:** category ax and a 9-step placement key; t and ax on every department; t on every shelf (ax where over 3 kinds); every kind's flat types replaced by hand-written tt groups.

**Shelves regrouped:** Cigars (humidor shelf split into Humidors & humidity control, Cutters & cases); Pipes (tools split from storage); Snus/snuff (split into snus and pouches, chewing/dipping/regional oral, nasal snuff, boxes and bottles); Hookah (tobacco split from hookahs, bowls/heat/coals split from hoses/parts); Herbal (two shelves by route); kind order set by each shelf's axis.

**Merged/renamed:** Hookah hose + Hookah mouth tip -> "Hookah hose & mouth tip"; Moist snuff -> "Dipping tobacco" (J10_renames.json). No moves.

**Added kinds (sourced, Wikipedia):** Cigalike, Vape drip tip (Construction of electronic cigarettes); Permanent match (Lighter); Creamy snuff, Gutkha, Naswar, Iqmik (Smokeless tobacco); Rapé (List of tobacco products); Khansar (Hookah).

**Added archetypes:** Cuban marques Vegas Robaina, Diplomáticos, Fonseca, El Rey del Mundo, Saint Luis Rey, Juan López, Vegueros, La Gloria Cubana, Sancho Panza (Habanos S.A.); Don Pepin Garcia (List of cigar brands); Poker, Tankard (Tobacco pipe); Ronson Pist-O-Liter, Ronson Wonderlite, Thorens Standard Original, Flaminaire Gentry (Lighter). Five stub brands added to J10_brands.json.

**Generic archetypes demoted to m (versions kept):** Burmese/Indian cheroot; Davidoff desktop humidor, Boveda humidor, Elie Bleu; Henckels cutter; Turkish carved meerschaum; Missouri Meerschaum cob; Clay churchwarden; Calabash; Rau/Nobe kiseru; German snuff; three snuff-bottle forms; Chillum, One-hitter and dugout; Dunhill butane, S.T. Dupont, Colibri; RooR, Illadelph. A stray heated-tobacco entry ("with") removed and Ploom given its maker.

**References per shelf:** Wikipedia List of tobacco products, Tobacco pipe, Hookah, Lighter, Humidor, Construction of electronic cigarettes, Habanos S.A., Smokeless tobacco, List of cigar brands (fetched via WebFetch 2026-10-31). Cannabis, herbal and rolling shelves were checked only against those pages' lists and the existing sources; no extra cannabis reference was fetched.

**Cross-links:** E6 Hygrometer, E3 Rosin, C3 Salvia (required pairs) plus 16 within-category links.

**Not done:** no new archetypes in tier shelves; heated-tobacco devices have no sourced archetype (IQOS not fetched); some old archetype makers (Castleford, Senior, Flamagas and others) are not in the brand index.
