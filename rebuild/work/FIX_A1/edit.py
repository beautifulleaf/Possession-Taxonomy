import json,copy,os
B='/home/user/Possession-Taxonomy/rebuild/work/FIX_A1/bak/'
W='https://en.wikipedia.org/wiki/'
d=json.load(open(B+'A1.json')); br=json.load(open(B+'A1_brands.json')); tr=json.load(open(B+'A1_traditions.json')); mv=json.load(open(B+'A1_moves.json'))

def find(name):
    for D in d['depts']:
        for S in D['s']:
            for i,k in enumerate(S['k']):
                if k['n']==name: return D,S,i,k
    raise KeyError(name)
def A(n,d_,s,mk='',y='',a='',v=None,dt=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,d_='',mk='',y=''): return {"n":n,"mk":mk,"y":y,"d":d_}
def K(n,a,d_,s,t=None,x=None,tg=None,m=None,r=None):
    k={"n":n,"a":a,"d":d_}
    if t: k["t"]=t
    if tg: k["tg"]=tg
    k["s"]=s
    if x: k["x"]=x
    k["m"]=m or []
    if r: k["r"]=r
    return k

# ---- A1-1 headwear split
D,S,i,old=find("Traditional, ceremonial & uniform headwear")
new=[
K("Skullcap","kippah · yarmulke · taqiyah · zucchetto · kufi · kopiah","Small brimless cap fitting the crown, worn for faith or custom; the faith is a tag, the form is the kind.",W+"Kippah",
  t=["kippah / yarmulke (Judaism)","taqiyah (Islam)","songkok / kopiah / peci (Maritime South-East Asia)","zucchetto (Catholic clergy)","kufi","kofia (East Africa)","crocheted","velvet","suede, leather or satin","cotton or fleece prayer cap"],
  tg=["Jewish","Islamic","Christian"],
  x=[A("Kippah","Brimless cloth skullcap worn by Jewish men and some women; the Hebrew word means 'dome'.",W+"Kippah",a="yarmulke · koppel",
        v=[V("Crocheted (kippah serugah)","Common among Religious Zionists and Modern Orthodox Jews"),V("Black velvet","Worn by many Haredi, Hasidic and Yeshivish Jews"),V("Suede, leather or satin","Seen in Conservative and Reform communities"),V("Bukharian and Yemenite","Yemenite kippot are typically stiff black velvet with embroidered borders")],
        dt="crocheted, velvet, suede, satin · colour and size by community"),
     A("Taqiyah","Short rounded skullcap worn by Muslim men, signalling faith and sometimes regional identity.",W+"Taqiyah_(cap)",a="takke · araqchin · topi · kopiah",
        v=[V("Takke","Turkish cap in wool or cotton fleece"),V("Araqchin","Persian name"),V("Peci / songkok","Indonesian and Malaysian forms, often machine-knitted"),V("Tahýa","Turkmen cap in velvet, silk, satin or chintz")],
        dt="cotton, wool, velvet, knitted · regional name"),
     A("Zucchetto","Small hemispherical skullcap of Catholic clergy whose colour shows rank.",W+"Zucchetto",
        v=[V("White","Pope"),V("Scarlet","Cardinals"),V("Amaranth","Archbishops, bishops and territorial abbots and prelates"),V("Black","Priests, deacons and non-territorial abbots, though most do not wear one")],
        dt="silk · colour by rank"),
     A("Kufi","Brimless rounded cap worn across Africa, South Asia and the Middle East and in the African diaspora.",W+"Kufi",a="ade · fila · kofia",
        dt="kente cloth, mudcloth, knitted or crocheted yarn")]),
K("Fez & brimless cap","fez · tarboosh · tubeteika · doppa","Peakless, brimless cap in felt or embroidered cloth, from the Ottoman, North African and Central Asian worlds.",W+"Fez_(hat)",
  t=["Gandhi cap","Dhaka topi / Bhadgaunle topi (Nepal)","pakul (Afghanistan, Pakistan)","telpek","kolah namadi"],
  x=[A("Fez","Short cylindrical peakless felt hat, usually red with a black tassel; named for the Moroccan city of Fez.",W+"Fez_(hat)",a="tarboosh",y="1827",
        v=[V("Ottoman army fez","Made official headdress of Mahmud II's new army in 1827 and of civil and religious officials in 1829",y="1827"),V("Tunisian fez","Tunisia produced the earliest high-quality caps"),V("Moroccan fez","Felt dyed crimson with a berry in Fez")],
        dt="felt · red or other dyes · tassel"),
     A("Tubeteika","Russian term for many Turkic caps of Central Asia; the Uzbek and Uyghur doppa has a square base.",W+"Tubeteika",a="doppa · tyubeteyka",
        v=[V("Chust doppa","Uzbek cap decorated with white embroidery"),V("Northern Tajik cap","Square, black and white (Sughd)"),V("Southern Tajik cap","Round and brightly coloured (Khatlon)"),V("Pamir cap","Round, red or green")],
        dt="embroidered cloth · square or round · colour by region")]),
K("Turban & head-wrap","turban · pagri · dastar · imama","Headwear made by winding cloth around the head or a cap.",W+"Turban",
  t=["Sikh dastar","Rajasthani safa","pheta and Mysore peta (India)","Albanian shall","Cretan sariki","Kurdish jamadani","blangkon (Java)","tengkolok (Malay)","gaung paung (Myanmar)"],
  tg=["Sikh","Islamic"],
  x=[A("Dastar","Sikh turban; dastar is also the Persian word for turban.",W+"Turban",a="dastaar",dt="cotton or voile · length · colour"),
     A("Pagri","Hand-tied South Asian turban; the Rajasthani form is the safa.",W+"Turban",a="pagadi · safa · pheta",dt="cloth length · tying style · regional colour"),
     A("Imama","Islamic turban.",W+"Turban",a="imamah · amama",dt="cloth length · colour"),
     A("Kavuk","Ottoman imperial turban.",W+"Turban",dt="padded cap wound with cloth"),
     A("Tagelmust","Tuareg head-wrap.",W+"Turban",a="cheche",dt="cotton, often indigo · wrapped length")]),
K("Conical & woven sun hat","nón lá · salakot · kasa · sombrero vueltiao","Hat woven or sewn from palm, bamboo, sedge or straw, conical or domed, worn against sun and rain.",W+"N%C3%B3n_l%C3%A1",
  t=["buntal hat (Philippines)","chupalla (Chile)","mokorotlo (Lesotho)","jingasa (see Uniform headwear)"],
  x=[A("Nón lá","Traditional Vietnamese conical hat of leaves sewn onto a bamboo frame and varnished.",W+"N%C3%B3n_l%C3%A1",a="nón tơi",v=[V("Nón bài thơ","Thin white Huế cone decorated with pictures or verses")],dt="palm or bamboo leaves · varnish · cone shape"),
     A("Salakot","Philippine dome- or cone-shaped hat held by an inner headband and chinstrap.",W+"Salakot",
        v=[V("Talugong","Ivatan"),V("Kalugung","Ilocano, Kalinga"),V("Sarók","Visayan, Bicolano"),V("S'laong","T'boli")],dt="bamboo, rattan, buri straw, nipa or pandan leaves · horn or tortoiseshell trim"),
     A("Kasa","Traditional Japanese hat; the sugegasa is a conical sedge hat and the amigasa a wickerwork one.",W+"Kasa_(hat)",v=[V("Sugegasa","Conical, pointed, sedge"),V("Amigasa","Wickerwork; straw version worn in folk dances")],dt="sedge or straw · cone or dome"),
     A("Sombrero vueltiao","Colombian hat of the Zenú people made of caña flecha palm fibre, named a National Cultural Symbol in 2004.",W+"Sombrero_vueltiao",y="2004",dt="caña flecha fibre · black and white pattern · plait count")]),
K("Folk felt hat","Tyrolean hat · kalpak · qeleshe","Felt, fleece or knitted hat or cap tied to a region's folk dress.",W+"Tyrolean_hat",
  t=["Balmoral bonnet","Tam o' Shanter","barretina (Catalonia)","caubeen (Ireland)","šajkača (Serbia)","Montenegrin cap","Lika cap","Sami hat","montera (bullfighting)","sombrero cordobés","sombrero (charro)"],
  x=[A("Tyrolean hat","Alpine hat of green felt with a pointed crown, corded hatband and a side spray of flowers, feathers or a brush.",W+"Tyrolean_hat",v=[V("Gamsbart trim","The traditional brush, made from chamois hair")],dt="green felt · brim width · hatband · side trim"),
     A("Kalpak","Turkic tall-crowned cap of felt or sheepskin worn across Central Asia and the Caucasus.",W+"Kalpak",a="qalpaq · calpack",dt="felt or sheepskin · crown height · season weight"),
     A("Qeleshe","White brimless skullcap of wool felt worn by Albanians.",W+"Qeleshe",v=[V("Northern qeleshe","Hemispherical"),V("Kukës qeleshe","Truncated"),V("Southern qeleshe","Taller")],dt="pressed wool felt · white · height by region")]),
K("Academic cap","mortarboard · Oxford cap","Cap worn with academic dress.",W+"Square_academic_cap",
  t=["Tudor bonnet"],
  x=[A("Mortarboard","Flat square board fixed on a skullcap with a central tassel; probably Italian, from no later than 1520.",W+"Square_academic_cap",a="square academic cap · Oxford cap",y="by 1520",v=[V("Tasselled mortarboard","Tassels appeared in the 18th century")],dt="cloth-covered board · tassel colour")]),
K("Clerical hat","mitre · biretta · cappello romano","Hat of bishops and clergy whose shape or colour shows office.",W+"Biretta",
  t=["mitre (bishops)","cappello romano","capirote (Holy Week)","shovel hat (Anglican)","kolpik (Hasidic)"],
  tg=["Christian","Jewish"],
  x=[A("Biretta","Square cap with three or four peaks, sometimes with a pom; worn by Catholic and some Anglican and Lutheran clergy.",W+"Biretta",
        v=[V("Scarlet","Cardinals"),V("Amaranth with purple pom","Bishops"),V("Black","Priests and deacons"),V("Four-peaked","Marks pontifical doctorates")],dt="three or four peaks · pom · colour by rank")]),
K("Court & official hat","gat · wushamao","Hat tied to rank at an East Asian court or in officialdom.",W+"Gat_(hat)",
  t=["jeongjagwan (Korea)","ayam (Korea)","wushamao (China)","guapi mao (China)","damao (China)","weimao (China)"],
  x=[A("Gat","Korean men's hat worn with hanbok in the Joseon period, of bamboo or horsehair on a bamboo frame, partly transparent.",W+"Gat_(hat)",dt="horsehair or bamboo · brim width · status of wearer")]),
K("Uniform headwear","military hat · bearskin · shako · kepi","Caps and hats set by regiment, service or rank; historical pieces are also collected as militaria (E4).",W+"Shako",
  t=["busby","bicorne","tricorne","Hardee hat","campaign hat","garrison / forage cap","Glengarry","sailor cap","budenovka","jingasa (Japan)"],
  x=[A("Bearskin","Tall fur cap descended from 17th–18th-century grenadier mitre caps; worn in ceremonial dress by the British Foot Guards.",W+"Bearskin",v=[V("Grenadier Guards","Adopted after Waterloo in 1815",y="1815"),V("Coldstream and Scots Guards","Adopted by 1831",y="1831")],dt="fur · height · plume"),
     A("Shako","Tall cylindrical peaked military cap, adopted by European armies from about 1800.",W+"Shako",y="c.1800",v=[V("French stovepipe"),V("British Albert"),V("British bell-top"),V("Russian kiwa"),V("Swedish m/1815")],dt="felt or leather · plate · plume"),
     A("Kepi","Flat-topped visored cap that began in the French Army in Algeria in the 1830s as a lighter alternative to the shako.",W+"Kepi",y="1830s",v=[V("Foreign Legion white kepi","Especially notable")],dt="cloth · crown height · cover colour")]),
K("Historical hat & bonnet","mobcap · poke bonnet · capotain · hennin","Hat or bonnet from a past era, now worn for costume, re-enactment or collected as an antique.",W+"Mob_cap",
  t=["cavalier hat","capotain","pilgrim's hat","wideawake","bycocket","hennin","mobcap","poke bonnet","coal scuttle bonnet","widow's cap"],
  x=[A("Mobcap","Circular gathered linen cap with a ruffled brim, worn by married women in the 18th and early 19th centuries and later by servants and nurses.",W+"Mob_cap",y="18th century",dt="linen · ruffle · tie")]),
K("Country & weather hat","deerstalker · sou'wester","Hat made for rural wear or wet weather.",W+"Deerstalker",
  t=["deerstalker","sou'wester"],
  x=[A("Deerstalker","Cloth cap of English country wear with front and rear peaks and earflaps tied up or under the chin, usually tweed.",W+"Deerstalker",dt="tweed · earflaps · peaks"),
     A("Sou'wester","Collapsible oilskin hat with a wide slanting brim, longer at the back to protect the neck.",W+"Sou%27wester",dt="oilskin · brim · chin tie")]),
]
S['k'][i:i+1]=new
# novelty hats -> E1
mv['out'].append({"to":"E1","dept":"Pretend & role play","kind":{"n":"Novelty hat","a":"party hat · costume hat","d":"Party, fancy-dress and joke hats such as the Santa hat, wizard hat, dunce cap and umbrella hat.","t":["party hat","Santa hat","wizard / witch hat","dunce cap","umbrella hat"],"s":W+"List_of_hat_styles","m":[],"r":[]}})

# Fur hat: coonskin
_,_,_,fh=find("Fur hat"); fh.setdefault('t',[]).append("coonskin cap")

# ---- A1-2 jerseys
D,S,i,tj=find("Team jersey")
fb_r=[r for r in tj['r'] if r[0] in("Authentic / Replica","Match / Stadium","Retro football shirts")]
other_r=[r for r in tj['r'] if r not in fb_r]
tj['r']=other_r
tj['d']="Pullover top in a team's colours for sports without their own jersey kind here; football, basketball, ice-hockey and baseball have their own kinds, cycling jerseys are in Sports."
tj['a']="fan jersey · supporter shirt"
fbk=K("Football shirt","soccer jersey · replica shirt · football kit · kit","Team shirt of association football, sold as authentic player issue, replica or retro shirt.",W+"Football_shirt",
  t=["home / away / third","authentic (player-issue) vs replica","retro / throwback","goalkeeper shirt","long-sleeve","printed name and number"],
  x=[A("adidas Equipment","Early-1990s adidas range with chunky colour-blocked stripes across the shoulder, oversized fit and the triangular Equipment logo in place of the trefoil.","https://www.soccerbible.com/features/2026/03/adidas-equipment-an-era-defining-aesthetic/amp/",mk="adidas",y="1991",a="EQT",dt="colour blocking · shoulder stripes · EQT green accent"),
     A("adidas Ascend","Unofficial name for an Equipment-era template of about 1992–95 with conjoined sleeve stripes, a wide V-neck and a shadow triple-stripe pattern.","https://kitbliss.co.nz/100gfst/059-adidas-ascend.html",mk="adidas",y="1992",dt="wide V-neck with coloured trim · sleeve flashes"),
     A("adidas Horizon","Template of 1989–92 with a large simple V-neck, thin horizontal piping, baggy fit and large colour blocks across and under the arms.","https://www.kitbliss.co.nz/100gfst/071-adidas-horizon.html",mk="adidas",y="1989",dt="V-neck · piping · colour blocks"),
     A("Hummel halved shirt (Denmark 1986)","Denmark's halved World Cup shirt of 1986, a landmark of Hummel design.",W+"Football_shirt",mk="Hummel",y="1986",dt="two-tone halved body")],
  r=fb_r)
bk=K("Basketball jersey","basketball vest · NBA jersey","Sleeveless or sleeved team top of basketball, sold as authentic, replica or throwback.",W+"Basketball_uniform",
  t=["authentic","replica","throwback / retro","sleeved"],
  x=[A("Hardwood Classics","Mitchell & Ness line of throwback NBA jerseys, introduced in 1999.",W+"Mitchell_%26_Ness",mk="Mitchell & Ness",y="1999",dt="era-correct fabric and cut · team and season"),
     A("NBA Association, Icon, Statement and City editions","Naming system for NBA team uniforms: Association (white) and Icon (coloured) from 2017–18, with Statement and City alternates.",W+"Basketball_uniform",y="2017",dt="edition · team"),
     A("Sleeved NBA jersey","Short-sleeved NBA jersey introduced by adidas for the 2013 Christmas Day games and dropped after Nike took over.",W+"Basketball_uniform",mk="adidas",y="2013",dt="sleeve · team")],
  r=[r for r in tj['r'] if r[1]=="Mitchell & Ness"])
tj['r']=[r for r in tj['r'] if r[1]!="Mitchell & Ness"]
hk=K("Ice-hockey jersey","hockey sweater · hockey shirt","Team top of ice hockey, worn as an on-ice authentic or sold as a replica or fan jersey.",W+"Hockey_jersey",
  t=["authentic","fan / replica","alternate","throwback"],
  x=[A("Reebok Edge jersey","NHL jersey system redesigned by Reebok in 2007 with a V-neck insert.",W+"Hockey_jersey",mk="Reebok",y="2007",dt="V-neck insert · team"),
     A("adidas NHL jersey","NHL jersey line made by adidas from 2017, the subject of a 2022 lawsuit over retail quality against on-ice versions.",W+"Hockey_jersey",mk="adidas",y="2017",dt="on-ice vs retail version · team"),
     A("NHL alternate jersey","Third jersey programme begun by the NHL in 1995, including Winter Classic, Stadium Series and Reverse Retro designs.",W+"Hockey_jersey",y="1995",v=[V("Reverse Retro","Alternate series recalling past designs")],dt="special-event design · team")])
bb=K("Baseball jersey","baseball shirt · MLB jersey","Button-front or pullover team top of baseball, worn at home in white and on the road in grey or a dark colour.",W+"Baseball_uniform",
  t=["home","road","throwback","pinstripe"],
  x=[A("Mitchell & Ness wool-flannel throwback","Reproduction of vintage wool-flannel baseball uniforms, begun by Mitchell & Ness in 1983.",W+"Mitchell_%26_Ness",mk="Mitchell & Ness",y="1983",dt="wool flannel · era · team"),
     A("Pinstripe jersey","Narrow-striped jersey first worn by some major league teams in 1907 and widened in 1912; the Yankees made it a team symbol.",W+"Baseball_uniform",y="1907",dt="stripe width · team"),
     A("Nike-designed MLB jersey","MLB uniforms designed by Nike and made by Fanatics from 2024, which drew player complaints over number and lettering size.",W+"Baseball_uniform",mk="Nike",y="2024",dt="Elite vs replica · team")])
S['k'][i+1:i+1]=[fbk,bk,hk,bb]

# ---- A1-3 missing kinds
D,S,i,kilt=find("Kilt")
S['k'][i+1:i+1]=[
 K("Sporran","Highland pouch · sporran","Belt pouch worn with Highland dress, since a kilt has no pockets.",W+"Sporran",t=["day sporran (brown leather)","dress sporran (metal cantle, fur front)","semi-dress sporran","horsehair sporran (pipers and drummers)","military sporran (swinging-six, badger-head, plain leather)"]),
 K("Kilt pin","kilt brooch","Decorative pin worn on the lower corner of the kilt's outer apron to weight it; it does not fasten the layers.",W+"Kilt_pin",t=["silver","stone-set","claw brooch (grouse foot)","antler"]),
 K("Sgian-dubh","sgian dubh · skean dhu","Small single-edged knife worn tucked into the kilt hose with the hilt visible.",W+"Sgian-dubh",t=["leather sheath with silver fittings","stainless steel blade"]),
]
D,S,i,_=find("Tuxedo")
S['k'].append(K("Smoking jacket","lounge jacket · house jacket","Informal men's lounge jacket, usually velvet or silk, with a shawl collar and toggle, frog or tie-belt fastening; forerunner of the dinner jacket.",W+"Smoking_jacket",t=["velvet","silk","shawl collar","frog fastening","tie belt"]))
D,S,i,_=find("Chinos")
S['k'].append(K("Plus fours & breeks","plus-fours · shooting breeks · knickerbockers","Breeches ending below the knee, worn for golf and game shooting; plus fours hang four inches below the knee.",W+"Plus_fours",t=["plus fours","plus twos, sixes and eights","knickerbockers","shooting breeks"]))
D,S,i,_=find("Waxed cotton jacket")
S['k'].append(K("Mackinaw","Mackinaw jacket · mackinaw coat","Short double-breasted coat of thick blanket-weight wool, often red-and-black plaid, from Mackinaw cloth.",W+"Mackinaw_coat",t=["red-and-black plaid","Mackinaw cloth","double-breasted"],m=[]))

# ---- A1-4
D,S,i,cu=find("Cummerbund"); _,_,_,cs=find("Collar stay")
fa=K("Formal accessories","cummerbund · collar stay · kamarband","Small items of formal dress: the pleated waist sash worn with a dinner jacket and the strip that keeps shirt collar points flat.",W+"Cummerbund",
  t=["cummerbund: pleated silk (pleats upward)","cummerbund: black barathea or satin","cummerbund: coloured or patterned"]+["collar stay: "+t for t in cs['t']])
S['k'][i]=fa
S['k']=[k for k in S['k'] if k['n']!="Collar stay"]
D,S,i,_=find("Detachable lining or hood")
S['k'].pop(i)
_,_,_,oc=find("Overcoat"); oc['t'].append("detachable lining or hood (zip-in, button-in or stud-in)")

# ---- A1-5
D,S,i,ct=find("Corset top"); S['k'].pop(i)
D,S,i,co=find("Corset")
co['a']+=" · corset top · bustier top"
co['d']="Boned, laced garment that shapes the torso, worn under clothing or as a visible corset top or bustier."
co['t']+=["corset top / bustier (outerwear)","strapless","cropped"]
co['m']+=ct['m']
D,S,i,sw=find("Shapewear"); sw['t']=[t for t in sw['t'] if t!="bodysuit / body shaper"]
sw['d']+=" The body shaper is the Tops bodysuit with shaping."
_,_,_,bs=find("Bodysuit"); bs['a']+=" · body shaper"

# ---- A1-6 / A1-7
# Tracksuit move to Casual jackets; merge Beckenbauer/Firebird
D,S,i,ts=find("Tracksuit"); S['k'].pop(i)
D2,S2,i2,tj2=find("Track jacket")
for x in tj2['x']:
    for t in ts['x']:
        if x['n'].replace('adidas ','')==t['n'].replace('adidas ','').replace(' tracksuit',''):
            have={v['n'] for v in t['v']}
            for v in x['v']:
                if v['n'] not in have: t['v'].append(v)
tj2['x']=[x for x in tj2['x'] if x['n'] not in('adidas Beckenbauer','adidas Firebird')]
tj2['d']+=" The adidas Beckenbauer and Firebird sets are listed under Tracksuit."
S2['k'].insert(i2+1,ts)
# Bisht from Cape
_,_,_,cape=find("Cape"); cape['x']=[x for x in cape['x'] if x['n']!='Bisht']
# Swimsuit racing
_,_,_,sws=find("Swimsuit")
sws['x']=[x for x in sws['x'] if x['n'] not in('LZR Racer','Fastskin')]
sws['m']=[m for m in sws['m'] if m[0] not in('Super-body J01','Powerskin Carbon')]
sws['r']=[r for r in sws['r'] if r[0] not in('LZR Racer','Fastskin','Powerskin')]
sws['t']=[t for t in sws['t'] if not t.startswith('kneeskin')]
sws['d']+=" Competition racing suits are in Sports (E2)."
# Poncho utility types -> Raincoat
_,_,_,po=find("Poncho"); _,_,_,rc=find("Raincoat")
po['t']=[t for t in po['t'] if t not in("Rain poncho (waterproof)","Army / military poncho","Cycling poncho")]
rc['t']+=["rain poncho","army / military poncho","cycling poncho"]
# Tweed patterns
_,_,_,tw=find("Tweed cloth")
tw['x']=[x for x in tw['x'] if x['n'] not in('Glen plaid','Houndstooth')]
tw['t']+=["glen plaid (pattern)","houndstooth (pattern)"]
# sari cloth duplicates
for kn,rem in (("Ikat cloth",("Patola","Pochampally ikat")),("Khadi & handloom cloth",("Jamdani","Chanderi"))):
    _,_,_,kk=find(kn); kk['x']=[x for x in kk['x'] if x['n'] not in rem]
    kk['d']=kk['d'].rstrip('.')+". "+" and ".join(rem).replace(' ikat','')+" are listed under Sari."

# ---- A1-8 register hygiene
REN={"Levi Strauss & Co.":"Levi's","Adidas":"adidas","André Courrèges":"Courrèges"}
def walk(o):
    if isinstance(o,dict):
        if o.get('mk') in REN: o['mk']=REN[o['mk']]
        for k in ('m','r'):
            if k in o and isinstance(o[k],list):
                for p in o[k]:
                    if isinstance(p,list) and len(p)==2 and p[1] in REN: p[1]=REN[p[1]]
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
b=br['b']; byn={x['n']:x for x in b}
lv,ls=byn["Levi's"],byn["Levi Strauss & Co."]
for f in('lines','eras','sig','sc','rel'):
    for v in ls.get(f,[]):
        if v not in lv.setdefault(f,[]): lv[f].append(v)
lv['rel']=[r for r in lv['rel'] if r not in("Levi's","Levi Strauss & Co.")]
lv['d']=lv['d']+" Its first western shirt was the 1926 Cowboy Overall Shirt."
b.remove(ls)
for x in b:
    x['rel']=[("Levi's" if r=="Levi Strauss & Co." else r) for r in x.get('rel',[])]
have={x['n'].lower() for x in b}
if 'orchard corset' not in have:
    b.append({"n":"Orchard Corset","c":"United States","f":"","seg":"Specialist","d":"Wenatchee, Washington retailer of steel-boned corsets sold by curve and length.","lines":["CS series"],"eras":[],"sig":["Orchard Corset CS series"],"sc":["corsetry"],"rel":[],"s":"https://www.orchardcorset.com/collections/underbust-corsets","kf":"steel-boned corsets"})
if 'fanatics' not in have:
    b.append({"n":"Fanatics","c":"United States","f":"2011","seg":"Athletic & sportswear","d":"US maker and seller of licensed sports merchandise, trading cards and collectibles.","lines":["Breakaway"],"eras":[],"sig":[],"sc":["sports fan"],"rel":[],"s":W+"Fanatics_(company)","kf":"licensed sportswear"})
# traditions merge
T=tr['t']; tn={x['n']:x for x in T}
def merge(keep,drop,**over):
    a,bb_=tn[keep],tn[drop]
    for f in('forms','ctr'):
        for v in bb_.get(f,[]):
            if v not in a.setdefault(f,[]): a[f].append(v)
    for f in('auth','tech','mat'):
        if not a.get(f) and bb_.get(f): a[f]=bb_[f]
    a.update(over); T.remove(bb_)
merge("Donegal tweed","Donegal tweed weaving")
merge("Loden","Loden cloth")
merge("Shemma weaving","Ethiopian shemma weaving")
merge("Bisht","Hasawi bisht making",r="Arabian Peninsula and Arab world; Al-Ahsa, Saudi Arabia and Kuwait for Hasawi bisht",d="Men's ceremonial cloak of camel hair or wool worn over the thobe; Hasawi bisht from Al-Ahsa is hand-made with zari edging (skills UNESCO-listed 2025).",mat="Camel hair, goat wool, wool, linen; gold and silver thread",auth="Hand finishing; pure gold-thread trim ranks highest.")
# fix forms referencing
for t in T:
    t['forms']=[f for f in t.get('forms',[])]

out='/home/user/Possession-Taxonomy/rebuild/out/'
for name,obj in (('A1.json',d),('A1_brands.json',br),('A1_traditions.json',tr),('A1_moves.json',mv)):
    json.dump(obj,open(out+name+'.tmp','w'),ensure_ascii=False,indent=1 if name=='A1.json' else None)
    os.replace(out+name+'.tmp',out+name)
print('ok')
