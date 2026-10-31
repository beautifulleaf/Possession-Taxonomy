# FIX_J8 report

Counts: archetypes 532 -> 524, kinds 111 -> 111 (audit's "123" was models+kinds; the 12 empty nut kinds no longer exist), brands 247 -> 341 (6 merged away, 7 real brands and 93 stubs added).

- J8-1 done/partly: Single-origin dark chocolate re-axed on makers (Amedei, Cluizel, Pralus, Domori, Marou, To'ak, Dandelion). Concepts (vintage, two-ingredient, Criollo varietal, Chuao/Porcelana) moved to the Chocolate dept `b`. Added Askinosie, Pacari, Friis-Holm, Fruition, Menakao (fetched pages). Not added: Raaka (403), Akesson's, Castronovo (no page fetched). Marou province versions (Ben Tre etc.) left out: not confirmed. Valrhona vintage archetype dropped (no versions).
- J8-2, J8-4 skipped: nut kinds already collapsed; Marcona/Bronte/Piemonte PDO archetypes not sourced this session.
- J8-3 done: 13 flavour archetypes became `t` types; added maker archetypes Ben & Jerry's, Haagen-Dazs, Jeni's, Salt & Straw (fetched Wikipedia). Heritage forms (Moose Tracks, hokey pokey, booza, Maras) kept.
- J8-5 partly: Brioche removed from Viennoiserie; Toblerone removed from Countline. Dulce de leche (J3) and hot chocolate bomb (J6 Drinking chocolate) duplicates kept, noted only; no RULES clause homes them elsewhere.
- J8-6 done: department renamed "Sweets & confectionery".
- J8-7 done: merged Arnott's Group, Barry Callebaut, Kellanova, Lotte Wellfood, Meiji Seika, Frito Company into the consumer brands (old names in `rel`), mk remapped. 93 missing mk values got stub register entries (name and source only; country, founding, segment left blank as unsourced).
- No moves to J5 needed; _moves.json unchanged. validate.py: OK.
