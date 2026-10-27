import sys, subprocess, json
sys.path.insert(0,'.')
from titles import T
for job in sys.argv[1:]:
    vals = ' '.join(json.dumps(t, ensure_ascii=False)+'@en' for t in T[job])
    q = ('SELECT ?item ?title ?article ?desc ?inc WHERE { VALUES ?title { '+vals+' } ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?title . '
         'OPTIONAL { ?item schema:description ?desc FILTER(lang(?desc)="en") } OPTIONAL { ?item wdt:P571 ?inc } }')
    out = subprocess.run(['python3','tools/local.py','wd','F3',job,'sparql',q],capture_output=True,text=True,cwd='/home/user/Possession-Taxonomy/rebuild').stdout
    open(f'wd_{job}.json','w').write(out); print(job, len(out))
