import json,copy,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from spec_tt import TT
from spec_struct import *
R='/home/user/Possession-Taxonomy/rebuild/'
src=json.load(open(R+'out/J8.json'))
old={}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']: old[k['n']]=k
before=dict(d=len(src['depts']),s=sum(len(d['s']) for d in src['depts']),k=len(old),x=sum(len(k.get('x',[])) for k in old.values()))
REN={"Gluten-free bread":"Sliced & tin loaf","Dairy-free ice cream":"Ice cream tub","Countline & chocolate bar snack":"Countline","Cone":"Ice cream cone","Frozen yogurt":"Frozen yogurt"}
REN.pop("Frozen yogurt")
def A(n,d,y="",mk="",s=""): return dict(n=n,a="",d=d,mk=mk,y=y,s=s,v=[])
def newk(n,a,d,s,x=()):
    return dict(n=n,a=a,d=d,s=s,x=list(x))
B=WL+"breads";P=WL+"pastries";C=WL+"cakes";CK=WL+"cookies";CR=WL+"crackers";CF=WL+"confectionery_brands";FD=WL+"frozen_desserts";CB=WL+"chocolate_bar_brands";SN=WL+"snack_foods"
NEW={
"Quick bread & cornbread":newk("Quick bread & cornbread","cornbread · banana bread · bannock","Breads raised with baking soda or powder instead of yeast, such as cornbread, banana bread and bannock.",B,[A("Cornbread","Bread made with cornmeal, baked in a skillet or tin.",s=B),A("Banana bread","Sweet loaf bread made with mashed bananas.",s=B),A("Bannock","Flat quick bread cooked on a griddle or baked.",s=B),A("Broa","Maize bread from Portugal and Brazil.",s=B)]),
"English muffin & crumpet":newk("English muffin & crumpet","muffin (UK) · pikelet","Round griddle-cooked yeast breads split and toasted, such as English muffins and crumpets.",B,[A("English muffin","Split, toasted yeast bread cooked on a griddle; called just muffin in the UK.",s=B),A("Crumpet","Griddle-cooked batter bread with holes on top for butter.",s=B)]),
"Puff pastry":newk("Puff pastry","mille-feuille · palmier","Flaky pastry from dough folded with butter, sold as palmiers, mille-feuilles, cream horns and pithiviers.",P,[A("Mille-feuille","Layers of puff pastry with cream or custard.",s=P),A("Palmier","Sugared puff pastry folded and cut into hearts.",s=P),A("Cream horn","Puff pastry spiral filled with cream.",s=P),A("Pithivier","Round puff pastry pie, usually with almond cream.",s=P)]),
"Choux pastry":newk("Choux pastry","éclair · profiterole","Light hollow pastry filled with cream, such as éclairs, profiteroles and Paris–Brest.",P,[A("Éclair","Finger of choux pastry with cream filling and icing.",s=P),A("Profiterole","Small choux puff, called a cream puff in the US.",s=P),A("Paris–Brest","Ring of choux pastry filled with praline cream.",s=P),A("Croquembouche","Tower of choux puffs bound with caramel.",s=P)]),
"Turnover & strudel":newk("Turnover & strudel","empanada · apple strudel","Pastry wrapped around a filling, such as strudel, empanadas and panzerotti.",P,[A("Apple strudel","Thin rolled pastry wrapped around spiced apple.",s=P),A("Empanada","Folded pastry turnover filled with meat, cheese or fruit.",s=P),A("Panzerotti","Small folded Italian turnover.",s=P)]),
"Tart & shortcrust pastry":newk("Tart & shortcrust pastry","egg tart · Bakewell tart","Short or sweet pastry cases with a set filling, such as Bakewell tarts, egg tarts and Linzer tortes.",P,[A("Bakewell tart","English shortcrust tart with jam and almond sponge.",s=P),A("Linzer torte","Lattice-topped tart with nut pastry and jam.",s=P),A("Egg tart","Pastry case with a baked egg custard, sold in Chinese bakeries.",s=SN)]),
"Cupcake & muffin":newk("Cupcake & muffin","fairy cake · magdalena","Small single-portion cakes baked in a paper case, from frosted cupcakes to muffins.",C,[A("Cupcake","Small frosted cake baked in a paper case; from the United States.",s=C),A("Magdalena","Spanish muffin-style small cake.",s=C)]),
"Madeleine & financier":newk("Madeleine & financier","small French cakes","Small French sponge cakes baked in moulds, the shell-shaped madeleine and the almond financier.",C,[A("Madeleine","Small shell-shaped sponge cake from Lorraine.",s=C),A("Financier","Small almond-flour cake from France.",s=C)]),
"Loaf & Bundt cake":newk("Loaf & Bundt cake","tin cake · pound cake","Plain butter cakes baked in a loaf tin or ring mould, such as Madeira cake, Bundt cake and Battenberg.",C,[A("Madeira cake","English butter cake flavoured with lemon.",s=C),A("Bundt cake","Cake baked in a ring-shaped fluted tin.",s=C),A("Battenberg cake","Chequered sponge cake wrapped in marzipan.",s=C)]),
"Cheesecake":newk("Cheesecake","baked cheesecake · Japanese cheesecake","Cake of soft cheese on a biscuit or sponge base, baked or set without baking.",C,[A("Japanese cheesecake","Soufflé-style light cheesecake from Japan.",y="",s=C)]),
"Cheese cracker":newk("Cheese cracker","cheddar cracker","Small baked crackers made with cheese, often square or fish-shaped.",CR,[A("Cheez-It","Square baked cheese cracker.",s=CR),A("Cheese Nips","Small square cheese cracker.",s=CR)]),
"Graham cracker":newk("Graham cracker","graham","Sweet wholemeal cracker, flat and scored, used for snacking and pie bases.",CR),
"Oyster & animal cracker":newk("Oyster & animal cracker","soup cracker · fish cracker","Tiny crackers for soup or snacking, in oyster, animal or fish shapes.",CR,[A("Oyster cracker","Small round cracker served with soup.",s=CR),A("Animal cracker","Small biscuit in animal shapes.",s=CR),A("Goldfish","Small fish-shaped baked cheese cracker.",s=CR)]),
"Aerated chocolate bar":newk("Aerated chocolate bar","bubble chocolate","Chocolate bars whipped with air bubbles for a light, melting texture.",CB,[A("Aero","Aerated milk chocolate bar.",s=CB),A("Dairy Milk Bubbly","Aerated version of Dairy Milk.",s=CB)]),
"Coconut bar":newk("Coconut bar","coconut chocolate","Chocolate-coated bars with a coconut centre.",CB,[A("Bounty","Coconut centre bar coated in chocolate.",s=CB),A("Mounds","Dark chocolate coconut bar.",s=CB),A("Almond Joy","Coconut bar with almonds in chocolate.",s=CB)]),
"Candy floss":newk("Candy floss","cotton candy · fairy floss","Spun sugar threads sold in bags, tubs or on sticks.",CF,[A("Fluffy Stuff","Brand of cotton candy sold in tubs.",s=CF)]),
"Novelty sweets":newk("Novelty sweets","toy candy · candy dispenser","Sweets sold for the shape or toy, such as dispensers, wax shapes and whistle lollipops.",CF,[A("Pez","Candy sold in character dispensers.",s=CF),A("Wax Lips","Sweet wax in the shape of lips, chewed for fun.",s=CF),A("Whistle Pops","Lollipops with a whistle handle.",s=CF)]),
"Fruit snack":newk("Fruit snack","fruit leather · fruit roll","Chewy fruit-flavoured sheets, rolls or shapes sold as a snack sweet.",CF,[A("Fruit Roll-Ups","Rolled fruit-flavoured sheet snack.",s=CF),A("Fruit by the Foot","Long strip of fruit snack.",s=CF),A("Fruit Gushers","Fruit snack with a liquid centre.",s=CF)]),
"Frozen custard":newk("Frozen custard","soft serve · custard ice cream","Dense ice cream made with egg yolk, served soft or sold in pints; includes soft serve.",FD),
"Shaved ice":newk("Shaved ice","snow cone · bingsu · sno-ball","Finely shaved ice with syrup or toppings, sold as cones, bowls or kits.",FD,[A("Bingsu","Korean shaved ice dessert with sweet toppings.",s=FD),A("Snow cone","Shaved ice in a cup with flavoured syrup.",s=FD),A("Sno-ball","Fine shaved ice with syrup, from New Orleans.",s=FD)]),
}
# demotions: (kind, archetype) -> 'm' generic or 'r' maker range
DEM_M=[("Sliced & tin loaf","Pre-sliced wrapped loaf"),("Celebration cake","Birthday cake"),("Celebration cake","Wedding cake"),("Doughnut","Ring doughnut"),("Doughnut","Doughnut holes"),("Rice cake","Puffed rice cake"),("Pork scratchings & chicharrón","Pork scratchings"),("Pork scratchings & chicharrón","Pork rinds"),("Chocolate Easter egg","Hollow chocolate egg"),("Seasonal moulded chocolate","Chocolate bunny"),("Seasonal moulded chocolate","Chocolate Advent calendar"),("Chocolate-coated nuts & fruit","Chocolate-covered raisin"),("Pretzel","Chocolate-covered pretzel"),("Pretzel","Hard pretzel"),("Mozartkugel & marzipan chocolate","Chocolate-covered marzipan"),("Popcorn","Microwave popcorn"),("Wafer","Rolled wafer"),("Macaron & meringue","Meringue"),("Rye & wholegrain bread","Whole wheat bread"),("Liquorice","Salty liquorice"),("Ice cream sandwich","Wafer ice cream sandwich"),("Seaweed snack","Seasoned gim"),("Dragée & sugared almond","Silver dragées"),("Praline & filled bonbon","Liqueur bonbon"),("Dulce de leche sweets","Dulce de leche")]
DEM_R=[("Single-origin dark chocolate",n) for n in ["Amedei single-origin bars","Michel Cluizel plantation bars","Domori Criollo range","Marou provincial origin bars","Dandelion origin bars","Askinosie single-origin bars","Pacari bars","Friis-Holm Nicaraguan bars","Fruition bars","Menakao Madagascar bars"]]+[("Couverture & baking chocolate",n) for n in ["Callebaut couverture","Baker's unsweetened chocolate"]]+[("Potato crisps",n) for n in ["Smiths crisps","Walkers crisps","Golden Wonder","Calbee Potato Chips","Torres","Terra Chips","McCoy's","Lay's"]]+[("Kettle crisps",n) for n in ["Cape Cod Potato Chips","Kettle Brand","Tyrrells","Zapp's"]]+[("Rice cracker & senbei","Want Want rice crackers"),("Seaweed snack","Tao Kae Noi"),("Crispbread","Wasa"),("Crispbread","Ryvita"),("Crispbread","Finn Crisp Original"),("Crispbread","Peter's Yard sourdough crispbread"),("Gummy & jelly sweet","Haribo Starmix and mixes"),("Chewing gum","Extra and Orbit"),("Ice cream tub","Ben & Jerry's pints"),("Ice cream tub","Häagen-Dazs pints"),("Ice cream tub","Jeni's pints"),("Ice cream tub","Salt & Straw pints"),("Frozen yogurt","Tart frozen yogurt with toppings"),("Frozen yogurt","Self-serve frozen yogurt")]
MOVE_X=[("Sliced & tin loaf","Soda bread","Quick bread & cornbread"),("Wafer","Fortune cookie","Cookie"),("Hard candy & boiled sweet","Pez","Novelty sweets")]
DEMOTED=[];MOVED=[]
def norm(s):return s.lower().strip()
# merge renamed kinds first
kinds={n:copy.deepcopy(k) for n,k in old.items()}
for o,nw in REN.items():
    if o not in kinds: print("missing",o);continue
    a=kinds.pop(o)
    if nw in kinds:
        t=kinds[nw]
        for key in('x','m','r'):t[key]=(t.get(key) or [])+(a.get(key) or [])
        t['a']=' · '.join([z for z in [t.get('a',''),a['n'].lower()] if z])
        MOVED.append(f"{o} -> {nw}")
    else:
        a['n']=nw;kinds[nw]=a;MOVED.append(f"{o} renamed {nw}")
kinds["Ice cream cone"]=kinds.get("Ice cream cone") or kinds.pop("Cone")
for n,k in NEW.items():kinds[n]=k
def find(kn,xn):
    for i,a in enumerate(kinds[kn].get('x',[])):
        if a['n']==xn:return i
    raise SystemExit(f"no archetype {kn}/{xn}")
for kn,xn in DEM_M+DEM_R:
    kk=kn
    if kk=="Frozen yogurt" and kk not in kinds:raise SystemExit
    k=kinds[kk];a=k['x'].pop(find(kk,xn))
    mk=a.get('mk','')
    if (kn,xn) in DEM_R:
        k.setdefault('r',[]).append([xn,mk])
    else:
        k.setdefault('m',[]).append([xn,mk])
    for v in a.get('v',[]):
        k.setdefault('m',[]).append([v['n'],v.get('mk') or mk])
    DEMOTED.append(f"{kn}/{xn} -> {'r' if (kn,xn) in DEM_R else 'm'}")
for kn,xn,to in MOVE_X:
    a=kinds[kn]['x'].pop(find(kn,xn));kinds[to].setdefault('x',[]).append(a)
# dedupe m/r
for k in kinds.values():
    for key in('m','r'):
        if k.get(key):
            seen=[];[seen.append(t) for t in k[key] if t not in seen];k[key]=seen
# see links
SEE={
"Hot chocolate bomb & drinking flakes":[["J6","Drinking chocolate","a powder or flake drink base"]],
"Couverture & baking chocolate":[["J6","Cocoa powder","cocoa for baking"]],
"Gianduja":[["J5","Hazelnut-chocolate spread","spread made from hazelnut and chocolate"]],
"Granola & cereal bar":[["J5","Granola","loose granola"],["J8","Flapjack","baked oat bar"]],
"Popcorn":[["J5","Popcorn kernels","kernels to pop at home"]],
"Seaweed snack":[["J5","Dried seaweed","plain dried seaweed"]],
"Celebration cake":[["J5","Cake and baking mixes","mixes to bake at home"],["J8","Ice cream cake","frozen cake"]],
"Puff pastry":[["J5","Ready-made pastry","pastry sheets to bake with"]],
"Gingerbread & Lebkuchen":[["J8","Speculoos & spiced biscuit","spiced biscuit"]],
"Speculoos & spiced biscuit":[["J8","Gingerbread & Lebkuchen","spiced festive bake"]],
"Wafer":[["J8","Ice cream cone","wafer cone"]],
"Ice cream cone":[["J8","Wafer","dry wafer"]],
"Mochi ice cream":[["J8","Wagashi","Japanese sweet with a mochi shell"]],
"Chocolate-coated biscuit":[["J8","Countline","wrapped bar snack"]],
"Countline":[["J8","Chocolate-coated biscuit","biscuit with a chocolate coat"]],
"Rice cake":[["J8","Rice cracker & senbei","baked or fried rice cracker"]],
"Rice cracker & senbei":[["J8","Rice cake","puffed rice cake"]],
"Oatcake":[["J8","Flapjack","baked oat bar"]],
"Flapjack":[["J8","Oatcake","savoury oat biscuit"]],
"Danish pastry":[["J8","Doughnut","fried sweet dough"]],
"Panettone & pandoro":[["J8","Enriched bread","rich yeast bread"]],
"Fruitcake":[["J8","Candied fruit & marron glacé","candied fruit used inside"]],
"Pretzel":[["J8","Bagel & rolls","boiled soft pretzel-style roll"]],
"Grissini & breadsticks":[["J8","Italian bread","bread from the same region"]],
"Matzo":[["J8","Flatbread","unleavened flatbread"]],
"Crispbread":[["J8","Rye & wholegrain bread","rye bread"]],
"Cookie":[["J8","Ice cream sandwich","cookie around ice cream"]],
"Marzipan":[["J8","Mozartkugel & marzipan chocolate","marzipan in chocolate"]],
"Baklava & syrup pastries":[["J8","Mithai","syrup sweets of South Asia"]],
"Cheesecake":[["J8","Castella & sponge cake","Japanese cheesecake is a sponge cousin"]],
}
for kn,v in SEE.items(): kinds[kn]['see']=v
# assemble
out={"c":"J8","rev":True,"lead":src['lead'],"b":src.get('b',[]),"ax":CAT_AX,"key":CAT_KEY,"depts":[]}
used=set()
for dn,dsp in DEPTS.items():
    od=[d for d in src['depts'] if d['n']==dn][0]
    dp={"n":dn,"mode":od['mode'],"t":dsp['t'],"ax":dsp['ax']}
    for kk in('note','b'):
        if od.get(kk):dp[kk]=od[kk]
    dp['s']=[]
    for sn,st,sax,kl in dsp['shelves']:
        sh={"n":sn,"t":st,"ax":sax,"k":[]}
        for kn in kl:
            k=kinds[kn];k.pop('t',None)
            assert kn in TT,kn
            k['tt']=TT[kn];used.add(kn)
            sh['k'].append(k)
        dp['s'].append(sh)
    out['depts'].append(dp)
miss=set(kinds)-used
assert not miss,miss
extra=set(TT)-used
assert not extra,extra
# order x within kinds left as is
json.dump(out,open('J8_new.json','w'),ensure_ascii=False,indent=1)
json.dump({o:n for o,n in REN.items()},open('renames.json','w'),ensure_ascii=False,indent=1)
after=dict(d=len(out['depts']),s=sum(len(d['s']) for d in out['depts']),k=len(kinds),x=sum(len(k.get('x',[])) for k in kinds.values()))
json.dump(dict(before=before,after=after,dem=DEMOTED,moved=MOVED),open('stats.json','w'),ensure_ascii=False,indent=1)
print(before,after,len(DEMOTED))
