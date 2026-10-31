import sys,urllib.parse
cl=sys.argv[1]; lim=sys.argv[2] if len(sys.argv)>2 else '300'; off=sys.argv[3] if len(sys.argv)>3 else '0'
q='SELECT ?i ?iLabel (MIN(YEAR(?d)) AS ?y) (SAMPLE(?coL) AS ?co) WHERE{?c rdfs:label "%s"@en.?i wdt:P31 ?c.?a schema:about ?i;schema:isPartOf <https://en.wikipedia.org/>.OPTIONAL{?i wdt:P571 ?d}OPTIONAL{?i wdt:P495 ?o.?o rdfs:label ?coL FILTER(lang(?coL)="en")}SERVICE wikibase:label{bd:serviceParam wikibase:language "en"}}GROUP BY ?i ?iLabel ORDER BY ?iLabel LIMIT %s OFFSET %s'%(cl,lim,off)
print("https://query.wikidata.org/sparql?format=csv&query="+urllib.parse.quote(q,safe=""))
