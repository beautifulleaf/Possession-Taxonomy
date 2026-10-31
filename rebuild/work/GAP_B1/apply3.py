import json,os,urllib.parse
P='rebuild/out/B1.json'; PB='rebuild/out/B1_brands.json'
d=json.load(open(P)); bd=json.load(open(PB))
Q='SELECT DISTINCT ?iLabel ?mLabel ?y WHERE {?i wdt:P31/wdt:P279* wd:Q14745. ?i wdt:P176 ?m. OPTIONAL{?i wdt:P571 ?t. BIND(YEAR(?t) AS ?y)} SERVICE wikibase:label {bd:serviceParam wikibase:language "en"}} ORDER BY ?iLabel LIMIT 200'
U='https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(Q)
R=[('Stool','Allunaggio chair','Zanotta','1966'),('Moulded, shell & bentwood lounge chair','La Chaise','Vitra','1948'),('Sofa','Bocca sofa','Gufram',''),('Bookcase','Bookworm','Kartell',''),('Desk','Theodore Roosevelt desk','A. H. Davenport and Company','1903'),('Dining chair','S chair','Cappellini','1991'),('Modular shelving system','Deutsche Werkstätten furniture programme','Deutsche Werkstätten Hellerau','1967')]
kinds={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
have={e['n'].lower() for k in kinds.values() for e in k.get('x',[])}
for kn,n,mk,y in R:
    if n.lower() in have: continue
    k=kinds[kn]
    e={"n":n,"a":"","d":f"Furniture piece made by {mk}"+(f", {y}" if y else "")+"; listed in Wikidata with its maker.","mk":mk,"y":y,"s":U,"v":[],"g":(y[:3]+'0s') if y else 'Undated'}
    k['x'].append(e)
    if all(x.get('g') for x in k['x']): k['x']=sorted(k['x'],key=lambda x:x['g']=='Undated')
names={x['n'] for x in bd['b']}
for mk in ['Zanotta','Gufram','A. H. Davenport and Company','Cappellini','Deutsche Werkstätten Hellerau']:
    if mk not in names and mk!='Cappellini S.p.A.': bd['b'].append({'n':mk,'c':'','seg':'Premium','d':'Maker of a furniture piece listed in Wikidata.','s':U,'kf':'furniture'})
for p,o in ((P,d),(PB,bd)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
