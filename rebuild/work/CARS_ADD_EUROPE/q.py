import json,urllib.parse,sys
def q(labels):
    vals=' '.join('"%s"@en'%l for l in labels)
    s='''SELECT ?mkl ?xl (MIN(YEAR(?inc)) AS ?y) (GROUP_CONCAT(DISTINCT ?cl;separator=",") AS ?cls) (SAMPLE(?an) AS ?art) WHERE { VALUES ?mkl {%s} ?mk rdfs:label ?mkl. ?x wdt:P176 ?mk; wdt:P31/wdt:P279* wd:Q3231690; rdfs:label ?xl. FILTER(LANG(?xl)="en") ?a schema:about ?x; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?an. OPTIONAL{?x wdt:P571 ?inc} OPTIONAL{?x wdt:P279 ?c. ?c rdfs:label ?cl. FILTER(LANG(?cl)="en")} } GROUP BY ?mkl ?xl ORDER BY ?mkl ?y'''%vals
    return 'https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(s,safe='')
print(q(sys.argv[1].split('|')))
