import sys, os, json, time
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/tools')
import run
terms = [l.strip() for l in open(sys.argv[1]) if l.strip()]
out = {}
for t in terms:
    r = json.loads(run.handle_client_tool('J8','03_00','wikidata',{'search':t}))
    out[t] = r.get('search', [])[:3]
    print(t, '|', ' ; '.join(f"{x['id']} {x['label']} — {x.get('description','')}" for x in out[t]))
    time.sleep(0.2)
json.dump(out, open(sys.argv[2],'w'))
