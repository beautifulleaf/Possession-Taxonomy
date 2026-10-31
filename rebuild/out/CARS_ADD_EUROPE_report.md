# CARS_ADD_EUROPE report

Output: rebuild/out/G1_parts/cars_add/EUROPE.json (loads under python3 -I). 872 new model entries, 0 duplicates of CARS.json names (checked by normalised name), 20 brand_updates-covered marques already in CARS.json plus about 80 new ones.

Method: Wikidata SPARQL through WebFetch (about 25 fetches), automobile models with manufacturer, English Wikipedia article, inception/publication year, class labels; country and parent from P17/P749. The Wikipedia "List of <marque> vehicles" tables were NOT read: no list page was reached by search and the category API call for Triumph returned nothing, so no budget was spent guessing. Years are therefore mostly blank (only where Wikidata has one); versions `v` are empty.

Kinds: Sports car 73, Three-wheeled car 8, Supercar 9, Grand tourer 8, City car 3, Microcar 3, Off-roader 3, Roadster 2, Luxury saloon 2, Saloon 1, Coupé 1, and "Car, body style not stated" 759 (sectioned by `g`). Wikidata classes such as supermini, family car, compact car, executive car were not mapped to a kind, so those models sit in the not-stated kind.

Marques with entries (count): Austin 43, Lancia 41, Triumph 32, Tatra 31, Lada 27, GAZ 22, Morris 22, TVR 21, Ruf 19, Moskvitch 17, Simca 16, Saab 16, DKW 14, Bristol 14, Wolseley 14, Daimler 13, ZIL 13, Riley 12, Bugatti 11, Alpina 11, Jensen 11, then Sunbeam, Bandini, Standard, Panhard, Vauxhall, De Tomaso, MG, Amilcar, DAF, Hillman, NSU, Delahaye, Spyker, Monteverdi and about 100 smaller marques.

Not reached or thin: Rover (4), Humber, Singer, Hillman (Wikidata models partial); Venturi, Wartburg/Trabant (2-3 each), Borgward (1), Koenigsegg (0 new), Volvo, Škoda, SEAT-group, Peugeot/Citroën/DS/Renault, Alfa Romeo, Ferrari, Fiat, Maserati, Lamborghini, Lotus, Aston Martin etc. were excluded from the new-model queries as already covered, so missing models of covered marques are NOT completed. Lynk & Co, Smart (Germany) and Rimac have few or no models in Wikidata. Pagani/Piaggio unclassed models skipped. Many pre-war models of covered marques lack classes.

Skipped as non-cars or pickups: Dacia Pick-Up, Tarpan Honker (pickup/4x4), GAZelle, GAZ Sobol, GAZ-2332, UAZ-452, Mercedes Sprinter Classic, Barkas B1000, Bedford, AEC, buses, race-only cars (Lancia LC1/LC2/037/Delta S4, Reynard, Zytek, March, Footwork, Brabham, Leyton House, HWA DTM, X-raid Mini), tuner specials (Brabus), transmissions, Jeep/Opel/Ford rows listed under European manufacturers.

Class not stated: all 759 entries in the not-stated kind.

Marque facts (brand_updates, Wikidata P17/P749, fetched 2026-10-31): tier set Global group where the parent is a global carmaker (Stellantis, Volkswagen, Geely, Tata, SAIC, Renault, Audi AG), otherwise Independent. Years only where a start-time qualifier exists (Daimler/Tata 2008, DAF/PACCAR 1996, Vauxhall/Stellantis 2021, Dacia/Renault 1999, Škoda/VW 1991, Lamborghini/Audi AG 1998, Autobianchi/Fiat 1955, Fiat/Alfa/Lancia/Maserati/Abarth/Opel/Stellantis 2021). Unmatched labels (no sourced facts): Triumph, Rover, Austin, Morris owner, Venturi, Tatra, Trabant, Wartburg, Hispano-Suiza, Borgward, Zastava owner, Ferrari parent, Pagani, Rimac owner.

Stored values that differ from sourced: Lamborghini own (stored Volkswagen Group, sourced Audi AG, 1998); Smart own (stored Smart Automobile, sourced Mercedes-Benz Group and Geely, both without end date); Alpine own (stored Renault Group, sourced Renault, wording only). Volvo, MG, Škoda, Fiat, Lancia, Maserati, Dacia, Lada country and owner agree or were country-only. Polestar has two sourced parents (Volvo Cars, Geely): own left blank. Bugatti has historic countries beside France: France kept.
