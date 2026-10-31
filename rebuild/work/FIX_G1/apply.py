import json,os,copy
os.chdir('/home/user/Possession-Taxonomy/rebuild')
d=json.load(open('out/G1.json')); B=json.load(open('out/G1_brands.json'))
W='https://en.wikipedia.org/wiki/'
def find(name):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==name: return dp,s,k
    raise KeyError(name)
def arch(n,d_,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":mk if len(x)<4 else x[3],"y":x[1],"d":x[2]} for x in v],"dt":dt}
def add(kind,x):
    k=find(kind)[2]; k.setdefault('x',[]).append(x)
# G1-1
add('Bus or coach',arch('AEC Routemaster','Front-engined London double-decker designed by London Transport; widely preserved and privately owned.','AEC','1954–1968',W+'AEC_Routemaster',
 [('RM','1959','standard bus'),('RML','1965','long bus with extra half-window bay'),('RMC','','Green Line coach'),('RMF','1964','front-entrance long bus, mainly Northern General')],'length: standard or long · bus or coach · body liveries'))
add('Bus or coach',arch('Bristol Lodekka','Low-height double-decker with step-free lower deck, built by Bristol with Eastern Coach Works bodies.','Bristol Commercial Vehicles','1953–1968',W+'Bristol_Lodekka',
 [('LD','','rear entrance platform'),('FS','','flat floor, short'),('FSF','','flat floor, short, forward entrance'),('FL','','flat floor, long'),('FLF','','flat floor, long, forward entrance')],'rear or forward entrance · short or long · Eastern Coach Works body'))
dp,sh,_=find('Panel van')
taxi={"n":"Taxi","a":"cab · hackney carriage · black cab","d":"Passenger car built or converted for licensed hire; preserved cabs are privately owned.","t":["London-style purpose-built cab","saloon-based cab","wheelchair-accessible"],"s":W+'Austin_FX4',"x":[
 arch('Austin FX4','London black cab made 1958–1997 by BMC, British Leyland and then Carbodies.','Austin','1958–1997',W+'Austin_FX4',
  [('FX4','1958–1968','original BMC diesel model'),('FX4D','1971–1982','2520 cc diesel'),('FX4R','1982','Carbodies model, Land Rover engine'),('FX4S','1984','2495 cc diesel stopgap'),('Fairway','1989–1997','Nissan TD27 diesel')],'diesel or petrol · wheelchair-accessible FX4W · livery'),
 arch('Checker Marathon','American taxi and passenger car built by Checker Motors of Kalamazoo.','Checker Motors','1960–1982',W+'Checker_Marathon',
  [('A11 taxi','1963','taxi body code after the 1963 facelift'),('A12','1963','passenger saloon and wagon'),('Marathon Town Custom','1963','eight-seat limousine')],'taxi or passenger · saloon, wagon or limousine')]}
sh_k=[s for s in dp['s'] if s['n']=='Vans & minibuses'][0]
sh_k['n']='Vans, minibuses & taxis'; sh_k['k'].append(taxi)
# G1-2
add('Saloon',arch('Citroën DS','French executive car with hydropneumatic suspension, built 1955–1975.','Citroën','1955–1975',W+'Citro%C3%ABn_DS',
 [('DS 19','1955','original model'),('ID 19','1957','cheaper, less powerful'),('Break','1958','station wagon'),('Pallas','1965','luxury trim'),('DS 21','1965','2,175 cc engine'),('Series 3','1967','Opron restyle with swivelling headlights'),('DS 23','1973','2,347 cc engine')],'saloon, Break or Chapron cabriolet · Pallas trim · carburettor or injection'))
add('Coupé',arch('Toyota AE86','Rear-wheel-drive Corolla Levin and Sprinter Trueno coupé and liftback of 1983–1987.','Toyota','1983–1987',W+'Toyota_AE86',
 [('Corolla Levin','1983','fixed-headlight nose'),('Sprinter Trueno','1983','pop-up headlight nose'),('GT Apex','','top Japanese trim'),('GT-S','1984','North American DOHC 4A-GEC trim')],'coupé or liftback · Levin or Trueno · GT, GTV, GT Apex'))
add('Sport motorcycle',arch('Brough Superior SS100','Hand-built 998 cc V-twin from Nottingham, built 1924–1940.','Brough Superior','1924–1940',W+'Brough_Superior_SS100',
 [('Alpine Grand Sports','1925','full touring specification'),('Pendine','1925','racing model')],'JAP or Matchless V-twin engine · sidecar fittings'))
add('Sport motorcycle',arch('Suzuki GSX-R','Suzuki sports-bike family from 1984 in 250 to 1,100 cc and later 600 and 1000 cc sizes.','Suzuki','1984–',W+'Suzuki_GSX-R_series',
 [('GSX-R400','1984','Japan only'),('GSX-R750','1985','750 cc'),('GSX-R1100','1986–1998','1,100 cc'),('GSX-R750WN','1992','first water-cooled'),('GSX-R1000','2001','replaced the 1100'),('GSX-R1000R','2017','upgraded 1000')],'capacity 125–1000 cc · generation · race replica liveries'))
add('Trail bike',arch('Yamaha XT500','Single-cylinder 499 cc dual-sport that began the large trail-bike class.','Yamaha','1975–1981',W+'Yamaha_XT500',
 [('SR500','','road version sharing the engine'),('TT500','','off-road sibling')],'twin-valve single · kick start only'))
add('Single-engine piston airplane',arch('de Havilland Tiger Moth','British two-seat biplane trainer first flown in 1931; widely owned by private flyers.','de Havilland','1931–1945',W+'De_Havilland_Tiger_Moth',
 [('DH.82','1932','Tiger Moth I, 120 hp Gipsy III'),('DH.82A','1934','Tiger Moth II, 130 hp Gipsy Major'),('DH.82C','1937','Canadian cold-weather version')],'open cockpits · Gipsy engine · RAF or civil colours'))
# G1-3 Biltwell
k=find('Full-face helmet')[2]
k['m']=[m for m in k['m'] if m[0]!='Biltwell Gringo']
k['x'].append(arch('Biltwell Gringo','Retro-styled full-face helmet sold by Biltwell in several variants.','Biltwell','',  'https://www.biltwellinc.com/collections/gringo',[('Gringo S','','listed as its own collection'),('Gringo SV','','listed as its own collection; integrated shield')],'gloss, flat and metallic colours · special graphics'))
# G1-4 vehicle care
care=[s for s in find('Car-wash shampoo')[0]['s']]
def trim(m,cap=8):
    m=[x for x in m if x[1] not in('Halfords','CarPlan')]
    seen={};out=[]
    for x in m:
        if len(m)>cap and seen.get(x[1],0)>=1: continue
        seen[x[1]]=1;out.append(x)
    return out[:cap]
for s in care:
    for k in s['k']:
        if 'm' in k:
            k['m']=trim(k['m'])
            if not k['m']: del k['m']
# G1-5 utility trailer
ut={"n":"Utility trailer","a":"box trailer · cargo trailer","d":"Towed trailer for goods, vehicles or boats, from open box trailers to car transporters.","t":[],"s":"https://www.iwt.co.uk/products/box-van/box-van-braked?tab=spec","m":[],"r":[]}
dpc,shc,_=find('Box trailer')
names=['Box trailer','Boat trailer','Car transporter trailer','Tipper trailer','Motorcycle trailer']
tmap={'Box trailer':'box trailer (open or enclosed, braked or unbraked)','Boat trailer':'boat trailer','Car transporter trailer':'car transporter (open or enclosed)','Tipper trailer':'tipper trailer','Motorcycle trailer':'motorcycle trailer'}
for n in names:
    k=find(n)[2]; ut['t'].append(tmap[n]); ut['m']+=k.get('m',[]); ut['r']+=k.get('r',[])
shc['k']=[k for k in shc['k'] if k['n'] not in names]
shc['k'].insert(0,ut)
# G1-6 chain care shelf
dpv,shv,ck=find('Chain cleaner and lubricant')
shv['k']=[k for k in shv['k'] if k is not ck]
dpv['s'].append({"n":"Chain care","k":[ck]})
# G1-7 bicycles
find('BMX bike')[2]['m']=[['Boulevard','Haro'],['Nova','WeThePeople'],['BK Team','GT'],['Solo','Premium'],['Amplitude Wave','Saracen']]
find('Electric bike')[2]['m']=[['Turbo Vado SL 5.0 EQ','Specialized'],['Compact Neo','Cannondale'],['eSpresso CC 675 EQ','Merida'],['RadRunner 3 Plus','Rad Power'],['RHe0 3','Whyte'],['Charger3','Riese & Müller']]
find('Gravel bike')[2]['m']=[['Kanzo Fast','Ridley'],['Grail CF SLX','Canyon'],['Revolt Advanced','Giant'],['Rave SLR','Wilier'],['Topstone Carbon','Cannondale'],['Áspero','Cervélo'],['Diverge','Specialized'],['Stigmata','Santa Cruz'],['Checkpoint ALR','Trek'],['Tripster AT+','Kinesis']]
# brands
bs=B['b']; have={x['n'].lower() for x in bs}
def brand(n,c,f,seg,kf,dd,sig,s):
    if n.lower() in have: return
    bs.append({"n":n,"c":c,"f":f,"seg":seg,"d":dd,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s,"kf":kf}); have.add(n.lower())
brand('AEC','United Kingdom','1912','Heritage manufactory','buses and lorries','British maker of buses, motorcoaches and lorries; shut down by British Leyland in 1979.',['AEC Routemaster'],W+'Associated_Equipment_Company')
brand('Bristol Commercial Vehicles','United Kingdom','1908','Heritage manufactory','buses and lorries','English builder of buses, trucks and railbus chassis; closed in 1983.',['Bristol Lodekka'],W+'Bristol_Commercial_Vehicles')
brand('Austin','United Kingdom','1905','Heritage manufactory','cars and cabs','British carmaker at Longbridge that merged with Morris in 1952; the marque ended in 1988.',['Austin FX4'],W+'Austin_Motor_Company')
brand('Checker Motors','United States','1922','Heritage manufactory','taxicabs','Kalamazoo, Michigan maker of taxicabs and the Marathon; ceased business in 2010.',['Checker Marathon'],W+'Checker_Motors_Corporation')
brand('Brough Superior','United Kingdom','1919','Heritage manufactory','V-twin motorcycles','Nottingham motorcycle maker; production ended in 1940 and the name was revived in 2008.',['Brough Superior SS100'],W+'Brough_Superior')
brand('de Havilland','United Kingdom','1920','Heritage manufactory','Moth aircraft','British aircraft maker founded by Geoffrey de Havilland; absorbed into Hawker Siddeley in 1963.',['de Havilland Tiger Moth'],W+'De_Havilland')
brand('Biltwell','','','Specialist','retro helmets','Maker of the Gringo retro helmet line.',['Biltwell Gringo'],'https://www.biltwellinc.com/collections/gringo')
for fn,o in(('out/G1.json',d),('out/G1_brands.json',B)):
    json.dump(o,open(fn+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(fn+'.tmp',fn)
