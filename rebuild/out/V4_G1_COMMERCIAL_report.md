# V4_G1_COMMERCIAL report (round 2)

Part file: rebuild/out/G1_parts/COMMERCIAL.json (about 418 KB, 43 kinds, 1,374 entries); validates OK. Replaces the four departments by exact name. About 90 fetches in total.

## Entries before -> after (references)
- Panel van 6 -> 173, Window van 2 -> 17: Wikipedia List of vans, read whole (dated 2013; minivans and MPVs left to Cars). Volkswagen Transporter carries T1 to T7 versions.
- Utility pickup (new kind) 275 entries from 282 rows of List of pickup trucks, read to the end. The CARS part drops its Pickup truck kind.
- Rigid truck 0 -> 237 and Heavy truck (new kind) 288: List of trucks, now read to its end (three windows, characters 0-269,154), split by the page's class column. Rows already under vans or pickups are not repeated. The Actros row was cut at a window edge.
- Minibus 1, Taxi 2, Bus or coach 3. Tractor unit and Special-purpose truck have no entries (Tractor unit points to Heavy truck).
- Caravans and motorhomes 33 -> 168 (Thor, Hymer, Winnebago, Airstream, Swift Leisure, RV manufacturers list, Knaus Tabbert release).
- Off-road 36 -> 109. ATV article now read to its end (nothing after 100,000). Added Yamaha Kodiak, YFZ450R, Wolverine and Viking (atv.com, 2021 model year), Kawasaki Bayou, Brute Force, Prairie, KFX, Lakota and Mojave (List of Kawasaki motorcycles, no years), Suzuki KingQuad, Eiger, QuadSport and LT-R450 (atv.com, Powersports Business 2007).
- Heritage 36 -> 101 (Horse-drawn vehicle article).

## Owners
`own`, `tier`, `cty` and `own_y` now come only from the fetched Wikipedia articles of Ford, Toyota (Daihatsu 2016, Hino to Archion 2026), Stellantis (2021), Isuzu (UD Trucks 2021), Traton (2021), Volvo Group (Renault Trucks, Mack 2000), Daimler Truck (2021), Paccar, Iveco (2022), Tata, Ashok Leyland, Mahindra (KGM 2022), Nissan, Mitsubishi, Hyundai (Kia 1998), Renault (Dacia 1999), Mercedes-Benz, GM, BRP, Honda, Suzuki and Kawasaki. Blank where a page is silent (Yamaha, Subaru, Mazda, Great Wall, Tesla). Hymer 2019 (Thor page) against 2018 (Hymer page) is unresolved. 15 owner brands added to the register; about 150 truck makers used as `mk` are not registered.

## Market facts (`ms`)
EU 2024: vans 1,586,688 (+8.3 %, diesel 84.5 %), trucks 327,896 (-6.3 %), buses 35,579 (+9.2 %). Volvo Trucks 2024: Europe 17.9 %, Brazil 23.7 %, North America 10.5 %. Ford F-Series US 2024: 765,649. Earlier RV, snowmobile, European Ranger and China pickup figures stay. Unsourced: brand shares for vans and rival truck makers (ACEA and fleet.ie pages blocked; Firecrawl out of credits).

## Winnebago Chieftain
Placed in A-class motorhome with year 1969 (Winnebago milestones page); the fetched pages do not state its class (a search excerpt calls it Class A, not fetched). Winnie Wagon 1974, LeSharo 1983 and Rialta 1995 corrected from that page; the Minnie Winnie year conflicts (1973 against 1994) and is noted.

## Still short
Most entries cite their list page. Removed loose models are as in round 1.
