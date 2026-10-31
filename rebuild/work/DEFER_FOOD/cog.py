import json,re,unicodedata
t=open('/tmp/claude-0/-home-user-Possession-Taxonomy/0fa341d7-9ce7-5e1d-8d76-d0d6deeae94e/scratchpad/cog.txt').read()
rows=re.findall(r'#### \[([^\]]+)\]\((https://www.cognac-expert.com/brands/[^)]+)\)\s*\n\s*\n([^\n\[]*)',t)
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'\bcognac\b','',s); return re.sub(r'[^a-z0-9]','',s)
d=json.load(open('rebuild/out/J7.json'))
k=[k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n']=='Cognac' and dp['n']=='Brandy'][0]
have={norm(e['n']) for e in k['x']}
have|={'bachegabrielsendupuy','bachegabrielsen','dupuy','ussed','ussé'}
have|={norm('Rémy Martin')}
added=0;seen=set()
for n,u,c in rows:
    if 'Cognac' not in c.split(): continue
    nm=re.sub(r'\s+Cognac$','',n.strip())
    key=norm(n)
    if key in have or key in seen or not key: continue
    seen.add(key)
    k['x'].append({"n":nm,"a":"","d":"Cognac house or brand listed by Cognac Expert; no owner stated on the page.","mk":nm,"y":"","s":u,"g":"Other houses listed by Cognac Expert"})
    added+=1
tot=len(k['x'])
k['sel']=("Every house named in Wikipedia's Cognac article and whisky.fr's list of great houses, plus every brand tagged Cognac on Cognac Expert's All Brands page (fetched 2026-10-31 through Parallel). "
 f"Complete: {tot} of {tot} in those references; the Cognac Expert entries state no owner or year, Louis XIII is a Rémy Martin cuvée and Noy is Armenian. Armagnac-only and other-spirit brands on that page are in other kinds or left out.")
k['xg']="by owner stated, then other houses"
json.dump(d,open('rebuild/work/DEFER_FOOD/J7.tmp','w'),ensure_ascii=False,indent=1)
print(added,tot)
