import json,sys,time,urllib.request,urllib.parse
UA={"User-Agent":"possession-taxonomy/1.0 (noreply@anthropic.com)"}
for t in sys.argv[1:]:
    u="https://en.wikipedia.org/w/api.php?action=query&prop=extracts|info&inprop=url&explaintext=1&redirects=1&format=json&titles="+urllib.parse.quote(t)
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA)))
    for p in d['query']['pages'].values():
        print("=====",t,"->",p.get('title'),p.get('fullurl'),'MISSING' if 'missing' in p else '')
        open(t.replace('/','_')+'.txt','w').write(p.get('extract',''))
    time.sleep(0.3)
