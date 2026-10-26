import sys, json, re
sys.path.insert(0, 'tools')
import run
pat=re.compile(sys.argv[1], re.I)
titles=sys.argv[2:]
r=json.loads(run.handle_client_tool('H4','03_00','wiki',{'titles':titles}))
for p in r.get('pages',[]):
    if not p.get('exists'): print('-- MISSING',p.get('title')); continue
    print('##',p['title'],'|',p['url'])
    for s in re.split(r'(?<=[.!?])\s+', p['extract'].replace('\n',' ')):
        if pat.search(s): print('  *',s[:300])
