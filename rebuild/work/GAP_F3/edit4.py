import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
ks={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh.get('k',[])}
U='https://en.wikipedia.org/wiki/List_of_circulating_currencies'
rows=[l.split('|') for l in open('/home/user/Possession-Taxonomy/rebuild/work/GAP_F3/cur.txt',encoding='utf8').read().splitlines() if l]
cnt={}
for kind,suffix,noun in(('Circulation coin','coins','Coins'),('Circulation banknote','banknotes','Banknotes')):
    k=ks[kind]; have={e['n'].lower() for e in k['x']}; c=0
    for st,cur,iso,reg in rows:
        n=f"{cur} {suffix}"
        if n.lower() in have: continue
        code=f"ISO code {iso}" if iso else "no ISO code"
        k['x'].append({"n":n,"a":"","d":f"{noun} of the {cur} ({code}), circulating in {st}.","mk":"","y":"","s":U,"v":[],"g":st,"dt":reg})
        c+=1
    cnt[kind]=c
    k['sel']=k['sel'].rstrip()+f" Round 2: every currency of Wikipedia's List of circulating currencies (read to its end) not already held is an entry named for the currency, with the issuing state in g, the region in dt and the ISO code in d; the euro, US dollar, sterling, rand, rupee and the other currencies of states listed above were already held. Complete: all currencies of that list; individual series of each currency are versions only where an earlier pass named them."
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
print(cnt)
