import sys, json, urllib.parse
sys.path.insert(0, 'tools')
import run
titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
vals = ' '.join('"%s"@en' % t.replace('"','') for t in titles)
q = """SELECT ?t ?item ?d (GROUP_CONCAT(DISTINCT ?cl;separator="/") AS ?country) (GROUP_CONCAT(DISTINCT ?il;separator="/") AS ?inst) (SAMPLE(?inc) AS ?inception) WHERE {
VALUES ?t { %s }
?a schema:about ?item; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?t.
OPTIONAL { ?item schema:description ?d FILTER(lang(?d)='en') }
OPTIONAL { ?item wdt:P495 ?c. ?c rdfs:label ?cl FILTER(lang(?cl)='en') }
OPTIONAL { ?item wdt:P31 ?i. ?i rdfs:label ?il FILTER(lang(?il)='en') }
OPTIONAL { ?item wdt:P571 ?inc }
} GROUP BY ?t ?item ?d""" % vals
r = json.loads(run.handle_client_tool('J8', '00_00', 'wikidata', {'sparql': q}))
rows = r.get('sparql')
if isinstance(rows, str): print(rows); sys.exit()
found = set()
for row in rows:
    found.add(row.get('t'))
    print(row.get('t'), '|', row.get('item','').rsplit('/',1)[-1], '|', row.get('d',''), '|', row.get('country',''), '|', row.get('inst',''), '|', row.get('inception',''))
print('NOT FOUND:', [t for t in titles if t not in found])
