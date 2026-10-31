import json,os
W="https://en.wikipedia.org/wiki/"
def A(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(zip(("n","mk","y","d"),x)) for x in v],"dt":dt}
carriage={"n":"Horse-drawn carriage","a":"carriage · driving vehicle","d":"Wheeled passenger vehicle drawn by one or more horses or ponies.",
 "t":["two-wheeled","four-wheeled","open","closed","original antique","modern reproduction","competition (marathon) vehicle"],
 "s":"https://www.ehorses.com/classified-ads/carriage-and-vehicles/carriages",
 "x":[
  A("Coach","drag · road coach · mail coach · state coach","Large enclosed four-wheeled carriage driven from a raised box seat, usually by two or more horses.","","18th–19th century","Coach_(carriage)",
    [("Mail coach","","1785","British public mail coach; London–Edinburgh service c. 1785"),("Road coach","","","Public coach later kept by private owners for pleasure and show"),("Drag (park drag)","","","Lighter private coach for sport and driving clubs"),("State coach","","","Ornate ceremonial coach; Diamond Jubilee State Coach built 2014")],
    "body (mail, road, drag, state) · team size · paint and livery"),
  A("Concord coach","Concord stagecoach","Egg-shaped stagecoach hung on leather thoroughbraces, the most popular coach in North America.","Abbot-Downing Company","1847–1899","Concord_coach",
    [("Overland (Western passenger) wagon","Abbot-Downing Company","","Simpler, lighter and cheaper companion vehicle"),("Concord Stagecoach","G&F Companies","","Modern reproduction (old data)")],
    "six, nine or twelve passengers · Eastern or Western finish · thoroughbrace suspension"),
  A("Hansom cab","hansom · safety cab","Two-wheeled hire carriage with the driver on a high seat behind the passenger compartment.","","1834","Hansom_cab",
    [("Hansom Safety Cab","","1834","Joseph Hansom's patent; tall wheels, driver on the roof front"),("Chapman hansom","","1836","John Chapman's redesign: driver at the rear, smaller wheels, dropped axle"),("Forder hansom","","","Upgraded cabs with brass fittings, rubber tyres and luxurious interiors"),("Parlour hansom","","1887","Four passengers facing each other"),("Court hansom","","","Four wheels, two seats")],
    "two or four wheels · tyres (iron, rubber, pneumatic from 1909)"),
  A("Brougham","brougham carriage","Light enclosed four-wheeled carriage for one horse, seating two, with a box seat for the coachman.","","1838","Brougham_(carriage)",
    [("Original brougham","","1838","Built by London coachbuilders Robinson & Cook for Lord Brougham"),("Brougham-landaulet","","","Collapsible top behind the doors"),("Clarence","","","Larger version of the brougham")],
    "one horse · elliptical springs · lamps and trim"),
  A("Landau","landau carriage","Large four-wheeled carriage with face-to-face seats and a two-part folding leather top.","","18th century","Landau_(carriage)",
    [("Landaulet (demi-landau)","","1771","Shorter two-passenger coupé version"),("Briska landau","","1830s","Introduced by Holborn coachbuilder Luke Hopkinson"),("Britzka landau","","1838","English variation with folding hood"),("Sefton (canoe) landau","","","French-style canoe-shaped body"),("State and Ascot landaus","","","Ceremonial landaus")],
    "body shape (canoe, square, round-cornered) · one, two or four horses"),
  A("Phaeton","phaeton carriage","Sporty open four-wheeled carriage with a lightly sprung body on large wheels, driven by its owner.","","18th century","Phaeton_(carriage)",
    [("Highflyer","","late 1700s","Very large rear wheels and a high, unstable body"),("Mail phaeton","","","Heavy box body on mail springs, groom's seat behind"),("George IV phaeton","","1824","Low pony phaeton built for King George IV"),("Spider phaeton","","1860s","American show vehicle with a Tilbury-type body"),("Pony phaeton","","","Small phaeton popular with women drivers")],
    "one or two horses · body height · wicker (basket) or panelled"),
  A("Gig","whirligig","Light two-wheeled open carriage for one horse with a single forward-facing seat.","","1791","Gig_(carriage)",
    [("Stanhope gig","","c. 1814","Designed by Fitzroy Stanhope; high seat, closed back"),("Tilbury","","","Seven-spring gig named after its builder Tilbury"),("Dennett gig","","early 1800s","Three springs"),("Whiskey","","","Light gig, often with cane work"),("Spider gig","","","Very high gig with curved dash")],
    "springing · seat back (stick-back, panelled) · wheel size"),
  A("Dogcart","dog cart","Two-wheeled cart with back-to-back seats and a box under the seat for gun dogs.","","early 1800s","Dogcart",
    [("Dogcart phaeton","","","Four-wheeled version")],"single horse or tandem · sliding body"),
  A("Governess cart","governess car · tub cart","Low two-wheeled tub-bodied pony cart entered from the rear, built for carrying children safely.","","1880–1900","Governess_cart",
    [("Princess car","","","Same body, entered from the front"),("Beverley car","","","Square sides")],"basketwork or wooden tub · wheel size for pony or horse"),
  A("Buggy","Amish buggy · road buggy","Light four-wheeled American carriage with one seat for two and a vertical leather dash.","","19th century","Buggy_(carriage)",
    [("Amish and Old Order Mennonite buggy","","","Still in daily use; top colour (black, grey, brown, yellow, white) marks the community"),("Auto-seat buggy","","","Curved seat in early motor-car style")],
    "open or enclosed · folding hood · top colour · lamps"),
  A("Surrey","fringe-top surrey","American four-wheeled family carriage with two forward-facing seats for four.","","1880s","Surrey_(carriage)",
    [("Fringed-canopy surrey","","1880s","Most popular top style from the 1880s")],"top (open, half-hood, umbrella, extension, canopy, fringed) · one or two horses"),
 ],
 "m":[["Cinderella Carriage","G&F Companies"],["Allgäu Wagonette","Kühnle"]]}
wagon={"n":"Horse-drawn wagon","a":"cart · farm wagon · covered wagon","d":"Wheeled goods vehicle drawn by horses or other draught animals.",
 "t":["two-wheeled cart","four-wheeled wagon","covered","open","original antique","reproduction"],
 "s":"https://www.ehorses.com/classified-ads/carriage-and-vehicles/carriages",
 "x":[
  A("Conestoga wagon","Conestoga","Heavy boat-shaped freight wagon under a canvas cover on hickory bows, pulled by four to six horses.","","1716","Conestoga_wagon",
    [("Prairie schooner","","19th century","Lighter, cheaper covered wagon used by westward pioneers")],"white-oak body · blue box, vermilion running gear · canvas cover"),
  A("Chuckwagon","camp wagon · round-up wagon","Covered wagon fitted as a mobile range kitchen with a chuck box at the back.","","1866","Chuckwagon",
    [("Goodnight chuckwagon","","1866","Charles Goodnight's conversion of an army-surplus Studebaker wagon")],"chuck box · water barrel · pan boot"),
 ],
 "m":[["Versatile Wagon","G&F Companies"]]}
vardo={"n":"Romani vardo","a":"vardo · Gypsy caravan · living wagon","d":"Horse-drawn living wagon of British Romani travellers, with stove, bed and carved, painted decoration.",
 "t":["original","restored","new-built"],"s":W+"Vardo_(Romani_wagon)",
 "x":[
  A("Reading wagon","kite wagon","Straight-sided wagon sloping out to the eaves on high wheels outside the body, porches at both ends.","Dunton and Sons","1870","Vardo_(Romani_wagon)",
    [("Skylight Reading wagon","","early 1900s","Raised skylight roof")],"red matchboard picked out in yellow and green · carved lion heads, gold leaf"),
  A("Ledge wagon","cottage wagon","Robust wagon whose living area extends over the large rear wheels on brackets, with a tall arched roof.","","","Vardo_(Romani_wagon)",[],"tongue-and-groove walls · carved scrollwork · porches"),
  A("Bow top","barrel top","Light wagon with low sides and a barrel-shaped canvas roof over wooden bows, drawn by one horse.","","","Vardo_(Romani_wagon)",
    [("Open lot","","","No front wall or doors; canvas folds back")],"green paint, teal cloth · scrollwork end boards"),
  A("Burton wagon","showman's wagon","Wagon with small wheels set under the body, the oldest British wagon home, used by showmen and Romani.","","","Vardo_(Romani_wagon)",[],"plain or elaborately decorated"),
  A("Brush wagon","fen wagon","Reading-type trade wagon with outside racks for brushes, brooms and baskets and a rear door.","","","Vardo_(Romani_wagon)",[],"roof rails · painted trade boards"),
 ]}
sleigh={"n":"Sleigh","a":"sledge · horse sleigh","d":"Horse-drawn vehicle on runners for carrying people or goods over snow or ice.",
 "t":["single-seat","double (four-passenger)","open","enclosed"],
 "s":"https://www.ehorses.com/classified-ads/carriage-and-vehicles/carriages",
 "x":[
  A("Cutter","Albany cutter · Portland cutter","Light North American one-horse sleigh seating two, with a high S-shaped dash.","","c. 1800","Sleigh",
    [("Albany cutter","","","Most popular and widely copied style"),("Portland cutter","","","Most popular and widely copied style")],"single or double seat · dash shape"),
  A("Troika sleigh","troika","Russian sleigh drawn by three horses abreast, the centre horse under a shaft bow trotting while the outer horses canter.","","17th century","Troika_(driving)",[],"horse breed (Vyatka, Orlov Trotter) · harness and bells"),
  A("Bobsled","bob sleigh · double-ripper","Vehicle body set on two pairs of bob runners, often a carriage converted for winter.","","","Sleigh",[],"body type · runner sets"),
  A("Prunkschlitten","splendour sleigh · parade sleigh","Richly carved and gilded ceremonial sleigh from Bavaria and Austria, often animal- or ship-shaped.","","","Sleigh",
    [("Ludwig II illuminated sleigh","","c. 1880","Built for Ludwig II of Bavaria")],"carved figure · gilding"),
  A("Vozok","","Enclosed Russian winter sleigh used by nobles, clergy and officials in Muscovy.","","","Sleigh",[],""),
  A("Booby-hut","Boston booby","New England enclosed sleigh with a coach body hung on runners by leather thoroughbraces.","","","Sleigh",[],""),
 ]}
brands=[
 {"n":"Abbot-Downing Company","c":"United States","f":"1813","seg":"Coach and carriage builder (historic)","d":"Concord, New Hampshire builder of coaches, wagons and carriages, later trucks; dissolved in the 1920s.","lines":["Concord coach","Overland wagon"],"eras":["Lewis Downing and J. Stephen Abbot partnership, 1828–1847"],"sig":["Concord coach"],"sc":["Stagecoach era","Wild West"],"rel":[],"s":W+"Abbot-Downing_Company"},
 {"n":"Dunton and Sons","c":"United Kingdom","f":"","seg":"Romani wagon builder (historic)","d":"Reading wagon builder whose living wagons gave the Reading vardo its name.","lines":["Reading wagon"],"eras":[],"sig":["Reading wagon"],"sc":["Romani travellers"],"rel":[],"s":W+"Vardo_(Romani_wagon)"},
]
trads=[
 {"n":"Wheelwrighting","g":"Woodwork & furniture","r":"Europe and North America","p":"Pre-industrial to present (rare since the 1960s)","d":"Craft of building and repairing wooden spoked wheels for carts, wagons and carriages.","tech":"Nave, spokes and felloes built from the centre out; spokes tenoned into the nave; hot iron tyre shrunk on; dishing and staggered spokes","mat":"Elm nave, oak spokes, ash felloes (hickory, black locust); iron or steel tyre","forms":["Horse-drawn carriage","Horse-drawn wagon","Romani vardo"],"ctr":["Worshipful Company of Wheelwrights (London)","Colonial Williamsburg","Hansen Wheel and Wagon Shop","Stutzman Amish shop"],"auth":"Wooden nave, spokes and felloes with a shrunk-on tyre; dish and spoke stagger","s":W+"Wheelwright"},
 {"n":"Coachbuilding (horse-drawn)","g":"Woodwork & furniture","r":"Britain, Europe and North America","p":"16th–19th century","d":"Specialised trade building horse-drawn coach and carriage bodies and undercarriages.","tech":"Cabinet-style joinery of curved timber framing; separate body-maker, carriage-maker, coach-smith, trimmer and painter","mat":"Ash, beech, elm, oak, mahogany; iron axles and springs; leather; brass","forms":["Coach","Brougham","Landau","Phaeton","Concord coach"],"ctr":["Worshipful Company of Coachmakers and Coach Harness Makers (1630)","Barker (1710)","Brewster & Co. (1810)","Thrupp & Maberly","Abbot-Downing Company","Studebaker"],"auth":"Builder's plates and maker records; period joinery, springs and trimming","s":W+"Coachbuilder"},
 {"n":"Romani wagon building and painting","g":"Woodwork & furniture","r":"Britain","p":"From c. 1870","d":"Building and decorating vardo living wagons with carving, scrollwork and gold leaf.","tech":"Tongue-and-groove panelling, carved ornament, painted scrollwork, gilding","mat":"Timber, canvas (bow top), cast-iron stove, gold leaf","forms":["Reading wagon","Ledge wagon","Bow top","Burton wagon","Brush wagon"],"ctr":["Dunton and Sons (Reading)","Jim Berry","John Pockett","Tom Stevens","Tommy Gaskin","Yorkie Greenwood","Lol Thompson"],"auth":"Wagon type by body shape and wheel placement; carving and painting by known wagon artists","s":W+"Vardo_(Romani_wagon)"},
]
out={"kinds":[carriage,wagon,vardo,sleigh],"brands":brands,"traditions":trads,
 "notes":"All four planned kinds kept. Old G&F Concord Stagecoach became a version of Concord coach; Cinderella Carriage and Kühnle Allgäu Wagonette stay in m (no archetype page). No page found for Kühnle or modern marathon carriages, so none added. Amish community colour codes, Scandinavian sleigh types and pung left out (not on retrieved pages). Historic coachbuilders (Barker, Brewster, Studebaker) named only in the tradition, not as brands."}
p="work/G1/shelves/09_01.json";t=p+".tmp";json.dump(out,open(t,"w"),ensure_ascii=False,indent=1);os.replace(t,p)
