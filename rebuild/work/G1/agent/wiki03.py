import sys, json, time
sys.path.insert(0, 'tools')
import run
titles = [t.strip() for t in open(sys.argv[1]) if t.strip()]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 500
for i in range(0, len(titles), 10):
    r = json.loads(run.handle_client_tool('G1', '00_03', 'wiki', {'titles': titles[i:i+10]}))
    for p in r.get('pages', []):
        print('##', p.get('title'), p.get('exists'), p.get('url'), p.get('error', ''))
        print((p.get('extract') or '')[:n].replace('\n', ' '))
    time.sleep(1)
