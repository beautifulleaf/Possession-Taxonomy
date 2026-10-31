import json,re,sys,os,copy,shutil
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J3')
from names import nz,existing
R='/home/user/Possession-Taxonomy/rebuild/'
B=R+'work/V4_J3/'
d=json.load(open(B+'bak/J3.json'))
brands=json.load(open(B+'bak/J3_brands.json'))
reg={x['n']:x for x in brands['b']}
W='https://en.wikipedia.org/wiki/'
SRC={'PDO':W+'List_of_European_cheeses_with_protected_geographical_status','IT':W+'List_of_Italian_PDO_cheeses','UK':W+'List_of_British_cheeses','CH':W+'List_of_Swiss_cheeses','MAIN':W+'List_of_cheeses','FR':W+'List_of_French_cheeses','ES':W+'List_of_Spanish_cheeses'}
LIST_REFS="Wikipedia's List of cheeses ("+SRC['MAIN']+"), the lists of French, Spanish, Swiss and British cheeses and of Italian PDO cheeses, and the list of European cheeses with protected geographical status ("+SRC['PDO']+")"
# ---------- index
depts={dp['n']:dp for dp in d['depts']}
def find_kind(name):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==name: return dp,s,k
    return None
def find_shelf(name):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==name: return s
# ---------- remove loose models
removed=[]
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for m in k.pop('m',[]) or []:
                removed.append({'dept':dp['n'],'shelf':s['n'],'kind':k['n'],'model':m[0],'maker':m[1]})
json.dump(removed,open(B+'removed_m.json','w'),ensure_ascii=False,indent=1)
# ---------- new kinds
newkinds={
 'Central European & Balkan pressed cheese':('Regional pressed cheese',"Pressed table cheeses of Central and Eastern Europe and the Balkans, sold under their own regional names.",'trappista · Tolminc · Koryciński'),
 'Caucasian cheese':('Regional pressed cheese',"Armenian and Caucasian regional cheeses ripened in clay, skins or by mould, outside the brined and string-cheese kinds.",'Armenian cheese'),
 'Spanish regional cheese':('Spanish, Portuguese & Latin American cheese',"Named regional cheeses of Spain, mostly protected, that are not goat, blue, torta or Galician cheeses.",'queso Casín · Nata de Cantabria'),
 'Americas regional cheese':('Spanish, Portuguese & Latin American cheese',"Named cheeses of Latin America and Canada, mostly cow's milk and often melting or semi-hard.",'queso de Colonia · Chanco'),
 'Swiss regional cheese':('Alpine cheese',"Swiss cheeses outside the Gruyère, Emmental and Appenzeller families, from hard mountain wheels to soft and blue cheeses.",'Swiss cheese'),
}
for n,(sh,dd,al) in newkinds.items():
    find_shelf(sh)['k'].append({'n':n,'a':al,'d':dd,'s':SRC['MAIN'],'x':[]})
sh=find_shelf('Regional pressed cheese')
sh['t']=sh['t'].rstrip('.')+', plus Central European, Balkan and Caucasian pressed cheeses.'
sh['ax']=sh['ax'].rstrip('.')+', then Central Europe and the Caucasus'
# ---------- add entries
def cap(s): return s[:1].upper()+s[1:]
rows=[l.rstrip('\n').split('|') for l in open(B+'rows.txt') if l.strip()]
S=existing(d)
added=[];skipped=[]
for kind,name,alias,place,milk,typ,src,desg in rows:
    hit=S.get(nz(name))
    if hit: skipped.append((name,hit)); continue
    f=find_kind(kind)
    if not f: print('NO KIND',kind); continue
    k=f[2]
    mp=(', made from '+milk) if milk else ''
    if ',' in typ: dd=f"Cheese of {place}: {typ}{mp}."
    elif typ: dd=f"{cap(typ)} cheese of {place}{mp}."
    else: dd=f"Cheese of {place}{mp}."
    if desg: dd=dd[:-1]+f"; protected as a {desg}."
    e={'n':name,'a':alias,'d':dd,'mk':'','y':desg,'s':SRC[src],'v':[],'dt':''}
    k.setdefault('x',[]).append(e); added.append((kind,name,src))
    S[nz(name)]=(kind,name)
# versions
def addv(kn,xn,v):
    for x in find_kind(kn)[2]['x']:
        if x['n']==xn: x['v'].append(v)
addv('British farmhouse hard cheese','Cornish Yarg',{'n':'Wild Garlic Yarg','mk':'','y':'','d':'Cornish Yarg with a wild garlic leaf rind, listed separately on the page'})
for vn,vd in [('Queijo de Castelo Branco','Beira Baixa cheese of the Castelo Branco area'),('Queijo Amarelo da Beira Baixa','Beira Baixa cheese, yellow type'),('Queijo Picante da Beira Baixa','Beira Baixa cheese, piquant type')]:
    addv('Portuguese cured cheese','Queijos da Beira Baixa',{'n':vn,'mk':'','y':'PDO','d':vd})
# ---------- own / tier / cty
OWN={
 'Activia':('Danone','Global group','France',''),'Actimel':('Danone','Global group','France',''),'Oikos':('Danone','Global group','',''),
 'Fage Total':('Fage','Independent','Greece',''),'Chobani Greek Yogurt':('Chobani','National champion','United States',''),
 "siggi's":('Lactalis','Global group','United States','2018'),'Yakult':('Yakult Honsha','National champion','Japan',''),
 'Vifit':('FrieslandCampina','Global group','Netherlands',''),'Philadelphia':('Kraft Heinz and Mondelez International','Global group','United States',''),
 'Boursin':('Bel Group','Global group','France','2007'),'Mini Babybel':('Bel Group','Global group','France',''),
 'Leerdammer':('Lactalis','Global group','Netherlands','2021'),'Blue Castello':('Arla Foods','Global group','Denmark',''),
 'Saint Agur':('Savencia Fromage & Dairy','Independent','France',''),'Etorki':('Savencia Fromage & Dairy','Independent','France',''),
 "P'tit Basque":('Lactalis','Global group','France',''),'Cambozola':('Käserei Champignon','Independent','Germany',''),
 'Jarlsberg':('Tine','National champion','Norway',''),'Gudbrandsdalsost':('Tine','National champion','Norway',''),'Pultost':('Tine','National champion','Norway',''),
 'Icelandic skyr':('Mjólkursamsalan','National champion','Iceland',''),'Arla Icelandic-style skyr':('Arla Foods','Global group','Denmark',''),
 'Oka':('Agropur','National champion','Canada',''),'Västerbotten':('Norrmejerier','Independent','Sweden',''),'Džiugas':('Žemaitijos Pienas','National champion','Lithuania',''),
 'Yorkshire Wensleydale PGI':('Wensleydale Creamery (Saputo subsidiary)','Independent','United Kingdom',''),
 'Aseptic silken tofu':('Morinaga Nutritional Foods','Independent','United States',''),
}
nown=0
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for x in k.get('x',[]):
                t=OWN.get(x['n'])
                if not t and x.get('mk') and x['mk'] in reg and reg[x['mk']].get('c'):
                    t=(x['mk'],'Independent',reg[x['mk']]['c'],'')
                if t:
                    x['own'],x['tier'],x['cty']=t[0],t[1],t[2]
                    if t[3]: x['own_y']=t[3]
                    nown+=1
# ---------- nl / sel
P=sum(len(l.split(';')) for l in open(B+'pdo_all.txt'))
CHEESE=['Fresh, soft & blue cheese','Pressed & hard cheese','Stretched, brined & dried cheese']
COV=f"Covers the protected-status cheeses of the European list that fit this kind ({P} rows in the list, all placed in the three cheese departments) and part of the rows of the other lists; Wikipedia's List of cheeses was read in full (about 470 cheese rows, with France, Italy, Germany, the Netherlands, Belgium, Austria and Denmark on separate pages), so cheeses named only on those pages, dishes and rows with no make family are left out."
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            xs=k.get('x')
            if not xs: continue
            if dp['n'] in CHEESE:
                k['nl']="One entry is a named cheese of this kind: a protected-origin cheese, a regional traditional cheese or a named farmhouse cheese; makers, affineurs and ages are versions."
                k['sel']=f"Follows {LIST_REFS}, cut to the cheeses that belong to this make family. {COV}"
            else:
                k['nl']="One entry is a named product of this kind: a protected-origin product, a traditional regional product or an established brand; makers, flavours and sizes are versions."
                k['sel']=f"No complete list of this kind was fetched; entries follow the protected-name and brand pages cited on each entry. Covers {len(xs)} entries of an unknown total; not claimed complete."
# ---------- market layer
RANK=W+'List_of_largest_dairy_companies'
rk=[('Lactalis','France',30.2),('Nestlé','Switzerland',24.1),('Dairy Farmers of America','United States',21.7),('Danone','France',19.7),('Yili Group','China',17.5),('Fonterra','New Zealand',15.1),('Arla Foods','Denmark',14.8),('FrieslandCampina','Netherlands',14.1),('Mengniu Dairy','China',13.9),('Saputo Inc.','Canada',12.8),('Amul','India',11),('Unilever','United Kingdom',8.7),('Schreiber Foods','United States',7.4),('Savencia Fromage & Dairy','France',7.4),('Müller','Germany',6.7),('Sodiaal','France',6.3),('Agropur','Canada',6.1),('DMK Deutsches Milchkontor','Germany',5.9),('Froneri','United Kingdom',5.7),('Grupo Lala','Mexico',5.6)]
ms_milk=[{'mkt':'World dairy companies by dairy revenue','who':w,'share':f'US${v} billion (rank {i+1})','yr':2023,'s':RANK,'note':f'{c}; Rabobank estimates as reproduced in the page table headed 2024, revenue for FY 2023'} for i,(w,c,v) in enumerate(rk)]
ms_milk+=[
 {'mkt':'World cattle milk production','who':'India','share':'17 %','yr':2024,'s':'https://openknowledge.fao.org/server/api/core/bitstreams/23eaa328-ac5a-444e-ac62-80a636acd81f/content','note':'share of 985 Mt world raw milk, 81 % of it cattle milk; United States 13 %, Brazil and China 5 % each, Germany 4 % (FAO)'},
 {'mkt':'US raw milk','who':'Dairy Farmers of America','share':'about 22 %','yr':2016,'s':W+'Dairy_Farmers_of_America','note':'cooperative net sales said to represent about 22 percent of US raw milk production'},
 {'mkt':'Finnish milk','who':'Valio','share':'about 80 %','yr':'','s':W+'Valio','note':'owner farms produce around 80 percent of Finnish milk; the page gives no year'},
 {'mkt':'World dairy exports','who':'Fonterra','share':'about 30 %','yr':'','s':W+'Fonterra','note':'share of world dairy exports, undated on the page; consumer brands were 15 % of milk solids in 2024'},
 {'mkt':'New Zealand and Australian consumer dairy brands','who':'Lactalis','share':'','yr':2025,'s':W+'Lactalis','note':'agreed 22 August 2025 to buy Fonterra consumer brands Anchor, Mainland, Kāpiti, Anlene, Anmum, Fernleaf, Western Star and Perfect Italiano'},
]
msum_milk="Lactalis was the largest dairy company by dairy revenue (US$30.2 billion, FY 2023), ahead of Nestlé and Dairy Farmers of America. Chinese, Indian, Canadian, German, French and Mexican groups lead their home markets in the same table. India produced 17 % of the world's cattle milk in 2024. No African, South American or Middle Eastern group appears in the top 20, and no retail share figures were found."
ms_butter=[
 {'mkt':'India dairy co-operatives','who':'Amul','share':'INR 90,000 crore (about US$9.3 billion)','yr':2025,'s':W+'Amul','note':'all products; butter is one of them; the page gives no market share'},
 {'mkt':'Butter brands of New Zealand and Australia','who':'Lactalis','share':'','yr':2025,'s':W+'Lactalis','note':'Anchor and Western Star butter are among the brands in the Fonterra consumer business Lactalis agreed to buy'},
 {'mkt':'Butter brands of Denmark','who':'Arla Foods','share':'','yr':2022,'s':W+'Arla_Foods','note':'Lurpak sold worldwide; Arla revenue EUR 13.8 billion in 2022'},
]
msum_butter="Butter is sold by large cooperatives (Amul, Arla) and, in New Zealand and Australia, by brands now moving to Lactalis. The fetched pages gave no butter share figures."
ms_yog=[
 {'mkt':'Yoghurt brands of Danone','who':'Danone','share':'','yr':2025,'s':W+'Danone','note':'Activia, Danette, Danonino, Oikos, YoPro and Les 2 Vaches are listed main brands; group revenue EUR 27.283 billion in 2025'},
 {'mkt':'Organic and skyr yoghurt in the US','who':'Lactalis','share':'','yr':2018,'s':W+'Lactalis','note':'purchase of siggi\'s agreed January 2018; Stonyfield bought from Danone (agreed July 2017, US$875 million); General Mills US yogurt business completed 30 June 2025'},
 {'mkt':'Dutch dairy cooperative brands','who':'FrieslandCampina','share':'','yr':2024,'s':W+'FrieslandCampina','note':'revenue EUR 12.92 billion in 2024; brands include Friesche Vlag, Campina Vifit, Optimel, Fristi and Yazoo'},
]
msum_yog="Danone and Lactalis hold the best-known yoghurt brands of the groups reviewed. The fetched pages gave no yoghurt share figures."
ms_cheese1=[
 {'mkt':'Cheese brands of Lactalis','who':'Lactalis','share':'','yr':2020,'s':W+'Lactalis','note':'Président (Camembert, launched 1968), Galbani (bought 2006), Kraft Natural Cheese (agreed September 2020), Leerdammer, Castelli, Invernizzi, Ambrosi; Athenos and Polly-O divested as a US condition'},
 {'mkt':'Cheese brands of Arla Foods','who':'Arla Foods','share':'','yr':2022,'s':W+'Arla_Foods','note':'Castello cheese, including blue and yellow varieties, sold worldwide'},
 {'mkt':'French cheese groups','who':'Savencia Fromage & Dairy','share':'US$7.4 billion (rank 14)','yr':2023,'s':RANK,'note':'dairy revenue FY 2023'},
]
ms_cheese2=[
 {'mkt':'Canadian, US, Australian and UK cheese brands','who':'Saputo Inc.','share':'','yr':2019,'s':W+'Saputo_Inc.','note':'brands include Alexis de Portneuf, Armstrong, Cathedral City (Dairy Crest deal completed 15 April 2019), Frigo, Stella (1997), Treasure Cave, Woolwich Dairy, Yorkshire Wensleydale; revenue C$19.061 billion in FY 2025'},
 {'mkt':'Norwegian cheese','who':'Tine','share':'','yr':2025,'s':W+'Tine_(company)','note':'farmer-owned; Jarlsberg, Norvegia, Snøfrisk, Ski-Queen brunost; revenue NOK 30.1 billion in 2025; the page gives no share but says Tine faces little or no domestic competition in many categories'},
 {'mkt':'Dutch and German cheese brands','who':'FrieslandCampina','share':'','yr':2024,'s':W+'FrieslandCampina','note':'Frico, Milner, Parrano, Landliebe, Debic among the brands named'},
 {'mkt':'Finnish and US cheese','who':'Valio','share':'','yr':1992,'s':W+'Valio','note':'Koskenlaskija processed cheese since 1933; Finlandia brand bought in 1992; revenue EUR 2.4 billion in 2025'},
]
ms_cheese3=[
 {'mkt':'Mozzarella-type cheese in New Zealand and Australia','who':'Lactalis','share':'','yr':2025,'s':W+'Lactalis','note':'Perfect Italiano and Mainland are among the Fonterra consumer brands Lactalis agreed to buy in August 2025'},
 {'mkt':'US milk and cheese cooperatives','who':'Dairy Farmers of America','share':'US$21.7 billion (rank 3)','yr':2023,'s':RANK,'note':'brands include Plugrá, Meadow Gold, Kemps (2011), Oakhurst (2014); Breakstone\'s butter and Bel brands under licence'},
]
ms_eggs=[{'mkt':'World hen egg production','who':w,'share':sh,'yr':2024,'s':'https://openknowledge.fao.org/server/api/core/bitstreams/23eaa328-ac5a-444e-ac62-80a636acd81f/content','note':'share of 100 Mt world egg output, 94 % of it hen eggs (FAO)'} for w,sh in [('China','33 %'),('India','9 %'),('Indonesia','7 %'),('United States','7 %'),('Brazil','4 %')]]
ms_eggs.append({'mkt':'US commercial eggs','who':'Cal-Maine Foods','share':'about 20 %','yr':2025,'s':W+'Cal-Maine_Foods','note':'largest US egg producer as of 2024; brands include Egg-Land\'s Best, Land O\'Lakes, Farmhouse Eggs, Sunups'})
msum_eggs="China produced a third of the world's eggs in 2024, ahead of India, Indonesia, the United States and Brazil. In the US, Cal-Maine Foods produced about a fifth of commercial eggs. No grade or retail-brand figures were found."
ms_plant=[
 {'mkt':'US refrigerated oat milk','who':'Planet Oat','share':'35.2 %','yr':2023,'s':W+'Plant_milk','note':'dollar sales, 52 weeks to 21 May 2023; category sales about US$551 million'},
 {'mkt':'Oat drink company revenue','who':'Oatly','share':'US$722 million','yr':2022,'s':W+'Oatly','note':'revenue, not market share; key markets Sweden, Germany and the United Kingdom; Nativus (China Resources affiliate) holds 45.9 %'},
 {'mkt':'Plant drinks of Danone','who':'Danone','share':'','yr':2016,'s':W+'Danone','note':'Silk and Horizon came with WhiteWave (announced July 2016); Alpro is listed as a main brand'},
]
msum_plant="Planet Oat led US refrigerated oat milk in 2023 with 35.2 % of dollar sales. Danone owns Silk and Alpro; Oatly is an independent listed specialist. The fetched pages gave no share for soy, almond or other plant drinks."
msum_cheese="Cheese brands are held by the same dairy groups as milk: Lactalis, Arla, Saputo, FrieslandCampina, Savencia, Tine and Valio, plus protected-origin cheeses made by cooperatives and farms. No cheese retail share figures were found on the fetched pages."
MS={'Milk & cream':(ms_milk,msum_milk),'Butter & ghee':(ms_butter,msum_butter),'Yoghurt & fermented milks':(ms_yog,msum_yog),'Fresh, soft & blue cheese':(ms_cheese1,msum_cheese),'Pressed & hard cheese':(ms_cheese2,msum_cheese),'Stretched, brined & dried cheese':(ms_cheese3,msum_cheese),'Eggs':(ms_eggs,msum_eggs),'Dairy-free alternatives':(ms_plant,msum_plant)}
for n,(ms,su) in MS.items():
    depts[n]['ms']=ms; depts[n]['msum']=su
# ---------- brand register
def addb(n,c,f,d_,s):
    if n in reg: return
    brands['b'].append({'n':n,'c':c,'f':f,'seg':'Mainstream','d':d_,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':'dairy'})
    reg[n]=brands['b'][-1]
addb('Dairy Farmers of America','United States','1998','US dairy marketing cooperative, third largest dairy company by revenue in the Rabobank-based list.',W+'Dairy_Farmers_of_America')
addb('Fonterra','New Zealand','2001','New Zealand dairy cooperative; agreed in August 2025 to sell its consumer brands to Lactalis.',W+'Fonterra')
addb('Saputo','Canada','1954','Canadian dairy processor founded by the Saputo family; owner of Cathedral City since 2019 and Wensleydale Creamery.',W+'Saputo_Inc.')
addb('Cal-Maine Foods','United States','1957','Largest US egg producer, about a fifth of US commercial eggs; brands include Egg-Land\'s Best.',W+'Cal-Maine_Foods')
addb('Kraft Heinz','United States','','Owner, with Mondelez International, of the Philadelphia cream cheese brand.',W+'Philadelphia_Cream_Cheese')
addb('Mondelez International','United States','','Owner, with Kraft Heinz, of the Philadelphia cream cheese brand.',W+'Philadelphia_Cream_Cheese')
addb('Morinaga Nutritional Foods','United States','1985','Torrance, California maker of Mori-Nu silken tofu in aseptic cartons.','https://well.ca/brand/mori-nu.html')
addb('Nestlé','Switzerland','','Swiss food group, second largest dairy company by revenue in the Rabobank-based list.',RANK)
for n,c in [('Schreiber Foods','United States'),('Sodiaal','France'),('DMK Deutsches Milchkontor','Germany'),('Grupo Lala','Mexico'),('Froneri','United Kingdom'),('Unilever','United Kingdom')]:
    addb(n,c,'',f'Dairy group ranked in the top 20 by dairy revenue (FY 2023) in the Rabobank-based list.',RANK)
addb('Valio','Finland','1905','Finnish dairy owned by 13 cooperatives; owner of Finlandia since 1992.',W+'Valio')
for b in brands['b']:
    if b['n']=='Lactalis':
        b['d']='French dairy group headquartered in Laval, founded by André Besnier; owner of Parmalat, Galbani, Leerdammer and, since 2025, Fonterra\'s consumer brands such as Anchor.'
        b['s']=W+'Lactalis'
    if b['n']=='Anchor': pass
# ---------- write
def dump(p,o):
    open(p+'.tmp','w').write(json.dumps(o,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
dump(R+'out/J3.json',d); dump(R+'out/J3_brands.json',brands)
json.dump({'added':added,'skipped':skipped,'nown':nown,'removed':len(removed),'P':P},open(B+'stats.json','w'),ensure_ascii=False,indent=1)
print(len(added),'added',len(skipped),'skipped',nown,'own',len(removed),'removed m')
