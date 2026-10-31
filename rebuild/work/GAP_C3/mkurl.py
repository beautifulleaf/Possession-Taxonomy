import sys,urllib.parse
for g in sys.argv[1:]:
    q='SELECT DISTINCT ?l WHERE { ?g wdt:P225 "%s"; wdt:P105 wd:Q34740. ?sp wdt:P171+ ?g; wdt:P105 wd:Q7432; rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?l'%g
    print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q,safe=''))
