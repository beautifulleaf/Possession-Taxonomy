import sys, json, os, time
sys.path.insert(0, 'tools')
import run, netlib
for t in sys.argv[1].split('|'):
    fn = f"work/E3/agent/t01/{t.replace('/','_')}.txt"
    if os.path.exists(fn): print('have', t); continue
    j=None
    for i in range(6):
        st, j = netlib.get_json(netlib.WP, {'action':'query','titles':t,'prop':'extracts|info','inprop':'url','redirects':1,'explaintext':1,'format':'json'})
        if j: break
        time.sleep(5*(i+1))
    if not j: print('FAIL', t, st); continue
    p = list(j['query']['pages'].values())[0]
    if 'missing' in p: print('MISSING', t); continue
    run.log_source('E3','01_00',p['fullurl'],'api')
    open(fn,'w').write(p['fullurl']+'\n'+p.get('extract',''))
    print('OK', t, '->', p['fullurl'], len(p.get('extract','')))
    time.sleep(1.5)
