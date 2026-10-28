import json, os
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/E1X/'
d=json.load(open(W+'bak/E1.json'))
br=json.load(open(W+'bak/E1_brands.json'))
WP='https://en.wikipedia.org/wiki/'
def A(n,dd,mk='',y='',s='',v=None,dt=None,a=''):
    o={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: o['dt']=dt
    return o
def V(n,mk='',y='',dd=''): return {'n':n,'mk':mk,'y':y,'d':dd}
def K(n,dd,s,x=None,a='',t=None,m=None):
    o={'n':n,'a':a,'d':dd}
    if t: o['t']=t
    o['s']=s
    if x: o['x']=x
    if m: o['m']=m
    return o
def dept(p): return [x for x in d['depts'] if x['n'].startswith(p)][0]
def shelf(dp,p): return [x for x in dp['s'] if x['n'].startswith(p)][0]
def kind(sh,n): return [k for k in sh['k'] if k['n']==n][0]
before_k=sum(len(s['k']) for dp in d['depts'] for s in dp['s'])
before_x=sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])

# ---------- Creative & activity toys (Building & construction)
bc=dept('Building')
creative={'n':'Creative & activity toys','k':[
 K('Modelling dough','Soft non-hardening compound sold in tubs for hand-shaping, often with extruders and moulds.',WP+'Play-Doh',
   [A('Play-Doh','Modelling compound from a 1930s wallpaper-cleaning putty, sold to schools and shops from 1955–56.','Hasbro','1955',WP+'Play-Doh',
      [V('Fun Factory','Hasbro','1960','extruder toy'),V('Fuzzy Pumper Barber & Beauty Shop','Hasbro','1977','playset'),
       V('Mop Top Hair Shop','Hasbro','1986','playset'),V('Creativity Center','Hasbro','2007',''),V('Play-Doh Plus','Hasbro','2013','softer compound')],
      dt='tub or can · colours · playset with moulds',a='Play-Dough')],
   t=['Tub or can','Playset with tools','Extruder']),
 K('Drawing toy','A mechanical or magnetic device for making line drawings without pens, from gears or knobs.',WP+'Spirograph',
   [A('Spirograph','Geared drawing set that traces looping curves; sold from 1965 after Denys Fisher showed it at Nuremberg.','Denys Fisher','1965',WP+'Spirograph',
      [V('Kenner US launch','Kenner','1966',''),V('Super-Spirograph','Kenner','','adds triangles, straight bars and more rings'),
       V('Spirotot','Kenner','','junior version'),V('Magnetic Spirograph','Kenner','',''),V('Kahootz relaunch','','2013','removable putty replaces pins')],
      dt='gear rings and wheels · pins or putty · pens'),
    A('Etch A Sketch','Two-knob drawing screen that makes a continuous line in aluminium powder; designed by André Cassagnes as L\'Écran Magique.','Ohio Art Company','1960',WP+'Etch_A_Sketch',
      [V('Ohio Art US launch','Ohio Art Company','1960','12 July 1960'),V('Etch A Sketch Animator','Ohio Art Company','1986','40×30 dot-matrix display'),
       V('Animator 2000','Ohio Art Company','1987','60×40 LCD, cartridges'),V('Etch A Sketch Color','Ohio Art Company','1993','coloured markers on paper'),
       V('Spin Master ownership','Spin Master','2016','rights acquired February 2016')],
      dt='screen size · knob colour · frame colour')],
   t=['Gear-ring set','Magnetic screen','Refill pens']),
 K('Light-peg toy','A lit panel with coloured translucent pegs pushed through a template to make glowing pictures.',WP+'Lite-Brite',
   [A('Lite-Brite','Light-box pegboard invented at Marvin Glass and Associates and licensed to Hasbro in 1967.','Hasbro','1967',WP+'Lite-Brite',
      [V('Flat screen','Hasbro','','plug-in lamp'),V('Four-Share cube','Hasbro','','3D cube lit on four sides'),
       V('FX Edition','Hasbro','','spins and plays music'),V('LED flat screen','Hasbro','','three AA batteries')],
      dt='peg colours · template sheets · screen shape')],
   t=['Flat screen','3D cube']),
 K('Fuse beads','Small tubes threaded on pegboards, then fused by iron, or by water spray, into flat shapes.',WP+'Fuse_beads',
   [A('Hama beads','Fusible pegboard beads made from 1971 and fusible from the late 1970s; sold as mini, midi and maxi.','Hama','1971',WP+'Fuse_beads',
      [V('Mini','Hama','','2 mm'),V('Midi','Hama','','5 mm'),V('Maxi','Hama','','10 mm')],dt='bead size 2, 5 or 10 mm · pegboard shape · colours',a='Hamabeads'),
    A('Perler beads','Californian fuse beads founded by Peter and Dee Dee Schneck.','Perler','1981',WP+'Fuse_beads',
      [V('Mini','Perler','','2.6 mm'),V('Classic','Perler','','5 mm'),V('Biggie','Perler','','10 mm')],dt='bead size · pegboard · colours'),
    A('Pyssla','IKEA fuse beads sold in one 5 mm size.','IKEA','',WP+'Fuse_beads'),
    A('Aquabeads','Spherical beads that bond when sprayed with water instead of ironed.','Spin Master','',WP+'Aquabeads',
      [V('2007 recall','Spin Master','2007','November 2007 recall of one batch')],dt='bead colours · spray bottle · template trays'),
    A('Knutsson pegboard','Pegboard-and-bead pattern invented by Gunnar Knutsson in Vällingby, Sweden, as therapy; patented 1962, granted 1967.','','early 1960s',WP+'Fuse_beads')],
   t=['5 mm bead size','2 mm mini','10 mm maxi','Heat-fused','Water-fused','Pegboard','Pattern sheets']),
 K('Shrink plastic','Printed or blank plastic sheets that shrink and thicken in an oven to make keyrings and charms.',WP+'Shrinky_Dinks',
   [A('Shrinky Dinks','Oven-shrinking plastic sheets invented in 1973 by Betty Morris and Kate Bloomberg in Brookfield, Wisconsin.','Shrinky Dinks','1973',WP+'Shrinky_Dinks',
      [V('Shrinkles','','','alternative brand name'),V('Pre-printed character kit','','','outline images to colour'),V('Blank sheets','','','bulk sheets for adult crafters')],
      dt='sheet size · printed or blank · frosted or clear')],
   t=['Pre-printed kit','Blank sheets']),
 K('Slime & putty toy','A gooey, stretchy non-setting toy compound sold in pots or novelty containers.',WP+'Slime_(toy)',
   [A('Mattel Slime','Green guar-gum slime sold in a plastic bin from February 1976.','Mattel','1976',WP+'Slime_(toy)',
      [V('Slime with rubber insects, eyeballs and worms','Mattel','1970s',''),V('Slime Monster board game','Mattel','late 1970s','')]),
    A('Ecto-Plazm','Play gel sold with selected Real Ghostbusters figures.','Kenner','1980s',WP+'Slime_(toy)'),
    A('Retro-mutagen ooze','Slime sold in containers and with Teenage Mutant Ninja Turtles playsets.','Playmates Toys','1980s',WP+'Slime_(toy)'),
    A('Flubber-type slime','Rubbery slime from polyvinyl alcohol rather than plant gum.','','',WP+'Slime_(toy)')],
   t=['Pot','Novelty container','Kit'])]}
bc['s'].insert(2,creative)

# ---------- Skill toys: kite, marbles; circus shelf
sk=dept('Skill, music')
st=shelf(sk,'Skill toys')
kite=kind(st,'Toy kite')
kp=WP+'Kite_types'
kite['x']+= [
 A('Box kite','Single-line kite with a box-shaped cell frame.','','',kp),
 A('Sled kite','Frameless-spar single-line kite; the earliest example named in the kite-type list is the 1904 Buda Jewish kite.','','1904',kp),
 A('Parafoil kite','Spar-less ram-air kite based on the wing invented by Domina Jalbert.','','',kp),
 A('Malay kite','Pre-Eddy bowed kite; the Kirby and Woglum kites are variants.','','',kp,[V('Eddy kite','','','named for William A. Eddy; US patent 646375')]),
 A('Rokkaku kite','Bowed hexagonal kite.','','',kp),
 A('Fighter kite','Light single-line kite that can move fast under control.','','',kp)]
marb=K('Marble','A small glass, clay, steel or agate sphere, about 0.5–3.5 cm across, played with or collected.',WP+'Marbles',
 [A('German handmade glass marble','Antique hand-drawn glass marbles with swirled bodies, sold across Europe.','','',WP+'Marbles',
    [V('Sulphide','','','contains a small figure'),V('Lutz','','',''),V('Onionskin','','','')],dt='swirl pattern · size · condition'),
  A('Clay and china marble','Cheap unglazed clay (commie or crock) and painted china marbles, mass-produced after the 1870s.','','1870s',WP+'Marbles'),
  A('Christensen machine-made marble','First machine-made glass marbles, made by M.F. Christensen in Akron, Ohio.','M.F. Christensen','1903',WP+'Marbles'),
  A('Akro Agate marble','Marbles from Akron, moved to Clarksburg, West Virginia, in 1914; production ceased in 1951.','Akro Agate Company','1911',
    'https://wvencyclopedia.org/entries/161',[V('Corkscrew','Akro Agate Company','','spiral marble collectors credit to Akro')],
    dt='colour combination · size · condition'),
  A('Vitro Agate marble','Machine-made American marbles produced from 1932 to 2004.','Vitro Agate','1932',WP+'Marbles'),
  A('Marble King marble','Paden City, West Virginia, maker, the only remaining American toy marble manufacturer.','Marble King','',WP+'Marbles'),
  A('Vacor marble','Mexican playing marbles; the world\'s largest maker, founded 1934.','Vacor de Mexico','1934',WP+'Marbles'),
  A('Steelie','Steel ball, traditionally folded from flat steel.','','',WP+'Marbles'),
  A('Contemporary art marble','Marble made singly by glass artists for collectors.','','',WP+'Marbles')],
 a='marbles',t=['Alley','Aggie (agate)','Cat\'s eye','Commie','China','Bumblebee','Galaxy','Swirly'])
# place after Toy ball
i=[k['n'] for k in st['k']].index('Toy ball')
st['k'].insert(i+1,marb)

jp=WP+'Juggling_prop'
circus={'n':'Circus & juggling props','k':[
 K('Juggling ball','A ball made to be thrown and caught in patterns.',WP+'Juggling_ball',
   [A('Beanbag juggling ball','Soft filled ball, about 2.5–3 in and 90–130 g, that neither bounces nor rolls.','','',WP+'Juggling_ball',dt='shell vinyl or microfibre · filling millet, birdseed or pellets'),
    A('Stage ball','Hollow ball with a hard polished shell, 2.5–4 in; rolls when dropped.','','',WP+'Juggling_ball'),
    A('Bouncing ball','Silicone or rubber ball with 75–90% bounce return.','','',WP+'Juggling_ball'),
    A('DX ball','Hard PVC shell part-filled with millet so it flies true and stays put.','','',WP+'Juggling_ball'),
    A('Russian ball','Thin shell mostly filled with sand or salt, giving a low centre of mass.','','',WP+'Juggling_ball')],
   t=['Contact ball']),
 K('Juggling club','A pin-shaped prop balanced for throwing and spinning, usually 19–21 inches.',WP+'Juggling_club',
   [A('American-style wooden club','Large hollowed wooden club with a solid handle, made by Edward Van Wyck and Harry Lind.','','early 20th century',WP+'Juggling_club'),
    A('European club','Solid cork body on a wooden handle, or thin solid wood.','','',WP+'Juggling_club'),
    A('One-piece plastic club','Single moulded hollow piece; durable and cheap with a rigid handle.','','',WP+'Juggling_club'),
    A('Multi-piece composite club','Core, moulded body, flexible wrapped handle and foam ends; pioneered by Jay Green and refined by Brian Dube.','','1960s',WP+'Juggling_club',
      [V('Dube refinement','','1975','')],dt='thin European or larger American style · decoration')],
   t=['Fire club']),
 K('Juggling ring','A flat ring thrown and caught in patterns.',jp,t=['Standard ring']),
 K('Devil stick','A baton kept in the air with two handsticks.',WP+'Devil_stick',
   [A('Tapered devil stick','Traditional baton, thinner in the middle.','','',WP+'Devil_stick',dt='wood, plastic, aluminium, fibreglass or carbon fibre · elastomer grip'),
    A('Flower stick','Straight baton with tasselled or padded ends; the extra drag slows it for beginners.','','',WP+'Devil_stick')],
   t=['Fire','Illuminated (LED)','Weighted-end baton'],a='devilstick · juggling stick'),
 K('Diabolo','A two-cupped spool spun on a string tied between two handsticks.',WP+'Diabolo',
   [A('Chinese yo-yo','Bamboo air-bell spool, the diabolo\'s ancestor, first recorded in the late Ming dynasty.','','',WP+'Diabolo'),
    A('Philippart rubber diabolo','Modern diabolo developed by Belgian engineer Gustave Philippart; rubber version patented 1905.','Gustave Philippart','1905',WP+'Diabolo'),
    A('Parker Brothers diabolo','Steel-axle moulded-rubber and hollow celluloid diabolos; US licence acquired 1906.','Parker Brothers','1906',WP+'Diabolo'),
    A('Monobolo','Single-cup variant weighted on the other side.','','',WP+'Diabolo')],
   t=['Fixed axle','Bearing axle','Wood','Rubber','Rubberised plastic','Metal (fire)']),
 K('Poi','A weight on a cord swung in circles; originally Māori flax or bulrush.',WP+'Poi_(performance_art)',
   [A('Māori raupō or flax poi','Traditional poi woven from harakeke or raupō around a core, with a cord; short or long.','','',WP+'Poi_(performance_art)',
      [V('Tāniko poi','','','woven patterned')]),
    A('Sock poi','Practice poi from weighted socks.','','',WP+'Poi_(performance_art)'),
    A('Rope-and-ball poi','Practice poi from tennis balls and cord, with swivels or handles added.','','',WP+'Poi_(performance_art)')],
   t=['Short','Long','Glow or LED','Fire (Kevlar or Technora wicks)','Contact ball'])]}
sk['s'].insert(1,circus)

# ---------- Magic set
ms=kind(shelf(sk,'Music'),'Magic set')
ms['x'][0]['v'].insert(0,V('Mysto Magic sets','Mysto Manufacturing Company','1910s–1950s','interlocking rings, playing cards, wand'))
ms['x'].append(A('Executive magic set','Adult-oriented set with higher-quality materials and more complex tricks.','','',WP+'Magic_kit'))

# ---------- Model rocketry & rolling stock
mk=dept('Models')
rocket={'n':'Model rocketry','k':[
 K('Model rocket kit','A kit for a small rocket flown on a commercial motor and recovered for reuse.',WP+'Model_rocket',
   [A('Carlisle model rocket','First modern model rocket and motor, designed by Orville and Robert Carlisle.','','1954',WP+'Model_rocket',
      [V('Model Missiles Incorporated','','','first American model rocket company, co-founded by G. Harry Stine')]),
    A('Estes Astron Scout','Estes Industries\' first kit (K-1); Estes was founded 1958 in Denver by Vernon Estes.','Estes Industries','',WP+'Estes_Industries'),
    A('Estes Astron X-Ray','Kit with a see-through plastic payload compartment.','Estes Industries','',WP+'Estes_Industries'),
    A('Estes Alpha','Estes entry-level kit, pictured in a 1969 company photo.','Estes Industries','',WP+'Estes_Industries'),
    A('Estes Saturn V','Semi-scale Saturn V; Estes later offered models as complex as it.','Estes Industries','',WP+'Estes_Industries'),
    A('Estes Cineroc and Camroc','Movie-camera and small camera rockets.','Estes Industries','',WP+'Estes_Industries'),
    A('Estes Space Shuttle','Replica Space Shuttle kit.','Estes Industries','1981',WP+'Estes_Industries')],
   t=['Semi-scale','Camera rocket','Glide recovery','Micro (6 mm motor)']),
 K('Model rocket motor','A single-use solid-fuel engine rated by total-impulse class and delay time.',WP+'Model_rocket',
   t=['Black powder (up to F)','Composite (A to O)','1/4A to G (model rocket)','Micro 6 mm','10.5 mm micro (discontinued 2001)'],
   a='rocket engine'),
 K('Model rocket launch set','Launch pad and electrical controller for igniting model rocket motors.',WP+'Model_rocket',t=['Pad and controller set'])]}
mk['s'].insert(1,rocket)

rs=kind(shelf(mk,'Model railways'),'Model rolling stock')
rs['s']=rs.get('s') or WP+'Rolling_stock'
rs['x']=[
 A('Lionel Standard Gauge','Wide three-rail trains sold by Lionel as "The Standard of the World".','Lionel','1906–1939',WP+'Lionel_Corporation'),
 A('Märklin H0','Märklin H0 system: AC studded-track trains from the 1935 H0 scale.','Märklin','1935',WP+'M%C3%A4rklin'),
 A('Hornby Dublo','OO trains with tinplate coaches and wagons.','Hornby','1938–1963',WP+'Hornby_Railways',
   [V('Super Detail plastic rolling stock','Hornby','1959','two-rail track')]),
 A('Tri-ang Hornby','Tri-ang\'s cheaper plastic OO range, replacing Hornby Dublo after Lines Bros\' purchase.','Lines Bros','1964–1972',WP+'Hornby_Railways',
   [V('Dublo tooling sold on','','','went to G & R Wrenn')]),
 A('Märklin Mini-Club','Märklin\'s Z scale range.','Märklin','1972',WP+'M%C3%A4rklin'),
 A('Hornby Railways','Adult-hobbyist upgraded OO range after 1972.','Hornby','1972',WP+'Hornby_Railways'),
 A('Lionel Standard O','Scale-sized O freight cars.','Lionel','1973',WP+'Lionel_Corporation',
   [V('MPC rolling stock','Lionel','1970','fast-angle wheels, needlepoint bearings, Delrin trucks')]),
 A('Bachmann Branchline','British-outline OO range from moulds taken over from Mainline Railways and Replica.','Bachmann','1990',WP+'Bachmann_Branchline')]

# ---------- Traditional sets & dolls' house miniatures
tg=dept('Board')
trad=shelf(tg,'Traditional')
xq=kind(trad,'Xiangqi set'); xp=WP+'Xiangqi'
xq['x']=[
 A('Traditional-character xiangqi set','Sixteen flat discs a side lettered in traditional characters, red against black; most common.','','',xp),
 A('Simplified-character xiangqi set','Same layout with simplified characters, for example the horse as 马.','','',xp),
 A('Same-character xiangqi set','Both sides share one character per piece type, such as 炮.','','',xp),
 A('Different-character xiangqi set','Sides use different characters for the same piece, such as 砲 and 炮.','','',xp)]
dr=kind(trad,'Draughts set'); dp_=WP+'Draughts'
dr['x']=[
 A('International draughts set','10×10 board with 50 playing squares and 20 pieces a side.','','',dp_),
 A('English draughts set','8×8 board and 12 pieces a side; American checkers.','','',dp_,a='American checkers'),
 A('Russian draughts set','8×8 board and 12 pieces a side.','','',dp_),
 A('Brazilian draughts set','8×8 board and 12 pieces a side.','','',dp_),
 A('Canadian checkers set','12×12 board and 30 pieces a side; also played in Malaysia and Singapore.','','',dp_)]
dm=kind(trad,'Domino set'); dd_=WP+'Dominoes'
dm['s']=dm.get('s') or dd_
dm['x']=[
 A('Double-six domino set','Traditional European set of 28 tiles.','','',dd_),
 A('Double-nine domino set','55 tiles; common commercial set.','','',dd_),
 A('Double-twelve domino set','91 tiles.','','',dd_),
 A('Double-fifteen domino set','136 tiles.','','',dd_),
 A('Double-eighteen domino set','190 tiles, the practical maximum.','','',dd_),
 A('Chinese domino set','32 tiles from the 21 throws of two dice, no blanks, longer tiles.','','',dd_)]
dh=dept('Dolls')
mn=kind(shelf(dh,"Dolls' houses"),"Dolls' house miniatures")
mn['s']=mn.get('s') or WP+'Dollhouse'
dhp=WP+'Dollhouse'
mn['x']=[
 A('1:12 miniatures','One inch to the foot; the adult collectors\' scale.','','',dhp),
 A('1:24 miniatures','Half scale, popular with US collectors.','','',dhp),
 A('1:48 miniatures','Quarter-size scale, popular with US collectors.','','',dhp),
 A('1:18 play-scale miniatures','Two-thirds of an inch to the foot; the usual children\'s dolls\' house scale.','','',dhp),
 A('TynieToy','Rhode Island replicas of American antique houses and furniture in uniform scale from about 1917.','TynieToy','1917',dhp),
 A('Lundby furniture','Swedish 1:18 dolls\' house furniture, made of wood.','Lundby','',dhp)]

# ---------- brands
have={b['n'].lower() for b in br['b']}
idx={x[0].lower() for x in json.load(open(R+'reader/_brand_index.json'))['b']}
def B(n,c,seg,kf,dd,s,f=None,sig=None):
    o={'n':n,'c':c,'seg':seg,'kf':kf,'d':dd,'s':s}
    if f: o['f']=f
    if sig: o['sig']=sig
    return o
new=[
 B('Denys Fisher','United Kingdom','Heritage manufactory','Spirograph','British toy company of engineer Denys Fisher, maker of the first Spirograph.',WP+'Spirograph',sig=['Spirograph']),
 B('Ohio Art Company','United States','Heritage manufactory','Etch A Sketch','Ohio toy maker that sold Etch A Sketch from 1960 to 2016.',WP+'Etch_A_Sketch',sig=['Etch A Sketch']),
 B('Perler','United States','Specialist','fuse beads','Californian fuse-bead maker founded by Peter and Dee Dee Schneck.',WP+'Fuse_beads','1981'),
 B('Hama','','Specialist','fuse beads','Maker of Hama pegboard beads, produced from 1971.',WP+'Fuse_beads','1971'),
 B('IKEA','Sweden','Own-label & retailer','Pyssla beads','Furniture retailer whose Pyssla range is a fuse-bead set.',WP+'Fuse_beads'),
 B('Shrinky Dinks','United States','Specialist','shrink plastic','Oven-shrinking plastic craft brand invented in 1973.',WP+'Shrinky_Dinks','1973'),
 B('Estes Industries','United States','Specialist','model rockets','Colorado model rocket company founded in 1958 by Vernon Estes.',WP+'Estes_Industries','1958',['Astron Scout','Alpha']),
 B('Akro Agate Company','United States','Heritage manufactory','glass marbles','Marble maker founded in Akron in 1911, in Clarksburg from 1914 to 1951.','https://wvencyclopedia.org/entries/161','1911',['Corkscrew']),
 B('M.F. Christensen','United States','Heritage manufactory','glass marbles','Akron maker of the first machine-made glass marbles in 1903.',WP+'Marbles'),
 B('Vitro Agate','United States','Heritage manufactory','glass marbles','American marble producer active from 1932 to 2004.',WP+'Marbles','1932'),
 B('Marble King','United States','Specialist','toy marbles','Paden City, West Virginia, the last American toy marble maker.',WP+'Marbles'),
 B('Vacor de Mexico','Mexico','Mainstream','playing marbles','Founded in 1934, the world\'s largest maker of playing marbles.',WP+'Marbles','1934'),
 B('Parker Brothers','United States','Heritage manufactory','games, diabolos','US games maker; Charles Parker took the US diabolo licence in 1906.',WP+'Diabolo'),
 B('Gustave Philippart','Belgium','Artisan & independent','rubber diabolo','Belgian engineer who developed the modern diabolo and patented a rubber one in 1905.',WP+'Diabolo'),
 B('TynieToy','United States','Heritage manufactory','miniature furniture','Providence, Rhode Island maker of antique-house replicas and furniture from about 1917.',WP+'Dollhouse','1917')]
added=[]
for b in new:
    if b['n'].lower() in have: continue
    br['b'].append(b); added.append(b['n'])

# ---------- checks: every mk in archetypes/versions registered
reg={b['n'] for b in br['b']}
miss=set()
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for x in k.get('x',[]):
                for o in [x]+x.get('v',[]):
                    if o.get('mk') and o['mk'] not in reg: miss.add(o['mk'])
print('unregistered mk:',sorted(miss) if len(miss)<40 else len(miss))
print('added brands',added)
after_k=sum(len(s['k']) for dp in d['depts'] for s in dp['s'])
after_x=sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])
print('kinds',before_k,'->',after_k,'archetypes',before_x,'->',after_x)
for n,o in (('E1.json',d),('E1_brands.json',br)):
    json.dump(o,open(R+'out/'+n+'.tmp','w'),ensure_ascii=False)
    os.replace(R+'out/'+n+'.tmp',R+'out/'+n)
