import json,os
W='https://en.wikipedia.org/wiki/'
BA='https://brokenarrowranch.com/pages/wholesale-product-list'
TE='https://teara.govt.nz/en/deer-and-deer-farming/page-8'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
CUT='cut: haunch, saddle, loin, fillet, rack, shoulder, mince · wild or farmed · season'
kinds=[
{'n':'Venison by species','a':'venison · deer meat','d':'Deer meat sold whole or as any cut, grouped by the deer species and origin scheme it comes from.','s':'https://www.wildmeat.co.uk/collections/game-meat',
 't':['wild','farmed','park'],
 'x':[X('Red deer venison','Venison from red deer, the largest British deer; wild from Scottish hills or farmed, notably in New Zealand.',W+'Red_deer',dt=CUT),
  X('Roe deer venison','Venison from roe deer, dark, fine-grained meat and the main source of venison in Europe.',W+'Roe_deer',a='roe buck · chevreuil · Reh',dt=CUT),
  X('Fallow deer venison','Venison from fallow deer, sold as saddles, legs, loins and racks.',BA,dt=CUT),
  X('Sika venison','Venison from sika deer, an introduced species culled in Britain and Ireland and sold as saddles, legs and loins.',BA,dt=CUT),
  X('Muntjac venison','Venison from the small introduced Reeves\'s muntjac of south-east England, sold as loin steaks and small joints.','https://www.countryandtownhouse.com/food-and-drink/wild-venison',dt=CUT),
  X('Axis venison','Venison from axis (chital) deer ranched wild in Texas, sold in a full range of cuts.',BA,a='chital',dt=CUT),
  X('Reindeer meat','Meat of herded reindeer from Sápmi, eaten as thin-sliced sautéed reindeer (poronkäristys, renskav).','https://en.wikipedia.org/wiki/Saut%C3%A9ed_reindeer',a='poro · ren'),
  X('Elk (moose) meat','Meat of the moose, called elk in Europe, hunted in Scandinavia and sold fresh or as smoked roasts.',W+'Moose',a='moose · älg · elg',v=[{'n':'Varmrökt älgrostbiff (jägarstek)','mk':'','y':'','d':'hot-smoked elk roast, Sweden'}]),
  X('Cervena','Trademarked appellation for New Zealand farmed venison meeting set standards.',TE,a='NZ farmed venison'),
  X('Scottish Quality Wild Venison','Assurance scheme for wild Scottish venison covering welfare, hygiene and traceability from hill to consumer.','https://www.farminguk.com/news/wild-venison-assurance-scheme-records-50-members_754.html',y='2003',a='SQWV')]},
{'n':'Venison haunch','a':'leg of venison','d':'The hind leg of a deer, whole or as a roasting joint or steaks, on or off the bone.','s':'https://www.wildmeat.co.uk/collections/game-meat',
 't':['whole haunch on the bone','boned and rolled joint','haunch steaks','Denver leg (boned-out leg muscles)']},
{'n':'Venison saddle & loin','a':'venison medallions · backstrap','d':'The loin section of a deer, as a saddle on the bone, a boneless loin or medallions.','s':'https://swaledale.co.uk/collections/wild-british-game-meat',
 't':['saddle on the bone','loin','medallions']},
{'n':'Venison fillet','a':'tenderloin','d':'The tenderloin of a deer, whole or cut into steaks.','s':'https://www.salterandking.co.uk/collections/game-meat'},
{'n':'Venison rack','a':'','d':'The rib section of a deer with its chops joined, sold raw.','s':'https://www.dartagnan.com/buy/meat-game','t':['French-trimmed rack','chops']},
{'n':'Venison mince & burgers','a':'ground venison · venison meatballs','d':'Raw minced venison, loose or shaped into burgers or meatballs, plain or only seasoned.','s':'https://swaledale.co.uk/collections/wild-british-game-meat',
 't':['mince','burgers','meatballs','mince with added fat']},
]
out={'kinds':kinds,'brands':[],'traditions':[],'notes':'All six planned kinds kept; saddle and medallions merged (Venison saddle & loin), mince and burgers merged. Species and schemes are archetypes of Venison by species (red, roe, fallow, sika, muntjac, axis, reindeer, elk/moose, Cervena, Scottish Quality Wild Venison); cut is detail. Cervena year left out (sources differ 1991-93). No brand entries: no maker is an archetype mk. Chinese water deer left out (no fetched page).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/04_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
