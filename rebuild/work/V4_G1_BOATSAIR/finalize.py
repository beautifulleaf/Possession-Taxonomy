import json
f='/home/user/Possession-Taxonomy/rebuild/out/G1_parts/BOATSAIR.json'
p=json.load(open(f))
BEN="https://en.wikipedia.org/wiki/Beneteau"
for m in p['moves']:
    for e in m['kind']['x']: e.pop('role',None)
AIR_BASE=("Follows Wikidata's aircraft family and aircraft model items (Q15056993, Q15056995) for the makers queried (Beechcraft, Cessna, Piper, Diamond, Pilatus, Schempp-Hirth, Tecnam, Robinson, Aeronca, Lancair, Luscombe, Maule, Pipistrel, Grob, Rutan, Robin, Icon, Daher, Jonker, Gulfstream, Dassault, Embraer, Bombardier, Learjet, Honda; first flights from P606) and the Wikipedia pages of Cirrus, Mooney, Robinson, Alexander Schleicher, Schempp-Hirth, Slingsby, Aviat, CubCrafters, Van's Aircraft, Extra, Diamond DA62, Tecnam P2012, Pilatus PC-24, Embraer Praetor and Gulfstream G650, plus the earlier hand-built lines.")
for d in p['depts']:
    for s in d['s']:
        for k in s['k']:
            if k['n']=='Trawler' and not any(e['n']=='Beneteau Swift Trawler' for e in k['x']):
                k['x'].append({'n':'Beneteau Swift Trawler','a':'Swift Trawler 42','d':"Beneteau's first trawler yacht and first Beneteau powerboat sold in the US.",'mk':'Beneteau','y':'','s':BEN,'v':[],'g':'Year not stated'})
            if d['n']=='Aircraft' and k.get('x'):
                n=len(k['x'])
                if k['n'] in('Glider','Motor-glider'):
                    tail=" Complete for the makers read from their Wikipedia pages: Alexander Schleicher (31 gliders, 5 motor-gliders), Schempp-Hirth and Slingsby; Wikidata holds no items for DG Flugzeugbau, LAK or Schweizer under those maker labels, so their earlier entries stand."
                else:
                    tail=" Covers %d entries: every model of the queried makers with an item in Wikidata (military-only types left out) or a read page; Wikidata returned no items under the maker labels Bell, Aviat, Extra, Van's, Cameron, AutoGyro, Socata and Mooney, so those come from Wikipedia pages (Bell and AutoGyro keep their earlier entries only; the Cameron page names no models)."%n
                k['sel']=AIR_BASE+tail
            elif d['n']=='Boats' and k.get('x') and 'Complete' not in k['sel'] and 'Covers' not in k['sel']:
                k['sel']+=' Covers %d entries from the pages read; no reference counts the whole space, so the total is not known.'%len(k['x'])
json.dump(p,open(f,'w'),ensure_ascii=False)
