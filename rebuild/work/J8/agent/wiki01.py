import sys, json
sys.path.insert(0, 'tools')
import run
titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
for i in range(0, len(titles), 20):
    r = json.loads(run.handle_client_tool('J8', '00_01', 'wiki', {'titles': titles[i:i+20]}))
    for p in r.get('pages', []):
        if p.get('exists'): print('##', p['title'], '|', p['url'], '\n', p.get('extract','')[:int(sys.argv[2]) if len(sys.argv)>2 else 500].replace('\n',' '))
        else: print('## MISSING', p)
