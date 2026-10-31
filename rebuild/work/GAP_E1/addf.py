import json,sys,os
f='rebuild/work/GAP_E1/facts.json'
F=json.load(open(f)) if os.path.exists(f) else {}
F.update(json.loads(sys.stdin.read()))
json.dump(F,open(f,'w'),ensure_ascii=False,indent=0)
print(len(F))
