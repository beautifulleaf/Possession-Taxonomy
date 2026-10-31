import json, os
def write(job, kinds, brands, trads, notes):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/J5/shelves/{job}.json'
    json.dump({"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1)
    os.rename(p+'.tmp',p)
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def X(n,a,d,s,v=(),dt="",mk="",y=""): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(v),"dt":dt}
W="https://en.wikipedia.org/wiki/"
