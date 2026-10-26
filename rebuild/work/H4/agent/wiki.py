import sys, json
sys.path.insert(0, 'tools')
import run
titles = [t.strip() for t in open(sys.argv[1]) if t.strip()]
for i in range(0, len(titles), 40):
    r = json.loads(run.handle_client_tool('H4', '00_00', 'wiki', {'titles': titles[i:i+40]}))
    for p in r.get('pages', []):
        if p.get('exists'): print('##', p['title'], '|', p['url'], '\n', p['extract'][:500].replace('\n', ' '))
        else: print('-- MISSING', p.get('title'), p.get('error', ''))
