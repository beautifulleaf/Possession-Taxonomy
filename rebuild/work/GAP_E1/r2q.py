import json,sys,urllib.parse
q=json.load(open('rebuild/work/GAP_E1/queue.json'))
d=json.load(open('rebuild/out/E1.json'))
noown={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x') or []:
                noown[(k['n'],e['n'])]=e.get('own') in(None,'','owner not stated')
q=[x for x in q if x[0]!=2 or noown.get((x[1],x[2]))]
titles=[]
for p,k,n,t in q:
    if t not in titles: titles.append(t)
json.dump(titles,open('rebuild/work/GAP_E1/titles.json','w'),ensure_ascii=False)
i=int(sys.argv[1]); 
ch=titles[i*20:(i+1)*20]
print(len(titles),len(ch),file=sys.stderr)
print('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=1&explaintext=1&exlimit=20&redirects=1&titles='+urllib.parse.quote('|'.join(ch)))
