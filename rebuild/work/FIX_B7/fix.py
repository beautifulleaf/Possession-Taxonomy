import json,os
p='out/B7.json'; d=json.load(open(p))
drop={'Fan heater':['PB-H12-UK mini ceramic','RHCH2001G ceramic','PCH-125D-W ceramic','Kazedan'],
'Window air conditioner':['MAW08V1YWT-S inverter','LW6023IVSM','LW6017R','FFRA051WAE'],
'Portable air conditioner':['Duo MAP12S1TBL','NEX ARC-1230WN','BPACT14WT','Dolceclima 12000 BTU'],
'Air purifier':['5500-2','HPA300','MC55VB','Smart Air Purifier 4'],
'Humidifier':['EVDC300 Energy Smart Evaporative','KC850U Plasmacluster purifier-humidifier','Warm Mist Humidifier'],
'Dehumidifier':['MeacoDry Arete Two 12L','1500ml Mini Dehumidifier','30L High Capacity Smart Dehumidifier','Cube 50 pt']}
ren={'U-Shaped MAW12V1QWT':'U-Shaped','Smart MAW08HV1CWT':'Smart window','LW8024IVSM':'Dual Inverter window'}
fan=None
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for x in drop.get(k['n'],[]):
        k['m']=[m for m in k['m'] if m[0]!=x]
      if k['n']=='Window air conditioner':
        k['m']=[[ren.get(m[0],m[0]),m[1]] for m in k['m']]
      if k['n']=='Electric fireplace':
        k['d']='Freestanding plug-in electric stove or fire with a flame effect that can run with or without heat; inset and wall-mounted units are in Home Fixtures.'
    if s['n']=='Fans': fan=dp
W='https://en.wikipedia.org/wiki/'
kind={"n":"Electric fan (design & vintage)","a":"collectable fan · antique fan · designer fan","d":"Electric fans collected or chosen for their maker and design, from early brass-blade table fans to bladeless and DC-motor designer fans.",
"s":W+"Emerson_Electric","x":[
{"n":"Emerson Northwind","a":"Emerson electric table fan","d":"Early American electric table fan from the first company to sell electric fans in the United States.","mk":"Emerson Electric","y":"1890s–1910s","s":W+"Emerson_Electric","v":[{"n":"Northwind table fan","mk":"Emerson Electric","y":"c. 1915","d":"Example held by the National Museum of American History"}]},
{"n":"Vornado air circulator","a":"Vornadofan","d":"Ducted fan with propeller-style blades and flared intake ring that circulates air round a whole room.","mk":"Vornado","y":"1945","s":W+"Vornado_Air","v":[{"n":"Original Vornadofan","mk":"Vornado","y":"1940s–1958","d":"Made by the O.A. Sutton Corporation, Wichita; production stopped 1958"},{"n":"Revived spiral-grille circulator","mk":"Vornado","y":"1989","d":"Vortex Action design; table, floor, stand and window models"},{"n":"Energy Smart line","mk":"Vornado","y":"2017","d":"DC motors and variable speed"}],"dt":"table · floor · stand · window · size small to large"},
{"n":"Dyson Air Multiplier","a":"bladeless fan","d":"Bladeless fan that draws air through a base and projects it from a ring-shaped aperture.","mk":"Dyson","y":"2009","s":W+"Dyson_Air_Multiplier","v":[{"n":"AM01 · AM02 · AM03","mk":"Dyson","y":"2009","d":"Original bladeless fans; second generation 2014 was quieter"},{"n":"AM04 Dyson Hot","mk":"Dyson","y":"2011","d":"Heater that also runs as a fan; early units recalled for fire risk"}],"dt":"desk · pedestal · tower · colours"},
{"n":"Balmuda GreenFan","a":"","d":"Fan with two blade sets running at different speeds, designed to avoid the harsh gusts of a single-blade fan.","mk":"Balmuda","y":"2010","s":W+"Balmuda","dt":"desk · pedestal"}]}
fan['s'].append({"n":"Design & vintage fans","k":[kind]})
json.dump(d,open('out/B7.json.tmp','w'),indent=1,ensure_ascii=False); os.rename('out/B7.json.tmp',p)
bp='out/B7_brands.json'; b=json.load(open(bp))
b['b'].append({"n":"Emerson Electric","c":"United States","f":"1890","seg":"Premium","kf":"early electric fans","d":"St. Louis maker of electric motors and, from 1892, the first electric fans sold in the United States.","lines":["Northwind"],"eras":[],"sig":["Emerson Northwind"],"sc":["vintage fans"],"rel":[],"s":W+"Emerson_Electric"})
json.dump(b,open(bp+'.tmp','w'),indent=1,ensure_ascii=False); os.rename(bp+'.tmp',bp)
