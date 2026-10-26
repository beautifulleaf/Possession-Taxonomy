import json, os
W='https://en.wikipedia.org/wiki/'
TW=W+'Trailer_bike'; BT=W+'Bicycle_trailer'; CS=W+'Child_bicycle_seat'; BU=W+'Burley_Design'
TH='https://www.thule.com/en-us/articles/guides/thule-bike-trailer-comparison'
TS='https://www.thule.com/en-us/child-bike-seats'
HX='https://hamax.com/en/timeline-history'; WO='https://woom.com/en_INT/find-the-right-woom-bike'
WB=W+'Wheelie_bike'; CH=W+'Raleigh_Chopper'; SR=W+'Schwinn_Sting-Ray'; IS=W+'Islabikes'; TR=W+'Training_wheels'
CP='https://www.cpsc.gov/Recalls/2011/Weehoo-Recalls-Bike-Trailers-Due-to-Fall-and-Crash-Hazards'
FR='https://bikebiz.com/leaps-and-bounds-the-story-behind-frog-bikes/'
B=['baby']
def v(n,mk='',y='',d=''):
    o={'n':n}
    if mk:o['mk']=mk
    if y:o['y']=y
    if d:o['d']=d
    return o
kinds=[
{'n':"Children's bicycle",'a':"kids' bike · child's bike",'d':"Pedal bicycle scaled for a child, usually sized by wheel diameter from about 12 to 26 inches.",
 't':['with training wheels','coaster-brake single-speed','geared junior','kids\' mountain bike','lightweight child-specific'],'tg':B,'s':TR,
 'x':[
  {'n':'Huffy Convertible','a':'','d':'Children\'s bike sold with the first training wheels, introduced by Huffy.','mk':'Huffy','y':'1949','s':TR,'v':[],'dt':'removable side training wheels'},
  {'n':'Wheelie bike','a':'muscle bike · high-riser · dragster · banana bike','d':'1960s children\'s bike styled like a chopper motorcycle: ape-hanger bars, banana seat with sissy bar, 16–20 in wheels.','mk':'','y':'1963','s':WB,
   'v':[v('Penguin','Huffy','1963','first of the type to market'),v('Dragster II','Huffy','1964'),v('Kingkat','Murray','','long chopper-style forks'),
        v('Tomahawk','Øglænd (DBS)','','Norwegian'),v('Dragstar','Malvern Star','','Australian'),v('Tigrão','Monark','','Brazilian')],
   'dt':'wheels 16–20 in · banana seat · sissy bar · ape-hanger bars'},
  {'n':'Schwinn Sting-Ray','a':'Project J-38','d':'Schwinn\'s wheelie bike designed by Al Fritz after a California youth trend.','mk':'Schwinn','y':'1963','s':SR,
   'v':[v('Sting-Ray','Schwinn','1963','launched June 1963, 20 in tyres'),v('Sting-Ray Deluxe','Schwinn','1963','mudguards, white-wall tyres, padded seat'),
        v('Sting-Ray Super Deluxe','Schwinn','1964','front spring fork, sissy bar'),v('Krate','Schwinn','1968','front spring fork, drum brake (per Wheelie bike article)'),
        v('Pea Picker','Schwinn','1972','rear disc brake (per Wheelie bike article)'),v('Sting-Ray reintroduction','Schwinn','2010','under Dorel')],
   'dt':'20 in wheels · banana seat · ape-hanger bars · 5-speed versions'},
  {'n':'Raleigh Chopper','a':'','d':'British wheelie bike with 16 in front and 20 in rear wheels and frame-mounted gear lever; best-selling children\'s bike in the UK.','mk':'Raleigh','y':'1968','s':CH,
   'v':[v('Mk1','Raleigh','1968','UK launch 1969; to 1972'),v('Mk2','Raleigh','1972','to 1983 in UK; Sprint GT, Pink 5-speed, SE sub-models'),
        v('Mk3','Raleigh','2004','re-issue to 2012, handlebar gear controls'),v('Mk-IV','Raleigh','2023','second re-issue, crossbar shifter')],
   'dt':'16/20 in wheels · 3- or 5-speed Sturmey-Archer · colours'},
  {'n':'woom GO','a':'woom ORIGINAL (to 2024)','d':'Lightweight child-specific bike range numbered by size; woom\'s first model.','mk':'woom','y':'','s':WO,
   'v':[v('GO 2','woom','','14 in, ages 3–4.5'),v('GO 3','woom','','16 in, ages 4–6'),v('GO 3 AUTOMAGIC','woom','','16 in, automatic two-speed hub'),
        v('GO 4','woom','','20 in, ages 6–8'),v('EXPLORE 4–6','woom','','20–26 in'),v('OFF / OFF AIR 4–6','woom','','kids\' mountain bikes')],
   'dt':'wheel 14–26 in · gears · colours'},
  {'n':'Islabikes Beinn','a':'','d':'Lightweight child-sized bike from Isla Rowntree\'s company, with components scaled to the rider.','mk':'Islabikes','y':'','s':IS,
   'v':[v('Beinn 24','Islabikes','','children\'s model'),v('Beinn 29','Islabikes','2011','adult model'),v('Cnoc 14, 16, 18','Islabikes','2025','limited batch of learner bikes')],
   'dt':'wheel size · frame size'}]},
{'n':'Trailer bike','a':'trailercycle · trail-a-bike · tagalong · half wheeler','d':'One-wheeled half bicycle with saddle, bars and pedals, hitched to an adult bicycle so a child can ride and pedal behind.',
 't':['seatpost hitch','rack hitch','two-wheeled tandem trailer','recumbent','tow-bar conversion (FollowMe coupling, Trail-Gator bar)'],'tg':B,'s':'https://www.tikesbikes.com/collections/burley-trailers',
 'x':[
  {'n':'Adams Trail-a-Bike','a':'','d':'Seatpost-hitched one-wheel trailer bike patented by Canadian inventor Delbert Adams.','mk':'Adams','y':'1987','s':TW,'v':[v('patent','Adams','1987'),v('Trail-a-Bike sales','Adams','early 1990s')],'dt':'single speed or geared'},
  {'n':'Burley Piccolo','a':'','d':'Burley trailercycle that attaches to a rack on the adult bike rather than the seatpost.','mk':'Burley','y':'','s':TW,'v':[],'dt':'rack hitch'},
  {'n':'Burley Kazoo','a':'','d':'Burley trailercycle that hitches behind an adult bicycle.','mk':'Burley','y':'','s':BU,'v':[],'dt':''},
  {'n':'Weehoo iGo','a':'','d':'Pedal trailer with a recumbent-style seat for passengers 38–52 in tall, 20 in wheel and pannier pockets.','mk':'Weehoo','y':'2011','s':CP,'v':[v('2011 model year','Weehoo','2011','recalled for cracking hitch receiver')],'dt':'steel frame · 20 in wheel · panniers'},
  {'n':'Pashley U+2','a':'','d':'Two-wheeled tandem trailer bike.','mk':'Pashley','y':'','s':TW,'v':[],'dt':''},
  {'n':'Hase Trets','a':'','d':'Recumbent two-wheeled trailer bike.','mk':'Hase','y':'','s':TW,'v':[],'dt':''}]},
{'n':'Bicycle trailer','a':'child trailer · bike trailer','d':'Trailer towed by a bicycle, for a child, a dog or goods.',
 't':['child trailer','multisport trailer (stroller, jogging, ski)','cargo trailer','pet trailer','single-seat','double-seat'],'tg':B,'s':'https://burley.com/products/bee',
 'x':[
  {'n':'Burley child trailer','a':'','d':'Burley\'s blue-and-yellow child trailers, among the first on sale in the early 1980s.','mk':'Burley','y':'early 1980s','s':BU,
   'v':[v("d'lite ST",'Burley','2009'),v('Solo ST','Burley','2009'),v('D Lite X','Burley'),v('Cub X','Burley'),v('Encore X','Burley'),v('Bee','Burley'),v('Honey Bee','Burley')],
   'dt':'single or double · suspension · stroller kit'},
  {'n':'Thule Chariot','a':'Chariot Carriers','d':'Canadian multisport child trailer line, bought by Thule in 2011 and rebranded Thule in 2013.','mk':'Thule','y':'2013','s':TH,
   'v':[v('Chariot Sport 2','Thule','','premium; disc brakes, integrated lights'),v('Chariot Cross 2','Thule','','adjustable suspension'),v('Chariot Cab','Thule','','double only, cargo and commuting'),v('Chariot Lite','Thule','','lightweight basic model')],
   'dt':'single or double · cycling, strolling, jogging, ski kits'},
  {'n':'Hamax Outback','a':'','d':'Multifunctional child bike trailer from Hamax.','mk':'Hamax','y':'2015','s':HX,'v':[],'dt':''}],
 'm':[['Cocoon','Hamax'],['Breeze','Hamax'],['Courier','Thule'],['Travoy','Burley'],['Nomad','Burley'],['Tail Wagon','Burley']]},
{'n':'Child bike seat','a':'child bicycle seat · kid seat','d':'Seat with harness fitted to an adult bicycle to carry a small child, mounted front or rear.',
 't':['front-mounted','rear frame-mounted','rear rack-mounted','top-tube saddle (older children)'],'tg':B,'s':CS,
 'x':[
  {'n':'Thule Yepp 2 maxi','a':'','d':'Rear child seat from the Dutch Yepp line, for rack, frame or MIK HD mounting.','mk':'Thule','y':'','s':TS,'v':[v('Yepp 2 maxi rack mount','Thule'),v('Yepp 2 maxi frame mount','Thule'),v('Yepp 2 MIK HD','Thule')],'dt':'mount · colours'},
  {'n':'Thule Yepp 2 mini','a':'','d':'Front-mounted child seat placing the child between rider\'s arms.','mk':'Thule','y':'','s':TS,'v':[v('Yepp 2 mini','Thule'),v('Yepp Nexxt 2 mini','Thule')],'dt':'colours'},
  {'n':'Hamax Siesta','a':'','d':'Hamax rear child seat, launched alongside the Smiley.','mk':'Hamax','y':'2006','s':HX,'v':[],'dt':''},
  {'n':'Hamax Caress','a':'','d':'Hamax rear child seat.','mk':'Hamax','y':'2013','s':HX,'v':[],'dt':''}]}]
brands=[
 {'n':'Burley','c':'United States','f':'1978','seg':'Child, cargo and pet bike trailers','d':'Eugene, Oregon, maker run as a worker cooperative until 2006; bicycles dropped in 2006 to focus on trailers.','lines':["d'lite",'Solo','Cub','Encore','Honey Bee','Bee','Nomad','Travoy','Piccolo','Kazoo'],'sig':['Burley child trailer','Burley Piccolo'],'rel':['Thule','Weehoo'],'s':BU},
 {'n':'Thule','c':'Sweden','f':'1942','seg':'Carrying and child transport','d':'Swedish group from Hillerstorp, owner of Chariot (2011) and Yepp (2016).','lines':['Chariot','Yepp','Courier'],'sig':['Thule Chariot','Thule Yepp 2 maxi'],'rel':['Burley','Hamax'],'s':W+'Thule_Group'},
 {'n':'Hamax','c':'Norway','f':'1958','seg':'Child bike seats and trailers','d':'Fredrikstad firm, founded as Plast & Form AS, which made its first bike seat (Bike Rider) in 1981.','lines':['Siesta','Caress','Outback','Cocoon','Breeze'],'sig':['Hamax Siesta','Hamax Outback'],'rel':['Thule'],'s':HX},
 {'n':'woom','c':'Austria','seg':"Lightweight children's bikes",'d':"Austrian children's bike maker co-founded by two fathers, Marcus and Christian.",'lines':['GO','EXPLORE','OFF','OFF AIR','UP','NOW'],'sig':['woom GO'],'rel':['Islabikes','Frog Bikes'],'s':WO},
 {'n':'Islabikes','c':'United Kingdom','f':'2005','seg':"Lightweight children's bikes",'d':'Shropshire company founded by Isla Rowntree; stopped regular bike production in 2023.','lines':['Beinn','Cnoc'],'sig':['Islabikes Beinn'],'rel':['woom','Frog Bikes'],'s':IS},
 {'n':'Frog Bikes','c':'United Kingdom','f':'2013','seg':"Lightweight children's bikes",'d':'Founded by Jerry and Shelley Lawson; opened a UK factory in 2016.','rel':['Islabikes','woom'],'s':FR},
 {'n':'Weehoo','c':'United States','seg':'Trailer bikes','d':'Golden, Colorado, maker of the iGo pedal trailer.','lines':['iGo'],'sig':['Weehoo iGo'],'rel':['Burley'],'s':CP},
 {'n':'Raleigh','c':'United Kingdom','f':'1887','seg':'Bicycles','d':'Nottingham bicycle maker.','sig':['Raleigh Chopper'],'rel':['Schwinn'],'s':'knowledge'},
 {'n':'Schwinn','c':'United States','f':'1895','seg':'Bicycles','d':'Chicago-founded bicycle maker, later owned by Dorel.','sig':['Schwinn Sting-Ray'],'rel':['Raleigh','Huffy'],'s':'knowledge'},
 {'n':'Huffy','c':'United States','seg':'Mass-market bicycles','d':'American bicycle maker that introduced training wheels in 1949.','sig':['Huffy Convertible'],'rel':['Schwinn'],'s':TR},
 {'n':'Adams','c':'Canada','seg':'Trailer bikes','d':'Trail-a-Bike brand of inventor Delbert Adams, who patented the trailer bike in 1987.','lines':['Trail-a-Bike'],'sig':['Adams Trail-a-Bike'],'s':TW},
 {'n':'Pashley','c':'United Kingdom','seg':'Traditional and utility bicycles','d':'English bicycle maker.','sig':['Pashley U+2'],'s':'knowledge'},
 {'n':'Hase','c':'Germany','seg':'Recumbent and special cycles','d':'German maker of recumbent and special-needs cycles.','sig':['Hase Trets'],'s':'knowledge'}]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':"Children's bicycle and Child bike seat are new kinds. Balance bikes left to Toys (woom GO 1 / 1 PLUS not listed). Frog Bikes has a brand entry but no archetype: frogbikes.com now redirects to Evans Cycles and no retrieved page named its models. Hamax Zenith/Observer and Thule RideAlong, Burley Bee details not confirmed on retrieved pages, left out. Chariot founding year not confirmed. Raleigh/Schwinn/Pashley/Hase facts are knowledge-level; Huffy cites Training wheels page."}
p='work/G1/shelves/03_04.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('written')
