import json, glob, os
os.chdir('/home/user/Possession-Taxonomy/rebuild')
SEG={'PF':'Professional & flagship','PR':'Premium','MA':'Mainstream','VA':'Value','HM':'Heritage manufactory',
     'AI':'Artisan & independent','SP':'Specialist','OL':'Own-label & retailer','IN':'Institution & issuer'}
src=dict(l.rstrip('\n').split('\t') for l in open('work/_harvest/H1_work/src.tsv'))
reg={b['n'].strip().lower():b for b in json.load(open('reader/_brands.json'))['b']}
DROP={'elixir','parachute','playtex','zenith','royal crown','eisenberg'}
out=[];seen=set()
p='work/_harvest/H1.json'
if os.path.exists(p):
    for b in json.load(open(p))['b']: out.append(b); seen.add(b['n'].lower())
for f in sorted(glob.glob('work/_harvest/H1_work/b*.txt')):
    for l in open(f):
        l=l.rstrip('\n')
        if not l or l.startswith('#'): continue
        n,sg,kf,c,y,s=l.split('|')
        if n.lower() in DROP or n.lower() in seen: continue
        seen.add(n.lower())
        r=reg.get(n.lower())
        seg=r['seg'] if (r and 'H1' not in r.get('cats',[])) else SEG.get(sg)
        b={'n':n,'seg':seg,'kf':kf}
        if c: b['c']=c
        if y: b['f']=y
        b['s']=src[s]
        out.append(b)
json.dump({'b':out},open(p+'.tmp','w'),ensure_ascii=False,indent=0)
os.replace(p+'.tmp',p)
print(len(out))
