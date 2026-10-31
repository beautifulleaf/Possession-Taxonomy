# CARS_ADD_ASIA report (round 2)

File: rebuild/out/G1_parts/cars_add/ASIA.json (loads with python3 -I). 1,206 new entries (round 1: 1,003), 38 brand_updates, 19 register entries, plus `y_updates` (586 "marque|model" -> first year for models already in CARS.json whose `y` is blank; the coordinator can apply them).

Round 2 sources (WebFetch, about 30 fetches): "List of Toyota vehicles" (windows 0-200000), Honda automobiles, Nissan, Mitsubishi Motors, Subaru, Suzuki automobiles, Mazda, Hyundai, Kia, Daihatsu, Isuzu, Holden, Proton vehicles; Tata and Mahindra have no list page (404), so the "Tata Motors Passenger Vehicles" and "Mahindra & Mahindra" pages' model tables were used. Firecrawl not called.

Kinds: SUV 271, Saloon 64, Hatchback 57, MPV 49, City car 24, Luxury saloon 21, Kei car 20, Sports car 10, Coupé 6, Estate 6, Utility coupé 5, Off-roader 2, Microcar 1, "Car, body style not stated" 670 (sectioned by marque). New models in round 2: Toyota 43, Datsun 20, Mazda 23 (incl. Autozam, Eunos, Efini), Honda 18, Tata 15, Hyundai 12, Isuzu 11, Mitsubishi 10, Suzuki 9, Daihatsu 7, Mahindra 7, Proton 7, Nissan 6, Kia 6, Holden 5, Subaru 4.

Years: the lists give first years; 418 entries now carry `y` (all round-2 entries and 216 earlier ones). Class kinds follow the list's class text only; rows with no class (most "Former" tables) went to the not-stated kind.

Owner: Nissan, Mitsubishi and Hindustan owner/tier updates removed (country kept). Remaining owners come from Wikidata P749 (Lexus, Daihatsu: Toyota; Genesis: Hyundai Motor Company; Kia, Hyundai: Hyundai Motor Group; Maruti Suzuki: Suzuki; Holden: General Motors; others in file). Not checked against infoboxes: Lexus/Daihatsu/Holden/Genesis parents look current, but Holden (GM, brand closed 2020) is a former parent; treat as a candidate to drop. No acquisition years sourced (`own_y` omitted).

Stored vs sourced differences: Lexus and Daihatsu `own` ("Toyota Motor Corporation" vs "Toyota"); no `cty` differences.

Not done
- Chinese, Malaysian and other marques still have blank `y` (no list pages read; budget used on item 1). Honda page second window and Toyota offset 200000 were nav/concept sections and skipped. Nissan list rows for Nissan race cars (R38x etc.) and concepts, Proton concept cars, Mazda concept cars were excluded.
- Item 2 (subcategories) skipped: every named marque had a list page except Tata/Mahindra, which were covered by their company pages.
- Pickups/vans/trucks excluded as before (lists already separate them).
