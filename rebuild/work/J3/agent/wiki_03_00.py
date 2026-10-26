import sys, json, os
sys.path.insert(0, 'tools')
import run
titles = json.load(open(sys.argv[1]))
r = json.loads(run.handle_client_tool('J3', '03_00', 'wiki', {'titles': titles}))
for p in r['pages']:
    print('==', p.get('title'), p.get('exists'), p.get('url'))
    if p.get('extract'): print(p['extract'][:int(sys.argv[2]) if len(sys.argv)>2 else 500])
