import sys,json,urllib.parse
names=json.load(open(sys.argv[1]))
vals=" ".join('"%s"@en'%n.replace('"','') for n in names)
q='''SELECT ?l ?i ?cl ?inc WHERE { VALUES ?l { %s } ?i rdfs:label ?l . ?i wdt:P31/wdt:P279* ?t . VALUES ?t { wd:Q4830453 wd:Q431289 wd:Q167270 wd:Q783794 } OPTIONAL{?i wdt:P495|wdt:P17 ?c . ?c rdfs:label ?cl FILTER(lang(?cl)="en")} OPTIONAL{?i wdt:P571 ?inc} } LIMIT 300'''%vals
print("https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(q))
