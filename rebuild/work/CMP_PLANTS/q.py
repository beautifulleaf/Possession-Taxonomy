import json,sys,re,urllib.parse
def clean(n):
    n=re.sub(r'\s*\[.*?\]','',n)
    n=re.sub(r'\s*\((.*?)\)',lambda m:'',n).strip()
    n=re.sub(r'\s+(PDO|PGI|AOP|AOC|GI|IG|DO|IP|TSG)$','',n).strip()
    return n
LANGS=['en','fr','de','it','es','pt','ja','zh','ko','nl','pl','el','hu','cs','sl','hr','mul']
def url(names,langs=('en','fr','de','it','es')):
    vals=" ".join('"%s"@%s'%(n.replace('"','\\"'),l) for n in names for l in langs)
    q='''SELECT ?i ?l (GROUP_CONCAT(DISTINCT ?cl;separator="|") AS ?cls) (GROUP_CONCAT(DISTINCT ?pl;separator="|") AS ?par) WHERE { VALUES ?l { %s } ?i rdfs:label ?l . {?i wdt:P31/wdt:P279* wd:Q4886} . OPTIONAL{?i wdt:P31 ?c. ?c rdfs:label ?cl FILTER(lang(?cl)="en")} OPTIONAL{?i wdt:P171|wdt:P279|wdt:P1420 ?p. ?p rdfs:label ?pl FILTER(lang(?pl)="en")} } GROUP BY ?i ?l'''%vals
    return "https://query.wikidata.org/sparql?format=csv&query="+urllib.parse.quote(q,safe="")
if __name__=='__main__':
    r=json.load(open('../V4_J4/removed_m.json'))
    k=sys.argv[1]
    names=sorted({clean(a) for a,b in r[k]['m'] if clean(a)})
    print(url(names))
