import sys, json, re, time
sys.path.insert(0,'tools')
import run, netlib
titles=sys.argv[1].split('|'); kw=re.compile(sys.argv[2],re.I)
for t in titles:
    st,j=netlib.get_json(netlib.WP,{'action':'query','titles':t,'prop':'extracts|info','explaintext':1,'inprop':'url','redirects':1,'format':'json'})
    if not j: print('##',t,'ERR',st); continue
    for p in j['query']['pages'].values():
        if 'missing' in p: print('##',t,'MISSING'); continue
        txt=p.get('extract','');u=p['fullurl']
        run.log_source('B5','05_00',u,'api')
        print('##',p['title'],u,len(txt))
        for s in re.split(r'(?<=[.!?])\s+',txt):
            if kw.search(s): print('  -',s[:280])
    time.sleep(0.3)
