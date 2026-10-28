import json,os,tempfile
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'B6.json')); br=json.load(open(O+'B6_brands.json'))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=(dp,s,k)
W='https://en.wikipedia.org/wiki/'
def rm(kind,pairs):
  k=K[kind][2]; k['m']=[m for m in k.get('m',[]) if m[0] not in pairs]
def arch(n,a,dd,mk,y,s,v,dt):
  return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":W+s,"v":v,"dt":dt}
def V(n,mk,y,dd): return {"n":n,"mk":mk,"y":y,"d":dd}
# B6-1 archetypes
K['Cylinder vacuum cleaner'][2]['x']=[
 arch("Henry","Henry vacuum · Numatic Henry","Smiling-faced bagged cylinder vacuum on a bucket body, widely used in homes and workplaces in Britain.","Numatic","1981","Henry_(vacuum_cleaner)",
  [V("HVC200","Numatic","1981","Original Henry"),V("HVR200","Numatic","1987","Manual cable reel; successor to HVC200"),V("HVR200A (AutoSave)","Numatic","2008","Energy-saving motor control"),V("Hetty (HET200)","Numatic","2007","Pink variant"),V("James","Numatic","1985","JVC225, later JVR225"),V("Charles","Numatic","1983","Larger CVC375, later CVC370")],"bucket body · bagged · colour variants and character names"),
 arch("Hoover Constellation","Model 82 · Constellation","Round cylinder cleaner designed by Henry Dreyfuss whose exhaust let it float on air.","Hoover","1954","Hoover_Company",
  [V("Constellation (Model 82)","Hoover","1954","Original"),V("Constellation reissue","Hoover","2006","Reintroduced 2006 to 2009")],"spherical body · floats on exhaust air"),
 arch("Rainbow","Rexair Rainbow · water-filter vacuum","Water-filtration cylinder vacuum that traps dust in a water basin instead of a bag.","Rexair","1936 (Rainbow name 1955)","Rexair",
  [V("A","Rexair","1936","First Rexair cleaner with water filtration"),V("D","Rexair","1955","First Rainbow-named model"),V("D4C","Rexair","1986","Late D-series"),V("E2 Type 12","Rexair","2004","Gold, then silver (2008) and black (2011) versions"),V("RHCS19 SRX","Rexair","2019","Current series in the source table")],"water basin · sold by direct demonstration · colour finishes")]
K['Upright vacuum cleaner'][2]['x']=[
 arch("Hoover Model O","Hoover Model 0","Hoover's first production upright, sold from 1908 after the company bought James Spangler's patent.","Hoover","1908","Hoover_Company",
  [V("Model O","Hoover","1908","First machine"),V("Model 150","Hoover","1936","Dreyfus-designed upright with Bakelite hood")],"cloth bag · beater bar"),
 arch("Dyson DC01","DC01 · Dyson Dual Cyclone","Dyson's first bagless cyclonic upright, launched in 1993.","Dyson","1993","Dyson_DC01",
  [V("DC01","Dyson","1993","Original"),V("DC07","Dyson","2001","Upright successor"),V("DC14","Dyson","2004","Revision of DC07")],"bagless cyclone · upright"),
 arch("Kirby","Kirby upright · Kirby Classic","American direct-sale upright vacuum made with a heavy metal body, from the 1935 Kirby Model C.","Kirby","1935","Kirby_Company",
  [V("Model C","Kirby","1935","First Kirby-named vacuum"),V("Model 508","Kirby","1948","Introduced the Belt Lifter"),V("Classic","Kirby","1970","Second generation"),V("Generation 3 (G3)","Kirby","1990","Facelift with HEPA bag"),V("Gsix","Kirby","1999","HEPA filtration"),V("Sentria","Kirby","2006","Dated 2006 to 2012")],"metal body · sold by demonstration · attachment range"),
 arch("Vorwerk Kobold","Kobold","German household upright vacuum first built in 1929 from a gramophone motor, sold by direct demonstration.","Vorwerk","1929","Vorwerk_(company)",
  [V("Kobold (Model 30)","Vorwerk","1930","Patented 25 May 1930")],"upright · direct sale")]
K['Handheld vacuum cleaner'][2]['x']=[
 arch("Dustbuster","Black+Decker Dustbuster","Cordless hand vacuum sold for household use from 1979, designed by Carroll Gantz.","Black+Decker","1979","Dustbuster",
  [V("Spot Vac (Model 9321)","Black+Decker","1974","Power-tool precursor"),V("Dustbuster","Black+Decker","1979","Household redesign")],"wall-charging base · crevice tool"),
 arch("Hoover Dustette","Dustette","Hoover handheld cleaner described as the first handheld vacuum cleaner.","Hoover","1930","Hoover_Company",[],"corded handheld")]
K['Robot vacuum cleaner'][2]['x']=[
 arch("Electrolux Trilobite","Trilobite","First commercially available robotic vacuum cleaner, shown on television in 1996 and sold from 2001.","Electrolux","2001","Electrolux_Trilobite",
  [V("ZA1","Electrolux","2001","First model"),V("ZA2 (Version 2.0)","Electrolux","2004","Second generation")],"ultrasonic sensing"),
 arch("Roomba","iRobot Roomba","iRobot's disc-shaped robot vacuum, first sold in September 2002 and made in numbered generations.","iRobot","2002","Roomba",
  [V("Original series","iRobot","2002","First generation"),V("Discovery and 400 series","iRobot","2004","Second generation"),V("500/600 series","iRobot","2007","Third generation"),V("900 series","iRobot","2015","Sixth generation"),V("i and e series","iRobot","2018","Seventh generation"),V("s series","iRobot","2019","Eighth generation"),V("j series","iRobot","2021","Ninth generation")],"vacuum only or combo · dock type")]
rm('Cylinder vacuum cleaner',{'Henry HVR200'})
rm('Upright vacuum cleaner',{'Model O','DC01','DC07'})
rm('Handheld vacuum cleaner',{'Dustbuster'})
rm('Robot vacuum cleaner',{'Trilobite','Roomba (2002 original)'})
# brands
have={b['n'].lower() for b in br['b']}
new=[("Kirby","United States","1914","Premium","direct-sale uprights","Ohio maker of metal-bodied upright vacuums sold by home demonstration.",["Classic","Generation series","Sentria","Avalir"],"Kirby_Company"),
("Vorwerk","Germany","","Premium","Kobold vacuums","German household-appliance maker whose Kobold upright vacuum dates from 1929.",["Kobold"],"Vorwerk_(company)"),
("Rexair","United States","","Premium","Rainbow water vacuum","Troy, Michigan maker of the Rainbow water-filter vacuum cleaner.",["Rainbow"],"Rexair")]
for n,c,f,sg,kf,dd,ln,s in new:
  if n.lower() not in have: br['b'].append({"n":n,"c":c,"f":f,"seg":sg,"d":dd,"lines":ln,"eras":[],"sig":[],"sc":[],"rel":[],"s":W+s,"kf":kf})
# B6-3 folds
def merge_into(dst,src,types=(),alias=()):
  dk=K[dst][2]; sk=K[src][2]
  dk['t']=dk.get('t',[])+[t for t in types if t not in dk.get('t',[])]
  al=[a for a in dk.get('a','').split(' · ') if a]+[sk['n'].lower()]+[a for a in sk.get('a','').split(' · ') if a]+list(alias)
  seen=[];[seen.append(a) for a in al if a and a not in seen and a!=dk['n'].lower()]
  dk['a']=' · '.join(seen)
  dk['m']=dk.get('m',[])+sk.get('m',[]); dk['r']=dk.get('r',[])+sk.get('r',[])
  s=K[src][1]; s['k']=[k for k in s['k'] if k['n']!=src]
merge_into('Wet mop','Spin mop system',['spin mop and bucket system'])
merge_into('Wet mop','Dust mop',['dust (dry) mop'])
merge_into('Dishwasher detergent','Dishwasher rinse aid',['rinse aid (separate liquid)'])
merge_into('Dishwasher detergent','Dishwasher salt',['dishwasher salt (water-softener)'])
merge_into('Kitchen bin','Waste-paper basket',['waste-paper basket (small open bin)'])
# drop trade polisher
s=K['Hard-floor scrubber-polisher'][1]; s['k']=[k for k in s['k'] if k['n']!='Hard-floor scrubber-polisher']
# B6-4 pedestal kit
k=K['Front-load washing machine'][2]
k['t'].append('pedestal and stacking kit (accessory)')
k['a']=(k.get('a','')+' · ' if k.get('a') else '')+'washer pedestal · stacking kit'
s=K['Laundry pedestal and stacking kit'][1]; s['k']=[x for x in s['k'] if x['n']!='Laundry pedestal and stacking kit']
# B6-2 trim m to 6, dedupe m/r
for n,(dp,s,k) in K.items():
  if 'm' in k and len(k['m'])>6:
    seen=set();first=[];rest=[]
    for m in k['m']:
      (rest if m[1] in seen else first).append(m); seen.add(m[1])
    keep=(first+rest)[:6]
    k['m']=[m for m in k['m'] if m in keep]
  if k.get('r'):
    ms=k.get('m',[]); out=[];ns=set()
    for r in k['r']:
      if r[0].lower()==r[1].lower(): continue
      if any(r[1]==m[1] and (r[0].lower() in m[0].lower() or m[0].lower() in r[0].lower()) for m in ms): continue
      if r[0] in ns: continue
      ns.add(r[0]); out.append(r)
    k['r']=out
def dump(p,o):
  t=p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
dump(O+'B6.json',d); dump(O+'B6_brands.json',br)
