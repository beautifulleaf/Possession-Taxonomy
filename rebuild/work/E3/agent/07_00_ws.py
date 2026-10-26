import sys,json
sys.path.insert(0,'tools')
import netlib,time
for q in sys.argv[1].split('|'):
    st,r=netlib.wiki_search(q,5); print('##',q,st,[x.get('title') if isinstance(x,dict) else x for x in (r or [])]); time.sleep(0.2)
