import json,os,sys
os.chdir('/home/user/Possession-Taxonomy/rebuild')
S={'W':'https://en.wikipedia.org/wiki/List_of_watch_manufacturers','SW':'https://en.wikipedia.org/wiki/List_of_Swiss_watch_manufacturers','DE':'https://en.wikipedia.org/wiki/List_of_German_watch_manufacturers','FR':'https://www.fratellowatches.com/watchbrands/','MO':'https://monochrome-watches.com/all-brands/','CL':'https://en.wikipedia.org/wiki/List_of_clock_manufacturers','US':'https://en.wikipedia.org/wiki/List_of_United_States_clock_companies','CP':'https://www.cuckoopalace.com/Information/Cuckoo-Clocks-Information-Guide/','FHH':'https://en.worldtempus.com/article/industry-news/fhh-twelve-new-partner-brands-24882.html','K':'knowledge'}
reg={b['n'].strip().lower():b for b in json.load(open('reader/_brands.json'))['b']}
P='work/_harvest/A5.json'
cur=json.load(open(P))['b'] if os.path.exists(P) else []
have={b['n'].lower() for b in cur}
skipped=[]
for l in open('work/_harvest/A5_work/rows.txt'):
    l=l.rstrip('\n')
    if not l or l.startswith('#'): continue
    n,seg,kf,src,c,f,d=(l.split('|')+['']*7)[:7]
    r=reg.get(n.lower())
    if r and 'A5' in (r.get('cats') or []): skipped.append(n); continue
    if n.lower() in have: continue
    b={'n':n,'seg':seg,'kf':kf,'s':S[src]}
    if c: b['c']=c
    if f: b['f']=f
    if d: b['d']=d
    cur.append(b); have.add(n.lower())
json.dump({'b':cur},open(P+'.tmp','w'),ensure_ascii=False,indent=0); os.replace(P+'.tmp',P)
print('total',len(cur),'skipped existing A5:',len(skipped),skipped)
from collections import Counter
print(Counter(b['seg'] for b in cur))
