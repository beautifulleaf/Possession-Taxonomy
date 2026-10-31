# CARS_ADD_AMERICAS report

Output: rebuild/out/G1_parts/cars_add/AMERICAS.json (loads with python3 -I). 80 entries, 25 marques named, 24 brand updates plus register entries. About 50 fetches used. Result is PARTIAL.

## Method and limits
- Wikidata models (P176) carried almost no year or class (Oldsmobile, GMC returned a handful with no values), so it was used only for marque facts (country P17, parent P749).
- Models come from MediaWiki API category members with first-sentence extracts (`generator=categorymembers&prop=extracts`). The API gives extracts for only 20 pages per call, so a model without a stated body style, or beyond the pages read, is not entered. Kind is only the body style or class the extract names. `s` is the model's Wikipedia page; the facts were read from the API extract of that page.
- Firecrawl not used.

## Entries by marque
Oldsmobile 7, Saturn 5, Hummer 3, GMC 3, Edsel 3, Studebaker 8, Packard 1, Hudson 1, Nash 1, Eagle 2, Mercury 9, Pontiac 7, Plymouth 6, Dodge 7 (Caravan carries the five Chrysler minivan generations as versions), Rivian 3, Lucid 2, Fisker 2, Shelby 2, Saleen 3, Gurgel 3, Troller 1, Mastretta 1.

## Not reached
- Geo, Bricklin, Felino: category names returned no pages (need a search for the right category). Tucker, Saleen category found no Tucker. Ram, Imperial, DeSoto, Duesenberg, Cord, Auburn, DeLorean: pages fetched but no extract stated a body style.
- Chrysler, Jeep, Lincoln, Tesla, Cadillac, Buick, Chevrolet, Ford: missing-model comparison not done. Chrysler minivans only as Dodge Caravan versions.
- Pontiac, Dodge, Plymouth, Mercury, Studebaker, Packard: read only to the extract limit; later pages (Dodge past about 80 titles, Packard, Pontiac beyond 60) unread. Argentina: no marque found.

## Class not stated (body style absent; not entered)
Oldsmobile: Series 60, Series 70, 88, 98, Cutlass family, Alero, Omega, Firenza, Toronado (personal luxury car), Starfire, Model/Series pre-1915 cars. Packard: Caribbean (luxury car), Eight, Clipper, Patrician, Twelve and others. Hudson Hornet/Jet/Wasp/Commodore/Greater Eight. Nash Ambassador/Rambler/Statesman/600/Metropolitan. Studebaker Lark, Champion, President, Commander, Hawk. DeSoto Adventurer, Firedome, Fireflite, Airflow and others. Duesenberg Model J/A, Cord 810/812 and L-29, Auburn 12 and Speedster, Imperial (1955-83), Edsel Citation/Corsair/Pacer/Ranger. Pontiac Firebird, GTO, Fiero, Grand Prix, Catalina, Bonneville, Grand Am, Tempest, Sunbird, Sunfire, G6. Plymouth Barracuda (pony car), Fury, Belvedere, GTX, Valiant, Volare, Reliant. Dodge Charger (1966), Coronet, Colt, Dart, Aspen, Challenger (1970), Brisa. Mercury Cougar, Capri, Sable, Grand Marquis, Monterey, Marquis, Montclair, Comet, Tracer. Saturn Ion, S-Series. Shelby Mustang, Shelby Lancer, GLH-S, CSX. Gurgel Itaipu. Mastretta MXT. Rivian/Lucid/Fisker concepts (Fisker Pear, Ronin, Alaska, Hummer HX, Saturn Curve, Mercury Meta One) skipped as not sold.

## Pickups and non-cars met (skipped)
GMC Canyon, GMC Sonoma, Dodge Dakota, A100, B/C/D series, Studebaker Champ, E-series, Transtar, Rivian R1T and EDV, Troller Pantanal, Fisker Alaska, military trucks (Dodge WC54, Studebaker US6, GMC CCKW, M29 Weasel, T7/T27).

## Marque facts (Wikidata, one SPARQL call)
Sourced: Oldsmobile and Saturn parent General Motors; Buick, Cadillac, Chevrolet parent General Motors; Auburn parent Cord Automobile; Nash parent Nash-Kelvinator Corporation; Troller parent Ford do Brasil, country Brazil; Dodge and Jeep parent "Stellantis North America" (Wikidata, no dates; Stellantis North America's own parents: Fiat S.p.A. 2009, Fiat Chrysler Automobiles 2014, Stellantis 2021). Gurgel Brazil. No acquisition years are given on the marque items, so `own_y` is blank everywhere.
Differences from CARS.json: Dodge and Jeep own stored "Stellantis", Wikidata says "Stellantis North America"; Ram cty stored United States, Wikidata gives United States and Canada (also GMC); Felino is Italy in Wikidata, not Canada as the batch list implied; Pontiac, Mastretta, Bricklin, Packard have no country in Wikidata (stored Pontiac United States unsourced); Ford, Tesla, Lincoln, Chrysler, Ram, Pontiac, Plymouth have no P749 in the query result, so stored owners are unsourced. Tier was not set (not sourced).
