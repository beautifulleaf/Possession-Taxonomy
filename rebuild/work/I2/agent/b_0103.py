import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Sample pack","a":"loop pack · one-shots","d":"Recorded loops and one-shot sounds held as files for a music program.","t":["Loops","One-shots","Construction kit","WAV","REX"],"r":[["Sample Magic packs on Splice","Sample Magic"]],"s":"https://samplemagic.com/","x":[
 A("Splice Sounds","Splice","2015","Splice_(platform)","Subscription sample marketplace inside the Splice music platform."),
 A("Loopmasters packs and Loopcloud","Loopmasters","2003","Loopmasters","UK sample, MIDI and preset distributor, with the Loopcloud search subscription.")]},
{"n":"Virtual instrument library","a":"sampled instrument · orchestral library","d":"A sampled orchestral, piano or drum instrument played through a sampler such as Kontakt.","t":["Orchestral","Piano","Drums","Kontakt format","Standalone player"],"m":[["Kit Bag (Andy Findon)","Spitfire Audio"]],"s":W+"Vienna_Symphonic_Library","x":[
 A("Vienna Instruments and Synchron series","Vienna Symphonic Library","2000","Vienna_Symphonic_Library","Vienna orchestral sample libraries; since 2012 delivered by download or drive.",[("Synchron Player","Vienna Symphonic Library","","Dedicated sample player for the Synchron series")]),
 A("Spitfire BBC Symphony Orchestra","Spitfire Audio","2007","Spitfire_Audio","Orchestral recordings made at the BBC's Maida Vale Studios, from a London company founded in 2007.",[("LABS","Spitfire Audio","","Occasional free products"),("Pianobook","Spitfire Audio","2018","Free sampled-instrument project launched by Christian Henson")])]},
{"n":"Synth and effect preset pack","a":"soundbank","d":"Saved sound settings loaded by a synthesiser or effect plug-in.","t":["Serum","Vital","Massive","Effect chain"],"s":"https://payhip.com/b/4K8Jt","x":[
 A("Serum presets","Xfer","2014","Steve_Duda","Wavetable softsynth by Steve Duda released in 2014, with a large third-party preset market.")]},
{"n":"MIDI file","a":"Standard MIDI File","d":"A file of note and control data that a program plays or edits.","t":["Standard MIDI File","General MIDI","Song transcription (titles are out of scope)"],"r":[["Jacob's Piano MIDI bundles","Jacob's Piano"]],"s":"https://jacobspiano.com/midi-files/","x":[
 A("General MIDI","MIDI Manufacturers Association","1991","General_MIDI","Standard sound set of 128 programs and 47 percussion sounds, so files play alike on different devices.",[
  ("GS","Roland","1991","Sound Canvas superset"),("XG","Yamaha","1994","MU-series superset"),("GM2","MIDI Manufacturers Association","1999","32-note update reconciling GS and XG")])]},
{"n":"SoundFont and sample-format bank","a":"SF2 · SFZ · sample bank","d":"A bank of samples mapped across a keyboard with playing parameters, for synthesis from MIDI.","t":["SF2","SF3 (OGG compressed)","SFZ (plain text)","Kontakt NKI","GigaStudio"],"s":W+"SoundFont","x":[
 A("SoundFont","E-mu Systems and Creative Labs","1994","SoundFont","Sample-bank format first shipped on the Sound Blaster AWE32.",[
  ("SoundFont 2.0","E-mu Systems and Creative Labs","1996","Public specification, .sf2"),
  ("SoundFont 2.04","E-mu Systems and Creative Labs","2005","24-bit samples"),
  ("SF3","Werner Schweer","","Unofficial, OGG-compressed, made for MuseScore")])]},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Spitfire Audio","United Kingdom","2007","Premium","orchestral libraries","London company of Christian Henson and Paul Thomson.",W+"Spitfire_Audio"),
 B("Vienna Symphonic Library","Austria","2000","Premium","orchestral libraries","Vienna firm founded by Herb Tucmandl.",W+"Vienna_Symphonic_Library"),
 B("Splice","United States","","Mainstream","sample subscription","New York music platform; Splice Sounds launched 2015.",W+"Splice_(platform)"),
 B("Loopmasters","United Kingdom","2003","Mainstream","sample packs","Sample, MIDI and preset distributor; runs Loopcloud.",W+"Loopmasters"),
 B("Sample Magic","United Kingdom","","Specialist","dance sample packs","Sample library label; first distributed through Sounds to Sample (2007).",W+"Sounds_to_Sample"),
 B("Xfer","United States","","Specialist","Serum","Steve Duda's company, publisher of Serum (2014).",W+"Steve_Duda"),
 B("Native Instruments","Germany","","Professional & flagship","Kontakt sampler","Maker of the Kontakt sampler that hosts many third-party libraries.","knowledge"),
]
put('I2','01_03',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Cut the Sample Magic genre-pack SKU list (7 titles) to one range, and the Jacob's Piano titled MIDI bundles (4) to one range (titles out). Other preset packs (ArtsyGet Luminous Stars) dropped as a single-shop SKU; its source kept on Synth and effect preset pack. EastWest and Kontakt not archetypes: no usable fetched page (Kontakt page was a disambiguation). Founding year of Splice left blank (private beta 2013 only)."})
