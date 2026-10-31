def TT(s):
    out=[]
    for g in s.split(';;'):
        g=g.strip()
        if not g: continue
        lab,items=g.split(':',1)
        out.append([lab.strip(),[i.strip() for i in items.split('|') if i.strip()]])
    return out
WP='https://en.wikipedia.org/wiki/'
def K(old,tt,ren=None,d=None,a=None,see=None,keep=None):
    return dict(kind='old',old=old,tt=TT(tt),ren=ren,d=d,a=a,see=see)
def N(n,a,d,s,tt,take=None,see=None):
    return dict(kind='new',n=n,a=a,d=d,s=s,tt=TT(tt),take=take or {},see=see)
def SH(n,t,ax,kinds): return dict(n=n,t=t,ax=ax,k=kinds)
def DP(n,t,ax,shelves,mode=None,note=None): return dict(n=n,t=t,ax=ax,s=shelves,mode=mode,note=note)
