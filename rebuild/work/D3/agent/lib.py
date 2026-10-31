import json, os
WP='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),vv)) for vv in v]}
    if dt: x["dt"]=dt
    return x
def B(n,c,f,seg,kf,d,s,sig=(),lines=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if lines: b["lines"]=list(lines)
    if sig: b["sig"]=list(sig)
    return b
def K(n,a,d,s,t=None,x=None,m=None,r=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if x: k["x"]=x
    if m: k["m"]=[list(i) for i in m]
    if r: k["r"]=[list(i) for i in r]
    return k
def write(job,kinds,brands,notes,traditions=()):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/D3/shelves/{job}.json'
    t=p+'.tmp'; json.dump({"kinds":kinds,"brands":brands,"traditions":list(traditions),"notes":notes},open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
