import json,os,re
def load(c): return json.load(open(f'rebuild/out/{c}.json'))
def save(c,d):
    p=f'rebuild/work/DEFER_FOOD/{c}.tmp'; json.dump(d,open(p,'w'),ensure_ascii=False); os.replace(p,f'rebuild/out/{c}.json')
def dept(d,n): return [x for x in d['depts'] if x['n']==n][0]
def kind(d,n): return [k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n']==n][0]
def ms(d,dn,rows):
    dp=dept(d,dn); dp.setdefault('ms',[]).extend(rows)
# J1
d=load('J1'); k=kind(d,'Meat box')
DEL="https://www.deliciousmagazine.co.uk/best-online-meat-delivery-services/"; GWG="https://www.thegoodwebguide.co.uk/best-sites/online-butchers/18547"
new=[("Provenance Village Butcher","Online butcher with long-lasting relationships with farmers.",DEL),
("Parson's Nose","Family-run London butcher with a large online range of free-range meat from farms in England and Scotland; two-star Great Taste Awards turkeys.",DEL),
("Swaledale","Whole-carcass butcher working with family farmers rearing native breeds around the Yorkshire Dales.",DEL),
("Pipers Farm","Devon-based supplier working with small farms in Devon, Dorset, Somerset and Cornwall; whole-carcass butchery.",DEL),
("Wild Meat Company","Suffolk game specialist: wild duck, rabbit, hare and grouse delivered overnight; listed by both guides.",DEL),
("The Ethical Butcher","Online retailer of pasture-fed, regeneratively farmed meat delivered next day.",DEL),
("Haye Farm","East Devon organic, regeneratively farmed meat, run by Harry Boglione and Emily Perry.",DEL),
("Knepp Wild Range Meat","Wild-range meat seller named in the Delicious guide; the page gives no further description in the fetched part.",DEL),
("Huntsham Farm","Farm known for rare Middle White pork and sausages, listed by the Good Web Guide.",GWG),
("Eversfield Organic","Family-run organic box business near Tavistock, Devon, selling meat, fish and vegetables nationwide.",GWG),
("Abel & Cole","London-area organic box company that also delivers ethically sourced organic meat.",GWG),
("The Blackface Meat Company","Dumfries farm selling Scottish Blackface lamb, Galloway beef, wild venison and game birds.",GWG),
("Albert Matthews","Family butcher founded in 1935 in Bury, Lancashire, sourcing from rare and traditional breeds within 100 miles.",GWG)]
have={e['n'].lower() for e in k['x']}
for n,dd,s in new:
    if n.lower() in have: continue
    k['x'].append({"n":n,"a":"","d":dd,"mk":n,"y":"","s":s,"v":[],"g":"Premium online butchers (UK)","cty":"United Kingdom"})
k['sel']=k['sel'].replace("No current ranked list of kosher meat delivery or of premium UK butchers could be fetched: the Delicious magazine page (403) and Good Web Guide (403) were blocked, and searches for kosher meat delivery returned only vendor pages.","Also Complete: the Delicious magazine 'best online meat delivery services' page (2024, read through the first part of its list) and the Good Web Guide online butchers page (read in excerpts) added through Parallel on 2026-10-31. No current ranked list of kosher meat delivery could be fetched; searches returned only vendor pages.")
save('J1',d)
b=json.load(open('rebuild/out/J1_brands.json'))
AU="https://www.agriculture.gov.au/export/controlled-goods/meat/elmer-3/list-islamic-halal-certification"
for n,p in [("A.M.O. Saudita Islamica Certificadora Halal","Weir Views, Victoria"),("Al-Iman Islamic Society","Westmeadows, Victoria"),("Al Sadeq Association","Thomastown, Victoria"),("Australian Halal Development and Accreditation","Archerfield, Queensland"),("Australian Halal Authority and Advisers","Sunnybank Hills, Queensland"),("The Halal Approval","Auburn, New South Wales"),("Halal Australia","Parramatta, New South Wales"),("Halal Certification Authority","Australia (suburb not shown in the fetched part)")]:
    if n in [x['n'] for x in b['b']]: continue
    b['b'].append({"n":n,"c":"Australia","f":"","seg":"Institution & issuer","kf":"halal certifier","d":f"Islamic organisation on the Australian Government list of recognised halal certifiers for red meat export; based at {p}.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":AU})
json.dump(b,open('rebuild/work/DEFER_FOOD/b.tmp','w'),ensure_ascii=False); os.replace('rebuild/work/DEFER_FOOD/b.tmp','rebuild/out/J1_brands.json')
# J2
d=load('J2'); DF="https://www.deliciousmagazine.co.uk/the-best-home-fish-delivery-services/"
rows=[]
for i,(w,note) in enumerate([("Rockfish","Devon seafood group delivering nationwide, buying from Brixham's fleet or MSC-certified fisheries"),("Pipers Farm","also in the list"),("Sole of Discretion","Plymouth, co-owned by a collective of local fishers paid an agreed price"),("Rick Stein's Online Fishmongers","Cornish fish and shellfish, boxes from £40"),("Wright Brothers","Devon and Cornwall landings, boxes £32-90"),("Fish for Thought","whole fish £6-£56"),("ChalkStream Foods","Wormley; fish frozen the day after landing"),("Ish Fish","Grimsby dockside fish, recyclable packaging"),("Pesky","direct-to-customer webshop opened over lockdown"),("The Tinned Fish Market","tinned oily fish from family producers")],1):
    rows.append({"mkt":"UK online fishmongers (delicious. magazine, 10 best, April 2023)","who":w,"share":f"listed {i} of 10","yr":2023,"s":DF,"note":note})
ms(d,'Fresh & frozen fish',rows); save('J2',d)
# J6
d=load('J6'); IT="https://www.indiatea.org/tea_growing_regions"
tea=[("Assam","312,210 ha under tea; 507 million kg","Indian Tea Association page; described as the single largest tea-growing region in the world; no year on the page"),("Darjeeling","17,820 ha; 9.8 million kg (about 1 % of India's tea)","same page; no year"),("Kangra (Himachal Pradesh)","2,063 ha in Mandi and Kangra districts","same page; tea grown since 1949"),("Karnataka","over 5 million kg of tea","same page; coffee is the main crop"),("Munnar (Kannan Devan Hills Produce Co.)","16 estates on about 8,600 ha","same page; company formed April 2005 from Tata plantations")]
ms(d,'Tea',[{"mkt":"Indian tea growing regions","who":w,"share":s,"yr":None,"s":IT,"note":n} for w,s,n in tea]); save('J6',d)
# J7
d=load('J7'); SP="https://spiritedagave.com/tequila-nom-list"
t=open('/tmp/claude-0/-home-user-Possession-Taxonomy/0fa341d7-9ce7-5e1d-8d76-d0d6deeae94e/scratchpad/nom.txt').read()
rows=[(a,b.strip(),c.strip(),int(n)) for a,b,c,n in re.findall(r'\|\[NOM (\d+)\]\([^)]*\) \|([^|]+)\|([^|]*)\|(\d+) \|',t)]
rows.sort(key=lambda r:-r[3])
ms(d,'Agave',[{"mkt":"Tequila brands registered per producer (CRT list of 1 October 2026, as reproduced by Spirited Agave)","who":f"NOM {a} {b.title() if False else b}","share":f"{n} brands","yr":2026,"s":SP,"note":f"{c}; the list holds {len(rows)} NOM producers and {sum(r[3] for r in rows)} brand lines, with some brands registered at several producers"} for a,b,c,n in rows[:6]])
k=kind(d,'Tequila'); k['sel']=k['sel'].replace("The NOM distillery register was not fetched.","The CRT NOM register was read through Spirited Agave's reproduction of the CRT list of 1 October 2026 (203 NOM producers, 2,466 brand lines); its producers are in the market facts, not entries.").replace("the NOM register is JavaScript-only and is logged for Firecrawl.","the individual brand rows (about 2,466 lines) were not added as entries.")
k=kind(d,'French cider'); k['sel']=k['sel'].rstrip()+" The IDAC press kit (2019) names seven Normandy cider-family appellations: AOC Calvados, Calvados Pays d'Auge, Calvados Domfrontais, Pommeau de Normandie and the AOPs Cidre Pays d'Auge, Cidre Cotentin and Poiré Domfront; all are placed in the kinds here or in Calvados."
save('J7',d)
# J8
d=load('J8'); LS="https://www.lsa-conso.fr/le-pain-de-mie-toujours-en-forme,124419"
dp=dept(d,'Bread & bakery'); dp['ms']=[m for m in dp['ms'] if m['mkt']!='French bread']
ms(d,'Bread & bakery',[{"mkt":"French sliced bread (pain de mie)","who":"Harry's","share":"close to 36 %","yr":2011,"s":LS,"note":"volume share; LSA article of 21 September 2011"},{"mkt":"French sliced bread (pain de mie)","who":"Jacquet","share":"about 15 %","yr":2011,"s":LS,"note":"second national brand; same article"}])
ms(d,'Biscuits & crackers',[{"mkt":"UK biscuits (excluding discounters)","who":"Pladis brands","share":"22.2 %","yr":2023,"s":"https://www.thegrocer.co.uk/results/pladis-reports-record-revenues-as-share-gains-boost-trading/692443.article","note":"up from 21.5 %; Pladis UK revenue £984.4m in 2023 (+14.9 %); owner of McVitie's"}])
ms(d,'Sweets & confectionery',[{"mkt":"US sweets","who":"Haribo","share":"2 %","yr":2017,"s":"https://www.lsa-conso.fr/turbulences-dans-le-bonbon,257658","note":"LSA article of 12 April 2017 says Haribo weighs only 2 % there; Haribo is the French leader and France its first market after Germany"}])
ms(d,'Crisps & savoury snacks',[{"mkt":"Saudi Arabian salty snacks","who":"Saudi Snack Foods (PepsiCo, with Tasali)","share":"over 45 %","yr":2001,"s":"https://progressivegrocer.com/pepsico-inc-acquires-tasali-foods-saudi-arabias-leadnig-snack-maker","note":"share of a market of more than US$100 million after PepsiCo bought Tasali Snack Foods from Savola on 23 July 2001"}])
save('J8',d)
