import sys, json, os, time
sys.path.insert(0, 'tools')
import run, netlib
titles = sys.argv[1].split('|')
r = json.loads(run.handle_client_tool('E3', '01_00', 'wiki', {'titles': titles}))
for p in r['pages']:
    print('##', p.get('title'), p.get('exists'), p.get('url'))
    if p.get('exists') and len(sys.argv) > 2:
        st, j = netlib.get_json(netlib.WP, {'action':'query','titles':p['title'],'prop':'extracts','explaintext':1,'format':'json'})
        t = list(j['query']['pages'].values())[0].get('extract','')
        open(f"work/E3/agent/t01/{p['title'].replace('/','_')}.txt",'w').write(t)
        print(len(t))
