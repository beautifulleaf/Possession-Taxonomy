import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP='https://en.wikipedia.org/wiki/'
L=WP+'List_of_amateur_radio_transceivers'; COL=WP+'Collins_Radio_Company'; DR=WP+'R._L._Drake_Company'
YA=WP+'Yaesu_(brand)'; EL=WP+'Elecraft'; KW='https://kenwoodcommunications.co.uk/comm_amateur/'
FX='https://www.wimo.com/de/flexradio-8600'; AT='https://www.wimo.com/en/at-d878uv2b2'
TK=WP+'Telegraph_key'; VB=WP+'Vibroplex'
def V(n,mk,y='',d=''):
    v={"n":n,"mk":mk,"y":y}
    if d: v["d"]=d
    return v
def X(n,mk,y,s,d,vs,a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":vs}
    if dt: x["dt"]=dt
    return x
I,Y,K,E,C,D="Icom","Yaesu","Kenwood","Elecraft","Collins Radio","Drake"
base=[
 X("Collins S-Line",C,"1958",COL,"Matched Collins receiver, transmitter and amplifier system; the classic collector station, made until 1978.",
   [V("75S-1 / 32S-1",C,"1958","original receiver and transmitter"),V("75S-3 / 32S-3",C,"","S-3 generation; -3A/-3B/-3C variants"),V("30S-1",C,"","kilowatt amplifier"),V("30L-1",C,"","desktop amplifier"),V("62S-1",C,"","6 m and 2 m transverter")],
   a="S/Line",dt="round or winged emblem · -3A/-3B/-3C variants"),
 X("Collins KWM-2",C,"",COL,"Compact Collins HF transceiver that replaced the KWM-1 and shared S-Line design.",
   [V("KWM-1",C,"1957","predecessor, first compact HF transceiver"),V("KWM-2",C)]),
 X("Drake 4-Line",D,"1965",DR,"Drake's matched transmitter and receiver 'twins' and the TR-4 transceiver.",
   [V("T-4X / R-4",D,"1965","original twins"),V("T-4XC / R-4C",D,"1973","C-Line"),V("TR-4",D,"","transceiver, made to 1978; TR-4C last"),V("L-4",D,"","matching linear amplifier")],a="Drake twins"),
 X("Drake 7-Line",D,"1978",DR,"Drake's solid-state, synthesised transceiver line.",[V("TR-7",D,"1978"),V("R-7",D,"1978","receiver"),V("L-7",D,"","linear amplifier")]),
 X("Yaesu FT-101",Y,"1970s",YA,"Valve-hybrid HF transceiver series that was very popular with 1970s amateurs.",[V("FT-101 series",Y,"1970s","tube hybrid")]),
 X("Kenwood TS-820S",K,"late 1970s",L,"Hybrid valve and solid-state HF transceiver with built-in power supply.",[V("TS-820",K,"","predecessor without frequency counter"),V("TS-820S",K)]),
 X("Kenwood TS-2000",K,"2000",L,"All-band base transceiver covering HF to 70 cm, made until 2018.",[V("TS-2000",K,"2000"),V("TS-2000X",K,"","adds 23 cm"),V("TS-B2000",K,"","no front panel"),V("TS-2000LE",K,"","black limited run")]),
 X("Icom IC-7300",I,"",L,"Icom's compact 100 W HF direct-sampling base rig.",[V("IC-7300",I)]),
 X("Icom IC-7610",I,"",L,"Icom's dual-receiver HF base transceiver.",[V("IC-7600",I,"","predecessor"),V("IC-7610",I)]),
 X("Icom IC-7800 / IC-7851",I,"",L,"Icom's top-of-range HF flagship transceivers.",[V("IC-7800",I),V("IC-7851",I)]),
 X("Yaesu FT-991A",Y,"2015",L,"Yaesu's HF to 70 cm all-mode base transceiver.",[V("FT-991",Y,"2015"),V("FT-991A",Y,"2016")]),
 X("Yaesu FTDX10",Y,"2020",L,"Yaesu's compact hybrid-SDR HF transceiver.",[V("FT-DX10",Y,"2020"),V("FTDX-10 Optima / FTX-1",Y,"2025")]),
 X("Yaesu FTDX101",Y,"",L,"Yaesu's flagship HF hybrid-SDR transceiver.",[V("FTDX-101D",Y),V("FTDX-101MP",Y,"","200 W")]),
 X("Kenwood TS-590",K,"",L,"Kenwood's mid-range HF/6 m base station.",[V("TS-590S",K),V("TS-590SG",K)]),
 X("Kenwood TS-890 / TS-990",K,"",KW,"Kenwood's current HF/50/70 MHz transceivers and the TS-990S flagship.",[V("TS-890S",K),V("TS-890SE2",K),V("TS-990S",K,"","HF flagship")]),
 X("Elecraft K3 / K4",E,"2008",EL,"Elecraft's high-end HF transceivers, top-ranked in Sherwood receiver tests.",[V("K3",E,"2008"),V("K3S",E,"2015"),V("K4",E,"2021","touchscreen, panadapter"),V("K4D",E)]),
 X("FlexRadio FLEX-6000 / 8000","FlexRadio","",FX,"Server-style SDR transceivers run from a PC, Mac or iPad client.",[V("FLEX-6600","FlexRadio"),V("FLEX-8400","FlexRadio"),V("FLEX-8600","FlexRadio","","builds on FLEX-6600"),V("FLEX-8600M","FlexRadio","","front-panel version")]),
]
mob=[
 X("Yaesu FT-857",Y,"",L,"Compact MF/HF/VHF/UHF multimode transceiver widely used as a mobile rig.",[V("FT-857",Y)]),
 X("Yaesu FTM-400",Y,"2012",L,"Yaesu's dual-band C4FM/FM mobile with colour touchscreen.",[V("FTM-400 series",Y,"2012–2015")]),
 X("Kenwood TM-D750",K,"",KW,"Kenwood's digital dual-band mobile with APRS.",[V("TM-D750E",K)]),
]
ht=[
 X("Baofeng UV-5R","Baofeng","2012",L,"Low-cost dual-band handheld sold since 2012; the most widespread entry-level HT.",
   [V("UV-5R","Baofeng","2012"),V("UV-82","Baofeng"),V("BF-F8HP","Baofeng"),V("UV-5X3","Baofeng")]),
 X("Yaesu VX series",Y,"1997",L,"Yaesu's compact rugged handhelds, VX-1R to VX-8R.",[V("VX-1R",Y,"1997"),V("VX-8R",Y,"","last of the series")]),
 X("Yaesu FT-5DR",Y,"2015",L,"Yaesu's C4FM Fusion dual-band handhelds.",[V("FT-2DR",Y),V("FT-3DR",Y),V("FT-5DR",Y,"2021")]),
 X("Kenwood TH-D75",K,"",KW,"Kenwood's 144/430 MHz D-STAR and APRS handheld.",[V("TH-D75E",K)]),
 X("Icom ID-52",I,"",L,"Icom's D-STAR digital handheld line.",[V("ID-31",I),V("ID-51",I),V("ID-52",I)]),
 X("AnyTone AT-D878UV","AnyTone","",AT,"DMR and FM dual-band handheld with VFO and APRS, popular for ham DMR.",[V("AT-D868UV","AnyTone","","predecessor"),V("AT-D878UV Plus","AnyTone"),V("AT-D878UV II Plus","AnyTone")]),
]
qrp=[
 X("Yaesu FT-817",Y,"2000",L,"Pioneering all-band, all-mode 5 W portable transceiver.",[V("FT-817",Y,"2000","original"),V("FT-818ND",Y,"2018")]),
 X("Elecraft KX3",E,"",EL,"Portable SDR transceiver covering 160 m–2 m, run without a computer.",[V("KX3",E),V("KX2",E,"","smaller 80–10 m sibling")],a="KX line"),
 X("Icom IC-705",I,"",L,"Icom's portable HF/VHF/UHF all-mode QRP transceiver.",[V("IC-705",I)]),
 X("Xiegu G90","Xiegu","",L,"Low-cost portable HF SDR transceiver.",[V("G90","Xiegu"),V("X6100","Xiegu"),V("X6200","Xiegu")]),
]
key=[
 X("Vibroplex Original bug","Vibroplex","1905",VB,"Semi-automatic 'bug' key with a pendulum for dits; in production over 100 years.",[V("Original","Vibroplex","1905","patented 1904"),V("Vibrokeyer","Vibroplex","","electronic variant")]),
 X("J-38 straight key","","WWII",TK,"US military straight key of the Second World War, widely reused by amateurs.",[]),
 X("Bencher iambic paddle","Bencher","",TK,"Commercial dual-lever iambic paddle used with an electronic keyer.",[]),
]
kinds=[
 {"n":"HF base transceiver","a":"base-station radio · base-station transceiver · HF rig","d":"Desktop amateur transceiver for a home station, usually 100 W on HF.","t":["superheterodyne","SDR (direct sampling)","valve or hybrid (vintage)","HF/VHF/UHF all-mode"],"s":L,"x":base,
  "m":[["IC-718","Icom"],["IC-7200","Icom"],["IC-9700","Icom"],["FT-891","Yaesu"],["FTDX-3000","Yaesu"],["TS-850S","Kenwood"]]},
 {"n":"Mobile transceiver","a":"vehicle two-way radio · vehicle-mounted two-way radio","d":"Amateur transceiver made to be installed in a vehicle, VHF/UHF FM or HF.","t":["VHF/UHF FM","HF mobile","digital (D-STAR, C4FM, DMR)"],"s":L,"x":mob,
  "m":[["FT-2900R","Yaesu"],["FTM-100","Yaesu"],["FTM-500","Yaesu"],["FTM-6000","Yaesu"],["DR-138/438","Alinco"],["CT 2000","Midland"]]},
 {"n":"Amateur handheld transceiver","a":"HT · ham handheld","d":"Battery handheld transceiver for the amateur VHF/UHF bands.","t":["single-band","dual-band","digital (D-STAR, C4FM, DMR)"],"s":L,"x":ht,
  "m":[["IC-2AT","Icom"],["FT-60","Yaesu"],["UV-K5","Quansheng"],["KG-UV9D","Wouxun"],["DJ-VX11","Alinco"]]},
 {"n":"Portable QRP transceiver","a":"QRP rig · field radio","d":"Low-power (about 5–10 W) transceiver for portable and field operating.","t":["factory-built","kit"],"s":L,"x":qrp,"m":[["G1M","Xiegu"],["X5105","Xiegu"]]},
 {"n":"Amateur antenna","a":"aerial","d":"Antenna for an amateur station, from wire dipoles to rotatable beams.","t":["dipole","doublet","vertical","Yagi beam","end-fed half-wave","end-fed long wire","full-wave loop","magnetic loop"],"s":"https://wiki.oarc.uk/hf:antennas"},
 {"n":"Antenna tuner","a":"ATU · antenna matching unit","d":"Box that matches a transceiver to an antenna's impedance.","t":["manual","automatic","remote (at the antenna)","L, T or pi network"],"s":WP+"Antenna_tuner","m":[["KAT500","Elecraft"],["MN-2000","Drake"]]},
 {"n":"Linear amplifier","a":"HF amplifier · PA","d":"Amplifier that raises a transceiver's output, typically to 500–1500 W.","t":["solid-state","valve (tube)"],"s":"https://www.wimo.com/en/amplifiers/hf-amplifiers",
  "m":[["1200S","Acom"],["1400S","Acom"],["2100","Acom"],["Signature Power Genius XL","4O3A"],["KPA500","Elecraft"],["KPA1500","Elecraft"],["KXPA100","Elecraft"],["MLA300","RM Italy"],["30L-1","Collins Radio"],["L-4","Drake"]]},
 {"n":"Morse key","a":"telegraph key · CW key","d":"Hand key or paddle for sending Morse code.","t":["straight key","sideswiper (cootie)","semi-automatic bug","single-lever paddle","iambic paddle"],"s":TK,"x":key,"m":[["Iambic Deluxe","Vibroplex"]]},
]
def B(n,c,f,seg,kf,d,s,sig=None,lines=None,rel=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    if lines: b["lines"]=lines
    if rel: b["rel"]=rel
    return b
brands=[
 B("Icom","Japan","1954","Professional & flagship","ham transceivers","Osaka radio maker, one of the big three amateur brands.",WP+"Icom_Incorporated",["Icom IC-7300","Icom IC-705","Icom IC-7610"],rel=["Yaesu","Kenwood"]),
 B("Yaesu","Japan","1959","Professional & flagship","ham transceivers","Tokyo-founded amateur radio maker, one of the big three.",YA,["Yaesu FT-817","Yaesu FT-101","Yaesu FT-991A"],rel=["Icom","Kenwood"]),
 B("Kenwood","Japan","","Professional & flagship","ham transceivers","Japanese electronics maker with a long amateur radio line.","knowledge",["Kenwood TS-590","Kenwood TS-2000"],rel=["Icom","Yaesu"]),
 B("Elecraft","United States","1998","Specialist","high-end HF, QRP","Watsonville, California maker of high-performance and portable HF rigs, founded by Wayne Burdick and Eric Swartz.",EL,["Elecraft K3 / K4","Elecraft KX3"]),
 B("FlexRadio","United States","","Specialist","SDR transceivers","American maker of server-style software-defined amateur transceivers.","knowledge",["FlexRadio FLEX-6000 / 8000"]),
 B("Collins Radio","United States","1933","Heritage manufactory","vintage S-Line","Cedar Rapids, Iowa radio maker whose S-Line is the classic vintage amateur station.",COL,["Collins S-Line","Collins KWM-2"],rel=["Drake"]),
 B("Drake","United States","1943","Heritage manufactory","vintage twins","Ohio maker of amateur and shortwave equipment from the 1950s to the 1980s.",DR,["Drake 4-Line","Drake 7-Line"],rel=["Collins Radio"]),
 B("Vibroplex","United States","1905","Heritage manufactory","bug keys","Maker of the original semi-automatic 'bug' Morse key, now in Knoxville, Tennessee.",VB,["Vibroplex Original bug"]),
 B("Baofeng","China","","Value","budget handhelds","Chinese maker of low-cost VHF/UHF handhelds.","knowledge",["Baofeng UV-5R"]),
 B("AnyTone","China","","Value","DMR handhelds","Chinese maker of DMR and analogue amateur handhelds.","knowledge",["AnyTone AT-D878UV"]),
 B("Xiegu","China","","Value","portable SDR","Chinese maker of low-cost portable HF SDR transceivers.","knowledge",["Xiegu G90"]),
 B("Bencher","United States","","Specialist","iambic paddles","American maker of Morse iambic paddles.","knowledge",["Bencher iambic paddle"]),
]
w('D2','05_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Old Base-station radio merged into HF base transceiver and Vehicle two-way radio into Mobile transceiver (old names kept as aliases); Motorola MOTOTRBO MTR3000/SLR8000/MTR2000 and APX 4500 trade models and ranges dropped (scope rule). New kinds sourced from Wikipedia list of amateur transceivers, OARC wiki, Antenna_tuner, WiMo amplifier listing, Telegraph_key. FT-817/818, KX3, IC-705, G90 placed under Portable QRP. Years left blank where no retrieved page gave them (IC-7300, IC-7610, IC-705, KWM-2). Left out: FlexRadio SDR-1000/FLEX-5000 (search snippet only), QRP kit models (no maker on retrieved page), Begali and Kent keys (not on retrieved pages)."})
