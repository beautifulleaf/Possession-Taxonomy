import sys, json
sys.path.insert(0, 'tools'); import run
titles = sys.argv[1].split('|')
r = json.loads(run.handle_client_tool('D4', '01_00', 'wiki', {'titles': titles}))
for p in r.get('pages', []):
    print('##', p.get('title'), p.get('exists'), p.get('url'), p.get('error','')); print((p.get('extract') or '')[:700])
