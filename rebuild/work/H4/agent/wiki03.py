import sys, json
sys.path.insert(0, 'tools')
import run
mode=sys.argv[1]
if mode=='s':
    for q in sys.argv[2:]:
        r=json.loads(run.handle_client_tool('H4','03_00','wiki',{'search':q}))
        s=r.get('search')
        print('==',q, [ (x.get('title') if isinstance(x,dict) else x) for x in s] if isinstance(s,list) else s)
else:
    titles=sys.argv[2:]
    for i in range(0,len(titles),40):
        r=json.loads(run.handle_client_tool('H4','03_00','wiki',{'titles':titles[i:i+40]}))
        for p in r.get('pages',[]):
            if p.get('exists'): print('##',p['title'],'|',p['url'],'\n',p['extract'][:int(mode)].replace('\n',' '))
            else: print('-- MISSING',p.get('title'))
