start
wd offset 0 done (wd0.txt, 200 rows; sorted by maker, next offset 200)
wd offset 200 done (wd1.txt, '=' means title=label with underscores; next offset 400; stopped at Honda CM250C)
wd offset 400 done (wd2.txt grouped '## maker' format; stopped at KR Motors; next offset 600)
wd offset 600 done (wd3.txt; stopped at Matchless G50; next offset 800)
wd offset 800 done (wd4.txt; stopped at Triumph TT600; next offset 1000)
wd offset 1000 done (wd5.txt; stopped at Yamaha YZR-M1; next check offset 1180)
wd all done (1194 rows, wd0-wd5, tail added). next: Wikipedia lists by manufacturer
wp_honda.txt written (curated extras from Wikipedia List_of_Honda_motorcycles engine-size table); fetches used ~16. next lists: Yamaha, Suzuki, Kawasaki, HD, BMW, RE, Triumph, Guzzi, others
wp_yamaha.txt done (concepts/prototypes excluded as out of scope: not sold). fetches ~17
wp_suzuki.txt done (concepts excluded). fetches ~18
wp_kawasaki.txt, wp_hd.txt done (hd has years in parens). fetches ~22
wp_re.txt wp_triumph.txt done; BMW list URL returned cars (skip). fetches ~25
wp_guzzi/norton/bsa done. fetches ~28. BMW list needs a different URL. next: Benelli,Bimota,Laverda,AMC,Ariel,Douglas,Greeves,James,Peugeot,Velocette,Vincent, then Hero/Bajaj/TVS/Ducati/KTM/Piaggio/Vespa/Lambretta/Aprilia/Indian brand pages
vincent/velocette/laverda/benelli/bimota done. fetches ~33
AMC/ariel/greeves/james/peugeot/douglas done. fetches ~39. next: BMW (find URL), Ducati, KTM, Hero, Bajaj, TVS, Piaggio, Vespa, Lambretta, Aprilia, Indian, + market
wd6.txt = wikidata series+motorcycle classes (extra ~225 rows). Concerns: out-of-scope items (concept/streamliner) will be dropped. fetches ~49. next: Bajaj, Hero, TVS, KTM cat, Vespa, Lambretta, Indian
wp_india.txt (Bajaj/KTM/Hero/TVS from Wikipedia company pages & KTM cat). fetches ~53. Next: Vespa page + market share pages
marques.txt written (owner/tier table). fetches ~62; no more fetching. next: build.py in work dir producing rebuild/out/G1_parts/MOTO.json
build.py run OK, part file written & validated. remaining: sources.tsv, report
REVISION 2 started: restore type kinds, wikidata owners, finish Honda table, US/world shares. v1 backups in bak2/
type-category files saved (cat_*.txt): Standard,Sport(+Sport touring merged in Touring),Cruiser,Touring,Dual-sport,Trail(offroad cat),Scooter,Moped,Underbone,Trike. fetches this revision ~17. Note Sport touring merged into cat_Touring. TODO: list-section types (Yamaha/Honda/Kawasaki/Suzuki), Honda eng table, wikidata owners, US/world shares, rebuild build2.py
honda_eng.txt (full engine-size table, name|cc) and wp_honda_sec.txt saved; wikidata owner query done (see below). fetches this rev ~19
marques2.txt = owner table from Wikidata P749/P127 (query https://query.wikidata.org/sparql P31 Q23866334 + P176 maker, parents) and fetched pages (Royal Enfield: Eicher per List of motorcycle manufacturers; TVS: TVS Holdings 50.26% per TVS page; Bajaj Group per Bajaj page). shares fetched: HD 10-K US 37.3% 2024; Honda FY24 unit sales from PDF. next: build2.py
build2.py run, part validated; remaining: report rewrite, sources.tsv additions
