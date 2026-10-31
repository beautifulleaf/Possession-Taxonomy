import sys, json, time
sys.path.insert(0, 'tools')
import run, netlib
titles = sys.argv[1].split('|')
for i in range(0, len(titles), 8):
    b = titles[i:i+8]
    for k in range(6):
        st, r = netlib.wiki_pages(b)
        if st == 200: break
        time.sleep(5 + k*5)
    print('status', st)
    for p in r:
        if p.get('exists') and p.get('url'): run.log_source('E3', '02_03', p['url'], 'api')
        print('##', p.get('title'), p.get('exists'), p.get('url'))
    time.sleep(2)
