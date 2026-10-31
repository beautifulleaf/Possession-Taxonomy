import json,sys,copy,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_J5')
from tt import TT
B='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(B+'work/STR_J5/bak/J5.json'))
K={};DEPT={}
for dp in d['depts']:
    DEPT[dp['n']]=dp
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=dict(dept=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))
W='https://en.wikipedia.org/wiki/'
def nk(n,a,dd,s,x=None,m=None,r=None,tg=None):
    k={'n':n,'a':a,'d':dd,'s':W+s}
    if x: k['x']=x
    if m: k['m']=m
    if r: k['r']=r
    if tg: k['tg']=tg
    assert n not in K,n
    K[n]=k; return k
def ar(n,dd,s,mk='',y='',a=''):
    return {'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':W+s,'v':[]}
# ---------- renames
REN={'Dried beans':'Heirloom beans','Somen':'Somen and hiyamugi','Prepared wasabi':'Wasabi and karashi'}
for o,n in REN.items():
    K[n]=K.pop(o); K[n]['n']=n
K['Heirloom beans']['a']='haricot types · heirloom beans · dried beans'
K['Heirloom beans']['d']='Dried heirloom and specialty beans sold by their own names, mostly common beans with speckled or mottled coats; the market classes have their own kinds.'
K['Somen and hiyamugi']['d']='Very thin Japanese wheat noodles: somen under 1.3 mm, stretched with oil and air-dried, and slightly thicker hiyamugi, both eaten cold.'
K['Somen and hiyamugi']['a']='hiyamugi'
K['Wasabi and karashi']['a']='prepared wasabi · Japanese mustard · karashi'
K['Wasabi and karashi']['d']='Pungent Japanese pastes sold in tubes and powder: wasabi, mostly made from horseradish, and hot yellow karashi mustard.'
K['Wasabi and karashi']['s']=W+'List_of_condiments'
K['Wasabi and karashi']['tt_pre']=1
TT['Wasabi and karashi']=[["Paste",["Wasabi (real rhizome)","Wasabi (horseradish-based)","Karashi mustard"]],["Form",["Tube","Powder"]]]
TT['Somen and hiyamugi']=[["Thickness",["Somen (under 1.3 mm)","Hiyamugi (1.3-1.7 mm)"]]]
TT['Navy (haricot) beans']=[["Class",["Navy (pea bean)","Great Northern"]]]
REN_OUT={o:n for o,n in REN.items()}
# ---------- archetype demotions
def rm_x(kn,names,to_r=None,note=None):
    k=K[kn]; keep=[];
    for a in k.get('x',[]):
        if a['n'] in names:
            if to_r: k.setdefault('r',[]).append([a['n'],a.get('mk','') or to_r])
        else: keep.append(a)
    if keep: k['x']=keep
    else: k.pop('x',None)
DEM=[]
def dem(kn,names,to_r=None):
    rm_x(kn,set(names),to_r); DEM.append((kn,list(names),'range' if to_r else 'type/definition'))
dem('Estate olive oils',['Castillo de Canena','Cobram Estate','California Olive Ranch'],'x')
dem('Potato gnocchi',['Potato gnocchi']); dem('Flattened rice',['Poha']); dem('Bread flour',['Italian Type 00'])
dem('Palm and coconut sugar',['Coconut sugar']); dem('Date syrup and fruit molasses',['Date syrup'])
dem('Curry powder',['Madras, Bombay and Bengal curry powders'])
dem('Frozen ready meals',["Stouffer's lasagna",'Lean Cuisine',"Amy's vegetable pot pie","Marie Callender's frozen entrées"],'x')
dem('Frozen pizza',["Totino's frozen pizza",'Tombstone','Red Baron','DiGiorno','Freschetta','Mama Celeste'],'x')
dem('Tater tots and hash browns',['Frozen hash browns'])
dem('Frozen Yorkshire puddings and accompaniments',["Aunt Bessie's Yorkshire puddings"],'x')
dem('Baby purées and pouches',['Gerber baby food',"Clapp's baby food",'Beech-Nut baby food','Heinz baby food',"Earth's Best","Ella's Kitchen"],'x')
dem('Beer kits',['Coopers homebrew kits','Muntons Flagship kits'],'x')
dem('Heirloom beans',['Tarbais bean','Judiones de la Granja'])
# r fixups: use maker names for demoted ranges
def fixr(kn,mp):
    K[kn]['r']=[[n,mp.get(n,mk)] for n,mk in K[kn].get('r',[])]
fixr('Estate olive oils',{'Castillo de Canena':'Castillo de Canena','Cobram Estate':'Cobram Estate','California Olive Ranch':'California Olive Ranch'})
fixr('Frozen ready meals',{"Stouffer's lasagna":"Stouffer's",'Lean Cuisine':'Lean Cuisine'})
fixr('Frozen pizza',{"Totino's frozen pizza":"Totino's",'Tombstone':'Tombstone','Red Baron':'Red Baron','DiGiorno':'DiGiorno','Freschetta':'Freschetta','Mama Celeste':'Celeste'})
fixr('Frozen Yorkshire puddings and accompaniments',{"Aunt Bessie's Yorkshire puddings":"Aunt Bessie's"})
fixr('Baby purées and pouches',{'Gerber baby food':'Gerber',"Clapp's baby food":"Clapp's",'Beech-Nut baby food':'Beech-Nut','Heinz baby food':'Heinz',"Earth's Best":"Earth's Best","Ella's Kitchen":"Ella's Kitchen"})
fixr('Beer kits',{'Coopers homebrew kits':'Coopers','Muntons Flagship kits':'Muntons'})
# junk m entries
for kn,bad in [('Infant cereals',['Infant cereal']),('Dried and instant soup',['Dried soup'])]:
    K[kn]['m']=[m for m in K[kn].get('m',[]) if m[0] not in bad]
    if not K[kn]['m']: K[kn].pop('m')
# ---------- new archetypes on existing kinds
def addx(kn,items): K[kn].setdefault('x',[]).extend(items)
P='List_of_pasta'
addx('Long-strand pasta',[ar('Pici','Thick hand-rolled Tuscan strands, made without egg.',P),ar('Bigoli','Thick Veneto strands pressed through a bronze die, traditionally wholewheat.',P),ar('Busiate','Sicilian long twists wound round a thin rod.',P)])
addx('Egg pasta, ribbons and nests',[ar('Tagliolini','Thin egg-pasta ribbons, narrower than tagliatelle.',P)])
addx('Tube pasta',[ar('Mezze maniche','Short wide tubes, the name meaning half sleeves.',P),ar('Tortiglioni','Wide tubes with deep spiral ridges.',P)])
addx('Short and twisted pasta',[ar('Casarecce','Short rolled strips with an S-shaped section.',P),ar('Gemelli','Two strands twisted together into a short spiral.',P),ar('Campanelle','Bell-shaped pasta with a frilled edge.',P),ar('Radiatori','Short ruffled shapes that look like radiators.',P),ar('Malloreddus','Small ridged shells of Sardinian semolina dough.',P)])
addx('Filled pasta',[ar('Cappelletti','Little hat-shaped filled pasta from Emilia-Romagna.',P)])
addx('Soup pasta',[ar('Ditali','Short smooth tubes cooked in soups and with beans.',P),ar('Corallini','Tiny short tubes for broth.',P),ar('Alphabet pasta','Tiny letter shapes for soup.',P)])
R='List_of_rice_cultivars'
addx('Long-grain rice',[ar('Carolina Gold','Heritage long-grain rice of the American Carolinas.',R)])
addx('Medium- and short-grain rice',[ar('Nishiki','California medium-grain rice sold for sushi.',R)])
addx('Risotto rice',[ar('Baldo','Italian rice used for risotto and desserts.',R)])
addx('Paella rice',[ar('Senia','Spanish round pearly rice of the Valencia region.',R),ar('Bahia','Spanish pearly round rice grown for paella.',R)])
addx('Red and black rice',[ar('Wehani','Red-brown aromatic rice grown in California.',R),ar('Venere','Italian black aromatic rice.',R)])
N='List_of_noodles'
addx('Chinese wheat and egg noodles',[ar('Misua','Very thin salted wheat vermicelli, eaten in soup.',N),ar('Biangbiang noodles','Wide hand-pulled belt noodles from Shaanxi.',N)])
H='List_of_hop_varieties'
addx('Hops',[ar('Northern Brewer','English bittering and aroma hop bred at Wye College.',H,y='1934'),ar('Challenger','English dual-purpose hop.',H,y='1972'),ar('Target','English high-alpha bittering hop.',H),ar('Perle','German dual-purpose hop.',H),ar('Tettnang','German noble-type aroma hop.',H,a='Tettnanger'),ar('Magnum','German high-alpha bittering hop from the Hüll research centre.',H,y='1980'),ar('Chinook','American hop with pine and grapefruit notes.',H,y='1985'),ar('Centennial','American dual-purpose hop, called a super Cascade.',H,y='1990'),ar('Amarillo','American citrus-and-floral aroma hop.',H),ar('Columbus','American high-alpha hop.',H),ar('Motueka','New Zealand aroma hop.',H)])
addx('Barbecue rubs and seasonings',[ar('Old Bay Seasoning','Celery-salt based seafood seasoning from Baltimore.','Spice_mix')])
# ---------- new kinds
O='List_of_vegetable_oils'
nk('Soybean oil','','Oil pressed from soybeans, the most used cooking oil in the United States, often sold simply as vegetable oil.',O)
nk('Corn oil','maize oil','Oil pressed from maize germ, bland and used for frying and baking.',O)
nk('Palm oil','','Oil from the fruit of the oil palm, solid at room temperature and found in margarines and frying fats; red palm oil is unrefined.',O)
nk('Safflower oil','','Oil pressed from safflower seed, high-oleic or high-linoleic, with a high smoke point.',O)
nk('Rice bran oil','','Oil pressed from rice bran, used for frying in Japan and India.',O)
nk('Grapeseed oil','','Mild oil pressed from the seeds left after winemaking.',O)
for n in ['Soybean oil','Corn oil','Palm oil','Safflower oil','Rice bran oil','Grapeseed oil']: pass
TT['Soybean oil']=[["Refining",["Refined","Cold-pressed"]]]
TT['Corn oil']=[["Refining",["Refined","Unrefined"]]]
TT['Palm oil']=[["Colour",["Refined (pale)","Red (unrefined)"]],["Sourcing",["Certified sustainable"]]]
TT['Safflower oil']=[["Fatty acid",["High-oleic","High-linoleic"]]]
TT['Rice bran oil']=[["Refining",["Refined","Unrefined"]]]
TT['Grapeseed oil']=[["Pressing",["Cold-pressed","Refined"]]]
nk('Sake rice','sakamai','Large-grained rice bred for brewing sake, with a starchy core, sold to home brewers and collectors.',R,x=[ar('Yamada Nishiki','The leading sake rice, prized for fine sake.',R),ar('Gohyakumangoku','Sake rice widely grown in Niigata and Hokuriku.',R),ar('Omachi','Old sake rice variety grown in Okayama.',R)])
TT['Sake rice']=[["Milling",["Polished (seimai)","Unpolished"]]]
nk('Korean wheat noodles','kalguksu · jjolmyeon','Korean wheat noodles: knife-cut kalguksu for soup and thin chewy jjolmyeon for spicy cold dishes.',N,x=[ar('Kalguksu','Knife-cut Korean wheat noodles served in broth.',N),ar('Jjolmyeon','Chewy thin Korean wheat noodles eaten with spicy sauce.',N)])
TT['Korean wheat noodles']=[["Freshness",["Fresh","Dried"]]]
# beans
PV='Phaseolus_vulgaris'
nk('Pinto beans','','Speckled beige-and-brown common beans, the usual bean for refried beans.',PV)
nk('Black beans','black turtle beans','Small glossy black common beans used in Latin American cooking.',PV)
nk('Borlotti beans','cranberry beans','Plump cream beans streaked with red, a staple of Italian soups; also sold as cranberry beans.',PV)
nk('Flageolet beans','','Small pale green French beans, delicate and creamy, eaten with lamb.',PV)
for n in ['Pinto beans','Black beans','Borlotti beans','Flageolet beans']: TT[n]=[["Pack",["Dried","Tinned"]]] if n!='Black beans' else [["Pack",["Dried","Tinned"]]]
LG='Legume'
nk('Black-eyed peas','cowpeas · black-eyed beans','Small cream pulses with a black spot, cooked in West African, Indian and Southern US dishes.',LG)
nk('Broad beans (dried)','fava beans','Dried seeds of Vicia faba, sold whole, skinned or split, for stews and falafel.',LG)
nk('Adzuki beans','azuki beans','Small red beans of East Asia, cooked sweet into pastes and desserts.',LG)
TT['Black-eyed peas']=[["Pack",["Dried","Tinned"]]]
TT['Broad beans (dried)']=[["Form",["Whole with skin","Skinned","Split"]]]
TT['Adzuki beans']=[["Form",["Whole","Paste (anko)"]]]
FL='Flour'
nk('Nut and root flours','almond flour · cassava flour · chestnut flour','Flours ground from nuts such as almond, chestnut and coconut, or from roots such as cassava and taro, used for gluten-free baking.',FL)
TT['Nut and root flours']=[["Source",["Almond","Chestnut","Coconut","Cassava","Taro"]]]
nk('Sorghum and teff flour','','Wholegrain flours of sorghum or teff, the base of Ethiopian injera and a gluten-free baking flour.',FL)
TT['Sorghum and teff flour']=[["Grain",["Sorghum","Teff"]],["Colour",["White","Brown"]]]
CO='List_of_condiments'
nk('Tartar sauce','tartare sauce','Cold mayonnaise-based sauce with chopped gherkins and capers, served with fried fish.',CO)
nk('Mint sauce','','British sauce of chopped mint in sweetened vinegar, served with roast lamb.',CO)
nk('Cranberry sauce','','Sweet-tart sauce of cooked cranberries, served with turkey and game.',CO)
nk('Plum sauce','duck sauce','Sweet-and-sour Chinese sauce of plums, vinegar and sugar, served with duck and spring rolls.',CO)
nk('Peanut sauce','satay sauce','Spiced sauce of ground peanuts used in Indonesian and Thai dishes, sold as a jar or paste.',CO)
nk('Banana ketchup','banana sauce','Sweet red-brown Filipino table sauce made from bananas.',CO)
nk('Ssamjang','','Thick Korean dipping paste of doenjang and gochujang, eaten with leaves and grilled meat.',CO)
nk('Yuzu kosho','yuzukoshō','Japanese paste of yuzu zest, chilli and salt.',CO)
for n,t in {'Tartar sauce':[["Texture",["Smooth","Chunky"]]],'Mint sauce':[["Form",["Liquid","Jelly"]]],'Cranberry sauce':[["Texture",["Whole berry","Jellied"]]],'Plum sauce':[["Taste",["Sweet-and-sour","Spicy"]]],'Peanut sauce':[["Texture",["Smooth","Crunchy"]],["Heat",["Mild","Hot"]]],'Banana ketchup':[["Colour",["Red-dyed","Natural brown"]]],'Ssamjang':[["Heat",["Mild","Spicy"]]],'Yuzu kosho':[["Pepper",["Green chilli","Red chilli"]]]}.items(): TT[n]=t
SM='Spice_mix'
nk('Baharat','','Middle Eastern blend of black pepper, cumin, coriander, cinnamon and other warm spices.',SM)
nk('Tandoori masala','','South Asian blend of chilli, cumin, coriander and ginger used to season grilled meat and vegetables.',SM)
nk('Panch phoron','five-spice (Bengali)','Whole-seed blend of five spices (fenugreek, nigella, mustard, cumin and fennel) fried in oil at the start of cooking.',SM)
nk('Quatre épices','','French blend of pepper, nutmeg, cloves and ginger for charcuterie and stews.',SM)
nk('Mixed spice','pudding spice','British blend of sweet spices such as cinnamon, nutmeg and allspice for cakes and puddings.',SM)
for n,t in {'Baharat':[["Region",["Turkish","Gulf","Levantine"]]],'Tandoori masala':[["Colour",["Red","Natural"]]],'Panch phoron':[["Form",["Whole seeds"]]],'Quatre épices':[["Form",["Ground"]]],'Mixed spice':[["Form",["Ground"]]]}.items(): TT[n]=t
DF='List_of_dried_foods'
nk('Fruit leather','lavashak · tklapi · aam papad','Fruit pulp dried into thin sheets, from Persian lavashak and Georgian tklapi to Indian mango aam papad.',DF,x=[ar('Lavashak','Persian sheets of dried fruit pulp.',DF),ar('Tklapi','Georgian dried plum sheet.',DF),ar('Aam papad','Indian sheets of sun-dried mango pulp.',DF)])
TT['Fruit leather']=[["Fruit",["Plum","Mango","Apricot","Mixed"]]]
nk('Dried root vegetables','chuño · dried potato','Roots and tubers dried for storage: freeze-dried Andean potato (chuño), dried daikon and instant potato flakes.',DF,x=[ar('Chuño','Freeze-dried Andean potato.',DF)])
TT['Dried root vegetables']=[["Root",["Potato","Daikon","Sweet potato"]]]
FF='List_of_frozen_food_brands'
nk('Frozen waffles and breakfast foods','','Waffles, pancakes and hash-brown breakfasts sold frozen and heated in a toaster or oven.',FF,r=[['Eggo waffles','Eggo']])
nk('Stuffed sandwiches and turnovers','','Pastry or bread pockets filled with meat, cheese or vegetables, sold frozen and microwaved or baked.',FF,r=[['Hot Pockets','Hot Pockets']])
TT['Frozen waffles and breakfast foods']=[["Item",["Waffles","Pancakes","Hash browns"]]]
TT['Stuffed sandwiches and turnovers']=[["Filling",["Meat","Cheese","Vegetable"]]]
for k in ('Tater tots and hash browns','Frozen Yorkshire puddings and accompaniments','Frozen crispy pancakes and coated savouries','Pizza rolls','Tzatziki','Infant cereals','Toddler meals and snacks','Tinned tomatoes'): pass
# ---------- see
SEE={
'Horseradish':[['J4','Horseradish','the fresh root']],
'Wasabi and karashi':[['J4','Fresh wasabi','the fresh rhizome']],
'Cooking sake':[['J7','Sake (junmai, honjozo, ginjo & daiginjo)','sake sold for drinking']],
'Brewing yeast':[['C3','Ale yeast','living culture for brewing'],['C3','Lager yeast','living culture for brewing']],
'Fermented bean curd':[['J3','Tofu','fresh tofu']],
'Peanut butter':[['J8','Peanuts','whole peanuts as a snack']],
'Dates':[['J4','Date','fresh dates']],
'Dried seaweed':[['J4','Wakame','fresh sea vegetable']],
'Dried mushrooms':[['J4','Shiitake','fresh mushroom']],
'Sun-dried tomatoes':[['J4','Tomato','fresh tomato']],
'Dried chilli':[['J4','Chilli','fresh chilli']],
'Ground ginger':[['J4','Ginger','fresh root']],
'Table olives':[['J4','Fresh olive','the uncured fruit']],
'Dried herbs':[['J4','Mixed herbs','fresh herbs']],
'Granola':[['J8','Granola & cereal bar','granola as a bar']],
'Desiccated coconut':[['J4','Coconut','fresh coconut']],
'Cider vinegar':[['C3','Vinegar mother','culture for making vinegar'],['J9','Drinking vinegar & shrub','sold to drink']],
'Wine vinegar':[['J9','Drinking vinegar & shrub','sold to drink']],
'Chilli paste':[['J5','Gochujang','fermented Korean chilli paste']],
'Gochujang':[['J5','Chilli paste','unfermented chilli pastes']],
'Doubanjiang':[['J5','Chilli paste','unfermented chilli pastes']],
'Kimchi':[['J5','Sauerkraut','salt-fermented cabbage without chilli']],
'Sauerkraut':[['J5','Kimchi','chilli-fermented cabbage']],
'Soy sauce':[['J5','Kecap manis','sweet Indonesian soy sauce']],
'Kecap manis':[['J5','Soy sauce','Japanese soy sauces']],
'Fish sauce':[['J5','Shrimp paste','fermented shrimp rather than fish liquid']],
'Mayonnaise':[['J5','Salad cream','thinner egg-and-oil sauce']],
'Salad cream':[['J5','Mayonnaise','thicker egg-and-oil sauce']],
'Ramen noodles':[['J5','Instant noodles','pre-cooked block form']],
'Instant noodles':[['J5','Ramen noodles','fresh and dried ramen']],
'Atta flour':[['J5','Wholemeal flour','wholemeal wheat flour']],
'Semolina':[['J5','Couscous','steamed semolina granules']],
'Curry powder':[['J5','Curry paste','wet curry base']],
'Curry paste':[['J5','Curry powder','dry blend']],
'Polenta and cornmeal':[['J5','Masa harina','nixtamalised maize flour']],
'Dashi and dashi ingredients':[['J5','Dried seaweed','kombu sold as a dried sea vegetable']],
'Molasses and treacle':[['J5','Jaggery','unrefined cane sugar block']],
'Honey':[['J5','Honeydew honey','honey from sap secretions']],
'Black pepper and peppercorns':[['J5','Sichuan pepper','a different plant despite the name']],
'Hazelnut-chocolate spread':[['J8','Chocolate bars','chocolate sold as a bar']],
'Frozen dumplings':[['J5','Fermented bean curd','']] if False else [],
'Gelatine and setting agents':[['J5','Jam and fruit spreads','setting with pectin and sugar']],
'Hot sauce':[['J5','Chilli oil and chilli crisp','chilli in oil']],
'Mustard':[['J5','Wasabi and karashi','Japanese mustard']],
'Cooking bitters':[['J7','Spirits','bitter liqueurs sold to drink']],
}
SEE={k:v for k,v in SEE.items() if v}
# ---------- layout
def S(n,t,ax,kinds): return dict(n=n,t=t,ax=ax,kinds=kinds)
L={}
L['Oils, vinegars & fats']=dict(
t='Pressed oils, rendered and hardened fats, and vinegars soured from wine, cider, grain or cane; seasoning sauces → Sauces & condiments, butter and ghee → Butter & ghee in the dairy category.',
ax='What is it made from: olives, other seeds and nuts, animal or hardened fat, or a soured liquid?',
shelves=[
S('Olive oil','Oil pressed from olives, sold by grade, by protected origin or under an estate name; other pressed oils → Seed, fruit & nut oils.','kinds by what the name guarantees: grade and protected origin first, then the producer',['Olive oil','Estate olive oils']),
S('Seed, fruit & nut oils','Oils pressed from a seed, fruit or nut other than the olive, for frying, dressing or flavour, such as sunflower, rapeseed, sesame and walnut; lard and shortening → Animal & hardened fats.','kinds by the crop pressed: everyday seed oils first, then tree-fruit and specialty oils',['Sunflower oil','Rapeseed oil','Soybean oil','Corn oil','Palm oil','Safflower oil','Rice bran oil','Groundnut oil','Coconut oil','Avocado oil','Grapeseed oil','Sesame oil','Mustard oil','Nut and seed oils']),
S('Animal & hardened fats','Solid fats for frying and baking: rendered lard and dripping, white vegetable shortening and margarine; liquid oils → Seed, fruit & nut oils.','kinds by how the fat is made: rendered animal fat, hardened plant fat, then spread',['Lard, dripping and poultry fat','Vegetable shortening','Margarine']),
S('Vinegars','Vinegar made by souring wine, cider, grain or cane juice, for dressing, pickling and cooking; vinegar drinks → J9 Drinking vinegar & shrub.','kinds by the liquid that was soured: grape, apple, grain, then cane and coconut',['Wine vinegar','Balsamic vinegar','Cider vinegar','Rice and grain vinegar','Malt and distilled vinegar','Cane and coconut vinegar']),
])
L['Rice, pasta & noodles']=dict(
t='Starchy staples cooked in water: milled rice, wheat pasta and couscous, and noodles; whole grains such as barley and bulgur → Grains, pulses & seeds, and ready-cooked noodle dishes belong to the Culinary taxonomy.',
ax='Is it a rice grain, an Italian-style wheat pasta, or an Asian noodle?',
shelves=[
S('Rice','Milled or whole-grain rice sold to cook, by grain shape and the dish it suits, such as basmati, risotto and sushi rice; rice noodles → Noodles, rice flour → Other flours & starches.','kinds by grain shape and use: long aromatic, long plain, medium and round, sticky, coloured, flattened, brewing',['Basmati rice','Jasmine rice','Long-grain rice','Medium- and short-grain rice','Risotto rice','Paella rice','Sticky rice','Red and black rice','Flattened rice','Sake rice']),
S('Pasta','Wheat pasta in dried, fresh or filled form, from spaghetti and penne to ravioli, plus couscous and gnocchi, which are cooked the same way; Asian wheat noodles → Noodles.','kinds by shape: strands, ribbons, tubes, twists, sheets, filled, soup shapes, then dumplings and granules',['Long-strand pasta','Egg pasta, ribbons and nests','Tube pasta','Short and twisted pasta','Sheet pasta','Filled pasta','Soup pasta','Potato gnocchi','Couscous']),
S('Noodles','Asian noodles of wheat, buckwheat, rice or bean starch, such as udon, soba, rice vermicelli and instant ramen; European pasta → Pasta.','kinds by the main flour or starch: wheat, buckwheat, rice, bean starch, then instant blocks',['Udon','Somen and hiyamugi','Ramen noodles','Chinese wheat and egg noodles','Korean wheat noodles','Soba','Rice noodles','Glass noodles','Instant noodles']),
])
L['Grains, pulses & seeds']=dict(
t='Seeds sold whole to cook or eat as they are: breakfast cereals, grains, edible seeds, beans, lentils, peas and dals; milled flours → Flour, sugar & baking, and tinned beans → Tins, jars & preserves.',
ax='Is it a breakfast cereal, a whole grain or seed, a bean, or a lentil, pea or dal?',
shelves=[
S('Breakfast cereals','Oat and grain cereals eaten for breakfast, from porridge oats to muesli, granola and cereal from the box; cereal bars → J8 Snack nuts & bars.','kinds by how much the buyer prepares: cook, soak, bake-and-eat, eat from the box',['Porridge oats','Muesli','Granola','Ready-to-eat breakfast cereal']),
S('Grains & seeds','Whole or cracked grains and seeds cooked as a side or a porridge, such as pearl barley, bulgur, farro, polenta, millet, quinoa and wild rice; rice → Rice, pasta & noodles.','kinds by plant family: wheat and barley, maize, small cereals, seed-like grains, then edible seeds',['Pearl barley','Cracked wheat and bulgur','Farro and ancient wheats','Polenta and cornmeal','Popcorn kernels','Millet','Quinoa','Buckwheat groats','Wild rice','Tapioca pearls','Edible seeds']),
S('Dried beans','Dried beans of the common bean group and its relatives, sold by market class, such as kidney, pinto and cannellini, or as named heirlooms; chickpeas and lentils → Lentils, peas & other pulses.','kinds by market class: common beans first, then lima and runner, then heirlooms',['Red kidney beans','Pinto beans','Black beans','Cannellini beans','Navy (haricot) beans','Borlotti beans','Flageolet beans','Lima and butter beans','Runner beans (dried)','Heirloom beans']),
S('Lentils, peas & other pulses','Dried lentils, chickpeas, split pulses and the beans of other plant families, such as black-eyed peas, broad beans and adzuki; common beans → Dried beans.','kinds by plant: lentil, split dal, chickpea, cowpea, broad bean, adzuki',['Lentils','Split pulses and dals','Chickpeas','Black-eyed peas','Broad beans (dried)','Adzuki beans']),
])
L['Flour, sugar & baking']=dict(
t='Baking and thickening basics: milled flours and starches, sugars and sweeteners, raising and setting agents, flavourings and ready mixes; syrups and honey → Honey, syrups & spreads, bread and cakes → Bread & bakery.',
ax='What does it do in the recipe: give body (flour), sweeten, lift or set, flavour or decorate, or arrive ready made?',
shelves=[
S('Wheat flour','Flour milled from wheat, sold by how refined it is and how strong the wheat is, such as plain, bread, wholemeal and atta; other grains → Other flours & starches.','kinds by milling and wheat: refined soft, refined strong, whole grain, other wheat, South Asian whole wheat, durum',['Plain flour','Bread flour','Wholemeal flour','Spelt flour','Atta flour','Semolina']),
S('Other flours & starches','Flours and starches from grains other than wheat, from pulses, nuts or roots, and ready gluten-free blends; wheat flour → Wheat flour.','kinds by source plant: cereal, pulse and grain, nut or root, then pure starch and blends',['Rye flour','Rice flour','Sorghum and teff flour','Pulse and grain flours','Nut and root flours','Masa harina','Cornflour and starches','Gluten-free flour blends']),
S('Sugar & sweeteners','Crystalline sugars and sugar substitutes for baking and sweetening, from white sugar to jaggery and stevia; syrups and honey → Honey, syrups & spreads.','kinds by refining: fully refined, partly refined cane, unrefined block sugars, palm sap sugars, then non-sugar sweeteners',['White sugar','Brown sugar','Jaggery','Palm and coconut sugar','Sugar substitutes']),
S('Raising & setting agents','Powders and leaves that lift a dough or set a liquid, such as baking powder, yeast and gelatine; flour mixes → Ready mixes & pastry.','kinds by action: chemical lift, living yeast, setting',['Baking powder and bicarbonate of soda','Dried yeast','Gelatine and setting agents']),
S('Flavourings & decorations','Extracts, waters, colours and toppings added to bakes, such as vanilla extract, rose water, sprinkles and desiccated coconut; whole vanilla pods → Herbs, spices & salt.','kinds by role: flavour, filling texture, then colour and topping',['Baking extracts and flower waters','Desiccated coconut','Food colouring and cake decorations']),
S('Ready mixes & pastry','Mixes and doughs that need little more than liquid or an oven, such as cake mixes, puff pastry and filo; plain flour → Wheat flour.','kinds by the stage that is done for you: dry mix, rolled dough',['Cake and baking mixes','Ready-made pastry']),
])
L['Herbs, spices & salt']=dict(
t='Dry seasonings sold by the jar or bag: single spices, dried herbs, mixed blends and salt; liquid and paste seasonings → Sauces & condiments, fresh herbs and chillies → Fruit & Vegetables.',
ax='What is it: a fruit or seed spice, another plant part, a blend of several, or mineral salt?',
shelves=[
S('Fruit & seed spices','Spices from the fruit or seed of a plant, such as pepper, chilli, cardamom, vanilla, cumin and mustard seed; bark, buds and roots → Leaf, bark, bud, root & flower spices.','kinds by the part: peppers and chillies, pods and aromatic fruits, then small kitchen seeds',['Black pepper and peppercorns','Sichuan pepper','Paprika','Dried chilli','Cardamom','Nutmeg and mace','Star anise','Vanilla','Cumin','Coriander seed','Fennel seed','Mustard seed']),
S('Leaf, bark, bud, root & flower spices','Spices and herbs from the leaf, bark, flower bud, stigma or root, such as cinnamon, cloves, saffron, turmeric and dried oregano; seeds and fruits → Fruit & seed spices.','kinds by the part: leaf, bark, bud, stigma, root, bulb',['Dried herbs','Cinnamon','Cloves','Saffron','Turmeric','Ground ginger','Garlic and onion powder']),
S('Spice blends','Ready-made mixtures of several spices, named for a cuisine, such as garam masala, ras el hanout and five-spice; single spices → the spice shelves.','kinds by cuisine, east to west: South Asia, Middle East and Africa, East Asia, Europe and the Americas',['Garam masala','Curry powder','Tandoori masala','Chaat and jal-jeera masala','Panch phoron','Baharat','Za\'atar','Ras el hanout','Berbere','Chinese five-spice','Shichimi togarashi','Herbes de Provence and mixed herbs','Quatre épices','Mixed spice','Barbecue rubs and seasonings']),
S('Salt','Salt sold for the table, the kitchen and finishing, from refined table salt to flaked and smoked sea salts; seasoned salts with spices → Spice blends.','kinds by source and crystal: refined and kosher, sea-evaporated, mined, then treated salts',['Table salt','Kosher salt','Sea salt','Flake salt','Fleur de sel','Rock salt','Black salt','Smoked and flavoured salt']),
])
L['Sauces & condiments']=dict(
t='Liquid, paste and jelly seasonings added at the table or in the pot, from ketchup to soy sauce and curry paste; dry spice blends → Herbs, spices & salt, fermented vegetables → Tins, jars & preserves.',
ax='Where is it from and how is it used: a western table sauce, a chilli sauce, a Japanese or Korean seasoning, a Chinese or Southeast Asian sauce, or a base for cooking?',
shelves=[
S('Table sauces & condiments','Western sauces and relishes put on the plate, such as ketchup, mustard, mayonnaise and brown sauce; chilli sauces → Hot sauces & chilli condiments.','kinds by base: tomato, brown fruit-and-malt, mustard and root, egg-and-oil, fruit and herb, then bitters',['Ketchup','Barbecue sauce','Brown sauce','Worcestershire sauce','Mustard','Horseradish','Mayonnaise','Tartar sauce','Salad cream','Salad dressing','Cranberry sauce','Mint sauce','Cooking bitters']),
S('Hot sauces & chilli condiments','Condiments whose point is chilli heat, from pourable hot sauce to salsa, pastes and chilli oil; sweet dipping sauces without heat → Table sauces & condiments.','kinds by form: thin sauce, chunky salsa, paste, sweet dip, oil',['Hot sauce','Salsa','Chilli paste','Sweet chilli sauce','Chilli oil and chilli crisp']),
S('Japanese & Korean seasonings','Seasonings of Japanese and Korean cooking made from soybeans, rice, fish and sea vegetables, such as soy sauce, miso, gochujang and dashi.','kinds by what gives the flavour: soy, bean paste, chilli paste, sweet rice, stock, citrus, pungent paste, dry sprinkle',['Soy sauce','Miso and soybean pastes','Gochujang','Ssamjang','Mirin','Cooking sake','Dashi and dashi ingredients','Ponzu and tsuyu','Wasabi and karashi','Yuzu kosho','Furikake']),
S('Chinese & Southeast Asian sauces','Sauces and pastes from Chinese, Thai, Vietnamese, Indonesian and Filipino kitchens, such as oyster sauce, fish sauce and kecap manis; Japanese soy sauce → Japanese & Korean seasonings.','kinds by base: soybean, shellfish and sweet fruit, wine, then fish and shrimp, sweet soy, nut, fruit',['Doubanjiang','Black bean sauce and douchi','Oyster sauce and hoisin sauce','Plum sauce','Fermented bean curd','XO sauce','Shaoxing and Chinese cooking wine','Fish sauce','Shrimp paste','Kecap manis','Peanut sauce','Banana ketchup','Tamarind paste']),
S('Cooking sauces, pastes & stock','Bases bought to cook with rather than add at the table, such as pasta sauce, pesto, curry paste, stock cubes and gravy granules.','kinds by what is cooked with it: pasta, curry or stir-fry, any dish, then stock and gravy',['Tomato pasta sauces','Pesto','Curry paste','Jarred cooking sauces','Stock cubes and bouillon','Gravy granules','Liquid seasonings']),
])
L['Tins, jars & preserves']=dict(
t='Foods kept in a can, a jar or a brine: heat-sealed tomatoes, pulses and fruit, and pickled or fermented vegetables, olives and chutneys; tinned fish → Tinned & jarred fish, tinned meat → Deli, cooked & tinned meats.',
ax='Is it heat-sealed in a tin or jar, or kept by brine, vinegar or fermentation?',
shelves=[
S('Tinned goods','Foods heat-sealed in a can or jar, such as tinned tomatoes, beans, sweetcorn, fruit and coconut milk; pickles and olives → Pickles, olives & ferments.','kinds by the food: tomato, pulses and vegetables, fruit, coconut, then soup',['Tinned tomatoes','Tomato purée and paste','Passata','Tinned beans and pulses','Tinned sweetcorn','Tinned vegetables','Tinned fruit','Coconut milk and cream','Tinned soup']),
S('Pickles, olives & ferments','Vegetables and fruit kept in brine, vinegar or ferment, such as olives, gherkins, sauerkraut, kimchi and mango pickle; jams and marmalade → Syrups, jams & spreads.','kinds by the preserving method and region: brined olives and capers, vinegar pickles, fermented cabbage, Asian pickles, sweet-sour relishes',['Table olives','Capers','Gherkins','Pickled peppers','Sauerkraut','Kimchi','Japanese pickles','Indian pickles','Chutneys and relishes']),
])
L['Dried fruit & vegetables']=dict(
t='Fruit, mushrooms, seaweed and vegetables sold dried to eat or soak; fresh produce → Fruit & Vegetables, dried chillies and herbs → Herbs, spices & salt, dried pulses → Grains, pulses & seeds.',
ax='Is the dried food a fruit, or a mushroom, seaweed or vegetable?',
shelves=[
S('Dried fruit','Fruit dried whole or in pieces to eat as it is or bake with, such as raisins, dates, apricots, prunes and mango; fresh fruit → Fruit & Vegetables.','kinds by fruit: vine and palm fruit first, then stone and tree fruit, berries, tropical, and pressed sheets',['Raisins, sultanas and currants','Dates','Dried figs','Dried apricots','Prunes','Dried apple and pear','Dried cranberries and berries','Dried tropical fruit','Fruit leather']),
S('Dried mushrooms, seaweed & vegetables','Fungi, sea vegetables and vegetables dried for storage and rehydrated to cook, such as porcini, nori and sun-dried tomatoes.','kinds by what is dried: fungus, seaweed, tomato, root',['Dried mushrooms','Dried seaweed','Sun-dried tomatoes','Dried root vegetables']),
])
L['Honey, syrups & spreads']=dict(
t='Sweet and savoury spreads and sweeteners bought by the jar or bottle: honey, boiled syrups, fruit preserves and nut or yeast spreads; table sugar → Flour, sugar & baking.',
ax='Is it bee-made honey, a boiled syrup, a fruit preserve, or a spread of nuts or yeast?',
shelves=[
S('Honey','Honey sold by flower or source, such as clover, acacia, mānuka and honeydew; syrups from plants → Syrups & treacles.','kinds by what the bees gathered: mixed nectar, a graded single nectar, honeydew',['Honey','Manuka honey','Honeydew honey']),
S('Syrups & treacles','Sweet liquids boiled from sap, cane, fruit or grain, such as maple syrup, golden syrup, molasses and date syrup; honey → Honey.','kinds by the plant source: tree sap, cane, fruit, other plants',['Maple syrup','Golden syrup','Molasses and treacle','Date syrup and fruit molasses','Agave and plant syrups']),
S('Jams & marmalade','Fruit cooked with sugar to a spread, as jam, conserve, jelly or citrus marmalade; chutneys → Pickles, olives & ferments.','kinds by fruit: any fruit, then citrus',['Jam and fruit spreads','Marmalade']),
S('Nut & other spreads','Spreads of ground nuts, chocolate-hazelnut or yeast eaten on bread; jams → Jams & marmalade.','kinds by base: peanut, other nuts and seeds, hazelnut-chocolate, yeast',['Peanut butter','Nut and seed butters','Hazelnut-chocolate spread','Yeast extract spread']),
])
L['Home brewing']=dict(
t='Ingredients for making beer, wine and cider at home, bought loose or as a kit; the brewing equipment is in Kitchen & Dining or Tools, and finished drinks are in Wine, Beer & Spirits.',
ax='Is it a separate ingredient or a ready-made kit?',
shelves=[
S('Brewing ingredients','Loose ingredients for a beer wort and its fermentation: hops, malt and grain, malt extract and yeast.','kinds by the stage: flavour and bitterness, fermentable grain, concentrated extract, then yeast',['Hops','Brewing malt and grain','Malt extract','Brewing yeast']),
S('Brewing kits','Boxed or canned sets with everything but water and sugar: beer extract kits and wine or cider concentrate kits.','kinds by the drink: beer, then wine and cider',['Beer kits','Wine and cider kits']),
])
L['Prepared & frozen foods']=dict(
t='Packaged foods bought ready to heat or eat: frozen meals and snacks, frozen potato products, chilled dips, dried soups and baby food; restaurant and home dishes belong to the Culinary taxonomy.',
ax='How is it kept and served: frozen to heat, chilled to eat cold, dried to rehydrate, or made for babies?',
shelves=[
S('Frozen meals & snacks','Frozen dishes and savoury snacks heated at home, such as ready meals, pizza, dumplings and waffles; frozen chips → Frozen potato products.','kinds by dish type: plated meals, accompaniments, pizza, filled dumplings, coated snacks, breakfast, hand-held',['Frozen ready meals','Frozen Yorkshire puddings and accompaniments','Frozen pizza','Pizza rolls','Frozen dumplings','Frozen crispy pancakes and coated savouries','Frozen waffles and breakfast foods','Stuffed sandwiches and turnovers']),
S('Frozen potato products','Potato cut, shaped or grated and sold frozen to oven-bake or fry, such as chips, wedges, hash browns and tater tots.','kinds by shape: cut sticks, then grated or mashed shapes',['Frozen chips and fries','Tater tots and hash browns']),
S('Chilled dips & spreads','Fresh dips sold from the chill cabinet, such as hummus, tzatziki, guacamole and taramasalata; jarred pastes → Cooking sauces, pastes & stock.','kinds by base: chickpea, yoghurt, avocado, fish roe',['Hummus','Tzatziki','Guacamole','Taramasalata']),
S('Instant soups','Soups sold dried in a packet or cup and made with hot water; tinned soup → Tinned goods.','kinds by form: dried soup',['Dried and instant soup']),
S('Baby food','Foods made for infants and toddlers, such as purées, pouches and first cereals; infant milk → Baby & toddler milks.','kinds by stage: weaning purée, first cereal, toddler meal',['Baby purées and pouches','Infant cereals','Toddler meals and snacks']),
])
# ---------- assemble
used=set()
for dn,spec in L.items():
    dp=DEPT[dn]; dp['t']=spec['t']; dp['ax']=spec['ax']
    dp['s']=[]
    for sh in spec['shelves']:
        ks=[]
        for kn in sh['kinds']:
            k=K[kn]; used.add(kn); ks.append(k)
        s={'n':sh['n'],'t':sh['t'],'k':ks}
        if len(ks)>3: s['ax']=sh['ax']
        dp['s'].append(s)
miss=set(K)-used
assert not miss,miss
for kn,k in K.items():
    k.pop('tt_pre',None)
    if kn in TT:
        k['tt']=TT[kn]; k.pop('t',None)
    elif k.get('t'):
        print('NO TT',kn)
    if kn in SEE: k['see']=SEE[kn]
# vinegar sec ref fix: use dept name not code
for dp in d['depts']:
    for s in dp['s']:
        s['t']=s['t'].replace('J9 Drinking vinegar & shrub','Drinking vinegar & shrub in the soft-drinks category').replace('J8 Snack nuts & bars','Snack nuts & bars in the baked-goods category')
d['ax']='What is the food and how does a cook use it: a fat or vinegar, a starchy staple, a seed to cook, a baking basic, a seasoning, a sauce, a preserve, a sweet spread or a ready-to-heat product?'
d['key']=[
'1. Is it an oil, a hard cooking fat or a vinegar? → Oils, vinegars & fats',
'2. Is it a dry spice, dried herb, spice blend or salt? → Herbs, spices & salt',
'3. Is it a liquid, paste or jelly seasoning added at the table or in the pot? → Sauces & condiments',
'4. Is it honey, a syrup, a jam or a nut or yeast spread? → Honey, syrups & spreads',
'5. Is it a malt, hop, yeast or kit for brewing beer, wine or cider at home? → Home brewing',
'6. Is it flour, sugar, a raising or setting agent, a flavouring or a baking mix? → Flour, sugar & baking',
'7. Is it rice, pasta, couscous or noodles? → Rice, pasta & noodles',
'8. Is it dried fruit, mushrooms, seaweed or vegetables? → Dried fruit & vegetables',
'9. Is it kept in a tin, a jar, a brine or a ferment? → Tins, jars & preserves',
'10. Is it a breakfast cereal, a whole grain or seed, a bean, a lentil or a pea? → Grains, pulses & seeds',
'11. Is it a frozen, chilled or dried meal, snack, dip, soup or baby food ready to heat or eat? → Prepared & frozen foods',
'<i>Precedence: a ready-to-heat meal is a prepared food (step 11) before any ingredient step; a chilli sauce is a sauce (step 3) before a spice; dry beans are grains, pulses & seeds (step 10) and tinned beans are tins (step 9); honey and syrups (step 4) come before sugar (step 6).</i>']
# lead check
d['lead']='Shelf-stable and store-cupboard foods to cook with, oils, rice, pasta, grains, flour, spices, sauces, preserves, dried fruit, spreads and home-brew ingredients, organised by what the food is and how a cook uses it, with protected origins and named varieties as archetypes.'
json.dump(d,open(B+'work/STR_J5/new.json','w'),ensure_ascii=False)
import shutil
after=dict(dept=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))
print(before,after)
json.dump({'before':before,'after':after,'dem':DEM},open(B+'work/STR_J5/stats.json','w'))
json.dump(REN_OUT,open(B+'work/STR_J5/ren.json','w'),ensure_ascii=False)
