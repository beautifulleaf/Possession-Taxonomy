import urllib.parse as u,sys
names=sys.argv[1].split('|')
vals=' '.join('"%s"@en'%n for n in names)
q='''SELECT DISTINCT ?t ?mkL ?y ?y2 WHERE {
 VALUES ?mkL { %s }
 ?mk rdfs:label ?mkL .
 ?m wdt:P31 wd:Q3231690 ; wdt:P1716|wdt:P176 ?mk .
 ?a schema:about ?m ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t .
 OPTIONAL{?m wdt:P571 ?d} OPTIONAL{?m wdt:P729 ?e} OPTIONAL{?m wdt:P577 ?f}
 BIND(YEAR(COALESCE(?d,?e,?f)) AS ?y)
 OPTIONAL{?m wdt:P730 ?e2} BIND(YEAR(?e2) AS ?y2)
} ORDER BY ?t'''%vals
print('https://query.wikidata.org/sparql?format=csv&query='+u.quote(q,safe='/'))
