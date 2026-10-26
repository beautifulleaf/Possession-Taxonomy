import sys, json, time
sys.path.insert(0, 'tools')
import run
titles = [t.strip() for t in open(sys.argv[1]) if t.strip()]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 450
for i in range(0, len(titles), 8):
    for attempt in range(4):
        r = json.loads(run.handle_client_tool('G1', '00_00', 'wiki', {'titles': titles[i:i+8]}))
        if any(p.get('error') for p in r['pages']):
            time.sleep(20 * (attempt + 1)); continue
        break
    for p in r['pages']:
        print('##', p.get('title'), p.get('exists'), p.get('url'), p.get('error', ''))
        print((p.get('extract') or '')[:n].replace('\n', ' '))
    time.sleep(3)
