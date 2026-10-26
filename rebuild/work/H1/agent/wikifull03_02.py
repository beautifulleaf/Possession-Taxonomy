import sys, json, re
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/tools')
import netlib
for t in sys.argv[1:]:
    st, j = netlib.get_json(netlib.WP, {'action':'query','prop':'extracts','explaintext':1,'titles':t,'format':'json','redirects':1})
    if not j: print('##', t, 'ERR', st); continue
    for p in j['query']['pages'].values():
        tx = p.get('extract','')
        print('##', t, len(tx))
        for kw in ['grade','silvertip','Silvertip','pure','Best','boar','synthetic','green','1948','Eucalyptus','Ice Blue','1937','Trumper','Truefitt','Skin Food','West Indian','Clubman','scuttle','Tabac','1959','Lilac','1900']:
            for m in re.finditer(kw, tx):
                print('  ', kw, ':', tx[max(0,m.start()-150):m.start()+200].replace('\n',' '))
                break
