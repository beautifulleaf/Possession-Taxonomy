import json, os
def A(n, s, d, mk="", y="", a="", v=None, dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[{"n":i[0],"mk":i[1] if len(i)>1 else "","y":i[2] if len(i)>2 else "","d":i[3] if len(i)>3 else ""} for i in v]
    if dt: x["dt"]=dt
    return x
def K(n, d, x=None, t=None, a="", s=None, m=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    if s: k["s"]=s
    if x: k["x"]=x
    if m: k["m"]=[[i,""] if isinstance(i,str) else i for i in m]
    return k
def save(job, kinds, brands, trads, notes):
    p=f"work/J4/shelves/{job}.json"
    json.dump({"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1)
    os.rename(p+".tmp",p)
