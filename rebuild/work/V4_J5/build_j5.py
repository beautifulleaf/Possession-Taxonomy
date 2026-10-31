import json,re,sys,os,unicodedata
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J5')
from data_pasta_rice import *
R='/home/user/Possession-Taxonomy/rebuild/'
j=json.load(open(R+'work/V4_J5/bak/J5.json'))
brands=json.load(open(R+'work/V4_J5/bak/J5_brands.json'))
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
K={}
for dp in j['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=(dp,s,k)
def kn(n): return K[n][2]
def allnames(k):
    out=set()
    for e in k.get('x',[]):
        out.add(norm(e['n']))
        for a in (e.get('a') or '').split('·'):
            if a.strip(): out.add(norm(a))
    return out
S=dict(KH="https://en.wikipedia.org/wiki/Kraft_Heinz",CON="https://en.wikipedia.org/wiki/Conagra_Brands",MCC="https://en.wikipedia.org/wiki/McCormick_%26_Company",AJI="https://en.wikipedia.org/wiki/Ajinomoto",KIK="https://en.wikipedia.org/wiki/Kikkoman",UNI="https://en.wikipedia.org/wiki/List_of_Unilever_brands",NES="https://en.wikipedia.org/wiki/List_of_Nestl%C3%A9_brands",BAR="https://en.wikipedia.org/wiki/Barilla_Group",INN="https://en.wikipedia.org/wiki/List_of_instant_noodle_brands",MIZ="https://en.wikipedia.org/wiki/Mizkan",LKK="https://en.wikipedia.org/wiki/Lee_Kum_Kee",KEW="https://en.wikipedia.org/wiki/Kewpie_Corporation",PDO="https://en.wikipedia.org/wiki/List_of_Protected_Designation_of_Origin_products_by_country")
stats={}
def addx(kind,e):
    k=kn(kind)
    if norm(e['n']) in allnames(k): return False
    e.setdefault('a',''); e.setdefault('mk',''); e.setdefault('y',''); e.setdefault('v',[]); e.setdefault('dt','')
    k.setdefault('x',[]).append(e); stats[kind]=stats.get(kind,0)+1; return True
def newkind(shelf,name,d,s):
    for dp in j['depts']:
        for sh in dp['s']:
            if sh['n']==shelf:
                k={"n":name,"a":"","d":d,"s":s,"x":[]}
                sh['k'].append(k); K[name]=(dp,sh,k); return k
PK={"long":"Long-strand pasta","egg":"Egg pasta, ribbons and nests","tube":"Tube pasta","short":"Short and twisted pasta","sheet":"Sheet pasta","filled":"Filled pasta","soup":"Soup pasta","gnocchi":"Potato gnocchi"}
cnt=0; seen_pasta=0
for sec,rows in PASTA.items():
    for line in rows.split('\n'):
        name,reg,desc=line.split('|'); cnt+=1
        if sec.startswith('Long'): kk='sheet' if name in SHEET else 'tube' if name in TUBE else 'egg' if name in EGGRIB else 'long'
        elif sec.startswith('Short'): kk='tube' if name in TUBE else 'egg' if name in EGGRIB else 'short'
        elif sec.startswith('Stretched'): kk='short'
        elif sec.startswith('Soup'): kk='soup'
        elif sec.startswith('Stuffed'): kk='filled'
        else: kk='gnocchi'
        alias=ALIAS.get(norm(name))
        hit=None
        for kx in PK.values():
            for e in kn(kx).get('x',[]):
                if norm(e['n'])==norm(name) or (alias and norm(e['n'])==norm(alias)) or norm(name) in [norm(a) for a in (e.get('a') or '').split('·') if a.strip()]: hit=e
        if hit:
            hit['g']=sec; seen_pasta+=1; continue
        e={"n":name,"d":desc+("." if not desc.endswith('.') else ''),"s":PASTA_URL,"g":sec}
        if reg: e['dt']='region: '+reg
        addx(PK[kk],e)
PASTA_N=cnt
for kx in PK.values():
    for e in kn(kx).get('x',[]):
        if e['n']=='Mandala': e['mk']='Panzani'
rice_cnt=0; rice_new=0
rice_kinds=[x for x in K if K[x][1]['n']=='Rice']
for cty,groups in RICE.items():
    for kind,desc,names in groups:
        for nme in names:
            rice_cnt+=1
            nn=nme.replace(' (Portugal)','')
            found=False
            for kx in rice_kinds:
                for e in kn(kx).get('x',[]):
                    a=[norm(z) for z in (e.get('a') or '').split('·') if z.strip()]
                    if norm(e['n'])==norm(nn) or norm(nn) in a or norm(e['n']).startswith(norm(nn)+' ') or norm(nn).startswith(norm(e['n'])+' '):
                        found=True; e.setdefault('g',cty)
            if found: continue
            if addx(kind,{"n":nme.replace(' (Portugal)',' (Portuguese rice)'),"d":desc,"s":RICE_URL,"g":cty}): rice_new+=1
spice_n=0
for reg,(kind,rows) in SPICE.items():
    if kind not in K: newkind("Spice blends",kind,"Blends named in the Wikipedia list of spice mixes for the region.",SPICE_URL)
    for n,d in rows:
        spice_n+=1; addx(kind,{"n":n,"d":d,"s":SPICE_URL,"g":reg})
for e in kn("Barbecue rubs and seasonings")['x']: e.setdefault('g',"North and Central America")
def pdo(kind,n,a,d,y): addx(kind,{"n":n,"a":a,"d":d,"y":y,"s":S['PDO']})
pdo("Olive oil","Aprutino Pescarese DOP","Aprutino Pescarese","Abruzzo olive oil protected by a PDO.","PDO")
pdo("Olive oil","Bruzio DOP","Bruzio","Calabrian olive oil protected by a PDO.","PDO")
pdo("Olive oil","Terre Tarentine DOP","Terre Tarentine","Extra virgin olive oil from the Taranto area of Apulia, protected by a PDO.","PDO")
pdo("Split pulses and dals","Latvijas lielie pelēkie zirņi PDO","Latvian large grey peas","Large dried grey peas from Latvia, protected by a PDO.","PDO")
pdo("Paprika","Paprika Žitava PDO","Žitavská paprika","Red paprika from Slovakia protected by a PDO.","PDO")
def E(kind,n,d,mk,y,own,tier,cty,oy,src,a='',v=None,g=None):
    e={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":S[src],"v":v or [],"dt":""}
    if own: e['own']=own
    if tier: e['tier']=tier
    if cty: e['cty']=cty
    if oy: e['own_y']=oy
    e['g']=g or own or cty or 'Owner not stated'
    if not addx(kind,e):
        for x in kn(kind)['x']:
            if norm(x['n'])==norm(n):
                for f in('own','tier','cty','own_y'):
                    if f in e: x[f]=e[f]
    return e
G="Global group"; NC="National champion"; IND="Independent"
KH="Kraft Heinz"; UN="Unilever"; NE="Nestlé"; CO="Conagra Brands"; MC="McCormick"; AJ="Ajinomoto"; MZ="Mizkan"
E("Ketchup","Heinz Tomato Ketchup","Heinz tomato ketchup, listed among Kraft Heinz condiments.","Kraft Heinz","",KH,G,"",None,"KH")
E("Ketchup","Kissan","Ketchup, squash and jam brand sold in India.","Kissan","",UN,G,"India",None,"UNI")
E("Ketchup","Tortex","Unilever ketchup brand sold in Poland.","Tortex","",UN,G,"Poland",None,"UNI")
E("Ketchup","Fruco","Unilever ketchup, mayonnaise and condiment brand sold in Colombia.","Fruco","",UN,G,"Colombia",None,"UNI")
E("Ketchup","Globus","Unilever mayonnaise, mustard and ketchup brand sold in Hungary.","Globus","",UN,G,"Hungary",None,"UNI")
E("Mayonnaise","Hellmann's Real Mayonnaise","Hellmann's mayonnaise, listed among Unilever sauces.","Hellmann's","",UN,G,"",None,"UNI")
E("Mayonnaise","Kraft Mayo","Kraft mayonnaise, listed among Kraft Heinz condiments.","Kraft Mayo","",KH,G,"",None,"KH")
E("Mayonnaise","Kewpie Mayonnaise","Japanese mayonnaise made since 1925 and described as the best-selling brand in Japan.","Kewpie","1925","Kewpie Corporation",NC,"Japan",None,"KEW")
E("Mayonnaise","Amora","Unilever mayonnaise and mustard brand sold in France, Belgium and Morocco.","Amora","",UN,G,"France",None,"UNI")
E("Mayonnaise","Thomy","Nestlé brand of mayonnaise and sauces.","Thomy","",NE,G,"",None,"NES")
E("Mustard","Maille Dijon Mustard","Maille mustard, listed among Unilever brands.","Maille","",UN,G,"France",None,"UNI")
E("Mustard","Grey Poupon","Mustard brand listed among Kraft Heinz condiments.","Grey Poupon","",KH,G,"",None,"KH")
E("Mustard","Gulden's","Mustard brand owned by Conagra Brands.","Gulden's","",CO,G,"",None,"CON")
E("Mustard","French's Mustard","Mustard brand that McCormick took over with Reckitt Benckiser's food division in 2017.","French's","",MC,G,"","2017","MCC")
E("Mustard","Slotts","Unilever mustard brand sold in Sweden.","Slotts","",UN,G,"Sweden",None,"UNI")
E("Mustard","Turun sinappi","Unilever mustard brand sold in Finland and Sweden.","Turun sinappi","",UN,G,"Finland",None,"UNI")
for x in kn("Mustard")['x']:
    if x['n']=='English mustard': x.update({"own":UN,"tier":G,"cty":"United Kingdom"})
E("Brown sauce","HP Sauce","HP Sauce, listed among Kraft Heinz sauces.","HP Foods","",KH,G,"",None,"KH")
E("Brown sauce","Daddies Sauce","Brown sauce listed with HP Sauce among Kraft Heinz sauces.","Daddies","",KH,G,"",None,"KH")
E("Worcestershire sauce","Lea & Perrins Worcestershire Sauce","Lea & Perrins sauce, listed among Kraft Heinz sauces.","Lea & Perrins","",KH,G,"",None,"KH")
E("Worcestershire sauce","French's Worcestershire Sauce","French's sauce, part of the food division McCormick took over in 2017.","French's","",MC,G,"","2017","MCC")
E("Barbecue sauce","Bull's-Eye","Barbecue sauce from the European sauce business Kraft Heinz bought from Mondelez in 2017.","Bull's-Eye","",KH,G,"Germany","2017","KH")
E("Barbecue sauce","Stubb's","Barbecue sauce bought by McCormick in June 2015.","Stubb's","",MC,G,"","2015","MCC")
E("Barbecue sauce","Cattlemen's","Barbecue sauce brand owned by McCormick.","Cattlemen's","",MC,G,"",None,"MCC")
for x in kn("Hot sauce")['x']:
    if x['n']=="Frank's RedHot": x.update({"own":MC,"tier":G,"cty":"United States","own_y":"2017"})
    if x['n']=="Cholula": x.update({"own":MC,"tier":G,"cty":"Mexico","own_y":"2020"})
    if x['n']=="Tabasco": x.update({"own":"McIlhenny Company","tier":IND,"cty":"United States"})
    if x['n']=="Crystal Hot Sauce": x.update({"own":"Baumer Foods","tier":IND,"cty":"United States"})
E("Soy sauce","Kikkoman","Japanese soy sauce brand name adopted in 1940; the company was the world's largest soy sauce producer as of 2002.","Kikkoman","1940","Kikkoman Corporation",NC,"Japan",None,"KIK")
E("Soy sauce","Amoy","Soy sauce brand listed among Kraft Heinz sauces.","Amoy","",KH,G,"",None,"KH")
E("Kecap manis","Kecap Bango","Sweet soy sauce brand sold in Indonesia.","Bango","",UN,G,"Indonesia",None,"UNI")
E("Oyster sauce and hoisin sauce","Lee Kum Kee","Hong Kong maker of oyster, hoisin and other Chinese sauces since 1888, still a family business.","Lee Kum Kee","1888","Lee Kum Kee",IND,"Hong Kong",None,"LKK")
E("Oyster sauce and hoisin sauce","Kikkoman Hoisin Sauce","Hoisin sauce sold under the Kikkoman name.","Kikkoman","","Kikkoman Corporation",NC,"Japan",None,"KIK")
E("Stock cubes and bouillon","Knorr","Unilever brand of sauces, stock cubes, ready soups and frozen food sold in many markets.","Knorr","",UN,G,"",None,"UNI")
E("Stock cubes and bouillon","Maggi","Nestlé brand of seasonings and culinary aids.","Maggi","",NE,G,"",None,"NES")
E("Stock cubes and bouillon","Royco","Unilever stock-cube brand sold in Indonesia and Kenya.","Royco","",UN,G,"",None,"UNI")
E("Stock cubes and bouillon","Winiary","Nestlé seasoning and prepared-food brand sold in Poland.","Winiary","",NE,G,"Poland",None,"NES")
E("Liquid seasonings","Maggi Seasoning","Maggi liquid seasoning from Nestlé's seasonings range.","Maggi","",NE,G,"",None,"NES")
E("Liquid seasonings","Aromat","Unilever seasoning sold in South Africa, Sweden, Switzerland and the Netherlands.","Knorr","",UN,G,"",None,"UNI")
E("Tomato pasta sauces","Ragú","US pasta sauce that Mizkan bought from Unilever in May 2014.","Ragú","",MZ,G,"United States","2014","MIZ")
E("Tomato pasta sauces","Bertolli Pasta Sauce","Pasta sauce that Mizkan bought from Unilever in May 2014.","Bertolli","",MZ,G,"","2014","MIZ")
E("Jarred cooking sauces","Cook Do","Ajinomoto cooking-sauce range launched in Japan in 1978.","Cook Do","1978",AJ,G,"Japan",None,"AJI")
E("Jarred cooking sauces","Manwich","Sauce brand owned by Conagra Brands.","Manwich","",CO,G,"",None,"CON")
E("Jarred cooking sauces","La Choy","Asian sauce and canned-food brand owned by Conagra Brands.","La Choy","",CO,G,"",None,"CON")
E("Dashi and dashi ingredients","Hon-Dashi","Ajinomoto dashi seasoning launched in Japan in 1970.","Hon-Dashi","1970",AJ,G,"Japan",None,"AJI")
E("Cornflour and starches","Maizena","Cornstarch brand listed among Unilever brands.","Maizena","",UN,G,"",None,"UNI")
E("Tinned beans and pulses","Heinz Baked Beans","Baked beans listed among Kraft Heinz pantry brands.","Heinz","",KH,G,"",None,"KH")
E("Tinned beans and pulses","Van Camp's","Canned beans and soup brand owned by Conagra Brands.","Van Camp's","",CO,G,"",None,"CON")
E("Tinned tomatoes","Hunt's","Tomato products brand owned by Conagra Brands.","Hunt's","",CO,G,"",None,"CON")
E("Tinned tomatoes","Ro-Tel","Tomato products brand owned by Conagra Brands.","Ro-Tel","",CO,G,"",None,"CON")
E("Frozen ready meals","Stouffer's","Nestlé frozen meals brand.","Stouffer's","",NE,G,"",None,"NES")
E("Frozen ready meals","Lean Cuisine","Nestlé frozen meals brand.","Lean Cuisine","",NE,G,"",None,"NES")
E("Frozen ready meals","Healthy Choice","Conagra frozen dinner brand.","Healthy Choice","",CO,G,"",None,"CON")
E("Frozen ready meals","Marie Callender's","Frozen products brand that Conagra acquired in 1994.","Marie Callender's","",CO,G,"","1994","CON")
E("Frozen ready meals","Smart Ones","Frozen meals brand listed among Kraft Heinz prepared foods.","Smart Ones","",KH,G,"",None,"KH")
E("Frozen ready meals","Bertolli frozen meals","Frozen meals brand that Conagra took over from Unilever in 2012.","Bertolli","",CO,G,"","2012","CON")
E("Frozen pizza","DiGiorno","Nestlé frozen pizza brand sold in the US.","DiGiorno","",NE,G,"United States",None,"NES")
E("Frozen pizza","Tombstone","Nestlé frozen pizza brand.","Tombstone","",NE,G,"",None,"NES")
E("Frozen pizza","Delissio","Nestlé frozen pizza brand sold in Canada.","Delissio","",NE,G,"Canada",None,"NES")
E("Frozen pizza","California Pizza Kitchen","Nestlé frozen pizza brand sold in the US.","California Pizza Kitchen","",NE,G,"United States",None,"NES")
E("Frozen pizza","Wagner","Nestlé frozen pizza brand sold in the European Union.","Wagner","",NE,G,"",None,"NES")
E("Stuffed sandwiches and turnovers","Hot Pockets","Nestlé frozen stuffed-sandwich brand sold in the US.","Hot Pockets","",NE,G,"United States",None,"NES")
E("Stuffed sandwiches and turnovers","Lean Pockets","Nestlé frozen stuffed-sandwich brand.","Lean Pockets","",NE,G,"",None,"NES")
E("Pizza rolls","Bagel Bites","Frozen snack listed under Ore-Ida among Kraft Heinz prepared foods.","Ore-Ida","",KH,G,"",None,"KH")
E("Frozen dumplings","Ajinomoto frozen gyoza","Frozen gyoza sold by Ajinomoto in the US, Europe, Brazil and much of Asia and Oceania.","Ajinomoto","",AJ,G,"Japan",None,"AJI")
E("Yeast extract spread","Bovril","Beef extract spread listed among Unilever brands.","Bovril","",UN,G,"",None,"UNI")
for x in kn("Yeast extract spread")['x']:
    if x['n']=='Marmite': x.update({"own":UN,"tier":G})
E("Peanut butter","Kraft Peanut Butter","Peanut butter listed among Kraft Heinz spreads.","Kraft Peanut Butter","",KH,G,"Canada",None,"KH")
E("Margarine","Parkay","Margarine that Conagra acquired from RJR Nabisco in 1998.","Parkay","",CO,G,"","1998","CON")
E("Margarine","Blue Bonnet","Margarine that Conagra acquired from RJR Nabisco in 1998.","Blue Bonnet","",CO,G,"","1998","CON")
E("Margarine","Flora Original","Margarine brand from the Unilever spreads business spun off in 2018 and now Flora Food Group.","Flora","","Flora Food Group",G,"","2018","UNI")
E("Chutneys and relishes","Branston Original Pickle","Pickle that Mizkan bought from Premier Foods in late 2012.","Branston","",MZ,G,"","2012","MIZ")
E("Malt and distilled vinegar","Sarson's Vinegar","Vinegar brand that Mizkan bought from Premier Foods in July 2012.","Sarson's","",MZ,G,"","2012","MIZ")
E("Honey","Billy Bee Honey","Canadian honey brand that McCormick acquired in 2008.","Billy Bee","",MC,G,"Canada","2008","MCC")
inn=kn("Instant noodles")['x']
UP={"Chikin Ramen":("Nissin Foods",IND,"Japan"),"Cup Noodles":("Nissin Foods",NC,"Japan"),"Shin Ramyun":("Nongshim",NC,"South Korea"),"Indomie Mi Goreng":("Indofood",NC,"Indonesia"),"MAMA":("Thai President Foods",NC,"Thailand"),"Maggi":(NE,G,""),"Buldak Bokkeum Myun":("Samyang Foods",IND,"South Korea")}
for x in inn:
    if x['n'] in UP:
        o,t,c=UP[x['n']]; x['own']=o; x['tier']=t
        if c: x['cty']=c
        x['g']=c or o
E("Instant noodles","Lucky Me!","Philippine instant noodles from Monde Nissin, launched in 1989 and named the most popular in the Philippines in 2020.","Lucky Me!","1989","Monde Nissin",NC,"Philippines",None,"INN")
E("Instant noodles","Wai Wai","Instant noodles first made in Thailand in 1972 and in Nepal in 1984.","Wai Wai","1972","Thai Preserved Food Factory",NC,"Thailand",None,"INN")
E("Instant noodles","Maruchan","Toyo Suisan instant noodles sold in Japan and the United States.","Maruchan","","Toyo Suisan",IND,"Japan",None,"INN")
E("Instant noodles","Sapporo Ichiban","Sanyo Foods instant noodles sold in Japan.","Sapporo Ichiban","","Sanyo Foods",IND,"Japan",None,"INN")
E("Instant noodles","Pot Noodle","Unilever instant cup noodles from the United Kingdom, launched in 1977.","Pot Noodle","1977",UN,G,"United Kingdom",None,"INN")
E("Instant noodles","Super Noodles","Premier Foods instant noodles from the United Kingdom, launched in 1979.","Super Noodles","1979","Premier Foods",IND,"United Kingdom",None,"INN")
E("Instant noodles","Kang Shi Fu","Instant noodles made by Master Kong in China.","Kang Shi Fu","","Master Kong",IND,"China",None,"INN")
E("Instant noodles","Mie Sedaap","Indonesian instant noodles from Wings Food, launched in 2003.","Mie Sedaap","2003","Wings Food",IND,"Indonesia",None,"INN")
E("Instant noodles","Rollton","Russian instant noodles from Mareven Food Central, which was founded in 1999.","Rollton","","Mareven Food Central",IND,"Russia",None,"INN")
E("Instant noodles","Rara Noodle","Nepali instant noodles from Gandaki Noodles, made since the early 1980s.","Rara","","Gandaki Noodles",IND,"Nepal",None,"INN")
E("Instant noodles","Vifon","Instant noodles from Vietnam Food Industries JSC, with a large share of the Polish instant soup market.","Vifon","","Vietnam Food Industries JSC",IND,"Vietnam",None,"INN")
E("Instant noodles","YumYum","Ajinomoto instant noodles with 20 to 21 per cent of the Thai market in 2019.","YumYum","",AJ,G,"Thailand",None,"AJI")
E("Instant noodles","Demae Iccho","Nissin ramen launched in Japan in 1969 and Hong Kong in 1970.","Demae Iccho","1969","Nissin Foods",IND,"Japan",None,"INN")
newkind("Pasta","Pasta brands","Packaged dried pasta sold under a maker's brand name rather than as a shape.",S['BAR'])
E("Pasta brands","Barilla","Parma pasta maker founded in 1877 and the world's leading pasta maker, with 24.5 per cent of the Italian market.","Barilla","1877","Barilla Group",NC,"Italy",None,"BAR")
E("Pasta brands","Misko","Greek pasta brand that Barilla acquired in 1991.","Misko","","Barilla Group",G,"Greece","1991","BAR")
E("Pasta brands","Filiz Makarna","Turkish pasta brand that Barilla acquired in 1994.","Filiz Makarna","","Barilla Group",G,"Turkey","1994","BAR")
E("Pasta brands","Catelli","Canadian pasta brand that Barilla acquired in early 2021.","Catelli","","Barilla Group",G,"Canada","2021","BAR")
E("Pasta brands","Voiello","Pasta brand listed among Barilla brands.","Voiello","","Barilla Group",G,"Italy",None,"BAR")
newkind("Spice blends","Spice and seasoning brands","Spice and seasoning lines sold under a company's brand name, with owner and year of acquisition.",S['MCC'])
sp=[("Schwartz","Spice brand McCormick bought in 1984.","United Kingdom","1984",MC,"MCC"),("Ducros","French spice brand McCormick bought in 2000.","France","2000",MC,"MCC"),("Zatarain's","Louisiana seasoning brand McCormick bought in 2003.","United States","2003",MC,"MCC"),("Lawry's","Seasoning brand McCormick bought in 2008.","","2008",MC,"MCC"),("Kamis","Polish spice brand McCormick bought in 2011.","Poland","2011",MC,"MCC"),("Club House","Spice brand owned by McCormick.","","",MC,"MCC"),("Vahiné","Baking and seasoning brand owned by McCormick.","","",MC,"MCC"),("Just Spices","German spice brand in which Kraft Heinz holds a majority stake.","Germany","",KH,"KH"),("Cerebos Pacific","Seasoning business Kraft Heinz bought in March 2018.","","2018",KH,"KH"),("Robertson's","Unilever spice and seasoning brand sold in South Africa.","South Africa","",UN,"UNI")]
for n,d,c,oy,o,sr in sp: E("Spice and seasoning brands",n,d,n,"",o,G,c,oy or None,sr)
for x in kn("Barbecue rubs and seasonings")['x']:
    if x['n']=='Old Bay Seasoning': x.update({"own":MC,"tier":G,"cty":"United States","own_y":"1990"})
DROP={"Whole grain thin spaghetti","Tagliatelle nests","Elbows","Macarrones","Medium shells","Acini di pepe","Dried soup","Infant cereal","Thai Hom Mali","Lentille verte du Puy AOP"}
rm={"conv":0,"drop":0,"merged":0}
for name,(dp,sh,k) in list(K.items()):
    ms=k.get('m')
    if not ms: continue
    groups={}; order=[]
    for model,maker in ms:
        if model in DROP: rm['drop']+=1; continue
        match=None
        for e in k.get('x',[]):
            if norm(e['n'])==norm(model) or (maker and e.get('mk')==maker) or (maker and len(norm(maker))>3 and norm(maker) in norm(e['n'])):
                match=e;break
        if match:
            if norm(match['n'])!=norm(model) and not any(norm(v['n'])==norm(model) for v in match['v']): match['v'].append({"n":model,"mk":maker,"y":"","d":""})
            rm['merged']+=1; continue
        key=maker or model
        if key not in groups: groups[key]=[]; order.append(key)
        groups[key].append((model,maker))
    for key in order:
        lst=groups[key]; src=k.get('s') or sh.get('s') or S['PDO']
        if len(lst)==1:
            model,maker=lst[0]
            e={"n":model,"a":"","d":(f"{model}, sold under the {maker} name." if maker else f"{model}, a named regional or varietal type of this kind."),"mk":maker,"y":"","s":src,"v":[],"dt":"","g":maker or "Named types"}
        else:
            e={"n":key,"a":"","d":f"{key}, with {len(lst)} products named on the page cited.","mk":key,"y":"","s":src,"v":[{"n":m_,"mk":key,"y":"","d":""} for m_,_ in lst],"dt":"","g":key}
        if not any(norm(x['n'])==norm(e['n']) for x in k.get('x',[])):
            k.setdefault('x',[]).append(e); rm['conv']+=1
    k.pop('m')
srcname=lambda u: re.sub(r'^https?://(www\.)?','',u).split('/')[0]
for name,(dp,sh,k) in K.items():
    x=k.get('x') or []
    if not x: continue
    if 'nl' not in k:
        branded=sum(1 for e in x if e.get('mk'))>len(x)/2
        k['nl']=("One entry is a branded product line sold under its own name; flavours, sizes and pack variants are versions." if branded else "One entry is a named variety, style or protected origin of this kind; grades, sizes and pack variants are versions.")
    if 'sel' not in k:
        hosts=sorted({srcname(e['s']) for e in x if e.get('s')})
        k['sel']="Follows the pages cited on each entry ("+", ".join(hosts[:4])+("…" if len(hosts)>4 else "")+"). No whole-space reference list exists for this kind, so the entries are the named items those pages give, not a complete canon."
pasta_sel=f"Follows Wikipedia, List of pasta, read through all tables to the end of the page (section as g). Complete: {PASTA_N} of {PASTA_N} named pastas in Wikipedia, List of pasta, spread over the pasta kinds of this shelf; shapes the page lists under another name are matched to the existing entry. Producer ranges are not entries."
for kx in PK.values():
    k=kn(kx); k['nl']="One entry is a named pasta shape from the Wikipedia list of pasta; makers' ranges are not entries."; k['sel']=pasta_sel
kn("Pasta brands")['nl']="One entry is a packaged pasta brand; shapes and pack sizes are not versions."
kn("Pasta brands")['sel']="Follows Wikipedia, Barilla Group (brands owned, with acquisition years). Covers 5 of the brands that page names for the Barilla portfolio; other pasta makers were not read."
rice_sel=f"Follows Wikipedia, List of rice cultivars, country by country. Covers {rice_cnt} of about 1,000 named cultivars; scope cut to the national lists for Italy, Spain, Japan, California, Carolina, Louisiana, Australia, Portugal, Thailand, Vietnam and India. The long Bangladeshi, Indonesian, Pakistani, Philippine, Nepali and regional Indian landrace lists and the Greek list were not added."
for kx in ["Risotto rice","Paella rice","Medium- and short-grain rice","Sake rice","Sticky rice","Red and black rice","Long-grain rice"]:
    k=kn(kx); k['nl']="One entry is a named rice cultivar or protected rice from the Wikipedia list of rice cultivars; brands and pack sizes are not entries."; k['sel']=rice_sel
spice_sel=f"Follows Wikipedia, Spice mix, by region. Covers {spice_n} blends not already a kind of their own on this shelf; the page reader may have dropped rows, so this is not a verified complete count."
for kx in ["European herb and spice blends","Middle Eastern and African spice blends","East and Southeast Asian spice blends","South Asian masalas","Barbecue rubs and seasonings"]:
    k=kn(kx); k['nl']="One entry is a named spice or seasoning blend from the Wikipedia list of spice mixes."; k['sel']=spice_sel
k=kn("Spice and seasoning brands"); k['nl']="One entry is a spice or seasoning brand; its owner and acquisition year are recorded where a fetched page gives them."; k['sel']="Follows the McCormick, Kraft Heinz and Unilever brand pages. Covers 10 brands from those three portfolios; no whole-space list of spice brands exists."
for kx in ["Olive oil","Split pulses and dals","Paprika"]:
    k=kn(kx); k['sel']=(k.get('sel') or '')+" Protected names added from Wikipedia, List of Protected Designation of Origin products by country. Covers 5 olive oil, pulse and spice rows; the eAmbrosia register is the complete source and was not readable, and the page reader returned no Spanish, Greek or French oil rows."
kn("Instant noodles")['nl']="One entry is an instant-noodle brand sold under its own name; flavours are versions."
kn("Instant noodles")['sel']="Follows Wikipedia, List of instant noodle brands. Covers 20 of about 70 brands, chosen as the national champions of 14 markets; the first 100,000 of 144,545 characters were read."
for kx in ["Ketchup","Mayonnaise","Mustard","Soy sauce","Stock cubes and bouillon","Frozen ready meals","Frozen pizza"]:
    k=kn(kx); k['sel']=k['sel']+" Branded entries follow the portfolio pages of Kraft Heinz, Unilever, Nestlé, Conagra Brands, McCormick, Mizkan, Ajinomoto and Kikkoman (owner, tier and year of acquisition as those pages state)."
def D(n): return [d for d in j['depts'] if d['n']==n][0]
D("Rice, pasta & noodles")['ms']=[
 {"mkt":"Italian pasta","who":"Barilla","share":"24.5 %","yr":2021,"s":S['BAR'],"note":"share of the Italian market; the page cites a May 2021 source and gives no other date"},
 {"mkt":"Thai instant noodles","who":"Ajinomoto (YumYum)","share":"20–21 %","yr":2019,"s":S['AJI'],"note":"of a 17 billion baht market"},
 {"mkt":"Indian instant noodles","who":"Nestlé (Maggi)","share":"60 %","yr":2018,"s":S['INN'],"note":"as the page states"},
 {"mkt":"Malaysian instant noodles","who":"Nestlé (Maggi)","share":"39 %","yr":2018,"s":S['INN'],"note":"as the page states"},
 {"mkt":"Ramen (Demae Iccho)","who":"Nissin Foods","share":"about 60 %","yr":2016,"s":S['INN'],"note":"of the ramen market, as the page states"}]
D("Sauces & condiments")['ms']=[{"mkt":"World soy sauce production","who":"Kikkoman Corporation","share":"largest producer","yr":2002,"s":S['KIK'],"note":"the page gives no percentage"}]
have={b['n'] for b in brands['b']}
def B(n,c,f,kf,d,s):
    if n in have: return
    b={"n":n,"c":c,"seg":"Mainstream","kf":kf,"d":d,"s":s}
    if f: b["f"]=f
    brands['b'].append(b); have.add(n)
B("Kraft Heinz","United States","2015","sauces, spreads","American food group formed in 2015 by the merger of Kraft Foods Group and H.J. Heinz.",S['KH'])
B("Unilever","","","sauces, soups","British multinational whose food brands include Hellmann's, Knorr and Maille.",S['UNI'])
B("Nestlé","","","seasonings, frozen meals","Food group whose brands include Maggi, Buitoni and Stouffer's.",S['NES'])
B("Conagra Brands","United States","","frozen and canned foods","Chicago food company that owns Hunt's, Healthy Choice and Marie Callender's.",S['CON'])
B("McCormick","United States","","spices, hot sauce","Hunt Valley spice company, the largest spice producer by revenue.",S['MCC'])
B("Ajinomoto","Japan","1917","seasonings, instant noodles","Tokyo food company behind Aji-no-moto, Hon-Dashi and Cook Do.",S['AJI'])
B("Kikkoman Corporation","Japan","1917","soy sauce","Noda soy sauce maker, the world's largest producer as of 2002.",S['KIK'])
B("Mizkan","Japan","1804","vinegar, pasta sauce","Handa company that owns Ragú, Bertolli pasta sauce and Sarson's.",S['MIZ'])
B("Barilla Group","Italy","1877","pasta","Parma pasta maker, the world's leading pasta producer.",S['BAR'])
B("Lee Kum Kee","Hong Kong","1888","oyster sauce","Family-owned maker of over 300 Chinese-style sauces.",S['LKK'])
B("Kewpie Corporation","Japan","1919","mayonnaise","Tokyo maker of Kewpie mayonnaise, produced since 1925.",S['KEW'])
B("Flora Food Group","","2018","margarine","Spreads business spun off from Unilever in 2018, first as Upfield.",S['UNI'])
def wr(p,o):
    t=p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
wr(R+'out/J5.json',j); wr(R+'out/J5_brands.json',brands)
tx=sum(len(k.get('x',[])) for _,(a,b,k) in K.items())
print('pasta rows',PASTA_N,'matched existing',seen_pasta,'rice rows',rice_cnt,'rice new',rice_new,'spice',spice_n,'m',rm,'total x',tx,stats)
