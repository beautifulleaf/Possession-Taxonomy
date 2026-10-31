import urllib.parse as u,sys
names=sys.argv[1].split('|')
vals=' '.join('"%s"@en'%n for n in names)
q='''SELECT ?mkL ?t (MIN(?y) AS ?yr) WHERE {
 VALUES ?mkL { %s }
 ?mk rdfs:label ?mkL .
 ?m wdt:P31 wd:Q3231690 ; wdt:P1716|wdt:P176 ?mk .
 ?a schema:about ?m ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t .
 OPTIONAL{?m wdt:P571 ?d} BIND(YEAR(?d) AS ?y)
 FILTER NOT EXISTS {?m wdt:P279 wd:Q850270}
} GROUP BY ?mkL ?t ORDER BY ?mkL ?t'''%vals
print('https://query.wikidata.org/sparql?format=csv&query='+u.quote(q,safe='/'))
