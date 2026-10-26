import json,os,sys
def w(code,job,obj):
    p=f'work/{code}/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
