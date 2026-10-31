import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
OW="owner not stated"
def add(kind,rows,src,dtpl):
  k=K[kind]; have={e['n'].lower() for e in k['x']}
  for n,mk,y,cty,own,tier in rows:
    if n.lower() in have: continue
    k['x'].append({"n":n,"a":"","d":dtpl%(y or 'year not stated') if '%s' in dtpl else dtpl,"mk":mk,"y":y,"s":src,"v":[],"g":mk or "Other","own":own,"tier":tier,"cty":cty})
M="https://en.wikipedia.org/wiki/Mechanical_calculator"
rows=[("Schickard's calculating machine","Wilhelm Schickard","1623","Germany"),("Pascaline","Blaise Pascal","1642","France"),("Stepped Reckoner","Gottfried Leibniz","1672","Germany"),("Arithmaurel","Timoleon Maurel","1842","France"),("Baldwin pinwheel calculator","Frank S. Baldwin","1872","United States"),("Grant mechanical calculating machine","George B. Grant","1877","United States"),("Dalton adding machine","Dalton","1902","United States"),("Facit-T","Facit","1932","Sweden"),("Olivetti Divisumma-14","Olivetti","1948","Italy"),("Facit NTK","Facit","1954","Sweden"),("Marchant Figurematic","Marchant","1950","United States"),("Triumphator CRN1","Triumphator","1958","Germany"),("Walther WSR160","Walther","1960","Germany"),("Olivetti Divisumma 24","Olivetti","1964","Italy")]
add("Mechanical calculator",[(n,mk,y,c,OW,"Independent") for n,mk,y,c in rows],M,"Mechanical calculator of %s, named on the Wikipedia article on mechanical calculators.")
S="https://en.wikipedia.org/wiki/Slide_rule"
rows=[("Gunter's rule","Edmund Gunter","1620","United Kingdom"),("Coggeshall slide rule","Henry Coggeshall","1677","United Kingdom"),("Thacher cylindrical slide rule","Edwin Thacher","1881","United States"),("Mannheim rule","Amédée Mannheim","1859","France"),("Fuller cylindrical slide rule","Fuller","1928","United Kingdom"),("Gilson circular slide rule","Gilson","1931","United States"),("Pickett N902-T simplex trig","Pickett","","United States"),("Concise Model 28 circular slide rule","Concise","","Japan"),("Boykin RotaRule Model 510","B. C. Boykin","","United States")]
add("Slide rule",[(n,mk,y,c,OW,"Independent") for n,mk,y,c in rows],S,"Slide rule or related scale of %s, named on the Wikipedia slide rule article.")
R="https://goldspot.com/collections/rhodia-notebooks"
for n,dd in[("Rhodia Webnotebook","Hardcover and softcover journal in dot grid, lined or blank paper."),("Rhodiarama","A5 softcover notebook in several colours."),("Rhodia Goalbook","A5 dot-grid journal with index, numbered pages and undated calendar pages."),("Rhodia Wirebound","Lay-flat wirebound notebooks and pads in lined, dot, graph and blank paper."),("Rhodia Staplebound","Top-stapled numbered notepads in sizes from No. 8 to No. 19.")]:
  K['Notebook']['x'].append({"n":n,"a":"","d":dd,"mk":"Rhodia","y":"","s":R,"v":[],"g":"France","own":"Exacompta Clairefontaine","tier":"Independent","cty":"France"})
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/tmp/c5.tmp',P)
