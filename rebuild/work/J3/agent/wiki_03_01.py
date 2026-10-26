import sys, json
sys.path.insert(0, 'tools')
import run
titles = json.load(open(sys.argv[1]))
n = int(sys.argv[2]) if len(sys.argv)>2 else 500
for i in range(0, len(titles), 40):
    r = json.loads(run.handle_client_tool('J3', '03_01', 'wiki', {'titles': titles[i:i+40]}))
    for p in r['pages']:
        print('==', p.get('title'), p.get('exists'), p.get('url'))
        if p.get('extract'): print(p['extract'][:n].replace('\n',' '))
