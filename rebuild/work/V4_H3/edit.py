import json,os
p='rebuild/out/H3.json'
d=json.load(open(p))
reg_p='rebuild/out/H3_brands.json'
bj=json.load(open(reg_p)); reg={b['n'] for b in bj['b']}
cnt={}
mk=set()
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for m in k.pop('m',[])+k.pop('r',[]): mk.add(m[1]); cnt['m/r']=cnt.get('m/r',0)+1
            for e in k.pop('x',[]):
                mk.add(e.get('mk')); cnt['x']=cnt.get('x',0)+1
                for v in e.get('v',[]): mk.add(v.get('mk'))
            for f in ('nl','sel','xg'): k.pop(f,None)
for n in sorted(x for x in mk if x and x not in reg):
    bj['b'].append({"n":n,"c":"","f":"","seg":"Specialist","kf":"","d":"Maker named for products in this category; country and founding year not sourced.","s":""})
print(cnt,len(bj['b']))
for path,o in((p,d),(reg_p,bj)):
    json.dump(o,open(path+'.tmp','w'),indent=1,ensure_ascii=False); os.rename(path+'.tmp',path)
