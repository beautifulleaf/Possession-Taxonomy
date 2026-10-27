import sys, json
sys.path.insert(0,'tools')
import run
job=sys.argv[1]
for q in sys.argv[2:]:
    r=json.loads(run.handle_client_tool('F6',job,'wiki',{'search':q}))
    print('##',q)
    s=r.get('search')
    if isinstance(s,list):
        for x in s[:6]: print('  ',x if not isinstance(x,dict) else (x.get('title'),(x.get('snippet') or '')[:100]))
    else: print(s)
