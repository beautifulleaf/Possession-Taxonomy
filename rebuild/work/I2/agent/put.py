import json,os,sys
def put(code,job,obj):
    p=f'work/{code}/shelves/{job}.json'
    json.dump(obj,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
    os.replace(p+'.tmp',p)
