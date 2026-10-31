import sys,urllib.parse
ids=sys.argv[1:]
q="""SELECT ?mk ?m (SAMPLE(?t) AS ?title) (MIN(?y) AS ?yr) (GROUP_CONCAT(DISTINCT ?cl;separator="/") AS ?cls) WHERE {VALUES ?mk {%s} ?m wdt:P176 ?mk. ?art schema:about ?m; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?t. OPTIONAL{?m wdt:P571 ?y0 BIND(YEAR(?y0) AS ?y)} OPTIONAL{?m wdt:P31 ?c. ?c rdfs:label ?cl FILTER(LANG(?cl)="en")}} GROUP BY ?mk ?m ORDER BY ?mk ?yr"""%" ".join("wd:"+i for i in ids)
print("https://query.wikidata.org/sparql?format=csv&query="+urllib.parse.quote(q))
