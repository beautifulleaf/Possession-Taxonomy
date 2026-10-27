import sys, json
sys.path.insert(0,'tools')
import run
job=sys.argv[1]
titles=sys.argv[2:]
r=json.loads(run.handle_client_tool('F6',job,'wiki',{'titles':titles}))
for p in r['pages']:
    print(p.get('title'), p.get('exists'), p.get('url'))
    print('   ', (p.get('extract') or '')[:int(__import__("os").environ.get("N","600"))].replace('\n',' '))
