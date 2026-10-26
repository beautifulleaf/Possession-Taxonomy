import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
mono = {"n":"Monophonic synthesizer","a":"mono synth · bass synth · semi-modular synth",
 "d":"Synthesizer that plays one note at a time, used for bass and lead lines; keyboard, desktop and semi-modular forms.",
 "t":["keyboard","desktop module","semi-modular","analogue","virtual analogue"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("Minimoog Model D","Minimoog","Portable three-oscillator analogue keyboard synth with a ladder filter that set the template for the mono synth.","Moog Music","1970",W+"Minimoog",
    [("Original Model D","Moog Music","1970–1981","built until July 1981"),("Minimoog 204E","Moog Music","1998","limited run"),("Minimoog Voyager","Moog Music","2002","updated Minimoog"),("Model D reissue","Moog Music","2016","produced to 2017"),("Model D reissue","Moog Music","2022",""),("SE-02","Roland","2017","compact Minimoog-modelled synth")],"walnut case · fold-up panel · 44 keys"),
  X("Korg MS-20","MS-20","Semi-modular analogue mono synth with patch panel and aggressive dual filters.","Korg","1978",W+"Korg_MS-20",
    [("Original MS-20","Korg","1978–1983",""),("MS-20 Mini","Korg","2013","scaled-down reissue"),("MS-20 Kit","Korg","2014","full-size self-assembly kit"),("MS-20M Kit","Korg","2015","desktop module kit"),("K-2","Behringer","2019","low-cost clone"),("MS-20 FS","Korg","2020","full-size reissue")],"full-size or mini keys · patch panel"),
  X("Roland TB-303","TB-303 · Bassline","Small sequenced bass synth whose squelchy filter slides defined acid house.","Roland","1981",W+"Roland_TB-303",
    [("Original TB-303","Roland","1981","designed by Tadao Kikumoto"),("TB-3 Touch Bassline","Roland","2014",""),("TB-03","Roland","2017","Boutique recreation"),("TD-3","Behringer","2019","clone")],"silver case · built-in step sequencer"),
  X("ARP Odyssey","Odyssey","Duophonic analogue keyboard synth, ARP's compact rival to the Minimoog.","ARP Instruments","1972",W+"ARP_Odyssey",
    [("Mk I (Model 2800)","ARP Instruments","1972–1975","white panel"),("Mk II (Models 2810–2815)","ARP Instruments","1975–1978",""),("Mk III (Models 2820–2823)","ARP Instruments","1978–1981",""),("ARP Odyssey reissue","Korg","2015","reduced-size keys; module and full-size FS versions followed"),("Odyssey","Behringer","2019","clone")],"Mk I–III panel colours · filter revision"),
  X("ARP 2600","2600","Semi-modular analogue synth with normalled patch points and built-in speakers, long used for teaching and sound design.","ARP Instruments","1971",W+"ARP_2600",
    [("Original 2600","ARP Instruments","1971–1981",""),("TTSH","Human Comparator","2013","PCB kits"),("ARP 2600 FS","Korg","2020","full-size reissue"),("2600","Behringer","2020","clone"),("ARP 2600M","Korg","2022","smaller version of the FS")],"cabinet with separate keyboard · patch cords"),
  X("Roland SH-101","SH-101","Light single-oscillator analogue mono synth with arpeggiator and sequencer, playable strapped on.","Roland","1982",W+"Roland_SH-101",
    [("Original SH-101","Roland","1982–1986","grey, red or blue case"),("SH-01A","Roland","2018","Boutique virtual-analogue version"),("MS-101","Behringer","2019","clone with MIDI and USB")],"case colour · optional modulation grip"),
 ],
 "m":[["Messenger","Moog Music"],["Grandmother","Moog Music"],["Subsequent 37","Moog Music"]]}
poly = {"n":"Polyphonic synthesizer","a":"poly synth · workstation · FM synth · virtual analogue",
 "d":"Synthesizer that plays several notes at once with patch memory; analogue, digital, FM, sample-based and hybrid engines.",
 "t":["keyboard","desktop or rack module","analogue","digital","FM","hybrid","workstation","MPE"],
 "s":W+"Sequential_Circuits_Prophet-5",
 "x":[
  X("Sequential Prophet-5","Prophet-5","Five-voice analogue poly synth with full patch memory, designed by Dave Smith and John Bowen.","Sequential","1978",W+"Sequential_Circuits_Prophet-5",
    [("Rev 1","Sequential","1978","hand-assembled; 182 made"),("Rev 2","Sequential","","cassette patch storage"),("Rev 3","Sequential","","CEM chips; almost 6,000 made"),("Prophet-10","Sequential","1981","10 voices, two keyboards"),("Prophet-5 Rev 4","Sequential","2020","USB, MIDI, velocity, aftertouch"),("Pro-16","Behringer","2025","prototype shown at NAMM")],"walnut case · revision"),
  X("Roland Juno-60 / Juno-106","Juno","Six-voice analogue poly with one oscillator per voice and built-in chorus.","Roland","1982",W+"Roland_Juno-60",
    [("Juno-6","Roland","1982","predecessor without patch memory"),("Juno-60","Roland","1982–1984",""),("Juno-106","Roland","1984","successor with MIDI"),("JU-06A","Roland","2019","Boutique, switchable Juno-60/106"),("Juno-X","Roland","2022","")],"chorus I/II · 61 keys"),
  X("Roland Jupiter-8","Jupiter-8 · JP-8","Eight-voice analogue flagship poly with split and layer modes.","Roland","1981",W+"Roland_Jupiter-8",
    [("Jupiter-8","Roland","1981–1985",""),("JP-08","Roland","2015","Boutique, 4 voices"),("Jupiter-X / Jupiter-Xm","Roland","2019",""),("JT Mini","Behringer","2024","clone")],""),
  X("Yamaha DX7","DX7","Digital FM synth that became the best-selling synth of the 1980s.","Yamaha","1983",W+"Yamaha_DX7",
    [("DX7","Yamaha","1983",""),("TX7","Yamaha","1985","desktop module"),("DX7II","Yamaha","1987",""),("Reface DX","Yamaha","2015","compact FM synth")],"6 operators · 32 algorithms"),
  X("Oberheim OB-X","OB-X","Analogue poly built on Oberheim's discrete voice circuits, with a big brassy sound.","Oberheim","1979",W+"Oberheim_OB-X",
    [("OB-X","Oberheim","1979–1981",""),("OB-Xa","Oberheim","1981","replaced the OB-X"),("OB-X8","Sequential","2022","made with Tom Oberheim")],"4, 6 or 8 voices"),
  X("Korg M1","M1","Sample-based synth workstation with sequencer and effects, among the best-selling synths.","Korg","1988",W+"Korg_M1",
    [("M1","Korg","1988–1995",""),("M1R","Korg","","rack module"),("T-series","Korg","1989","successor"),("01/W","Korg","1991","successor")],"61 keys · PCM cards"),
  X("Access Virus","Virus","German virtual-analogue poly synth that dominated trance and dance production around 2000.","Access Music","1997",W+"Access_Virus",
    [("Virus A","Access Music","1997",""),("Virus B","Access Music","1999",""),("Virus C","Access Music","2002",""),("Virus TI","Access Music","2005","computer integration"),("Virus TI2","Access Music","2009","discontinued by 2024")],"desktop, rack or keyboard"),
  X("Nord Lead","Nord Lead","Red virtual-analogue synth from Sweden with modelling engine and hands-on panel.","Clavia","1995",W+"Nord_Lead",
    [("Nord Lead","Clavia","1995",""),("Nord Lead 2","Clavia","1997",""),("Nord Lead 3","Clavia","2001",""),("Nord Lead 2X","Clavia","2003",""),("Nord Lead 4","Clavia","2013",""),("Nord Lead A1","Clavia","2014","")],"red case · rack versions"),
 ],
 "m":[["MiniFreak","Arturia"],["PolyBrute","Arturia"],["Osmose","Expressive E"],["Muse","Moog Music"],["Moog One","Moog Music"],["Prophet-6","Sequential"]],
 "r":[["Roland Boutique","Roland"]]}
mod = {"n":"Modular synthesizer and Eurorack module","a":"modular · Eurorack · modular synthesizer module",
 "d":"Synthesizer built from separate function modules patched with cables, sold as systems, cases and single modules such as Eurorack.",
 "t":["module","case and power","complete system","Eurorack","5U / Moog format","Buchla format"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("Moog modular","Moog synthesizer · Moog modular system","Large cabinet modular of oscillators, filters and envelopes patched by cord; the first commercial synthesizer.","Moog Music","1964",W+"Moog_synthesizer",
    [("Original modular systems","Moog Music","1965–1981","modules such as 921 oscillator, 911 envelope, 902 amplifier"),("Modular 55","Moog Music","1975","system shown in source"),("Modular reissues","Moog Music","2014","production resumed")],"cabinet size · module complement"),
  X("Buchla 100 / 200","Buchla Modular Electronic Music System","West-coast modular built around complex oscillators, low-pass gates and touch plates rather than a keyboard.","Buchla","1963",W+"Buchla_Electronic_Musical_Instruments",
    [("100 series","Buchla","1963","installed at San Francisco Tape Music Center 1965"),("200 series","Buchla","1970",""),("Music Easel","Buchla","1973","portable system; reintroduced 2013"),("200e","Buchla","2004","")],"banana-jack patching · touch-plate controllers"),
  X("Eurorack (Doepfer A-100)","Eurorack · A-100","Small 3U module format with 3.5 mm jack patching and ±12 V power, now the main modular standard.","Doepfer","1996",W+"Eurorack",
    [("A-100","Doepfer","1996","first Eurorack system; format specified 1995")],"3U height · width in HP · 10- or 16-pin power"),
 ],
 "m":[["A-100","Doepfer"],["Braids","Mutable Instruments"],["Clouds","Mutable Instruments"],["Rings","Mutable Instruments"],["Marbles","Mutable Instruments"],["Grandmother","Moog Music"]]}
# drop duplicated Grandmother from modular m (kept in mono)
mod["m"]=[m for m in mod["m"] if m[0]!="Grandmother" and m[0]!="A-100"]
ther = {"n":"Theremin","a":"thereminvox · etherphone",
 "d":"Electronic instrument played without contact, pitch and volume set by the hands' distance from two antennas.",
 "t":["kit","assembled","with CV outputs"],
 "s":"https://www.sweetwater.com/shop/by-category",
 "x":[
  X("RCA Theremin","RCA Thereminvox","First mass-produced theremin, built under licence from Leon Theremin's patents.","RCA","1929",W+"Theremin",[],"cabinet on legs · two antennas"),
  X("Moog Etherwave","Etherwave · Etherwave Standard","Moog's long-running performance theremin, sold assembled or as a kit.","Moog Music","",
    "https://vintageking.com/blog/moog-etherwave-theremin/",
    [("Etherwave Standard","Moog Music","","best-selling model"),("Etherwave (2022)","Moog Music","2022","CV outputs, headphone output")],"hardwood cabinet · brass antennas"),
 ],
 "m":[["Theremini","Moog Music"]]}
def B(n,c,f,seg,d,sig,s,lines=None,rel=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines or [],"eras":[],"sig":sig,"sc":["synth"],"rel":rel or [],"s":s}
    return b
brands=[
 B("Moog Music","USA","1953","Synthesizers & theremins","Founded as R. A. Moog Co. by Robert Moog; based in Asheville, North Carolina; owned by inMusic since 2023.",["Minimoog Model D","Moog modular","Moog Etherwave"],W+"Moog_Music"),
 B("Korg","Japan","1962","Synthesizers & keyboards","Japanese electronic instrument maker, owner of the ARP name since its 2015 reissues.",["Korg MS-20","Korg M1"],"knowledge",rel=["ARP Instruments"]),
 B("Roland","Japan","1972","Synthesizers, drum machines & keyboards","Japanese electronic instrument maker founded by Ikutaro Kakehashi.",["Roland TB-303","Roland SH-101","Roland Juno-60 / Juno-106","Roland Jupiter-8"],"knowledge",lines=["Boutique"]),
 B("ARP Instruments","USA","1969","Synthesizers","American synth maker founded by Alan R. Pearlman; closed 1981, name revived by Korg.",["ARP Odyssey","ARP 2600"],"knowledge",rel=["Korg"]),
 B("Sequential","USA","1974","Synthesizers","Founded by Dave Smith as Sequential Circuits in San Francisco; owned by Focusrite since 2021.",["Sequential Prophet-5"],W+"Sequential_(company)",rel=["Oberheim"]),
 B("Yamaha","Japan","1887","Instruments & audio","Japanese maker of pianos, synths, wind instruments and audio.",["Yamaha DX7"],"knowledge"),
 B("Oberheim","USA","","Synthesizers","American synth maker founded by Tom Oberheim.",["Oberheim OB-X"],"knowledge",rel=["Sequential"]),
 B("Access Music","Germany","","Synthesizers","German maker of the Virus virtual-analogue synth line.",["Access Virus"],W+"Access_Virus"),
 B("Clavia","Sweden","","Keyboards & synthesizers","Swedish maker of red Nord keyboards and synths.",["Nord Lead"],"knowledge",lines=["Nord"]),
 B("Buchla","USA","1963","Modular synthesizers","Founded by Don Buchla in Berkeley, California; assets owned by Buchla U.S.A. since 2018.",["Buchla 100 / 200"],W+"Buchla_Electronic_Musical_Instruments"),
 B("Doepfer","Germany","","Modular synthesizers","German maker run by Dieter Döpfer in Gräfelfing; created the Eurorack format.",["Eurorack (Doepfer A-100)"],W+"Doepfer",lines=["A-100","Dark Energy"]),
 B("Mutable Instruments","France","","Eurorack modules","Émilie Gillet's open-source Eurorack module maker; closed December 2022.",[],"https://www.synthtopia.com/content/2022/12/11/mutable-instruments-r-i-p/",lines=["Braids","Clouds","Rings","Marbles","Grids","Tides"]),
 B("Make Noise","USA","","Eurorack modules","American Eurorack maker based in Asheville, North Carolina.",[],"knowledge"),
 B("Intellijel","Canada","","Eurorack modules and cases","Canadian maker of Eurorack modules and cases.",[],"knowledge"),
 B("Behringer","Germany","1989","Audio gear & synth clones","Founded by Uli Behringer in Willich; part of Music Tribe; known for low-cost clones of classic synths.",[],W+"Behringer"),
 B("Arturia","France","1999","Synthesizers & software","Grenoble maker founded by Frédéric Brun and Gilles Pommereuil; software emulations and hybrid synths.",[],W+"Arturia",lines=["MiniFreak","MicroFreak","PolyBrute","MiniBrute"]),
 B("Expressive E","France","","Expressive controllers & synths","French maker of the Osmose expressive keyboard synth.",[],"knowledge"),
 B("RCA","USA","1919","Electronics","American electronics company that made the first mass-produced theremin in 1929.",["RCA Theremin"],"knowledge"),
]
# Mutable country not on a fetched page: drop
for b in brands:
    if b["n"]=="Mutable Instruments": b["c"]=""
out={"kinds":[mono,poly,mod,ther],"brands":brands,"traditions":[],
 "notes":"Split old Synthesizer into Monophonic and Polyphonic. MiniFreak (6-voice per Arturia page), Osmose and Muse moved to Polyphonic; Messenger stays mono; Roland Boutique range placed under Polyphonic (spans both). Eurorack maker register: Doepfer, Mutable Instruments, Make Noise, Intellijel as brands (Make Noise/Intellijel from knowledge, no fetched page; no modules listed for them). Left out: Behringer Model D clone year (not on fetched page), Moog Etherwave launch year, Claravox, Mutable founding year/country, Oberheim/Clavia founding years (unsure). Wikipedia API rate-limited (429), all pages via WebFetch."}
p='work/E3/shelves/02_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
