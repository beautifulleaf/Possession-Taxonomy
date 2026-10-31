import json, glob, os
os.chdir('/home/user/Possession-Taxonomy/rebuild')
SEG={'PF':'Professional & flagship','PR':'Premium','MA':'Mainstream','VA':'Value','HM':'Heritage manufactory',
     'AI':'Artisan & independent','SP':'Specialist','OL':'Own-label & retailer','IN':'Institution & issuer'}
src=dict(l.rstrip('\n').split('\t') for l in open('work/_harvest/H1_work/src.tsv'))
reg={b['n'].strip().lower():b for b in json.load(open('reader/_brands.json'))['b']}
DROP={'elixir','parachute','playtex','zenith','royal crown','eisenberg'}|{x.strip().lower() for l in open('work/_harvest/H1_work/cut.txt') for x in l.rstrip('\n').split('|') if x.strip()}
D={'Burma-Shave':'American brushless shaving cream famed for its roadside rhyming signs; historically important, revived in the 1990s.','Rolls Razor':'British self-stropping safety razor made from 1927; defunct, historically important.','Madam C. J. Walker':'Hair care company of America\'s first self-made woman millionaire; historically important, revived as a brand in 2016.','Kalodont':'Early toothpaste in a tube from Vienna; historically important.','Bonne Bell':'American cosmetics company that created Lip Smackers; historically important.'}
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
        if n in D: b['d']=D[n]
        b['s']=src[s]
        out.append(b)
json.dump({'b':out},open(p+'.tmp','w'),ensure_ascii=False,indent=0)
os.replace(p+'.tmp',p)
print(len(out))
