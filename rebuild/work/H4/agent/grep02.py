import sys, json, re
sys.path.insert(0, 'tools')
import run
kw=sys.argv[1].split('|'); titles=sys.argv[2:]
r=json.loads(run.handle_client_tool('H4','02_00','wiki',{'titles':titles}))
for p in r.get('pages',[]):
    if not p.get('exists'): print('-- MISSING',p.get('title')); continue
    print('##',p['title'],'|',p['url'])
    for s in re.split(r'(?<=[.!?])\s+',p['extract']):
        if any(k.lower() in s.lower() for k in kw): print('  *',s[:400])
