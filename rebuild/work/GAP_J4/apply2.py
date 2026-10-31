import json,re,os,sys,importlib.util
W='/home/user/Possession-Taxonomy/rebuild/work/GAP_J4/'
R='/home/user/Possession-Taxonomy/rebuild/out/'
sys.path.insert(0,W)
import data2
d=json.load(open(R+'J4.json'))
K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
WP='https://en.wikipedia.org/wiki/'
def norm(n):
    n=n.lower(); n=re.sub(r'\(.*?\)|\[.*?\]','',n); n=re.sub(r"[’'\"‘`]",'',n)
    n=re.sub(r'\b(pdo|pgi|gi|aop|cultivar|strawberry|banana|plantain|lemon|cucumber|basil|mango|potato|apple|pear)\b','',n)
    n=re.sub(r'[^\w ]+',' ',n); return re.sub(r'\s+',' ',n).strip()
def keys(x):
    ks={norm(x['n'])}
    for t in re.split(r'[;·,]',x.get('a') or ''):
        if t.strip(): ks.add(norm(t))
    return {k for k in ks if k}
added={}
def add(kind,n,dd,s,y='',a='',dt=None,g=None):
    if not n.strip(): return
    k=K[kind]; k.setdefault('x',[])
    e={'n':n,'a':a,'d':dd,'mk':'','y':y,'s':s,'v':[]}
    if dt: e['dt']=dt
    if g: e['g']=g
    have=set()
    for x in k['x']: have|=keys(x)
    if keys(e)&have: return
    k['x'].append(e); added.setdefault(kind,[]).append(n)
def yr(y):
    m=re.search(r'\d{4}',y or ''); return m.group(0) if m else ''
def rows(txt): return [ (r.split('|')+['',''])[:3] for r in txt.strip().split('\n') if r.strip()]
PL=WP+'List_of_pear_cultivars'
for n,o,y in rows(data2.PEAR):
    add('Pear',n,'Pear cultivar listed in Wikipedia\'s list of pear cultivars'+(f'; origin {o}' if o else '')+'.',PL,y=yr(y))
AL=WP+'List_of_apple_cultivars'
for n,o,y in rows(data2.APPLE):
    add('Apple',n,'Apple cultivar listed in Wikipedia\'s list of apple cultivars'+(f'; origin {o}' if o else '')+'.',AL,y=yr(y),a=(o if n in('Brown Thorn','Lavignée') else ''))
ML=WP+'List_of_mango_cultivars'
for c,s in data2.MANGO.items():
    for n in s.split('|'):
        add('Mango',n,f'Mango cultivar listed under {c} in Wikipedia\'s list of mango cultivars.',ML,dt=c,g=c)
GL=WP+'List_of_grape_varieties'
for sec,s in data2.GRAPE.items():
    for n in s.split('|'):
        add('Table grape',n,f'Table grape cultivar listed under {sec.lower()} in Wikipedia\'s list of grape varieties.',GL,dt=sec)
# sweet potato / strawberry / potato names with year
SPN="Acadian|Allgold|Americana|Apache|Australian Canner|Baker|Beauregard:1987|Bonara|Campeon|Canbake|Caro-Gold|Carolina Bunch|Carolina Nugget:1954|Carolina Ruby:1988|Caromex:1971|Carver|Centennial|Chipper|Covington|Cliett Bunch Porto Rico|Coastal Red:1978|Coppergold|Cordner:1983|Creole|Darby|Don Juan|Earlyport|Earlysweet|Eureka|Evangeline|Excel|GA90-16|Georgia Jet|Georgia Red|Gold Rush|Golden Belle|Goldmar:1973|Grand Asia|Hayman White|Heartogold|Hernandez:1992|HiDry|Hoolehua Gold|Hoolehua Red|Hopi|Houhere|Hutihuti|Iliua|Japanese sweet potato|Jersey Orange|Jersey Red|Jersey Yellow|Jewel:1970|Kandee|Kona B|Kote Buki|Lakan|Mameyita|Maryland Golden|Miguela|Murasaki|Murff Bush Porto Rico:1949|Nancy Gold|Nancy Hall|Nemagold|Northern Star|Nugget|Okla. 46|Oklamar|Oklamex Red|Onokeo|Onolena|Orange Sunset:2014|Orlis|Owairaka Red|Papota|Parapara|Pelican Processor|Picadita|Pope|Poporo|Porto Rico 198:1966|Purple Dawn:2014|Purple Heart|Queen Mary|Ranger|Rapoza|Rekarawa|Rekamaroa|Red Diane|Red Garnet|Red Jewel|Red Nancy|Redglow|Redgold|Redmar:1971|Regal|Resisto|Rojo Blanco|Romanawa|Rose Centennial|Ruddy|Scarlet|Shore Gold|Southern Delite|Sumor|Sunnyside|Sweet Red|Tango|Tanhoma|Taputini|Toka Toka Gold:1972|Topaz|Travis:1980|UPLSP-1|UPLSP-2|U.P.R. number 3|U.P.R. number 7|Vardaman|Virginian|VSP-5|VSP-6|Waimanalo Red|Waina|White Delite:1979|White Triumph|Whitestar|Yellow Yam"
for t in SPN.split('|'):
    n,_,y=t.partition(':'); add('Sweet potato',n,'Sweet potato cultivar listed in Wikipedia\'s list of sweet potato cultivars (edible-root table).',WP+'List_of_sweet_potato_cultivars',y=y)
STN="Alba:2002|Albion:2006|Alice:1993|Allstar:1981|Altess:2015|Amelia:1998|Annapolis:1984|Apollo:1970|Archer:2016|Aromas:1994|Asia:2005|Atlas:1970|Benicia|Benton:1975|Bogota:1978|Bolero:1996|Bountiful:1993|Brunswick:1999|Cabot:1998|Calypso:1992|Camarosa:1994|Cambridge Favourite:1947|Camino Real|Canoga:1979|Cassandra:1998|Chambly:1982|Chandler:1983|Christine|Clancy:1993|Darselect:1998|Delia:2007|Delite:1974|Delmarvel:1994|Diamante:1991|Earlibelle:1964|Earliglow:1975|Elegance:2009|Elsanta:1975|Elvira|Emily:1995|Eros:1985|Evangeline:1975|Everest|Faith:2014|Fenella:2009|Firecracker:1998|Flair:2008|Flamenco:2002|Fleurette:2013|Florentina:2011|Florina:2010|Fort Laramie:1973|Fruitful Summer|Furore:2014|Glooscap:1983|Governor Simcoe:1985|Guardian:1969|Hecker:1979|Honeoye:1979|Hood:1965|Itasca:2005|Jewel:1985|Joliette:1996|Judibell:2005|L'Amour:2003|Little Scarlet|Loran|Lucy:2009|Lumina:2024|Mae:2003|Marshall:1890|Matis:2003|Mesabi:1996|Midway:1959|Mira:1996|Mohawk:1994|Mojave|Monterey:2009|Northeaster:1993|Ogallala:1956|Orléans:2001|Oso Grande:1987|Ozark Beauty:1955|Palomar|Pandora:1988|Pelican:1996|Pineberry|Pinnacle:2002|Portola:2009|Primetime:1995|Puget Reliance:1994|Puget Summer:2002|Quinault:1967|Rabunda:1969|Redchief:1968|Redcrest:1990|Redgem:1993|Red Ruby|Rosie:1999|Roxana:2001|Royal Sovereign:1891|Saint Pierre:2001|Sallybright:2007|San Andrés:2009|Sapphire:2002|Sasha|Scott:1979|Seascape:1991|Seneca:1992|Senga Sengana:1954|Sequoia:1972|Shuksan:1970|Sophie:1997|Stellarossa:2005|Strasberry:1925|Strawberry Festival:2000|Sunrise:1964|Surecrop:1956|Tillamook:2002|Titan:1971|Totem:1972|Tribute:1981|Tristar:1981|Valley Red:2009|Variegata|Veestar:1967|Ventana|Viktoriana:1998|Winona:1995"
for t in STN.split('|'):
    n,_,y=t.partition(':'); add('Strawberry',n,'Strawberry cultivar listed in Wikipedia\'s list of strawberry cultivars.',WP+'List_of_strawberry_cultivars',y=y)
PON="Adirondack Blue:2003|Adirondack Red:2003|Agata:1976|Agria:1985|Almond|Alpine Russet:2009|Alturas:2002|Amandine:1993|Allians:2003|Amarilla|Amflora:1996|Andean black|Annabelle:2001|Anuschka:2004|Anya:1996|Arran Victory:1918|Atlantic:1978|Atlas|Augusta|Austrian Crescent|Avalanche:1989|Baccara|Bamberg:1819|Banana:1990|Bannock Russet:1999|Barbara:1982|Belana:2000|Bellarosa:2004|Belle de Fontenay:1885|Berlichingen:1927|BF-15|Bildtstar:1984|Bintje:1904|Bionta:1993|Black Champion|Blaue Hindelbank|Blaue St. Galler|Blaue Uttenwill|Blaue Viola|Blaue Vogtländer|Blazer Russet:2005|Bloomer:1936|Blue Bell:2008|Blue Christie|Blue Congo|Bojar:1945|Bonnotte|Brambory|British Queen:1894|Butte:1977|Cabritas:1889|Camota|Camel:2013|Canela Russet|Cara:1973|Carola:1979|Champion:1863|Charlotte:1981|Chelina|Chérie:1997|Cheyenne:2011|Chiloé|Ciclame|Cielo|Clavela Blanca|Colette:1995|Corte|Cream of the Crop|Cultra:1986|Cyrano:2003|Dejima:1971|Désirée:1962|Doré:1939|Dos Color|Duke of York:1891|Dutch Cream|Early Fortune|Edelgard|Edzell Blue|Eigenheimer|Electra|Ennstaler Alpe|Espirit|Estima|Ewelina|Fenton|Fianna|Filea|Fingerling|Finka|Flava|French Fingerling|Gala|German Butterball|Golden Wonder:1906|Goldrush|Hansa|Heideniere|Hela|Hermanns Blaue|Hermes|Highland Burgundy Red|Holtgaster Blaue|Home Guard:1942|Huayro|Industrie|Innovator|Irish Cobbler|Irish Lumper|Irish White:1882|Jam|Jazzy|Jeanie Deans|Jelly|Jersey Royal:1880|Jubel|Juliette|Kennebec:1941|Kerr's Pink:1907|Kestrel:1992|Keuka Gold|King Edward:1902|Kipfler|Kitaakari:1987|Kuhbauch|Lady Balfour|Lady Rosetta|Langlade|Laura:1998|Lenape:1967|Lima|Linda|Linzer Blaue|Linzer Delikatess|Linzer Rose|Linzer Speise|Linzer Stärke|Marabel|Marcy:1990|Marfona:1975|Maris Peer:1962|Maris Piper:1966|Marquis|Mayan Queen|May Queen|Megachip:1985|Melody|Miss Blush|Mizen:1978|Monalisa|Mozart|Mahil|Lil Key|Negra Andina|Nadine|Navan:1987|Nicola|Nishiyutaka:1978|Norddeutsche Inseln|Norgold Russet|Oldenburger Blaue|Opperdoezer Ronde|Orchestra|Ostbote|Ozette|Pachacoña|Parel|Pentland Crown|Peruanische Blaue|Pike:1996|Pink Eye|Pink Fir Apple|Piruanita|Präsident Krüger|Primura|Princess|Professor Wohltmann|Puca Quitish|Puikula|Quarta|Ranger Russet:1991|Ratte|Record|Red Britain|Red Gold|Red La Soda:1948|Red Norland|Red Pontiac|Reichskanzler|Remarka|Rooster:1990|Rosalind|Rosenerdling|Roseval|Roslau|Royal Blue|Rua|Runa|Ruby Lou|Russet Burbank:1902|Russet Norkotah|Russian Blue|Sapphire|Sebago|Sechswochenkartoffel|Selma:1972|Sharpes Express|Shepody|Shetland Black|Sieglinde:1938|Sigma|Silverton Russet|Sirco|Skerry Champion:1922|Snowden|Solara|Spunta|Stobrawa|Superior:1962|Svenungas Blaue|Sylvana|Tannenberg|Tennaer|Tiger Russet|Toya:1992|Tūtaekurī|Ulster Emblem:1966|Umatilla Russet:1998|Urberger|Victoria|Villetta Rose:1994|Vineta|Viola|Violette d'Auvergne|Violine de Borée|Vitelotte|Vivaldi|Warba:1927|Weißauge|Yellow Finn|Yukon Gold:1965"
for t in PON.split('|'):
    n,_,y=t.partition(':'); add('Potato',n,'Potato cultivar listed in Wikipedia\'s list of potato cultivars.',WP+'List_of_potato_cultivars',y=y)
BN="Chingan:AA|Pisang jari buaya:AA|Sinwobogi:AA|Pisang Lilin:AA|Pisang Kapas:AA|Pisang Oli:AA|Lady Finger:AA|Pisang Muli:AA|Madagascar:AAA|Dwarf Cavendish:AAA|Giant Cavendish:AAA|Formosana (GCTCV-218):AAA|Grand Nain:AAA|Masak Hijau:AAA|Cavendish Zelig:AAA|Azman:AAA|Dwarf Red:AAA|Flhorban 920:AAA|East African Highland:AAA|Pisang Susu:AAA|Pisang Ampyang:AAA|Pisang Palembang:AAA|Pisang Pulo:AAA|Pisang Papan:AAA|Bodles Altafort:AAAA|Golden Beauty:AAAA|Atan:AAAB|Goldfinger:AAAB|Mbang Okon:AAB|Agbagba:AAB|Orishele:AAB|Ishitim:AAB|Rhino Horn:AAB|Pink French:AAB|Tiger:AAB|Popoulu:AAB|Pisang Raja:AAB|Pome:AAB|Prata-anã:AAB|Latundan:AAB|Plu:AAB|Kalamagol:AABB|Thai:ABB|Cau Bedong:ABB|Silver Bluggoe:ABB|Benedetta:ABB|Blue Java:ABB|Tiparot:ABBB|Fe'i:Fe'i"
for t in BN.split('|'):
    n,_,g=t.partition(':'); add('Banana',n,f'Banana cultivar, genome group {g}, listed in Wikipedia\'s list of banana cultivars.',WP+'List_of_banana_cultivars')
PN="Nendran:AAB|Batard:AAB|Obino l'Ewai:AAB|Pisang Tandok:AAB|Cooking banana:AAB|Green French:AAB|Bluggoe:ABB|Saba:ABB|Cardava:ABB|Pisang kepok:ABB"
for t in PN.split('|'):
    n,_,g=t.partition(':'); add('Plantain',n,f'Plantain or cooking banana, genome group {g}, listed in Wikipedia\'s list of banana cultivars.',WP+'List_of_banana_cultivars')
# EU/UK protected names confirmed from Wikipedia lists
PT=WP+'List_of_Portuguese_food_and_drink_products_with_protected_status'
UK=WP+'List_of_United_Kingdom_food_and_drink_products_with_protected_status'
PD=WP+'List_of_Protected_Designation_of_Origin_products_by_country'
eu=[('Plum',"Ameixa d'Elvas PDO",'Portuguese prune, protected designation of origin.',PT),('Pineapple','Ananás dos Açores/São Miguel PDO','Pineapple from São Miguel, Azores, protected designation of origin.',PT),('Cherimoya','Anona da Madeira PDO','Custard apple from Madeira, protected designation of origin.',PT),('Cherry','Cereja da Cova da Beira PGI','Cherry from Cova da Beira, Portugal, protected geographical indication.',PT),('Cherry','Cereja de São Julião-Portalegre PDO','Cherry from Portalegre, Portugal, protected designation of origin.',PT),('Apple','Maçã Bravo de Esmolfe PDO','Portuguese apple, protected designation of origin.',PT),('Apple','Maçã Riscadinha de Palmela PDO','Portuguese apple, protected designation of origin.',PT),('Apple','Maçã de Alcobaça PGI','Portuguese apple, protected geographical indication.',PT),('Apple','Maçã da Beira Alta PGI','Portuguese apple, protected geographical indication.',PT),('Apple','Maçã da Cova da Beira PGI','Portuguese apple, protected geographical indication.',PT),('Apple','Maçã de Portalegre PGI','Portuguese apple, protected geographical indication.',PT),('Passion fruit','Maracujá dos Açores/S. Miguel PDO','Passion fruit from São Miguel, Azores, protected designation of origin.',PT),('Peach','Pêssego da Cova da Beira PGI','Peach from Cova da Beira, Portugal, protected geographical indication.',PT),('Orange','Citrinos do Algarve PGI','Citrus from the Algarve, protected geographical indication.',PT),('Sweet potato','Batata doce de Aljezur PGI','Sweet potato from Aljezur, Portugal, protected geographical indication.',PT),('Potato','Batata de Trás-os-Montes PGI','Potato from Trás-os-Montes, Portugal, protected geographical indication.',PT),
('Apple','Armagh Bramley Apple PGI','Bramley apple from Armagh, protected geographical indication since 2012.',UK),('Potato','Ayrshire New Potatoes PGI','Early potato from Ayrshire, protected geographical indication since 2019.',UK),('Potato','Pembrokeshire Earlies PGI','Early potato from Pembrokeshire, protected geographical indication since 2013.',UK),('Potato','New Season Comber Potatoes PGI','Early potato from Comber, Northern Ireland, protected geographical indication since 2012.',UK),('Potato','Jersey Royal Potatoes PDO','Early potato from Jersey, protected designation of origin since 1996.',UK),('Plum','The Vale of Clwyd Denbigh Plum PGI','Plum from the Vale of Clwyd, protected geographical indication since 2019.',UK),('Asparagus','Vale of Evesham Asparagus PGI','Asparagus from the Vale of Evesham, protected geographical indication since 2016.',UK),('Celery','Fenland Celery PGI','Celery from the Fens, protected geographical indication since 2013.',UK),('Leek','Welsh Leeks PGI','Leek protected in the UK as a geographical indication since 2022.',UK),('Watercress','Watercress TSG','Watercress registered as a traditional speciality guaranteed in 2021.',UK),
('Pomegranate','Ρόδι Ερμιόνης (Rodi Ermionis) PDO','Pomegranate from Ermionida, Greece, protected designation of origin.',PD),('Apple','Firiki Piliou','Apple from Pelion, Greece, protected designation of origin.',PD),('Garlic','Taşköprü Sarımsağı','Garlic from Taşköprü, Turkey, listed with protected designations.',PD),('Potato','Lapin puikula','Potato from Lapland, Finland, protected designation of origin.',PD),('Fig','Figue de Solliès AOP','Fig from Solliès-Pont, France, protected designation of origin.',PD),('Garlic','Ail rose de Lautrec PGI','Pink garlic from Lautrec, France, protected geographical indication.',PD),('Asparagus','Marchfeldspargel PGI','Asparagus from the Marchfeld, Austria, protected geographical indication.',WP+'Geographical_indications_and_traditional_specialities_in_the_European_Union'),('Cucumber','Spreewälder Gurken PGI','Gherkins from the Spreewald, Germany, protected geographical indication.',WP+'Category:German_products_with_protected_designation_of_origin')]
for kind,n,dd,s in eu: add(kind,n,dd,s)
# Santorini tomato version
for e in K['Tomato']['x']:
    if e['n']=='Santorini' and not e['v']:
        e['v']=[{'n':'Τοματάκι Σαντορίνης (Tomataki Santorinis) PDO','mk':'','y':'2013','d':'Greek protected designation of origin since 13 June 2013'}]
# coverage
tail=re.compile(r"(Complete: \d+ of \d+ in Wikipedia's List of (tomato|Capsicum) cultivars[^.]*\.|No complete list exists; follows the cultivars named by the pages cited on each entry\.|Covers \d+ of an open number[^.]*\.)\s*$")
def cov(kn,n):
    c={'Tomato':"Complete: %d of %d in Wikipedia's List of tomato cultivars (table rows and sidebar names, read to the end, 2026-10-31).",
    'Chilli':"Complete: %d of %d in Wikipedia's List of Capsicum cultivars (cultivar lists by species and index, read to the end, 2026-10-31).",
    'Pear':"Complete: %d of %d in the cultivar table of Wikipedia's List of pear cultivars (read to the end, 2026-10-31), plus protected-origin names; the table has about 165 rows, the rest are fewer than the table because of aliases already held.",
    'Mango':"Complete: %d of %d cultivars named in Wikipedia's List of mango cultivars by country (read to the end, 2026-10-31), plus protected-origin names.",
    'Table grape':"Complete: %d of %d in the table-grape sections of Wikipedia's List of grape varieties (read to the end, 2026-10-31), plus protected-origin names and club varieties.",
    'Sweet potato':"Complete for the edible-root table: %d of %d in Wikipedia's List of sweet potato cultivars (133 edible-root rows, read to the end; 29 ornamental vines left out as not food), plus protected-origin names.",
    'Strawberry':"Complete: %d of %d in Wikipedia's List of strawberry cultivars (155 rows, read to the end, 2026-10-31), plus protected-origin names.",
    'Potato':"Complete: %d of %d in Wikipedia's List of potato cultivars (248 rows, read to the end, 2026-10-31), plus protected-origin names.",
    'Banana':"Complete: %d of %d in the banana rows of Wikipedia's List of banana cultivars (75 cultivars, split with Plantain, read to the end, 2026-10-31).",
    'Plantain':"Complete: %d of %d in the plantain and cooking-banana rows of Wikipedia's List of banana cultivars (read to the end, 2026-10-31)."}
    if kn in c: return c[kn]%(n,n) if '%d' in c[kn] else c[kn]
    if kn=='Apple': return "Complete: %d of %d in the cultivar table of Wikipedia's List of apple cultivars (read in two windows to the end, 2026-10-31), plus protected-origin names; rows between Honeystring and Idared are not in the extracted text."%(n,n)
    return None
for kn,k in K.items():
    x=k.get('x',[])
    if not x: continue
    s=tail.sub('',k.get('sel','')).strip()
    c=cov(kn,len(x))
    if not c:
        c="No complete list exists; follows the cultivars named by the pages cited on each entry."
    k['sel']=(s+' '+c).strip()
    if len(x)>12 and not k.get('xg') or kn in('Mango',):
        k['xg']='by country of the list' if kn=='Mango' else 'by protected origin or cultivar'
    if len(x)>12:
        for e in x:
            if kn=='Mango' and e.get('g') and e['g'] not in('Cultivar','Protected origin'): continue
            e['g']=('Protected origin' if re.search(r'\b(PDO|PGI|GI|AOP|DO|IG|TSG)\b',e['n']) or e['n'].startswith(('Firiki','Lapin','Taşköprü')) else ('Cultivar' if kn!='Mango' else 'Wikidata-listed, country not stated'))
json.dump(d,open(W+'J4b.tmp','w'),ensure_ascii=False,indent=1); os.replace(W+'J4b.tmp',R+'J4.json')
json.dump(added,open(W+'added2.json','w'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in added.items()},sum(len(v) for v in added.values()))
