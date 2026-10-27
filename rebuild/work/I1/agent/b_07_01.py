from common import *
D='https://blog.dubspot.com/plugins/best/'
def K(n,d,s,x,t=None,a='',m=None):
    k={'n':n,'a':a,'d':d,'s':s,'x':x}
    if t: k['t']=t
    if m: k['m']=m
    return k
comp=K('Compressor & dynamics plug-in','Plug-in that evens out or shapes loudness; many emulate named hardware compressors.','https://www.pluginboutique.com/categories/2-Effects',[
 A('Teletronix LA-2A','Tube optical leveller made by Teletronix from 1962 to 1969, reissued by Universal Audio from 1999; the most emulated vocal compressor.',WP+'LA-2A_Leveling_Amplifier',[V('UAD LA-2A','Universal Audio','2002','Included with the UAD-1 DSP card'),V('UAD Teletronix LA-2A Leveler Collection','Universal Audio','2013','LA-2, Gray and Silver versions'),V('Waves CLA-2A','Waves'),V('Avid BF-2A','Avid Technology','','Formerly Bomb Factory'),V('Cakewalk CA-2A','Cakewalk'),V('T-RackS White 2A','IK Multimedia'),V('VC 2A','Softube')],mk='Teletronix',y='1962'),
 A('UREI 1176','FET limiter introduced by UREI in 1967, reissued by Universal Audio in 1999-2000; revisions A to H.',WP+'1176_Peak_Limiter',[V('1176 Revision A','UREI','1967','June 1967'),V('1176LN (Revision C)','UREI','1970','Black panel, low-noise circuit'),V('1176 Revision H','UREI','','Silver faceplate; last original series'),V('UAD 1176 Classic Limiter Collection','Universal Audio','','Rev A, Rev E and 1176AE')],mk='UREI',y='1967'),
 A('SSL bus compressor','The VCA bus compressor from Solid State Logic consoles, widely copied for mix-bus glue.',D+'compressor',[V('SSL Native Bus Compressor 2','Solid State Logic'),V('SSL G-Master Buss Compressor','Waves'),V('The Glue','Cytomic','','SSL-style VCA bus compressor')],mk='Solid State Logic'),
 A('Fairchild 660 and 670','Tube limiters from the 1950s, modelled by Universal Audio for mix-bus glue.',D+'compressor',[V('UAD Fairchild Tube Limiter Collection','Universal Audio','','Mono 660 and stereo 670')],mk='Fairchild'),
 A('Tube-Tech CL 1B','Optical vocal compressor modelled by Softube.',D+'compressor',[V('Tube-Tech CL 1B Mk II','Softube','','Mk I and Mk II in one interface')],mk='Tube-Tech'),
 A('FabFilter Pro-C','FabFilter\'s modern stereo compressor with eight styles, and the multiband Pro-MB.',D+'compressor',[V('Pro-C 2','FabFilter','','Eight compression styles, sidechain EQ, mid/side'),V('Pro-C 3','FabFilter'),V('Pro-MB','FabFilter','','Multiband dynamics, up to six bands')],mk='FabFilter'),
 A('Tokyo Dawn Labs free dynamics','Free compressors from Tokyo Dawn Labs.',D+'compressor',[V('TDR Kotelnikov','Tokyo Dawn Records','','Free wideband dynamics processor'),V('TDR Molotok','Tokyo Dawn Records','','Free character compressor, eleven flavours')],mk='Tokyo Dawn Labs')],
 t=['hardware emulation','multiband','bus compressor','limiter','free'],m=M(('OTT','Xfer Records')))
eq=K('EQ & filter plug-in','Plug-in that boosts or cuts parts of the frequency range; includes surgical, dynamic and hardware-style EQs.',D+'compressor',[
 A('Pultec EQP-1A','Passive tube EQ made by Pulse Techniques (EQP-1 from 1956, EQP-1A 1961), the most imitated boost-and-cut EQ.',WP+'Pultec_EQP-1',[V('Pultec EQP-1','Pulse Techniques','1956','Made until 1981; revived from 2000'),V('Pultec EQP-1A','Pulse Techniques','1961','Added 20 Hz and 16 kHz settings'),V('Waves PuigTec EQ','Waves'),V('UA Pultec Passive EQ Collection','Universal Audio'),V('Avid Pultec Bundle','Avid Technology'),V('iZotope Ozone 8 Vintage EQ','iZotope'),V('Apogee FX Rack','Apogee')],mk='Pulse Techniques',y='1956'),
 A('FabFilter Pro-Q','FabFilter\'s surgical EQ, first released in 2009; Pro-Q 3 won a 2019 Engineering Emmy.',WP+'FabFilter',[V('Pro-Q','FabFilter','2009'),V('Pro-Q 3','FabFilter','2019','Engineering Emmy 2019'),V('Pro-Q 4','FabFilter','','Spectral Dynamics mode')],mk='FabFilter',y='2009'),
 A('TDR Nova','Free 4-band dynamic EQ from Tokyo Dawn Labs; the GE edition is paid.','https://samplefocus.com/blog/best-eq-plugins-of-2026',[V('TDR Nova','Tokyo Dawn Records','','Free; GE edition $60')],mk='Tokyo Dawn Labs'),
 A('Neve 1081','Neve console EQ emulated by Waves as V-EQ4.','https://samplefocus.com/blog/best-eq-plugins-of-2026',[V('V-EQ4','Waves')],mk='Neve'),
 A('Dynamic EQ plug-ins','EQs with dynamic processing on each band.','https://samplefocus.com/blog/best-eq-plugins-of-2026',[V('Infinity EQ 2','Slate Digital'),V('TotalEQ MK2','HoRNet'),V('Carbon Q','Mastering the Mix')]),
 A('Kilohearts Slice EQ','Surgical EQ with up to 32 filters.','https://samplefocus.com/blog/best-eq-plugins-of-2026',[V('Slice EQ','Kilohearts')],mk='Kilohearts')],
 t=['hardware-style passive EQ','surgical','dynamic EQ','filter','free'])
rev=K('Reverb plug-in','Plug-in that adds a room, plate, hall or spring space to a sound; many model named hardware units.',D+'reverb',[
 A('EMT 140 plate','The plate reverb introduced by EMT in the late 1950s, a metal sheet vibrated by a transducer.',WP+'Reverb_effect',[V('UA EMT 140 Classic Plate','Universal Audio'),V('SuperPlate','Soundtoys','','Models five electromechanical plates'),V('Valhalla Plate','Valhalla DSP'),V('ResoPlate','Reso Audio','','Physically modelled metal plates')],mk='EMT',y='1957'),
 A('Lexicon 224 and 480L','Lexicon\'s digital reverbs: the 224 (1978) and its successor the 480L (1986).',WP+'Lexicon_(company)',[V('Lexicon 224','Lexicon','1978','Shown at the 1978 AES convention'),V('Lexicon 480L','Lexicon','1986'),V('Relab LX480','Relab Development','','Emulates the 480L; dual engine'),V('Valhalla VintageVerb','Valhalla DSP','','Recreates late-1970s and 1980s digital reverbs')],mk='Lexicon',y='1978'),
 A('EMT 250','The 1976 digital reverb.',D+'reverb',[V('UA EMT 250 Classic Electronic Reverb','Universal Audio')],mk='EMT',y='1976'),
 A('Bricasti M7','Studio digital reverb emulated by LiquidSonics Seventh Heaven.',D+'reverb',[V('Seventh Heaven Professional','LiquidSonics','','Emulates the Bricasti M7')],mk='Bricasti'),
 A('Valhalla reverbs','Low-cost reverbs from ValhallaDSP, founded by Sean Costello in 2009.',WP+'ValhallaDSP',[V('Valhalla VintageVerb','Valhalla DSP'),V('Valhalla FutureVerb','Valhalla DSP'),V('Valhalla Room','Valhalla DSP'),V('Valhalla Shimmer','Valhalla DSP'),V('Valhalla Supermassive','Valhalla DSP','','Free')],mk='ValhallaDSP',y='2009'),
 A('FabFilter Pro-R','FabFilter\'s natural-space reverb with a Decay Rate control.',D+'reverb',[V('Pro-R 2','FabFilter')],mk='FabFilter'),
 A('Eventide reverbs','Algorithmic reverbs from Eventide.',D+'reverb',[V('Blackhole','Eventide'),V('SP2016 Reverb','Eventide'),V('UltraReverb','Eventide')],mk='Eventide')],
 t=['plate','room and hall','spring','shimmer','convolution','free'])
dly=K('Delay & modulation plug-in','Plug-in that repeats a sound or modulates it with short delays and low-frequency oscillators: echo, chorus, flanger, volume shaper.',D+'delay',[
 A('Echoplex','Tape-loop echo first made in 1959 by Mike Battle, with a moving record head to change delay time.',WP+'Echoplex',[V('Echoplex','Maestro','1959'),V('EchoBoy','Soundtoys','','Models about 30 vintage echo and tape units; includes EchoPlex, Space Echo, Memory Man styles')],mk='Maestro',y='1959'),
 A('Roland RE-201 Space Echo','1973 tape delay with several playback heads.',WP+'Delay_(audio_effect)',[V('Space Echo style in EchoBoy','Soundtoys')],mk='Roland',y='1973'),
 A('Binson Echorec','Delay that uses a rotating magnetic drum instead of tape.',WP+'Delay_(audio_effect)',[],mk='Binson'),
 A('Valhalla delays','Valhalla Delay emulates vintage tape, bucket-brigade and 1980s digital units; Freq Echo is free.',D+'delay',[V('Valhalla Delay','Valhalla DSP'),V('Valhalla Freq Echo','Valhalla DSP','','Free')],mk='ValhallaDSP'),
 A('FabFilter Timeless','Tape-style delay with extensive modulation.',D+'delay',[V('Timeless 3','FabFilter')],mk='FabFilter'),
 A('Character delays','BBD, tape and digital character delays from several makers.',D+'delay',[V('Colour Copy','u-he'),V('Replika XT','Native Instruments','','Five modelled delay modes'),V('Comeback Kid','Baby Audio'),V('H-Delay','Waves'),V('UltraTap','Eventide'),V('Crystallizer','Soundtoys','','Granular echo with pitch shifting and reverse echo')])],
 t=['tape delay','bucket-brigade','digital delay','chorus and flanger','volume shaper','granular'],m=M(('LFO Tool','Xfer Records')))
sat=K('Saturation & distortion plug-in','Plug-in that adds harmonic warmth, tape colour or overdrive.',D+'saturation',[
 A('Soundtoys Decapitator','Saturator based on Ampex, EMI, Neve and Culture Vulture circuit styles.',D+'saturation',[V('Decapitator','Soundtoys','','Five analogue-gear styles on one switch'),V('Radiator','Soundtoys'),V('Little Radiator','Soundtoys')],mk='Soundtoys'),
 A('FabFilter Saturn','Multiband distortion with 28 styles and extensive modulation.',D+'saturation',[V('Saturn 2','FabFilter')],mk='FabFilter'),
 A('Ampex ATR-102','Two-track mastering tape machine.',D+'saturation',[V('UAD Ampex ATR-102','Universal Audio')],mk='Ampex'),
 A('Studer A800','Multitrack two-inch tape machine.',D+'saturation',[V('UAD Studer A800','Universal Audio')],mk='Studer'),
 A('Sony TC-260 tape','Open-source tape model based on the Sony TC-260.',D+'saturation',[V('Chow Tape Model','Chowdhury DSP','','Free')],mk='Sony'),
 A('Tape plug-ins','Tape colour from several makers.',D+'saturation',[V('Satin','u-he'),V('Softube Tape','Softube'),V('TAIP','Baby Audio')]),
 A('Other saturators','Console and character saturators.',D+'saturation',[V('Black Box HG-2','Plugin Alliance'),V('VintageWarmer2','PSP Audioware'),V('Kelvin Tone Shaper','Tone Projects'),V('Harmonics','Softube'),V('Saturation Knob','Softube','','Free')])],
 t=['tape','tube and transformer','multiband','fuzz and overdrive'])
amp=K('Amp & cabinet simulator','Plug-in that models guitar and bass amps, cabinets, microphones and pedals.',D+'amp-sim',[
 A('Neural DSP plug-ins','Finnish company (founded 2017) known for amp-series and artist plug-ins and the Quad Cortex modeller.',WP+'Neural_DSP',[V('Archetype: Nolly X','Neural DSP'),V('Archetype: Gojira X','Neural DSP'),V('Fortin Nameless Suite X','Neural DSP'),V('Quad Cortex','Neural DSP','2020','Hardware modeller')],mk='Neural DSP',y='2017'),
 A('Line 6 Helix Native','Desktop version of the Helix modeller.',D+'amp-sim',[V('Helix Native','Line 6')],mk='Line 6'),
 A('AmpliTube','IK Multimedia\'s amp and effects modeller, released in 2002.',WP+'Amplifier_modeling',[V('AmpliTube','IK Multimedia','2002'),V('AmpliTube 5','IK Multimedia'),V('TONEX 2 Player','IK Multimedia','','Free capture-based modeller')],mk='IK Multimedia',y='2002'),
 A('Positive Grid BIAS FX','Preset-rich amp and effects suite.',D+'amp-sim',[V('BIAS FX 2','Positive Grid','','Standard and Pro tiers')],mk='Positive Grid'),
 A('Guitar Rig','Native Instruments\' multi-effects rack with amp models.',D+'amp-sim',[V('Guitar Rig 7','Native Instruments','','Machine-learning circuit modelling')],mk='Native Instruments'),
 A('Neural Amp Modeler','Free open-source capture-based modeller with a large library of captures.',D+'amp-sim',[V('TONE3000 Plugin','TONE3000','','Free')]),
 A('UA Paradise Guitar Studio','Eleven modelled tube amps with cabinets and mics; needs UAD hardware.',D+'amp-sim',[V('Paradise Guitar Studio','Universal Audio')],mk='Universal Audio')],
 t=['amp suite','capture-based','multi-effects rack','free','bass'])
pit=K('Pitch correction & vocal plug-in','Plug-in that tunes, aligns or reshapes vocals.',D+'vocal-pitch',[
 A('Auto-Tune','Antares pitch corrector released on 19 September 1997, created by Andy Hildebrand; the sound of the "Cher effect".',WP+'AutoTune',[V('Auto-Tune','Antares Audio Technologies','1997','19 September 1997'),V('Auto-Tune Pro X','Antares Audio Technologies'),V('Auto-Tune Artist','Antares Audio Technologies'),V('AutoTune Advanced','Antares Audio Technologies')],mk='Antares Audio Technologies',y='1997'),
 A('Melodyne','Celemony\'s note-based pitch and timing editor, shown at Winter NAMM 2001.',WP+'Celemony_Software',[V('Melodyne','Celemony','2001'),V('Melodyne 5','Celemony','2020'),V('Melodyne 5 Essential','Celemony','','Lighter edition')],mk='Celemony',y='2001'),
 A('Synchro Arts alignment tools','Tools for aligning, pitching and doubling vocals.',D+'vocal-pitch',[V('Revoice Pro 5','Synchro Arts'),V('VocALign Ultra','Synchro Arts')],mk='Synchro Arts'),
 A('Vocal effects and suites','Pitch-based vocal processors.',D+'vocal-pitch',[V('Little AlterBoy','Soundtoys'),V('Tune Real-Time','Waves'),V('Nectar 4','iZotope'),V('VocalSynth 2','iZotope'),V('MicroPitch','Eventide'),V('Topline Vocal Tune','Universal Audio')])],
 t=['automatic','note-based editing','harmony','formant','alignment'])
con=K('Console & channel-strip emulation','Plug-in that copies a mixing console channel (preamp, EQ, dynamics) or a whole console bus.',D+'channel-strip',[
 A('SSL 4000','Solid State Logic console channel, emulated by several makers.',D+'channel-strip',[V('SSL Native Channel Strip 2','Solid State Logic'),V('bx_console SSL 4000 E','Brainworx'),V('Waves SSL E-Channel','Waves')],mk='Solid State Logic'),
 A('Softube Console 1','Hardware control surface with matching channel software.',D+'channel-strip',[V('Console 1 Mk III','Softube')],mk='Softube'),
 A('Slate Digital Virtual Mix Rack','Virtual mix rack sold per month or perpetual.',D+'channel-strip',[V('Virtual Mix Rack','Slate Digital')],mk='Slate Digital'),
 A('Modular and AI strips','Modular or AI-assisted channel strips.',D+'channel-strip',[V('InfiniStrip','PSP Audioware'),V('Navy 2','Acustica Audio'),V('smart:chain','sonible'),V('Neutron 5','iZotope')])],
 t=['console emulation','modular strip','AI-assisted'])
mast=K('Mastering suite','Plug-in or bundle that covers the final steps of mastering: EQ, multiband dynamics, stereo width and limiting.',D+'mastering',[
 A('iZotope Ozone','iZotope\'s all-in-one mastering suite with an AI assistant.',WP+'IZotope',[V('Ozone 7','iZotope'),V('Ozone 10','iZotope','2022','13 September 2022'),V('Ozone 11','iZotope','','Elements, Standard and Advanced editions'),V('Ozone 12 Advanced','iZotope','','20 modules')],mk='iZotope'),
 A('Abbey Road TG Mastering Chain','Waves emulation of the EMI chain used in Abbey Road\'s mastering rooms.',D+'mastering',[V('Abbey Road TG Mastering Chain','Waves')],mk='Waves'),
 A('Mastering chains from other makers','Mastering processors and bus tools.',D+'mastering',[V('bx_masterdesk','Brainworx'),V('FG-X 2','Slate Digital'),V('Portico II Master Buss Processor','Rupert Neve Designs','','Modelled by McDSP'),V('CenterOne 3','Leapwing Audio'),V('FASTER MASTER','Mastering The Mix')])],
 t=['all-in-one suite','analog-style chain','online mastering'])
res=K('Audio restoration software','Tools that remove noise, hum, clicks, clipping and other defects from recordings.',D+'restoration',[
 A('iZotope RX','The standard repair and de-noise suite; the page says RX 12 replaces RX 11.',D+'restoration',[V('RX 6','iZotope'),V('RX 11','iZotope','2024','14 May 2024'),V('RX 11 Standard','iZotope')],mk='iZotope'),
 A('Steinberg SpectraLayers','AI spectral editor with unmixing and reconstruction.',D+'restoration',[V('SpectraLayers 13','Steinberg')],mk='Steinberg'),
 A('Acon Digital Acoustica','Editor and mastering suite with ML-based DeNoise 3 and DeHum 3.',D+'restoration',[V('Acoustica 8','Acon Digital')],mk='Acon Digital'),
 A('Celemony Capstan','Program that removes wow and flutter from recordings.',WP+'Celemony_Software',[V('Capstan','Celemony')],mk='Celemony'),
 A('Other repair tools','Targeted repair tools.',D+'restoration',[V('UNFILTER','Zynaptiq'),V('T-De-Breather','Techivation'),V('MDrumCleaner','MeldaProduction')])],
 t=['broadband repair','spectral editor','dialogue clean-up'])
met=K('Metering & analysis plug-in','Plug-in that shows loudness, spectrum, phase and tonal balance rather than changing the sound.',D+'metering',[
 A('Voxengo SPAN','Free real-time spectrum analyser.',D+'metering',[V('SPAN','Voxengo','','Free')],mk='Voxengo'),
 A('Youlean Loudness Meter','LUFS meter with true peak and loudness range; free with a Pro upgrade.',D+'metering',[V('Youlean Loudness Meter 2','Youlean')],mk='Youlean'),
 A('iZotope Insight','Loudness, spectrum, stereo and mix diagnostics suite.',D+'metering',[V('Insight 2','iZotope'),V('Tonal Balance Control 2','iZotope')],mk='iZotope'),
 A('Mastering The Mix metering','LUFS, phase and reference-track comparison.',D+'metering',[V('LEVELS','Mastering The Mix'),V('REFERENCE','Mastering The Mix')],mk='Mastering The Mix')],
 t=['loudness','spectrum','stereo and phase','reference comparison'])
brands=[B('FabFilter','Netherlands','2002','Premium','EQ, dynamics, reverb','Amsterdam plug-in maker founded in 2002; Pro-Q is its best-known product.',s=WP+'FabFilter'),
 B('ValhallaDSP','','2009','Specialist','reverb, delay','Sean Costello\'s reverb and delay plug-in company, founded in 2009.',s=WP+'ValhallaDSP'),
 B('Universal Audio','United States','1958','Professional & flagship','UAD plug-ins, hardware','Founded by Bill Putnam Sr. in 1958 and re-established in 1999; makes UAD emulations.',s=WP+'Universal_Audio_(company)'),
 B('Waves Audio','Israel','1992','Mainstream','plug-in bundles','Tel Aviv company founded in 1992 whose first product was the Q10 EQ.',s=WP+'Waves_Audio'),
 B('iZotope','United States','2001','Professional & flagship','Ozone, RX','Cambridge, Massachusetts maker of Ozone, RX and Neutron; owned by Boris FX in 2026.',s=WP+'IZotope'),
 B('Soundtoys','','','Premium','Decapitator, EchoBoy','Maker of Decapitator, EchoBoy and the Soundtoys bundle.',s=D+'saturation'),
 B('Antares Audio Technologies','United States','','Professional & flagship','Auto-Tune','Maker of Auto-Tune, created by Andy Hildebrand.',s=WP+'AutoTune'),
 B('Celemony','Germany','2000','Premium','Melodyne','Munich company founded in October 2000, maker of Melodyne and Capstan.',s=WP+'Celemony_Software'),
 B('Neural DSP','Finland','2017','Premium','amp modelling','Helsinki company that makes the Quad Cortex and amp plug-ins.',s=WP+'Neural_DSP'),
 B('IK Multimedia','Italy','','Mainstream','AmpliTube, T-RackS','Maker of AmpliTube, released in 2002.',s=WP+'Amplifier_modeling'),
 B('Tokyo Dawn Labs','','','Specialist','free dynamics and EQ','Maker of the free TDR Kotelnikov and TDR Nova.',s=D+'compressor'),
 B('Softube','Sweden','','Premium','hardware emulation','Maker of Console 1 and emulations of Tube-Tech and other gear.',s=D+'channel-strip'),
 B('Eventide','United States','','Professional & flagship','reverb, effects','Maker of Blackhole, SP2016 and other effects.',s=D+'reverb'),
 B('Solid State Logic','United Kingdom','','Professional & flagship','consoles','Console maker whose bus compressor and channel strips are widely emulated.',s=D+'compressor'),
 B('Plugin Alliance','','','Mainstream','plug-in bundles','Distributor of Brainworx, Black Box and other plug-ins.',s=D+'compressor')]
notes=('Redistributed k125 (6 old models): Pro-C 3 into FabFilter Pro-C; TDR Kotelnikov into Tokyo Dawn dynamics; TDR Nova into EQ; Valhalla Supermassive into Valhalla reverbs; OTT into Compressor; LFO Tool into Delay & modulation volume shapers. '
 'Ten further kinds are new and built from the Dubspot 2026 rankings, a SampleFocus EQ roundup and Wikipedia articles on the hardware (LA-2A, 1176, Pultec, Lexicon, Echoplex, Reverb effect) and companies. Hardware-emulation archetypes group the community-named originals (LA-2A, 1176, SSL bus, Fairchild, Pultec, EMT 140/250, Lexicon, Echoplex, Space Echo, Ampex, Studer). '
 'Not on any retrieved page and therefore omitted: Xfer OTT details beyond the old-data entry, Lexicon 480L plug-in from Lexicon itself, Neve 1073 emulations, Pro Tools stock plug-ins, Voxengo and Youlean makers beyond the ranking. EQ coverage is thinner because the Dubspot EQ page was not found. Brand entries use fetched pages; countries blank where unsure.')
put('07_01',{'kinds':[comp,eq,rev,dly,sat,amp,pit,con,mast,res,met],'brands':brands,'traditions':[],'notes':notes})
