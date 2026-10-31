import json,subprocess,sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_I3')
import apply as A
R=A.R
out,rep=A.main()
for dep in out['depts']:
    for sh in dep['s']:
        if len(sh['k'])>3 and not sh.get('ax'): sh['ax']="Which of these services does the plan give you?"
# brand register
b=json.load(open(R+'work/V4_I3/bak/I3_brands.json'))
have={x['n'].lower() for x in b['b']}
new={}
for dep in out['depts']:
    for sh in dep['s']:
        for k in sh['k']:
            for x in k.get('x') or []:
                for nm in {x.get('own'),x.get('mk')}:
                    if nm and nm.lower() not in have and nm not in new and len(nm)<60:
                        new[nm]={"n":nm,"c":x.get('cty','') if nm==x.get('own') and ' / ' not in nm else "","f":"","seg":"Mainstream","kf":"","d":f"Owner or maker of {x['n']}.","s":x['s']}
for nm,v in sorted(new.items()): b['b'].append(v)
b['b'].sort(key=lambda x:x['n'].lower())
def w(p,o):
    open(p+'.tmp','w').write(json.dumps(o,ensure_ascii=False,indent=1)); import os; os.replace(p+'.tmp',p)
w(R+'out/I3.json',out); w(R+'out/I3_brands.json',b); w(R+'out/I3_renames.json',{})
print(len(new),'new brands')
json.dump(rep,open(R+'work/V4_I3/rep.json','w'))
