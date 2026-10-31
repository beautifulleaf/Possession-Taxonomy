import sys, json, re
sys.path.insert(0,'tools')
import run
titles=sys.argv[1].split('|'); kw=re.compile(sys.argv[2],re.I)
r=json.loads(run.handle_client_tool('B5','03_00','wiki',{'titles':titles}))
for p in r.get('pages',[]):
    t=(p.get('extract') or p.get('text') or '')
    print('##',p.get('title'),p.get('url'),len(t))
    for s in re.split(r'(?<=[.!?])\s+',t):
        if kw.search(s): print('  -',s[:300])
