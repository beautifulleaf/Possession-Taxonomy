import json
P='/home/user/Possession-Taxonomy/rebuild/out/J1.json'
d=json.load(open(P))
def pop(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,s['k'].pop(i)
    raise KeyError(n)
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
    raise KeyError(n)
# J1-4 offal merge
offal=[pop(n) for n in ['Beef liver','Beef tongue','Beef heart','Beef kidney','Sweetbreads']]
dp,sh=offal[0][0],offal[0][1]
types=['liver (ox or calf)','tongue','heart','kidney','sweetbreads']
for o in offal:
    for t in o[2].get('t',[]):
        if t not in types and t!="calf's liver": types.append(t)
for o in offal: print('offal',o[2]['n'],o[2].get('a'),o[2]['s'],o[2].get('t'))
kind={"n":"Beef & veal offal","a":"ox liver · ox tongue · beef heart · ox kidney · sweetbreads · variety meats","d":"Edible organs of cattle and calves sold raw: liver, tongue, heart, kidney and sweetbreads.","t":types,"s":offal[0][2]['s']}
sh['k'].append(kind)
# minor steaks
names=['Rump steak (top sirloin)','Tri-tip','Flat iron steak','Flank steak','Skirt steak','Hanger steak']
ms=[pop(n) for n in names]
sh=ms[0][1]
t=[]
al=[]
for m in ms:
    k=m[2]; print('steak',k['n'],k.get('a'),k.get('t'),k['s'])
    t.append(k['n']); 
    for x in k.get('t',[]):
        if x not in t: t.append(x)
    al+= [a.strip() for a in k.get('a','').split('·') if a.strip()]
# insert after picanha position: place at end of steaks shelf
sh['k'].append({"n":"Minor grilling steaks","a":' · '.join(dict.fromkeys(al)),"d":"Secondary steaks and roasts for grilling or pan-frying: rump, tri-tip, flat iron, flank, skirt and hanger.","t":t,"s":ms[0][2]['s']})
# J1-5 dry aged
da=pop('Dry-aged beef')[2]
for n in ['Ribeye steak','Sirloin steak (striploin)','T-bone & porterhouse','Rib roast']:
    k=find(n); 
    if 'dry-aged' not in k.setdefault('t',[]): k['t'].append('dry-aged')
# boxes shelf
mb=pop('Meat box'); cs=pop('Charcuterie & deli selection')
od=[x for x in d['depts'] if x['n']=='Other meats'][0]
od['s'].append({"n":"Boxes & selections","k":[mb[2],cs[2]]})
# J1-6
k=find("'Nduja & sobrasada"); k['n']="Spreadable raw sausage"; k['a']="'nduja · sobrasada · Teewurst · spreadable dry-cured sausage"
k['d']="Soft, spreadable raw or cured pork sausage sold in a casing, from Calabria, Mallorca and Germany (a jar of spread is in Pantry Staples)."
pk=find('Ibérico pork')
lab=[a for a in pk['x'] if 'label classes' in a['n']][0]
pk['x'].remove(lab)
pdp=[x for x in d['depts'] if x['n']=='Pork'][0]
pdp['b'].append({"m":"Ibérico label class (Real Decreto 4/2014)","v":"Black (100% ibérico de bellota) > Red (ibérico de bellota) > Green (cebo de campo) > White (cebo)","w":"Spanish quality norm with coloured seals, also applied to fresh cuts; "+lab['d']})
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
