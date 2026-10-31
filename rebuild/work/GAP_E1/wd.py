import json,urllib.parse,sys
d=json.load(open('rebuild/out/E1.json'))
kinds=sys.argv[1].split('|')
labs=[]
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if k['n'] in kinds:
                for e in k['x']:
                    if not e.get('cty') or e.get('own') in(None,'owner not stated'): labs.append(e['n'])
vals=' '.join('"%s"@en'%l.replace('"','') for l in labs)
q='''SELECT ?l ?i ?desc ?cL ?oL ?inc WHERE { VALUES ?l { %s } ?i rdfs:label ?l . OPTIONAL{?i schema:description ?desc FILTER(lang(?desc)="en")} OPTIONAL{ {?i wdt:P495 ?c} UNION {?i wdt:P17 ?c} UNION {?i wdt:P176/wdt:P17 ?c} } OPTIONAL{ {?i wdt:P127 ?o} UNION {?i wdt:P749 ?o} UNION {?i wdt:P137 ?o} } OPTIONAL{?i wdt:P571 ?inc} ?i wdt:P31 ?t . FILTER(?t != wd:Q4167410) SERVICE wikibase:label {bd:serviceParam wikibase:language "en". ?c rdfs:label ?cL. ?o rdfs:label ?oL.} } LIMIT 400'''%vals
print(len(labs),file=sys.stderr)
print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q))
