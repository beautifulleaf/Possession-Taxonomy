import sys, json, time
sys.path.insert(0, 'tools')
import run
titles = json.load(open(sys.argv[1]))
n = int(sys.argv[2]) if len(sys.argv)>2 else 500
for i in range(0, len(titles), 20):
    for t in range(8):
        r = json.loads(run.handle_client_tool('J3', '03_06', 'wiki', {'titles': titles[i:i+20]}))
        if not any(p.get('error') for p in r['pages']): break
        time.sleep(20)
    for p in r['pages']:
        print('==', p.get('title'), p.get('exists'), p.get('url'), p.get('error',''))
        if p.get('extract'): print(p['extract'][:n].replace('\n',' '))
    time.sleep(1)
