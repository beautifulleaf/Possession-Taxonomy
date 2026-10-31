import json,re,os,unicodedata
from urllib.parse import urlparse
P='/home/user/Possession-Taxonomy/rebuild/out/F6.json'
d=json.load(open(P))
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=s.replace('northwest africa','nwa').replace('canon diablo','canyon diablo')
    return re.sub(r'[^a-z0-9]','',s)
W='https://en.wikipedia.org/wiki/'
def ent(n,y,d_,s,a=''): return {'n':n,'a':a,'d':d_,'mk':'','y':y,'s':s,'v':[],'dt':''}
mars=open('mars.txt').read().split('\n'); 
adds={}
# Martian
M=[]
for ln in mars:
    if '|' not in ln: continue
    n,y=[p.strip() for p in ln.split('|')[:2]]
    M.append(ent(n,'found '+y if y else '', 'Meteorite classified as Martian, listed in the Wikipedia list of Martian meteorites.',W+'List_of_Martian_meteorites'))
adds['Martian meteorite']=(M,"Covers %d of 277 classified Martian meteorites in List of Martian meteorites (Wikipedia, which says its table is incomplete); the rest are unlisted there and no fetched page lists them all.")
L=[]
for ln in open('luna.txt').read().split('\n'):
    m=re.match(r'(.+?) \((.+)\)$',ln.strip())
    if m: L.append(ent(m.group(1),'found '+m.group(2),'Lunar meteorite, listed in the Wikipedia list of lunar meteorites (row may group several paired stones).',W+'List_of_lunar_meteorites'))
adds['Lunar meteorite']=(L,"Covers %d named rows of List of lunar meteorites (Wikipedia, which calls itself incomplete); unnamed rows and meteorites not on that page are left out.")
def mk(lst,src,txt):
    return [ent(n,y,txt.format(n=n,g=g),W+src) for n,y,g in lst]
adds['Pallasite']=(mk([('Mineo','fell 1826','Italy'),('Zaisho','found 1898','Japan'),('Marjalahti','recovered 1902','Karelia, Russia'),('Omolon','fell 1981','Magadan Region, Russia'),('Huckitta','found 1937','Australia'),('Brahin','known since 1810','Belarus'),('Pallasovka','found 1990','Russia'),('Krasnojarsk','detected 1749','Russia'),('Hambleton','found 2005','North Yorkshire, United Kingdom'),('Glorieta Mountain','','New Mexico, United States'),('Eagle Station','','type specimen of the Eagle Station group'),('Vermillion','','pyroxene pallasite grouplet'),('Yamato 8451','','pyroxene pallasite')],'Pallasite','Pallasite named by the Wikipedia article ({g}).'),"Covers %d of the pallasites named in Wikipedia's Pallasite article; the Meteoritical Bulletin lists many more and was not fetched.")
adds['Mesosiderite']=(mk([('Chinguetti','','not stated'),('Dong Ujimqin Qi','1995','China'),('Barea','1842','Spain'),('Varamin','1880','Iran'),('Dyarrl Island','1933','Papua New Guinea'),('Patwar','1935','India')],'Mesosiderite','Mesosiderite named by the Wikipedia article ({g}).'),"Covers %d of the mesosiderites named in Wikipedia's Mesosiderite article, which is not a full list.")
adds['Iron meteorite']=(mk([('Tamentit','found 1864','Sahara'),('Hoba','','Namibia'),('Willamette','','United States'),('Bendegó','found 1784','Brazil'),('Otumpa','found 1783','Chaco, Argentina'),('Chinga','','group IVB'),('Murnpeowie','discovered 1910','South Australia'),('Cape York','','Greenland'),('Hraschina','','named in the article')],'Iron_meteorite','Iron meteorite named by the Wikipedia article ({g}).'),"Covers %d of the iron meteorites named in Wikipedia's Iron meteorite article, which is not a full list.")
adds['Carbonaceous chondrite']=(mk([(n,'',g) for n,g in [('Ivuna','CI'),('Orgueil','CI'),('Alais','CI'),('Tonk','CI'),('Revelstoke','CI'),('Bali','CV'),('Bukhara','CV'),('Grosnaja','CV'),('Kaba','CV'),('Mokoia','CV'),('Vigarano','CV'),('NWA 3118','CV'),("Sutter's Mill",'CM'),('Aguas Zarcas','CM'),('Jbilet Winselwan','CM'),('Winchcombe','CM'),('Mighei','CM'),('Renazzo','CR'),('Al Rais','CR'),('Dar al Gani 574','CR'),('El Djouf 001','CR'),('Northwest Africa 801','CR'),('ALH 85085','CH'),('Bencubbin','CB'),('Gujba','CB'),('Karoonda','CK'),('Ornans','CO'),('Kainsaz','CO'),('Warrenton','CO'),('Moss','CO'),('Dar al Gani 749','CO'),('Loongana','CL'),('Tagish Lake','ungrouped'),('Tarda','ungrouped'),('Flensburg','')]] and [(n,'2019' if n=='Flensburg' else '',g) for n,g in [('Ivuna','CI'),('Orgueil','CI'),('Alais','CI'),('Tonk','CI'),('Revelstoke','CI'),('Bali','CV'),('Bukhara','CV'),('Grosnaja','CV'),('Kaba','CV'),('Mokoia','CV'),('Vigarano','CV'),('NWA 3118','CV'),("Sutter's Mill",'CM'),('Aguas Zarcas','CM'),('Jbilet Winselwan','CM'),('Winchcombe','CM'),('Mighei','CM'),('Renazzo','CR'),('Al Rais','CR'),('Dar al Gani 574','CR'),('El Djouf 001','CR'),('Northwest Africa 801','CR'),('ALH 85085','CH'),('Bencubbin','CB'),('Gujba','CB'),('Karoonda','CK'),('Ornans','CO'),('Kainsaz','CO'),('Warrenton','CO'),('Moss','CO'),('Dar al Gani 749','CO'),('Loongana','CL'),('Tagish Lake','ungrouped'),('Tarda','ungrouped'),('Flensburg','ungrouped')]],'Carbonaceous_chondrite','Carbonaceous chondrite of group {g}, named by the Wikipedia article.'),"Covers %d of the carbonaceous chondrites named in Wikipedia's Carbonaceous chondrite article, which is not a full list.")
adds['HED meteorite']=(mk([('NWA 2698','','howardite'),('Bilanga','','diogenite'),('QUE 94200','','howardite'),('Johnstown','','diogenite')],'HED_meteorite','HED meteorite ({g}) named by the Wikipedia article.'),"Covers %d of the HED meteorites named in Wikipedia's HED meteorite article, which is not a full list.")
adds['Asteroidal achondrite']=(mk([('Cumberland Falls','','aubrite'),('Acapulco','','acapulcoite, Mexico'),('Lodran','','lodranite'),('Winona','','winonaite')],'Achondrite','Achondrite ({g}) named by the Wikipedia article.'),"Covers %d added from Wikipedia's Achondrite article, which names examples only.")
adds['Tektite']=([ent('Ivorite','about 1 million years','Black tektite of the Ivory Coast strewn field, linked to the Lake Bosumtwi impact.',W+'Tektite')],"Covers all %d named tektite types in Wikipedia's Tektite article (australite, indochinite, philippinite, moldavite, ivorite, bediasite, georgiaite).")
adds['Impact glass']=([ent('Kärnäite','','Impact glass from the Lappajärvi crater, Finland.',W+'Impact_glass')],"Covers %d added from Wikipedia's Impact glass article, which names examples only.")
HOST={'en.wikipedia.org':'Wikipedia','www.handbookofmineralogy.org':'the Handbook of Mineralogy','www.minerals.net':'minerals.net','www.fossilera.com':'Fossilera','www.gia.edu':'GIA','www.mindat.org':'Mindat','luciteria.com':'Luciteria','geology.com':'geology.com'}
cnt=0;ext=0
for dp in d['depts']:
  for sh in dp.get('s',[]):
    for k in sh.get('k',[]):
      x=k.get('x')
      if not x: continue
      sel=k.get('sel','')
      sel=re.sub(r'\s*Complete: .*$|\s*Covers .*$|\s*No complete list exists;.*$','',sel).strip() if False else sel
      if k['n'] in adds:
        new,line=adds[k['n']]
        have={norm(e['n']) for e in x}
        for e in x: have|={norm(a) for a in e.get('a','').split('·') if a.strip()}
        c=0
        for e in new:
            if norm(e['n']) in have: continue
            x.append(e);have.add(norm(e['n']));c+=1
        tot=len(x)
        k['sel']=sel+' '+(line%tot)
        ext+=c
      else:
        hosts=[]
        for e in x:
            for u in [e.get('s','')]+[v.get('s','') for v in e.get('v',[])]:
                h=urlparse(u).netloc if u else ''
                if h: hosts.append(HOST.get(h,h.replace('www.','')))
        hs=[]
        for h in hosts:
            if h not in hs: hs.append(h)
        if k.get('s'):
            h=urlparse(k['s']).netloc
            h=HOST.get(h,h.replace('www.',''))
            if h not in hs: hs.append(h)
        k['sel']=sel+' No complete list exists; follows '+(', '.join(hs) if hs else 'collector overviews')+'.'
      cnt+=1
print(cnt,ext)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'.tmp',P)
