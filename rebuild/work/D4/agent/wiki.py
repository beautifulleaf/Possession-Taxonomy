import sys, json, os
sys.path.insert(0, 'tools'); import run
titles = sys.argv[1].split('|')
r = json.loads(run.handle_client_tool('D4', '01_01', 'wiki', {'titles': titles}))
for p in r['pages']:
    print('##', p.get('title'), p.get('exists'), p.get('url')); print((p.get('extract') or '')[:600])
