import json,urllib.parse,sys
d=json.load(open('rebuild/out/E1.json'))
skip=set(sys.argv[1].split('|'))  # kinds to skip
idx=int(sys.argv[2]); size=int(sys.argv[3])
labs=[]
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if k['n'] in skip: continue
            for e in k.get('x') or []:
                if not e.get('cty') or e.get('own') in(None,'owner not stated'): labs.append(e['n'])
labs=[l for l in dict.fromkeys(labs) if all(ord(c)<128 and c not in "'\"" for c in l)]
ch=labs[idx*size:(idx+1)*size]
vals=' '.join('"%s"@en'%l.replace('"','') for l in ch)
q='''SELECT ?l ?i (SAMPLE(?desc) AS ?ds) (SAMPLE(?cL) AS ?c) (SAMPLE(?oL) AS ?o) (SAMPLE(?inc) AS ?y) WHERE { VALUES ?l { %s } ?i rdfs:label ?l . ?i wdt:P31 ?t . OPTIONAL{?i schema:description ?desc FILTER(lang(?desc)="en")} OPTIONAL{ {?i wdt:P495 ?cc} UNION {?i wdt:P17 ?cc} UNION {?i wdt:P176/wdt:P17 ?cc} ?cc rdfs:label ?cL FILTER(lang(?cL)="en")} OPTIONAL{ {?i wdt:P127 ?oo} UNION {?i wdt:P749 ?oo} UNION {?i wdt:P137 ?oo} ?oo rdfs:label ?oL FILTER(lang(?oL)="en")} OPTIONAL{?i wdt:P571 ?inc} } GROUP BY ?l ?i LIMIT 500'''%vals
print(len(labs),len(ch),file=sys.stderr)
print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q))
