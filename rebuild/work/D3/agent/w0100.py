import json, os
p='/home/user/Possession-Taxonomy/rebuild/work/D3/shelves/01_00.json'
WP='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),vv)) for vv in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Bookshelf speakers","a":"standmount speaker · monitor speaker","d":"Compact speaker cabinet made to stand on a stand, shelf or desk, passive or active.",
 "t":["passive","active (powered)","wireless/streaming","sealed (acoustic suspension)","ported"],"s":"https://www.richersounds.com/hi-fi",
 "x":[
  X("BBC LS3/5A","","1974",WP+"LS3/5A","BBC-designed miniature monitor for outside-broadcast vans, built under licence by many makers.",
    [("Rogers LS3/5A","Rogers","1975","earliest licensee"),("Spendor LS3/5A","Spendor","",""),("Audiomaster LS3/5A","Audiomaster","",""),("Harbeth LS3/5A","Harbeth","",""),("KEF LS3/5A","KEF","1994",""),("11-ohm version","","1987","KEF-redesigned drivers and crossover"),("Stirling Broadcast LS3/5A V2","Stirling Broadcast","2005",""),("Falcon LS3/5A (15 ohm)","Falcon Acoustics","2014","current licence")],dt="15 or 11 ohm · KEF B110 and T27 drivers · veneer"),
  X("Spendor BC1","Spendor","1969",WP+"Spendor","Bextrene-cone BBC-school monitor by Spencer Hughes, made until 1994 and reborn in the Classic range.",
    [("BC1","Spendor","1969",""),("BC2","Spendor","",""),("BC3","Spendor","",""),("SP1","Spendor","",""),("Classic SP1/2R2","Spendor","2011","current BC1 descendant")]),
  X("Harbeth HL Monitor","Harbeth","1977",WP+"Harbeth_Audio_Limited","First Harbeth speaker, with Dudley Harwood's patented polypropylene cone.",
    [("HL Monitor","Harbeth","1977",""),("Super HL5plus","Harbeth","","")]),
  X("Acoustic Research AR-1 / AR-3","Acoustic Research","1954",WP+"Acoustic_Research","Sealed acoustic-suspension speakers that made deep bass possible from a small box.",
    [("AR-1","Acoustic Research","1954","first acoustic suspension"),("AR-2","Acoustic Research","1957",""),("AR-3","Acoustic Research","1958","first dome midrange"),("AR-3a","Acoustic Research","1969","")]),
  X("The Advent Loudspeaker","Advent","1968",WP+"Advent_Corporation","Henry Kloss's affordable two-way with a 10-inch woofer, later called the Larger Advent.",
    [("Advent Loudspeaker (Larger Advent)","Advent","",""),("Smaller Advent","Advent","",""),("Advent/2","Advent","","")]),
  X("JBL 4310 / L100","JBL","1968",WP+"JBL","Three-way control monitor and its 1970s best-selling home version.",
    [("4310","JBL","1968","studio control monitor"),("L100","JBL","1969","consumer version"),("4311","JBL","",""),("4300 series","JBL","1973","")]),
  X("ProAc Tablette","ProAc","1979","https://www.proac-loudspeakers.com/proac-tablette","Very small two-way monitor designed in 1976, made in many versions.",
    [("Tablette","ProAc","1979",""),("Super Tablette","ProAc","",""),("Tablette Anniversary","ProAc","",""),("Tablette 10 Signature","ProAc","","current")]),
  X("KEF LS50","KEF","2012",WP+"KEF","50th-anniversary Uni-Q coaxial standmount that brought the LS3/5A idea into the living room.",
    [("LS50","KEF","2012",""),("LS50 Wireless","KEF","2017","first KEF wireless hi-fi speaker"),("KEF LS50 Meta","KEF","","Metamaterial Absorption Technology"),("KEF LS50 Wireless II","KEF","","")]),
  X("Genelec active monitors","Genelec","1978",WP+"Genelec","Finnish active studio monitors also bought by home listeners, including the home G series.",
    [("S30","Genelec","1978","original Triamp"),("1031A","Genelec","1991",""),("8030A","Genelec","2005",""),("8040A","Genelec","2005",""),("8341A (The Ones)","Genelec","","coaxial"),("G Three","Genelec","","home series")]),
 ],
 "m":[["Magnat Signature Edelstein","Magnat"],["Polk Audio Reserve R200","Polk Audio"],["Polk Audio Signature Elite ES20","Polk Audio"],["Polk Audio Monitor XT20","Polk Audio"],["Technics SC-CX700","Technics"]],
 "r":[["Reserve Series","Polk Audio"],["Signature Elite Series","Polk Audio"],["Monitor XT Series","Polk Audio"]]},
{"n":"Floor-standing speakers","a":"tower speaker · floorstander","d":"Tall speaker cabinet that stands on the floor.","t":["passive","active/wireless","dual-concentric"],"s":"https://www.richersounds.com/hi-fi",
 "x":[
  X("Bowers & Wilkins 800 series","Bowers & Wilkins","1979",WP+"Bowers_%26_Wilkins","Flagship three-way monitor line used at Abbey Road, from the 801 to the Diamond-tweeter 800D.",
    [("801","Bowers & Wilkins","1979",""),("Matrix 801","Bowers & Wilkins","1987","Matrix honeycomb cabinet"),("Nautilus 800 series","Bowers & Wilkins","1998",""),("800D range","Bowers & Wilkins","2005","replaced Nautilus 800")]),
  X("Bowers & Wilkins Nautilus","Bowers & Wilkins","1993",WP+"Bowers_%26_Wilkins","Spiral-shell four-way flagship with tapered-tube driver loading."),
  X("Linn Isobarik","Linn","1975",WP+"Linn_Products","Floor-standing speaker using Linn's patented isobaric bass loading.",
    [("Isobarik","Linn","1975",""),("Isobarik DMS","Linn","","built-in crossover")]),
  X("Wilson Audio WATT/Puppy","Wilson Audio","1986",WP+"Wilson_Audio","Tiny monitor (WATT) on a bass module (Puppy) that became the best-known high-end floor system.",
    [("WATT Series 1","Wilson Audio","1986",""),("WATT Series 8","Wilson Audio","2006",""),("Sasha W/P","Wilson Audio","2009",""),("Sasha V","Wilson Audio","2023",""),("WATT/Puppy (2024)","Wilson Audio","2024","")]),
  X("Wilson Audio WAMM / Alexandria / Alexx","Wilson Audio","1981",WP+"Wilson_Audio","Wilson's modular cost-no-object flagships.",
    [("WAMM Series 1","Wilson Audio","1981",""),("Alexandria X-2","Wilson Audio","2003",""),("Alexandria XLF","Wilson Audio","2012",""),("Alexx","Wilson Audio","2016",""),("Chronosonic XVX","Wilson Audio","2019",""),("WAMM Master Chronosonic","Wilson Audio","2017","")]),
  X("Bose 901","Bose","1968",WP+"Bose_901","Direct/reflecting speaker with nine 4.5-inch drivers and an active equaliser.",
    [("901 Series II","Bose","",""),("901 Series VI","Bose","","discontinued 2016")]),
  X("KEF Blade","KEF","2011",WP+"KEF","Single Apparent Source flagship with Uni-Q and force-cancelling woofers."),
  X("Tannoy Prestige dual concentric","Tannoy","",WP+"Tannoy","Tannoy's flagship home range built around its Dual Concentric driver, tweeter behind the bass cone."),
 ],
 "m":[["KEF LS60 Wireless","KEF"],["Klipsch RP-6000F II","Klipsch"],["Klipsch RP-8000F II","Klipsch"],["Polk Audio Signature Elite ES55","Polk Audio"],["Polk Audio Monitor XT60","Polk Audio"],["Polk Audio T50","Polk Audio"],["Sonus faber Sonetto VIII G2","Sonus faber"]],
 "r":[["Reference Premiere","Klipsch"],["Signature Elite Series","Polk Audio"],["Monitor XT Series","Polk Audio"],["T Series","Polk Audio"]]},
{"n":"Electrostatic and planar loudspeakers","a":"electrostat · panel speaker · magnetostatic · ribbon speaker","d":"Loudspeaker driven by a large thin film panel, electrostatic or planar-magnetic, usually radiating front and back.",
 "t":["full-range electrostatic","hybrid electrostatic","planar-magnetic (quasi-ribbon)","true ribbon"],"s":WP+"Magnepan",
 "x":[
  X("Quad ESL","Quad","1957",WP+"Quad_Electroacoustics","First production full-range electrostatic loudspeaker.",
    [("ESL (ESL-57)","Quad","1957","original"),("ESL-63","Quad","1981","concentric-ring stator, delay lines"),("988 / 989","Quad","",""),("2805 / 2905","Quad","",""),("2812 / 2912","Quad","","")]),
  X("Magnepan Magneplanar","Magnepan","1972",WP+"Magnepan","Thin dipole planar-magnetic panels from Minnesota.",
    [("MG-I","Magnepan","1972",""),("Tympani I","Magnepan","1973",""),("MG-III","Magnepan","1983","ribbon tweeter"),("MMG","Magnepan","1990",""),("1.7i","Magnepan","2010",""),("3.7i","Magnepan","2013",""),("20.7","Magnepan","2011",""),("30.7","Magnepan","2017",""),("LRS","Magnepan","2019","")]),
  X("MartinLogan hybrid electrostats","MartinLogan","1983",WP+"MartinLogan","Curved CLS electrostatic panels joined to dynamic woofers.",
    [("Monolith","MartinLogan","1983","shown at CES"),("Statement e2","MartinLogan","",""),("Summit","MartinLogan","2005","XStat transducer")]),
  X("Bowers & Wilkins DM70","Bowers & Wilkins","1970",WP+"Bowers_%26_Wilkins","Electrostatic mid/treble panel on a conventional bass unit."),
 ]},
{"n":"Horn loudspeakers","a":"horn speaker · horn-loaded speaker","d":"Home loudspeaker whose drivers fire through horns for high efficiency, often suited to low-power valve amplifiers.",
 "t":["fully horn-loaded","horn with direct-radiating woofer","corner horn","spherical horn"],"s":WP+"Klipschorn",
 "x":[
  X("Klipschorn","Klipsch","1946",WP+"Klipschorn","Three-way corner horn using the room walls as horn extensions, made in Hope, Arkansas since 1946.",
    [("Klipschorn","Klipsch","1946",""),("60th Anniversary Klipschorn","Klipsch","2006",""),("70th Anniversary Klipschorn","Klipsch","2016","enclosed horn, 70 pairs")]),
  X("Klipsch Heritage series","Klipsch","",WP+"Klipschorn","Klipsch's horn-loaded siblings of the Klipschorn.",
    [("La Scala II","Klipsch","","fully horn-loaded"),("Belle Klipsch","Klipsch","","fully horn-loaded"),("Cornwall IV","Klipsch","","horns plus direct woofer"),("Heresy IV","Klipsch","",""),("Forte IV","Klipsch","","")]),
  X("Altec Lansing Voice of the Theatre","Altec Lansing","1945","https://www.theatrecrafts.com/bhc/equipment/altec-lansing-voice-of-the-theatre","Two-way cinema horn systems later used in studios and homes.",
    [("A-1","Altec Lansing","1945",""),("A-5","Altec Lansing","1945",""),("A-7","Altec Lansing","1966",""),("Legacy A-7","Altec Lansing","2003","reissue")]),
  X("Avantgarde Duo / Trio","Avantgarde Acoustic","",
    "https://stereophile.com/content/avantgarde-acoustic-duo-loudspeaker","Spherical-horn speakers with active woofers: two-way Duo and three-way Trio.",
    [("Trio","Avantgarde Acoustic","","three-way"),("Duo","Avantgarde Acoustic","","two-way horn, active woofer")]),
 ]},
{"n":"Subwoofer","a":"sub · bass speaker","d":"Speaker that reproduces only bass.","t":["active","passive","wireless","sealed","ported"],"s":"https://www.richersounds.com/hi-fi",
 "m":[["SVS SB-2000 Pro","SVS"],["REL No. 35","REL"],["KEF KC62","KEF"],["Bowers & Wilkins DB3D","Bowers & Wilkins"],["Bowers & Wilkins ASW610XP","Bowers & Wilkins"],["Klipsch THX-1200-SW","Klipsch"],["Klipsch Flexus Sub 200","Klipsch"],["Cambridge Audio MINX X301","Cambridge Audio"],["Sonos Sub 4","Sonos"],["Sonos Sub Mini","Sonos"],["Bluesound Pulse Sub+","Bluesound"],["Sennheiser Ambeo Sub","Sennheiser"]]},
]
def B(n,c,f,seg,kf,d,s,sig=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=list(sig)
    return b
brands=[
 B("KEF","United Kingdom","1961","Premium","Uni-Q speakers","Maidstone speaker maker founded by Raymond Cooke.",WP+"KEF",["LS50","Blade","LS3/5A"]),
 B("Bowers & Wilkins","United Kingdom","1966","Professional & flagship","800 series","Worthing speaker maker founded by John Bowers and Roy Wilkins.",WP+"Bowers_%26_Wilkins",["801","Nautilus"]),
 B("Klipsch","United States","1946","Premium","horn speakers","Hope, Arkansas maker founded by Paul W. Klipsch.",WP+"Klipschorn",["Klipschorn","La Scala","Heresy"]),
 B("JBL","United States","1946","Mainstream","studio monitors","Los Angeles speaker maker founded by James B. Lansing.",WP+"JBL",["L100","4310"]),
 B("Quad","United Kingdom","1936","Heritage manufactory","electrostatic speakers","British maker founded by Peter Walker; first full-range electrostatic speaker.",WP+"Quad_Electroacoustics",["ESL","ESL-63"]),
 B("Acoustic Research","United States","1954","Heritage manufactory","acoustic suspension","Cambridge, Massachusetts maker founded by Edgar Villchur and Henry Kloss.",WP+"Acoustic_Research",["AR-3","AR XA"]),
 B("Advent","United States","1967","Heritage manufactory","affordable speakers","Henry Kloss's Cambridge, Massachusetts company.",WP+"Advent_Corporation",["Advent Loudspeaker"]),
 B("Tannoy","United Kingdom","1926","Heritage manufactory","dual concentric","London-founded speaker maker, now in the Music Tribe group.",WP+"Tannoy",["Prestige"]),
 B("Magnepan","United States","1969","Specialist","planar speakers","White Bear Lake, Minnesota maker of planar-magnetic panels.",WP+"Magnepan",["MG","LRS"]),
 B("MartinLogan","United States","1979","Specialist","hybrid electrostatics","Lawrence, Kansas maker of curvilinear electrostatic speakers.",WP+"MartinLogan",["Monolith"]),
 B("Harbeth","United Kingdom","1977","Artisan & independent","BBC-school monitors","Founded by ex-BBC engineer Dudley Harwood; owned by Alan Shaw since 1986.",WP+"Harbeth_Audio_Limited",["HL Monitor","LS3/5A"]),
 B("Spendor","United Kingdom","1969","Artisan & independent","BBC-school monitors","East Sussex maker founded by Spencer and Dorothy Hughes.",WP+"Spendor",["BC1"]),
 B("Rogers","United Kingdom","","Heritage manufactory","LS3/5A","Earliest LS3/5A licensee.",WP+"LS3/5A",["LS3/5A"]),
 B("Falcon Acoustics","United Kingdom","","Artisan & independent","LS3/5A","Holds the current 15-ohm LS3/5A licence.",WP+"LS3/5A",["LS3/5A"]),
 B("Wilson Audio","United States","1974","Professional & flagship","high-end speakers","Founded by David and Sheryl Lee Wilson; based in Provo, Utah.",WP+"Wilson_Audio",["WATT/Puppy","Alexandria"]),
 B("Linn","United Kingdom","1972","Premium","LP12, streaming","Glasgow hi-fi maker founded by Ivor Tiefenbrun.",WP+"Linn_Products",["Isobarik","Sondek LP12"]),
 B("Genelec","Finland","1978","Professional & flagship","active monitors","Iisalmi maker of active studio monitors.",WP+"Genelec",["8030","1031A"]),
 B("Bose","United States","1964","Premium","direct/reflecting","American audio company.",WP+"Bose_901",["901"]),
 B("Altec Lansing","United States","","Heritage manufactory","cinema horns","Maker of the Voice of the Theatre horn systems.","https://www.theatrecrafts.com/bhc/equipment/altec-lansing-voice-of-the-theatre",["A-7"]),
 B("Avantgarde Acoustic","Germany","","Specialist","spherical horns","German maker of spherical-horn loudspeakers.","https://stereophile.com/content/avantgarde-acoustic-duo-loudspeaker",["Duo","Trio"]),
 B("ProAc","United Kingdom","1979","Artisan & independent","small monitors","Stewart Tyler's speaker company, grown from Celef.","https://www.proac-loudspeakers.com/proac-tablette",["Tablette"]),
 B("Wharfedale","United Kingdom","1932","Mainstream","value hi-fi speakers","Founded by Gilbert Briggs as Wharfedale Wireless Works.",WP+"Wharfedale_(company)"),
 B("Sonus faber","Italy","1983","Premium","wood-cabinet speakers","Arcugnano maker founded by Franco Serblin.",WP+"Sonus_Faber",["Aida"]),
 B("Dynaudio","Denmark","1977","Premium","speakers","Skanderborg speaker maker.",WP+"Dynaudio"),
 B("Polk Audio","United States","1972","Mainstream","value speakers","Baltimore speaker maker.","knowledge"),
 B("SVS","United States","","Specialist","subwoofers","American direct-sale subwoofer and speaker maker.","knowledge"),
 B("REL","United Kingdom","","Specialist","subwoofers","British subwoofer maker.","knowledge"),
]
notes=("Polk/Klipsch SKU lists trimmed (Polk XT15, R100, ES15, XT70, Klipsch RP-5000F II, RP-8060FA II dropped as near-duplicates); subwoofers trimmed from 19 to 12 (dropped B&W ASW608/DB2D, Cambridge MINX X201/MSX SUB 200/300, Klipsch Flexus Sub 100, Denon Home Subwoofer). "
 "Brief items not attested on any retrieved page and so left out: Harbeth P3/Compact 7/M30/M40, Wharfedale Denton/Linton, Tannoy Westminster/Autograph (Tannoy page names only Prestige), Sonus faber Electa Amator/Guarneri, Dynaudio models, B&W 600 series and 800 D4, JBL L100 Century/Classic, Avantgarde years (no dated page). LS3/5A has no single maker so mk is empty and licensees are versions. Tannoy dual-concentric placed under Floor-standing rather than Horn.")
t=p+'.tmp'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
