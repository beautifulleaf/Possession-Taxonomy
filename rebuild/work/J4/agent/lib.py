import json,subprocess
W="https://en.wikipedia.org/wiki/"
def x(n,mk,y,s,d,v=None,a="",dt=""):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt:o["dt"]=dt
    return o
def v(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def K(n,d,s,x=None,m=None,t=None,a="",tg=None):
    k={"n":n,"a":a,"d":d,"s":s}
    if t:k["t"]=t
    if x:k["x"]=x
    if m:k["m"]=[[i,""] if isinstance(i,str) else i for i in m]
    return k
def B(n,c,seg,kf,d,s,**k): return dict(n=n,c=c,seg=seg,kf=kf,d=d,s=s,**k)
def write(job,kinds,brands,trads,notes,urls):
    d=f"work/J4/shelves/{job}"
    json.dump({"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes},open(d+".tmp","w"),ensure_ascii=False,indent=1)
    subprocess.run(["python3","tools/local.py","logsrc","J4",job,"fetched"]+urls)
    import os;os.rename(d+".tmp",d+".json")
    print(subprocess.run(["python3","tools/local.py","check","J4",job],capture_output=True,text=True).stdout)
