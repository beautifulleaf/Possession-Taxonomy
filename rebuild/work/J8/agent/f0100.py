import sys, json, time, re
sys.path.insert(0, 'tools')
import run, netlib
# log existence of new titles
new = ["Manner (confectionery)", "Viennese whirls", "List of shortbread biscuits and cookies", "List of biscuits and cookies"]
for i in range(6):
    r = json.loads(run.handle_client_tool('J8','01_00','wiki',{'titles':new}))
    if all('error' not in p for p in r['pages']): break
    time.sleep(30)
for p in r['pages']: print('##', p.get('title'), p.get('url'), (p.get('extract') or '')[:500].replace('\n',' '))
full = sys.argv[1].split('|')
kw = re.compile(sys.argv[2], re.I)
for t in full:
    for i in range(6):
        st, j = netlib.get_json(netlib.WP, {'action':'query','prop':'extracts','explaintext':1,'titles':t,'redirects':1,'format':'json'})
        if j: break
        time.sleep(30)
    txt = list(j['query']['pages'].values())[0].get('extract','')
    sents = re.split(r'(?<=[.!?])\s+', txt)
    hits = [s for s in sents if kw.search(s)]
    print('\n####', t, len(txt)); print(' | '.join(hits)[:2500])
    time.sleep(0.3)
