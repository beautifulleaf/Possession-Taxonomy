# CARS_ADD_ASIA report

Output: rebuild/out/G1_parts/cars_add/ASIA.json (loads with python3 -I). 1,003 new model entries, 38 brand_updates, 19 register entries (sourced country only).

Method: Wikipedia MediaWiki API category members with wikibase-shortdesc (class stated by the page), Wikidata SPARQL for marque country (P17) and parent (P749). About 66 fetches. Firecrawl not called.

Entries by kind: SUV 232, Saloon 54, Hatchback 51, MPV 40, City car 21, Luxury saloon 20, Kei car 9, Sports car 6, Utility coupé 3, Coupé 3, Off-roader 2, Estate 1, "Car, body style not stated" 561 (sectioned by marque via `sec`/`mk`).
Class kinds use the page's short description (stored in `d`); mapping to body kind is by its wording (e.g. "compact car" -> Hatchback, "mid-size car" -> Saloon).

Marques with new models (all kinds): Chery, Haval, Changan, FAW, Hongqi, Roewe, Trumpchi, Aion/Hyptec, BAIC, JAC, Baojun, Li Auto, Zeekr, Leapmotor, Xiaomi, Jetour, Proton, Perodua, VinFast, Holden, HSV, Daewoo, Isuzu, Mitsuoka, Genesis, Iran Khodro, Saipa, Daihatsu, Tata, Great Wall/Tank, Maruti Suzuki, Hindustan, Dongfeng (Aeolus, Fengon, Forthing, Voyah, Nammi, M-Hero), Wuling, XPeng, Ora, SsangYong/KGM, Renault Samsung, Naza; plus gaps in Toyota (63), Mazda (47), Honda, Nissan, Mitsubishi, Subaru, Suzuki, Hyundai, Mahindra.

Not reached / limits
- Years: category shortdescs rarely state years, so `y` is blank except a few; the "List of <marque> vehicles" tables were NOT read (budget). This is the main gap.
- Honda, Nissan, Mitsubishi, Subaru, Suzuki, Hyundai, Kia: only members with a shortdesc were seen (about 38/72/82/45/42/42/33 members without one were omitted by the fetch), so their class-less models are missing; Kia had no gaps among the classified ones.
- Not reached: Premier, Dongfeng-owned Venucia, Tank/Wey/Ora beyond listed, SAIC MG China, NIO (category holds brands only: Firefly, Onvo, Hycan), Laraki (category absent), Samsung/Daewoo subcats, Holden Commodore/Caprice subcategories, Lexus (already complete), Geely/BYD/Datsun gaps, Hyundai/Kia/Toyota subcategories (Corolla, Camry, Prius, Land Cruiser).
- Tata Motors, Great Wall, Premier, Perodua etc. have no P17/P749 row: country/owner left blank. No acquisition years (P580 absent): `own_y` omitted.

Pickups/commercial skipped (not entered): Tata Telcoline; Great Wall Cannon, Cannon Alpha, Wingle; Jetour Zongheng F700; JAC T9, Ruiling, Shuailing T6/T8, V7; Holden Colorado, Rodeo; Isuzu D-Max, Faster, Traga, Panther, KB/LB/P'up/Hombre; Chery Himla, Rely R08, Stockman; Dongfeng Z9; KGM Musso EV; Toyota Hilux, Tacoma, Tundra; Nissan Navara, Frontier, Titan, Datsun truck; Honda Ridgeline; Hyundai Santa Cruz; Kia Tasman; Mahindra Scorpio Getaway, Genio; Mitsubishi Triton; Subaru Baja, BRAT; Suzuki Equator; Wuling Zhengtu; Daihatsu Delta. Vans/buses/military also skipped.

Stored values differing from sourced (cty/own):
- Lexus own: "Toyota Motor Corporation" vs "Toyota"
- Daihatsu own: "Toyota Motor Corporation" vs "Toyota"
- Nissan own: "Nissan Motor Company" vs "Renault" (and Renault-Nissan-Mitsubishi Alliance)
- Mitsubishi own: "Mitsubishi Motors" vs "Mitsubishi"
No stored cty differed. Tier follows the coordinator rule (Global group if sourced parent is a global carmaker, else Independent); Honda/Mazda/Toyota have no sourced parent, tier left blank there.
