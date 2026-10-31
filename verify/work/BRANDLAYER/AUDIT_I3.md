# AUDIT I3 Subscriptions, Memberships & Online Services (cold audit, Opus)

- Accuracy: 0 wrong of 25 checked (random.seed(7)); every sampled name shown on its raw source page and claim supported.
- Additions: 649 brands ({'cultural': 637, 'premium': 12}), 2 regions, 4 drops.
- Cross-tags/known-name notes: 11; quality evidence for already-known brands: 5 groups.

## Main additions by area
- Mobile phone plan: 176
- Magazine subscription: 170
- Private members' club: 123
- Transit pass: 42
- Heritage & parks membership: 40
- Newspaper subscription: 20
- Sports, hobby or social club membership: 17
- Email service: 13
- Antivirus and security suite: 11
- Language-learning plan: 10
- Cloud storage plan: 9
- Password manager plan: 4
- Ski resort pass: 3
- Golf or country club membership: 2
- Grocery and veg box: 2
- Rail discount card: 1
- Online backup plan: 1
- Meal kit and menu plan: 1
- Video streaming service: 1
- Home security monitoring: 1
- Producer club: 1
- Retailer delivery membership: 1

## Drops
- Bandcamp: a music store/marketplace (pay per album), not a subscription or streaming plan; category-member only
- Player FM: free podcast player app (entertainment platform, no paid subscription tier stated on source); owner rule: free entertainment platforms are out
- Kaspersky Secure Connection: same product as harvest row "Kaspersky VPN" (renamed); merge as alias, keep the AV-TEST 2021 Approved evidence
- WiMP: defunct predecessor of Tidal (register row "Tidal"); merge as alias of Tidal, not a separate brand

## Regions
- St James's, London (clubland) (Private members' and gentlemen's clubs): "The original clubs were established in the West End of London. The area of St James's is still sometimes called "clubland"."
- Japan (Home-delivered newspaper subscriptions): "Japan remains the only large wealthy country whose biggest dailies still print several million copies."

## Harvest homonym / cross-tag table
See `homonym_table_harvest` in AUDIT_I3.json (operators named by country in the Opensignal and Ookla rows).

## Notes
Accuracy: 25/25 sampled harvest rows shown on their raw source pages and claims supported (0 wrong); existence-only tags on AV-Comparatives 2020 and the Kaspersky-commissioned AV-TEST 2025 test are correct. Scope checks: all 74 rows from the Wikipedia streaming list come from its subscriber-count (paid SVOD) sections, none from FAST/broadcaster sections; music category rows include defunct services (Grooveshark, Rdio, Beats Music, Groove Music, Simfy, Guvera, Primephonic, Baidu Music, TikTok Music) and mostly-free platforms with paid tiers (SoundCloud = register 'SoundCloud Global Limited & Co. KG' alias, Audiomack, Mixcloud, Bilibili in the video list): keep only as paid-tier services. Additions (649): by dept {"Mobile phone plan": 176, "Heritage & parks membership": 40, "Private members' club": 123, "Sports, hobby or social club membership": 17, "Golf or country club membership": 2, "Transit pass": 42, "Rail discount card": 1, "Email service": 13, "Password manager plan": 4, "Cloud storage plan": 9, "Online backup plan": 1, "Meal kit and menu plan": 1, "Grocery and veg box": 2, "Antivirus and security suite": 11, "Magazine subscription": 170, "Newspaper subscription": 20, "Ski resort pass": 3, "Video streaming service": 1, "Home security monitoring": 1, "Producer club": 1, "Retailer delivery membership": 1, "Language-learning plan": 10}; by region {"Europe": 263, "Asia & Oceania": 57, "Americas": 98, "Middle East & Africa": 49, "Oceania": 35, "Asia": 87, "Africa": 4, "Asia and Oceania": 21, "unspecified": 35}. Sources fetched raw: Wikipedia mobile-operator lists for Europe, Asia & Oceania, Americas and telecom companies of Middle East & Africa (one list per region; only rows linked to own articles; group subsidiaries of register companies and EE/Telekom Slovenije/SoftBank/XLSMART/CelcomDigi left as aliases); INTO member directory (heritage trusts, directory = listed unless own article); Wikipedia List of members' clubs in London, Gentlemen's club (Distribution) and List of gentlemen's clubs in India; List of public transport smart cards and Transit pass (Klimaticket, Deutschlandticket, Eurail, Swiss Travel Pass); Comparison of webmail providers, Comparison of file hosting services, List of password managers; Stiftung Warentest report of the Que Choisir/Test-Achats password-manager test (quality for NordPass, LastPass, RoboForm; Sticky Password and Zoho Vault added); AV-TEST Windows home test Aug 2026 (Top product = quality; AhnLab, K7, TotalAV, SpyHunter added; Avast, AVG, Avira, Bitdefender, ESET, F-Secure, Kaspersky, Malwarebytes, McAfee, Defender gain quality evidence: see quality_evidence_for_known); Opensignal Global Awards 2025 (quality upgrades for Movilnet, Digitel, Teletalk, Metfone, Chunghwa, eir and known operators); Wikipedia newspapers and magazines by circulation (long-running rankings: cultural); Oisix/Daichi wo Mamoru Kai/Radish Boya (Japanese trade press); Cadw, Historic Scotland, Historic Houses; Dolomiti Superski, Magic Pass, Paradiski; Secom; The Wine Society; Coupang WOW; language self-study programmes. Retries: AV-TEST has no password-manager test (searched again; only a 2019 advice article) - used Stiftung Warentest/Que Choisir instead; Which? still paywalled (not retried); Business Wire J.D. Power wireless release blocked by Akamai (not used; J.D. Power remains cultural/standing per caveat, no new rows); Oisix has no English/Japanese Wikipedia page reachable by search - used trade press. Not done (budget): Ookla fixed/5G awards, Opensignal per-country reports, Consumer Reports, America the Beautiful pass (register has 'US federal recreation agencies'), audiobook/dating/creator platforms by region (Ximalaya, Bookmate, BookBeat, Pairs, Tantan, Fanbox), retailer memberships beyond Coupang (JD Plus, Meli+, Flipkart Plus), Benesse/BYJU'S, golf clubs beyond those on the club lists, museum city passes (Paris Museum Pass, Museumkaart). Region balance: operator lists give all inhabited regions; clubs and magazines are Anglosphere/Europe-weighted by their sources (REGIONS ARE NOT QUOTAS); Africa additions are mainly operators and two INTO trusts. Register defects found: 'Norton' row conflates Norton motorcycles (G1) with Norton security (I1); 'Three' (H1 cosmetics) carries I3, conflated with the mobile operator; see cross_tag_known. Own-website rows (Historic Houses, Dolomiti Superski, Magic Pass) tier 'listed'; INTO directory rows are 'listed' unless the verifier finds own articles.
