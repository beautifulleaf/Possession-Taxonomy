import json,os,sys
def save(job,obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/F4/shelves/{job}.json'
    open(p+'.tmp','w').write(json.dumps(obj,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
