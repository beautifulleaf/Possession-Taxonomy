import json,urllib.parse
def U(ns):
    v="".join('"%s"@en '%n for n in ns)
    q='SELECT ?l ?i (GROUP_CONCAT(DISTINCT ?ql;separator=",") AS ?p) WHERE{VALUES ?l{%s}?i rdfs:label ?l;wdt:P31/wdt:P279* wd:Q4886 .OPTIONAL{?i wdt:P171|wdt:P279|wdt:P1420 ?q.?q rdfs:label ?ql FILTER(lang(?ql)="en")}}GROUP BY ?l ?i'%v
    return "https://query.wikidata.org/sparql?format=csv&query="+urllib.parse.quote(q,safe="")
names=json.load(open('names.json'))
new=[];cur=[]
for n in names:
    if len(U(cur+[n]))>1950: new.append(cur);cur=[]
    cur.append(n)
new.append(cur)
for i,c in enumerate(new): open('v%d.txt'%i,'w').write(U(c))
json.dump(new,open('chunks.json','w'));print(len(new),[len(c) for c in new])
