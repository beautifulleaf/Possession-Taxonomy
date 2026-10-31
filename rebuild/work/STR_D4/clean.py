import json,os
p='/home/user/Possession-Taxonomy/rebuild/out/D4.json'
d=json.load(open(p))
def clean(o):
    if isinstance(o,dict):
        for k in list(o):
            if o[k]==[] and k in('r','m','x','see'): del o[k]
            else: clean(o[k])
    elif isinstance(o,list):
        for i in o: clean(i)
clean(d)
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
