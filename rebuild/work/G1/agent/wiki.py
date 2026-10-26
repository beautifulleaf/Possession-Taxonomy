import sys, json, os
sys.path.insert(0, 'tools')
import run
titles = [t.strip() for t in open(sys.argv[1]) if t.strip()]
r = json.loads(run.handle_client_tool('G1', '00_00', 'wiki', {'titles': titles}))
for p in r['pages']:
    print('##', p.get('title'), p.get('exists'), p.get('url'))
    print((p.get('extract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 500].replace('\n',' '))
