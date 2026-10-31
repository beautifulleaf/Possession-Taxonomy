import urllib.parse as u,sys
off=int(sys.argv[1]);lim=int(sys.argv[2])
q='''SELECT ?mkL (COUNT(DISTINCT ?m) AS ?n) (GROUP_CONCAT(DISTINCT CONCAT(?t,"~",COALESCE(STR(?y),"")); separator="; ") AS ?l) WHERE {
 ?m wdt:P31/wdt:P279* wd:Q3231690 .
 ?a schema:about ?m ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t .
 OPTIONAL{?m wdt:P1716 ?b} OPTIONAL{?m wdt:P176 ?f}
 BIND(COALESCE(?b,?f) AS ?mk)
 ?mk rdfs:label ?mkL . FILTER(LANG(?mkL)="en")
 OPTIONAL{?m wdt:P571 ?d} BIND(YEAR(?d) AS ?y)
} GROUP BY ?mkL ORDER BY ?mkL LIMIT %d OFFSET %d'''%(lim,off)
print('https://query.wikidata.org/sparql?format=json&query='+u.quote(q,safe='/'))
