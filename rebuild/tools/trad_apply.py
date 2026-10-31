"""Apply TRAD_APPLY placements (verify/work/TRAD_RUBRIC/APPLY_<C>.json) to out/<C>.json.
add_archetype -> appended to the kind's x list; add_kind -> appended to the shelf's k list.
Makers are collected to verify/work/TRAD_RUBRIC/makers_<C>.json for the brand layer.
Usage: python3 tools/trad_apply.py G1 G2 ..."""
import json,sys,shutil,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V=os.path.join(ROOT,'..','verify','work','TRAD_RUBRIC')
for c in sys.argv[1:]:
    ap=json.load(open(f'{V}/APPLY_{c}.json'))
    p=f'{ROOT}/out/{c}.json'; shutil.copy(p,f'{ROOT}/work/TRAD_APPLY/{c}.before.json')
    d=json.load(open(p)); added=skipped=0; makers=[]
    for it in ap['items']:
        if it['decision'] not in ('add_archetype','add_kind'): continue
        dp=next((x for x in d['depts'] if x['n']==it['dept']),None)
        sh=dp and next((x for x in dp['s'] if x['n']==it['shelf']),None)
        if not sh: print(c,'NO SHELF',it['dept'],'>',it['shelf']); skipped+=1; continue
        r={k:v for k,v in it['record'].items() if v not in ('',[],None) or k in('n','d','s')}
        if it['decision']=='add_kind':
            if any(k['n']==r['n'] for k in sh['k']): skipped+=1; continue
            sh['k'].append({k:r[k] for k in ('n','a','d','s') if k in r}); added+=1
        else:
            k=next((x for x in sh['k'] if x['n']==it['kind']),None)
            if not k: print(c,'NO KIND',it['kind']); skipped+=1; continue
            xs=k.setdefault('x',[])
            if any(x['n']==r['n'] for x in xs): skipped+=1; continue
            r.setdefault('mk',''); xs.append(r); added+=1
        for m in it.get('makers',[]): makers.append({**m,'cat':c,'for':r['n'],'ve_link':it.get('ve_link')})
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
    json.dump(makers,open(f'{V}/makers_{c}.json','w'),ensure_ascii=False,indent=1)
    print(c,'added',added,'skipped',skipped,'makers',len(makers))
