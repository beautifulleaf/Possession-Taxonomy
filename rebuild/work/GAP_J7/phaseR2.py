import json,re,unicodedata,os
P='../../out/J7.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'\b(cachaca|premium|tequila|absinthe|absinth)\b','',s);return re.sub(r'[^a-z0-9]+','',s)
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
def ent(n,src,desc,mk='',cty=None,own=None,tier=None,y='',g=None):
    e={'n':n,'a':'','d':desc,'mk':mk or n,'y':y,'s':W+src,'v':[]}
    for a,b in(('cty',cty),('own',own),('tier',tier),('g',g)):
        if b: e[a]=b
    return e
def put(k,e):
    for x in k['x']:
        if norm(x['n'])==norm(e['n']):
            for a in('own','tier','cty','y'):
                if e.get(a) and not x.get(a): x[a]=e[a]
            if e.get('g') and e['g']!=x.get('g') and e.get('own'): x['g']=e['g']
            if e.get('s') and not x.get('s'): x['s']=e['s']
            return False
    k['x'].append(e);return True
def setsel(k,tail):
    k['sel']=re.split(r'(No complete list exists;|Complete:|Covers \d)',k['sel'])[0].rstrip()+' '+tail
# Cognac
c=kind('Cognac');S='Houses with a stated owner';O='Other houses named'
rows=[('Camus','Camus_Cognac','Camus La Grande Marque','Independent','France','1863',S),
('Delamain','Delamain_(Cognac_producer)','Bollinger','Independent','France','1824',S),
('Hine','Thomas_Hine_%26_Co.','EDV SAS','Independent','France','1763',S),
('Otard','Otard','Bacardi','Global group','France','1795',S),
('Bache-Gabrielsen/Dupuy','Bache-Gabrielsen','Bache-Gabrielsen family','Independent','France','1905',S),
('Braastad','Braastad','Arcus AS','Independent','France','1875',S),
('Moyet','Moyet',None,None,'France','1864',O),
('Frapin','Frapin',None,None,'France','',O),
('Gautier','Cognac_Gautier','Marie Brizard Wine & Spirits','Independent','France','1755',S),
('Monnet','Monnet_Cognac','EDV SAS','Independent','France','1838',S),
("D'Ussé","D%27USS%C3%89",'Bacardi','Global group','France','',S),
('Renault','Renault_(cognac)','Altia Plc','Independent','France','1835',S),
('Rome de Bellegarde','Rome_De_Bellegarde',None,None,'France','1725',O),
('Sève Fournier','S%C3%A8ve_Fournier',None,None,'France','1832',O),
('Fromy, Rogée & Co','Fromy,_Rog%C3%A9e_%26_Co',None,None,'France','1815',O),
('La Fontaine de La Pouyade','La_Fontaine_de_La_Pouyade_Cognac','Maison Dubosquet','Independent','France','',S)]
nn=0
for n,src,own,tier,cty,y,g in rows:
    nn+=put(c,ent(n,src,'Cognac house named on Wikipedia.',cty=cty,own=own,tier=tier,y=y,g=g))
for e in c['x']:
    if e['n'] in('Hennessy',) : e.setdefault('os','Wikipedia Hennessy: LVMH 66 %, Diageo 34 %')
setsel(c,f"Complete: {len(c['x'])} of {len(c['x'])} in Wikipedia Category:Cognac brands (16 pages) and Category:Cognac (18 pages) plus the great houses on whisky.fr; Louis XIII is a Rémy Martin cuvée, Noy is Armenian, and the larger list of about 200 houses on cognac-expert.com could not be fetched (402).")
# Grape brandy: Noy, Three Barrels
gb=kind('Grape brandy')
put(gb,ent('Noy','Noy_(brandy)','Armenian brandy of the Yerevan Ararat Brandy Factory, founded 1877.','Noy','Armenia','Yerevan Ararat Brandy Factory',None,'1877'))
put(gb,ent('Three Barrels','Three_Barrels','French brandy of Raynal & Cie, owned by William Grant & Sons, founded 1947.','Raynal & Cie','France','William Grant & Sons',None,'1947'))
# Armagnac
a=kind('Armagnac')
put(a,ent('Domaine de Bordeneuve','Domaine_de_Bordeneuve','Family-owned Armagnac house whose labels include Baron de Sigognac.','Domaine de Bordeneuve','France','Guasch family','Independent','',g='Producers'))
setsel(a,"Complete: 4 of 4 in Wikipedia Category:Armagnac (its six pages are the appellation, three areas, one house and the Baron de Sigognac label of that house) plus Janneau from the earlier edition; no complete list of houses exists.")
# Calvados
cv=kind('Calvados')
put(cv,ent('Calvados Roger Groult','Calvados_Roger_Groult','Pays d\'Auge Calvados house of Saint-Cyr-du-Ronceray.','Calvados Roger Groult SA','France','Calvados Roger Groult SA','Independent','1975',g='Producers'))
setsel(cv,"Complete: all pages of Wikipedia's Calvados houses that could be found (Category:Calvados is empty; one house page, Calvados Roger Groult, exists); no complete list of houses exists.")
# Absinthe
ab=kind('Absinthe')
for n,src,own,cty,y,ti in [('Absente','Absente',None,None,'2000',None),('Hapsburg','Hapsburg_Absinthe','Pallini','Italy','1999','Independent'),("Hill's Absinth","Hill%27s_Absinth","Hill's Liquere",'Czech Republic','1990','Independent'),
 ('Kübler','K%C3%BCbler_Absinthe','Altamar Brands','Switzerland','1863','Independent'),('La Clandestine','La_Clandestine','Artemisia-Bugnon','Switzerland','2008','Independent'),
 ('La Fée','La_F%C3%A9e_Absinthe','Green Utopia','France','2000','Independent'),('Lucid','Lucid_Absinthe','Hood River Distillers','France','2007','Independent'),
 ('Obsello','Obsello_Absenta','Lost Spirits','United States','2010','Independent')]:
    put(ab,ent(n,src,'Absinthe brand named in Wikipedia Category:Absinthes.',cty=cty,own=own,tier=ti,y=y,g='Brands'))
for e in ab['x']:
    if e['n']=='Kübler La Bleue': e.setdefault('own','Altamar Brands');e.setdefault('cty','Switzerland');e.setdefault('tier','Independent')
setsel(ab,f"Complete: all 8 brand pages of Wikipedia Category:Absinthes (10 members: Absente, Hapsburg, Hill's, Kübler, La Clandestine, La Fée, Lucid, Obsello, Pernod, and the Bohemian-style absinth article, which names a style); {len(ab['x'])} entries with earlier ones. Wikipedia says nearly 200 brands exist; owners are as each page states.")
# Cachaça
ca=kind('Cachaça')
ca['xg']='by market: wide distribution, small batch and artisan, made for export'
W1='Wide distribution';W2='Small batch and artisan';W3='Made for the export market'
wide='''Cachaça 51|São Paulo;Cachaça 61|São Paulo;Carvalho|São Paulo;Caninha da Roça|São Paulo;Chapéu de Palha|São Paulo;Jamel Branca|São Paulo;Jamel Ouro|São Paulo;Pinissilina|Minas Gerais;Pitú|Pernambuco;Três Muínho|Minas Gerais;Única|São Paulo;Velho Barreiro|São Paulo;Ypióca|Ceará;Nega Fulô|Rio de Janeiro;Sagatiba Pura|São Paulo'''
small='''ABOUT Brazil|;Anísio de Santiago|Minas Gerais;Beija|;Boca Loca|;Agatão|Minas Gerais;Balsa Velha|Rio Grande do Sul;Bartolomeu|;Bayu|São Paulo;Casa Buco|Rio Grande do Sul;Bento Albino|Rio Grande do Sul;Bento Velho|Minas Gerais;Cabana|São Paulo;Cachoeira|Minas Gerais;Cãna|Rio de Janeiro;Carvalheira|Pernambuco;Chico Mineiro|Minas Gerais;Claudionor|Minas Gerais;Companheira|Paraná;Coqueiro|Rio de Janeiro;Colinas do Sul|Minas Gerais;Curandeira do Bosco|Paraíba;Dom Bueno|Santa Catarina;Don Diego|São Paulo;Da Mata|Espírito Santo;Engenho Água Doce|Pernambuco;Engenho da Vertente|São Paulo;Engenho Bahia|Bahia;Espírito de Minas|Minas Gerais;Fazenda Soledade|Rio de Janeiro;Gabriela|São Paulo;Germana|Minas Gerais;Guapiara|Minas Gerais;Itagibá|Bahia;Magnífica|Rio de Janeiro;Quizumba|São Paulo;Sagatiba Velha|Minas Gerais;Saturno|Minas Gerais;Sapucaia Velha|São Paulo;Sanhaçu|Pernambuco;Santo Grau|São Paulo, Minas Gerais, Rio de Janeiro;São Paulo (Paraíba)|Paraíba;Terra Forte|Minas Gerais;Senzala|São Paulo;Schermann|São Paulo;Seleta|Minas Gerais;Vale Verde|Minas Gerais;Velha Januária|Minas Gerais;Wruck|Santa Catarina;Yaguara|Rio Grande do Sul;Chave de Ouro|Ceará;DJ Cachaça|Minas Gerais;Leblon|Minas Gerais;Maria da Cruz|Minas Gerais;Milagre de Minas|Minas Gerais;São Cachaça|Rio Grande do Sul;Soul Brazilian Premium|São Paulo;Weber Haus|Rio Grande do Sul'''
exp='''CapuCana|São Paulo;Abelha|Bahia;Água Luca|São Paulo;Aluarez|;Beleza Pura|;Brasilla|;Cachaça HUB|;Cachaça Brazil|;Fazenda Mãe de Ouro|;Cuca Fresca|São Paulo;Espírito XVI|;Frisco Fish|;GRM|Minas Gerais;Rio D|;Seven Waves|;Vogner|'''
for e in ca['x']:
    if e['n'] in('Cachaça 51','Ypióca'): e['g']=W1
    elif e['n'] in('Avuá','Novo Fogo'): e['g']=W3
    else: e.setdefault('g',W2)
for g,lst in((W1,wide),(W2,small),(W3,exp)):
    for it in lst.split(';'):
        n,st=it.split('|')
        put(ca,ent(n if n.lower().startswith('cach') else n,'List_of_Cacha%C3%A7a_brands',f"Cachaça brand listed by Wikipedia{(' from '+st) if st else ''}.",cty='Brazil',g=g))
ca['x'].sort(key=lambda e:([W1,W2,W3].index(e['g']) if e.get('g') in(W1,W2,W3) else 3,e['n']))
setsel(ca,f"Complete: {len(ca['x'])} entries; every brand row in the three tables of Wikipedia List of Cachaça brands (wide distribution, small batch and artisan, export only), with near-duplicate rows merged. The page flags itself as incomplete and states no owners.")
# Tequila
t=kind('Tequila')
setsel(t,"Complete: all 37 brands named on Wikipedia List of tequilas (read to its end; it states no owners). The page covers only some of the CRT's roughly 2,500 domestic brands; the NOM register is JavaScript-only and is logged for Firecrawl.")
# American single malt
am=kind('American single malt whiskey')
put(am,ent('ASW Distillery','ASW_Distillery','Atlanta distillery of single malt whiskey; the page gives 2016 in its infobox and 2011 in its history.','ASW Distillery','United States',None,None,'',g='Brands'))
put(am,ent("McCarthy's Oregon Single Malt",'McCarthy%27s_Single_Malt','One of the first American single malts introduced after Prohibition, made by Clear Creek Distillery in Oregon.','Clear Creek Distillery','United States',None,None,'',g='Brands'))
setsel(am,"No complete list exists; Wikipedia has no American single malt article and its Single malt whisky article names no US distillery; follows the ASW Distillery and McCarthy's Single Malt pages and the earlier edition.")
# Madrid pago
m=kind('Madrid & Extremadura: denominations of origin')
put(m,{'n':'Pago El Rincón','d':'Vino de Pago of Madrid, named on the Wine With Seth pago system page; the page gives no year.','s':'https://www.winewithseth.com/winewiki/pago-system/','v':[]})
m['sel']=re.sub(r'\s*(Complete|Covers) \d.*$','',m.get('sel','')).rstrip()
m['sel']=(m['sel']+' ' if m['sel'] else '')+f"Complete: {len(m['x'])} of {len(m['x'])} on Wikipedia's Spanish wine regions page (2019) and the Wine With Seth pago system page, including the Madrid pago Pago El Rincón."
# Spain note fix
for kk in ['Navarre: single-estate wines','Castilla-La Mancha: single-estate wines','Aragon: single-estate wines','Valencia: single-estate wines']:
    k=kind(kk);k['sel']=k['sel'].replace(', one of them, Pago El Rincón of Madrid, has no kind here',"; Pago El Rincón of Madrid sits under the Madrid kind")
json.dump(d,open('stageR2.json','w'),ensure_ascii=False)
print(nn,len(c['x']),len(ca['x']))
