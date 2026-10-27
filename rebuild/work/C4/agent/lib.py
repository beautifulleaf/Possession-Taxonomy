import json,os,sys
def write(job,kinds,brands,traditions,notes):
    p=f'work/C4/shelves/{job}.json'
    json.dump({"kinds":kinds,"brands":brands,"traditions":traditions,"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1)
    os.replace(p+'.tmp',p)
def B(n,c,f,seg,kf,d,s='knowledge',**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}; b.update(kw); return b
def X(n,mk,s,d,y="",v=None,dt=""):
    x={"n":n,"mk":mk,"d":d,"s":s}
    if y: x["y"]=y
    if v: x["v"]=[{"n":a,"mk":mk,"y":"","d":dd} for a,dd in v]
    if dt: x["dt"]=dt
    return x
def old(job):
    t=open(f'work/C4/prompts/{job}.txt').read()
    i=t.index('```json\n')+8; j=t.index('\n```',i)
    return json.loads(t[i:j])
