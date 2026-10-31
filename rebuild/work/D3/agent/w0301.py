import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from lib import *
SC=WP+'Schiit_Audio'; DQ='https://darko.audio/2018/11/a-short-film-about-the-chord-qutest/'; DCS='https://www.stereonet.com/zh/reviews/dcs-bartok-dac-review'
BM='https://tmraudio.com/blogs/the-gearhead/how-benchmark-media-systems-set-and-still-set-the-standard-in-hi-fi'
O2='https://spectrum.ieee.org/nwavguy-the-audio-genius-who-vanished'; HA=WP+'Headphone_amplifier'
kinds=[
K("DAC and headphone amplifier","DAC/amp combo · USB DAC dongle · portable DAC/amp","External device that converts digital audio and drives headphones in one unit.","https://apos.audio/collections/brand-spotlight-fiio",
  ["desktop","portable with battery","USB dongle","Bluetooth receiver"],
  [X("Chord Mojo / Hugo","Chord Electronics","",DQ,"Chord's FPGA-based DAC/headphone amplifiers with Rob Watts's filter code, from pocket Mojo to desktop Hugo TT.",
     [("Hugo 2","Chord Electronics","","portable"),("Mojo","Chord Electronics","","pocket"),("Mojo 2","Chord Electronics","",""),("Hugo TT","Chord Electronics","","desktop"),("DAVE","Chord Electronics","","flagship")]),
   X("RME ADI-2 DAC","RME","2018","https://www.soundonsound.com/reviews/rme-adi-2-dac","Studio-maker DAC with headphone and IEM outputs and five-band parametric EQ; a simplified ADI-2 Pro.",
     [("ADI-2 Pro","RME","","with A-D conversion"),("ADI-2 DAC","RME","2018","")]),
  ],
  [("FiiO K9","FiiO"),("FiiO K11","FiiO"),("FiiO K17","FiiO"),("FiiO KA15","FiiO"),("FiiO BTR5","FiiO"),("Topping DX3 Pro+","Topping"),("Topping DX5 II","Topping"),("SMSL DL200","SMSL"),("iBasso DC04","iBasso"),("Rotel DX-3","Rotel")]),
K("DAC","digital-to-analogue converter · D/A converter","External device whose designed function is converting digital audio to analogue.","https://www.richersounds.com/hi-fi",
  ["R-2R / multibit","delta-sigma","FPGA","valve output stage","with preamplifier"],
  [X("dCS Ring DAC converters","dCS","1996",DCS,"British high-end converters built on dCS's own Ring DAC; Elgar was its first consumer DAC.",
     [("Elgar","dCS","1996","first dCS consumer DAC"),("Debussy","dCS","2008",""),("Vivaldi","dCS","2012","flagship system"),("Rossini","dCS","",""),("Bartók","dCS","2020","first dCS with a headphone output")]),
   X("Benchmark DAC1","Benchmark","",BM,"Converter from a studio-equipment maker that became an audiophile reference.",
     [("DAC1","Benchmark","",""),("DAC1 Pre","Benchmark","",""),("DAC1 HDR","Benchmark","",""),("DAC3","Benchmark","","current model")]),
   X("Chord Qutest","Chord Electronics","2018",DQ,"Standalone DAC derived from the Hugo 2 without battery or headphone output."),
   X("Schiit Bifrost","Schiit","2011",SC,"User-upgradable DAC, Schiit's first.",
     [("Bifrost","Schiit","2011",""),("Modi","Schiit","","small DAC"),("Modi+","Schiit","",""),("Modi Multibit 2","Schiit","",""),("Yggdrasil+","Schiit","","flagship")]),
  ],
  [("SMSL SU-2","SMSL"),("SMSL R100","SMSL"),("FiiO Warmer Desktop R2R Tube Buffer and DAC","FiiO")]),
K("Headphone amplifier","headphone amp","External device whose designed function is amplifying a headphone signal.","https://apos.audio/collections/brand-spotlight-fiio",
  ["solid-state","valve","hybrid","OTL valve","balanced","portable"],
  [X("Objective2 (O2)","","2011",O2,"Open-source headphone amplifier by the anonymous engineer NwAvGuy, built and sold by several firms.",
     [("O2","JDS Labs","","assembled version"),("O2","Epiphany Acoustics","","Hi-Fi World award 2012")],a="O2"),
   X("CMoy","","",HA,"Popular DIY op-amp headphone amplifier small enough to fit in a mint tin."),
   X("Schiit Asgard / Valhalla / Lyr","Schiit","2010",SC,"Schiit's first headphone amplifiers, which started the company.",
     [("Asgard","Schiit","2010",""),("Valhalla","Schiit","2010",""),("Lyr","Schiit","2011","hybrid, high power"),("Magni Heretic","Schiit","","")]),
   X("Woo Audio WA2","Woo Audio","","https://www.audioadvisor.com/products/woo-audio-wa2-single-ended-otl-headphone-amplifier","Hand-built all-valve single-ended OTL headphone amplifier with 6AS7/6080 power valves."),
   X("Musical Fidelity X-Cans","Musical Fidelity","",HA,"Headphone amplifier using two 6922 valves."),
   X("Little Dot Mk III","Little Dot","",HA,"Valve headphone amplifier."),
  ],
  [("Topping L70","Topping"),("SMSL H400 Mk2","SMSL"),("SMSL H200","SMSL"),("E1DA #9039S","E1DA"),("iBasso Kunlun","iBasso"),("xDuoo TA-66","xDuoo")]),
K("Master clock","word clock · reference clock","External unit whose designed function is supplying a reference clock signal to a DAC, streamer or transport in a hi-fi system.","https://www.audiovenue.uk/product-tag/dap/"),
K("Bluetooth audio adapter","Bluetooth audio transmitter · Bluetooth audio receiver","External unit that sends audio from a TV or player to wireless headphones or speakers, or receives Bluetooth audio for an amplifier.","https://apos.audio/collections/dac-amps?page=4",["transmitter","receiver","transmitter/receiver"]),
]
brands=[
 B("Chord Electronics","United Kingdom","1989","Premium","FPGA DACs","Kent maker founded by John Franks; DACs designed with Rob Watts.","knowledge",["Mojo","Hugo","Qutest","DAVE"]),
 B("dCS","United Kingdom","1987","Professional & flagship","Ring DAC","Cambridge digital-audio maker that began in defence and studio converters.","knowledge",["Elgar","Vivaldi","Bartók"]),
 B("Benchmark","United States","1983","Specialist","studio-grade DACs","Founded by Allen Burdick in Texas; based in Syracuse, New York.",BM,["DAC1","AHB2"]),
 B("RME","Germany","","Professional & flagship","studio converters","German maker of studio audio interfaces and converters.","knowledge",["ADI-2 DAC"]),
 B("Schiit","United States","2010","Value","desktop DACs and amps","California maker founded by Jason Stoddard and Mike Moffat.",SC,["Magni","Modi","Bifrost","Valhalla"]),
 B("JDS Labs","United States","","Value","measured headphone amps","American maker that put the O2 amplifier into production.",O2,["O2"]),
 B("Woo Audio","United States","","Artisan & independent","valve headphone amps","New York maker of hand-built valve headphone amplifiers.","https://www.audioadvisor.com/products/woo-audio-wa2-single-ended-otl-headphone-amplifier",["WA2"]),
 B("Musical Fidelity","United Kingdom","1982","Premium","amplifiers","London hi-fi maker founded by Antony Michaelson.","knowledge",["X-Cans"]),
]
notes=("All five kinds kept. DAC/amp combo cut from 14 to 10 models plus Chord and RME archetypes (dropped FiiO K19, KA11, Topping DX1 II, xDuoo XD05 Pro); old Chord Hugo 2/Mojo 2 moved into the Chord archetype, Qutest into its own. Portable, dongle and Bluetooth forms as types. Headphone amp kept 6 old models. Master clock and Bluetooth adapter stay kind-level with no models. "
 "Left out (no retrieved page): Topping, FiiO and iFi archetypes (no reference page found), JDS Labs Atom, Schiit Jotunheim, Burson, Cavalli, Mytek, dCS Vivaldi clock, Benchmark DAC1 year (not on page). Chord, dCS, RME and Musical Fidelity brand facts from knowledge.")
write('03_01',kinds,brands,notes)
