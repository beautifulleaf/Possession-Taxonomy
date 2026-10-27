import sys, subprocess, json
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from titles34 import T
for job in sys.argv[1:]:
    vals = ' '.join(json.dumps(t, ensure_ascii=False)+'@en' for t in T[job])
    q = ('SELECT ?item ?title ?desc ?inc WHERE { VALUES ?title { '+vals+' } ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?title . '
         'OPTIONAL { ?item schema:description ?desc FILTER(lang(?desc)="en") } OPTIONAL { ?item wdt:P571 ?inc } }')
    out = subprocess.run(['python3','tools/local.py','wd','F3',job,'sparql',q],capture_output=True,text=True,cwd='/home/user/Possession-Taxonomy/rebuild').stdout
    open(f'/home/user/Possession-Taxonomy/rebuild/work/F3/agent/wd_{job}.json','w').write(out)
    try:
        d=json.loads(out); rows=d.get('sparql') or d
        seen=set()
        for r in rows:
            k=r.get('title')
            if k in seen: continue
            seen.add(k); print(job,'|',k,'|',r.get('item','').rsplit('/',1)[-1],'|',(r.get('desc') or '')[:60],'|',(r.get('inc') or '')[:10])
        print(job,'MISSING:',[t for t in T[job] if t not in seen])
    except Exception as e: print(job,'ERR',e,out[:500])
