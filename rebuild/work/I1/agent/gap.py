import json,os
R='/home/user/Possession-Taxonomy/rebuild/work/I1'
adds={
 '09_01':('Desktop database software',[['LibreOffice Base','The Document Foundation'],['DB Browser for SQLite','']]),
 '02_03':('Accounting software',[['Xero','Xero Limited'],['Wave','']]),
 '06_01':('E-book reader',[['calibre','Kovid Goyal']]),
 '02_02':('Text-to-speech software',[['Balabolka',''],['NaturalReader','NaturalReaders'],['Panopreter Basic','']]),
}
for j,(kn,models) in adds.items():
    p=f'{R}/shelves/{j}.json'
    d=json.load(open(p))
    for k in d['kinds']:
        if k['n']==kn:
            have={m[0].lower() for m in k['m']}
            for m in models:
                if m[0].lower() not in have: k['m'].append(m)
            break
    else: raise SystemExit('missing '+kn)
    tmp=f'{R}/agent/{j}.gap.tmp.json'
    json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
    os.replace(tmp,p)
    print(j,'ok',len(k['m']))
