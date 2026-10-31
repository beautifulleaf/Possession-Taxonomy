import sys, json
sys.path.insert(0, 'tools')
import run
mode=sys.argv[1]
if mode=='s':
    for q in sys.argv[2:]:
        r=json.loads(run.handle_client_tool('H4','02_00','wiki',{'search':q}))
        print('==',q, [ (x.get('title') if isinstance(x,dict) else x) for x in (r.get('search') or [])] if isinstance(r.get('search'),list) else r)
else:
    titles=sys.argv[2:]
    r=json.loads(run.handle_client_tool('H4','02_00','wiki',{'titles':titles}))
    for p in r.get('pages',[]):
        if p.get('exists'): print('##',p['title'],'|',p['url'],'\n',p['extract'][:int(mode)].replace('\n',' '))
        else: print('-- MISSING',p.get('title'))
