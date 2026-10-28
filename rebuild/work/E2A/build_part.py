import json,copy
R='/home/user/Possession-Taxonomy/rebuild/'
W='https://en.wikipedia.org/wiki/'
d=json.load(open(R+'out/E2.json'))
IDX=[0,1,2,3,4,5,12,13]
depts=copy.deepcopy([d['depts'][i] for i in IDX])
D={x['n']:x for x in depts}
def find(kn):
    for dp in depts:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==kn: return k
    raise KeyError(kn)
def A(n,d_,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',y='',d_=''): return {"n":n,"mk":mk,"y":y,"d":d_}
def add(kn,*arch,front=False):
    k=find(kn); x=k.setdefault('x',[])
    have={a['n'].lower() for a in x}
    for a in arch:
        assert a['n'].lower() not in have,a['n']
        if front: x.insert(0,a)
        else: x.append(a)
# ---- Fitness
add('Rowing machine',A('Concept2 Model D','Air-and-flywheel indoor rower from the Concept2 line that began with Model A; the standard home and club rower.','Concept2','2003',W+'Concept2',
 [V('Model A','Concept2','1981','original design'),V('Model B','Concept2','1986'),V('Model C','Concept2','1993'),V('Model E','Concept2','2006','sold alongside Model D'),V('Dynamic','Concept2','2010','sliding-ergometer variant')],'monitor PM5 (from 2014) · standard or tall legs · black or grey',a='Concept2 RowErg'),front=True)
add('Ski ergometer',A('Concept2 SkiErg','Wall- or stand-mounted ergometer simulating a double-pole ski stroke, from the makers of the Concept2 rower.','Concept2','2009',W+'Concept2',[],'wall mount or floor stand · PM5 monitor'),front=True)
add('Spin bike',A('Peloton Bike','Connected stationary bike with a built-in screen and subscription classes; first sold through Kickstarter in 2013.','Peloton','2014',W+'Peloton_Interactive',[V('Bike+','Peloton','2020','later model')],'screen size · resistance knob · subscription'),front=True)
add('Treadmill',A('Peloton Tread','Connected treadmill sold with subscription classes; the Tread+ was unveiled in 2018, the lower-priced Tread in 2020.','Peloton','2018',W+'Peloton_Interactive',[V('Tread+','Peloton','2018','originally "the Tread"'),V('Tread','Peloton','2020','lower-priced model')],'belt or slat deck · screen · subscription'))
add('Air bike',A('Rogue Echo Bike','Fan-braked exercise bike with moving arms, sold by Rogue Fitness for strength and conditioning training.','Rogue Fitness','',W+'Rogue_Fitness',[],'fan resistance · steel frame · monitor'))
add('Home multi-gym',A('Bowflex home gym','Cable-and-rod resistance home gym; the first BowFlex product was the 2000X.','Bowflex','1986',W+'Bowflex',
 [V('BowFlex 2000X','Bowflex','1986','first BowFlex product'),V('Power Pro','Bowflex','','recalled 2004'),V('Ultimate 2','Bowflex','','recalled 2006, 2007, 2009')],'resistance rods · cable pulleys · attachments'),front=True)
# ---- Cycling
add('Cycling helmet',A('Bell Biker','First commercially successful purpose-designed bicycle helmet, with a polystyrene liner and hard shell.','Bell','1975',W+'Bicycle_helmet',[V('Bell V1-Pro','Bell','1983','first polystyrene helmet for racing')],'hard shell · polystyrene liner'),front=True)
add('Cycling computer',A('Garmin Edge','Garmin\'s first GPS-enabled cycling computer; the Edge line followed from 2006.','Garmin','2006',W+'Garmin',[],'GPS · mapping · sensor pairing'),front=True)
# ---- Racket
add('Squash ball',A('Dunlop Pro','Double-yellow-dot squash ball, the competition standard since 2000; slower and lower-bouncing than other dot colours.','Dunlop','',W+'Squash_(sport)',
 [V('Competition','Dunlop','','single yellow dot'),V('Progress','Dunlop','','red dot'),V('Intro','Dunlop','','blue dot')],'dot colour: orange, double yellow, yellow, green, red, blue'),front=True)
add('Pickleball paddle',A('Plywood pickleball paddle','Early solid-wood paddle that replaced table-tennis bats in 1965 and was sold in kits from 1968.','','1965',W+'Pickleball',[V('McCallum M2','','','Seattle paddle favoured by early players')],'plywood · smooth non-compressible face'),front=True)
# ---- Golf
add('Putter',A('PING 1A','Karsten Solheim\'s first putter, made in his garage with the shaft attached at the centre rather than the heel.','Ping (Karsten Manufacturing)','1959',W+'Ping_(golf)',[],'blade · centre shaft'),
 A('Odyssey White Hot','Putter line with a white insert face, launched after Callaway bought Odyssey in 1997.','Odyssey Golf','2000',W+'Odyssey_Golf',[V('White Hot 2-Ball mallet','Odyssey Golf','2002','public release')],'insert face · blade or mallet'))
add('Golf driver',A('Pinseeker Bombshell','First stainless-steel metalwood driver; discontinued after about three years.','Pinseeker Golf Corp.','1976',W+'Wood_(golf)',[],'stainless steel head'),front=True)
add('Golf wedge',A('Sarazen sand wedge','Wedge with lead added to the sole and the sole set about 10 degrees from level, prototyped by Gene Sarazen.','','1931',W+'Wedge_(golf)',[],'bounce angle · steel head'),front=True)
add('Golf iron set',A('PING K1 irons','Cast stainless-steel irons, described as Ping\'s last major innovation of the 1960s.','Ping (Karsten Manufacturing)','1960s',W+'Ping_(golf)',[V('"69" irons','Ping (Karsten Manufacturing)','1961','first Ping iron set')],'cast stainless steel'),
 A('Mizuno JPX','Mizuno cavity-back and forged iron line, sold in Hot Metal, Forged and Tour versions in the JPX925 generation.','Mizuno','',W+'Mizuno_Corporation',[V('JPX925 Hot Metal','Mizuno'),V('JPX925 Forged','Mizuno'),V('JPX925 Tour','Mizuno')],'cavity back · forged or cast'))
# ---- Target
add('Archery target',A('122 cm target face','Ten-ring World Archery face used at 70 m and 90 m; rings run white, black, blue, red, gold from the outside in.','','',W+'Target_archery',[],'122 cm · five colours in ten scoring rings'),
 A('80 cm target face','World Archery face used at 30 m and 50 m; an inner-six-ring spot variant is used indoors.','','',W+'Target_archery',[],'80 cm · full or six-ring spot'),
 A('3-spot target face','Three copies of the inner five rings of a 40 or 60 cm face, so archers do not damage their own arrows.','','',W+'Target_archery',[],'40 or 60 cm · vertical line or triangle'))
add('Dartboard',A('Manchester Log End board','Smaller dartboard with no triple ring, only doubles and bullseye; a 25 cm playing area.','','',W+'Dartboard',[],'doubles and bullseye only'),
 A('London Fives board','East End board with 12 equal segments, played from 505.','','',W+'Dartboard',[],'12 segments'))
# ---- Team
add('Goalie mask',A('Plante fibreglass mask','Contoured fibreglass face mask first worn by Jacques Plante in an NHL game on 1 November 1959.','','1959',W+'Goaltender_mask',[V('Fibrosport mask','','1970s','1970 Jacques Plante Elite FibroSport model 103')],'fibreglass shell'),
 A('Helmet and cage combination','Helmet fitted with a wire cage, popularised in the 1970s by Vladislav Tretiak.','','1970s',W+'Goaltender_mask',[V('Cooper HM30 / HM40','Cooper','','cage designs by Brian Heaton')],'helmet · cage'),
 A('Hybrid fibreglass-and-cage mask','Fibreglass mask combined with a cage, developed by Dave Dryden and Greg Harrison and adopted in the early 1980s.','','late 1970s',W+'Goaltender_mask',[],'fibreglass back · cage front'))
add('Sliotar',A('Cork-core leather sliotar','Cork core under a two-piece white-tanned leather cover; the modern design is credited to Johnny McAuliffe.','','',W+'Sliotar',[V('Yellow sliotar','','2020','standard for minor level and above from 2024'),V('Smart sliotar','','2022','NFC chip; mandated for inter-county play from 2023')],'69–72 mm · 110–120 g · size 4 or 5'),front=True)
add('Hurley',A('Ash hurley','Stick cut from the base of an ash tree near the root, with a flat curved bas; the traditional form.','','',W+'Hurley_(stick)',[V('Bamboo hurley','Torpey','2020','introduced because of ash dieback'),V('Plastic hurley','Wavin','1970s','phased out over injuries')],'45–96 cm · steel band · bas width up to 13 cm'),front=True)
add('Lacrosse stick',A('Wooden lacrosse stick','Netted wooden stick descended from Native American stickball sticks; made in volume by Chisholm until the 1968 fire.','','',W+'Lacrosse_stick',[],'U-shaped wooden head · gut or mesh pocket'),
 A('Brine Shotgun','Early pinched-head plastic lacrosse head from Brine, following the Magnum.','Brine','',W+'Lacrosse_stick',[V('Magnum','Brine','1981'),V('Shotgun II','Brine')],'plastic head · pinched'))
add('Ice hockey stick',A('One-piece composite stick','Single moulded carbon-fibre stick first made and sold by Composite Busch SA of Switzerland.','','1992',W+'Ice_hockey_stick',[],'carbon fibre · flex rating'),front=True)
add('Cricket bat',A('ComBat aluminium bat','Aluminium bat briefly used by Dennis Lillee; the laws were then amended so a blade must be wholly wood.','','1979',W+'Cricket_bat',[],'aluminium'),
 A('Mongoose MMi','Twenty20 bat with a blade about a third shorter and a handle about 43 per cent longer.','Mongoose','2009',W+'Cricket_bat',[V('MMi3','Mongoose','2009')],'short blade · long handle'))
# new kind: field hockey ball
fb={"n":"Field hockey ball","a":"hockey ball","d":"Hard dimpled or smooth ball for field hockey; plastic cover, sometimes in different colours.","t":["dimpled","smooth","astroturf","indoor"],"s":W+'Kookaburra_Sport',
 "x":[A('Kookaburra Dimple Elite','Dimpled hockey ball that became the international standard after its introduction at the 1984 World Cup and Olympics.','Kookaburra','1984',W+'Kookaburra_Sport',[],'dimpled · white or coloured')]}
# ---- Combat
add('Fencing sabre',A('FIE sabre blade','Straight 88 cm blade based on the Italian duelling sabre; target is waist up, excluding the hands.','','',W+'Sabre',[],'88 cm · steel'))
add('Fencing epee',A('FIE épée blade','Triangular 90 cm blade, 24 mm per side; a touch registers at 750 gf on the tip.','','',W+'Épée',[],'size 5 90 cm · triangular section'),front=True)
add('Kendo armour',A('Bōgu set','Four-part kendo armour: men helmet, kote gauntlets, dō breastplate and tare waist guard.','','',W+'Bōgu',[],'dō in lacquered bamboo, paper fibre or moulded plastic'))
# ---- Reorganise Team sports
T=D['Team sports']
allk={k['n']:k for s in T['s'] for k in s['k']}
allk['Field hockey ball']=fb
layout=[
 ('Balls & pucks',['Football','Rugby ball','American football','Basketball','Volleyball','Netball','Handball','Sliotar','Cricket ball','Field hockey ball','Hockey puck']),
 ('Bats, sticks & gloves',['Cricket bat','Baseball bat','Softball bat','Ice hockey stick','Goalie stick','Field hockey stick','Bandy stick','Lacrosse stick','Hurley','Baseball glove','Goalkeeper gloves','Wicket-keeping gloves','Cricket batting gloves']),
 ('Boots, goals & fixtures',['Football boot','Kicking tee','Football goal','Basketball hoop','Hockey goal','Hockey shooting pad','Cricket stumps']),
 ('Helmets & head protection',['American football helmet','Batting helmet','Cricket helmet','Hockey helmet','Hockey cage or visor','Goalie mask','Riding hat','Mouthguard']),
 ('Body protection',['American football shoulder pads','Hockey gloves','Hockey shoulder pads','Hockey elbow pads','Hockey pants','Hockey neck guard','Cricket batting pads','Catcher\'s gear','Equestrian body protector','Shin guard','Knee pad','Protective cup']),
 ('Goalie protection',['Goalie leg pads','Goalie blocker','Goalie catcher','Goalie chest and arm protector','Goalie pants']),
]
used=set(); new=[]
for n,ks in layout:
    new.append({"n":n,"k":[allk[k] for k in ks]}); used|=set(ks)
missing=set(allk)-used
assert not missing,missing
T['s']=new
T['note']='Balls, sticks and protective kit for team sports, grouped by object; club-owned fixtures stay kind-level.'
json.dump({"depts":depts},open(R+'out/E2A_part.json.tmp','w'),indent=1,ensure_ascii=False)
json.dump({"c":"E2","rev":True,"lead":"x","b":[],"depts":depts},open(R+'work/E2A/check.json','w'),ensure_ascii=False)
