import sys, json, time, os
sys.path.insert(0, 'tools')
import netlib
for t in sys.argv[1].split('|'):
    fn = f"work/E3/agent/t03/{t.replace('/','_')}.txt"
    if os.path.exists(fn): continue
    j=None
    for k in range(6):
        time.sleep(1.5+k*4)
        st, j = netlib.get_json(netlib.WP, {'action':'query','titles':t,'prop':'extracts','explaintext':1,'format':'json','redirects':1})
        if j: break
    if not j: print('fail', t); continue
    open(fn,'w').write(list(j['query']['pages'].values())[0].get('extract',''))
    print('ok', t)
