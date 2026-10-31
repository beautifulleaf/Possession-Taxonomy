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
 'Calèche':'floral chypre','Krasnaya Moskva':'floral chypre','Knowing':'floral chypre','Diorama':'fruity chypre','Ma Griffe':'green chypre','Aromatics Elixir':'woody chypre','Paco Rabanne Pour Homme':'fougère','Boss':'fougère','Canoe':'fougère (Canoe for Men)','Michael for Men by Michael Kors':'fougère','Kouros':'fougère','Vent Vert':'green','Chanel No. 19':'balsamic-green','Eternity':'green','Aliage':'green','Cool Water':'aquatic, ozonic','Dune':'aquatic, ozonic',"L'Eau d'Issey":'aquatic floral','Brut':'fougère','Drakkar Noir':'fougère'}
FAMSRC={'Quelques Fleurs':'https://en.wikipedia.org/wiki/Perfume','Joy':'https://en.wikipedia.org/wiki/Perfume'}
fam('Chypre fragrance','Calèche','Krasnaya Moskva','Knowing','Diorama','Ma Griffe','Aromatics Elixir')
fam('Fougère fragrance','Paco Rabanne Pour Homme','Boss','Canoe','Michael for Men by Michael Kors','Kouros')
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

# ---- follow-up: owners from Wikipedia API intros (houses.json batches) ----
WA='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&explaintext=1&format=json&redirects=1&titles='
for h in ['Coty','Coty Prestige','Coty US','Coty US LLC','Coty Beauty US','Coty, Inc.','Coty Inc.','Calvin Klein Cosmetics','Max Factor','Davidoff','Zino Davidoff','Zino Davidoff Group']:
    house([h],'Coty',G,'','',W_+'Coty,_Inc.')
for h in ['Tom Ford Beauty','The Estée Lauder Companies','Estée Lauder Companies','Estée Lauder Companies/Givaudan','Estée Lauder Cos./Ermenegildo Zegna','Estée Lauder USA','Prescriptives','Aramis (Estée Lauder)']:
    house([h],'The Estée Lauder Companies',G,'United States' if h=='Prescriptives' else '','',W_+'Est%C3%A9e_Lauder_Companies')
for h in ['Puig USA','Puig Prestige Beauty','Puig Beauty & Fashion Group']: house([h],'Puig',G,'','',W_+'Puig_(company)')
for h in ['Inter Parfums USA','Cosmopolitan Cosmetics / Inter Parfums','Interparfums']: house([h],'Interparfums',I,'','',IP)
for h in ["L'Oréal","L'Oréal/dsm-firmenich","Giorgio Armani Parfums","Giorgio Armani Beauty","Ralph Lauren Fragrances","Cacharel","Lancôme"]:
    house([h],"L'Oréal",G,'France' if h in('Cacharel','Lancôme') else '','',W_+'L%27Or%C3%A9al')
for h in ['Christian Dior Perfumes','Parfums Dior']: house([h],'LVMH',G,'France','',W_+'LVMH')
house(['Bulgari'],'LVMH',G,'Italy','2011',W_+'Bulgari')
house(['Parfums Fendi','Fendi'],'LVMH',G,'Italy','2001',W_+'Fendi')
house(['Gucci Parfums'],"L'Oréal",G,'','2026',W_+'L%27Or%C3%A9al')
house(['Elizabeth Arden'],'Revlon, Inc.',I,'United States','2016',W_+'Elizabeth_Arden,_Inc.')
house(['Revlon'],'Revlon',I,'United States','',W_+'Revlon')
house(["Victoria's Secret","Victoria's Secret Beauty"],"Victoria's Secret & Co.",I,'United States','2021',W_+"Victoria%27s_Secret")
house(['Versace'],'Prada Group',I,'Italy','2025',W_+'Versace')
house(['Hermès'],'H51 (descendants of the founder)',I,'France','',W_+'Herm%C3%A8s')
house(['Prince Matchabelli'],'Parfums de Coeur',I,'','1993',W_+'Prince_Matchabelli')
house(['Caron'],'Cattleya',I,'France','',W_+'Parfums_Caron')
house(['Roger & Gallet'],'Impala SAS',I,'France','2020',W_+'Roger_%26_Gallet')
house(['Mäurer & Wirtz'],'Dalli Group',I,'Germany','1990',W_+'M%C3%A4urer_%26_Wirtz')
house(['Chopard'],'Scheufele family',I,'Switzerland','1963',W_+'Chopard')
house(['Lalique'],'Lalique Group SA',I,'France','2010',W_+'Lalique')
house(['Cartier','Parfums Cartier Paris'],'Richemont Group',I,'France','',W_+'Cartier_(brand)')
house(['Banana Republic'],'The Gap',I,'United States','1983',W_+'Banana_Republic')
house(['Geoffrey Beene'],'Authentic Brands Group',I,'United States','2021',W_+'Geoffrey_Beene')
house(['Trussardi'],'Miroglio Group',I,'Italy','2024',W_+'Trussardi')
house(['Escada','Escada Beauté'],'Regent, L.P.',I,'Germany','',W_+'Escada')
house(['Schiaparelli'],'Tod\'s Group',I,'','',W_+'Schiaparelli_(fashion_house)')
CTY={'Carven':'France','Houbigant':'France','Houbigant Paris':'France','Robert Piguet':'Switzerland','Jean Patou':'France','Parfums de Marly':'France','Xerjoff':'Italy','Nishane':'Turkey','Lattafa':'United Arab Emirates','Bath & Body Works':'United States','Bond No. 9':'United States','Bond No. 9 New York':'United States','Caswell-Massey':'United States','Glossier':'United States','Halston':'United States','Halston Fragrances':'United States','Shiseido':'Japan','Gloria Vanderbilt':'United States','Charles of the Ritz':'United States','Molinard':'France','Issey Miyake':'Japan','Lolita Lempicka':'France','Elie Saab':'Lebanon','Christian Lacroix':'France','Farina':'Germany','Novaya Zarya':'Russia','Demeter Fragrance Library':'United States','The Demeter Fragrance Library':'United States','Sean John Fragrances':'United States','Dolce & Gabbana':'Italy','Yohji Yamamoto':'Japan','Gaultier':'France','Avon Products':'United States','Rochas':'France','Worth':'France'}
CTYH={norm(k):v for k,v in CTY.items()}
SRC_CTY='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&explaintext=1&format=json&redirects=1&titles=Wikipedia+house+articles'

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
    if mk=='unknown': mk=''
    if n=='Y': n='Y (1964)'
    add(n,y,mk,per,LOP)
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

# ================= stage 2: assemble =================
CIRC='https://www.cosmeticsbusiness.com/us-prestige-beauty-tops-33-billion-in-2024'
PUIGA='https://cosmeticsbusiness.com/puig-s-2024-full-year-profits-surge-14-percent'
def era(y):
    if 'century' in str(y or ''): return 'Before 1900'
    y=ydig(y)
    if y is None: return 'Year not stated'
    if y<1900: return 'Before 1900'
    if y<1950: return '1900 to 1949'
    if y<1980: return '1950 to 1979'
    if y<2000: return '1980 to 1999'
    if y<2010: return '2000 to 2009'
    return '2010 onwards'
ERAS=['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated']
PUIGLM={norm('Good Girl'):'Carolina Herrera Good Girl was the top women\'s fragrance line worldwide in 2024, per the cited Puig article.',norm('Le Male'):'Le Male ranked third among men\'s fragrances worldwide in 2024, per the cited Puig article.',norm('1 Million'):'1 Million ranked fourth among men\'s fragrances worldwide in 2024, per the cited Puig article.'}
def mkentry(k,kindname):
    e=REG[k]
    base=copy.deepcopy(e.get('ex')) if e.get('ex') else {'n':e['n'],'a':'','d':'','mk':e['mk'],'y':e['y'],'s':e['s']}
    base['n']=e['n']
    if not base.get('mk') and e['mk']: base['mk']=e['mk']
    if not base.get('mk') and e.get('fifi_h'): base['mk']=e['fifi_h']
    if not base.get('y') and e['y']: base['y']=e['y']
    if not base.get('s'): base['s']=e['s'] or LOP
    bits=[]
    if not e.get('ex') or not base.get('d'):
        t=FAMTXT.get(e['n'])
        if t: bits.append(f"Wikipedia describes the family as {t}.")
        l=''
        if base.get('y') and base.get('mk'): l=f"Launched {base['y']} by {base['mk']}"
        elif base.get('mk'): l=f"Fragrance by {base['mk']}"
        elif base.get('y'): l=(f"Dated to the {base['y']}; maker not stated" if 'century' in base['y'] else f"Launched {base['y']}")
        if l:
            if e.get('per'): l+=f"; perfumer {e['per']}"
            bits.append(l+'.')
        aw=[a for a in dict.fromkeys(e['awards']) if not (e.get('hof') and a.startswith('Fragrance Hall of Fame'))]
        if aw: bits.append("FiFi: "+'; '.join(aw[:4])+('; and others' if len(aw)>4 else '')+'.')
        if e.get('osm'): bits.append("Held in the Osmothèque reference collection.")
        if e.get('wd') and not bits: bits.append("Perfume with an English Wikipedia article.")
        if not bits: bits.append("Named perfume from the cited list.")
        base['d']=' '.join(bits)
    else:
        pass
    # versions
    vs=base.get('v') or []
    names={v['n'].lower() for v in vs}
    def addv(vn,vy,vd):
        if vn.lower() in names: return
        names.add(vn.lower()); vs.append({'n':vn,'mk':base.get('mk',''),'y':str(vy or ''),'d':vd})
    for vn,vy,note in e.get('vers',[]): addv(vn,vy,note or 'variant named by the cited list')
    for vn,vy in e.get('cv',[]): addv(vn,vy,'Chanel flanker named on the Chanel page')
    for vn,vy in e.get('kv',[]): addv(vn,vy,'named on the Francis Kurkdjian page')
    for vn,y_,note,h in e.get('pv',[]): addv(vn,y_,note)
    if vs: base['v']=vs
    # market
    h=house_of(base.get('mk',''))
    if not h and norm(base.get('mk','')) in CTYH:
        base['own']='owner not stated'; base['cty']=CTYH[norm(base['mk'])]
    if h:
        base['own'],base['tier']=h[0],h[1]
        if h[2]: base['cty']=h[2]
        if h[3]: base['own_y']=h[3]
    if e.get('hof') or k in PUIGLM:
        base['role']='landmark'
        hy=[a.split()[-1] for a in e['awards'] if a.startswith('Fragrance Hall of Fame')]
        if 'Inducted into' not in base['d'] and 'ranked' not in base['d'] and 'top women' not in base['d']: base['d']=base['d'].rstrip()+((' Inducted into the FiFi Fragrance Hall of Fame in '+' and '.join(hy)+'.') if e.get('hof') else ' '+PUIGLM[k])
    if not base.get('own'): base['own']='owner not stated'
    base.pop('g',None)
    if kindname==UNST: base['g']=era(base.get('y'))
    return base
KIND_ENT={}
for k in ORDER:
    e=REG[k]
    kn=FAM.get(k) or e['kind'] or UNST
    if kn not in {x['n'] for sh in dept['s'] for x in sh['k']}: kn=UNST
    KIND_ENT.setdefault(kn,[]).append(mkentry(k,kn))
def sortkey(x):
    y=ydig(x.get('y'))
    if 'century' in str(x.get('y') or ''): y=1300
    return (y if y is not None else 9999, x['n'].lower())
for kn in KIND_ENT: KIND_ENT[kn].sort(key=sortkey)
# fix sections ordering for UNST: by era order then year
KIND_ENT[UNST].sort(key=lambda x:(ERAS.index(x['g']),)+sortkey(x))
N_ALL=sum(len(v) for v in KIND_ENT.values())
COMMON=("Entries come from fetched references: all 112 Wikidata items that are perfumes with an English Wikipedia article (101 are named perfumes; 11 are not and are left out), "
 "every row of Wikipedia's List of perfumes that was read, every fragrance winner table and the Fragrance Hall of Fame on Wikipedia's FiFi Award page, and the fragrance lists on the Wikipedia pages of Guerlain, Chanel, Francis Kurkdjian and the Osmothèque. "
 "A perfume sits in a family kind only where a fetched page states its family; every other perfume is in Alcohol-based perfume. Fragrantica's and Fragrances of the World's own databases could not be read, so the list is not their complete catalogue.")
COV=f"Complete: 112 of 112 Wikidata perfume items read; 265 of 265 rows of the List of perfumes read; 318 of 318 FiFi winner rows read; the Guerlain, Chanel and Kurkdjian lists cover the notable fragrances those pages name, and the Osmothèque list covers 13 named perfumes of over 3,000 in the collection."
newshelves=[]
for sh in dept['s']:
    ns={k:v for k,v in sh.items() if k!='k'}
    ks=[]
    for kd in sh['k']:
        nk={f:kd[f] for f in kd if f not in('m','r','x','s')}
        nk['s']=LOP
        xs=KIND_ENT.get(kd['n'],[])
        nk['nl']="One entry is a perfume sold under its own name; flankers and concentrations (EDT, EDP, parfum, intense) are versions of it."
        if kd['n']==UNST:
            nk['d']="Perfume sold under its own name for which the cited pages state no olfactive family; strength (parfum, eau de parfum, eau de toilette) still tells versions apart."
            nk['sel']=COMMON+f" Covers {len(xs)} of the {N_ALL} named perfumes in this department. A second pass tried Wikipedia intros for 165 of them (most have no article) and a Fragrantica designer page (it gives no family); the Chypre and Fougère articles then placed 10 more. "+COV
            nk['xg']="by launch period, then year, then name"
        else:
            nk['sel']=f"The {len(xs)} perfumes here are the ones a fetched page places in this family (Wikipedia's Perfume page, the Fragrance wheel page or the perfume's own Wikipedia article), or that the earlier structure pass placed here; all other perfumes are in Alcohol-based perfume. "+COV
            nk['xg']="by year, then name"
        nk['x']=xs
        ks.append(nk)
    ns['k']=ks
    if sh['n']=='By concentration':
        ns['n']='Family not stated'
        ns['t']="Perfume for which the cited pages give no olfactive family, sold by strength such as parfum, eau de parfum or eau de toilette."
        ns['ax']="one kind, by launch period"
    newshelves.append(ns)
newdept={f:dept[f] for f in dept if f!='s'}
newdept['msum']="Fragrance is a branded market: a few groups own most prestige houses and many fashion fragrances are licences. The figures below are the ones the cited pages state."
newdept['ms']=[
 {"mkt":"US prestige beauty","who":"Fragrance","share":"28 %","yr":2024,"s":CIRC,"note":"share of US$33.9 billion prestige beauty sales (Circana via Cosmetics Business); fragrance sales rose 12 %, luxury brands held 12 % of prestige fragrance"},
 {"mkt":"Global selective fragrances (value)","who":"Puig","share":"11.5 %","yr":2024,"s":PUIGA,"note":"value share as Puig reports it; Puig holds three places in the global top-ten fragrance brands"},
 {"mkt":"Puig net revenue","who":"Puig","share":"EUR 4.79 billion","yr":2024,"s":PUIGA,"note":"net revenue, up 11.3 % on 2023"},
]
for b,sh_ in [('Jimmy Choo','17 %'),('Montblanc','15 %'),('Coach','14 %'),('GUESS','12 %'),('Donna Karan/DKNY','7 %'),('Lacoste','6 %'),('Ferragamo','5 %')]:
    newdept['ms'].append({"mkt":"Interparfums net sales by licence","who":b,"share":sh_,"yr":2024,"s":IP,"note":"share of Interparfums net sales; the seven largest brands make 76 %; European operations about 65 % and US operations about 35 %"})
newdept['s']=newshelves
part={'replaces':['Perfume'],'depts':[newdept]}
# brands
bj=json.load(open(R+'out/H4_brands.json'))['b']
bn={norm(b['n']):b for b in bj}
upd={}
for b in bj:
    h=H.get(norm(b['n']))
    if h:
        u={'own':h[0],'tier':h[1]}
        if h[2]: u['c']=h[2]
        upd[b['n']]=u
part['brand_updates']=upd
owners=[("LVMH",'', "Owner group of Parfums Christian Dior, Guerlain, Givenchy, Kenzo, Acqua di Parma and Maison Francis Kurkdjian fragrance houses.",W_+'LVMH'),
 ("L'Oréal",'',"Owner group whose luxury division holds Yves Saint Laurent Beauté (bought 2008), Creed (completed 2026) and licences such as Armani, Prada and Ralph Lauren.",W_+'L%27Or%C3%A9al'),
 ("The Estée Lauder Companies",'',"Owner group of Tom Ford, Jo Malone London, Le Labo, Frédéric Malle, Aramis and Clinique, with fragrance licences such as Tommy Hilfiger and Michael Kors.",W_+'Est%C3%A9e_Lauder_Companies'),
 ("Puig",'Spain',"Barcelona group founded 1914 that owns Rabanne, Nina Ricci, Jean Paul Gaultier, Penhaligon's, L'Artisan Parfumeur and Byredo and holds the Carolina Herrera licence.",W_+'Puig_(company)'),
 ("Interparfums",'',"Licence-based fragrance group whose largest brands are Jimmy Choo, Montblanc and Coach; it owns Rochas and Lanvin's class 3 rights.",IP),
 ("Chanel Limited",'United Kingdom',"London holding company, set up in 2018, through which the Wertheimer brothers own Chanel.",W_+'Chanel'),
 ("Manzanita Capital",'United Kingdom',"London private equity firm that bought Diptyque in 2005.",W_+'Diptyque'),
 ("Oman Perfumery LLC",'Oman',"Omani company of the SABCO Group that owns Amouage.",W_+'Amouage'),
 ("Revlon, Inc.",'United States',"US beauty company whose wholly owned subsidiary is Elizabeth Arden, Inc. (as of 2016).",W_+'Elizabeth_Arden,_Inc.'),
 ("Prada Group",'Italy',"Italian luxury group that bought Versace in 2025.",W_+'Versace'),
 ("Richemont Group",'',"Swiss luxury group that owns Cartier.",W_+'Cartier_(brand)'),
 ("Cattleya",'Luxembourg',"Luxembourg-based owner of Caron as of 2019.",W_+'Parfums_Caron'),
 ("Impala SAS",'France',"French company that took over Roger & Gallet in 2020.",W_+'Roger_%26_Gallet'),
 ("Dalli Group",'Germany',"German group that owns Mäurer & Wirtz (since 1990).",W_+'M%C3%A4urer_%26_Wirtz'),
 ("Parfums de Coeur",'',"Owner of Prince Matchabelli since 1993.",W_+'Prince_Matchabelli'),
 ("Lalique Group SA",'France',"Lalique group, formerly Art & Fragrance SA, owner of the Lalique fragrance business since 2010.",W_+'Lalique')]
part['brands']=[{'n':n,'c':c,'seg':'Owner group','d':d,'s':s} for n,c,d,s in owners if norm(n) not in bn]
part['renames']={}
part['moves']=[]
json.dump(part,open(R+'out/H4_parts/PERFUME.json','w'),ensure_ascii=False)
print('entries',N_ALL,{k:len(v) for k,v in KIND_ENT.items()})
print('role',sum(1 for v in KIND_ENT.values() for x in v if x.get('role')),'own',sum(1 for v in KIND_ENT.values() for x in v if x.get('own')))
print(os.path.getsize(R+'out/H4_parts/PERFUME.json'))
