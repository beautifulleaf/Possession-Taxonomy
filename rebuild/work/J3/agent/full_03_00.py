import sys, json, re
sys.path.insert(0, 'tools')
import netlib, time
spec = json.load(open(sys.argv[1]))  # {title: [keywords]}
for t, kws in spec.items():
    time.sleep(1.5)
    for _ in range(3):
        st, j = netlib.get_json(netlib.WP, {'action':'query','prop':'extracts','explaintext':1,'titles':t,'redirects':1,'format':'json'})
        if j: break
        time.sleep(5)
    if not j: print('FAIL',t,st); continue
    p = list(j['query']['pages'].values())[0]
    txt = p.get('extract') or ''
    print('#####', t, len(txt))
    sents = re.split(r'(?<=[.!?])\s+|\n+', txt)
    for s in sents:
        if any(k.lower() in s.lower() for k in kws): print(' -', s[:300])
