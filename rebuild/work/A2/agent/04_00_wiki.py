import sys, json
sys.path.insert(0, 'tools')
import run
titles = sys.argv[1].split('|')
r = json.loads(run.handle_client_tool('A2', '04_00', 'wiki', {'titles': titles}))
for p in r.get('pages', []):
    ex = (p.get('extract') or p.get('text') or '')
    print('==', p.get('title'), p.get('exists'), p.get('url'))
    print(ex[:int(sys.argv[2]) if len(sys.argv)>2 else 1500])
