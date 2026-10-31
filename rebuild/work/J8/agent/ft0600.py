import sys, json, time
sys.path.insert(0, 'tools')
import netlib
for t in sys.argv[1:]:
    for a in range(5):
        st, j = netlib.get_json(netlib.WP, {'action':'query','prop':'extracts','explaintext':1,'titles':t,'format':'json','redirects':1})
        if j: break
        time.sleep(8*(a+1))
    txt = ''.join(p.get('extract','') for p in j['query']['pages'].values()) if j else ''
    open('work/J8/agent/ft0600/'+t.replace('/','_')+'.txt','w').write(txt); print(t, len(txt)); time.sleep(1.5)
