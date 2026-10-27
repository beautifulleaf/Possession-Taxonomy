import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E5/agent')
from write import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":q[1],"y":q[2],"d":q[3]} for q in v],"dt":dt}
def B(n,c,f,seg,kf,d,s,sig=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}
    if sig: b["sig"]=list(sig)
    if rel: b["rel"]=list(rel)
    b["s"]=s; return b
RA=W+'Rhythm_game_accessories'; RO='RedOctane'; MC='Mad Catz'; K='Konami'; N='Nintendo'; S='Sony'
gtr={"n":"Guitar controller","a":"Guitar Hero guitar · Rock Band guitar","d":"Guitar-shaped controller with fret buttons and a strum bar for rhythm games.",
 "t":["five-fret guitar","six-button guitar","bass","Pro guitar with real strings or frets"],"s":RA,"x":[
 X("Guitar Hero guitar","Guitar Hero controller","RedOctane's five-fret guitar controllers styled on Gibson models, from the SG to the Les Paul.",RO,"",RA,
   [("Guitar Hero SG controller",RO,"","PlayStation 2; miniature Gibson SG"),("Guitar Hero X-plorer",RO,"","Xbox 360, PC and Mac; based on the Gibson Explorer"),("Guitar Hero Les Paul controller",RO,"","PS3, Wii, Xbox 360; Les Paul Wireless Controller for Xbox 360 is model 95339.805"),("Guitar Hero Guitar Controller for Wii U","","","")],"wired or wireless · platform"),
 X("Rock Band guitar","Rock Band Stratocaster","Fender- and Beatles-styled five-fret guitars and basses sold for the Rock Band series.","","",RA,
   [("Rock Band Stratocaster guitar controller","","",""),("Rock Band 2 guitar controller","","",""),("Rock Band Fender Precision bass controller",MC,"2008",""),("Mad Catz Telecaster guitar controller",MC,"",""),("Rickenbacker 325 guitar controller","","","Beatles series"),("Gretsch Duo Jet guitar controller","","","Beatles series"),("Hofner 500/1 bass controller","","","Beatles series")]),
 X("Rock Band Pro guitar","Fender Pro Guitar","Fender guitars for Rock Band 3 Pro mode that read real fret positions.","Fender","2010",RA,
   [("Fender Mustang Pro Guitar","Fender","2010","shown at E3 2010"),("Squier Stratocaster Pro Guitar","Fender","2010","real strings")])],
 "m":[["You Rock Guitar","You Rock Digital"]]}
drm={"n":"Drum kit controller","a":"Guitar Hero drums · Rock Band drums","d":"Drum-pad kit with kick pedal for rhythm games.","t":["four-pad kit","five-pad kit","cymbal add-on"],"s":RA,"x":[
 X("Rock Band drum kit","","Four-pad drum kit with kick pedal for the Rock Band series; cymbals were added for Pro mode.","","",RA,
   [("Rock Band drum kit","","","4 pads"),("Rock Band 2 drum kit","","","4 pads"),("The Beatles: Rock Band drum kit","","","Ludwig branding"),("Rock Band portable drum kit",MC,"",""),("Rock Band Pro cymbals","","","add-on")]),
 X("Guitar Hero drum kit","","Guitar Hero drum kit with raised cymbal pads and a MIDI input.",RO,"",RA,
   [("Guitar Hero World Tour drum kit",RO,"","MIDI input"),("Guitar Hero wireless drum controller (PS3)","Logitech","2009","")])],
 "m":[["ION Drum Rocker",""]]}
oth={"n":"Turntable, drum and other rhythm controller","a":"turntable controller · taiko drum · bongos · maracas · keyboard controller","d":"Instrument-shaped controller other than a guitar or drum kit, made to play a rhythm game.",
 "t":["turntable","hand drum","maracas or tambourine","keyboard","baton"],"s":RA,"x":[
 X("beatmania turntable controller","BeatMania controller","Konami's keys-and-turntable controller for its DJ rhythm series.",K,"",RA,[("BeatMania turntable controller",K,"","")]),
 X("DJ Hero turntable","","Turntable controller with crossfader and effects for the DJ Hero series.","","2009",RA,
   [("DJ Hero turntable controller","","2009",""),("Xbox 360 Wireless Turntable Controller","","","")]),
 X("DK Bongos","Taru Konga","Pair of barrel-shaped bongo drums with a clap microphone, for the GameCube.",N,"",W+"Donkey_Konga",
   [("Taru Konga (DK Bongos)",N,"","")]),
 X("Taiko drum controller","Taiko no Tatsujin drum","Japanese taiko-style drum controller struck with sticks.","","",RA,[("Taiko no Tatsujin drum controller","","","Japan")]),
 X("Samba de Amigo maracas","","Pair of maraca controllers for the Sega Dreamcast.","","",RA,[("Samba de Amigo maracas","","","Dreamcast")])],
 "m":[["DrumMania controller",K],["GuitarFreaks controller",K],["Pop'n Music controller",K],["Rock Band 3 Wireless Pro Keyboard",MC],["Rock Band MIDI Pro-Adapter",MC],["Shakatto Tambourine",""],["Mad Maestro baton controller",""]]}
dan={"n":"Dance or balance mat","a":"dance pad · dance mat · balance board","d":"Floor mat, pad or board that reads the player's steps or weight as game input.","t":["soft pad","hard metal pad","arcade stage","balance board"],"s":W+"Dance_pad","x":[
 X("Power Pad","Family Trainer · Family Fun Fitness","Bandai's floor mat controller for the Famicom and NES, renamed Power Pad by Nintendo in North America.","Bandai","1986",W+"Power_Pad",
   [("Family Trainer","Bandai","1986","Famicom, Japan"),("Family Fun Fitness","Bandai","1987","North America; Europe 1988"),("Power Pad (Family Trainer)",N,"1988","North American rename")]),
 X("Dance Dance Revolution dance pad","DDR pad","Konami's four-arrow soft dance pad for home versions of its dance series.",K,"",W+"Dance_pad",[("Dance Dance Revolution dance pad",K,"","soft pad")]),
 X("L-TEK dance pad","","Hard dance pad made for home use.","L-TEK","",W+"Dance_pad",[("L-TEK Core","L-TEK","",""),("L-TEK Prime","L-TEK","","")]),
 X("Wii Balance Board","","Board with four pressure sensors that reads weight and centre of balance over Bluetooth.",N,"2007",W+"Wii_Balance_Board",
   [("Wii Balance Board",N,"2007","Japan; Europe and North America 2008")],"four AA batteries")],
 "m":[["StepManiaX Stage","StepManiaX"],["ParaPara Paradise controller",K],["Wii Mat Controller","Bandai Namco Entertainment"]]}
mic={"n":"Game microphone","a":"SingStar type","d":"Microphone made and sold to plug into a console as game input, for singing or voice commands. A headset is in Audio & Video; a speech microphone sold for computers is in Computers & Components.",
 "t":["wired USB","wireless"],"s":W+"SingStar","x":[
 X("SingStar microphones","","Red and blue microphone pair for Sony's karaoke series, later sold as a wireless set.",S,"2004",W+"SingStar",
   [("SingStar Microphones",S,"2004","wired red and blue pair through one USB converter"),("Wireless SingStar Microphones",S,"2009","2.4 GHz USB receiver; PS2 and PS3")])],
 "m":[["Xbox 360 Wireless Microphone","Microsoft"],["Voice Recognition Unit",N],["Dreamcast Microphone","Sega"],["Nintendo 64 Mic",""]]}
br=[B(RO,"United States","","Specialist","rhythm-game guitars","Accessory maker behind the Guitar Hero guitar controllers; closed by Activision in 2010.","knowledge",["Guitar Hero guitar","Guitar Hero drum kit"],["Activision"]),
 B("Fender","United States","1946","Professional & flagship","electric guitars","US guitar maker; made Pro guitar controllers for Rock Band 3.","knowledge",["Rock Band Pro guitar"]),
 B(K,"Japan","1969","Mainstream","games","Japanese game publisher; Bemani rhythm controllers and DDR pads.","knowledge",["beatmania turntable controller","Dance Dance Revolution dance pad"]),
 B(N,"Japan","1889","Mainstream","consoles","Japanese console maker; DK Bongos and Wii Balance Board.","knowledge",["DK Bongos","Wii Balance Board"]),
 B("Bandai","Japan","1950","Mainstream","toys","Japanese toy company that made the Family Trainer mat.","knowledge",["Power Pad"]),
 B("L-TEK","","","Specialist","hard dance pads","Maker of hard dance pads.",W+"Dance_pad",["L-TEK dance pad"]),
 B(S,"Japan","1946","Mainstream","consoles","Japanese electronics group; SingStar microphones.","knowledge",["SingStar microphones"])]
w('E5','02_04',{"kinds":[gtr,drm,oth,dan,mic],"brands":br,"traditions":[],
 "notes":"All five old kinds kept; 'Other rhythm controllers' renamed 'Turntable, drum and other rhythm controller'. Guitar: 14 models grouped into Guitar Hero, Rock Band and Rock Band Pro archetypes (You Rock Guitar left in m). Drums: Rock Band and Guitar Hero kits. Other: beatmania and DJ Hero turntables, DK Bongos, taiko, maracas as archetypes; Konami Bemani controllers, Pro keyboard and MIDI adapter in m. Dance: Power Pad lineage (Family Trainer, Family Fun Fitness), DDR pad, L-TEK, Wii Balance Board. Microphones: SingStar wired and wireless. Old retailer kind sources replaced with Wikipedia pages. Rock Band guitar/drum originating maker not stated on retrieved pages, so mk left blank. No StepManiaX or L-TEK maker page fetched; L-TEK country not recorded."})
