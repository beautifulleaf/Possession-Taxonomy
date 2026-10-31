import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
d=load(); dp=dept(d,'Wine of the Balkans') if False else dept(d,'Wine of Eastern Europe')
SRC='https://winebrotherhoods.org/en/brotherhoods/romania-brotherhood/'
doc="Târnave;Alba Iulia;Sebeş-Apold;Aiud;Lechinţa;Cotnari;Iaşi;Bohotin;Huşi;Iana;Dealu Bujorului;Nicoreşti;Panciu;Odobeşti;Coteşti;Cernăteşti-Podgoria;Dealu Mare;Pietroasa;Ştefăneşti;Sâmbureşti;Drăgăşani;Banu Mărăcine;Segarcea;Mehedinţi;Recaş;Banat;Miniş;Crişana;Murfatlar;Babadag;Sarica Niculiţel;Oltina".split(';')
alias={'Alba Iulia':'Alba','Babadag':'Istria-Babadag','Miniş':'Miniș-Măderat','Cernăteşti-Podgoria':None,'Mehedinţi':None}
spark={'Târnave','Alba Iulia','Sebeş-Apold','Iaşi','Bucium','Huşi','Panciu','Dealu Mare','Şimleul Silvaniei','Murfatlar'}
sk,k=findkind(dp,'Romania: wine regions and vineyards')
byn={norm(e['n']):e for e in k['x']}
nm=allnames(dp); added=[];marked=[]
for n in doc:
    a=alias.get(n,n) or n
    key=norm(a)
    if n in('Banat','Crişana'): key=None
    e=byn.get(key) if key else None
    if e:
        if 'DOC' not in e['d']: e['d']=e['d'].rstrip()+' It is also a DOC appellation.'
        marked.append(n)
    else:
        nn=n+' (DOC)' if n in('Banat','Crişana') else n
        add(dp,k['n'],{'n':nn,'d':'DOC appellation (controlled designation of origin) for still wine in Romania'+('; also made as DOC sparkling wine.' if n in spark else '.'),'s':SRC},nm); added.append(nn)
print('marked',marked);print('added',added)
for n in spark:
    e=byn.get(norm(alias.get(n,n)))
    if e and 'sparkling' not in e['d']: e['d']=e['d'].rstrip()+' DOC sparkling wine is also made here.'
ig=["Hills of Transilvania","Hills of Moldova","Hills of Vrancea","Hills of Muntenia","Hills of Oltenia","Vineyards of Caraş","Vineyards of Timiş","Hills of Zarand","Hills of Crişana","Hills of Sătmar","Colinele Dobrogei","Terraces of the Danube"]
sk2,k2=findkind(dp,'Romania: IGP wine regions')
for n in ig: print(add(dp,k2['n'],{'n':n,'d':'Geographical indication (IG/IGP) for still wine in Romania.','s':SRC},nm))
cover(k,'Covers the 32 DOC names (and 10 DOC sparkling names) of the Romanian wine brotherhood list; Romania is cited as having 33 DOC elsewhere, and one name is missing from this list. Vineyard entries not on the DOC list are kept from earlier Wikipedia and ministry sources.')
cover(k2,'Covers 16 of the 12 IG names on the brotherhood list plus the four older regional names (Banat, Dobrogea, Muntenia, Transylvania) from Wikipedia, which the brotherhood list does not use.')
save(d)
