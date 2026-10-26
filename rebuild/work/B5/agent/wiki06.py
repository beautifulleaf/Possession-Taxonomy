import sys, json, re
sys.path.insert(0,'tools')
import run
titles=sys.argv[1].split('|'); kw=sys.argv[2] if len(sys.argv)>2 else ''; n=int(sys.argv[3]) if len(sys.argv)>3 else 800
r=json.loads(run.handle_client_tool('B5','06_00','wiki',{'titles':titles}))
for p in r.get('pages',[]):
    t=(p.get('extract') or p.get('text') or '').replace('\n',' ')
    print('##',p.get('title'),p.get('exists'),p.get('url'),len(t))
    print(t[:n])
    if kw:
        for s in re.split(r'(?<=[.!?]) ',t):
            if re.search(kw,s,re.I): print('  *',s[:300])
