import json,os,sys
def put(job,obj):
    R='/home/user/Possession-Taxonomy/rebuild/work/I1'
    tmp=f'{R}/agent/{job}.tmp.json'
    json.dump(obj,open(tmp,'w'),ensure_ascii=False,indent=1)
    os.replace(tmp,f'{R}/shelves/{job}.json')
