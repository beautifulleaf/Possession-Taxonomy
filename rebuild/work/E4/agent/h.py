import json, os
def v(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def x(n,mk,y,d,s,vs=(),dt="",a=""): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(vs),"dt":dt}
def B(n,c,f,seg,kf,d,s="knowledge",sig=(),lines=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=list(sig)
    if lines: b["lines"]=list(lines)
    if rel: b["rel"]=list(rel)
    return b
def W(job,obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E4/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
