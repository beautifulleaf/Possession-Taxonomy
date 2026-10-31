import csv,sys
S={'P':'Professional & flagship','Pr':'Premium','M':'Mainstream','V':'Value','H':'Heritage manufactory','A':'Artisan & independent','S':'Specialist','O':'Own-label & retailer','I':'Institution & issuer'}
D="""AEA|S|ribbon microphones
AKG|P|microphones
ARP Instruments|H|analogue synthesizers
Access Music|S|virus synthesizers
Adams|P|concert percussion
Aeolian|H|player pianos
Akai Professional|M|mpc samplers
Alembic|A|neck-through basses
Alesis|V|electronic drums
Alfred Arnold|H|bandoneons
Allen & Heath|P|mixing consoles
Allparts|S|guitar parts
AlphaTheta (Pioneer DJ)|P|dj equipment
Amati|A|violins
Ampeg|P|bass amplifiers
Antonio Stradivari|A|violins
Antonio de Torres|A|classical guitars
Arbiter|H|fuzz face
Arturia|M|synthesizers
Audio-Technica|M|turntables
Aulos|M|plastic recorders
Bach|P|trumpets
Behringer|V|synth clones
Benedetto|A|archtop guitars
Besson|P|brass band instruments
Beyerdynamic|Pr|headphones
Bigsby|H|vibrato tailpieces
Binson|H|echorec
Blüthner|Pr|pianos
Bosphorus|A|cymbals
Boss|M|effects pedals
Bozak|H|dj mixers
Brannen Brothers|P|flutes
Buchla|S|modular synthesizers
Buffet Crampon|P|clarinets
Bösendorfer|P|pianos
C. Bechstein|Pr|pianos
Camac|Pr|harps
Celestion|M|guitar speakers
Charvel|Pr|superstrats
Clarke|H|tin whistles
Clavia|P|nord keyboards
CodaBow|S|carbon-fibre bows
Coles|S|ribbon microphones
Conn|H|band instruments
Cordoba|M|classical guitars
D'Addario|M|strings
D'Angelico|Pr|archtop guitars
DOD|V|effects pedals
Dallas Musical|H|rangemaster booster
Danelectro|V|budget guitars
De Gregorio|S|cajons
DeArmond|H|pickups
Denon DJ|M|dj equipment
DiMarzio|M|pickups
DigiTech|M|whammy pedal
Dobro|H|resonator guitars
Doepfer|S|eurorack modules
Domenico Montagnana|A|cellos
Drum Workshop|Pr|drums
Dumble|A|custom amplifiers
Dusty Strings|A|lever harps
Dwarkin|H|harmoniums
E-mu Systems|H|samplers
EMG|M|active pickups
ESP|M|metal guitars
EVH|Pr|5150 amplifiers
Electro-Harmonix|M|effects pedals
Electro-Voice|P|microphones
Elektron|Pr|grooveboxes
Elixir|Pr|coated strings
Ensoniq|H|samplers
Epiphone|V|guitars
Ernie Ball|M|guitar strings
Eventide|P|effects processors
Expressive E|S|expressive controllers
F. Lorée|P|oboes
Fairlight|H|cmi sampler
Farfisa|H|combo organs
Fazioli|P|grand pianos
Fender|P|electric guitars
Finkenbeiner|A|glass armonicas
Floyd Rose|S|locking tremolos
Fox|P|bassoons
Fractal Audio Systems|P|amp modellers
François Tourte|A|violin bows
Fulltone|A|effects pedals
Gator|M|instrument cases
Gebr. Alexander|P|horns
Generation|V|tin whistles
Getzen|Pr|trumpets
Gibson|P|electric guitars
Giuseppe Guarneri del Gesù|A|violins
Gotoh|M|guitar hardware
Graph Tech|M|nuts and saddles
Gretsch|Pr|hollow-body guitars
Grover|M|tuners
Guild|Pr|acoustic guitars
Hammond|P|tonewheel organs
Heckel|P|bassoons
Hercules|M|instrument stands
Hercules DJ|V|dj controllers
Hermann Hauser|A|classical guitars
Hipshot|S|guitar hardware
Hiren Roy|A|sitars
Hiscox|Pr|hard cases
Hohner|M|harmonicas
Holton|M|french horns
Hugh Tracey|A|kalimbas
Höfner|H|violin bass
Ibanez|M|superstrats
Intellijel|S|eurorack modules
Istanbul Agop|A|cymbals
J. C. Deagan|H|mallet percussion
JHS Pedals|A|effects pedals
Jackson|M|metal guitars
Jean-Baptiste Vuillaume|A|violins
Jensen|H|guitar speakers
K&M|M|music stands
Kahler|S|tremolo systems
Kamaka|H|ukuleles
Kawai|M|pianos
Keilwerth|P|saxophones
Kemper|P|amp profilers
King|H|band instruments
Klon|A|centaur overdrive
Kluson|H|tuners
Koistinen Kantele|A|kanteles
Korg|M|synthesizers
Kramer|V|superstrats
Kyser|M|capos
Küng|Pr|recorders
Lachenal|H|concertinas
Latin Percussion|M|hand percussion
Leedy|H|drums
Leslie|S|rotary speakers
Line 6|M|amp modellers
Linn Electronics|H|drum machines
Lionel Tertis|A|tertis viola
Lowden|Pr|acoustic guitars
Lowrey|H|home organs
Ludwig|P|drums
Lyon & Healy|P|pedal harps
Légère|S|synthetic reeds
MONO|Pr|gig bags
MXR|M|effects pedals
Maestro|H|fuzz pedals
Make Noise|S|eurorack modules
Manhasset|P|music stands
Marigaux|P|oboes
Marimba One|P|marimbas
Mario Maccaferri|H|plastic ukuleles
Marshall|P|guitar amplifiers
Marshall Amplification|P|valve amplifiers
Martin|P|acoustic guitars
Maxon|M|tube screamer
Meinl|M|cymbals
Meinl Weston|P|tubas
Mesa/Boogie|Pr|valve amplifiers
Miraphone|P|tubas
Miyazawa|Pr|flutes
Moeck|Pr|recorders
Mollenhauer|Pr|recorders
Moog Music|P|analogue synthesizers
Muramatsu|P|flutes
Music Man|Pr|stingray bass
Mussehl & Westphal|S|musical saws
Musser|P|mallet percussion
Mutable Instruments|S|eurorack modules
National|H|resonator guitars
Native Instruments|M|music software
Neumann|P|studio microphones
Neural DSP|Pr|amp modelling
Novation|M|midi controllers
Numark|V|dj controllers
Oberheim|Pr|polyphonic synths
Orange|M|valve amplifiers
Ortofon|P|phono cartridges
Ovation|M|roundback guitars
Overton|A|low whistles
PANArt|A|hang
PRS|Pr|electric guitars
Paiste|P|cymbals
Paolo Soprani|H|accordions
Pearl|M|drums
Peavey|M|amplifiers
Pedaltrain|M|pedalboards
Pikaterä|S|musical saws
Pleyel|H|pianos
Polyphon|H|disc music boxes
Powell|P|flutes
Pro Co|M|rat distortion
Promark|M|drumsticks
RCA|H|ribbon microphones
Ramírez|H|classical guitars
Rane|P|dj mixers
Regina|H|disc music boxes
Reloop|V|dj equipment
Reuge|Pr|music boxes
Rhodes|H|electric pianos
Rickenbacker|Pr|12-string guitars
Rigoutat|P|oboes
Rikhi Ram|A|sitars
Roger Mayer|A|octavia
Rogers|H|drums
Roland|M|electronic instruments
Ross|S|compressor pedal
Rotosound|M|bass strings
Royer Labs|P|ribbon microphones
SKB|M|moulded cases
Sabian|M|cymbals
Salvi Harps|P|pedal harps
Sandvik|H|musical saws
Scandalli|H|accordions
Schaller|M|guitar hardware
Schecter|M|metal guitars
Schilke|P|trumpets
Schlagwerk|M|cajons
Schunda|H|cimbaloms
Selmer|P|saxophones
Sennheiser|P|microphones
Sequential|Pr|polyphonic synths
Seydel|Pr|harmonicas
Seymour Duncan|M|pickups
Shin-ei|H|uni-vibe
Shubb|M|capos
Shure|P|microphones
Simmons|H|electronic drums
Slingerland|H|radio king drums
Sola Sound|H|tone bender
Sonor|P|drums
Squier|V|budget guitars
Steinberger|S|headless guitars
Steingraeber & Söhne|Pr|pianos
Steinway & Sons|P|concert grands
Strymon|Pr|effects pedals
Suzuki|M|harmonicas
Symphonion|H|disc music boxes
Takamine|M|acoustic-electric guitars
Tama|M|drums
Taylor|Pr|acoustic guitars
Technics|P|dj turntables
Teenage Engineering|S|op-1
Telefunken|H|microphones
Thomann|O|budget instruments
Tombo|M|harmonicas
Vandoren|P|reeds
Vater|M|drumsticks
Vestax|H|dj mixers
Vic Firth|M|drumsticks
Vox|H|ac30 amplifiers
W. Schreiber|Pr|bassoons
Warm Audio|V|microphone recreations
Warmoth|S|replacement necks
Warwick|Pr|bass guitars
Washburn|M|acoustic basses
Watkins Electric Music|H|copicat echo
Welte|H|reproducing pianos
Wheatstone|H|concertinas
Wm. S. Haynes|P|flutes
Wurlitzer|H|electric pianos
Yamaha|M|musical instruments
Yanagisawa|P|saxophones
Z.Vex Effects|A|effects pedals
Zildjian|P|cymbals
Érard|H|pianos and harps"""
G=sys.argv[1]
rows=[l.split('|') for l in D.splitlines()]
with open(f'{G}.map.tsv.tmp','w',encoding='utf-8') as f:
    f.write('name\tseg\tkf\n')
    for n,s,k in rows: f.write(f'{n}\t{S[s]}\t{k}\n')
import os; os.replace(f'{G}.map.tsv.tmp',f'{G}.map.tsv')
