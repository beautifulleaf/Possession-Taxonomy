import json,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'C2.json'))
B=json.load(open(O+'C2_brands.json'))
T=json.load(open(O+'C2_traditions.json'))
dep={x['n']:x for x in d['depts']}
def shelf(dn,sn):
    for s in dep[dn]['s']:
        if s['n']==sn: return s
def find(dn,sn,kn):
    s=shelf(dn,sn)
    for i,k in enumerate(s['k']):
        if k['n']==kn: return s,i,k
    raise KeyError(kn)
def dedup(lst):
    out=[];seen=set()
    for t in lst:
        if tuple(t) not in seen: seen.add(tuple(t)); out.append(t)
    return out
def ar(n,d_,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def ver(n,mk,d_='',y=''): return {"n":n,"mk":mk,"y":y,"d":d_}
WP='https://en.wikipedia.org/wiki/'

# --- Outdoor cooking
OC='Outdoor cooking'
# C2-2 makers into existing kinds
_,_,k=find(OC,'Grills & smokers','Kamado grill')
k['x'].append(ar('Primo Oval','Ceramic kamado with a patented oval body, sold in Junior, Large and XL sizes.','Primo Grills','','https://www.primogrill.com/ceramic-grills.html',
  [ver('Junior 200','Primo Grills'),ver('Large 300','Primo Grills'),ver('XL 400','Primo Grills'),ver('XL 400 Jack Daniel\'s Edition','Primo Grills'),ver('XX-Large','Primo Grills')],'patented oval shape · Junior to XX-Large · charcoal'))
k['x'].append(ar('Komodo Kamado Big Bad','Insulated multi-layer kamado with tiled shell and 304 stainless grates; the 32 in Big Bad is the flagship.','Komodo Kamado','','https://komodokamado.com/collections/32-big-bad',
  [ver('32 in Big Bad','Komodo Kamado','Standard, Bronze or Pebble tiles')],'tile finish · 304 stainless grates · charcoal basket splitter'))
_,_,k=find(OC,'Grills & smokers','Pellet grill')
k['x'].append(ar('Recteq Bullseye Deluxe','Stainless wood-pellet grill with an afterburner firepot for direct-heat searing up to 1000 °F and a Wi-Fi PID controller.','Recteq','','https://www.recteq.com/products/bullseye-deluxe-380bd',
  [ver('Bullseye Deluxe 380BD','Recteq','380 sq in cooking area, 18 lb hopper')],'380 sq in · 200–1000 °F · 304 stainless · Wi-Fi controller'))
_,_,k=find(OC,'Grills & smokers','Offset smoker')
k['x'].append(ar('Lone Star Grillz offset smoker','Texas-built offset smoker sold in pipe, vertical, cabinet and hybrid forms.','Lone Star Grillz','','https://lonestargrillz.com/collections/smokers',
  [ver('LSG Texas Edition 20 x 30','Lone Star Grillz'),ver('24 x 48 Offset Smoker','Lone Star Grillz'),ver('24 x 48 Offset Hybrid Smoker','Lone Star Grillz'),ver('24 in Offset Vertical Smoker','Lone Star Grillz'),ver('24 in Offset Cabinet Smoker','Lone Star Grillz')],'pipe, vertical, cabinet or hybrid · 20 x 30 to 30 x 72 in · built in Conroe, Texas'))

# C2-2 split accessories
s,i,k=find(OC,'Pizza ovens, fire cooking & accessories','Barbecue tools & accessories')
k['t']=[t for t in k['t'] if t not in('Chimney starter','Meat thermometer','Rotisserie kit')]
new=[
 {"n":"Chimney starter","a":"charcoal chimney · lighting cone","d":"Metal tube with a grate that lights charcoal lumps or briquettes before they are tipped into the grill.","t":["steel cylinder","lighting cone"],"s":WP+"Chimney_starter","m":[["Rapidfire Chimney Starter","Weber"]]},
 {"n":"Grill thermometer","a":"meat thermometer · BBQ probe","d":"Thermometer that reads food or grill-chamber temperature, from dial and probe types to wireless units. See B5 Kitchen thermometer.","t":["dial","probe (leave-in)","wireless"],"s":WP+"Meat_thermometer"},
 {"n":"Rotisserie","a":"spit roaster","d":"Motor-turned spit that roasts meat evenly over a grill's fire.","t":["spit rod","electric motor kit"],"s":WP+"Rotisserie"},
]
k_idx=s['k'].index(k)
s['k'][k_idx+1:k_idx+1]=new

# C2-1 fire pits shelf
fp=[
 {"n":"Fire pit","a":"fire bowl · fire ring · smokeless fire pit","d":"Open container that holds a garden fire, from steel bowls and rings to gas burners and double-wall smokeless designs.","t":["wood-burning","gas or propane","bioethanol","fire bowl","fire ring","smokeless double-wall"],"s":WP+"Fire_pit",
  "x":[ar('Solo Stove Bonfire','Stainless double-wall wood fire pit whose 360° airflow gives a secondary burn and little smoke.','Solo Stove','','https://www.solostove.com/us/en-us/p/canyon-fire-pit-and-stand-bundle?sku=SSBON-SD-2.0',
        [ver('Ranger 15 in','Solo Stove'),ver('Bonfire 19.5 in','Solo Stove'),ver('Basecamp 24 in','Solo Stove'),ver('Yukon 27 in','Solo Stove'),ver('Canyon 30 in','Solo Stove')],'304 stainless steel · removable ash pan · optional stand · wood'),
       ar('Breeo X Series','Smokeless fire pit with X Airflow reburn, handcrafted in Pennsylvania in corten or stainless steel and compatible with Breeo cooking accessories.','Breeo','','https://breeo.com/products/x-series-smokeless-fire-pit',
        [ver('X19','Breeo'),ver('X24','Breeo'),ver('X30','Breeo'),ver('X42','Breeo'),ver('Y Series','Breeo','Portable fire pit for car camping or small spaces')],'four sizes · corten or 304 stainless steel')]},
 {"n":"Chiminea","a":"chimenea","d":"Freestanding front-loading fireplace with a bulbous body and vertical smoke vent, traditionally clay.","t":["clay","cast iron","aluminium"],"s":WP+"Chimenea"},
 {"n":"Patio heater","a":"mushroom heater · umbrella heater","d":"Radiant heater that warms an outdoor seating area, gas-fired or electric.","t":["propane","natural gas","electric","wall-mounted","hanging","tabletop"],"s":WP+"Patio_heater"},
]
dep[OC]['s'].insert(1,{"n":"Fire pits & patio heating","k":fp})

# --- C2-3 bonsai potters
_,_,k=find('Bonsai','Bonsai tools & pots','Bonsai pot')
V='https://valavanisbonsaiblog.com/2016/11/21/2016-autumn-japan-bonsai-exploration-part-7-final/'
pot=[('Gyozan bonsai pot','Hand-built Tokoname pot made without moulds, mostly unglazed with some glazed pieces.','Gyozan','hand-built, no moulds · mostly unglazed · some glazed'),
 ('Reiho bonsai pot','Tokoname pot with the Reiho seal on the base; known for smaller containers and glazes.','Reiho','Reiho seal on base · smaller containers · glazed'),
 ('Yamaaki bonsai pot','Tokoname pot of fine quality in normal sizes, mostly unglazed brown with some light blue glaze.','Yamaaki','unglazed brown · light blue glaze · normal sizes'),
 ('Koyo bonsai pot','Tokoname pot specialising in smaller glazed containers.','Koyo','smaller sizes · glazed'),
 ('Shuho bonsai pot','Tokoname pot specialising in unusual glazes, mostly small and shohin sizes.','Shuho','small and shohin · glazed'),
 ('Ikko bonsai pot','Tokoname pot in all sizes, glazed and unglazed, noted for detail and unusual glazes.','Ikko','all sizes · glazed and unglazed')]
pos=1
for n,dd,mk,dt in pot:
    k['x'].insert(pos,ar(n,dd,mk,'',V,[],dt)); pos+=1
# potter versions stay inside Tokoname archetype (unchanged)

# --- C2-4
sh=shelf('Pots, beds & plant supports','Pots, planters & raised beds')
pp=[x for x in sh['k'] if x['n']=='Plant pot'][0]
pp['t']+=['window box (long planter for a sill or railing)','cachepot (outer container without drainage)','vertical garden planter']
sh['k']=[x for x in sh['k'] if x['n'] not in('Window box','Cachepot','Vertical garden planter')]
sh=shelf('Pots, beds & plant supports','Supports, ties & labels')
tie=[x for x in sh['k'] if x['n']=='Plant tie'][0]
tie['n']='Plant tie & label'; tie['a']='plant label · garden twine'
tie['d']='Twine, wire, clip or tool that fastens a plant to its support, and the label that names it.'
tie['t']+=['plant label (marker pushed into the soil or tied on)']
sup={"n":"Plant support","a":"stake · cane · trellis · obelisk · garden arch · support frame","d":"Stake, frame, trellis, arch or obelisk that holds up a tall or climbing plant.","t":["stake or cane","support frame","trellis","garden arch","obelisk"],"s":WP+"Trellis"}
sh['k']=[sup,tie]
sh=shelf('Soil, feed & plant care','Compost, soil & mulch')
pc=[x for x in sh['k'] if x['n']=='Potting compost'][0]
pc['n']='Potting compost, soil & mulch'; pc['a']='soil improver · mulch · topsoil · grow bag'
pc['d']='Growing medium and soil cover for pots and beds: compost, topsoil, improver, mulch and compost-filled grow bags.'
pc['t']+=['soil improver','mulch','topsoil','compost-filled grow bag']
sh['k']=[x for x in sh['k'] if x['n'] not in('Soil improver','Mulch','Topsoil','Compost-filled grow bag')]

# --- C2-5
sh=shelf('Pools & pool care','Pool cleaners & water care')
names=['Robotic pool cleaner','Suction-side pool cleaner','Pressure-side pool cleaner','Robotic pool skimmer']
old=[x for x in sh['k'] if x['n'] in names]
m=[];r=[]
for x in old: m+=x.get('m',[]); r+=x.get('r',[])
pcl={"n":"Pool cleaner","a":"pool robot · automatic pool cleaner","d":"Automatic cleaner that vacuums or skims a pool, self-powered or driven by pump suction or water pressure.",
 "t":["robotic","suction-side","pressure-side (booster-pump or return-line driven)","robotic skimmer (often solar)","booster pump (accessory)"],
 "s":"https://lesliespool.com/automatic-pool-cleaners/","m":dedup(m),"r":dedup(r)}
j=sh['k'].index(old[0]); sh['k']=[x for x in sh['k'] if x['n'] not in names]; sh['k'].insert(j,pcl)
sh=shelf('Pools & pool care','Pumps, filters & heating')
pf=[x for x in sh['k'] if x['n']=='Pool filter'][0]
pf['t']=[t for t in pf['t'] if not t.startswith('Spare parts')]
sh['k'].append({"n":"Pool spare parts","a":"filter cartridges · DE grids","d":"Replacement parts for pool filters and pumps, such as filter cartridges and diatomaceous-earth grids.","t":["filter cartridges","DE grids"],"s":"https://lesliespool.com/filter-cartridges/"})
sh=shelf('Watering & ponds','Hoses & reels')
hc=[x for x in sh['k'] if x['n']=='Hose connector'][0]; hs=[x for x in sh['k'] if x['n']=='Hose spray gun'][0]
hf={"n":"Hose fittings","a":"hose connector · hose nozzle · spray gun","d":"Fittings that join a garden hose to a tap, tool or another hose, and the nozzle or spray gun on its end.","t":["connector","spray gun or nozzle"],"s":hc['s'],"m":dedup(hc.get('m',[])+hs.get('m',[]))}
j=sh['k'].index(hc); sh['k']=[x for x in sh['k'] if x['n'] not in('Hose connector','Hose spray gun')]; sh['k'].insert(j,hf)

# --- C2-8
sh=shelf('Watering & ponds','Ponds'); sh['n']='Pond liners & pumps'
pl=[x for x in sh['k'] if x['n']=='Pond liner'][0]
pl['d']='Flexible waterproof sheet laid to form a garden pond. Koi ponds, filtration and pond fish are in B10.'

# --- C2-7 merge ARS
sig=[];
b=B['b']; ars=[x for x in b if x['n']=='ARS'][0]; arc=[x for x in b if x['n']=='ARS Corporation'][0]
for s_ in arc['sig']:
    if s_ not in ars['sig']: ars['sig'].append(s_)
ars['d']+=' Also listed as ARS Corporation, Nishinomiya, Hyogo.'
B['b']=[x for x in b if x['n']!='ARS Corporation']
raw=json.dumps(d).replace('"mk": "ARS Corporation"','"mk": "ARS"'); d=json.loads(raw)

# --- brands
def br(n,c,seg,kf,dd,s,lines=None,sig=None,rel=None):
    return {"n":n,"c":c,"f":"","seg":seg,"d":dd,"lines":lines or [],"eras":[],"sig":sig or [],"sc":[],"rel":rel or [],"s":s,"kf":kf}
B['b']+= [
 br('Primo Grills','', 'Premium','kamado grills','Maker of ceramic kamado grills with a patented oval body.','https://www.primogrill.com/ceramic-grills.html',['Junior 200','Large 300','XL 400','XX-Large'],['Primo Oval'],['Big Green Egg','Kamado Joe']),
 br('Komodo Kamado','', 'Premium','kamado grills','Maker of insulated, tiled kamado grills; the 32 in Big Bad is its flagship.','https://komodokamado.com/collections/32-big-bad',['Big Bad'],['Komodo Kamado Big Bad'],['Big Green Egg']),
 br('Recteq','', 'Mainstream','pellet grills','Maker of wood-pellet grills with Wi-Fi controllers, including the Bullseye Deluxe.','https://www.recteq.com/products/bullseye-deluxe-380bd',['Bullseye Deluxe'],['Recteq Bullseye Deluxe'],['Traeger']),
 br('Lone Star Grillz','United States','Specialist','offset smokers','Conroe, Texas maker of offset, vertical, cabinet and hybrid smokers.','https://lonestargrillz.com/collections/smokers',[],['Lone Star Grillz offset smoker'],['Yoder Smokers']),
 br('Solo Stove','', 'Premium','smokeless fire pits','Maker of stainless double-wall smokeless fire pits including the Bonfire.','https://www.solostove.com/us/en-us/p/canyon-fire-pit-and-stand-bundle?sku=SSBON-SD-2.0',['Ranger','Bonfire','Basecamp','Yukon','Canyon'],['Solo Stove Bonfire'],['Breeo']),
 br('Breeo','United States','Premium','smokeless fire pits','Maker of smokeless fire pits handcrafted in Pennsylvania from corten and stainless steel.','https://breeo.com/products/x-series-smokeless-fire-pit',['X Series','Y Series'],['Breeo X Series'],['Solo Stove']),
 br('Koyo','Japan','Artisan & independent','bonsai pots','Tokoname kiln specialising in smaller glazed bonsai pots.',V,[],['Koyo bonsai pot'],['Reiho']),
 br('Shuho','Japan','Artisan & independent','bonsai pots','Tokoname kiln making unusual glazed pots, mostly small and shohin.',V,[],['Shuho bonsai pot'],['Reiho']),
 br('Ikko','Japan','Artisan & independent','bonsai pots','Tokoname kiln making bonsai pots in all sizes, glazed and unglazed.',V,[],['Ikko bonsai pot'],['Reiho']),
]
for x in B['b']:
    if x['n'] in('Gyozan','Reiho','Yamaaki') and x['n']+' bonsai pot' not in x['sig']: x['sig'].append(x['n']+' bonsai pot')
B['b'].sort(key=lambda x:x['n'].lower())
for fn,obj in (('C2.json',d),('C2_brands.json',B),('C2_traditions.json',T)):
    json.dump(obj,open(O+fn+'.tmp','w'),ensure_ascii=False,indent=1)
import os
for fn in ('C2.json','C2_brands.json','C2_traditions.json'): os.replace(O+fn+'.tmp',O+fn)
