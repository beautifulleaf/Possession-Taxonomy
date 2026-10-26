import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_,"mk":b,"y":c,"d":e} for a_,b,c,e in v],"dt":dt}
combo={"n":"Combo amp","a":"combo · combination amplifier","d":"Instrument amplifier and loudspeaker in one cabinet.",
 "t":["valve (tube)","solid-state","modelling","hybrid","guitar","bass","1x8 to 4x10 and 2x12 speaker layouts"],
 "s":"https://www.sweetwater.com/c625--Combo_Amp?pn=4",
 "x":[
 X("Fender Bassman (tweed 4x10)","5F6-A Bassman · tweed Bassman","Fender's first bass amp; the 1958 5F6-A 4x10 tweed circuit became a guitar reference and the basis of Marshall's JTM45.","Fender","1952 (5F6-A 1958)",W+"Fender_Bassman",
  [("5B6","Fender","1952","single 15-inch Jensen, tweed"),("5D6","Fender","1954","first 4x10, four Jensen P10R"),("5F6","Fender","1957","three-knob tone stack, long-tailed-pair phase inverter"),("5F6-A","Fender","1958","GZ34 rectifier; the classic version"),("6G6 piggyback","Fender","1960","head and cabinet, blonde Tolex"),("'59 Bassman reissue","Fender","1990","reissue of the 5F6-A")],
  "circuit code (5B6 to 5F6-A) · tweed, blonde, blackface, silverface · Jensen P10R or P10Q speakers"),
 X("Fender Twin Reverb","Twin · Twin Amp","Fender's loud two-12-inch combo; the blackface Twin Reverb added spring reverb and tremolo and became the clean-tone standard.","Fender","1952 (Twin Reverb 1963)",W+"Fender_Twin",
  [("Wide Panel Twin","Fender","c. 1952–1954","25 W, two 12-inch"),("Big Box tweed Twin","Fender","1957–1960","about 80 W, four 5881s"),("Blackface Twin Reverb","Fender","1963–1967","85 W, reverb and tremolo"),("Silverface Twin Reverb","Fender","1967 on","master volume 1972, 100 W, later 135 W"),("'65 Twin Reverb reissue","Fender","1992","85 W, Jensen C-12K"),("'68 Custom Twin Reverb","Fender","2013","silverface look, Celestion speakers"),("Tone Master Twin Reverb","Fender","2019","digital model, 85 W")],
  "era cosmetics (tweed, blonde, blackface, silverface) · 85–135 W · speaker make (Jensen, Oxford, JBL, Eminence)"),
 X("Fender Deluxe Reverb","Deluxe Reverb","22-watt Fender combo with two 6V6s, one 12-inch speaker and spring reverb; a studio and club favourite.","Fender","1963",W+"Fender_Deluxe_Reverb",
  [("Blackface (AA763, AB763)","Fender","1963","original circuits"),("Silverface","Fender","1968",""),("Deluxe Reverb II","Fender","1982–1986","20 W, gain and master controls"),("'65 Deluxe Reverb reissue","Fender","1993","printed circuit board"),("'68 Custom Deluxe Reverb","Fender","2013","silverface look, altered circuit")],
  "blackface or silverface · 22 W · Jensen C-12Q or other 12-inch speaker"),
 X("Fender Champ","Champion · Vibro Champ","Fender's small single-ended practice and studio amp of about 5 watts.","Fender","1948",W+"Fender_Champ",
  [("Champion 800","Fender","1948–1949","8-inch"),("Champion 600","Fender","1949–1955","6-inch"),("Tweed Champ 5F1","Fender","1958–1964","about 5 W, 8-inch"),("Vibro Champ","Fender","1964–1982","adds tremolo"),("Super Champ XD","Fender","2007–2012","15 W, 10-inch"),("'68 Custom Vibro Champ Reverb","Fender","2021","5 W, 10-inch")],
  "circuit and era · 3–18 W · 6, 8 or 10-inch speaker"),
 X("Vox AC30","AC30 Top Boost · AC30/6","Dick Denney's JMI combo with EL84 valves, two 12-inch Celestion Blues and the Top Boost circuit; the British chime sound.","Vox","1959",W+"Vox_AC30",
  [("AC30 1x12 (EL34)","Vox","1959","first version"),("AC30/6 Twin","Vox","1960","2x12, four EL84s"),("Top Boost standard","Vox","1963","retrofit from 1961"),("AC30TBX","Vox","mid-1990s","Korg era"),("AC30CC","Vox","2004","made in China"),("Handwired AC30","Vox","2004","limited, later regular"),("AC30BM","Vox","2006","Brian May signature")],
  "Normal, Top Boost or Custom channels · Celestion Alnico Blue or Greenback · 2x12 or 1x12"),
 X("Mesa/Boogie Mark series","Boogie · Mark IIC+","Randall Smith's cascading-gain combo, the original Boogie, developed through numbered Marks.","Mesa/Boogie","1972",W+"Mesa/Boogie",
  [("Mark I","Mesa/Boogie","1972","the original 'Boogie', renamed 1978"),("Mark II","Mesa/Boogie","1978",""),("Mark IIC+","Mesa/Boogie","1984–1985","most sought-after version"),("Mark III","Mesa/Boogie","",""),("Mark IV","Mesa/Boogie","",""),("Mark V","Mesa/Boogie","",""),("Mark VII","Mesa/Boogie","","after Gibson's 2021 purchase")],
  "Mark number · combo or head · 1x12 · graphic EQ option"),
 X("Roland JC-120 Jazz Chorus","Jazz Chorus · JC","Roland's solid-state 120-watt 2x12 combo with built-in stereo chorus, known for its clean tone.","Roland","1975",W+"Roland_Jazz_Chorus",
  [("JC-120","Roland","1975","120 W, 2x12, stereo chorus"),("JC-160","Roland","1976","4x10"),("JC-77","Roland","1984","80 W, 2x10"),("JC-120H","Roland","1984","head"),("JC-40","Roland","2015","DSP, 2x10"),("JC-22","Roland","2016","DSP, 2x6.5")],
  "size (JC-20 to JC-160) · analog or DSP"),
 X("Ampeg B-15 Portaflex","B-15 · flip-top","Ampeg's flip-top bass combo whose chassis stores inside the cabinet; the most-recorded bass amp.","Ampeg","1960",W+"Ampeg",[],
  "flip-top valve combo · 15-inch speaker")],
 "m":[["Catalyst CX 100","Line 6"],["Spider V 20 MkII","Line 6"],["CUBE-10GX","Roland"],["THR30 II Wireless","Yamaha"]],
 "r":[["Princeton","Fender"],["Mustang","Fender"],["Tone Master","Fender"],["AC15","Vox"],["AC10","Vox"],["DSL","Marshall Amplification"],["Origin","Marshall Amplification"],["Studio","Marshall Amplification"],["Rectifier","Mesa/Boogie"],["5150","EVH"],["SLO-30","Soldano"],["Crush","Orange"],["Debut","Blackstar"],["HT Venue","Blackstar"],["St. James","Blackstar"],["Blues Cube","Roland"],["Cube","Roland"],["Catalyst","Line 6"],["Spider V","Line 6"],["THR","Yamaha"],["Atma","Bogner (amplifiers)"],["Gremlin","Tone King"],["Ironball","ENGL Amplifiers"],["Martin Kidd","Victory Amplification"],["Master Collection","Magnatone"],["DGT","PRS"]]}
head={"n":"Amp head","a":"head · piggyback head","d":"Instrument amplifier without a loudspeaker, made to drive a separate cabinet.",
 "t":["valve (tube)","solid-state","hybrid","lunchbox / mini head","guitar","bass"],
 "s":"https://www.sweetwater.com/c623--Amp_Head?pn=4",
 "x":[
 X("Marshall JTM45","JTM 45","Marshall's first amp, a 45-watt head based on the Fender Bassman circuit.","Marshall Amplification","1963",W+"Marshall_Amplification",[],"KT66 or later valves · Bluesbreaker combo version (catalogue 1962)"),
 X("Marshall 1959 Super Lead 'Plexi'","Plexi · Super Lead 100","Marshall's 100-watt head with a Plexiglas front panel; the sound of the stacked British rock amp.","Marshall Amplification","1965",W+"Marshall_Amplification",[],"Plexi or aluminium panel · original or reissue (handwired, SLP)"),
 X("Marshall JCM800 2203","JCM800","Marshall's 100-watt single-channel master-volume head of the 1980s hard-rock sound.","Marshall Amplification","1981",W+"Marshall_JCM800",
  [("2203","Marshall Amplification","1981","100 W"),("2204","Marshall Amplification","1981","50 W"),("2205","Marshall Amplification","","two channels"),("2210","Marshall Amplification","","split channel, reverb"),("JCM800 reissue","Marshall Amplification","2002","")],
  "100 or 50 W · single or split channel"),
 X("Mesa/Boogie Dual Rectifier","Dual Rec · Recto","Mesa/Boogie's high-gain head of the 1990s, defining modern metal tone.","Mesa/Boogie","1991",W+"Mesa/Boogie",[],"channels and revisions · head or combo · matching Rectifier cabinets"),
 X("Dumble Overdrive Special","ODS","Hand-built two-channel amp whose overdrive stacks on the clean channel; about 300 Dumbles were made one at a time.","Dumble","1972",W+"Dumble_Amplifiers",
  [("Overdrive Special","Dumble","1972","grew out of the 1969 'Explosion'"),("Overdrive Reverb","Dumble","","adds reverb"),("Steel String Singer","Dumble","","clean, single channel")],
  "6L6 or EL34 · head or combo · HRM tone controls"),
 X("Peavey 5150","6505 · 5150","Peavey's high-gain head made as Eddie Van Halen's signature model; renamed 6505 after he left.","Peavey","1992",W+"Peavey_5150",
  [("5150","Peavey","1992","120 W"),("5150 II","Peavey","","second version"),("6505","Peavey","2005","renamed for the 40th anniversary"),("6505 2x12 combo","Peavey","","60 W"),("5150 (EVH brand)","EVH","2007","name returns with Fender")],
  "head or combo · 120 W"),
 X("Ampeg SVT","Super Valve Technology","Ampeg's 300-watt valve bass head, the rock bass stack standard.","Ampeg","1969",W+"Ampeg",[],"valve or solid-state · paired 8x10 cabinets"),
 X("Orange Graphic 120","Pics Only · Pics & Text · OR120","Orange's 120-watt head with picture-symbol controls and orange covering.","Orange","c. 1971",W+"Orange_Music_Electronic_Company",
  [("Pics Only","Orange","c. 1971","symbols, no text"),("Pics & Text","Orange","1974",""),("Gibson-licensed reissue","Orange","1994","")],
  "pictogram panel · orange Tolex · 120 W")],
 "m":[["DSL100HR","Marshall Amplification"],["ORI50H Origin 50","Marshall Amplification"],["SV20H Studio Vintage","Marshall Amplification"],["Mark VII","Mesa/Boogie"],["SYN-20IR","Synergy (amplifiers)"]],
 "r":[["JVM","Marshall Amplification"],["Classic Reissue","Marshall Amplification"],["Handwired","Marshall Amplification"],["5150","EVH"],["TH30","Orange"],["Badger","Suhr"],["Atma","Bogner (amplifiers)"],["Imperial","Tone King"],["Ironball","ENGL Amplifiers"],["Martin Kidd","Victory Amplification"],["Super-Sonic","Fender"],["AC30","Vox"],["Debut","Blackstar"],["St. James","Blackstar"],["DGT","PRS"]]}
cab={"n":"Speaker cabinet","a":"cab · speaker cab · 4x12","d":"Loudspeaker enclosure made to be driven by an amp head.",
 "t":["open-back","closed-back","angled or straight baffle","1x12, 2x12, 4x10, 4x12, 8x10","powered FRFR cabinet"],
 "s":"https://www.sweetwater.com/c624--Amp_Cab?pn=8",
 "x":[X("Marshall 1960 4x12","1960A · 1960B · Marshall stack","Marshall's four-12-inch closed-back cabinet, the half of the Marshall stack; 'A' marks the angled baffle.","Marshall Amplification","early 1960s","https://musewiki.org/Marshall_1960A_Cab",
  [("1960A","Marshall Amplification","early 1960s","angled baffle; now four Celestion G12T-75, 300 W"),("2536A Silver Jubilee Cab","Marshall Amplification","","from the old data")],"angled or straight · Celestion speaker type · 16 or 4/16 ohm")],
 "m":[["MX412AR","Marshall Amplification"],["PowerCab CL 112","Line 6"],["TONEX Cab","IK Multimedia"]],
 "r":[["Rectifier","Mesa/Boogie"],["PPC","Orange"],["5150","EVH"],["Classic Reissue","Marshall Amplification"],["Handwired","Marshall Amplification"],["Powercab","Line 6"],["ToneX","IK Multimedia"],["Badger","Suhr"],["SLO-30","Soldano"],["Debut","Blackstar"],["Hand-Wired AC","Vox"],["Imperial","Tone King"],["Martin Kidd","Victory Amplification"]]}
spk={"n":"Guitar speaker","a":"guitar driver · speaker swap","d":"Loudspeaker driver built for a guitar or bass amp or cabinet, voiced to colour the tone.",
 "t":["10-inch","12-inch","15-inch","alnico magnet","ceramic magnet","8 or 16 ohm"],
 "s":W+"Guitar_speaker",
 "x":[
 X("Celestion Blue","Alnico Blue · G12 T530","Celestion's alnico 12-inch, described as the first dedicated guitar speaker; the voice of the Vox AC30.","Celestion","",W+"Celestion",[("Korg-era Vox reissue fitment","Vox","1990s","Alnico Blue returned to AC30s")],"15 W · alnico · 8 or 15 ohm"),
 X("Celestion G12M Greenback","Greenback · G12M","Celestion's first ceramic-magnet guitar speaker, with a medium magnet and green back cover; the sound of early Marshall 4x12s.","Celestion","1960s","https://celestion.com/product/heritage-series-g12m",[("Heritage Series G12M","Celestion","","20 W reissue, 8 or 15 ohm")],"20–25 W · ceramic · 8, 15 or 16 ohm"),
 X("Celestion Vintage 30","V30","Celestion's 1980s speaker modelled on the Blue's cone with an H magnet, for hot-rodded rock amps.","Celestion","1986","https://celestion.com/blog/vintage-30-a-tonal-history/",[],"ceramic H magnet · 8 or 16 ohm"),
 X("Jensen P10R","P10R","Jensen's alnico 10-inch of the tweed era, used four at a time in the 4x10 Bassman; reissued from 1999.","Jensen","tweed era (reissued 1999)","http://www.jensentone.com/vintage-alnico/p10r",[("P10R reissue","Jensen","1999","25 W, 4, 8 or 16 ohm")],"25 W · alnico · 4, 8 or 16 ohm")]}
mod={"n":"Amp modeller","a":"amp simulator · profiler · modelling processor","d":"Floor, desktop or rack unit that carries amplifier models, usually with effects, in place of an amplifier.",
 "t":["floor unit","desktop","rack","pedal-size","capture / profiling"],
 "s":"https://www.sweetwater.com/c633--Amp_Modeling_Multi-effects_Pedals",
 "x":[
 X("Line 6 POD","POD","Line 6's red kidney-bean desktop amp modeller that brought amp modelling to home recording.","Line 6","1998",W+"Line_6_(company)",
  [("POD","Line 6","1998","kidney-bean desktop"),("POD XT Pro","Line 6","2003","rack"),("POD XT Live","Line 6","2004","floor"),("POD Go Wireless","Line 6","","from the old data"),("POD Express Guitar","Line 6","","from the old data")],"desktop, rack or floor"),
 X("Fractal Audio Axe-Fx","Axe-Fx","Fractal Audio's rack-mount amp modeller and effects processor, the company's debut product.","Fractal Audio Systems","",W+"Fractal_Audio_Systems",
  [("Axe-Fx","Fractal Audio Systems","","first rack unit"),("Axe-Fx III","Fractal Audio Systems","","current rack"),("AX8","Fractal Audio Systems","","floor unit"),("FM3","Fractal Audio Systems","","compact floor unit"),("FM9","Fractal Audio Systems","","larger floor unit")],"rack or floor"),
 X("Kemper Profiler","Kemper · KPA","Kemper's unit that captures a profile of a real amp, cabinet and microphone instead of using preset models.","Kemper","2011",W+"Kemper_Profiler",
  [("Profiler Head / Rack","Kemper","2011",""),("Profiler Stage","Kemper","","floorboard"),("Profiler Player","Kemper","","stompbox"),("Profiler MK 2","Kemper","2025","announced")],"head, rack, floor or stompbox · powered or unpowered"),
 X("Line 6 Helix","Helix · HX","Line 6's flagship floor modeller and effects unit, extended into the smaller HX family.","Line 6","2015",W+"Line_6_(company)",
  [("Helix","Line 6","2015",""),("HX Stomp XL","Line 6","","from the old data"),("Helix Stadium","Line 6","","from the old data"),("Helix Stadium XL","Line 6","","from the old data")],"floor, rack or pedal size"),
 X("Neural DSP Quad Cortex","Quad Cortex · QC","Neural DSP's floor modeller with amp capture, shown at NAMM 2020.","Neural DSP","2020",W+"Neural_DSP",
  [("Quad Cortex","Neural DSP","2020",""),("Nano Cortex","Neural DSP","2024","compact"),("Quad Cortex Mini","Neural DSP","2026","")],"full or compact floor unit")],
 "m":[["Tone Master Pro","Fender"],["GX-100","BOSS"],["GX-10","BOSS"],["TONEX Pedal","IK Multimedia"],["TONEX ONE","IK Multimedia"],["Iridium","Strymon"],["Ampero II Stomp","Hotone"],["Flex Prime","Headrush"],["MG-300 MKII","NUX"],["GP-200","Valeton"],["G1X FOUR","Zoom (audio)"],["Simplifier X","DSM Humboldt Electronics"]],
 "r":[["ToneX","IK Multimedia"],["UAFX","Universal Audio"],["ReVolt","Two Notes"],["Ampworx","TC Electronic"]]}
att={"n":"Power attenuator","a":"attenuator · power soak · load box","d":"Device between amp and speaker that soaks up part of the output so a valve amp can be driven hard at lower volume.",
 "t":["resistive","reactive load","L-pad","variac / power scaling","with impulse-response cab simulation"],
 "s":W+"Power_attenuator_(guitar)",
 "m":[["Power Brake","Marshall Amplification"],["Power Soak","Scholz"],["Hot Plate","THD"],["MASS","Weber"],["HotBox","Audiostorm"]]}
kinds=[combo,head,cab,spk,mod,att]
K='knowledge'
def B(n,c,f,seg,d,lines,eras,sig,rel,s): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":eras,"sig":sig,"sc":[],"rel":rel,"s":s}
brands=[
 B("Fender","United States","1946","Guitars and amplifiers","Californian maker whose tweed and blackface amps set the American amp sound.",["Vintage Reissue","Tone Master","'68 Custom"],["Tweed, 1950s","Blackface, 1963–1967","Silverface, 1967–1980"],["Fender Bassman (tweed 4x10)","Fender Twin Reverb","Fender Deluxe Reverb","Fender Champ"],["EVH"],K),
 B("Marshall Amplification","United Kingdom","1962","Valve guitar amplifiers","Jim Marshall's London firm, maker of the JTM45, Plexi and JCM800 and the 4x12 stack.",["JCM800","JCM900","JVM","DSL","Silver Jubilee","Origin","Studio"],["JTM, 1963–","Plexi, 1965–1969","JCM800, 1981–1990"],["Marshall JTM45","Marshall 1959 Super Lead 'Plexi'","Marshall JCM800 2203","Marshall 1960 4x12"],["Fender","Celestion"],W+"Marshall_Amplification"),
 B("Vox","United Kingdom","","Amplifiers and combo organs","Tom Jennings' JMI brand behind the AC15 and AC30; owned by Korg since 1992.",["AC30","AC15","AC10"],["Jennings Musical Industries, 1950s–1960s","Vox Sound Ltd, 1970–","Korg, 1992–"],["Vox AC30"],["Celestion"],W+"Vox_AC30"),
 B("Mesa/Boogie","United States","1969","Boutique valve amplifiers","Randall Smith's California maker of the Mark series and Rectifier; bought by Gibson in 2021.",["Mark","Rectifier","Lone Star","Express"],["Randall Smith, 1969–","Gibson, 2021–"],["Mesa/Boogie Mark series","Mesa/Boogie Dual Rectifier"],["Gibson"],W+"Mesa/Boogie"),
 B("Dumble","United States","1969","Hand-built custom amplifiers","Howard Alexander Dumble's Santa Cruz shop; about 300 amps, revived by the Dumble Preservation Society in 2022.",["Overdrive Special","Steel String Singer"],["Howard Dumble, 1969–2022","Dumble Preservation Society, 2022–"],["Dumble Overdrive Special"],[],W+"Dumble_Amplifiers"),
 B("Peavey","United States","1965","Amplifiers and audio","American amplifier maker; made the 5150 for Eddie Van Halen, later sold as the 6505.",["6505"],[],["Peavey 5150"],["EVH"],W+"Peavey_5150"),
 B("EVH","United States","","Signature guitars and amplifiers","Eddie Van Halen's brand, made with Fender; carries the 5150 amp name since 2007.",["5150"],[],[],["Fender","Peavey"],W+"Peavey_5150"),
 B("Ampeg","United States","1946","Bass amplifiers","Bass-amp maker of the B-15 Portaflex and SVT; part of Yamaha Guitar Group since 2018.",["Portaflex","SVT","Heritage"],["Yamaha Guitar Group, 2018–"],["Ampeg B-15 Portaflex","Ampeg SVT"],["Yamaha"],W+"Ampeg"),
 B("Roland","Japan","1972","Electronic instruments","Japanese electronic-instrument maker; its amps include the JC-120 Jazz Chorus and Cube.",["Jazz Chorus","Cube","Blues Cube"],[],["Roland JC-120 Jazz Chorus"],["BOSS"],K),
 B("Orange","United Kingdom","1968","Valve amplifiers","Cliff Cooper's London maker known for orange covering and picture-symbol controls.",["Graphic","Rockerverb","Tiny Terror","AD","Crush","TH"],[],["Orange Graphic 120"],[],W+"Orange_Music_Electronic_Company"),
 B("Celestion","United Kingdom","1924","Loudspeakers","Ipswich speaker maker of the Blue, Greenback and Vintage 30; owned by Gold Peak.",["Heritage","Vintage 30","G12"],[],["Celestion Blue","Celestion G12M Greenback","Celestion Vintage 30"],["Marshall Amplification","Vox","Orange"],W+"Celestion"),
 B("Jensen","United States","","Loudspeakers","Speaker maker of the alnico P10R and C12 series fitted to tweed-era Fender amps.",["Vintage Alnico"],[],["Jensen P10R"],["Fender"],"http://www.jensentone.com/vintage-alnico/p10r"),
 B("Line 6","United States","1996","Digital modelling gear","Calabasas maker of the POD and Helix modellers; owned by Yamaha since 2014.",["POD","Helix","HX","Spider","Catalyst"],["Yamaha, 2014–"],["Line 6 POD","Line 6 Helix"],["Yamaha"],W+"Line_6_(company)"),
 B("Fractal Audio Systems","United States","2006","Amp modelling processors","Cliff Chase's New Hampshire maker of the Axe-Fx rack and FM floor modellers.",["Axe-Fx","FM3","FM9","VP4"],[],["Fractal Audio Axe-Fx"],[],W+"Fractal_Audio_Systems"),
 B("Kemper","Germany","","Amp profiling","Christoph Kemper's German brand, maker of the Profiler, introduced in 2011.",["Profiler"],[],["Kemper Profiler"],[],W+"Kemper_Profiler"),
 B("Neural DSP","Finland","2017","Amp modelling software and hardware","Helsinki maker of Archetype plug-ins and the Quad Cortex floor modeller.",["Archetype","Cortex"],[],["Neural DSP Quad Cortex"],[],W+"Neural_DSP"),
]
notes=("All six planned kinds kept (4 old merged one-to-one; Guitar speaker and Power attenuator new, sourced to Wikipedia). "
 "Amp modeller flat list cut from 29 to 12; Line 6 POD/Helix and Neural DSP items moved into archetype versions; BOSS ME-90, Blackstar ID:X, Headrush Prime, Hotone Ampero II Stage, IK TONEX Board, Quilter DirectAmp/Elevate, TC Combo Deluxe 65, Zoom MS-80 IR+, Strymon-only duplicates dropped as SKU noise. "
 "Ranges trimmed and VOX normalised to 'Vox'. Left out for want of a retrieved page: Ampeg 8x10 cab archetype, Marshall 1960B and Celestion G12H/G12-65/G12T-75 details, Mesa Mark III-V years, Orange OR120 as a named model (Graphic 120 used), Two Notes/Fryette/Bad Cat attenuators, IK ToneX and BOSS GX archetypes. Sweetwater pages blocked (403), not retried. "
 "Brands with 'knowledge': Fender, Roland. Founding years left blank where pages did not give them (Vox, EVH, Jensen, Kemper).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/06_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('ok')
