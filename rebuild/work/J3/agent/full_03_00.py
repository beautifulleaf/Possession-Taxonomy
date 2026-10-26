import sys, json, re
sys.path.insert(0, 'tools')
import netlib
spec = json.load(open(sys.argv[1]))  # {title: [keywords]}
for t, kws in spec.items():
    st, j = netlib.get_json(netlib.WP, {'action':'query','prop':'extracts','explaintext':1,'titles':t,'redirects':1,'format':'json'})
    p = list(j['query']['pages'].values())[0]
    txt = p.get('extract') or ''
    print('#####', t, len(txt))
    sents = re.split(r'(?<=[.!?])\s+|\n+', txt)
    for s in sents:
        if any(k.lower() in s.lower() for k in kws): print(' -', s[:300])
