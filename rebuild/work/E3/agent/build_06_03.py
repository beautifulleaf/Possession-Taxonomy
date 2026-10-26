import json, os
W='https://en.wikipedia.org/wiki/'
WAH=W+'Wah-wah_pedal'; WH=W+'DigiTech_Whammy'; DC=W+'MXR_Dyna_Comp'; EV=W+'Eventide,_Inc.'
BOSS=W+'Boss_Corporation'; L6=W+'Line_6_(company)'; EHX=W+'Electro-Harmonix'; DUN=W+'Dunlop_Manufacturing'
NG=W+'Noise_gate'; FX=W+'Effects_unit'; LOOP='https://in.boss.info/promos/loop_station/'
GE7='https://www.bonedo.de/artikel/boss-ge-7-equalizer-test/'; EB='https://www.bonedo.de/?p=712606'
ROSS='https://delaydude.de/en/ross-compressor-reissue/'; H90='https://www.soundonsound.com/news/eventide-reveal-h90-harmonizer-pedal'
def v(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Multi-effects processor","a":"multi-effects pedal · multi-FX · effects processor","d":"Single unit offering many effect types, often with presets and switching, for one instrument signal chain.",
 "t":["floor multi-effects","pedal-format multi-effects","tabletop","rack-mount","with amp modelling (see Amp modeller)"],
 "s":"https://www.sweetwater.com/c633--Amp_Modeling_Multi-effects_Pedals",
 "x":[
  {"n":"Eventide Harmonizer pedal (H9 / H90)","a":"H9 · H90","d":"Eventide's algorithm-loaded stompbox line descended from its studio Harmonizers, covering pitch, delay, reverb and modulation.","mk":"Eventide","y":"2022 (H90)","s":H90,
   "v":[v("H9 Harmonizer","Eventide","","Single-knob predecessor"),v("H9 Max","Eventide","","H9 with the full algorithm set; its algorithms carried into the H90"),v("H90 Harmonizer","Eventide","2022","62 algorithms, two insert points, OLED display, ARM architecture from the H9000"),v("H910 Harmonizer","Eventide","1975","Original studio Harmonizer rack unit, the line's ancestor")],
   "dt":"algorithm set · number of simultaneous effects · insert loops · MIDI/expression control"},
  {"n":"Line 6 Helix","a":"Helix Floor · HX","d":"Floorboard modeller and multi-effects platform with matching smaller pedal-format units.","mk":"Line 6","y":"2015","s":L6,
   "v":[v("Helix","Line 6","2015","Original floorboard modeller"),v("Helix LT","Line 6","","Lower-cost floor version"),v("HX Stomp","Line 6","","Compact pedal-format unit"),v("HX Stomp XL","Line 6","","Larger HX Stomp with more footswitches")],
   "dt":"floor / compact format · footswitch count · I/O and effects loops"},
  {"n":"Boss ME series","a":"ME-5","d":"Boss floor multi-effects line with stored presets.","mk":"Boss","y":"1988","s":FX,
   "v":[v("ME-5","Boss","1988","Early preset multi-effects unit")],"dt":"effect blocks · preset count · expression pedal"}],
 "m":[["Plethora X3","TC Electronic"],["Plethora X5","TC Electronic"]],
 "r":[["Multi-effects","Boss"],["Plethora","TC Electronic"]]},
{"n":"Looper","a":"looper pedal · loop station · phrase sampler","d":"Unit that records and plays back loops of the live signal for overdubbing.",
 "t":["single-switch stompbox","twin-switch","multitrack floor looper","tabletop looper","stereo"],
 "s":"https://www.andertons.co.uk/boss-rc-1-compact-loop-station-looper-pedal",
 "x":[
  {"n":"Boss Loop Station","a":"RC series","d":"Boss looper line that took looping mainstream, from compact stompboxes to multitrack floor and tabletop units.","mk":"Boss","y":"2001","s":LOOP,
   "v":[v("DSD-2 / DSD-3","Boss","mid-1980s","Earlier digital delay/samplers with looping"),v("RC-20","Boss","2001","Twin switch, five minutes' sampling, overdub, 11 memory slots"),v("RC-20XL","Boss","2004","16 minutes' recording"),v("RC-2","Boss","2006","Compact single stompbox"),v("RC-50","Boss","2006","Three loop tracks"),v("RC-3","Boss","2011","Three hours' stereo recording, 99 loops, USB"),v("RC-30","Boss","2011","Two stereo tracks with faders, built-in effects"),v("RC-300","Boss","","Three-track floor unit after the RC-30"),v("RC-505","Boss","2013","Five stereo tracks, tabletop"),v("RC-1","Boss","2014","Simplest model, 12 minutes' stereo, circular loop indicator"),v("RC-202","Boss","2016","Compact tabletop version of the RC-505"),v("RC-1-BK","Boss","2018","Limited black RC-1 marking one million units sold")],
   "dt":"tracks · recording time · footswitches · rhythm guide · stompbox / floor / tabletop"},
  {"n":"Line 6 DL4","a":"DL4 Delay Modeler","d":"Digital delay pedal with a built-in looper, widely used as a looping tool.","mk":"Line 6","y":"1999","s":L6,
   "v":[v("DL4","Line 6","1999","Original"),v("DL4 MkII","Line 6","2024","Revised version")],"dt":"loop time · delay models"},
  {"n":"Electro-Harmonix multitrack looper","a":"2880 · 45000","d":"Electro-Harmonix multitrack looping recorders allowing complex looping and overdubbing.","mk":"Electro-Harmonix","y":"","s":EHX,
   "v":[v("2880","Electro-Harmonix","","Multi-track looping and overdubbing"),v("45000 Multi-Track Looping Recorder","Electro-Harmonix","","Multitrack looper")],"dt":"tracks · storage medium"}]},
{"n":"Wah pedal","a":"wah-wah · wah effect · auto-wah · envelope filter","d":"Foot-rocked or envelope-driven unit that sweeps a resonant filter across the signal.",
 "t":["treadle wah","auto-wah / envelope filter","optical wah","signature voicings","mini wah"],
 "s":"https://www.perfectcircuit.com/dunlop-gcb95-cry-baby-pedal.html",
 "x":[
  {"n":"Vox Clyde McCoy wah","a":"Vox wah-wah · V846","d":"The original wah: a transistor mid-boost sweep built into a Vox Continental organ volume pedal and sold with Clyde McCoy's endorsement.","mk":"Vox","y":"1967","s":WAH,
   "v":[v("Clyde McCoy","Vox","1967","Built by Brad Plunkett at Warwick Electronics/Thomas Organ in 1966; released February 1967 with McCoy's image, later his signature"),v("V846","Vox","","Italian-made Vox wah"),v("King Vox Wah","Vox","1968","Late-1960s version like Hendrix's")],
   "dt":"inductor · pot taper · era (US/Italian manufacture)"},
  {"n":"Cry Baby","a":"Crybaby · GCB95","d":"The wah sold under the Cry Baby name, first by Thomas Organ in America, now Dunlop's standard wah line.","mk":"Dunlop","y":"","s":WAH,
   "v":[v("Thomas Organ Cry Baby","Thomas Organ","1970","US-market name for the Vox wah, made by JEN"),v("Cry Baby (GCB95)","Dunlop","","Standard current model"),v("Crybaby 535Q","Dunlop","","Adjustable-voicing model")],
   "dt":"range / Q · inductor · signature voicings"},
  {"n":"Q-Tron","a":"envelope filter","d":"Electro-Harmonix envelope filter linked to Mike Beigel and the Mu-tron III circuit.","mk":"Electro-Harmonix","y":"","s":EHX,
   "v":[],"dt":"filter mode · sensitivity · boost"}],
 "m":[["V-Wah","Roland"]]},
{"n":"Pitch-shifter pedal","a":"pitch shifter · harmonizer · octaver · whammy","d":"Unit that adds or replaces the signal with a shifted pitch (octave, harmony, whammy).",
 "t":["treadle pitch-bend","polyphonic octave","intelligent harmonizer","detune","drop tune"],
 "s":"https://www.thomann.co.uk/electro_harmonix_pitch_fork_pitch_shifter.htm",
 "x":[
  {"n":"DigiTech Whammy","a":"Whammy","d":"Treadle-controlled digital pitch shifter bending up to two octaves; the first mass-market digital pitch shifter.","mk":"DigiTech","y":"1989","s":WH,
   "v":[v("Whammy","DigiTech","1989","Original, monophonic"),v("Whammy IV","DigiTech","","MIDI I/O"),v("Bass Whammy","DigiTech","","Bass version"),v("Whammy DT","DigiTech","","Later model (2010s)"),v("Whammy (5th generation)","DigiTech","","Later generation")],
   "dt":"mono / polyphonic · MIDI · drop tune · harmony intervals"},
  {"n":"Electro-Harmonix POG","a":"Polyphonic Octave Generator","d":"Polyphonic octave generator mixing sub and upper octaves with the dry signal.","mk":"Electro-Harmonix","y":"2005","s":EHX,
   "v":[v("POG","Electro-Harmonix","2005","Original"),v("POG 2","Electro-Harmonix","2009","Revised"),v("Micro POG","Electro-Harmonix","","Compact XO housing"),v("HOG","Electro-Harmonix","","Harmonic Octave Generator")],
   "dt":"octave voices · filter · housing size"}],
 "m":[["Pitch Fork","Electro-Harmonix"]]},
{"n":"Compressor pedal","a":"compressor · compression sustainer · comp","d":"Unit that narrows the dynamic range of the instrument signal for evenness and sustain.",
 "t":["OTA (Dyna Comp type)","optical","VCA","FET","with blend control","bass compressor"],
 "s":"https://www.sweetwater.com/c631--Guitar_Pedals_and_Effects",
 "x":[
  {"n":"MXR Dyna Comp","a":"Dyna Comp","d":"Two-knob compressor (Output, Sensitivity) that set the pattern for guitar compressor pedals.","mk":"MXR","y":"1970s","s":DC,
   "v":[v("Dyna Comp (script logo)","MXR","1970s","Original vintage version"),v("Dyna Comp (block logo)","MXR","","Later version with new transistors"),v("'76 Vintage Dyna Comp","MXR","","Reissue"),v("Super Comp","MXR","","Adds an Attack control")],
   "dt":"logo era · OTA chip · controls"},
  {"n":"Ross Compressor","a":"Ross Comp","d":"Late-1970s OTA compressor based on the script Dyna Comp, the basis of many boutique clones.","mk":"Ross","y":"late 1970s","s":ROSS,
   "v":[v("Ross Compressor","Ross","late 1970s","Original"),v("Ross Compressor reissue","Ross","2018","Original design with true bypass, US-made"),v("Compressor","Keeley","","Well-known derivative"),v("Bi-Comprossor","Analog Man","","Derivative"),v("SP Compressor","Xotic","","Derivative adding a mix control"),v("Ego Compressor","Wampler","","Derivative"),v("Tone Press","Barber","","Derivative adding a mix control")],
   "dt":"original / reissue / derivative · blend control"},
  {"n":"Boss CS series","a":"Compression Sustainer · CS-3","d":"Boss compact compressor line.","mk":"Boss","y":"1977","s":BOSS,
   "v":[v("CS-1","Boss","1977","First Boss compressor"),v("CS-3 Compression Sustainer","Boss","","Later compact model")],"dt":"controls · era"}],
 "m":[["Compressor Plus","Keeley"],["Tone Corset","Electro-Harmonix"]]},
{"n":"EQ pedal","a":"equaliser pedal · graphic EQ · parametric EQ","d":"Unit that boosts or cuts set frequency bands of the instrument signal.",
 "t":["graphic","parametric","bass EQ"],"s":"https://www.sweetwater.com/c631--Guitar_Pedals_and_Effects",
 "x":[{"n":"Boss GE-7","a":"GE-7 Equalizer","d":"Seven-band graphic EQ pedal (100 Hz–6.4 kHz, ±15 dB) sold almost unchanged since 1981.","mk":"Boss","y":"1981","s":GE7,
   "v":[v("GE-6","Boss","1977","Six-band predecessor"),v("GE-7","Boss","1981","Seven bands plus level slider")],"dt":"band count · level slider · era"}],
 "m":[["10-Band EQ","MXR"]]},
{"n":"Noise gate","a":"noise suppressor · noise reduction pedal","d":"Unit that mutes the signal below a set threshold to cut hum and hiss.",
 "t":["single-channel","with loop for gating a drive chain"],"s":"https://www.thomannmusic.com/isp_technologies_decimator_pedal.htm",
 "m":[["Decimator X","ISP Technologies"],["NS-2 Noise Suppressor","Boss"]]},
{"n":"Volume pedal","a":"volume swell pedal","d":"Foot-rocked pedal that sets the level of the instrument signal.",
 "t":["passive (high or low impedance)","active","stereo","with tuner out","volume/expression combo"],"s":"https://www.thomann.co.uk/ernie_ball_vpjr_volumepedal.htm",
 "x":[{"n":"Ernie Ball volume pedal","a":"VP · VP Jr","d":"Cable-driven aluminium volume pedal introduced in 1977, a pedalboard standard.","mk":"Ernie Ball","y":"1977","s":EB,
   "v":[v("VP Jr","Ernie Ball","","Compact version with tuner output"),v("EB6110 40th Anniversary","Ernie Ball","2017","VP Jr size, two swell rates, Kevlar cable")],"dt":"size · impedance · taper switch · mono / stereo"}],
 "m":[["Volume Pedal","Fender"]]}]
brands=[
{"n":"Boss","c":"Japan","f":"1973","seg":"Effects pedals","d":"Roland division best known for compact pedals and the Loop Station.","lines":["Compact pedals","Loop Station (RC)","ME multi-effects"],"sig":["Boss GE-7","Boss Loop Station","Boss CS series"],"rel":["Roland"],"s":BOSS},
{"n":"Eventide","c":"United States","f":"1971","seg":"Studio and pedal effects","d":"New Jersey effects maker that introduced the Harmonizer.","lines":["Harmonizer","Factor stompboxes","H9 / H90"],"sig":["Eventide Harmonizer pedal (H9 / H90)"],"s":EV},
{"n":"Line 6","c":"United States","f":"1996","seg":"Modelling amps and effects","d":"California modelling pioneer (POD), owned by Yamaha since 2014.","lines":["POD","Helix","DL4"],"sig":["Line 6 Helix","Line 6 DL4"],"rel":["Yamaha"],"s":L6},
{"n":"Electro-Harmonix","c":"United States","f":"1968","seg":"Effects pedals","d":"New York pedal maker founded by Mike Matthews.","lines":["POG","Q-Tron","loopers"],"sig":["Electro-Harmonix POG","Q-Tron"],"s":EHX},
{"n":"Dunlop","c":"United States","f":"1965","seg":"Accessories and effects","d":"Benicia, California firm founded by Jim Dunlop Sr.; owns Cry Baby, MXR and Way Huge.","lines":["Cry Baby","MXR","Way Huge"],"sig":["Cry Baby"],"rel":["MXR","Way Huge"],"s":DUN},
{"n":"MXR","c":"United States","seg":"Effects pedals","d":"Pedal maker now part of Dunlop.","sig":["MXR Dyna Comp"],"rel":["Dunlop"],"s":DUN},
{"n":"Vox","c":"United Kingdom","seg":"Amplifiers and effects","d":"British amplifier brand whose name went on the first wah pedal.","sig":["Vox Clyde McCoy wah"],"s":"knowledge"},
{"n":"DigiTech","c":"United States","seg":"Effects pedals","d":"Maker of the Whammy pitch shifter.","sig":["DigiTech Whammy"],"s":WH},
{"n":"Ross","c":"United States","seg":"Effects pedals","d":"1970s pedal brand revived in 2018 with a reissued Compressor.","sig":["Ross Compressor"],"s":ROSS},
{"n":"Ernie Ball","c":"United States","seg":"Strings and accessories","d":"Strings and accessories maker whose volume pedal dates from 1977.","sig":["Ernie Ball volume pedal"],"s":EB}]
notes=("All 8 planned kinds kept (old names 'Wah effect', 'Pitch-shifter effect', 'Compressor effect', 'EQ effect' renamed to planned pedal names). "
"Left out (could not confirm on a retrieved page): EHX 720 Stereo Looper, Boss PS pitch shifters, Boss FV volume pedals, Eventide H9 year, Cry Baby/MXR acquisition years, ISP/NS-2 archetypes (kept as flat models). "
"Helix overlaps the Amp modeller kind on the amplifiers shelf; kept here as the brief asks, merger may cross-link. Reverb.com Ross history blocked (403); used delaydude.de instead. "
"Ross reissue maker kept as 'Ross' (page names rossaudibles.com only as pre-order link). Whammy DT/5th-gen years not given in text, left blank.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/06_03.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
