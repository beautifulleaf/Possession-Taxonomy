import sys, json, os
sys.path.insert(0,'tools')
import run
titles=sys.argv[1].split('|')
r=json.loads(run.handle_client_tool('B5','03_00','wiki',{'titles':titles}))
for p in r.get('pages',[]):
    print('##',p.get('title'),p.get('exists'),p.get('url'))
    print((p.get('extract') or p.get('text') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 1500].replace('\n',' '))
