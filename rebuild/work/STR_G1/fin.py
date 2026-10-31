import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_G1')
from edit import *
import glob
d=load()
d['lead']="Everything a person can own that moves people or goods, from cars, motorcycles and bicycles to caravans, boats, aircraft, heritage rail and prams, plus riding gear and vehicle care; organised by what the vehicle is and how it is driven, with named model families as archetypes, marques in the brand register and classics as a period view."
d['ax']="What is it: a car, a two-wheeler, a bicycle, a van or lorry, a home on wheels, a boat, an aircraft, a rail or horse-drawn vehicle, a pram, riding gear, or something for looking after a vehicle?"
d['key']=[
"1. Is it a pram, pushchair or wheeled seat for a baby, child or small pet? → Prams & strollers",
"2. Is it a product or tool for washing, polishing, protecting, lifting or lubricating a vehicle? → Vehicle care & detailing",
"3. Is it worn to ride a motorcycle (helmet, suit, gloves, boots, protector)? → Motorcycle riding gear",
"4. Is it a pedal bicycle, a cycle with an unusual layout, or a part fitted to one? → Bicycles",
"5. Is it a powered two- or three-wheeler ridden astride or standing, from a motorcycle to an electric scooter? → Motorcycles & scooters",
"6. Does it float, or is it driven on water (boat, yacht, kayak, jet ski)? → Boats",
"7. Does it fly (airplane, glider, balloon, helicopter, paramotor)? → Aircraft",
"8. Does it run on rails or is it pulled by a horse (locomotive, carriage, wagon, sleigh)? → Heritage rail & horse-drawn",
"9. Is it a caravan, motorhome, campervan or trailer for living in or carrying loads? → Caravans, motorhomes & trailers",
"10. Is it a quad, buggy, snowmobile, golf cart, kart or other small machine for rough ground, snow or a course? → Off-road & leisure vehicles",
"11. Is it a van, minibus, taxi, lorry or coach? → Vans, trucks & buses",
"12. Is it a road car (saloon, hatchback, SUV, sports car, classic, kit car)? → Cars",
"<i>Precedence: a van converted for living in is a campervan (step 9) before a van (step 11); an electric bicycle is a bicycle (step 4) before an electric scooter (step 5); a pickup is a car (step 12) before a truck (step 11); a motorcycle with a sidecar stays in step 5.</i>"]
save(d)
# checks
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('t'): print('LEFT t',k['n'])
ok=0
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for sv in k.get('see',[]):
                tgt=sv[0]
                dd=d if tgt=='G1' else json.load(open(f'/home/user/Possession-Taxonomy/rebuild/reader/{tgt}.json'))
                names={kk['n'] for a in dd['depts'] for b in a['s'] for kk in b['k']}
                if sv[1] not in names: print('BAD SEE',k['n'],sv)
