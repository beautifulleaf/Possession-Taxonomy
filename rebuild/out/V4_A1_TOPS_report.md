# V4_A1_TOPS report

Part file: rebuild/out/A1_parts/TOPS.json. Replaces Tops; Trousers, jeans & shorts; Dresses; Skirts, jumpsuits & sets. Validates OK: 70 kinds, 265 entries (21 badges: 19 origin, 2 landmark).

## Method
- Read the whole brand register (2,531 brands; 1,306 `sig`/`lines` items) with a script and picked every item whose garment matches one of the 70 kinds. Register `s` pages were not re-fetched; they were fetched in the register pass (sources.tsv) and are used as the source of new register-based entries.
- Fetched 40 Wikipedia pages (log: rebuild/work/V4_A1_TOPS/sources.tsv): T-shirt, Polo shirt, Breton shirt, Jeans, Hoodie, Sweater, Cardigan, Chino cloth, Wrap dress, Little black dress, Slip dress, Pencil skirt, Poodle skirt, Miniskirt, Hot pants, Jumpsuit, Aloha shirt, Aran jumper, Guernsey, Fair Isle, Lopapeysa, Cowichan sweater, Sweatshirt, Leggings, Bodysuit, Cargo pants, Capri pants, Bermuda shorts, Tutu, Culottes, Wedding dress, Western wear, Dress shirt, Shorts, Tank top, Football kit, and the tails of Miniskirt, Jeans, Shorts, Football kit and Western wear (references only). Every originator they name became an entry.
- Each kind has `nl`, `sel` (with "Complete: n of n"), `xg` (brand country, then brand); every entry has `g`, `mk`, `y`, `d`, `s`, `cty`; `own`/`own_y` where the register description states the owner.

## Entries before -> after (named x; loose m removed everywhere)
Tops: T-shirt 5->8; Polo 7->8; Breton 5->5; Tank 2->3; Bodysuit 1->3; Baby bodysuit 1->1; Football shirt 4->7; Rugby 3->3; Basketball 2->2; Ice hockey 2->2; Baseball 2->2; Team jersey 0->1; Dress shirt 3->4; Button-up 5->6; Overshirt 3->3; Western 4->4; Aloha 5->9; Aran 0->4; Guernsey 0->3; Fair Isle 0->3; Lopapeysa 0->4; Norwegian 4->4; Cowichan 1->7; Hoodie 7->14; Sweatshirt 4->7; Sweater 4->4; Cardigan 3->3.
Trousers: Heritage jeans 7->7; Selvedge 12->15; Fashion jeans 3->5; Trousers 3->11; Chinos 2->3; Cargo 2->2; Capri 0->1; Bondage 1->1; Shorts 3->8; Bermuda 1->3; Hot pants 1->2; Joggers 1->3; Leggings 3->6.
Dresses and skirts: Wrap 3->4; Slip 1->3; Sheath 3->7; Shift 6->6; Shirt dress 1->1; Babydoll 2->2; Pinafore 1->4; Fit-and-flare 1->4; Sundress 0->2; Maxi 1->5; Evening 2->4; Wedding 1->2; Pencil 2->1; Poodle 1->1; Miniskirt 3->15; Tutu 0->6; Jumpsuit 0->6; Costume 2->1.
Empty by design (register and Wikipedia name none): Cricket shirt, Blouse, Sweater vest, Harem pants, Plus fours, Denim shorts, A-line, Pleated, Wrap, Tiered skirts, Culottes, Co-ord set.

## Removed
Loose models not in the register's `sig`/`lines` and not named by a fetched article were removed (about 190), e.g. Barbour overshirts, Uniqlo blouses, Lands' End vests, Naked & Famous Weird Guy, 3sixteen SL-100x, ONI 288, Real McCoy's Lot 001, Tellason Ladbroke Grove, Hering Camiseta Brasil, Collectif/Bettie Page minor dresses (the Collectif, Pinup Girl and Hell Bunny dresses became versions), Tripp bondage pants. Brandless forms (Shirtwaist, Hobble skirt, Jorts, Hotpants, Bermuda shorts, Kariyushi, Bridal gown, Prince of Wales Fair Isle) were removed or replaced by the named makers.
Not mine, left for other parts: tracksuits, overalls, kilts, saris, kaftans, dirndl, fleece pullovers, base layers, jackets.

## Market layer
No department `ms`/`msum` was written: no fetched market-share source for these four departments within the budget. `tier` omitted (no fetched basis); `cty` set from the register; `own` only where the register description states it (Bonds, Champion, DAKS, Dale of Norway, Hanes, Hervé Léger, Lacoste, Stubbies, A Bathing Ape, Icebreaker).

## Limits
- New register-based entries use the register `s` page, not re-fetched, and their `d` is the register's fact about the piece.
- `g` for 28 new brands (page-named designers) uses common knowledge where the Wikipedia page gives no country; their register entries leave `c` empty. Sonja de Lennart is "Country not stated".
- Wikipedia names (Kamehameha, Shaheen, Trimingham, etc.) are brands with no register page; 28 new brand entries are in `brands`.
- 40 of about 60 fetches used.
