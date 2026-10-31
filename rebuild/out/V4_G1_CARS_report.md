# V4_G1_CARS report

Part file: rebuild/out/G1_parts/CARS.json (about 0.7 MB). Replaces department Cars. Validates OK (26 kinds, 3,058 entries). Appendix with pickup and removed-model lists: rebuild/out/V4_G1_CARS_pickups.txt.

## Coordinator instruction followed
Kind "Pickup truck" is dropped and recorded as renames {"Pickup truck": "Utility pickup"}. No pickups are held in the part; the 9 former entries and 81 pickups met in the marque lists are in the appendix for COMMERCIAL to check (Honda Ridgeline, Ford Explorer Sport Trac and similar car-based ones included). Kind "Utility coupé" stays as an empty pointer.

## Entries per kind (before to after, total 143 to 3,058)
City car 8 to 183; Hatchback 9 to 390; Saloon 10 to 957; Estate 5 to 51; MPV 5 to 190; SUV 8 to 456; Luxury saloon 8 to 102; Grand tourer 8 to 91; Limousine 2 to 9; Sports car 15 to 146; Coupé 5 to 137; Convertible 3 to 17; Roadster 5 to 54; Hot hatch 6 to 21; Muscle car 7 to 15; Supercar 11 to 38; Hypercar 9 to 25; Track and racing car 4; Off-roader 11 to 91; Kei car 9 to 50; Microcar 5 to 6; Three-wheeled car 6; Kit car 5; Hot rod 3; Coachbuilt 6 to 11.
All former loose models (`m`) are removed: those matching an entry became that entry; 17 unattested ones are listed in the appendix.

## References and method
- Wikidata (SPARQL, automobile model, 7,585 items with an English Wikipedia article): used for VW Group, Toyota, Honda, Mazda and a few defunct marques. It has almost no years and misses many models (no Audi A3/A4/Q5, VW Tiguan, Mitsubishi Lancer).
- Wikipedia per-marque categories through the MediaWiki API (fetched): Nissan, Subaru, Mitsubishi, Suzuki, Ford (with Europe), Chevrolet, Cadillac, Buick, Lincoln, Jeep, BMW, Mercedes-Benz, Tesla, Renault, Peugeot, Citroën, Fiat, Opel, Kia, Volvo, Jaguar, Hyundai, Land Rover, Lotus, Ferrari, Maserati, MG, Rolls-Royce, Alfa Romeo, Dacia, BYD, Geely, Mahindra, Mini.
- Each entry's `s` is its English Wikipedia article; generation titles (Mk, chassis codes, "nth generation") are folded into versions. Every `sel` carries the coverage line "Covers n of about 7,585".

## Market facts (department ms, 15 rows)
Europe 2024 registrations by group (ACEA via best-selling-cars.com): VW Group 26.3 %, Stellantis 15.2 %, Renault 9.9 %, Hyundai 8.2 %, Toyota 7.8 %, BMW 7.1 %, Mercedes-Benz 5.4 %, Tesla 2.5 %, SAIC 1.9 %. Japan 2024 (JADA): Toyota 30.66 %, Suzuki 16.32 %, Honda 15.12 %, Nissan 10.76 %, Daihatsu 8.29 % (shares worked out from the page's registrations). China 2024: Chinese carmakers 65 %.

## Not done or not sourced
- Stopped at 62 category and Wikidata reads of the fetch budget. Not read: Toyota category, Honda category, Tesla beyond 4 models, GMC, Pontiac, Oldsmobile, Plymouth, Ram, Lancia, McLaren, Pagani, Koenigsegg, Morgan, Saab, Triumph, Studebaker, Smart, Lexus, Tata, SAIC (beyond MG), Chery, Great Wall, Changan, Hyundai Genesis, Polestar, Maruti, Skoda/Audi/VW gaps and about 200 other marques (Wikidata lists 1,000+ makers). Peugeot early "Type N" cars omitted.
- Years: only a few entries have `y` (Wikidata gave almost none), so order within a marque is mostly alphabetical. Generation versions are mostly without `d`. No `role` badges added.
- Global, US and India group shares: no fetched page gave figures (focus2move returned 403; the US page had no numbers).
- `cty`, group `own` and tier come from general knowledge, not a fetched page; `own_y` only where I was sure (not page-sourced). Owner of defunct and small marques needs checking.
- Classification into kinds is my judgement from names and Wikidata classes; some are doubtful.
