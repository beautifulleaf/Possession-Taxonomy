import json, os
H="https://www.handbookofmineralogy.org/pdfs/"; W="https://en.wikipedia.org/wiki/"
FE="https://www.fossilera.com/minerals-for-sale"
def X(n,d,s,a="",y="",v=None,dt=""):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"v":[{"n":q[0],"mk":"","y":q[1] if len(q)>1 else "","d":q[2] if len(q)>2 else ""} for q in (v or [])],"dt":dt}
def K(n,d,s,xs,a="",t=None):
    k={"n":n,"a":a,"d":d,"s":s,"x":xs}
    if a=="": k.pop("a")
    if t: k["t"]=t
    return k
def finish(job,kinds,notes):
    p=f"/home/user/Possession-Taxonomy/rebuild/work/F6/shelves/{job}.json"
    json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
