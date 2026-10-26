import json, os
W='https://en.wikipedia.org/wiki/'
def V(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def X(n,a,d,mk,y,s,v=(),dt=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(v),"dt":dt}
kit={"n":"Acoustic drum kit","a":"drum set · drum kit · trap set · shell pack",
 "d":"Set of acoustic drums (and usually cymbals and hardware) played by one drummer.",
 "t":["shell pack (drums only)","complete kit with hardware and cymbals","bop / jazz sizes","fusion sizes","rock sizes","maple shells","birch shells","mahogany shells","acrylic shells","mixed-wood shells","junior kit"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("Gretsch USA Custom","Round Badge","Gretsch's American-made flagship kit, the basis of 'That Great Gretsch Sound'.","Gretsch","","https://gretschdrums.com/drums/usa-custom",[],"6-ply maple/gum shells · 30° bearing edge · Silver Sealer interior · built in Ridgeland, South Carolina"),
  X("Ludwig Vistalite","Vistalite · acrylic kit","Ludwig's acrylic-shell kit of 1972, popularised by John Bonham's amber set.","Ludwig","1972",W+"Vistalite_Drums",
    [V("Original Vistalite","Ludwig","1972","clear, blue, green, red, amber, yellow"),V("Rainbow (e.g. Tequila Sunrise)","Ludwig","1976","multicoloured stripe shells"),V("Tivoli Vistalite","Ludwig","1978","light bulbs inside shells"),V("Reissue","Ludwig","2001","thicker shells, 45° edge; best seller the Bonham amber five-piece replica")],
    "shell colour and pattern · configuration"),
  X("Ludwig Classic Maple","Classic Maple","Ludwig's all-maple professional kit and snare line.","Ludwig","","https://drumcenternh.com/products/ludwig-classic-maple-snare-drum-14x6-5-natural-ls403xx0n",[],"all-maple shells · finish · sizes"),
  X("Rogers Holiday","Holiday","Rogers model of tom-toms and bass drums.","Rogers","",W+"Rogers_Drums",[],"often paired with Swiv-O-Matic hardware"),
  X("Yamaha Recording Custom","YD9000 · 9000 series · RC","Yamaha's all-birch kit of 1975, widely used in studios; reissued with Steve Gadd's input.","Yamaha","1975","https://downbeat.com/jazzschool/detail/yamaha-recording-custom-series",
    [V("9000 series (YD9000)","Yamaha","1975","original all-birch kit"),V("Recording Custom reissue","Yamaha","2016","6-ply North American birch, 30° edge; developed with Steve Gadd")],
    "birch shells · finish · configuration"),
  X("Tama Imperialstar","Imperial Star","Tama's original 1974 flagship kit, played by Stewart Copeland in the Police.","Tama","1974","https://www.shimamura.co.jp/update/?p=4630",[],""),
  X("Tama Superstar","Superstar","Tama birch kit developed in 1976 with 9 mm six-ply shells, played by Billy Cobham.","Tama","1976","https://www.shimamura.co.jp/update/?p=4630",[],"birch shells · finish"),
  X("DW Collector's Series","Collector's","Drum Workshop's top kit line with Timbre Matched shells tuned in pitch families.","Drum Workshop","1980s","https://articles.roland.com/on-the-drums-dw-sonic-philosophy/",
    [V("Tommy Lee touring kit","Drum Workshop","1989","Mötley Crüe Dr. Feelgood tour")],"shell construction VLT · HVLT · VLX · HVX · X-Shell · finish"),
  X("Pearl Export","Export · EXX","Pearl's most popular series and the best-selling drum set line; one millionth kit made in 1995.","Pearl","",W+"Pearl_Drums",
    [V("One millionth Export","Pearl","1995",""),V("Export EXX","Pearl","2013","described as the best-selling drum set of all time")],"complete kit · finish"),
  X("Pearl Masters","Masters · MCX · Masters Premium","Pearl line introduced in 1993.","Pearl","1993",W+"Pearl_Drums",[V("MCX and Masters Premium","Pearl","2007","line split into two")],"shell wood · finish"),
  X("Pearl Session","Session · Session Studio Classic","Pearl's mid-professional line of 1991–2006, revived in 2012.","Pearl","1991",W+"Pearl_Drums",[V("Session Studio Classic","Pearl","2012","reintroduction")],""),
  X("Pearl Reference","Reference","Pearl professional line with blended maple, birch and African mahogany shells.","Pearl","",W+"Pearl_Drums",[],"blended-wood shells by drum size"),
  X("Pearl Masterworks","Masterworks","Pearl's handmade flagship with customer-chosen plies, hardware and finish.","Pearl","",W+"Pearl_Drums",[],"wood plies · hardware · finish to order"),
  X("Sonor Signature","Signature · Horst Link Signature","Sonor kit line named on the maker's Horst Link history page, alongside the Phonic.","Sonor","",'https://www.sonor.com/drums/news/news-detail/happy-birthday-horst-link',[V("Phonic","Sonor","","")],""),
 ]}
snare={"n":"Snare drum","a":"snare · side drum","d":"Shallow double-headed drum with snare wires across the lower head.",
 "t":["brass shell","aluminium shell","steel shell","bronze shell","maple shell","birch shell","solid or steam-bent shell","piccolo (3–4 in deep)","standard (5–5.5 in)","deep (6.5 in and over)","field / marching snare"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("Ludwig Black Beauty","Black Beauty · LB416","Ludwig brass-shell snare with black-nickel finish, first made in the 1920s and revived in 1977.","Ludwig","1920s","https://www.bonedo.de/artikel/snare-vergleich-ludwig-black-beauty-vs-supraphonic-vs-acrolite/",
    [V("Original engraved Black Beauty","Ludwig","1920s",""),V("Reintroduction","Ludwig","1977","brass; bronze shells in the late 1980s, brass again from 1994"),V("LB416 14×5","Ludwig","","P85AC strainer")],"shell brass 1.2 mm · depth · engraving"),
  X("Ludwig Supraphonic","LM400 · Super Ludwig · Supra","Ludwig's chrome-finished metal snare, launched in 1958 as the Super Ludwig; the LM400 is the standard 14×5.","Ludwig","1958","https://www.bonedo.de/artikel/snare-vergleich-ludwig-black-beauty-vs-supraphonic-vs-acrolite/",
    [V("Super Ludwig","Ludwig","1958","early shells chrome-plated brass"),V("LM400 14×5","Ludwig","","aluminium shell, P83 strainer")],"depth 5 or 6.5 in · lug type"),
  X("Ludwig Acrolite","LM404","Ludwig's unplated aluminium snare, introduced in 1963 as a student model.","Ludwig","1963","https://www.bonedo.de/artikel/snare-vergleich-ludwig-black-beauty-vs-supraphonic-vs-acrolite/",[V("LM404 14×5","Ludwig","","1.6 mm aluminium, P85 strainer")],""),
  X("Slingerland Radio King","Radio King","Slingerland snare of 1936–37 with a single-piece steam-bent maple shell, associated with Gene Krupa.","Slingerland","1936",W+"Slingerland_Drum_Company",[V("Replica Radio King","Slingerland","2025","shown at NAMM under DW ownership")],"solid maple shell with maple reinforcing rings"),
  X("Rogers Dyna-Sonic","Dynasonic","Rogers snare (c. 1961–mid-1980s) whose cradle sets snare tension apart from head pressure.","Rogers","1961",W+"Rogers_Drums",[],""),
  X("Rogers PowerTone","PowerTone","Rogers snare model noted alongside the Dyna-Sonic.","Rogers","",W+"Rogers_Drums",[],""),
  X("Pearl Free-Floating snare","Free Floating","Pearl snare with no hardware on the shell, so shells swap like drumheads.","Pearl","",W+"Pearl_Drums",[],"interchangeable shells"),
  X("Pearl SensiTone","SensiTone","Pearl metal-shell snare line in several metals.","Pearl","",W+"Pearl_Drums",[V("Stainless, bronze and aluminium models discontinued","Pearl","2011","")],"shell metal"),
 ]}
ekit={"n":"Electronic drum kit","a":"e-kit · e-drums · digital drum kit","d":"Drum kit of pads or mesh heads that trigger electronic sounds from a sound module.",
 "t":["mesh-head pads","rubber pads","silicone pads","compact / practice kit","hybrid (acoustic shells with triggers)","sound module only"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("Simmons SDS-V","SDSV · Simmons hexagonal kit","Simmons' 1981 kit, called the first fully electronic drum set, with hexagonal pads.","Simmons","1981",W+"Simmons_(electronic_drum_company)",
    [V("SDS-V","Simmons","1981","developed with Richard James Burgess"),V("SDS 5 pads","Simmons","1981","start of the hexagonal pad design"),V("SDS7","Simmons","1984","rack brain with EPROM samples"),V("SDS9","Simmons","1985","hybrid digital/analogue brain")],"pad shape · module"),
  X("Roland V-Drums","V-Drums · TD series","Roland's mesh-head electronic kit line launched in 1997 with the TD-10 module.","Roland","1997",W+"V-Drums",
    [V("TD-10","Roland","1997","first V-Drums module, Remo-made mesh heads"),V("TD-30KV","Roland","","high-end 2010s kit"),V("TD-1","Roland","2014","entry kit, to 2023"),V("TD-50","Roland","2016","flagship to 2024"),V("TD-27","Roland","2020","to 2025"),V("TD-50X","Roland","2021",""),V("TD-02","Roland","2023","successor to TD-1"),V("V71","Roland","","successor to TD-50/TD-50X"),V("V51","Roland","","successor to TD-27")],"module · pad sizes · mesh or rubber"),
  X("Yamaha DTX","DTX series","Yamaha's sampled electronic kits and controllers, from beginner to professional.","Yamaha","",W+"Yamaha_DTX_series",
    [V("DTXTREME III","Yamaha","",""),V("DTX 950k","Yamaha","","2010s high-end kit"),V("DTX-502","Yamaha","",""),V("DTX-400K","Yamaha","","quietest Yamaha kit as of 2015")],"module · pad type"),
 ],
 "m":[["PerformancePad","Alesis"],["DM5 module","Alesis"]]}
epad={"n":"Electronic percussion pad","a":"multipad · sample pad · percussion controller","d":"Self-contained pad unit with built-in or sampled sounds, played with sticks or hands.",
 "t":["with onboard sounds","sample playback","controller only (MIDI)"],
 "s":"https://www.sweetwater.com/c645--Electronic_Drum_Controllers__and__Multipads",
 "x":[
  X("Roland Octapad","Octapad · SPD","Roland's eight-pad MIDI percussion controller line, first made in 1985.","Roland","1985",W+"Octapad",
    [V("Pad-8","Roland","1985","eight pads, no sounds"),V("Pad-80 (Octapad II)","Roland","1989",""),V("SPD-8","Roland","1990","onboard sounds"),V("SPD-11","Roland","1993","effects"),V("SPD-20","Roland","1998",""),V("Octapad SPD-30","Roland","2010","version 2 firmware 2012"),V("SPD-20X","Roland","2015",""),V("SPD-20 Pro","Roland","2020","")],"pad count · onboard sounds · trigger inputs"),
 ],
 "m":[["SPD-SX","Roland"],["DTX-Multi 12","Yamaha"],["SamplePad Pro","Alesis"],["Strike MultiPad","Alesis"],["KTMP1","KAT Percussion"],["DP-2000","NUX"]]}
def B(n,c,f,seg,d,sig,s,lines=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"sig":sig,"s":s}
    if lines: b["lines"]=list(lines)
    if rel: b["rel"]=list(rel)
    return b
brands=[
 B("Ludwig","United States","1909","Drums, snares and percussion","Chicago-founded drum maker, now in Monroe, North Carolina; Ringo Starr's kit maker; part of Conn-Selmer.",["Ludwig Supraphonic","Ludwig Black Beauty","Ludwig Vistalite","Ludwig Classic Maple"],W+"Ludwig_Drums",["Musser"]),
 B("Gretsch","United States","1883","Drums and guitars","Brooklyn-founded maker; drums built in Ridgeland, South Carolina.",["Gretsch USA Custom"],W+"Gretsch_Drums"),
 B("Rogers","United States","1849","Drums","Historic American drum maker, later a revived brand.",["Rogers Dyna-Sonic","Rogers Holiday"],W+"Rogers_Drums",["Swiv-O-Matic"]),
 B("Slingerland","United States","1912","Drums","Chicago drum maker of the Radio King; owned by DW since 2019.",["Slingerland Radio King"],W+"Slingerland_Drum_Company",rel=["Drum Workshop"]),
 B("Drum Workshop","United States","1972","Premium drums and hardware","Californian maker (DW), known for its 5000 pedal and Collector's Series; owned by Roland since 2022.",["DW Collector's Series"],W+"Drum_Workshop",["PDP","Gibraltar","Latin Percussion"],["Slingerland","Roland"]),
 B("Pearl","Japan","1946","Drums, from entry to professional","Japanese drum maker whose Export is the best-selling drum set line.",["Pearl Export","Pearl Masters","Pearl Free-Floating snare"],W+"Pearl_Drums"),
 B("Tama","Japan","1974","Drums and hardware","Hoshino Gakki's drum brand, made in Seto, Japan and China.",["Tama Imperialstar","Tama Superstar"],W+"Tama_Drums"),
 B("Sonor","Germany","1875","Drums and Orff instruments","German drum maker in Bad Berleburg, part of KHS.",["Sonor Signature"],W+"Sonor"),
 B("Yamaha","Japan","1887","Musical instruments of all kinds","Japanese instrument maker; drums include the Recording Custom and DTX electronic kits.",["Yamaha Recording Custom","Yamaha DTX"],"knowledge"),
 B("Roland","Japan","1972","Electronic instruments","Japanese electronic-instrument maker of V-Drums and the Octapad; owner of DW.",["Roland V-Drums","Roland Octapad"],"knowledge",rel=["Drum Workshop"]),
 B("Simmons","United Kingdom","1978","Electronic drums","Dave Simmons' company, maker of the hexagonal-pad SDS-V; name later owned by Guitar Center.",["Simmons SDS-V"],W+"Simmons_(electronic_drum_company)"),
 B("Alesis","United States","1984","Electronic drums and audio","Keith Barr's company, part of inMusic since 2012.",[],W+"Alesis"),
]
notes=("Kept all four planned kinds. Not included because no fetched page confirmed them: Tama Starclassic (only search snippets dated it), Gretsch Round Badge and Broadkaster detail, "
 "Ludwig Super Classic/Ringo kit model name, DW 5000-era kit names, Sonor SQ2/Phonic dates, Alesis Nitro/Strike kits, Sonor HLD590 snare. Sweetwater Classic Maple page blocked (403); a dealer page used instead. "
 "Rogers Holiday and PowerTone carry no year because the source gives none. No craft traditions apply to this shelf.")
out={"kinds":[kit,snare,ekit,epad],"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/03_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
