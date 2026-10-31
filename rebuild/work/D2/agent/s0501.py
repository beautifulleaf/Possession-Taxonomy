import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP='https://en.wikipedia.org/wiki/'
GJ='https://gearjunkie.com/technology/best-walkie-talkies'; OE='https://outdoorempire.com/best-walkie-talkies/'
ZS='https://www.zipscanners.com/pages/trx1-compare'; RS='https://www.rtl-sdr.com/review-airspy-vs-sdrplay-rsp-vs-hackrf/'
def V(n,mk,y='',d=''):
    v={"n":n,"mk":mk,"y":y}
    if d: v["d"]=d
    return v
def X(n,mk,y,s,d,vs,a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":vs}
    if dt: x["dt"]=dt
    return x
M="Motorola"; U="Uniden"
kinds=[
 {"n":"Walkie-talkie","a":"handheld two-way radio · FRS radio · PMR446 radio","d":"Battery-powered push-to-talk radio held in the hand, usually on licence-free channels.",
  "t":["FRS (US, licence-free)","GMRS (US, licensed)","PMR446 (Europe, licence-free)","UHF CB (Australia)","toy"],"s":GJ,
  "x":[X("Motorola SCR-536 Handie-Talkie",M,"1941",WP+"Walkie-talkie","The first handheld walkie-talkie, an AM wartime set; a militaria collector icon.",[V("SCR-300",M,"1940","backpack set first called 'walkie-talkie'"),V("SCR-536",M,"1941")]),
       X("Motorola Talkabout",M,"",OE,"Motorola's consumer FRS/GMRS walkie-talkie line.",[V("T600 H2O Talkabout",M,"","waterproof")])],
  "m":[["Mountain Radio","Rocky Talkie"],["Expedition Radio","Rocky Talkie"],["T71 X-Talker","Midland"],["GXT1000VP4","Midland"],["GXT1050VP4","Midland"],["ACXT1035R FLT","Cobra"],["CXT195","Cobra"],["BC Link 2.0","Backcountry Access"],["DXFRS800","DeWALT"],["RT22","Retevis"],["Rino","Garmin"]]},
 {"n":"CB radio","a":"citizens band radio · 27 MHz radio","d":"Transceiver for the licence-free 27 MHz citizens band, used by truckers and hobbyists.","t":["mobile","base","handheld","AM","AM/FM","AM/SSB"],"s":WP+"Citizens_band_radio",
  "x":[X("Cobra 29","Cobra","","https://www.overdriveonline.com/gear/product/14866877/classic-cb-fixture-in-many-cabs","Full-size 40-channel mobile CB, a fixture in truck cabs for some 50 years.",[V("29 LTD","Cobra","","4 W, 40 channels; later AM/FM")])],
  "m":[["18 WX ST II","Cobra"],["50 WX ST","Cobra"],["PC78LTXFM",U],["Bearcat 980SSB",U],["ME-4","TEAM Electronic"],["T-800","Thunderpole"],["T-X","Thunderpole"],["TRC-222","Realistic"]]},
 {"n":"Radio scanner","a":"police scanner · scanning receiver","d":"Receiver that scans many channels for active transmissions such as police, fire and air traffic.","t":["handheld","base / mobile","trunking","digital (P25, DMR, NXDN)"],"s":WP+"Scanner_(radio)",
  "x":[X("Uniden BCD436HP",U,"2013",ZS,"Uniden's digital handheld trunking scanner, the reference hobby scanner of the 2010s.",[V("BCD436HP",U,"2013")]),
       X("Uniden SDS100",U,"2018",ZS,"Uniden's SDR-based digital handheld scanner with simulcast support.",[V("SDS100",U,"2018")]),
       X("Whistler TRX-1","Whistler","2016",ZS,"Whistler's digital handheld scanner with NXDN and DMR.",[V("TRX-1","Whistler","2016")])],
  "m":[["BCD325P2",U],["BCT-15",U],["UB360",U],["IC-R5","Icom"],["MCP-1","Tennelec"]]},
 {"n":"SDR receiver","a":"software-defined radio · SDR dongle","d":"Radio receiver that sends raw signals to a computer, where software does the tuning and decoding.","t":["RTL-SDR dongle","wideband receiver","HF receiver","transmit-capable"],"s":RS,
  "x":[X("RTL-SDR dongle","","",RS,"Cheap RTL2832U/R820T2 USB TV-tuner dongle used as a wideband SDR; the entry point to the hobby.",[]),
       X("SDRplay RSP","SDRplay","",RS,"UK-designed 12-bit wideband SDR receiver line.",[V("RSP","SDRplay","","original"),V("RSP1A","SDRplay","","wideband pick"),V("RSPdx","SDRplay")]),
       X("Airspy","Airspy","",RS,"12-bit SDR receivers, with HF+ models for shortwave.",[V("Airspy","Airspy","","original; HF needs Spyverter"),V("Airspy Mini","Airspy"),V("Airspy R2","Airspy"),V("Airspy HF+ Discovery","Airspy","","HF pick")])],
  "m":[["HackRF One","Great Scott Gadgets"]]},
 {"n":"Pager","a":"beeper","d":"Small receiver that alerts its carrier and shows short messages sent over a paging network.","t":["tone-only","voice","numeric","alphanumeric","two-way"],"s":"https://www.radiodepot.com/collections/our-motorola-minitor-vi-products",
  "x":[X("Motorola Minitor",M,"1970s",WP+"Minitor","Voice pager carried by volunteer firefighters and EMS crews.",
        [V("Minitor",M,"1970s","original"),V("Minitor II",M,"1992"),V("Minitor III",M,"1999"),V("Minitor IV",M),V("Minitor V",M,"2005"),V("Minitor VI",M,"2014"),V("Minitor VII",M,"2025")]),
       X("Motorola Pageboy",M,"",WP+"Pager","Early Motorola pager used in New York.",[V("Pageboy II",M,"late 1970s")]),
       X("Motorola Bravo",M,"",WP+"Pager","Motorola's numeric pager, the everyday beeper.",[V("Bravo",M)])],
  "m":[["Bellboy","Bell System"],["Datalink Beepwear Pro","Timex"]]},
]
def B(n,c,f,seg,kf,d,s,sig=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
brands=[
 B("Motorola","United States","1928","Professional & flagship","two-way radio","American radio maker behind the Handie-Talkie, Talkabout and Minitor.","knowledge",["Motorola SCR-536 Handie-Talkie","Motorola Talkabout","Motorola Minitor"]),
 B("Cobra","United States","","Mainstream","CB radio","American maker of CB radios and consumer walkie-talkies.","knowledge",["Cobra 29"]),
 B("Midland","United States","","Mainstream","walkie-talkies, CB","American maker of consumer two-way radios.","knowledge"),
 B("Uniden","Japan","","Mainstream","scanners, CB","Japanese radio maker, best known for Bearcat scanners.","knowledge",["Uniden BCD436HP","Uniden SDS100"]),
 B("Whistler","United States","","Mainstream","scanners","American maker of scanners and radar detectors.","knowledge",["Whistler TRX-1"]),
 B("SDRplay","United Kingdom","","Specialist","SDR receivers","UK maker of RSP software-defined receivers.",RS,["SDRplay RSP"]),
 B("Airspy","","","Specialist","SDR receivers","Maker of Airspy SDR receivers designed by Benjamin Vernoux and Youssef Touil.",RS,["Airspy"]),
]
w('D2','05_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Walkie-talkie: trade models MOTOTRBO R7 and Kenwood Viking VP8000 (P25) and MOTOTRBO range dropped (scope rule); consumer FRS/GMRS/PMR446 picks from GearJunkie and Outdoor Empire tests; source switched to GearJunkie test. Pager kept with old source; Minitor II-VII kept as versions. New CB radio, Radio scanner, SDR receiver kinds sourced. Left out: President CB radios (no retrieved page), Uniden BCD536HP and Whistler TRX-2 (snippet only), Bearcat brand history."})
