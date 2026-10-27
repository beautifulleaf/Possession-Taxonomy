from common import *
S99='https://99sounds.org/best-synth-vst/'
AR=WP+'List_of_Arturia_products'
SS=WP+'Software_synthesizer'
syn={'n':'Software synthesiser','a':'VST instruments · software synths · virtual synths','d':'Synth that runs inside a music program and makes sound when played, whether built from oscillators and filters or emulating a hardware classic.',
 't':['wavetable','virtual analogue','FM','sample-based','modular','physical modelling','hardware emulation'],
 's':'https://www.pluginboutique.com/categories/1-Instruments','x':[
 A('Serum','Wavetable synth from Xfer Records (Steve Duda) that defined 2010s electronic production.',S99,[V('Serum','Xfer','2014','Wavetable; 144 wavetables, 10 effect modules per the page'),V('Serum 2','Xfer','2025')],mk='Xfer',y='2014'),
 A('Massive','Native Instruments\' wavetable synth for bass and leads, released in October 2006.',WP+'NI_Massive',[V('Massive','Native Instruments','2006','Released 16 October 2006'),V('Massive X','Native Instruments','','Successor; 170+ wavetables, EUR 199')],mk='Native Instruments',y='2006'),
 A('Omnisphere','Spectrasonics\' sample-and-synthesis instrument with tens of thousands of presets.',S99,[V('Omnisphere 2','Spectrasonics','','14,000+ presets per the page'),V('Omnisphere 3','Spectrasonics','')],mk='Spectrasonics'),
 A('Sylenth1','LennarDigital\'s virtual-analogue synth with four unison oscillators, a staple of early EDM.',WP+'Virtual_Studio_Technology',[V('Sylenth1','LennarDigital','','Listed with 2007-2008 production dates by Vintage Synth Explorer; four band-limited oscillators, 16-note polyphony')],mk='LennarDigital'),
 A('Diva','u-he\'s virtual-analogue synth that models oscillators and filters from classic hardware by circuit simulation.',S99,[V('Diva','u-he','','Five oscillator and five filter models; up to 16 voices per the page')],mk='u-he'),
 A('Pigments','Arturia\'s first original software synth, released in 2018, mixing wavetable, virtual analogue, sample and harmonic engines.',AR,[V('Pigments','Arturia','2018')],mk='Arturia',y='2018'),
 A('Vital','Free and low-cost wavetable synth by Matt Tytel with free, $25 and $80 tiers.',S99,[V('Vital','Matt Tytel','','Free, Plus ($25) and Pro ($80) per the page')],mk='Matt Tytel'),
 A('Phase Plant','Modular synth from Kilohearts with four signal generators.',S99,[V('Phase Plant','Kilohearts','')],mk='Kilohearts'),
 A('Surge XT','Free open-source hybrid synth, with sibling projects from the Surge Synth Team.',S99,[V('Surge XT','Surge Synth Team','','700+ wavetables, 2,800 patches per the page'),V('OB-Xf','Surge Synth Team'),V('Shortcircuit XT','Surge Synth Team','','Sampler')],mk='Surge Synth Team'),
 A('Minimoog','Arturia emulation of the Moog Minimoog.',AR,[V('Mini V','Arturia')],mk='Moog'),
 A('Roland Jupiter-8','Arturia emulation of the Jupiter-8.',AR,[V('Jup-8 V','Arturia')],mk='Roland'),
 A('Yamaha DX7','Arturia emulation of the DX7 FM synth.',AR,[V('DX7 V','Arturia')],mk='Yamaha'),
 A('Yamaha CS-80','Arturia emulation of the CS-80.',AR,[V('CS-80 V','Arturia')],mk='Yamaha'),
 A('Sequential Prophet-5','Arturia emulation of the Prophet-5.',AR,[V('Prophet V','Arturia')],mk='Sequential Circuits'),
 A('ARP 2600 and Oberheim classics','Arturia emulations of the ARP 2600, Oberheim SEM and Matrix-12.',AR,[V('ARP2600 V','Arturia'),V('SEM V','Arturia'),V('Matrix-12 V','Arturia')]),
 A('Reaktor','Native Instruments\' modular building environment, descended from Generator (1996), with Absynth and FM8 beside it.',WP+'Native_Instruments',[V('Generator','Native Instruments','1996'),V('Reaktor','Native Instruments'),V('Absynth','Native Instruments'),V('FM8','Native Instruments')],mk='Native Instruments',y='1996')],
 'm':M(('Analog Lab Pro','Arturia'),('Spire','Reveal Sound'),('Nexus','reFX'),('Vanguard','reFX'),('Falcon','UVI'),('Gladiator','Tone2'),('Discovery','Tone2'),('GForce Axxess','GForce'),('M-Tron Select 2','GForce'),('JE-8086','Usual Suspects'),('OB-Xd','discoDSP'),('Splice INSTRUMENT','Splice'),('Myth','Dawesome'),('Zyklop','Dawesome'))}
samp={'n':'Sampler & sample player','a':'software sampler','d':'Instrument that plays back recorded sounds across the keyboard and hosts sample libraries; many libraries run only inside one.',
 't':['library host','free player','scripted instrument engine','multi-format hybrid'],
 's':WP+'Kontakt_(software)','x':[
 A('Kontakt','Native Instruments\' software sampler, first introduced in 2002; the free Kontakt Player runs most commercial libraries.',WP+'Kontakt_(software)',[V('Kontakt','Native Instruments','2002'),V('Kontakt Player','Native Instruments','','Free, feature-limited player'),V('Kontakt Script Processor and Creator Tools','Native Instruments','','Let third parties build instruments on Kontakt')],mk='Native Instruments',y='2002'),
 A('HALion','Steinberg\'s sample-based software instrument, first released in 2001.',WP+'HALion',[V('HALion 1','Steinberg','2001'),V('HALion 3','Steinberg','2004'),V('HALion 4','Steinberg','2011','Added synthesis'),V('HALion 5','Steinberg','2013'),V('HALion 6','Steinberg','2017','Macros and Lua scripting'),V('HALion Sonic SE','Steinberg','','Free, bundled with Cubase')],mk='Steinberg',y='2001'),
 A('EXS24','Emagic\'s sampler, later Apple\'s Sampler inside Logic Pro.',SS,[V('EXS24','Emagic')],mk='Emagic'),
 A('Decent Sampler','Free sampler format and player (.dspreset) that plays Pianobook libraries without Kontakt.',WP+'SFZ_(file_format)',[V('Decent Sampler','Decent Samples')],mk='Decent Samples')],
 'm':M(('DYSEKT','Defuse Audio'),('Shortcircuit XT','Surge Synth Team'))}
orc={'n':'Orchestral sample library','a':'orchestral library · virtual orchestra','d':'Recorded orchestra sold as a playable instrument, with sections, solo players and articulations, usually run inside Kontakt or its own player.',
 't':['full orchestra','strings','brass','woodwinds','percussion and choir','free entry library'],
 's':SS,'x':[
 A('Spitfire BBC Symphony Orchestra','Spitfire Audio\'s orchestra recorded with the BBC Symphony Orchestra at Maida Vale.',WP+'Spitfire_Audio',[V('BBC Symphony Orchestra Discover','Spitfire Audio','','Free edition'),V('BBC Symphony Orchestra Core','Spitfire Audio'),V('BBC Symphony Orchestra Professional','Spitfire Audio'),V('LABS','Spitfire Audio','','Free series released from time to time')],mk='Spitfire Audio',y='2007',dt='tier (Discover, Core, Professional) · player'),
 A('EastWest Hollywood Orchestra','EastWest\'s orchestra recorded in Studio 1 at EastWest Studios with Hollywood session players.',WP+'EastWest_Studios',[V('Hollywood Orchestra','EastWest'),V('Symphonic Orchestra','EastWest','','Conceived with Nick Phoenix')],mk='EastWest',y='1988'),
 A('Vienna Symphonic Library','Austrian library founded in 2000 by Herb Tucmandl; Vienna Instruments, Synchron and Big Bang Orchestra series.',WP+'Vienna_Symphonic_Library',[V('Vienna Instruments','Vienna Symphonic Library','','Dry studio recordings; Standard and Full libraries'),V('Big Bang Orchestra','Vienna Symphonic Library','','Concluded 2021'),V('Synchron','Vienna Symphonic Library','','Recorded at Synchron Stage Vienna')],mk='Vienna Symphonic Library',y='2000'),
 A('Orchestral Tools','Berlin developer of the Berlin Series and Metropolis Ark libraries, recorded at Teldex Scoring Stage.','https://www.soundonsound.com/reviews/metropolis-ark-3-berlin-orchestra-inspire',[V('Metropolis Ark 3','Orchestral Tools','2018','Orchestra with heavy percussion; about 60GB; Kontakt'),V('Berlin Orchestra Inspire','Orchestral Tools','','23 instruments in about 9.5GB; Kontakt')],mk='Orchestral Tools')]}
piano={'n':'Virtual piano & keys','a':'piano plug-in','d':'Plug-in that plays pianos and other keyboard instruments from sampled recordings or physical models.',
 't':['sampled','physically modelled','free','keyboard collection'],
 's':'https://violetrecording.com/best-piano-vst/','x':[
 A('Keyscape','Spectrasonics\' broad keyboard collection with a concert grand, electric pianos, clavinets and hybrids.','https://violetrecording.com/best-piano-vst/',[V('Keyscape','Spectrasonics')],mk='Spectrasonics'),
 A('Pianoteq','Modartt\'s physically modelled piano, first released in August 2006, with a small footprint.',WP+'Pianoteq',[V('Pianoteq','Modartt Software','2006','August 2006'),V('Pianoteq 9','Modartt Software','2026','9.2.1 listed June 2026')],mk='Modartt',y='2006'),
 A('Addictive Keys','XLN Audio\'s producer-focused sampled keys with mix-ready presets.','https://violetrecording.com/best-piano-vst/',[V('Addictive Keys','XLN Audio')],mk='XLN Audio'),
 A('Noire','Native Instruments\' Yamaha CFX recorded with Nils Frahm, in Pure and Felt versions.','https://violetrecording.com/best-piano-vst/',[V('Noire','Native Instruments')],mk='Native Instruments'),
 A('EZkeys 2','Toontrack\'s piano with chord and MIDI-groove songwriting tools.','https://violetrecording.com/best-piano-vst/',[V('EZkeys 2','Toontrack')],mk='Toontrack'),
 A('Arturia Piano V','Modelled grand and upright piano from Arturia.',AR,[V('Piano V','Arturia')],mk='Arturia'),
 A('Garritan CFX Concert Grand','Detailed Yamaha CFX with several mic perspectives for solo classical piano.','https://violetrecording.com/best-piano-vst/',[V('CFX Concert Grand','Garritan')],mk='Garritan'),
 A('Spitfire LABS Soft Piano','Free felted upright with a hushed, intimate sound.','https://violetrecording.com/best-piano-vst/',[V('LABS Soft Piano','Spitfire Audio')],mk='Spitfire Audio')]}
drum={'n':'Virtual drum instrument','a':'drum plug-in · drum sampler','d':'Plug-in that plays multi-sampled drum kits with built-in grooves or a one-shot sampler for building your own kits.',
 't':['acoustic kit engine','pre-processed rock and metal kits','one-shot sampler'],
 's':'https://violetrecording.com/best-drum-vst/','x':[
 A('Superior Drummer','Toontrack\'s deep acoustic drum engine for realistic kits and full mixing control.','https://violetrecording.com/best-drum-vst/',[V('Superior Drummer 3','Toontrack')],mk='Toontrack'),
 A('EZdrummer','Toontrack\'s fast songwriting drummer with a Bandmate groove suggester.','https://violetrecording.com/best-drum-vst/',[V('EZdrummer 3','Toontrack')],mk='Toontrack'),
 A('BFD','Deep acoustic drum engine known for natural, room-heavy sound.','https://violetrecording.com/best-drum-vst/',[V('BFD3','')]),
 A('Addictive Drums','XLN Audio\'s polished genre-specific kits (ADpaks) that sit in a mix quickly.','https://violetrecording.com/best-drum-vst/',[V('Addictive Drums 2','XLN Audio')],mk='XLN Audio'),
 A('Steven Slate Drums','Slate Digital\'s big pre-processed rock and metal kits, with a free tier.','https://violetrecording.com/best-drum-vst/',[V('Steven Slate Drums 5.5','Slate Digital')],mk='Slate Digital'),
 A('Battery','Native Instruments\' cell-grid drum sampler, launched in 2002, for kits built from your own one-shots.',WP+'Native_Instruments',[V('Battery','Native Instruments','2002'),V('Battery 4','Native Instruments')],mk='Native Instruments',y='2002'),
 A('XLN Audio XO','XLN Audio\'s sampler that maps sample folders by sound similarity, with a step sequencer.','https://violetrecording.com/best-drum-vst/',[V('XO','XLN Audio')],mk='XLN Audio'),
 A('GetGood Drums','Focused acoustic packs for modern metal and progressive styles.','https://violetrecording.com/best-drum-vst/',[V('GetGood Drums libraries','GetGood Drums')],mk='GetGood Drums')]}
brands=[B('Native Instruments','Germany','','Professional & flagship','Kontakt, Komplete','Berlin maker of Kontakt, Massive and Reaktor.',s=WP+'Native_Instruments'),
 B('Arturia','France','1999','Premium','synth emulations','Grenoble maker of the V Collection and Pigments.',s=WP+'Arturia'),
 B('Spectrasonics','United States','1994','Premium','Omnisphere, Keyscape','Company of Eric and Lorey Persing, maker of Omnisphere and Keyscape.',s=WP+'Eric_Persing'),
 B('Steinberg','Germany','','Professional & flagship','Cubase, VST','Yamaha subsidiary that created the VST format.',s=WP+'Virtual_Studio_Technology'),
 B('Spitfire Audio','United Kingdom','2007','Premium','orchestral libraries','London company founded in 2007 by Christian Henson and Paul Thomson.',s=WP+'Spitfire_Audio'),
 B('EastWest','United States','1988','Premium','orchestral libraries','Company founded as EastWest Sounds by Doug Rogers.',s=WP+'EastWest_Studios'),
 B('Vienna Symphonic Library','Austria','2000','Premium','orchestral libraries','Vienna company founded in 2000 by Herbert Tucmandl.',s=WP+'Vienna_Symphonic_Library'),
 B('Orchestral Tools','Germany','','Premium','orchestral libraries','Berlin maker of the Berlin Series and Metropolis Ark.',s='https://www.soundonsound.com/reviews/metropolis-ark-3-berlin-orchestra-inspire'),
 B('Xfer','United States','','Specialist','Serum','Steve Duda\'s company, maker of Serum.'),
 B('u-he','Germany','','Premium','Diva, Zebra','German synth plug-in maker.'),
 B('Modartt','','','Specialist','Pianoteq','Maker of the physically modelled Pianoteq.',s=WP+'Pianoteq'),
 B('Toontrack','Sweden','','Premium','drums, EZkeys','Maker of Superior Drummer, EZdrummer and EZkeys.'),
 B('XLN Audio','Sweden','','Premium','Addictive Drums','Maker of Addictive Drums, Addictive Keys and XO.'),
 B('Kilohearts','Sweden','','Specialist','Phase Plant','Maker of Phase Plant and Snapin effects.')]
notes=('Software synthesiser (k124+k121): 44 old names reorganised into 16 archetypes (Serum, Massive, Omnisphere, Sylenth1, Diva, Pigments, Vital, Phase Plant, Surge XT family, Arturia hardware emulations as archetypes of the emulated Minimoog, Jupiter-8, DX7, CS-80, Prophet-5, ARP 2600/Oberheim, Reaktor family) plus 14 flat. Myth and Zyklop are synths and stay. '
 'Moved out: Flux Mini 2 and Flux Pro (Caelum Audio) are effects and should go to the Audio effects shelf; Spitfire LABS is now a version of the Spitfire archetype; DYSEKT and Shortcircuit XT moved to Sampler. '
 'New kinds Sampler, Orchestral sample library, Virtual piano & keys, Virtual drum instrument are sourced from Wikipedia and review roundups. Omitted because no retrieved page covered them: Synthogy Ivory II, Decent Sampler details beyond the format, Audio Imperia. Brand entries use fetched pages or owner-approved knowledge; countries left blank where unsure.')
put('07_00',{'kinds':[syn,samp,orc,piano,drum],'brands':brands,'traditions':[],'notes':notes})
