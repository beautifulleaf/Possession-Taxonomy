# V4_A1_TOPS report (second pass)

Part file: rebuild/out/A1_parts/TOPS.json. Replaces Tops; Trousers, jeans & shorts; Dresses; Skirts, jumpsuits & sets. Validates OK: 70 kinds, 377 entries, 61 new brand rows (25 badges: 23 origin, 2 landmark). No `m` or `r` remains.

## Method
- Brand register read in full by script; every `sig`/`lines` item matching a kind became an entry.
- 70 Wikipedia pages fetched (log: rebuild/work/V4_A1_TOPS/sources.tsv), including the twelve empty-kind checks. Every originator they name became an entry.
- Correction applied: all 178 earlier loose models and ranges were looked up in data/named_forms.tsv. 104 had a recorded page. Those pieces are restored as entries with that page and its note as `d` (3sixteen SL-100x, ONI 288, Burgus Plus Lot. 771, Mister Freedom Lot 64 Outlaw, Naked & Famous Weird Guy, Tellason Ladbroke Grove, Benzak BDD-006, Indigofera Clint, N.Peal, Barbour cardigans and others). Real McCoy's Lot. 001XX, orSlow 105 and 107, Edwin 503, the Barbour Steve McQueen Radial Overshirt, Reigning Champ Midweight Terry Hoodie, Uniqlo Super Non-Iron, Fila Borg polo, Freddy WR.UP, Gymshark Arrival, the Naked & Famous Elephant series, the J.Crew x Canterbury rugby shirt and Susana Duniau's pilucho were confirmed on fetched pages.
- Country (`g`, `cty`): register `c`; else the country stated in a fetched page; else `data/makers.tsv` (the earlier harvest's sourced maker record); else "Country not stated" (14 entries). No general knowledge.
- Tier: set only where `own` is known. Global group: Gildan (Bonds), Authentic Brands (Champion), Hanesbrands, VF (Icebreaker). Independent: Maus Frères, Sankyo Seiko, Rossignol, BCBG Max Azria, Workwear Group, I.T Group, Itochu (Edwin, per Wikipedia).

## Empty kinds (12 checked)
New originators: Pleated skirt (Fortuny pleats, Havelova-Vanek box pleat), Harem pants (Poiret, Margaine-Lacroix, Bourniche, Hammer pants), A-line skirt (Dior 1955), Culottes & skort (Montgomery Ward skort, Poiret jupe-culotte; plus Uniqlo culottes from a recorded page), Plus fours (Benjamin Bixby 2008).
Still empty (pages name none): Cricket shirt, Denim shorts & cut-offs, Wrap skirt, Tiered & prairie skirt, Co-ord set. Blouse (Uniqlo, from recorded pages; Wikipedia names only a 1913 catalogue seller) and Sweater vest (Lands' End, recorded) are filled from recorded pages.

## Removed: no page names the piece
Carter's Bodysuit multipack; adidas, Nike and Puma "Authentic / Replica" and "Match / Stadium" lines; Score Draw and COPA retro shops; Barbour Glendale and Crail overshirts; Worth London Pussycat bow blouse; Channel Jumpers; Prince of Wales Fair Isle (a wearer); Reigning Champ Midweight Terry crewneck; J.Crew Heritage 14 oz sweatshirt; Le Coq Sportif sweatpant (page 404); British battledress, US paratrooper and BDU trousers (brandless); Anne Fogarty shirtwaist; Kinderwhore babydoll; Overall dress; Pinup Girl Viva tulip skirt and Pinup Couture; Disco dance catsuit; Atsuko Kudo latex catsuits (search refused; no page); Women's playsuit.

## Limits
- Restored pieces cite the page recorded in named_forms.tsv; some are retailer, category or blog pages, and a few (Glenmuir g.Morar and g.Deacon, Andersen-Andersen on a forum) cite pages that name a neighbouring piece. Not re-fetched.
- New register-based entries cite the register `s` page, not re-fetched.
- No department `ms`/`msum`: no sourced market figures within budget.
