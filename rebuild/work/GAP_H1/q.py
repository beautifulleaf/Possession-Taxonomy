import json,urllib.parse,sys
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/H1.json'))
names=[]
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if len(k.get('x',[]))>20:
        for e in k['x']:
          if not e.get('own') and e['n'] not in names: names.append(e['n'])
json.dump(names,open('ownerless.json','w'))
i=int(sys.argv[1]); n=int(sys.argv[2])
chunk=names[i:i+n]
vals=' '.join('"%s"@en'%c.replace('"','') for c in chunk)
q='''SELECT ?l (GROUP_CONCAT(DISTINCT ?ol;separator="; ") AS ?o) WHERE { VALUES ?l {%s} ?i rdfs:label ?l. { ?i p:P127 ?st. ?st ps:P127 ?ow } UNION { ?i p:P749 ?st. ?st ps:P749 ?ow } FILTER NOT EXISTS{?st pq:P582 ?e} ?ow rdfs:label ?ol. FILTER(LANG(?ol)="en") } GROUP BY ?l'''%vals
print(len(names)); print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q))
