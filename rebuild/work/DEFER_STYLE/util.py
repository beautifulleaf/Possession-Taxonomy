import json,os
def load(p): return json.load(open(p))
def save(p,d):
    open(p+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1)); os.rename(p+'.tmp',p)
def walk(o,f,path=()):
    if isinstance(o,dict):
        f(o,path)
        for k,v in list(o.items()): walk(v,f,path+(k,))
    elif isinstance(o,list):
        for i in o: walk(i,f,path)
