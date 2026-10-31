import urllib.parse,sys
cs=sys.argv[1]; ex=sys.argv[2]
s='''SELECT ?mkl ?xl (MIN(COALESCE(YEAR(?inc),YEAR(?pub))) AS ?y) (SAMPLE(?an) AS ?art) WHERE { VALUES ?co {%s} ?mk wdt:P17 ?co. ?x wdt:P176 ?mk; wdt:P31/wdt:P279* wd:Q3231690; rdfs:label ?xl. ?mk rdfs:label ?mkl. FILTER(LANG(?xl)="en"&&LANG(?mkl)="en"&&!REGEX(?mkl,"%s")) ?a schema:about ?x; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?an. OPTIONAL{?x wdt:P571 ?inc} OPTIONAL{?x wdt:P577 ?pub} } GROUP BY ?mkl ?xl ORDER BY ?mkl ?y'''%(cs,ex)
print('https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(s,safe=''))
