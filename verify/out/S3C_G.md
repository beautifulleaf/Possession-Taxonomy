# S3C_G source census: domain G (Vehicles & Property)

Table: `verify/out/S3C_G.tsv` (79 rows: G1 53, G2 26). All pages were fetched through the Parallel MCP tools. "Fetch returned a shell" is noted in the table where a list is script-built.

**G1 Vehicles.** Harvest first: NHTSA vPIC GetAllMakes (12,372 makes, all vehicle classes incl. trailers, RVs and custom shops) as the maker spine, then per mode: cars, Carfolio and Ultimate Specs (brand A-Z with defunct tail) plus Wikipedia manufacturer lists; motorcycles, Bikez (550 brands, 40,000 models); bicycles, 99 Spokes (141,738 bikes, 509 brands) and Bike Index (makers); boats, Yachtall (3,574 builders with model ranges) and the USCG MIC list (16,263 builders), class designs from the World Sailing category; aircraft, ICAO Doc 8643 and the FAA Aircraft Reference file, with EASA and Pilotmix for gliders and light types; caravans and RVs, Out & About Live (UK/EU) and RV Trader (US); trailers, KBA type register and NATM; parts, TecDoc, RockAuto and Auto Care ACES (licensed or script-built). Gaps no catalogue covers well:
- Chinese cars and two-wheelers: Dongchedi came back as a login shell and Autohome was not reached; need a Chinese-language retry or Wikipedia's China manufacturer lists.
- Korean cars and Korean/Taiwanese two-wheelers: no catalogue found (Encar, Naver not tried).
- Buses, coaches and heavy trucks: only Wikipedia lists; no model database found. Tractors are out of scope (B/C domain).
- Canoes, rowing boats, dinghies, packrafts and inflatables as model lines: Paddling.com covers kayaks; no open canoe or inflatable database.
- Motorhome/campervan converters on base vans, and teardrops, micro-campers: only the UK buyer's guides; no converter register.
- Prams, strollers, cargo bikes, mobility scooters, e-scooters: only small US-centred lists (Stroller Compass 102 models; escooterwise 10 brands). BabyOne and electricscooterfinder were seen but not fetched.
- Rail: Wikipedia builder lists only; no model database; preserved rolling stock is museum territory.
- Horse-drawn vehicles: builder directory only (CAA), no types or model register. PWC, ATV/UTV and golf cart makers are covered only inside vPIC and boats.com.
- Pre-war and minor car and cycle makes: Ultimate Specs and Grace's Guide (British only) are the nearest; Wikipedia says 1,800 makers existed in the US alone and no list is complete.
- Ready-made data to avoid scraping: vPIC (API/DB), FAA registry (CSV), ICAO Doc 8643 (registration), Auto-Data/Teoalida (paid). Terms of each need checking before bulk use.

**G2 Property & Structures.** Harvest first: Rightmove's 66-value property type list plus the Wikipedia List of house types and List of building types for dwelling kinds and vernacular named forms; the Getty AAT and FISH thesauri to normalise terms; LandSale (100+ land types), LandWatch, REINZ and ALUM for land; Gartenbau.org, Hornbach, Dunster House and Bunnings for garden-building makers and lines; MHI and ManufacturedHomes.com for manufactured-home makers; LIFULL HOME'S for Japanese house makers; Dignity Memorial, PlotListings and Bestattungen.de for burial space. Gaps:
- Park-home and lodge makers (UK): the PHHPA site is no longer a manufacturer directory; no catalogue of makers or models found. The Tiny Home Industry Association domain returned a hijacked page and was dropped; no tiny-home builder register was confirmed.
- Pool-shell makers beyond Viking (River Pools, Leisure, Blue Haven) and their model names: not fetched; no neutral pool-model database.
- Container and modular home builders, log-cabin and sauna makers, Chinese and Japanese garden building makers: only retailer pages or none.
- Houseboat builders and models: only an enthusiast directory (All About Houseboats); the G1/G2 boundary decision (OWNER question 17) decides whether YachtWorld and Yachtall also feed this.
- Individual houses and plots are unique and have no catalogue (by design); architect and developer names are not tracked.
- Cemetery operators and plots as places: not catalogued here (Find a Grave and cemetery registers are individual records).
