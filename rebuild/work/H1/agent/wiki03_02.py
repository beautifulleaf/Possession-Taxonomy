import sys, json, os
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/tools')
import run
titles = json.loads(sys.argv[1])
r = json.loads(run.handle_client_tool('H1', '03_02', 'wiki', {'titles': titles}))
for p in r.get('pages', []):
    print('##', p.get('title'), p.get('exists'), p.get('url'), p.get('error',''))
    print((p.get('extract') or '')[:600])
