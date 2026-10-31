import json,copy,os
SRC='/home/user/Possession-Taxonomy/rebuild/out/A5.json'
d=json.load(open(SRC))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def arch(kn,an):
    k=K[kn]
    for i,a in enumerate(k['x']):
        if a['n']==an: return k['x'].pop(i)
    raise KeyError((kn,an))
def drop(kn,*names):
    for n in names: arch(kn,n)
W='https://en.wikipedia.org/wiki/Watch'
PW='https://en.wikipedia.org/wiki/Pocket_watch'
# --- demote generic archetypes ---
drop('Longcase clock','English longcase')
drop('Lantern clock','English lantern clock')
drop('Bracket clock','English bracket clock')
drop('Carriage clock','French carriage clock')
drop('Skeleton clock','English skeleton clock','French skeleton clock')
drop('Marine chronometer','English box chronometer')
drop('Watch strap','Dress leather strap','Aviator rivet strap','Rubber dive strap','Sailcloth strap')
drop('Early pocket watch','Verge pocket watch','Cylinder pocket watch')
drop('Lever pocket watch','English lever pocket watch')
drop('Cuckoo clock','Carved cuckoo clock','Chalet cuckoo clock')
# merge duplicate Vienna regulator
wr=K['Wall regulator']['x']
v=[a for a in wr if a['n']=='Vienna regulator']
v0=v[0]; v0['y']='c. 1780–1930'; v0['dt']=v[1].get('dt','')
wr.remove(v[1])
v0['d']='Glazed wall regulator with a long pendulum, first made in Vienna around 1780; factory-made across the German-speaking world until about 1930.'
# maker ranges -> r
def to_range(kn,an,rname,mk):
    arch(kn,an); K[kn].setdefault('r',[]).append([rname,mk])
to_range('Electric synchronous clock','Telechron clock','Telechron synchronous clocks','Telechron')
to_range('Marine chronometer','Ulysse Nardin marine chronometer','Marine chronometers','Ulysse Nardin')
to_range('Complicated pocket watch','Daniels co-axial watches','Co-axial pocket and wrist watches','George Daniels')
# moves between kinds
K['Terry']=None
terry=arch('Mantel clock','Terry thirty-hour shelf clock'); K['American shelf clock']['x'].insert(0,terry)
del K['Terry']
cart=arch('Bracket clock','French bracket clock (pendule cartel)')
cart['n']='Pendule cartel'; cart['d']='Rococo wall clock whose ornate gilt-bronze case and bracket are one piece; the Paris form behind the cartel clock.'
eco=arch('Everyday watch','Eco-Drive'); wave=arch('Digital watch','Wave Ceptor')
# --- new kinds ---
def newk(n,a,dd,s,**kw):
    k={'n':n,'a':a,'d':dd,'s':s,'x':[],'m':[],'r':[]}; k.update(kw); K[n]=k; return k
newk('Skeleton watch','open-worked watch · open heart','Mechanical watch with the movement cut away so its wheels and bridges show through the dial, case back or both.','https://en.wikipedia.org/wiki/Skeleton_watch',tt=[['Openwork',['Full skeleton','Semi-skeleton','Open heart']],['Showing through',['Dial','Case back','Both']]])
newk('Quartz watch','quartz analogue watch','Watch kept on time by a battery-driven quartz oscillator, with hands rather than a digital display.',W,tt=[['Hands',['Time only','Date','Chronograph']],['Second hand',['Ticking','Sweep']]])
newk('Solar-powered watch','light-powered watch','Quartz watch charged by light through cells behind the dial, so it needs no battery change.',W,x=[eco],tt=[['Cells',['Behind the dial','Around the dial']]])
newk('Radio-controlled watch','atomic watch','Watch that corrects itself from a broadcast radio time signal.',W,x=[wave],tt=[['Signal',['One region','Multi-band world']]])
newk('Trench watch','wristlet · campaign watch','First World War wrist-worn watch adapted from the pocket watch, with wire lugs and a protected dial.',PW)
newk('Nuremberg egg','clock-watch','Sixteenth-century spring-driven clock-watch worn on a chain, with only an hour hand.',PW)
newk('Cartel clock','wall clock · cartouche clock','Wall clock in a cartouche-shaped case that hangs directly on the wall, often in gilt bronze (ormolu).','https://en.wikipedia.org/wiki/Cartel_clock',x=[cart],tt=[['Case material',['Gilt bronze (ormolu)','Gilded wood']],['Style',['Rococo','Neoclassical']]])
K['Split-flap clock']['n']='Flip clock'; K['Flip clock']=K.pop('Split-flap clock')
fc=K['Flip clock']; fc['a']='split-flap clock · flap clock'; fc['d']='Clock that shows the time on flaps that drop to reveal each new number; table, wall and station sizes.'; fc['s']='https://en.wikipedia.org/wiki/Flip_clock'
fc['x'].insert(0,{'n':'Plato clock','a':'','d':'Eugene Fitch’s early flip clock, patented 1902–04 and sold in tens of thousands.','mk':'','y':'1904','s':'https://en.wikipedia.org/wiki/Flip_clock','v':[]})
fc['tt']=[['Power',['Synchronous mains motor','Quartz']],['Size',['Desk','Wall','Station']]]
# --- tt definitions ---
TT={
'GMT & world-time watch':[['Zones shown',['GMT (one extra zone)','World time (all zones)']],['Local hour setting',['Fixed 24-hour hand','Jumping local hour hand']]],
'Digital watch':[['Display',['LCD','LED','Analogue-digital']],['Case build',['Resin','Steel']]],
'Calendar watch':[['Calendar level',['Annual calendar','Perpetual calendar','Triple calendar']],['Astronomical display',['Moon phase','No moon phase']]],
'Chiming watch':[['Striking mode',['Minute repeater','Petite sonnerie','Grande sonnerie']]],
'Early pocket watch':[['Escapement',['Verge','Cylinder']],['Winding',['Key-wind']],['Case',['Open-face','Hunter','Demi-hunter']]],
'Lever pocket watch':[['Origin',['English lever','Swiss lever','American lever']],['Winding',['Key-wind','Stem-wind']],['Case',['Open-face','Hunter','Demi-hunter']]],
'Railroad-grade pocket watch':[['Size',['16-size','18-size']],['Setting',['Lever-set']],['Case',['Open-face']]],
'Dollar watch':[['Case',['Open-face']]],
'Complicated pocket watch':[['Complication',['Repeater','Chronograph','Perpetual calendar','Grande complication']]],
'Dive watch':[['Depth rating',['100 m','200–300 m','1,000 m and more']],['Case size',['Under 38 mm','38–42 mm','Over 42 mm']],['Bezel insert',['Aluminium','Ceramic','Steel']]],
'Chronograph':[['Dial layout',['Bicompax','Tricompax','Single register']],['Movement',['Manual-wind','Automatic','Quartz']]],
'Longcase clock':[['Size',['Grandfather','Grandmother']],['Run',['30-hour','8-day']],['Origin',['English','French (Comtoise)','Scandinavian','American']]],
'Lantern clock':[['Origin',['London','Rural','Turkish-market']],['Age',['17th-century','Victorian revival']]],
'Cuckoo clock':[['Style',['Carved','Chalet']],['Movement',['Weight-driven 30-hour','Weight-driven 8-day','Quartz']]],
'Bracket clock':[['Origin',['English','Continental']],['Striking',['Timepiece','Striking','Pull repeater']]],
'Carriage clock':[['Striking',['Timepiece only','Striking','Repeating','Grande sonnerie']],['Panels',['Glass','Enamel','Porcelain']]],
'Skeleton clock':[['Origin',['English','French']],['Frame style',['Cathedral','Rafter','Great-wheel','Keyhole']]],
'Marine chronometer':[['Origin',['English box','German','American']]],
'Alarm clock':[['Display',['Analogue','Digital']],['Smart features',['Smart speaker']]],
'Wall clock':[['Movement',['Quartz sweep (silent)','Quartz ticking','Radio-controlled','Pendulum']]],
'Digital clock':[['Time source',['Quartz','Radio-controlled ("atomic")']],['Extra display',['Projection','Weather station']]],
'Sundial':[['Form',['Horizontal garden','Vertical wall','Armillary','Portable']]],
'Watch strap':[['Material',['Calf leather','Alligator or crocodile','Rubber','Silicone','Nylon','Sailcloth','Canvas']],['Construction',['Two-piece','Pass-through (one piece)']],['Fastening',['Tang buckle','Deployant clasp']]],
'Watch bracelet':[['Construction',['Solid link','Mesh','Rubber-integrated']]],
'Watch case':[['Case size',['Under 38 mm','38–42 mm','Over 42 mm']],['Material',['Steel','Titanium']]],
'Watch dial':[['Movement fit',['NH35/NH36 (28.5 mm)']],['Date',['With date window','Without date window']],['Lume',['C3','BGW9']]],
'Watch hands':[['Movement fit',['NH-family']],['Hand shape',['Mercedes','Sword','Snowflake','Plongeur']]],
'Watch crystal':[['Material',['Sapphire','Mineral','Acrylic (hesalite)']],['Profile',['Flat','Double-domed']],['Coating',['Anti-reflective','Uncoated']]],
'Watch bezel & insert':[['Material',['Steel','Aluminium','Ceramic']],['Scale',['60-minute dive','GMT 24-hour']]],
'Small watch parts':[['Part',['Clasp & buckle','Spring bar','Crown & tube']]],
'Clock repair parts':[['Part',['Movement or fit-up','Pendulum','Hands','Dial','Suspension spring','Mainspring','Bushings','Chime rods and gongs','Weights and cable','Cuckoo and 400-day parts']]],
}
for n,t in TT.items():
    K[n]['tt']=t; K[n].pop('t',None)
for k in K.values():
    if k and k.get('t'): print('LEFT t:',k['n'],k['t']); 
# --- see ---
SEE={
'Digital watch':[['D2','Smartwatch','a digital watch with apps and sensors']],
'Dive watch':[['D2','Multisport GPS watch','dive computers and GPS sports watches']],
'Watch strap':[['D2','Watch strap','bands made for smartwatches']],
'Sundial':[['B4','Garden sundial','the garden-ornament sundial']],
'Hourglass':[['E1','Game clock','timers used in games']],
'Visual timer':[['B5','Kitchen timer','countdown timers for cooking']],
'Alarm clock':[['D3','Clock radio','alarm clock with a radio']],
'Alarm watch':[['A5','Alarm clock','alarm on a bedside clock instead']],
'Watch chain':[['A5','Early pocket watch','the watch it is worn with']],
'Chronometer watch':[['A5','Marine chronometer','the ship’s precision clock']],
'Marine chronometer':[['A5','Chronometer watch','certified precision on the wrist']],
'Skeleton watch':[['A5','Skeleton clock','the same open frame in a clock']],
'Skeleton clock':[['A5','Skeleton watch','the same open frame on the wrist']],
'Bracket clock':[['A5','Cartel clock','the wall-hung form']],
'Cartel clock':[['A5','Bracket clock','the table form with a handle']],
'Carriage clock':[['A5','Travel clock','a modern clock for journeys']],
'Travel clock':[['A5','Carriage clock','the antique travelling clock']],
'Flip clock':[['A5','Digital clock','a modern digital display']],
'Electric & early quartz watch':[['A5','Quartz watch','the later mass-market quartz']],
'Quartz watch':[['A5','Electric & early quartz watch','the first electric and quartz models']],
'Watch bezel & insert':[['A5','Dive watch','the watch the bezel is fitted to']],
'Coin watch':[['A3','Happy Diamonds watch','jewellery watches'] ] if False else [],
}
for n,s in SEE.items():
    if s: K[n]['see']=s
# --- structure ---
def sh(n,t,ax,kinds): return {'n':n,'t':t,'ax':ax,'k':[K[x] for x in kinds]}
old={dp['n']:dp for dp in d['depts']}
def dept(n,t,ax,shelves):
    o=old[n]; o['t']=t; o['ax']=ax; o['s']=shelves; return o
depts=[]
depts.append(dept('Wristwatches',
 'Watches worn on the wrist and collected as model families; a smartwatch or GPS sports watch → Phones, Tablets & Personal Devices (D2), a watch carried in a pocket → Pocket watches.',
 'What sets the watch apart: a job it is built for, a style, an electronic movement or a mechanism it shows?',
 [sh('Tool & sports watches','Watches built for a job: diving, flying, field service, crossing time zones or timing; a luxury sports look without the job → Style & dress watches.','kinds by job: water, air, ground, travel, timing',
     ['Dive watch','Pilot watch','Field watch','Trench watch','GMT & world-time watch','Chronograph','Flyback chronograph','Split-seconds chronograph']),
  sh('Style & dress watches','Watches chosen for their look and occasion, such as the Datejust, Tank or Calatrava; a watch built for a job → Tool & sports watches.','kinds from plainest to most ornamental',
     ['Everyday watch','Prestige everyday watch','Dress watch','Integrated-bracelet sports watch','Shaped watch','Jewellery watch']),
  sh('Electronic watches','Watches run by a battery, light or radio signal rather than a wound spring, such as the Accutron, Seiko Astron and F-91W; smart ones → D2.','kinds by electronic technology, oldest first',
     ['Electric & early quartz watch','Quartz watch','Digital watch','Solar-powered watch','Radio-controlled watch']),
  sh('Complication & precision watches','Mechanical watches prized for what the movement does or shows beyond the hours: certified precision, calendars, chimes, a rotating cage.','kinds by what the movement adds: precision, display, calendar, sound, spectacle',
     ['Chronometer watch','Jumping-hours watch','Skeleton watch','Calendar watch','Alarm watch','Chiming watch','Tourbillon watch','Grande-complication watch','Avant-garde watch'])]))
depts.append(dept('Pocket watches',
 'Watches carried on a chain or in a pocket, collected by era, grade and make; a wristwatch → Wristwatches.',
 'Is the watch defined by its era, its grade or a special form?',
 [sh('Movement eras','Pocket watches defined by the age and escapement of the movement, such as the Nuremberg egg or the Waltham Model 1857; a graded railroad watch → Grade & complexity.','kinds by era, oldest first',
     ['Nuremberg egg','Early pocket watch','Lever pocket watch']),
  sh('Grade & complexity','Pocket watches defined by how well or how elaborately they are made, such as the Hamilton 992 or the Ingersoll Yankee.','kinds by build, cheapest first',
     ['Dollar watch','Railroad-grade pocket watch','Complicated pocket watch']),
  sh('Special forms','Pocket watches hidden in another object, such as a Corum coin watch.','kinds by the object that hides the watch',['Coin watch'])]))
depts.append(dept('Collectible clocks',
 'Clocks collected for age, maker, form or design, from longcase to flip clocks; a clock bought just to use → Everyday clocks, a chess clock → E1.',
 'Where does the clock stand or hang, and is it a precision or electric piece?',
 [sh('Floor & wall clocks','Clocks that stand on the floor or hang on a wall, such as the longcase, banjo, Vienna regulator-style dial clock or cuckoo; a precision regulator → Precision clocks.','kinds from floor-standing to wall-hung, oldest first',
     ['Longcase clock','Lantern clock','Tavern clock','Cartel clock','Banjo clock','Dial clock','Cuckoo clock']),
  sh('Table & mantel clocks','Clocks that stand on a table, shelf or mantel, such as the carriage, bracket and Atmos clock; a wall form → Floor & wall clocks.','kinds by form: portable spring clocks, shelf clocks, glass-domed and novelty clocks',
     ['Bracket clock','Carriage clock','Mantel clock','American shelf clock','Wadokei','Skeleton clock','Anniversary & Atmos clock','Mystery clock']),
  sh('Precision clocks','Clocks built to keep exact time, such as wall regulators and marine chronometers; a wristwatch chronometer → Complication & precision watches.','kinds by use: observatory and shop, then ship',
     ['Wall regulator','Marine chronometer']),
  sh('Electric & design clocks','Clocks collected for mains power, display or designer, such as Telechron, Solari Cifra and Howard Miller; a mechanical antique → Floor & wall or Table & mantel.','kinds by how they run or look: mains motor, flap display, designer styling',
     ['Electric synchronous clock','Flip clock','Design clock'])]))
depts.append(dept('Everyday clocks',
 'Clocks bought to use at home; a clock radio → Audio & Video (D3), a kitchen timer → Kitchen & Dining (B5), a collectible clock → Collectible clocks.',
 'Where is the clock used: by the bed, on a wall, or on a desk or shelf?',
 [sh('Bedside clocks','Clocks made to wake you, such as alarm clocks and sunrise lamps; a clock without an alarm → Room clocks.','kinds by how they wake you: sound, then light',
     ['Alarm clock','Sunrise alarm clock']),
  sh('Room clocks','Clocks that tell the time in a room, hung on a wall, stood on a desk or carried; one that wakes you → Bedside clocks.','kinds by placement: hung, stood (analogue or digital), carried',
     ['Wall clock','Desk clock','Digital clock','Travel clock'])]))
depts.append(dept('Timers & timing instruments',
 'Things that time an interval or tell the time from sun or sand; kitchen timers → Kitchen & Dining (B5), game clocks → Toys & Games (E1).',
 'Does it measure an interval, or tell the time of day from the sun?',
 [sh('Interval timers','Devices that count an interval up or down, such as the Time Timer, a stopwatch or an hourglass.','kinds by how the interval shows: a count, a shrinking disc, falling sand',
     ['Stopwatch','Visual timer','Hourglass']),
  sh('Sundials','Instruments that tell the time of day from a shadow, for gardens, walls or the pocket.','one kind',['Sundial'])]))
depts.append(dept('Straps, storage & parts',
 'Things that hold, store, maintain or replace parts of a watch or clock; smartwatch bands → Phones, Tablets & Personal Devices (D2).',
 'What does it do for the watch: hold it on the person, store it, or replace a part?',
 [sh('Straps, bracelets & chains','What holds a watch to the wrist or pocket, such as a NATO strap, Jubilee bracelet or Albert chain.','kinds by build: flexible strap, linked bracelet, chain',
     ['Watch strap','Watch bracelet','Watch chain']),
  sh('Storage & winding','What keeps watches safe and running, such as a winder or watch roll.','kinds by job: keep wound, keep safe',['Watch winder','Watch box & roll']),
  sh('Watch modding parts','Parts swapped to rebuild or customise a watch, such as an NH35 movement or SKX-style case.','kinds from the inside out: movement, dial, hands, case, crystal, bezel, small parts',
     ['Watch movement','Watch dial','Watch hands','Watch case','Watch crystal','Watch bezel & insert','Small watch parts']),
  sh('Clock parts','Replacement parts for clocks.','one kind',['Clock repair parts'])]))
# fix remaining shelf ax that is not a real axis
for dp in depts:
    for s in dp['s']:
        if s['ax']=='one kind': del s['ax']
d['depts']=depts
d['ax']='What is the object: a watch worn on the wrist, a pocket watch, a clock, a timer, or something that holds, stores or repairs them?'
d['key']=['1. Is it a strap, bracelet, chain, winder, box or replacement part for a watch or clock? → Straps, storage & parts',
 '2. Is it worn on the wrist to tell the time? → Wristwatches',
 '3. Is it carried in a pocket or on a chain? → Pocket watches',
 '4. Does it time an interval, or tell the time from sun or sand (stopwatch, visual timer, hourglass, sundial)? → Timers & timing instruments',
 '5. Is it a clock collected for age, maker, form or design (longcase, carriage, cuckoo, marine chronometer, flip clock)? → Collectible clocks',
 '6. Is it a clock bought to use (alarm, wall, desk, travel)? → Everyday clocks',
 '<i>Precedence: a smartwatch is D2, a clock radio D3, a kitchen timer B5 and a chess clock E1; a strap or part is placed before the watch it fits.</i>']
# check no kind lost
placed={k['n'] for dp in depts for s in dp['s'] for k in s['k']}
orig=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/STR_A5/bak/A5.json'))
on={k['n'] for dp in orig['depts'] for s in dp['s'] for k in s['k']}
print('missing',on-placed-{'Split-flap clock'}, 'new',placed-on)
out='/home/user/Possession-Taxonomy/rebuild/out/A5.json'
json.dump(d,open(out+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(out+'.tmp',out)
