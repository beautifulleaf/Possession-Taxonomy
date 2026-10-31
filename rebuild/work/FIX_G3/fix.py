import json,os
p='out/G3.json'
d=json.load(open(p))
ks={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
sh={s['n']:s for dp in d['depts'] for s in dp['s']}
# G3-4
w=ks['Wall socket']
w['t']=["UK (BS 1363, Type G)","EU Schuko (CEE 7/4, Type F)","US (NEMA 5-15, Type B)","other national standard (see IEC World Plugs)"]+[t for t in w['t'] if not t.startswith('Type ')]
ks['Hard-shell hot tub'].pop('m')
for k in ks.values():
    if 'm' in k:
        k['m']=[e for e in k['m'] if e[1]!='Dunster House']
        if not k['m']: k.pop('m')
for n in ('Built-in coffee machine','Warming drawer'):
    ks[n]['m']=ks[n]['m'][:1]
# G3-5
ks['Staircase']['x']=[{"n":"Spiral staircase","a":"helical stair · winding stair · circular stair","d":"Helical stair winding around a central newel or open well, compact in plan.","mk":"","y":"c. 480 BCE (Selinunte)","s":"https://en.wikipedia.org/wiki/Spiral_staircase","dt":"newel or open well · timber, steel, glass, stone · diameter"}]
ks['Wine cellar']={"n":"Wine cellar","a":"wine room · cave","d":"Room fitted for storing wine at steady cool temperature, passive underground or actively cooled and insulated.","t":["passive (underground)","active (climate-controlled)","racked","glazed display room"],"s":"https://en.wikipedia.org/wiki/Wine_cellar"}
sh['Cooking & built-in appliances']['k'].append(ks['Wine cellar'])
cin={"n":"Home cinema room","a":"home theatre room · media room","d":"Dedicated room built for film viewing, with projector or large screen, surround sound, acoustic treatment and seating.","t":["projector and screen","large flat panel","acoustic treatment","tiered seating","blackout lining"],"s":"https://en.wikipedia.org/wiki/Home_cinema"}
sh['Ceiling fans & built-in media']['k'].append(cin)
war={"n":"Fitted wardrobe","a":"built-in wardrobe · walk-in wardrobe · dressing room","d":"Wardrobe or dressing room built to the room's dimensions, with hanging, shelving and drawers.","t":["sliding-door","hinged-door","walk-in dressing room","open walk-in","alcove","floor-to-ceiling"],"s":"https://en.wikipedia.org/wiki/Walk-in_closet"}
dp=[x for x in d['depts'] if x['n']=='Structure & circulation'][0]
dp['s'].append({"n":"Fitted storage","k":[war]})
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(p+'.tmp',p)
