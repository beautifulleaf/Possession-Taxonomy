import json,os,copy,shutil,re,datetime
R='/home/user/Possession-Taxonomy/rebuild'
exec(open('tt.py').read()); exec(open('struct.py').read())
d=json.load(open(R+'/out/C3.json'))
KI={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: KI[k['n']]=k
def X(kind,names):
    out=[]
    for n in names:
        for x in KI[kind]['x']:
            if x['n']==n: out.append(x)
    assert len(out)==len(names),(kind,names,len(out))
    return out
def newkind(n,x=None):
    a,dd,s=NEW[n]; k={'n':n,'a':a,'d':dd,'s':s}
    if x: k['x']=copy.deepcopy(x)
    return k
# archetype redistribution
bp,rb,sl,ce=KI['Bean & pea seed'],KI['Root & brassica seed'],KI['Salad & leaf seed'],KI['Celery & fennel seed']
runner=X('Bean & pea seed',["'Cherokee Trail of Tears'","'Scarlet Emperor'","'Painted Lady'","'Japanese Runner'","'White Dutch Runner'","'Judión de la Granja'"])
peas=X('Bean & pea seed',['Hurst Green Shaft','Kelvedon Wonder','Show Perfection','Terrain','Vivado','Serge','Jaguar'])
assert len(runner)+len(peas)==len(bp['x'])
rad=X('Root & brassica seed',['Daikon','Scarlet Globe','Sparkler','Amethyst','Celesta','Rudolf','Pink Beauty','Escala'])
pars=X('Root & brassica seed',['Gladiator','Picador','Pearl','Viper'])
turn=X('Root & brassica seed',['Tokyo Cross','Oasis','Temari Red','Brora','Gowrie','Magres'])
celi=X('Root & brassica seed',['Asterix','Ibis','Prinz'])
kale=X('Root & brassica seed',['Black Magic','Kapitan','Reflex','Starbor','Winterbor','Yurok'])
kohl=X('Root & brassica seed',['Kolibri','Korist','Olivia'])
pak=X('Root & brassica seed',['Baraku','Glacier','Red Choi','Summer Breeze'])
assert len(rad+pars+turn+celi+kale+kohl+pak)==len(rb['x'])
let=X('Salad & leaf seed',["'Little Gem'","'Buttercrunch'","'Forellenschluss'"])
spin=X('Salad & leaf seed',['Amazon','Matador','Medania','Mikado','Missouri','Fordhook Giant','Lucullus','Canary Yellow','Rhubarb Chard','Perpetual Spinach','Erbette'])
chic=X('Salad & leaf seed',['Palla Rossa','Pan di Zucchero','Pancalieri','Natacha','Wallone'])
assert len(let+spin+chic)==len(sl['x'])
# merged / renamed kinds
gb=KI['Green bean seed']; gb['n']='Runner & French bean seed'; gb['a']='runner bean · French bean · green bean · pole bean'
gb['d']='Packet of runner or French bean seed, climbing or dwarf, sown for green pods and shelling beans.'
gb['x']=gb['x']+runner
ce['n']='Celery, celeriac & fennel seed'; ce['d']='Packet of celery, celeriac or Florence fennel seed sold for sowing.'; ce['x']=ce['x']+celi
KI['Lettuce seed']['x']=KI['Lettuce seed']['x']+let
sl['x']=[]; sl['d']='Packet of salad-leaf seed other than lettuce, such as rocket, mizuna, mustard and corn salad, single or mixed.'
sl['a']='rocket · mizuna · corn salad · cut-and-come-again mix'
KI['Runner & French bean seed']=gb; KI['Celery, celeriac & fennel seed']=ce
extra={'Pea seed':peas,'Radish seed':rad,'Parsnip seed':pars,'Turnip & swede seed':turn,'Kale seed':kale,'Kohlrabi seed':kohl,'Pak choi seed':pak,'Spinach & chard seed':spin,'Chicory & endive seed':chic}
for n in NEW:
    KI[n]=newkind(n,extra.get(n))
# a few renames of definitions / aliases for existing kinds that moved
KI['Thaumatophyllum']['d']=KI['Thaumatophyllum']['d']
KI['Mushroom grow kit']['a']=KI['Mushroom grow kit'].get('a','')
# see links
SEE={
'Prickly pear':[('J4','Prickly pear','the fruit and pads as food')],
'Salvia':[('J10','Salvia','Salvia divinorum as a product')],
'Rosemary':[('J4','Rosemary','the cut herb as food')],
'Thyme':[('J4','Thyme','the cut herb as food')],
'Sage':[('J4','Sage','the cut herb as food')],
'Parsley plant':[('J4','Parsley','the cut herb as food')],
'Chives plant':[('J4','Chives','the cut herb as food')],
'Coriander plant':[('J4','Coriander','the cut herb as food')],
'Basil plant':[('J4','Basil','the cut herb as food')],
'Mint plant':[('J4','Mint','the cut herb as food')],
'Oregano & marjoram plant':[('J4','Oregano & marjoram','the cut herb as food')],
'Tomato plant':[('J4','Tomato','the fruit as food')],
'Chilli plant':[('J4','Chilli','the fruit as food')],
'Globe artichoke plant':[('J4','Globe artichoke','the buds as food')],
'Avocado tree':[('J4','Avocado','the fruit as food')],
'Banana plant':[('J4','Banana','the fruit as food')],
'Fig tree':[('J4','Fig','the fruit as food')],
'Lemon & lime tree':[('J4','Lemon','the fruit as food')],
'Olive tree':[('J4','Fresh olive','the fruit as food')],
'Seed potato':[('J4','Potato','the harvested crop as food')],
'Seed garlic':[('J4','Garlic','the harvested crop as food')],
'Onion set':[('J4','Bulb onion','the harvested crop as food')],
'Cauliflower seed':[('J4','Cauliflower','the harvested crop as food')],
'Tomato seed':[('J4','Tomato','the fruit as food')],
'Oyster mushroom spawn':[('J4','Oyster mushroom','the harvested mushroom as food')],
'Button mushroom spawn':[('J4','Button mushroom','the harvested mushroom as food')],
'Cannabis plant':[('J10','Cannabis flower','the harvested flower as a product')],
'Christmas tree':[('B4','Artificial Christmas tree','an artificial tree instead')],
'Fresh wreath':[('B4','Wreath','a lasting artificial wreath')],
'Mixed bouquet':[('B4','Artificial flower','a lasting artificial arrangement')],
'Cut foliage':[('B4','Dried flowers','dried and preserved stems')],
'Kombucha SCOBY':[('J9','Kombucha','the finished drink')],
'Water kefir grains':[('J9','Water kefir','the finished drink')],
'Milk kefir grains':[('J3','Kefir','the finished drink')],
'Tempeh starter':[('J3','Tempeh','the finished food')],
'Natto starter':[('J3','Natto','the finished food')],
'Sourdough starter':[('J8','Sourdough bread','the finished loaf')],
'Ale yeast':[('J5','Brewing yeast','yeast sold as a pantry product')],
'Wine, cider & mead yeast':[('J5','Brewing yeast','yeast sold as a pantry product')],
'Lotus':[('J4','Lotus root','the root as food')],
}
bad=[]
for n,l in SEE.items():
    for c,t,w in l:
        tg=json.load(open(f'{R}/reader/{c}.json')); names={k['n'] for dp in tg['depts'] for s in dp['s'] for k in s['k']}
        if t not in names: bad.append((n,c,t))
assert not bad,bad
for n,l in SEE.items(): KI[n]['see']=[list(x) for x in l]
# assemble
placed=set(); depts=[]
old={dp['n']:dp for dp in d['depts']}
for D in DEPTS:
    dp={'n':D['n'],'mode':D['mode']}
    if D.get('note'): dp['note']=D['note']
    elif old.get(D['n'],{}).get('note'): dp['note']=old[D['n']]['note']
    dp['b']=old.get(D['n'],{}).get('b',[])
    dp['t']=D['t']; dp['ax']=D['ax']; dp['s']=[]
    for sh in D['s']:
        ks=[]
        for n in sh['k']:
            k=copy.deepcopy(KI[n]); assert n not in placed,n; placed.add(n)
            k.pop('t',None); assert n in TT,('no tt',n); k['tt']=TT[n]
            ks.append(k)
        s={'n':sh['n'],'t':sh['t']}
        if sh['ax']: s['ax']=sh['ax']
        elif len(ks)>3: raise SystemExit('need ax '+sh['n'])
        s['k']=ks; dp['s'].append(s)
    depts.append(dp)
allk=set(KI)-{'Bean & pea seed','Root & brassica seed','Green bean seed','Celery & fennel seed'}
print('unplaced',sorted(allk-placed)); print('extra tt',sorted(set(TT)-placed))
out={'c':'C3','rev':True,'lead':d['lead'],'ax':AX,'key':KEY,'b':d.get('b',[]),'depts':depts}
json.dump(out,open('C3.new.json','w'),ensure_ascii=False,indent=1)
ren={"Bean & pea seed":"Runner & French bean seed","Green bean seed":"Runner & French bean seed","Root & brassica seed":"Radish seed","Celery & fennel seed":"Celery, celeriac & fennel seed"}
json.dump(ren,open('renames.json','w'),indent=1,ensure_ascii=False)
