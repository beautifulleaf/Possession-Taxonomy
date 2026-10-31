import sys,urllib.parse
cls=sys.argv[1].split(','); lim=sys.argv[2]; off=sys.argv[3]
v=" ".join('"%s"@en'%c for c in cls)
q='SELECT ?i ?iLabel ?cl (MIN(YEAR(?d)) AS ?y) (SAMPLE(?coL) AS ?co) WHERE{VALUES ?cl{%s}?c rdfs:label ?cl.?i wdt:P31 ?c.?a schema:about ?i;schema:isPartOf <https://en.wikipedia.org/>.OPTIONAL{?i wdt:P571 ?d}OPTIONAL{?i wdt:P495 ?o.?o rdfs:label ?coL FILTER(lang(?coL)="en")}SERVICE wikibase:label{bd:serviceParam wikibase:language "en"}}GROUP BY ?i ?iLabel ?cl ORDER BY ?cl ?iLabel LIMIT %s OFFSET %s'%(v,lim,off)
print("https://query.wikidata.org/sparql?format=csv&query="+urllib.parse.quote(q,safe=""))
