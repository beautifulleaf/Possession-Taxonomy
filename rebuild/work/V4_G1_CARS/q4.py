import urllib.parse as u,sys
off=int(sys.argv[1]);lim=int(sys.argv[2])
q='''SELECT ?mkL ?t (MIN(?y) AS ?yr) (SAMPLE(?cL) AS ?cls) WHERE {
 ?m wdt:P31 wd:Q3231690 ; wdt:P1716|wdt:P176 ?mk .
 ?a schema:about ?m ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t .
 ?mk rdfs:label ?mkL . FILTER(LANG(?mkL)="en")
 OPTIONAL{?m wdt:P571 ?d} BIND(YEAR(?d) AS ?y)
 OPTIONAL{?m wdt:P279 ?c . ?c rdfs:label ?cL . FILTER(LANG(?cL)="en")}
} GROUP BY ?mkL ?t ORDER BY ?mkL ?t LIMIT %d OFFSET %d'''%(lim,off)
print('https://query.wikidata.org/sparql?format=csv&query='+u.quote(q,safe='/'))
