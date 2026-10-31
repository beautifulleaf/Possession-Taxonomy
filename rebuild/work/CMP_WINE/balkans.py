import sys,copy; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
SRC='https://sommgeo.com/launchsommgeo/sommgeo-fast-maps/central-and-eastern-europe-fast-map/'
d=load()
def newkind(dp,tmpl,name,dsc,ref,cnt,tot):
    s,k=findkind(dp,tmpl)
    nk=findkind(dp,name)
    if nk: return nk[1]
    nk=copy.deepcopy(k); nk['n']=name; nk['d']=dsc; nk['x']=[]
    nk['nl']=f'One entry is a protected designation of origin (PDO) for wine in {ref}.'
    nk['sel']=''
    s['k'].append(nk); return nk
ee=dept(d,'Wine of Eastern Europe'); bk=dept(d,'Wine of the Balkans'); hc=dept(d,'Wine of Hungary & Central Europe')
# Romania
nm=allnames(ee)
sk,k=findkind(ee,'Romania: wine regions and vineyards')
for n in ['Adamclisi','Însurăței']:
    print(add(ee,k['n'],{'n':n,'d':'DOC appellation (controlled designation of origin) for still wine in Romania.','s':SRC},nm))
cover(k,'Complete: all 33 Romanian PDO (DOC) names of the Sommgeo Eastern Europe table are present, as entries or marked as DOC.')
# Bulgaria
bul="Asenovgrad;Bolyarovo;Brestnik;Chernomorski rayon;Dolinata na Struma;Dragoevo;Euxinograd;Harsovo;Haskovo;Hisarya;Ivaylovgrad;Karlovo;Karnobat;Khan Krum;Lom;Lovech;Lozitsa;Lyaskovets;Lyubimets;Melnik;Montana;Nova Zagora;Novi Pazar;Novo Selo;Oryahovitsa;Pavlikeni;Pazardzhik;Perushtitsa;Pleven;Plovdiv;Pomorie;Ruse;Sakar;Sandanski;Septemvri;Shivachevo;Shumen;Slavyantsi;Sliven;Stambolovo;Stara Zagora;Suhindol;Sungurlare;Svishtov;Targovishte;Varbitsa;Varna;Veliki Preslav;Vidin;Vratsa;Yambol;Yuzhno Chernomorie".split(';')
assert len(bul)==52
kb=newkind(ee,'Bulgaria: wine regions','Bulgaria: PDO wine areas','Bulgarian wine areas with a protected designation of origin.','Bulgaria',52,52)
nm=allnames(ee)
for n in bul: add(ee,kb['n'],{'n':n,'d':'Bulgarian wine PDO area.','s':SRC},nm)
cover(kb,'Complete: 52 of 52 Bulgarian PDOs in the Sommgeo Eastern Europe table; many are not in use.')
cover(findkind(ee,'Bulgaria: wine regions')[1],'The five viticultural regions are broad zones; the 52 PDO areas are in the next kind.')
# Slovenia
slo={"Bela krajina":"Bela krajina (White Carniola)","Belokranjec":None,"Bizeljčan":None,"Bizeljsko Sremič":"Bizeljsko-Sremič","Cviček":None,"Dolenjska":"Dolenjska (Lower Carniola)","Goriška Brda":"Goriška Brda","Kras":"Kras","Metliška črnina":None,"Prekmurje":"Prekmurje","Slovenska Istra":None,"Štajerska Slovenija":None,"Teran":None,"Vipavska dolina":"Vipava Valley"}
nm=allnames(bk)
ks=newkind(bk,'Slovenia: wine districts','Slovenia: PDO wine names','Slovenian wine names with a protected designation of origin that are not wine districts.','Slovenia',14,14)
for n,a in slo.items():
    if a: assert norm(a) in nm,(a)
    else: print(add(bk,ks['n'],{'n':n,'d':'Slovenian wine PDO name.','s':SRC},nm))
cover(ks,'Complete: all 14 Slovenian PDOs of the Sommgeo Eastern Europe table; the 8 that match a wine district (Bela krajina, Bizeljsko Sremič, Dolenjska, Goriška Brda, Kras, Prekmurje, Vipavska dolina) are listed in the districts kind.')
# Croatia
cro={"Dalmatinska zagora":"Dalmatian interior","Dingač":"Dingač","Hrvatska Istra":"Istria","Hrvatsko Podunavlje":"Podunavlje","Hrvatsko primorje":"Hrvatsko Primorje","Istočna kontinentalna Hrvatska":None,"Moslavina":"Moslavina","Muškat momjanski":None,"Plešivica":"Plešivica","Pokuplje":"Pokuplje","Ponikve":None,"Prigorje-Bilogora":"Prigorje-Bilogorje","Primorska Hrvatska":None,"Sjeverna Dalmacija":"Northern Dalmatia","Slavonija":"Slavonija","Srednja i Južna Dalmacija":"Central and South Dalmatia","Zagorje – Međimurje":"Zagorje-Međimurje","Zapadna kontinentalna Hrvatska":None}
nm=allnames(bk)
kc=newkind(bk,'Croatia: wine sub-regions','Croatia: PDO wine names','Croatian wine names with a protected designation of origin that are not already sub-regions.','Croatia',18,18)
for n,a in cro.items():
    if a and norm(a) in nm: continue
    if a: print('nomatch',n)
    else: print(add(bk,kc['n'],{'n':n,'d':'Croatian wine PDO name.','s':SRC},nm))
cover(kc,'Complete: all 18 Croatian PDOs of the Sommgeo Eastern Europe table; those that match a sub-region or Dingač are in the sub-regions kind.')
# Czech
cz=["Čechy","Morava","Novosedelské Slámové víno","Šobes","Znojmo"]
nm=allnames(hc)
kz=newkind(hc,'Czechia: wine sub-regions','Czechia: PDO wine names','Czech wine names with a protected designation of origin that are not sub-regions.','Czechia',11,11)
for n in cz: print(add(hc,kz['n'],{'n':n,'d':'Czech wine PDO name.','s':SRC},nm))
cover(kz,'Complete: all 11 Czech PDOs of the Sommgeo Eastern Europe table; the six sub-regions (Litoměřická, Mělnická, Mikulovská, Slovácká, Velkopavlovická, Znojemská) are in the sub-regions kind. Municipalities in decree 254/2010 were not fetched.')
save(d)
