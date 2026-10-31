import json, os
W="https://en.wikipedia.org/wiki/"
P="AlphaTheta (Pioneer DJ)"
def A(n,d,mk,y,s,v=(),a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":x[1],"y":x[2],"d":x[3]} for x in v],"dt":dt}
T=W+"Technics_SL-1200"; CDJ=W+"CDJ"; PDJ=W+"Pioneer_DJ"; VX=W+"Vestax"; CTL=W+"DJ_controller"
SEDA="https://seda.org.uk/2020/01/denon-sc6000-sc6000m-x1850-prime/"
kinds=[
{"n":"DJ turntable","a":"DJ deck · direct-drive turntable · wheels of steel","d":"Direct-drive record turntable with pitch control and high torque, sold for DJ mixing and scratching.",
 "t":["S-shaped tonearm","Straight tonearm","Pitch range ±8 / ±16 / ±50%","Silver or black finish","Limited and anniversary editions"],
 "s":"https://www.sweetwater.com/c1204--Direct_Drive_Turntables",
 "x":[
  A("Technics SL-1200","The direct-drive turntable that became the club and turntablist standard; the SL-1210 is the black twin.","Technics","1972",T,[
    ("SL-1200",  "Technics","1972","Original model"),
    ("SL-1200MK2","Technics","1979","Silver; with black SL-1210MK2, made until 2010"),
    ("SL-1200MK3","Technics","1989","Japan only, matte black"),
    ("SL-1200M3D / SL-1210M3D","Technics","1997","European/US version"),
    ("SL-1200MK5 / SL-1210MK5","Technics","2000",""),
    ("SL-1210M5G","Technics","2002","30th-anniversary edition, glossy black"),
    ("SL-1200MK6","Technics","2008","Japan"),
    ("SL-1200G","Technics","2016","Revival model announced at CES 2016"),
    ("SL-1200GR","Technics","2017","Lower-priced Grand Class model"),
    ("SL-1200MK7 / SL-1210MK7","Technics","2019","DJ model launched at CES 2019"),
    ("SL-1200GR2 / SL-1210GR2","Technics","2021","ΔΣ-Drive motor control")],
    a="Technics 1200 · 1210 · Tech 12s",dt="SL-1200 silver or SL-1210 black · limited editions (SL-1200LTD 1995, SL-1200GLD 2004, SL-1200GAE 2016, SL-1210GAE 2020)"),
  A("OEM direct-drive DJ deck","Taiwanese Hanpin-built direct-drive deck sold under many brands, closely following the SL-1210 layout.","","","https://www.bonedo.de/artikel/reloop-rp-5000-mk4-dj-plattenspieler-im-test/",[
    ("RP-5000 MK4","Reloop","","Quartz direct drive, S-arm, ±8/16/50% pitch")],
    a="super OEM deck · Hanpin deck · 1210 clone",dt="S-shaped or straight arm · torque · pitch range · brand styling"),
  A("Vestax PDX","Vestax's range of DJ turntables, with the PDX-3000 as late-1990s flagship.","Vestax","late 1990s",VX,[
    ("PDX-3000","Vestax","late 1990s","Flagship"),
    ("PDX-2000mk2 / PDX-2300mk2","Vestax","2010s",""),
    ("PDX-2000mk2pro / PDX-2300pro","Vestax","2010s","New tonearm suspension")]),
  A("Vestax QFO","Scratch turntable developed by Vestax with DJ Qbert.","Vestax","2010s",VX,[
    ("QFO LE","Vestax","2010s","")])],
 "m":[["PLX-500",P],["AT-LP120X","Audio-Technica"],["AT-LP5X","Audio-Technica"],["RP-7000 MK2","Reloop"],["SL-1500C","Technics"],["SL-50C","Technics"]],
 "r":[["PLX",P],["RP","Reloop"]]},
{"n":"DJ media player","a":"CDJ · DJ CD player · USB media player","d":"Tabletop or rack player with jog wheel and pitch control for mixing music from CD, USB or network.",
 "t":["Tabletop single player","Rack-mount dual player","USB / network player","Motorised-platter player","Video (DVD) player"],
 "s":CDJ,
 "x":[
  A("Pioneer CDJ","Pioneer's tabletop DJ media player line, the club standard from the CDJ-1000 onwards.",P,"1994",CDJ,[
    ("CDJ-500","Pioneer","1994","First CDJ"),
    ("CDJ-100S","Pioneer","1998",""),
    ("CDJ-1000","Pioneer","2001","Vinyl-style jog wheel"),
    ("CDJ-1000MK3","Pioneer","2006",""),
    ("CDJ-2000 / CDJ-900","Pioneer","2009","Also controls DJ software over HID"),
    ("CDJ-2000NXS","Pioneer","2012","Nexus"),
    ("CDJ-2000NXS2","Pioneer DJ","2016",""),
    ("CDJ-3000",P,"2020",""),
    ("CDJ-3000X",P,"2025",""),
    ("CDJ-1500X",P,"2026","")],a="CDJ",dt="flagship or mid-range · CD, USB, SD, network link"),
  A("Rack-mount dual CD player","Two-deck CD player with a separate rack transport and control unit, first credited to Denon in 1993.","Denon DJ","1993",CDJ,[
    ("CMX-5000","Pioneer","2000","19-inch rack dual CD player"),
    ("CMX-3000","Pioneer","2003",""),
    ("MEP-7000","Pioneer","2007","19-inch rack twin player")]),
  A("Pioneer DVJ","DJ player for DVDs, letting video be scratched and mixed with the audio.",P,"2004",CDJ,[
    ("DVJ-X1","Pioneer","2004",""),("DVJ-1000","Pioneer","2006","")]),
  A("Denon DJ SC6000","Denon DJ's flagship standalone media player running Engine OS, with touchscreen and internal drive bay.","Denon DJ","2020",SEDA,[
    ("SC5000 / SC5000M","Denon DJ","","Predecessor"),
    ("SC6000M","Denon DJ","2020","8.5-inch motorised platter")],dt="10.1-inch touchscreen · Wi-Fi streaming · internal HDD bay")]},
{"n":"DJ mixer","a":"club mixer · battle mixer · scratch mixer · rotary mixer","d":"Small mixer with phono and line channels, crossfader, EQ and headphone cue for blending two or more sources.",
 "t":["Two-channel scratch / battle mixer","Four-channel club mixer","Rotary mixer","Built-in DVS sound card","Analogue or digital signal path"],
 "s":W+"DJ_mixer",
 "x":[
  A("Bozak CMA-10-DL2","The first commercially available DJ mixing board and the club standard of the 1970s.","Bozak","1970s",W+"DJ_mixer",a="Bozak rotary"),
  A("Pioneer DJM","Pioneer's club mixer line, launched with the DJM-500 beside the CDJ-500 and now the club standard.",P,"1994",PDJ,[
    ("DJM-500","Pioneer","1994","Companion to the CDJ-500"),
    ("DJM-800","Pioneer","",""),
    ("DJM-3000","Pioneer","2008","Shown at NAMM 2008"),
    ("DJM-900NXS2","Pioneer DJ","2016","Four channels, 24-bit converters"),
    ("DJM-A9",P,"2023","Successor to the DJM-900NXS2; 32-bit converters, MAGVEL crossfader")],dt="channels · effects · converters"),
  A("Allen & Heath Xone:92","Analogue 4+2-channel club mixer with dual analogue filters, a club standard for over two decades.","Allen & Heath","","https://rubadub.co.uk/products/allen-heath-xone-92-mk-2-pro-6-channel-dj-mixer-w-analogue-filters",[
    ("Xone:92 MK2","Allen & Heath","","Mini innoFADER Pro crossfader, silent filter switching")],a="Xone 92"),
  A("Rane MP2015","Four-channel all-rotary digital mixer with three-band isolator, wooden frame and dual USB.","Rane","2015","https://ra.co/reviews/17251"),
  A("Vestax PMC-05Pro","Two-channel scratch mixer developed with DJs after talks at the 1993 NAMM show.","Vestax","early 1990s",VX,[
    ("PMC-05ProII","Vestax","",""),("PMC-05ProD Samurai","Vestax","",""),("PMC-05ProIII","Vestax","",""),
    ("PMC-05ProSL","Vestax","",""),("PMC-05ProIV","Vestax","","")],a="PMC-05"),
  A("Rane Seventy-Two","Two-channel Serato scratch mixer with touchscreen, performance pads and FX paddles.","Rane","","https://serato.com/dj/hardware/rane-seventy-two-mkii",[
    ("Seventy-Two MKII","Rane","","MAG FOUR faders, external crossfader tension")]),
  A("Denon DJ X1850 Prime","Four-channel club mixer with dual USB and BPM effects.","Denon DJ","2020",SEDA)],
 "m":[["DM2002X Pro Master","Numark"]]},
{"n":"DJ controller","a":"controller · all-in-one DJ system · standalone DJ system","d":"Control surface with jog wheels, faders and pads for DJ software, or a standalone unit with built-in players.",
 "t":["Two-channel software controller","Four-channel software controller","Standalone all-in-one system with screen","Party controller with speakers or lights","Add-on FX or remix controller","Motorised jog wheels"],
 "s":"https://www.sweetwater.com/c1158--DJ_Controllers?pn=2",
 "x":[
  A("Hercules DJ Console","One of the earliest DJ software controllers.","Hercules DJ","2004",CTL),
  A("Vestax VCI-100","Vestax's first digital DJ controller, an early widely used software controller.","Vestax","2006–2007",VX,[
    ("VCI-380","Vestax","",""),("VCI-400","Vestax","","")]),
  A("Native Instruments Traktor Kontrol S4","Four-deck Traktor controller with built-in audio interface.","Native Instruments","2010",CTL,[
    ("Traktor Kontrol S4 Mk2","Native Instruments","2013","")]),
  A("Pioneer DDJ","Pioneer's software controller line, made for rekordbox, Serato and Traktor.",P,"2011",CTL,[
    ("DDJ-S1","Pioneer","2011","Serato"),("DDJ-T1","Pioneer","2011","Traktor"),
    ("DDJ-SX2","Pioneer","2014",""),("DDJ-RX","Pioneer DJ","2015",""),
    ("DDJ-REV7",P,"","Old catalogue"),("DDJ-FLX10",P,"","Old catalogue")]),
  A("Pioneer XDJ-RX","Pioneer's all-in-one standalone system combining two players and a mixer around a screen.",P,"2015",PDJ,[
    ("XDJ-RX3",P,"2021","Two channels, effects matching the DJM-900NXS2")]),
  A("Denon DJ Prime 4","Four-channel standalone DJ system with 10-inch multi-touch display.","Denon DJ","",SEDA)],
 "m":[["DDJ-GRV6",P],["Prime GO+","Denon DJ"],["SC Live 4","Denon DJ"],["DJControl Inpulse T7","Hercules DJ"],["DJControl Starlight","Hercules DJ"],
      ["Traktor Kontrol X1 Mk3","Native Instruments"],["Traktor Kontrol Z1 MK2","Native Instruments"],["Party Mix III","Numark"],
      ["One MKII","Rane"],["Performer","Rane"],["Mixtour Pro","Reloop"],["DJ-505","Roland"]],
 "r":[["DDJ",P],["XDJ",P],["Prime","Denon DJ"],["Traktor","Native Instruments"],["Inpulse","Hercules DJ"],["Mixtrack","Numark"]]},
{"n":"DJ cartridge","a":"DJ needle · scratch cartridge · DJ stylus","d":"Phono cartridge built to track hard under scratching and back-cueing, often with an integrated headshell.",
 "t":["Conical stylus","Elliptical stylus","Integrated headshell body","Standard-mount on separate headshell"],
 "s":W+"Magnetic_cartridge",
 "x":[
  A("Ortofon Concorde","Ortofon's DJ pickup with integrated headshell body.","Ortofon","1979",W+"Ortofon",[
    ("Concorde second generation","Ortofon","2018","")]),
  A("Shure M44-7","Shure's widely used DJ cartridge, discontinued with the whole Shure phono line in summer 2018.","Shure","","https://www.thestranger.com/music/rip-shure-dj-cartridges-26128554/"),
  A("Ortofon OM","Ortofon's standard-mount cartridge series, sold with DJ styli.","Ortofon","1981",W+"Ortofon")]}]
K="knowledge"
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Technics","Japan","1965","Hi-fi and DJ turntables","Panasonic's audio brand, maker of the SL-1200 DJ turntable.",K,["SL-1200","SL-1500C"],["Technics SL-1200"]),
 B(P,"Japan","2014","DJ equipment","Pioneer's former DJ division, independent since 2014 and renamed AlphaTheta Corporation in 2020; owned by Noritsu.",PDJ,["CDJ","DJM","DDJ","XDJ","PLX","rekordbox"],["Pioneer CDJ","Pioneer DJM","Pioneer XDJ-RX"],["Denon DJ"]),
 B("Denon DJ","","","DJ equipment","DJ equipment brand of Denon, maker of the Prime standalone series.",K,["Prime","SC","X"],["Denon DJ SC6000","Denon DJ Prime 4"],[P]),
 B("Vestax","Japan","1977","DJ equipment","Tokyo maker of DJ mixers, turntables and controllers, founded by Hidesato Shiino; bankrupt in 2014.",VX,["PMC","PDX","VCI","QFO"],["Vestax PMC-05Pro","Vestax VCI-100"]),
 B("Rane","United States","1981","Pro audio and DJ equipment","Audio maker from Mukilteo, Washington, owned by inMusic since 2016.",W+"Rane_Corporation",["Seventy-Two","MP2015","One","Performer"],["Rane Seventy-Two","Rane MP2015"]),
 B("Allen & Heath","United Kingdom","1968","Mixing consoles","English mixing-console maker from Penryn, Cornwall, part of Audiotonix; Xone is its DJ line.",W+"Allen_%26_Heath",["Xone"],["Allen & Heath Xone:92"]),
 B("Ortofon","Denmark","1918","Phono cartridges","Danish cartridge maker founded in Copenhagen.",W+"Ortofon",["Concorde","OM"],["Ortofon Concorde"]),
 B("Shure","United States","1925","Microphones and audio","American audio maker that made phono cartridges until 2018.",K,[],["Shure M44-7"]),
 B("Bozak","United States","","DJ mixers and loudspeakers","Rudy Bozak's company, maker of the first commercial DJ mixer.",W+"DJ_mixer",[],["Bozak CMA-10-DL2"]),
 B("Hercules DJ","France","","DJ controllers","Guillemot's DJ controller brand.",K,["DJControl Inpulse"],["Hercules DJ Console"]),
 B("Native Instruments","Germany","1996","Music software and controllers","Berlin music software maker, home of Traktor.",K,["Traktor"],["Native Instruments Traktor Kontrol S4"]),
 B("Reloop","Germany","","DJ equipment","German DJ equipment brand.",K,["RP"],[]),
 B("Audio-Technica","Japan","1962","Turntables, cartridges and headphones","Japanese audio maker of turntables and cartridges.",K,["AT-LP"],[]),
 B("Numark","United States","","DJ equipment","American DJ equipment brand, part of inMusic.",K,["Mixtrack"],[]),
]
notes=("Kept both old kinds (k142 DJ turntable, k141 DJ controller); added DJ media player, DJ mixer, DJ cartridge. Controller list trimmed from 19 to 12 models plus archetype versions: "
 "dropped duplicate 'Traktor Z1 MK2', Reloop Buddy and Ready, DDJ-FLX2 (entry-level duplicates); DDJ-REV7, DDJ-FLX10, XDJ-RX3 moved into archetypes. Turntable ranges SL1200/SL1500/SL50 dropped as redundant with models. "
 "Standalone all-in-ones are a type and archetypes (XDJ-RX, Prime 4). Left out: Allen & Heath Xone:62/96/DB4 and year of Xone:92 (allen-heath.com returned 403), Rane TTM 56/57 and Sixty-Two/Seventy (no retrieved page), "
 "Shure Whitelabel and M44-7 launch year, Ortofon Nightclub/Scratch lines, DJM-600/900/V10/S rotary series, XDJ-RX2, PMC-05 per-model years (Vestax page gives none), Stanton ST-150 (snippet only). "
 "Clones are a maker-free 'OEM direct-drive DJ deck' archetype sourced to a Bonedo review naming Hanpin; only the RP-5000 MK4 is linked to it as a version, other clones stay in m. djworx.com returned 503.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/E3/shelves/08_00.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
