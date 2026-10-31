import json, os, subprocess
def save(job, kinds, brands, trads, notes):
    p=f'work/C4/shelves/{job}.json'; t=p+'.tmp'
    json.dump({'kinds':kinds,'brands':brands,'traditions':trads,'notes':notes}, open(t,'w'), ensure_ascii=False, indent=1)
    os.rename(t,p)
    print(subprocess.run(['python3','tools/local.py','check','C4',job],capture_output=True,text=True).stdout)
def B(n,c,f,seg,kf,d,s='knowledge',**kw):
    b={'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':d,'s':s}; b.update(kw); return b
def X(n,d,mk,s,y='',v=None,dt='',a=''):
    x={'n':n,'d':d,'mk':mk,'s':s}
    if a:x['a']=a
    if y:x['y']=y
    if v:x['v']=[{'n':i[0],'mk':i[1] if len(i)>1 else mk,'y':'','d':i[2] if len(i)>2 else ''} for i in v]
    if dt:x['dt']=dt
    return x
