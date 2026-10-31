# V4_G1_MOTO report (revision 2)

Part file: rebuild/out/G1_parts/MOTO.json (0.78 MB, validates OK). Replaces "Motorcycles & scooters" and "Motorcycle riding gear". No renames: the type kinds are restored.

## Motorcycles & scooters
- Kinds restored as in the structure pass (Standard, Sport, Cruiser, Touring, Adventure, Café racer, Scrambler, Chopper and bobber, Trike, Sidecar, Motocross, Enduro, Trials, Supermoto, Dual-sport, Trail, Pit bike, Scooter, Moped, Underbone, Mini bike) plus a new shelf "Type not stated" with kind "Motorcycle, type not stated". About 3,560 entries under 110 marques; `g` is the marque everywhere.
- Per kind: Standard 307, Sport 203, Cruiser 98, Touring 85, Dual-sport 145, Trail 125, Scooter 292, Moped 47, type not stated 2,134; smaller kinds 2 to 47.
- Type rests on: the structure pass's own kind for the 102 curated entries; Wikipedia type categories (Standard, Sport bikes, Cruiser, Touring, Sport touring, Dual-sport, Off-road, Motor scooters, Mopeds, Underbone, Tricycle;); list sections that name a type (Yamaha, Kawasaki, Honda, Suzuki, Harley-Davidson). Wikidata's own type classes cover only 10 items. The Off-road category states no finer type, so those go to Trail bike. Coverage lines in each kind's `sel`: categories read in full except the subcategories of Scooters, Mopeds and Dual-sport (not read).
- Honda engine-size table joined in full (378 rows; each with its cc in `d`), plus the Honda vehicle-type sections.
- Owners now come from Wikidata (one query over all maker items: parent organisation P749 or owner P127, start year) or a fetched page (Royal Enfield: Eicher, TVS: TVS Holdings, Bajaj Group). Where neither states an owner the entry says "owner not stated"; defunct marques follow the manufacturers page. `own_y` only where Wikidata gives a year (Aprilia 2004, Gilera 1969, Derbi 2001, Benelli 2005, Husqvarna 2013, Norton 2020, Moto Morini 2018, Malaguti 2018, Paton 2016, Peugeot 2023, Laverda 2004).
- 76 new register brands and about 38 brand_updates carry own, tier, country.
- Not finished: BMW, Ducati, Aprilia, Husqvarna, Indian and Lambretta have no usable Wikipedia list; other lists were read to their ends. Stopped at about 45 fetches of the 50.

## Market facts (ms)
India retail 2024-25: Hero 28.84 %, Honda 25.37 %, TVS 17.49 %, Bajaj 11.41 %, Royal Enfield 4.47 %, Yamaha 3.44 %. Harley-Davidson share of new US registrations of 601cc and over: 37.3 % in 2024, 37.9 % in 2023, 41.2 % in 2022 (Motorcycle Industry Council data, quoted in its FY2024 Form 10-K); Europe 5.0 % (2024). Honda Group units 18,819 thousand in the year to March 2024. Indonesia, Bajaj and Hero shares as before.
Not found: a world brand-share table, Yamaha's share and Honda's US share (Yamaha PDFs unreadable or 404; no Motorcycle Industry Council page surfaced).

## Motorcycle riding gear
Unchanged: 28 entries before, 1 after (Bell Star, origin); 24 loose models and boot ranges removed; helmet makers and standards are tt types.
