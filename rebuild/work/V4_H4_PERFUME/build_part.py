# -*- coding: utf-8 -*-
import json, re, unicodedata, sys, os, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_extra import *
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/V4_H4_PERFUME/'
LOP='https://en.wikipedia.org/wiki/List_of_perfumes'
FIFI='https://en.wikipedia.org/wiki/FiFi_Award'
def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c)).lower()
    s=s.replace('&','').replace('°','').replace('#','no')
    s=re.sub(r'\bno\.?\s*(\d)',r'n\1',s)
    s=re.sub(r'[^a-z0-9]','',s)
    return s
ALIAS={ # variant -> canonical display
 'N°5':'Chanel No. 5','No. 19':'Chanel No. 19','Chanel #19':'Chanel No. 19','N°22':'Chanel No. 22',
 'Egoiste':'Égoïste','Chanel Chance':'Chance','Tabu by Dana':'Tabu','Aramis (fragrance)':'Aramis','Kouros (perfume)':'Kouros',
 'Davidoff Cool Water':'Cool Water','Dolce & Gabbana Light Blue':'Light Blue','Jean Paul Gaultier \'Le Male\'':'Le Male','Le Mâle':'Le Male',
 'Fracas De Robert Piguet':'Fracas','Polo Ralph Lauren':'Polo','Estée Lauder Pleasures':'Pleasures','Elizabeth Taylor White Diamonds':'White Diamonds',
 'Clinique Happy':'Happy','Calvin Klein ckONE':'CK One','Issey Miyake L\'Eau D\'Issey':"L'Eau d'Issey",'Oscar de la Renta':'Oscar',
 'Paco Pour Homme':'Paco Rabanne Pour Homme','Elizabeth Taylor\'s Passion':'Passion','Viktor & Rolf Flowerbomb':'Flowerbomb',
 '24 Faubourg':'24, Faubourg','Annick Goutal Eau d\'Hadrien':"Eau d'Hadrien",'Eau d\'Hadrien':"Eau d'Hadrien",'Acqua di Giò de Giorgio Armani':'Acqua di Giò',
 'Eau de Cologne':'Eau de Cologne (Farina)','Vétiver (Guerlain)':'Vétiver','Rabanne 1 Million Eau de Toilette':'1 Million','Donna Karan Cashmere Mist':'Cashmere Mist',
 'Obsession (luxury)':'Obsession','Halston (men\'s)':'Halston','Boss (men\'s)':'Boss','Oscar de la Renta Pour Lui':'Oscar de la Renta Pour Lui',
 'Gucci Guilty Pour Homme':'Gucci Guilty Pour Homme','Giorgio Armani Sì EDP':'Sì','Dior Sauvage EDP':'Sauvage','Narciso Rodriguez For Her EDP':'Narciso Rodriguez for Her','Narciso Rodriguez For Her':'Narciso Rodriguez for Her',
 'Prada Infusion d\'Iris':"Infusion d'Iris",'Chloé Eau de Parfum':'Chloé Eau de Parfum','Bulgari Black':'Bulgari Black','Tom Ford Bois Pacifique':'Bois Pacifique','Tom Ford Lost Cherry':'Lost Cherry',
 'Kilian Paris Sunkissed Goddess':'Sunkissed Goddess','Kayali Vanilla Candy Rock Sugar 42':'Vanilla Candy Rock Sugar | 42','Tom Ford Grey Vetiver':'Grey Vetiver','Tom Ford White Suede':'White Suede',
 'Ralph Lauren Romance':'Romance','Ralph Lauren Blue':'Ralph Lauren Blue','Allure':'Allure','J.H.L.':'J.H.L.','Cologne Intensa Oud':'Colonia Intensa Oud','Dior Homme 2020':'Dior Homme',
 'Burberry Brit':'Burberry Brit','Y':'Y (1964)','Hugo by Hugo Boss':'Hugo','Chanel No. 5':'Chanel No. 5','Boss':'Boss','Light Blue Pour Homme':'Light Blue Pour Homme',
 'Gucci Rush for Men':'Gucci Rush for Men','Ralph Lauren Romance Men':'Romance Men','Eternity for Men':'Eternity for Men','Obsession for Men':'Obsession for Men','Joy':'Joy','Shalimar':'Shalimar',
 'Mon Paris':'Mon Paris','Euphoria Calvin Klein':'Euphoria','Gucci Rush':'Gucci Rush','Heidi Klum Shine':'Shine','Today Tomorrow Always EDP':'Today Tomorrow Always',
 'Giorgio Armani Sì EDP':'Sì','Tom Ford Soleil Blanc':'Soleil Blanc','Tom Ford Fabulous':'Fabulous','Tom Ford Velvet Orchid':'Velvet Orchid','Tom Ford Noir':'Noir','Tom Ford Noir Pour Femme':'Noir pour Femme','1 Million Eau de Toilette':'1 Million','Daisy Marc Jacobs':'Daisy','New West Skinscent for Her':'New West',
}
PARENT={ # fifi/list name -> (parent display, version name)
 'Dior Sauvage EDT':('Sauvage','Eau de Toilette'),'Dior Sauvage Parfum':('Sauvage','Parfum'),'Sauvage Parfum':('Sauvage','Parfum'),'Sauvage Elixir':('Sauvage','Elixir'),
 "Terre d'Hermès Eau Givrée":("Terre d'Hermès",'Eau Givrée'),'Bleu de Chanel Parfum':('Bleu de Chanel','Parfum'),'Armani Acqua di Giò Parfum':('Acqua di Giò','Parfum'),
 'Acqua di Giò pour Homme':('Acqua di Giò','pour Homme'),'Dior Homme Eau':('Dior Homme','Eau'),'Polo Red':('Polo','Polo Red'),'Ralph Lauren Polo 67 EDT':('Polo','Polo 67'),'Polo Crest':('Polo','Polo Crest'),
 'Eternity for Men':('Eternity','for Men'),'Obsession for Men':('Obsession','for Men'),'Kouros Fraîcheur':('Kouros','Fraîcheur'),'Light Blue Pour Homme':('Light Blue','Pour Homme'),
 'Opium Fraîcheur d\'Orient':('Opium',"Fraîcheur d'Orient"),'Costa Azzurra Parfum':('Costa Azzurra','Parfum'),'Gucci Rush for Men':('Gucci Rush','for Men'),'Romance Men':('Romance','Men'),
 'Dior Homme 2020':('Dior Homme','2020'),'Miss Dior Chérie':('Miss Dior','Chérie'),'Tom Ford Oud Minérale':None,
 'Allure Homme':('Allure','Homme'),'Burberry Brit for Men':('Burberry Brit','for Men'),'Burberry Brit Red':('Burberry Brit','Red'),'Tiffany for Men':('Tiffany','for Men'),
 'Oscar de la Renta Pour Lui':('Oscar','Pour Lui'),"L'Eau d'Issey pour Homme":("L'Eau d'Issey",'pour Homme'),'Shalimar Light':('Shalimar','Light'),'Gucci Guilty Pour Homme':('Gucci Guilty','Pour Homme'),
 'Today. Tomorrow. Always. for Men':('Today Tomorrow Always','for Men'),'Spirit Antonio Banderas for Women':('Spirit Antonio Banderas','for Women'),'Eternity Now':None,
}
# family placement from fetched pages: key -> kind
FAM={}
def fam(kind,*names):
    for n in names: FAM[norm(n)]=kind
fam('Floral fragrance','Quelques Fleurs','Rive Gauche','Tea Rose','Lovely','Beautiful','Peau d\'Espagne','Chanel No. 5','Joy')
fam('Fruity fragrance','Radiance')
fam('Amber fragrance','Shalimar','Opium','Coco Mademoiselle','Elixir','S by Shakira','Youth-Dew')
fam('Gourmand fragrance','Angel')
fam('Musk & skin scent','Narciso Rodriguez for Her')
fam('Woody fragrance','Bois des Îles','Fierce','Santal 33')
fam('Chypre fragrance','Mitsouko','Femme','Aventus')
fam('Leather fragrance','Bandit','Aramis','Antaeus','Azurée')
fam('Citrus & eau de cologne','4711 Eau de Cologne','Eau de Cologne Impériale','Florida Water','Lacoste Essential','CK One')
fam('Green fragrance','Vent Vert','Chanel No. 19','Eternity','Aliage')
fam('Aquatic & ozonic fragrance','Cool Water','Dune',"L'Eau d'Issey")
fam('Fougère fragrance','Brut','Drakkar Noir')
FAMTXT={ # why placed (fetched statement)
 'Quelques Fleurs':'Floral bouquet','Rive Gauche':'aldehydic floral','Tea Rose':'green rose soliflore','Lovely':'light floral musk','Beautiful':'bright floral','Peau d\'Espagne':'floral, spicy',
 'Chanel No. 5':'soft floral on the Edwards wheel','Joy':'floral bouquet','Radiance':'floral-fruity','Shalimar':'amber','Opium':'amber, oriental-spicy','Coco Mademoiselle':'amber','Elixir':'amber, spicy, woody',
 'S by Shakira':'amber','Youth-Dew':'powdery amber','Angel':'gourmand','Narciso Rodriguez for Her':'musk, amber, orange blossom','Bois des Îles':'woody','Fierce':'woody aromatic','Santal 33':'sandalwood',
 'Mitsouko':'fruity chypre, mossy woods on the Edwards wheel','Femme':'chypre','Aventus':'fruity chypre','Bandit':'leather','Aramis':'leather chypre','Antaeus':'leather, chypre','Azurée':'leather or animalic chypre',
 '4711 Eau de Cologne':'citrus','Eau de Cologne Impériale':'citrus','Florida Water':'citric, sweet orange with clove and floral qualities','Lacoste Essential':'citrus, woody','CK One':'citrus, aromatic',
 'Vent Vert':'green','Chanel No. 19':'balsamic-green','Eternity':'green','Aliage':'green','Cool Water':'aquatic, ozonic','Dune':'aquatic, ozonic',"L'Eau d'Issey":'aquatic floral','Brut':'fougère','Drakkar Noir':'fougère'}
FAMSRC={'Quelques Fleurs':'https://en.wikipedia.org/wiki/Perfume','Joy':'https://en.wikipedia.org/wiki/Perfume'}
# house table: name -> (own, tier, cty, own_y, src)
G='Global group'; I='Independent'; C='Craft & indie'
H={}
def house(names,own,tier,cty='',oy='',src=''):
    for n in names: H[norm(n)]=(own,tier,cty,oy,src)
W_='https://en.wikipedia.org/wiki/'
house(['Chanel'],'Chanel Limited',I,'France','',W_+'Chanel')
house(['Guerlain'],'LVMH',G,'France','1994',W_+'Guerlain')
house(['Christian Dior','Dior','Parfums Christian Dior'],'LVMH',G,'France','',W_+'LVMH')
house(['Givenchy','Parfums Givenchy'],'LVMH',G,'','',W_+'LVMH')
house(['Kenzo','Parfums Kenzo'],'LVMH',G,'','',W_+'LVMH')
house(['Acqua di Parma'],'LVMH',G,'','',W_+'LVMH')
house(['Maison Francis Kurkdjian','Francis Kurkdjian'],'LVMH',G,'France','2017','https://en.wikipedia.org/wiki/Francis_Kurkdjian')
house(['Yves Saint Laurent'],"L'Oréal",G,'France','2008',W_+'L%27Or%C3%A9al')
for h in ['Armani','Giorgio Armani','Emporio Armani','Azzaro','Cacharel','Diesel','Thierry Mugler','Mugler','Prada','Ralph Lauren','Viktor & Rolf','Valentino','Maison Margiela','Miu Miu']:
    house([h],"L'Oréal",G,'','',W_+'L%27Or%C3%A9al')
house(['Creed'],"L'Oréal",G,'France','2026',W_+'Creed_(perfume_house)')
house(['Gucci','Balenciaga'],"L'Oréal",G,'','2026',W_+'L%27Or%C3%A9al')
for h in ['Estée Lauder','Clinique','Aramis','Tom Ford','Kilian Paris','Balmain','Tommy Hilfiger','Michael Kors','Tory Burch','Zegna','Aerin']:
    house([h],'The Estée Lauder Companies',G,'','',W_+'Est%C3%A9e_Lauder_Companies')
house(['Jo Malone London'],'The Estée Lauder Companies',G,'','1999',W_+'Est%C3%A9e_Lauder_Companies')
house(['Le Labo'],'The Estée Lauder Companies',G,'United States','2014',W_+'Le_Labo')
house(['Frédéric Malle','Editions de Parfums Frédéric Malle'],'The Estée Lauder Companies',G,'France','2015',W_+'Fr%C3%A9d%C3%A9ric_Malle')
for h,y in [('Calvin Klein','2005'),('Chloé','2005'),('Marc Jacobs','2003'),('Burberry','2017'),('Vera Wang','2005'),('Tiffany & Co','2016')]:
    house([h],'Coty',G,'',y,W_+'Coty,_Inc.')
for h in ['Davidoff','Hugo Boss','Jil Sander','JOOP!','Jovan','Jōvan','Escada','Lancaster','Nautica','Max Factor','David Beckham','Beyoncé','Katy Perry','Adidas','Bruno Banani']:
    house([h],'Coty',G,'','',W_+'Coty,_Inc.')
for h,y in [('Rabanne','1968'),('Paco Rabanne','1968'),('Nina Ricci','1998'),('Jean Paul Gaultier','2010'),("L'Artisan Parfumeur",'2015'),("Penhaligon's",'2015'),('Byredo','2022'),('Antonio Banderas','1997'),('Dries Van Noten','2018'),('Christian Louboutin','2018'),('Carolina Herrera','')]:
    house([h],'Puig',G,'Sweden' if h=='Byredo' else '',y,W_+'Puig_(company)')
house(['Shakira'],'Puig',G,'','2008',W_+'Puig_(company)')
IP='https://www.sec.gov/Archives/edgar/data/0000822663/000175392625000424/ipar-20241231.htm'
for h in ['Jimmy Choo','Montblanc','Coach','GUESS','Donna Karan','DKNY','Lacoste','Salvatore Ferragamo','Ferragamo','Abercrombie & Fitch','Anna Sui','Boucheron','Emanuel Ungaro','Ungaro','Karl Lagerfeld','Lagerfeld','Kate Spade','Oscar de la Renta','Van Cleef & Arpels','Roberto Cavalli','Rochas','Lanvin','Hollister','Graff']:
    house([h],'Interparfums',I,'France' if h=='Rochas' else '','',IP)
house(['Diptyque'],'Manzanita Capital',I,'France','2005',W_+'Diptyque')
house(['Amouage'],'Oman Perfumery LLC',I,'Oman','',W_+'Amouage')
house(['Serge Lutens'],'owner not stated',C,'France','',W_+'Serge_Lutens')
HP=sorted(H.items(),key=lambda kv:-len(kv[0]))
def house_of(mk,name=''):
    if not mk: return None
    k=norm(mk)
    if k in H: return H[k]
    return None

src=json.load(open(R+'out/H4.json'))
dept=[x for x in src['depts'] if x['n']=='Perfume'][0]
REG={}   # key -> entry
ORDER=[]
KINDOF={}
def get_key(name):
    n=ALIAS.get(name,name)
    return norm(n),n
def strip_prefix(name):
    PRE=['tom ford','kilian paris','kayali','dior','christian dior','giorgio armani','armani','marc jacobs','ralph lauren','calvin klein','jo malone','burberry','kenzo','hermes','dolce gabbana','yves saint laurent','donna karan','gucci','prada','elizabeth taylors','elizabeth taylor','estee lauder','viktor rolf','rabanne','paco rabanne','chanel','bvlgari','davidoff','clinique','balenciaga','giorgio armani prive','armani prive']
    k=norm(name)
    for p in sorted(PRE,key=len,reverse=True):
        pk=norm(p)
        if k.startswith(pk) and len(k)>len(pk)+2: yield k[len(pk):]
def find(name):
    k,n=get_key(name)
    if k in REG: return k
    for s in strip_prefix(name):
        if s in REG: return s
    return None
def ydig(y):
    m=re.search(r'\d{4}',str(y or ''))
    return int(m.group()) if m else None
def add(name,y='',mk='',per='',s='',kind=None,d=None,existing=None,note=None,hof=False,roles=None):
    if name.startswith('Tom Ford ') and len(name)>10 and name not in ALIAS: name=name[9:]; mk=mk or 'Tom Ford'
    if name in PARENT and PARENT[name]:
        pn,vn=PARENT[name]
        pk=find(pn) or add(pn,'',mk,'',s)
        REG[pk].setdefault('vers',[]).append((vn,str(y or ''),note or ''))
        if note: REG[pk]['awards'].append(note+' ('+vn+')')
        if hof: REG[pk]['hof']=True
        return pk
    k=find(name)
    if k is None:
        k,n=get_key(name)
        e={'n':n,'a':'','d':'','mk':mk or '','y':str(y) if y else '','s':s,'per':per,'awards':[],'srcs':[],'kind':kind}
        REG[k]=e; ORDER.append(k)
    e=REG[k]
    if mk and not e['mk']: e['mk']=mk
    if y and not e['y']: e['y']=str(y)
    if per and not e.get('per'): e['per']=per
    if s and not e['s']: e['s']=s
    if kind and not e['kind']: e['kind']=kind
    if existing is not None: e['ex']=existing
    if note: e['awards'].append(note)
    if hof: e['hof']=True
    return k
# 1 existing
oldm=[]
for sh in dept['s']:
    for kd in sh['k']:
        for e in kd.get('x',[]):
            k=add(e['n'],e.get('y',''),e.get('mk',''),'',e.get('s',''),kd['n'],existing=copy.deepcopy(e))
        for m in (kd.get('m') or []):
            oldm.append((m[0],m[1],kd['n'],kd['s']))
UNST='Alcohol-based perfume'
# 2 list of perfumes
for line in open(W+'lop.txt',encoding='utf-8'):
    p=line.rstrip('\n').split('|')
    if len(p)<4: continue
    n,y,mk,per=p[:4]
    if n=='Y': n='Y (1964)'
    PYR=re.match(r'\d{4}',y)
    add(n,y if PYR else '',mk,per,LOP)
    if not PYR: REG[find(n)]['yn']=y
# 3 wikidata
WDKEPT=0
for line in WD.split('\n'):
    t,n,y,mk,per=line.split('|')
    WDKEPT+=1
    k=add(n,y,mk,per,WP+t)
    e=REG[k]
    if e['s']==LOP or not e['s']: e['s']=WP+t
    e['wd']=True
# 4 fifi
CATL={'WP':"Women's Fragrance of the Year, Prestige",'MP':"Men's Fragrance of the Year, Prestige",'ML':"Men's Fragrance of the Year, Luxury",'WPo':"Women's Fragrance of the Year, Popular",'WL':"Women's Fragrance of the Year, Luxury",'MPo':"Men's Fragrance of the Year, Popular",'HF':'Fragrance Hall of Fame'}
FIFI_N=0
PARENT_V={}
for line in open(W+'fifi.txt',encoding='utf-8'):
    if line.startswith('#') or '|' not in line: continue
    y,c,n,h=line.rstrip('\n').split('|')
    FIFI_N+=1
    note=f"{CATL[c]} {y}"
    if n in PARENT and PARENT[n]:
        pn,vn=PARENT[n]
        PARENT_V.setdefault(pn,[]).append((vn,y,note,h))
        continue
    k=add(n,y if c!='HF' else '',h if c!='HF' else '',"",FIFI,note=note,hof=(c=='HF'))
    e=REG[k]
    e['fifi_h']=h
# apply PARENT_V
for pn,lst in PARENT_V.items():
    k=find(pn)
    if k is None:
        k=add(pn,'','','',FIFI)
    REG[k].setdefault('pv',[]).extend(lst)
# 5 Guerlain, Chanel, Kurkdjian, Osmotheque
for n,y,per in GUERLAIN:
    add(n,y,'Guerlain',per,W_+'Guerlain')
for n,y in CHANEL:
    add(n,y,'Chanel','',W_+'Chanel')
for pn,lst in CHANEL_V.items():
    k=find(pn) or add(pn,'','Chanel','',W_+'Chanel')
    for vn,vy in lst: REG[k].setdefault('cv',[]).append((vn,vy))
for n,y,mk in KURK:
    add(n,y,mk,'Francis Kurkdjian',W_+'Francis_Kurkdjian')
for pn,vn,vy in KURK_V:
    k=find(pn) or add(pn,'','','Francis Kurkdjian',W_+'Francis_Kurkdjian')
    REG[k].setdefault('kv',[]).append((vn,vy))
OSMU0='https://en.wikipedia.org/wiki/Osmoth%C3%A8que'
for n,y,mk,per in OSM:
    k=add(n,y,mk,per,OSMU0)
    REG[k]['osm']=True
for n in ['Fougère Royale','Jicky','Peau d\'Espagne','Chypre de Coty','Émeraude','Bandit','Nombre Noir']:
    k=find(n)
    if k: REG[k]['osm']=True
# key for Osmotheque url
OSMU='https://en.wikipedia.org/wiki/Osmoth%C3%A8que'
OSMU='https://en.wikipedia.org/wiki/Osmoth%C3%A8que'
for e in REG.values():
    if e.get('osm') and not e['s']: e['s']=OSMU
M_KEPT=[];M_DROP=[]
for nm,mk,kn,ks in oldm:
    k=find(nm)
    if k is None: M_DROP.append((nm,mk))
    else:
        M_KEPT.append(nm)
        if not REG[k]['mk']: REG[k]['mk']=mk
        if not REG[k]['kind'] and kn!=UNST: REG[k]['kind']=kn
json.dump({k:{kk:vv for kk,vv in v.items() if kk!='ex'} for k,v in REG.items()},open(W+'registry.json','w'),ensure_ascii=False,indent=0)
json.dump({'kept':M_KEPT,'dropped':M_DROP},open(W+'m_fate.json','w'),ensure_ascii=False)
print('m kept',len(M_KEPT),'dropped',len(M_DROP))
print('registry',len(REG),'wd kept',WDKEPT,'fifi rows',FIFI_N,'old m',len(oldm))
