import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_[0],"mk":a_[1],"y":a_[2],"d":a_[3]} for a_ in v],"dt":dt}
GB=W+'Groovebox'
dm={"n":"Drum machine","a":"rhythm machine · beatbox · rhythm composer","d":"Electronic instrument that produces drum and percussion sounds and plays them from a built-in sequencer.",
 "t":["analogue synthesis","sample-based","hybrid analogue/digital","desktop","compact/pocket"],
 "s":"https://www.sweetwater.com/c643--Roland",
 "x":[
  X("Roland TR-808","808 · Rhythm Composer","Programmable analogue drum machine with a booming bass drum; the most-used drum machine on hit records.","Roland","1980",W+"Roland_TR-808",
    [("TR-808","Roland","1980–1983","original; about 12,000 built"),("TR-8","Roland","2010s","recreates 808 sounds electronically"),("TR-8S","Roland","2010s","recreates 808 sounds electronically; sample import"),("TR-08","Roland","2017","miniaturised 808 with MIDI, USB and speaker"),("RD-8 Rhythm Designer","Behringer","2019","unlicensed analogue recreation")],
    "original vs digital recreation vs analogue clone · condition · service mods"),
  X("Roland TR-909","909","Hybrid analogue and sampled drum machine, Roland's first with MIDI; foundational to techno and house.","Roland","1983",W+"Roland_TR-909",
    [("TR-909","Roland","1983","about 10,000 built; sampled cymbals"),("TR-09","Roland","2017","smaller version with extra features")],"original vs reissue · condition"),
  X("Roland CR-78 CompuRhythm","CR-78","First microprocessor drum machine, letting users store their own patterns; analogue sounds and preset rhythms.","Roland","1978",W+"Roland_CR-78",
    [("CR-78","Roland","1978","programmable"),("CR-68","Roland","","smaller, not programmable")],"condition · preset vs user patterns"),
  X("Linn LM-1 Drum Computer","LM-1","First drum machine to use samples of acoustic drums; a staple of 1980s pop.","Linn Electronics","1980",W+"Linn_LM-1",
    [("LM-1","Linn Electronics","1980","designed by Roger Linn"),("LinnDrum","Linn Electronics","1982–1985","cheaper successor, about 5,000 sold; often mislabelled LM-2")],"condition · sound-chip mods"),
  X("Oberheim DMX","DMX","Programmable digital drum machine with sampled drums, per-voice tuning and swing; used across new wave and hip-hop.","Oberheim","1980",W+"Oberheim_DMX",[],"condition · voice-card configuration"),
  X("Roland TR-606 Drumatix","606","Compact analogue drum machine designed to sync with the TB-303 bass synth.","Roland","1981",W+"Roland_TR-606",
    [("TR-606","Roland","1981–1984","32-pattern memory, DIN sync")],"condition · mods"),
  X("Roland TR-707","707","Roland's first all-sampled drum machine, with LCD and MIDI and DIN sync.","Roland","1985",W+"Roland_TR-707",
    [("TR-707","Roland","1985","8-bit samples"),("TR-727","Roland","1985","Latin percussion sounds")],"condition · memory cartridge"),
  X("Elektron Machinedrum lineage","Machinedrum · Analog Rytm · Syntakt","Swedish parameter-locking step-sequenced drum machines.","Elektron","2002","https://en.wikipedia.org/wiki/Elektron_(company)",
    [("Machinedrum SPS-1","Elektron","2002","digital drum synthesiser"),("Analog Rytm","Elektron","2014","analogue/sample hybrid"),("Analog Rytm MKII","Elektron","",""),("Syntakt","Elektron","2022","")],"generation · MKI/MKII"),
  X("Korg Volca rhythm units","Volca Beats · Volca Drum","Low-cost compact battery-powered drum machines in Korg's Volca range.","Korg","2013",W+"Korg_Volca",
    [("Volca Beats","Korg","2013","hybrid analogue/digital rhythm machine"),("Volca Drum","Korg","","digital percussion synthesiser")],"model · mods")],
 "m":[["Alesis SR-16","Alesis"],["Arturia DrumBrute Impact","Arturia"],["Behringer RD-78","Behringer"],["Behringer BMX","Behringer"],["Polyend Drums","Polyend"],["Roland TR-1000","Roland"]],
 "r":[["Roland AIRA Compact","Roland"],["Roland Boutique","Roland"],["Behringer RD6","Behringer"]]}
sm={"n":"Sampler","a":"sampling workstation · sampling drum machine · sampler-sequencer","d":"Electronic instrument that records, stores and plays back sound samples from its pads or keys.",
 "t":["keyboard","desktop","pad-based","rack-mount"],
 "s":"https://www.sweetwater.com/c643--Roland",
 "x":[
  X("Akai MPC","MPC · MIDI/Music Production Center","Pad-grid sampler and sequencer designed by Roger Linn; the defining hip-hop production instrument.","Akai Professional","1988",W+"Akai_MPC",
    [("MPC60","Akai Professional","1988","first model"),("MPC60 II","Akai Professional","1991",""),("MPC3000","Akai Professional","1993",""),("MPC2000","Akai Professional","1997–2000",""),("MPC2000XL","Akai Professional","1999–2004",""),("MPC4000","Akai Professional","2002–2008",""),("MPC1000","Akai Professional","2003",""),("MPC2500","Akai Professional","2005",""),("MPC500","Akai Professional","2006",""),("MPC5000","Akai Professional","2008–2012",""),("MPC X","Akai Professional","2017","standalone"),("MPC Live","Akai Professional","2017–2020","standalone, battery"),("MPC Live II","Akai Professional","2020",""),("MPC One","Akai Professional","2020",""),("MPC Live III","Akai Professional","",""),("MPC XL","Akai Professional","",""),("MPC Sample","Akai Professional","","")],
    "generation · computer-tethered vs standalone · memory and storage upgrades"),
  X("E-mu SP-1200","SP-12 · SP-1200","12-bit sampling drum machine whose gritty sound defined golden-age hip hop.","E-mu Systems","1987",W+"E-mu_SP-1200",
    [("SP-12","E-mu Systems","1985","predecessor, 'Drumulator II'"),("SP-1200","E-mu Systems","1987","original grey chassis"),("SP-1200 reissue","E-mu Systems","1993","black chassis, cooler power supply"),("SP-1200 Final Edition","E-mu Systems","1998","last run"),("SP-1200 reissue","Rossum Electro-Music","2021","announced November 2021")],"production run · chassis colour"),
  X("Fairlight CMI","Computer Musical Instrument","Early digital sampler-workstation whose Page R sequencer and orchestra hit shaped 1980s pop.","Fairlight","1979",W+"Fairlight_CMI",
    [("Series I","Fairlight","1979",""),("Series II","Fairlight","1982","Page R sequencer"),("Series IIx","Fairlight","1983","adds MIDI"),("Series III","Fairlight","1985","")],"series · options"),
  X("E-mu Emulator","Emulator · EII","Floppy-disk keyboard sampler series from E-mu.","E-mu Systems","1981",W+"E-mu_Emulator",
    [("Emulator","E-mu Systems","1981","first unit to Stevie Wonder"),("Emulator II","E-mu Systems","1984",""),("Emulator III","E-mu Systems","1987","")],"generation · sound library"),
  X("Ensoniq Mirage","Mirage","One of the first affordable sampler-synths; over 30,000 sold.","Ensoniq","1984",W+"Ensoniq_Mirage",[],"keyboard vs rack · storage"),
  X("Roland SP-404","SP-404 · 404","Compact 12-pad sampler with effects, central to lo-fi hip-hop.","Roland","2005",W+"Roland_SP-404",
    [("SP-303","Boss","2001","predecessor in the SP family"),("SP-404","Roland","2005",""),("SP-404SX","Roland","2009","SD card"),("SP-404A","Roland","2017",""),("SP-404MKII","Roland","2021",""),("SP-404MKII Stones Throw edition","Roland","2023","limited edition")],"generation · limited editions"),
  X("Elektron Octatrack","Octatrack DPS-1","Eight-track performance sampler with step sequencer, mixer and effects.","Elektron","2010",W+"Elektron_Octatrack",
    [("Octatrack DPS-1","Elektron","2010",""),("Octatrack MKII","Elektron","",""),("Anniversary Edition","Elektron","2020","limited run")],"MKI/MKII · edition"),
  X("Elektron Digitakt","Digitakt","Compact eight-track drum computer and sampler.","Elektron","2017","https://en.wikipedia.org/wiki/Elektron_(company)",
    [("Digitakt","Elektron","2017","announced"),("Digitakt II","Elektron","2024","")],"generation")],
 "m":[["Roland P-6","Roland"]],
 "r":[["Teenage Engineering EP","Teenage Engineering"],["Korg Electribe","Korg"]]}
gb={"n":"Groovebox","a":"all-in-one production box · standalone production system","d":"All-in-one instrument combining synth, drum and sample voices with a built-in pattern sequencer.",
 "t":["desktop","handheld/pocket","grid-based","keyboard"],
 "s":"https://www.thomannmusic.com/cat.html",
 "x":[
  X("Roland MC Groovebox","MC-303 · MC-505 · MC-707","Roland's MC series, which gave the groovebox its name.","Roland","1996",GB,
    [("MC-303","Roland","1996–1997","original 'Groovebox'"),("MC-505","Roland","1998","adds D-Beam and Megamix"),("MC-909","Roland","",""),("MC-808","Roland","",""),("MC-101","Roland","2019",""),("MC-707","Roland","2019","")],"generation"),
  X("Korg Electribe","Electribe","Korg's long-running series of grooveboxes and rhythm units.","Korg","1999",GB,[],"model · generation"),
  X("Native Instruments Maschine","Maschine","Pad-based groovebox controller-software system.","Native Instruments","2009",GB,[],"generation · standalone vs controller"),
  X("Teenage Engineering OP-1","OP-1","Portable synth, sampler and sequencer with AMOLED screen; Teenage Engineering's first product.","Teenage Engineering","2011",W+"Teenage_Engineering_OP-1",
    [("OP-1","Teenage Engineering","2011",""),("OP-1 Field","Teenage Engineering","","successor; now a core product")],"generation"),
  X("Novation Circuit","Circuit","Grid-based groovebox with two synth tracks and drum parts.","Novation","2015",W+"Novation_Digital_Music_Systems",
    [("Circuit","Novation","2015","two MiniNova-derived synth engines, four drum parts"),("Circuit Tracks","Novation","2021","synth-and-drums"),("Circuit Rhythm","Novation","2021","sample-based")],"model"),
  X("Teenage Engineering Pocket Operator","PO-10 · PO-20","Calculator-sized synthesiser, drum and sampler units.","Teenage Engineering","2015",W+"Teenage_Engineering",
    [("PO-10 series","Teenage Engineering","2015",""),("PO-20 series","Teenage Engineering","2016","")],"series · model")],
 "m":[["Ableton Push 3 Standalone","Ableton"]]}
ss={"n":"Step sequencer","a":"analogue sequencer · CV sequencer · MIDI sequencer","d":"Standalone device that plays a looping pattern of notes or triggers step by step to drive synths and drum machines.",
 "t":["analogue CV/gate","MIDI","desktop","modular module"],
 "s":W+"Music_sequencer",
 "x":[
  X("Moog 960 sequencer","960","Moog modular module with three rows of eight knobs; the most-used analogue sequencer.","Moog Music","",W+"Analog_sequencer",[],"original vs reissue module")]}
brands=[
 {"n":"Roland","c":"Japan","f":"1972","seg":"electronic instruments","d":"Japanese maker of synthesizers, drum machines and samplers, founded by Ikutaro Kakehashi in Osaka.","lines":["TR","SP","MC","AIRA","Boutique"],"sig":["TR-808","TR-909","SP-404","MC-303"],"rel":["Boss"],"s":W+"Roland_Corporation"},
 {"n":"Linn Electronics","c":"USA","f":"","seg":"drum machines (defunct 1986)","d":"Roger Linn's company that made the LM-1 and LinnDrum.","sig":["LM-1","LinnDrum"],"rel":["Akai Professional"],"s":W+"Roger_Linn"},
 {"n":"Oberheim","c":"USA","seg":"synthesizers and drum machines","d":"American maker of synthesizers and the DMX drum machine.","sig":["DMX"],"s":"knowledge"},
 {"n":"Elektron","c":"Sweden","f":"1998","seg":"drum machines, samplers, synths","d":"Gothenburg maker of step-sequenced instruments.","sig":["Machinedrum","Octatrack","Digitakt"],"s":"https://en.wikipedia.org/wiki/Elektron_(company)"},
 {"n":"Korg","c":"Japan","seg":"electronic instruments","d":"Japanese electronic instrument maker, also owner of Vox.","lines":["Volca","Electribe"],"sig":["Volca","Electribe"],"s":W+"Korg"},
 {"n":"Akai Professional","c":"","seg":"samplers and controllers","d":"Pro-audio brand descended from Japan's Akai, best known for the MPC.","lines":["MPC"],"sig":["MPC"],"rel":["Linn Electronics"],"s":W+"Akai"},
 {"n":"E-mu Systems","c":"USA","f":"1971","seg":"samplers (defunct)","d":"Santa Cruz-founded pioneer of samplers and sample-based drum machines.","sig":["Emulator","SP-1200"],"s":W+"E-mu_Systems"},
 {"n":"Fairlight","c":"Australia","seg":"digital workstations","d":"Sydney maker of the Fairlight CMI sampler-workstation.","sig":["Fairlight CMI"],"s":W+"Fairlight_CMI"},
 {"n":"Ensoniq","c":"USA","seg":"samplers and synths (defunct)","d":"American maker of affordable samplers, starting with the Mirage.","sig":["Mirage"],"s":W+"Ensoniq_Mirage"},
 {"n":"Teenage Engineering","c":"Sweden","f":"2005","seg":"design-led instruments","d":"Stockholm maker of the OP-1 and Pocket Operators.","lines":["OP","Pocket Operator","EP"],"sig":["OP-1","Pocket Operator"],"s":W+"Teenage_Engineering"},
 {"n":"Novation","c":"UK","f":"1992","seg":"controllers, synths, grooveboxes","d":"British maker of MIDI controllers, synthesizers and the Circuit grooveboxes.","lines":["Circuit"],"sig":["Circuit"],"s":W+"Novation_Digital_Music_Systems"},
 {"n":"Native Instruments","c":"Germany","seg":"music software and hardware","d":"Berlin maker of music software and the Maschine system.","sig":["Maschine"],"s":"knowledge"},
 {"n":"Moog Music","c":"USA","seg":"synthesizers","d":"American synthesizer maker whose modular systems included the 960 sequencer.","sig":["960 sequencer"],"s":"knowledge"},
 {"n":"Behringer","c":"Germany","f":"1989","seg":"budget audio and clones","d":"Willich-founded audio maker known for low-cost recreations of vintage instruments.","sig":["RD-8"],"s":W+"Behringer"},
 {"n":"Boss","c":"Japan","seg":"effects and compact instruments","d":"Roland-owned brand; made the SP-303 sampler.","rel":["Roland"],"s":"knowledge"}]
notes=("Kept all planned kinds; added Step sequencer (new, sourced to Music sequencer article). Removed duplicate P-6 (two entries -> Roland P-6). "
 "Moved old models into archetype versions (TR-8S, Analog Rytm MKII, Syntakt, Volca Drum, Octatrack MKII, SP-404MKII, MPC Live III/XL/Sample). "
 "Kept unattached old models in m (Alesis SR-16, DrumBrute Impact, BMX, RD-78, Polyend Drums, TR-1000, P-6, Push 3 Standalone). Dropped duplicated ranges "
 "(Roland TR, Elektron Analog, Korg Volca, Akai MPC, Novation Circuit, Pocket Operator) now covered by archetypes. Left out: Behringer RD-78 as CR-78 version and "
 "RD-9 as 909 version (not confirmed on a retrieved page); TR-8S as 909 version (only 808 link attested); MPC Key 61, Digitone, Monomachine, Yamaha RS7000, "
 "Toraiz SP-16 (no time/space); step-sequencer archetypes beyond Moog 960 (no retrieved source). Akai Professional country left blank (Akai brand ownership complex).")
out={"kinds":[dm,sm,gb,ss],"brands":brands,"traditions":[],"notes":notes}
p='work/E3/shelves/02_03.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('ok')
