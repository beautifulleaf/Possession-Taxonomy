import json, copy, os, shutil
R='/home/user/Possession-Taxonomy/rebuild/'
src=json.load(open(R+'work/STR_A3/bak/A3.json'))
OLD={}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']: OLD[k['n']]=k
used=set()
RING='https://en.wikipedia.org/wiki/Ring_(jewellery)'
EAR='https://en.wikipedia.org/wiki/Earring'
BRA='https://en.wikipedia.org/wiki/Bracelet'
BRO='https://en.wikipedia.org/wiki/Brooch'
PIE='https://en.wikipedia.org/wiki/Body_piercing_jewellery'
LST='https://en.wikipedia.org/wiki/List_of_jewellery_types'
def K(n, tt=None, drop=(), d=None, a=None, see=None, rn=None, addx=(), r=None, s=None, keepm=True):
    k=copy.deepcopy(OLD[n]); used.add(n)
    k.pop('t',None)
    if rn: k['n']=rn
    if d: k['d']=d
    if a is not None: k['a']=a
    if tt: k['tt']=tt
    if drop:
        dn=set(drop); have={x['n'] for x in k.get('x',[])}
        assert dn<=have,(n,dn-have)
        k['x']=[x for x in k.get('x',[]) if x['n'] not in dn]
    for x in addx: k.setdefault('x',[]).append(x)
    if r is not None: k['r']=(k.get('r') or [])+r
    if not keepm: k['m']=[]
    if see: k['see']=see
    if s: k['s']=s
    for key in ('x','m','r'):
        if key in k and not k[key]: k.pop(key)
    return k
def NEW(n,d,tt,s,a="",see=None,m=None,x=None):
    k={'n':n,'a':a,'d':d,'tt':tt,'s':s}
    if see: k['see']=see
    if m: k['m']=m
    if x: k['x']=x
    return k
def S(n,t,ks,ax=None):
    s={'n':n,'t':t,'k':ks}
    if ax: s['ax']=ax
    return s
def D(n,mode,t,ax,shelves,note=None):
    od=[d for d in src['depts'] if d['n']==n or d['n']==n.replace('&','&')]
    dp={'n':n,'mode':mode,'t':t,'ax':ax,'s':shelves}
    return dp
def sv(*a): return [list(x) for x in a]

depts=[]
# ---------------- RINGS
rings=[
 S("Engagement & stone-set rings","Rings built around how the stones are arranged, from the single centre stone to the full circle of stones; a plain band → Bands & fashion rings.",[
  K("Solitaire ring",[["Setting",["Prong (four- or six-claw)","Bezel","Tension","Basket","Cathedral","Trellis"]],["Band",["Plain","Pavé"]]],a="solitaire engagement ring",see=sv(["A3","Halo ring","one stone with a surround of stones"])),
  K("Halo ring",[["Halo",["Single halo","Double halo","Hidden halo"]],["Halo stones",["Plain","Pavé"]]]),
  K("Three-stone ring",[["Side stones",["Matched","Graduated","Coloured"]],["Setting",["Prong","Bezel"]]]),
  K("Toi et moi ring",[["Stone pairing",["Matching pair","Contrasting shapes","Diamond and coloured stone"]],["Shank",["Bypass"]]]),
  K("Cluster ring",[["Arrangement",["Flower cluster","Coloured centre with diamond surround","Illusion cluster"]]]),
  NEW("Giardinetti ring","Ring set with gems arranged as a small flower basket or garden of blooms.",[["Motif",["Flower basket","Bouquet"]]],RING,a="giardinetto ring"),
  K("Eternity ring",[["Extent",["Full eternity","Half eternity"]],["Setting",["Channel set","Claw set"]],["Stone shape",["Round brilliant","Princess","Emerald","Oval"]]],drop=["Diamond eternity ring"],d="Band set with a continuous line of identically cut stones, all the way round or across the face; the diamond version was marketed by De Beers from the 1960s as a symbol of never-ending love.",see=sv(["A3","Tennis bracelet","same line of matched stones"])),
 ],"kinds by how the stones are arranged: one, a surround, three, two, many, a basket, a full circle"),
 S("Bands & fashion rings","Rings worn for looks or as plain bands, from the wedding band to the statement stone and the thumb or knuckle ring; a ring set to propose → Engagement & stone-set rings.",[
  K("Band ring",[["Occasion",["Wedding band","Anniversary band","Men's band"]],["Profile",["Court","D-shape","Flat","Comfort fit"]],["Style",["Rolling (interlocked bands)","Stackable (slim, worn in stacks)"]]],a="Wedding band · Wedding ring · Band",see=sv(["D2","Smart ring","a ring-shaped wearable instead of jewellery"],["A3","Claddagh ring","Irish ring of hands and heart worn as a wedding band"])),
  K("Cocktail ring",[["Material",["Costume (paste)","Fine gemstone"]]]),
  NEW("Birthstone ring","Slim ring set with the wearer's birthstone or a family member's; a mother's ring carries several.",[["Stones",["Single birthstone","Several birthstones (family)"]]],RING,a="Mother's ring"),
  K("Thumb ring",[["Form",["Plain band","Hammered","Braided","Coil"]]],see=sv(["E2","Archery thumb ring","a thumb ring for drawing a bow"])),
  NEW("Midi ring","Slim ring worn above the middle joint of the finger, often in sets.",[["Form",["Plain band","Set of several"]]],RING,a="knuckle ring · above-knuckle ring"),
 ],"kinds from plain to showy, then by finger: band, statement stone, birthstone, thumb, knuckle"),
 S("Rings of identity & pledge","Rings that say who the wearer belongs to or what was promised: a family seal, a school, a pledge before engagement.",[
  K("Signet ring",[["Face shape",["Oxford oval","Cushion","Round"]],["Face",["Engraved crest or coat of arms","Monogram","Plain (unengraved)","Intaglio stone"]],["Worn on",["Little finger (pinky)"]]],drop=["Oxford oval signet","Cushion signet","Round signet","Intaglio stone signet"]),
  K("Class ring",[["School",["High school","College","Military academy"]]],see=sv(["F3","Championship ring","a ring given to a winning team"])),
  NEW("Promise ring","Slim band or small-stone ring given as a pledge before engagement or as a token of commitment.",[["Stone",["Plain band","Small diamond","Birthstone"]],["Metal",["Silver","Gold"]]],RING,a="pre-engagement ring"),
 ],"kinds by what the ring marks: family, school, a pledge"),
 S("Novelty & memorial rings","Rings with a trick, a message or a memory attached; a plain band → Bands & fashion rings.",[
  K("Puzzle ring",[["Number of bands",["Two (gimmel)","Three","Four or more"]]]),
  K("Mood ring",[["Stone",["Liquid-crystal stone"]]]),
  K("Poison ring",[["Lid",["Hinged bezel","Sliding bezel"]]],a="pillbox ring"),
  NEW("Acrostic ring","Ring whose stones are chosen so their initials spell a word such as 'dearest' or 'regard'.",[["Word spelled",["Dearest","Regard"]]],RING,a="regard ring"),
  K("Memento mori ring",[["Purpose",["Mourning (commemorative)","Reminder of death"]],["Motif",["Skull","Inscription"]]],a="mourning ring"),
 ],"kinds by what the ring does besides adorn: interlock, change colour, open, spell a word, remember the dead"),
]
depts.append(D("Rings","variety","Rings worn on the fingers or thumb, by what the ring is for; a ring made for a toe → Anklets & body chains, a ring for a piercing → Body piercing jewellery.","What is the ring for: a proposal setting, plain or fashion wear, marking identity or a pledge, or a novelty or memorial?",rings))
# ---------------- EARRINGS
ears=[
 S("Studs & hoops","Earrings that sit on or round the lobe without hanging far below it; a longer hanging earring → Drops & dangles.",[
  K("Stud earring",[["Back",["Friction (push) back","Screw back"]],["Setting",["Basket","Martini","Bezel"]],["Stone",["Diamond","Pearl","Gemstone","Plain metal"]]],drop=["Diamond solitaire stud","Pearl stud"],a="Studs · post earring",see=sv(["A3","Labret stud","a flat-back stud also worn in the ear"])),
  K("Hoop earring",[["Closure",["Continuous hoop","Hinged hoop","Spring hoop (unpierced)"]],["Size",["Huggie (hugs the earlobe)","Standard","Large"]],["Form",["Bali","Creole (broader at the bottom)","Sleeper (thin wire circle)"]]],drop=["Creole hoop","Sleeper"],keepm=False,see=sv(["A3","Circular barbell","a ring-shaped bar worn in the same piercing"])),
 ],None),
 S("Drops & dangles","Earrings whose ornament hangs below the lobe; a hoop or stud → Studs & hoops.",[
  K("Drop earring",[["Length",["Drop","Dangle","Statement"]]],a="Dangle earring",see=sv(["A3","Jhumka","South Asian bell-shaped drop"],["A3","Ear weight","a heavy hanger for stretched lobes"])),
  NEW("Chandelier earring","Drop earring wider at the base, with tiers or branches of stones and pendants.",[["Tiers",["Single tier","Multi-tier"]],["Material",["Gemstone","Crystal","Beaded","Metal"]]],EAR,see=sv(["A3","Chandbali","South Asian crescent earring"])),
  NEW("Threader earring","Fine chain pulled through the piercing so it hangs at the front and back, plain or with beads.",[["Ornament",["Plain chain","Beaded"]]],EAR,a="ear thread · ear string · earthreader"),
 ],"kinds by how it hangs: drop, tiered chandelier, threaded chain"),
 S("Ear wraps & clip-ons","Earrings held by the shape of the ear or by a clip instead of a post through the lobe.",[
  K("Clip-on earring",[["Mechanism",["Clip","Screw (ear screw)","Magnetic","Stick-on"]]],a="Clip earring · ear screw"),
  NEW("Ear cuff","Band that wraps the outer ear cartilage, with no piercing needed; some chain to a lobe piercing.",[["Form",["Open wrap","Ear climber"]],["Link",["Free","Chained to lobe piercing"]]],EAR,a="ear wrap · ear crawler"),
  NEW("Ear jacket","Ornament worn with a lobe stud whose second part passes behind the lobe, so it shows on both sides.",[["Material",["Gold","Silver","Gem-set"]]],EAR),
 ],"kinds by how it holds: clip or screw, wrap round the ear, jacket behind the lobe"),
]
for k in ears[2]['k'][:1]: pass
# attach archetype of old Ear cuff & jacket note
used.add("Ear cuff & jacket")
depts.append(D("Earrings","variety","Jewellery worn on the ear, pierced or not; ear jewellery for stretched lobes → Body piercing jewellery, a regional ear form → Traditional & regional jewellery.","Where does the ornament sit: on the lobe, hanging below it, or wrapped on or clipped to the ear?",ears))
# ---------------- NECKLACES
neck=[
 S("Chains & strands","Necklaces that are a strand of one material worn on their own; one with a hanging ornament → Pendants, lockets & charms.",[
  K("Necklace chain",[["Metal",["Yellow gold","White gold","Rose gold","Sterling silver","Platinum","Stainless steel"]],["Build",["Solid","Hollow"]]],a="chain necklace"),
  K("Pearl necklace",[["Length",["Collar (25–33 cm)","Choker (36–41 cm)","Princess (43–48 cm)","Matinée (51–61 cm)","Opera (71–89 cm)","Rope (over 110 cm)"]],["Pearl type",["Akoya","South Sea","Tahitian","Freshwater","Keshi","Baroque","Natural"]],["Strands",["Single strand","Multi-strand","Graduated"]]],drop=["Cultured Akoya pearl strand"],d="Strand of pearls worn as a necklace, named by length and pearl type; Mikimoto developed the round cultured Akoya strand in the early 1900s.",see=sv(["F6","Pearl","the loose pearl itself"])),
  K("Beaded necklace",[["Bead material",["Glass","Gemstone","Wood","Seed bead","Shell"]],["Strands",["Single strand","Multi-strand"]]],see=sv(["F4","Rosary","prayer beads are strung the same way"],["F4","Mala","prayer beads are strung the same way"])),
  K("Tennis necklace",[["Setting",["Four-prong","Bezel","Buttercup","Channel"]],["Stone spacing",["Graduated","Uniform"]],["Stone",["Natural diamond","Lab-grown diamond","Moissanite","Cubic zirconia"]]],see=sv(["A3","Tennis bracelet","same line of matched stones"])),
  K("Station necklace",[["Stations",["Bezel-set diamonds","Pearls","Beads"]],["Spacing",["Regular","Irregular"]]]),
  K("Lariat",[["Material",["Chain","Pearl","Beaded"]],["Ending",["Y-drop with clasp","Tassel"]]]),
 ],"kinds by what makes up the strand: links, pearls, beads, a line of stones, spaced stones, an open length"),
 S("Chokers, collars & neck rings","Necklaces defined by how they sit at the neck rather than by what they are made of.",[
  K("Choker",[["Material",["Velvet","Ribbon","Lace","Leather","Beaded","Metal"]],["Pendant",["Plain","With pendant"]]],drop=["Ribbon choker"],d="Necklace that fits closely round the neck, usually 36–41 cm long; the plain ribbon choker dates from the 19th century."),
  K("Collar necklace",[["Build",["Beaded broad collar","Chain collar","Metal plate collar"]]]),
  K("Statement necklace",[["Form",["Bib","Cluster"]],["Material",["Beaded","Crystal","Metal"]]],a="bib necklace"),
  K("Neck ring",[["Origin",["Celtic","Viking"]],["Build",["Single piece","Twisted strands"]]],drop=["Viking neck ring"],d="Rigid ring of metal worn round the neck, open or closed, from the Celtic torc to the Viking silver ring."),
 ],"kinds by how it sits at the neck: tight band, flat collar, bib, rigid ring"),
 S("Pendants, lockets & charms","Ornaments that hang from a chain or cord, by what the ornament is or does.",[
  K("Pendant",[["Metal",["Solid gold","Sterling silver"]],["Finish",["Gem-set","Enamel"]],["Hanging",["On chain","On cord"]],["Bail",["Sliding bail","Fixed bail"]]],see=sv(["A3","Hei-tiki","Māori carved pendant"])),
  K("Locket",[["Shape",["Round","Oval","Heart","Book"]],["Contents",["One photo","Multi-photo","Hair under glass","Perfume"]],["Use",["Mourning","Keepsake"]]],drop=["Mourning locket","Keepsake locket","Spinner locket","Photo locket","Perfume locket"],d="Pendant that opens to hold a picture or keepsake; Victorian mourning, hair-keepsake, spinner and perfume lockets are all variants.",see=sv(["A3","Cameo","carved relief often mounted as a locket face"])),
  K("Cameo",[["Material",["Shell","Hardstone (agate, onyx)","Glass","Ceramic (jasperware)"]],["Making",["Machine-cut","Hand-carved"]],["Mount",["Pendant","Brooch","Pendant-brooch","Ring"]]],drop=["Shell cameo","Hardstone cameo"],see=sv(["A3","Brooch","cameos are often brooches"])),
  K("Initial and name pendant",[["Form",["Script nameplate","Block letters","Single initial","Double plate"]],["Metal",["Gold","Silver"]]]),
  K("Charm",[["Attachment",["Dangle charm","Clip charm","Bead (threaded) charm","Modular link","Soldered flat"]],["Finish",["Enamel","Murano glass","Engravable tag"]]],drop=["Victorian charm","Mid-century charm"],d="Small ornament made to hang from or thread onto a bracelet, chain or pendant loop; Victorian and 1950s soldered charms are collected as vintage.",see=sv(["A3","Charm bracelet","the bracelet that carries charms"],["A4","Bag charm","a charm hung on a bag"])),
  K("Evil-eye amulet",[["Form",["Glass bead","Hamsa-backed"]],["Worn as",["Bracelet","Pendant"]]],see=sv(["F4","Protective charm","devotional protective charms"])),
  K("Cornicello",[["Material",["Gold","Silver","Red coral"]]],see=sv(["F4","Protective charm","devotional protective charms"])),
 ],"kinds by what hangs: any ornament, one that opens, a carved relief, lettering, a collectible charm, a protective amulet"),
]
depts.append(D("Necklaces & pendants","variety","Jewellery hung or fitted round the neck: strands, close collars and the ornaments hung on them; a form that belongs to one regional tradition → Traditional & regional jewellery.","What makes the piece: a chain or strand, something fitted close at the neck, or an ornament hung on one?",neck))
# ---------------- BRACELETS
brac=[
 S("Rigid bracelets","Bracelets of fixed shape that go on over the hand or the side of the wrist, plus the upper-arm armlet.",[
  K("Bangle",[["Material",["Metal","Glass","Lac","Shell (shakha)","Wood","Plastic","Jade (nephrite or jadeite)"]],["Build",["Hinged","Stacked set"]],["South Asian form",["Choor (chudi)","Kada","Kankan"]]]),
  K("Cuff bracelet",[["Form",["Open cuff","Wrap (coil) cuff","Wire cuff","Wide cuff","Hinged cuff"]]],a="cuff"),
  K("Armlet",[["Tradition",["Bajuband","Kelat bahu (Indonesia)","Vangi (Sri Lanka)"]],["Form",["Snake arm ring","Chainmail armlet"]]]),
 ],"kinds by how the ring closes: closed or hinged bangle, open cuff, upper-arm band"),
 S("Strand & chain bracelets","Flexible bracelets, by what the strand is made of.",[
  K("Tennis bracelet",[["Setting",["Four-claw","Bezel","Channel"]],["Stone",["Natural diamond","Lab-grown diamond","Coloured gemstone"]]],drop=["Diamond line bracelet"],d="Flexible hinged line of evenly set stones round the wrist; named after Chris Evert dropped hers at the 1978 US Open (often dated 1987).",see=sv(["A3","Tennis necklace","same line of matched stones"])),
  K("Chain bracelet",[["Link",["Curb","Anchor","Figaro","Paperclip","Rolo","Box","Snake","Station"]]]),
  K("Charm bracelet",[["Charm attachment",["Dangle charm","Threaded bead charm","Italian link charm"]]]),
  K("Beaded bracelet",[["Fastening",["Stretch","Clasped"]],["Bead",["Wood","Glass","Crystal","Gemstone (power-stone)","Plastic"]]]),
  K("Friendship bracelet",[["Pattern",["Alpha (letters)","Candystripe","Chevron","Zig zag","Hearts","Diamonds"]],["Knot",["Double chain knot","Chinese staircase"]]]),
 ],"kinds by what the strand is made of: set stones, links, charms, beads, knotted cord"),
 S("Identity, awareness & hand bracelets","Bracelets with a job beyond looks: naming the wearer, showing a cause, or linking to the hand.",[
  K("Identity bracelet",[["Form",["Engraved plate on chain","Medical alert tag","Silicone ID band"]]],drop=["Medical ID bracelet"],a="ID bracelet · medical ID bracelet"),
  NEW("Silicone wristband","Coloured silicone band worn for a cause, a team or a message, popularised by the yellow Livestrong band from 2003.",[["Use",["Charity or awareness","Team or event","Emergency ID"]]],BRA,a="gel bracelet · rubber wristband · baller band"),
  K("Hand harness",[["Form",["Single ring","Multi-ring","Beaded"]]]),
 ],"kinds by the job: identify, show a cause, join to the finger"),
]
depts.append(D("Bracelets & bangles","variety","Jewellery for the wrist and arm; an ankle form → Anklets & body chains, a watch strap → Watches & timekeeping.","Is the bracelet a rigid ring, a flexible strand, or made for a job such as naming the wearer or linking to the hand?",brac))
# ---------------- BROOCHES
bro=[
 S("Brooches","Ornaments fixed to clothing by a pin and catch, from ancient fibulae to costume jewellery.",[
  K("Brooch",[["Form",["Bar brooch","Clip brooch","Pendant brooch (convertible)","Locket brooch","Portrait brooch","Stomacher"]],["Style",["Mourning (jet, hair)","Cameo","Micromosaic","Edwardian platinum","Costume"]]],drop=["Victorian mourning brooch","Cameo brooch","Edwardian platinum brooch","Penannular brooch","Miriam Haskell beaded brooch","Schiaparelli surrealist brooch"],r=[["Beaded costume brooches","Miriam Haskell"],["Surrealist costume brooches","Schiaparelli"]],a="pin · clip brooch",see=sv(["A3","Cameo","carved relief mounted as a brooch"])),
  NEW("Fibula","Ancient European brooch, often bow-shaped, that fastened cloaks and tunics; penannular and annular rings are related forms.",[["Form",["Bow","Plate","Trumpet","Penannular","Annular","Cruciform","Equal-armed"]]],BRO,a="bow brooch",see=sv(["A3","Amazigh fibula","North African fibulae"]),x=[{"n":"Penannular brooch","a":"","d":"Ring-shaped brooch with a gap in the circle, elaborated in early medieval Ireland and Britain.","mk":"","y":"600 BC–early medieval","s":"https://en.wikipedia.org/wiki/Brooch","v":[{"n":"Tara Brooch","mk":"","y":"","d":""}]}]),
 ],None),
 S("Shirt & tie jewellery","Fastenings and ornaments for a formal shirt, collar or tie.",[
  K("Cufflink",[["Back",["Fixed back","Whale back","Toggle (swivel) back"]],["Form",["Chain-link","Stud-style"]]],drop=["Chain-link cufflink"],a="cuff link"),
  K("Shirt stud",[["Fastening",["Sliding-pin stud","Screw-back stud","Collar stud"]],["Material",["Mother-of-pearl","Onyx"]]]),
  K("Tie clip",[["Form",["Tie bar (slide)","Tie pin","Tie chain"]]],a="tie bar · tie slide · tie clasp · tie pin"),
  NEW("Collar pin","Bar or pin that fastens the two points of a dress-shirt collar under the tie knot, lifting the knot.",[["Fastening",["Collar bar with screw-off ends","Pin through the collar","Bar with clips at each end"]]],'https://en.wikipedia.org/wiki/Collar_pin',a="collar bar"),
 ],"kinds by the part of the shirt: cuff, front, tie, collar"),
 S("Lapel pins, badges & hat pins","Small pins worn on a jacket, bag or hat.",[
  K("Lapel pin",[["Making",["Hard enamel (cloisonné)","Soft enamel","Photo-etched","Printed"]],["Fastening",["Butterfly clutch","Magnetic clasp","Stick pin","Rosette"]]],drop=["Flag pin"],a="enamel pin",d="Small pin with a post and clutch worn in a jacket lapel, such as a flag pin."),
  K("Pin badge",[["Form",["Button badge","Enamel badge"]]],drop=["Button badge"]),
  K("Hat pin",[["Accessory",["Hatpin holder","Point protector"]]]),
 ],"kinds by where the pin goes: lapel, any garment or bag, hat"),
]
depts.append(D("Brooches, pins & cufflinks","variety","Ornaments fixed to clothing by a pin, clip or fastening, by what they fasten; a medal or military badge → Trophies & awards.","What is it fixed to: clothing as pure ornament, a shirt or tie, or a lapel, bag or hat?",bro))
# ---------------- HEAD
head=[
 S("In the hair","Ornaments worn on or in the hair, by how they are held; plain everyday clips → Personal Care & Beauty.",[
  K("Tiaras & crowns",[["Shape",["Bandeau","Circlet (runs round the full head)"]],["Material",["Diamond","Pearl","Costume"]]],rn="Tiara",a="diadem",d="Jewelled open half-circlet worn on formal occasions, from royal diamond tiaras to bridal pieces.",drop=["Kokoshnik tiara"] and ["Bandeau","Circlet"]),
  NEW("Crown","Closed circle or arch of metal and jewels worn for ceremony or pageant; a crown of office → F4.",[["Form",["Closed circle","Arched"]],["Make",["Gem-set","Costume"]]],LST,a="pageant crown",see=sv(["F4","Crown of office","a crown that belongs to an office"],["A3","Tiara","the open half-circlet"])),
  K("Hairpin",[["Form",["Hair stick","U-shaped hairpin"]],["Head",["Plain","Jewelled"]]],drop=["Kanzashi","Binyeo","Fazan"],see=sv(["A3","Kanzashi","Japanese hair ornaments"],["H1","Hair clip","everyday clips"])),
  K("Hair comb",[["Form",["Side comb","French twist comb"]]],see=sv(["H1","Hair clip","everyday clips"])),
 ],"kinds by how they are held: sit on the head, push into a bun, comb in"),
 S("On the face & teeth","Ornaments fixed to the forehead or the teeth.",[
  K("Stick-on bindi",[["Material",["Felt","Thin metal","Jewelled"]]],see=sv(["H1","Bindi","the made-up bindi"])),
  K("Grillz",[["Teeth covered",["Top 6","Top 8","Bottom 8","Bottom 10","Single cap"]],["Fitting",["Removable","Permanent"]],["Metal",["10k–24k gold","Silver","Platinum"]],["Coverage",["Solid","Open-face","Double-cap"]],["Stones",["Plain","Iced (pavé-set)"]]],drop=["Solid gold grill","Open-face grill","Iced grill","Double-cap grill"],a="Grills · fronts · golds · caps"),
 ],None),
]
depts.append(D("Hair & head jewellery","variety","Jewellery worn on the head, hair, forehead or teeth; a South Asian form such as the maang tikka → Traditional & regional jewellery.","Where on the head does it sit: in the hair, or on the face and teeth?",head))
# ---------------- ANKLETS
anklets=[
 S("Ankle & toe","Jewellery for the foot, by which part it circles.",[
  K("Anklet",[["Build",["Chain (flexible)","Rigid band","Beaded or string","Leather or cord","Barefoot sandal"]],["Regional form",["Payal / pazeb / jhanjhar","Ghungroo (dancers' bell anklet)","Kholkhal (Egyptian)","Heavy silver tribal (Rajasthan)"]]]),
  K("Toe ring",[["Fit",["Fitted","Adjustable (open)"]],["Style",["Plain band","Jewelled or floral"]],["Metal",["Silver","Gold","Rubber or non-precious"]]]),
 ],None),
 S("Waist & torso","Jewellery worn on the waist or hung across the body.",[
  K("Waist chain",[["Build",["Chain","Beaded"]],["Trim",["Plain","With charms or drops"]],["Wear",["Single","Layered"]]]),
  K("Body chain",[["Layout",["Torso harness (crosses chest and back)","Back chain (nape to waist)","Shoulder-to-waist (diagonal)"]],["Make",["Fine-jewellery convertible version"]]]),
  NEW("Chatelaine","Ornamental waist hook with several chains, each holding a useful item such as scissors, thimble case, watch or keys; popular in the 18th and 19th centuries.",[["Hanging items",["Scissors","Thimble case","Watch","Keys"]]],'https://en.wikipedia.org/wiki/Chatelaine_(chain)'),
 ],"kinds by how it is worn: round the waist, across the torso, hung from the waist"),
]
depts.append(D("Anklets & body chains","variety","Jewellery for the foot, waist and torso; a South Asian waist belt → Traditional & regional jewellery.","Which part carries it: the ankle or toe, the waist, or the torso?",anklets))
# ---------------- PIERCING
pier=[
 S("Bars & barbells","Bars worn through a piercing with an end at each side, by the bar's shape.",[
  K("Straight barbell",[["Thread",["Internally threaded","Threadless"]],["Use",["Nipple bar","Industrial bar"]],["Gauge",["Large gauge"]]],a="barbell · industrial bar"),
  K("Curved barbell",[["Thread",["Internally threaded","Threadless"]]]),
  K("Circular barbell",[["Thread",["Externally threaded","Internally threaded","Threadless"]]],see=sv(["A3","Hoop earring","a ring-shaped piece in the ear"])),
  NEW("Spiral barbell","Coiled barbell worn through a piercing, often made in glass.",[["Material",["Glass","Metal"]]],PIE),
  K("Navel curve",[["Ornament",["Plain gem","Double gem","Dangle","Navel clicker"]],["Material",["PTFE"]]]),
  K("Surface bar",[["Angle",["90-degree"]],["Thread",["Internally threaded","Threadless"]],["Material",["PTFE"]]]),
  NEW("Nipple shield","Decorative metal shield worn over a nipple piercing, attached to a barbell.",[["Material",["Steel","Titanium","Gold"]]],PIE),
 ],"kinds by the bar's shape: straight, curved, circular, coiled, navel curve, surface staple, shielded"),
 S("Posts, rings & ends","The piece through the hole or the top that goes on it.",[
  K("Labret stud",[["Thread",["Internally threaded","Threadless"]],["Back",["Flat disc back"]]],see=sv(["A3","Stud earring","a flat-back stud also worn in the ear"])),
  K("Nose stud",[["Shape",["L-shape","Nose screw","Straight pin","Nose bone","Flat-back labret"]]]),
  K("Piercing ring",[["Closure",["Seamless (twist-open)","Captive bead (CBR)","Hinged segment clicker"]],["Placement",["Nose","Septum","Daith","Ear or lip"]]],see=sv(["A3","Nath","bridal nose ring"])),
  K("Threadless end",[["Setting",["Prong-set gem","Bezel-set gem","Cabochon","Cluster","Plain gold shape"]]]),
 ],"kinds by where it sits: the post, the ring, the top"),
 S("Stretched-ear jewellery","Pieces for lobes stretched beyond standard earring gauges.",[
  K("Ear plug",[["Flare",["Double flare","Single flare with O-ring","No flare (straight)"]],["Material",["Glass","Stone","Wood","Horn and bone","Amber","Titanium","Steel","Silicone","Acrylic"]]],drop=["Double-flare plug","Single-flare plug","Gorilla Glass plug","Silicone plug"],r=[["Gorilla Glass plugs","Gorilla Glass"],["Silicone plugs","Kaos Softwear"]],a="plug · earspool · gauge (colloquial)",see=sv(["A3","Ear tunnel","the hollow version"])),
  K("Ear tunnel",[["Flare",["Double flare","Single flare with O-ring","Threaded (screw-back)"]],["Material",["Steel","Titanium","Glass","Silicone","Wood","Stone"]]],drop=["Flesh tunnel","Skin Eyelets","Gorilla Glass eyelet"],r=[["Skin Eyelets","Kaos Softwear"],["Glass eyelets","Gorilla Glass"]]),
  K("Ear weight",[["Material",["Brass","Silver","Bronze","Copper","Stone","Horn","Wood"]]],drop=["Diablo Organics ear weights"],r=[["Ear weights","Diablo Organics"]]),
  K("Ear taper",[["Shape",["Straight taper","Crescent taper","Spiral","Pincher"]],["Material",["Steel","Acrylic","Glass","Horn"]]],drop=["Crescent taper","Spiral"]),
 ],"kinds by how they fill the lobe: solid plug, hollow tunnel, hanging weight, tapered stretcher"),
]
depts.append(D("Body piercing jewellery","mixed","Jewellery made to be worn through a piercing, sold by gauge and material; an ordinary earring → Earrings.","What form does the piece take where it passes through the piercing: a bar, a post, a ring, a replaceable end or a stretching piece?",pier))
# ---------------- TRADITIONAL
trad=[
 S("South Asian jewellery","Forms of India and its neighbours, worn for weddings and festivals; techniques are in the traditions register.",[
  K("Maang tikka",[["Technique",["Kundan","Polki","Temple gold"]],["Material",["Pearl","Oxidised silver"]]],see=sv(["A3","Matha patti","forehead ornament with side chains"])),
  K("Matha patti",[["Technique",["Kundan","Polki"]],["Material",["Pearl"]],["Strands",["Single-strand","Multi-strand"]]]),
  K("Jhumka",[["Material",["Gold","Oxidised silver","Pearl","Diamond"]],["Technique",["Kundan","Meenakari","Polki"]]],see=sv(["A3","Drop earring","the general hanging earring"])),
  K("Chandbali",[["Use",["Antique (beads and pendants)","Contemporary bridal","Everyday small"]],["Material",["Pearl","Diamond"]],["Technique",["Kundan"]]],see=sv(["A3","Chandelier earring","tiered western equivalent"])),
  K("Nath",[["Chain",["With chain (nathni)","Without chain"]],["Material",["Gold","Silver"]],["Stone",["Pearl","Ruby"]]],see=sv(["A3","Piercing ring","ring worn in the nostril or septum"])),
  K("Mangalsutra",[["Length",["Long","Short (daily wear)"]],["Make",["Black-bead chain","Turmeric thread","Diamond pendant"]]],see=sv(["A3","Necklace chain","chain base of the necklace"])),
  K("Haar and rani haar",[["Technique",["Kundan","Polki","Filigree gold","Temple gold"]],["Material",["Pearl"]]],see=sv(["A3","Pendant","the pendant that anchors it"])),
  K("Kamarbandh",[["Build",["Rigid","Flexible","Chain"]],["Finish",["Temple (kemp)","Antique","Diamond-set"]]],see=sv(["A3","Waist chain","the western waist chain"])),
 ],"kinds by body part from head to waist: forehead, ear, nose, neck, waist"),
 S("East Asian jewellery","Hair ornaments of Japan, Korea and China; a plain hairpin or comb → Hair & head jewellery.",[
  NEW("Kanzashi","Japanese hair ornament family of pins, sticks and combs, often floral, used from the Heian to Edo period.",[["Style",["Kogai","Bira-bira","Ōgi bira","Tama kanzashi","Hirauchi kanzashi","Tsumami kanzashi"]]],'https://en.wikipedia.org/wiki/Kanzashi',see=sv(["A3","Hairpin","the general hairpin"])),
  NEW("Binyeo","Korean hairpin fixing a woman's chignon; material and shape marked status.",[["Form",["Jam","Chae"]]],'https://en.wikipedia.org/wiki/Binyeo',see=sv(["A3","Hairpin","the general hairpin"])),
  NEW("Fazan","Chinese hairpin securing and decorating a bun, sometimes marking status.",[["Form",["Chai","Buyao"]]],'https://en.wikipedia.org/wiki/Hair_stick',see=sv(["A3","Hairpin","the general hairpin"])),
 ],"kinds by country: Japan, Korea, China"),
 S("African jewellery","Silver and brass forms of the Sahara, the Horn of Africa and North Africa.",[
  K("Tuareg cross pendant",[["Metal",["Silver","Copper or brass","Stone"]]],drop=["Agadez cross"],see=sv(["A3","Pendant","the general pendant"])),
  K("Ethiopian cross pendant",[["Material",["Silver","Brass","Wood"]]]),
  K("Amazigh fibula",[["Material",["Silver","Brass","Coral-set","Enamelled"]]],see=sv(["A3","Fibula","the ancient European fibula"])),
 ],"kinds by region: the Sahara, the Horn of Africa, North Africa"),
 S("European, American & Oceanic jewellery","Forms tied to Ireland, the American south-west and New Zealand.",[
  K("Claddagh ring",[["Metal",["Silver","Gold"]],["Band",["Celtic interlace band"]]],see=sv(["A3","Band ring","often worn as a wedding band"])),
  K("Squash blossom necklace",[["Make",["Plain silver","Turquoise-set blossoms","Coral-set","Coin beads","Overlay"]]]),
  K("Hei-tiki",[["Material",["Nephrite pounamu (kawakawa, īnanga, kahurangi)","Tangiwai (bowenite)","Bone","Imported jade (tourist)"]]],drop=["Hei-tiki"],see=sv(["A3","Pendant","the general pendant"])),
 ],"kinds by region: Ireland, the American south-west, New Zealand"),
]
depts.append(D("Traditional & regional jewellery","variety","Forms named for and belonging to one regional tradition, which a buyer asks for by their own name; the general form → the department of that body part.","Which regional tradition does the form belong to?",trad))
# ---------------- PARTS
parts=[S("Jewellery parts","Replaceable bits for jewellery an owner already has; findings for making jewellery → Craft & Art Supplies.",[
  K("Spare parts",[["Part",["Earring back (butterfly, screw, push)","Chain extender","Ring guard"]]],see=sv(["C4","Earring finding","the loose finding for making earrings"]))],None)]
depts.append(D("Jewellery parts","tier","Replacement backs, extenders and guards for jewellery already owned.","Which small fitting does the owner replace: a back, an extender or a guard?",parts))

# carry over dept notes/b
newd=[]
for dp in depts:
    o=next((d for d in src['depts'] if d['n']==dp['n']),None)
    if o:
        for key in ('note','b'):
            if o.get(key) is not None: dp[key]=o[key]
    newd.append(dp)
newd[3]['note']=None; newd[3].pop('note')
out=copy.deepcopy(src)
out['depts']=newd
out['ax']="Where on the body is the piece worn, or does it belong to one regional tradition?"
out['key']=[
 "1. Is it made to pass through a piercing, such as a barbell, labret, plug or threadless end? → Body piercing jewellery",
 "2. Is it a form named for and tied to one regional tradition, such as a mangalsutra, kanzashi or squash blossom necklace? → Traditional & regional jewellery",
 "3. Is it worn on a finger or thumb? → Rings",
 "4. Is it worn on the ear, pierced or clipped? → Earrings",
 "5. Is it worn round the neck, or hung from a chain there? → Necklaces & pendants",
 "6. Is it worn on the wrist or arm? → Bracelets & bangles",
 "7. Is it pinned or fastened to clothing, a shirt, a tie or a lapel? → Brooches, pins & cufflinks",
 "8. Is it worn in the hair, on the forehead or on the teeth? → Hair & head jewellery",
 "9. Is it worn on the ankle, toe, waist or torso? → Anklets & body chains",
 "10. Is it a replacement back, extender or guard? → Jewellery parts",
 "<i>Precedence: a piercing part (step 1) before an earring (step 4); a regional form (step 2) before its general body part, with a see link back to the general kind.</i>"]
# check all old kinds accounted
miss=set(OLD)-used
print('unused old kinds',miss)
json.dump(out,open(R+'work/STR_A3/A3.new.json','w'),ensure_ascii=False,indent=1)
