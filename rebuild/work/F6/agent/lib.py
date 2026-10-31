import json, os
W="https://en.wikipedia.org/wiki/"
def X(n,d,s,a="",y="",v=None,dt="",mk=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":(q[3] if len(q)>3 else ""),"y":q[1],"d":q[2]} for q in (v or [])],"dt":dt}
def K(n,d,s,xs,a="",t=None,m=None):
    k={"n":n,"a":a,"d":d,"s":s,"x":xs}
    if t: k["t"]=t
    if m: k["m"]=m
    return k
def B(n,c,f,seg,kf,d,s,**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}; b.update(kw); return b
def save(job,kinds,brands,notes,trads=None):
    p=f"work/F6/shelves/{job}.json"
    json.dump({"kinds":kinds,"brands":brands,"traditions":trads or [],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1)
    os.replace(p+".tmp",p)
