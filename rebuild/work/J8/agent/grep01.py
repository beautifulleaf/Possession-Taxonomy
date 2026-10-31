import sys, json, re
sys.path.insert(0, 'tools')
import run
titles = sys.argv[1].split('|'); pat = re.compile(sys.argv[2], re.I)
r = json.loads(run.handle_client_tool('J8', '00_01', 'wiki', {'titles': titles}))
for p in r.get('pages', []):
    if not p.get('exists'): print('## MISSING', p['title']); continue
    print('##', p['title'], p['url'], len(p.get('extract','')))
    for s in re.split(r'(?<=[.!?])\s+', p.get('extract','')):
        if pat.search(s): print('  -', s[:300])
