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
q='''SELECT ?l ?i ?desc ?cL ?oL ?inc WHERE { VALUES ?l { %s } ?i rdfs:label ?l . OPTIONAL{?i schema:description ?desc FILTER(lang(?desc)="en")} OPTIONAL{ {?i wdt:P495 ?c} UNION {?i wdt:P17 ?c} UNION {?i wdt:P176/wdt:P17 ?c} } OPTIONAL{ {?i wdt:P127 ?o} UNION {?i wdt:P749 ?o} UNION {?i wdt:P137 ?o} } OPTIONAL{?i wdt:P571 ?inc} SERVICE wikibase:label {bd:serviceParam wikibase:language "en". ?c rdfs:label ?cL. ?o rdfs:label ?oL.} } LIMIT 400'''%vals
print(len(labs),len(ch),file=sys.stderr)
print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q))
