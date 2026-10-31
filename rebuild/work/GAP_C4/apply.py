import json,re,os,collections
from urllib.parse import urlparse
P='out/C4.json'
d=json.load(open(P))
OW={ # mk: (own, tier, own_y)
 'Daler-Rowney':('F.I.L.A. S.p.A.','Global group','2016'),
 'Arches':('F.I.L.A. S.p.A.','Global group','2019'),
 'St Cuthberts Mill':('F.I.L.A. S.p.A.','Global group','2016'),
 'Strathmore':('F.I.L.A. S.p.A.','Global group','2018'),
 'Lyra':('F.I.L.A. S.p.A.','Global group','2008'),
 'Royal Talens':('Sakura Color Products Corporation','Independent','1991'),
 'Faber-Castell':('Faber-Castell AG','Independent',''),
 'Staedtler':('Staedtler SE','Independent',''),
 'Janome':('Janome Corporation','Independent',''),
 'Bernina':('Bernina International','Independent',''),
 'DMC':('Lion Capital','Independent','2019'),
 'Brother':('Brother Industries','Independent',''),
 'Tamiya':('Tamiya Corporation','Independent',''),
}
nown=0;ng=0;nsel=0
def hosts(k):
    c=collections.Counter(urlparse(e.get('s','')).netloc.replace('www.','') for e in k['x'] if e.get('s'))
    return [h for h,_ in c.most_common(3) if h]
for dp in d['depts']:
 for sh in dp['s']:
  for k in sh['k']:
   if not k.get('x'): continue
   sel=k.get('sel','')
   if not re.search(r'(Complete:|Covers |No complete list)',sel):
     n=k['n']
     if n=='Yarn weight class': add=" Complete: 8 of 8 in Wikipedia's Yarn article (Craft Yarn Council classes 0 to 7)."
     elif n=="Artists' pigment": add=" Covers every row of Wikipedia's List of inorganic pigments but only part of the organic pigments in the Colour Index; no free complete list of organic generic names was found by search or Wikidata (class query returned 0 rows)."
     else:
       h=hosts(k)
       add=" No complete list exists; follows "+(", ".join(h) if h else "the makers' own pages")+" and the makers' ranges cited on each entry."
     k['sel']=(sel.rstrip()+add).strip(); nsel+=1
   for e in k['x']:
     if k.get('xg') and not e.get('g'):
       e['g']=e.get('cty') or 'Country not stated'; ng+=1
     mk=e.get('mk')
     if mk in OW and not e.get('own'):
       o,t,y=OW[mk]; e['own']=o; e['tier']=t
       if y: e['own_y']=y
       nown+=1
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
B='out/C4_brands.json'
b=json.load(open(B)); key=list(b)[0]; L=b[key]; names={x['n'] for x in L}
new=[('F.I.L.A. S.p.A.','Italy','Italian art and stationery group (Milan); owns Lyra, Daler-Rowney, Canson, Arches, Strathmore and Princeton.','https://en.wikipedia.org/wiki/F.I.L.A._(company)'),
 ('Sakura Color Products Corporation','','Privately owned Osaka firm; owns Royal Talens since 1991.','https://en.wikipedia.org/wiki/Royal_Talens'),
 ('Lion Capital','United Kingdom','British investment firm; bought DMC in February 2019.','https://en.wikipedia.org/wiki/DMC_(company)')]
for n,c,dd,s in new:
  if n not in names: L.append({"n":n,"c":c,"f":"","seg":"Mainstream","kf":"brand group","d":dd,"s":s,"sig":[]})
json.dump(b,open(B+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(B+'.tmp',B)
print(nsel,ng,nown)
