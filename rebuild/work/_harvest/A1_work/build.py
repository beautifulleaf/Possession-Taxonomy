import json, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SEG={'L':'Luxury house','D':'Designer','C':'Contemporary & premium','H':'Heritage & workwear','J':'Japanese & denim','S':'Streetwear','O':'Outdoor & technical','A':'Athletic & sportswear','HS':'High street','V':'Value & basics','B':'Bespoke & artisan','T':'Traditional & national dress','SA':'Subculture & alternative'}
src=dict(l.rstrip('\n').split('\t') for l in open('srcmap.tsv') if l.strip())
reg={l.strip().lower() for l in open('reg_a1.txt')}
out=[];seen=set();skipped=[]
for fn in sorted(glob.glob('e_*.txt')):
  for line in open(fn):
    line=line.strip()
    if not line or line.startswith('#'): continue
    p=(line.split('|')+['']*7)[:7]
    n,sg,kf,c,f,s,d=[x.strip() for x in p]
    k=n.lower()
    if k in seen or k in reg: skipped.append(n); continue
    seen.add(k)
    b={'n':n,'seg':SEG[sg],'kf':kf,'s':src[s or 'K']}
    if c: b['c']=c
    if f: b['f']=f
    if d: b['d']=d
    out.append(b)
tmp='../A1.json.tmp'
json.dump({'b':out},open(tmp,'w'),ensure_ascii=False,indent=0)
os.replace(tmp,'../A1.json')
from collections import Counter
print(len(out),'written; skipped dup/existing',len(skipped))
print(Counter(b['seg'] for b in out))
if '-v' in sys.argv: print(skipped)
