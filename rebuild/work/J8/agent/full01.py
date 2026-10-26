import sys, re, time
sys.path.insert(0, 'tools')
import netlib
titles = sys.argv[1].split('|'); pat = re.compile(sys.argv[2], re.I)
for t in titles:
    st, j = netlib.get_json(netlib.WP, {'action':'query','titles':t,'prop':'extracts','explaintext':1,'redirects':1,'format':'json'})
    for p in j['query']['pages'].values():
        tx = p.get('extract') or ''
        print('##', p.get('title'), len(tx))
        for s in re.split(r'(?<=[.!?])\s+', tx):
            if pat.search(s): print('  -', s[:260].replace('\n',' '))
    time.sleep(0.2)
