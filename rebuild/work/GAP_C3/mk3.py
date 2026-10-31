import sys,urllib.parse
def q(s): return 'https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(s,safe='')
print(q('SELECT DISTINCT ?cn ?l WHERE { VALUES ?cn {"apple cultivar"@en "pear cultivar"@en "plum cultivar"@en "cherry cultivar"@en "peach cultivar"@en "apricot cultivar"@en "grape cultivar"@en "wine grape"@en} ?c rdfs:label ?cn. ?sp wdt:P31/wdt:P279* ?c; rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?cn ?l'))
