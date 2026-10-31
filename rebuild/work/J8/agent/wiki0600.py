import sys, json, time
sys.path.insert(0, 'tools')
import run
titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 500
for i in range(0, len(titles), 6):
    for attempt in range(6):
        r = json.loads(run.handle_client_tool('J8', '06_00', 'wiki', {'titles': titles[i:i+6]}))
        ps = r.get('pages', [])
        if any(p.get('error') for p in ps): time.sleep(10 * (attempt + 1)); continue
        break
    for p in ps:
        if p.get('exists'): print('##', p['title'], '|', p['url'], '\n', p.get('extract','')[:n].replace('\n',' '))
        else: print('## MISSING', p)
    time.sleep(1.5)
