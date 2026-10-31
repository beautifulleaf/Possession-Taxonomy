import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
TF=WP+'Table_football'; AH=WP+'Air_hockey'; CA=WP+'Carrom'; CR=WP+'Crokinole'; NO=WP+'Novuss'; PN=WP+'Pitchnut'; SH=WP+'Table_shuffleboard'; BB=WP+'Bar_billiards'; JE=WP+'Jenga'; PS=WP+'Pick-up_sticks'; KP=WP+'KerPlunk'; GA=WP+'Garlando'
tf=K('Table football','A table with rods of players for a game of football.',TF,a='foosball · babyfoot · futbolín · table soccer',
 t=['European (one goalkeeper)','American (three goalkeepers)','Futbolín','Coin-operated','Folding / home','Tabletop'],
 x=[X('Thornton table football','The first patent with the core features of the modern game.','','1921',TF,[('UK patent, Harold Searles Thornton','','1921','Apparatus for playing a game of table football')]),
    X('Futbolín','Spanish table football, patented in Madrid by Alejandro Finisterre.','','1937',TF),
    X('ITSF tournament table','Tables used in International Table Soccer Federation world cups and championships.','Bonzini','',TF,
      [('Bonzini (French style)','Bonzini','',''),('Roberto Sport','Roberto Sport','',''),('Garlando','Garlando','','founded 1954 at Spinetta Marengo'),('Tornado (American style)','Tornado','',''),('Leonhart','Leonhart','','')],dt='goalkeeper count · rod type · corner shape · ball')],
 r=[['Bonzini','Bonzini'],['Garlando','Garlando'],['Leonhart','Leonhart'],['Tornado','Tornado'],['Roberto Sport','Roberto Sport']])
ah=K('Air hockey table','A table with an air cushion for a puck game.',AH,t=['8-foot tournament','Full-size novelty','Mini (1.5-2.5 ft)','Four-player','Coin-operated'],
 x=[X('Brunswick air hockey table','The first air hockey table, built by Brunswick Billiards staff.','Brunswick','1972',AH,[('Original patent design','Brunswick','1972','Phil Crossman, Bob Kenrick, Bob Lemieux'),('Dynamo','Dynamo','','approved for sanctioned play'),('Gold Standard Games','Gold Standard Games','','approved for sanctioned play')],dt='length · air-hole pattern · puck (Lexan) · high-top or flat-top mallet')])
ca=K('Carrom board','A square board with pockets, played by flicking discs.',CA,t=['ICF tournament board (73.5-74 cm)','Family board','Folding / portable','With stand'],
 x=[X('Indian carrom','Standard ICF game with 9 white, 9 black and a red queen, flicked with a striker into corner pockets.','','',CA,
      [('Surco','Surco','','named Indian exporter'),('Precise','Precise','','named Indian exporter'),('Syndicate Sports','Syndicate Sports','',''),('Paul Traders','Paul Traders','','')],dt='plywood board · bumpers · striker 15 g, 4.1 cm · carrom men 3.02-3.18 cm'),
    X('North American carrom','Haskell version with ring pieces and built-in pockets.','','c. 1890',CA),
    X('Pitchnut','French Canadian wooden board with a gutter and pegs, 28 inches square.','','mid-20th century',PN,[('Achille Scalabrini boards','','','Coaticook, Quebec; all known boards handmade')])],
 m=[['Big Game Hunters Championship Carrom Board','Big Game Hunters'],['Philos Classic Carrom Set','Philos'],['Uber Games Championship carrom set','Uber Games'],['Uber Games Tournament carrom set','Uber Games'],['Uber Games Premium carrom set','Uber Games']],r=[['Uber Games carrom boards','Uber Games']])
cr=K('Crokinole board','A round board with a central hole, played by flicking discs.',CR,t=['Octagonal','Round','Tournament (26 in)','Folding'],
 x=[X('Wettlaufer board','Earliest known crokinole board, made in Perth County, Ontario.','Eckhardt Wettlaufer','1876',CR),
    X('Tournament crokinole board','About 26 in board with 5, 10, 15 point rings and a 20 point hole, used at the World Crokinole Championships.','Tracey','',CR,[('World Championship board builder','Jeremy Tracey','','Tavistock, Ontario, held annually since 1999')],dt='diameter · ring scoring · bumpers · wood')],
 m=[['Masters Crokinole Tournament Board','Masters Traditional Games'],['Philos Compact Octagonal Crokinole Board','Philos'],['Tracey Tour Championship Crokinole Board','Tracey']])
nv=K('Novuss board','A cue-and-disc table game from Latvia and Estonia, played on a square board with corner pockets.',NO,a='koroona · korona',t=['Tabletop','On stand'],
 x=[X('Novuss','Baltic national game: each player cues a puck at eight object discs; board about 100 cm square.','','c. 1925-1927',NO,[('Korona õpetus rulebook','','1930','oldest known printed rules'),('Latvian Novuss Federation','','1963','')])])
sb=K('Table shuffleboard','A long smooth table down which weighted pucks are pushed by hand, or a small sliding-disc board.',SH,a='shovelboard · sjoelbak',t=['Full-length (9-22 ft)','Sjoelbak (about 2 m)','Shove ha\'penny board'],
 x=[X('Table shuffleboard','Pucks slid by hand along a waxed wooden table into a scoring zone.','','',SH,dt='length 9-22 ft · width 20 in or more · silicone wax'),
    X('Sjoelen','Dutch board where 30 wooden pucks are slid through arches into numbered boxes; maximum 148.','','',SH,[('Homas','Homas','',''),('Heemskerk Sport','Heemskerk Sport','',''),('Schilte','Schilte','','')])])
bb=K('Bar billiards table','A pub billiards table where balls are potted into holes and pegs and mushrooms score.',BB,t=['Standard league (32 in)','Narrow (28 in)','Tabletop'],
 x=[X('Jelkes table','First bar billiards table in Britain, built in London after David Gill saw billard russe in Belgium.','Jelkes','early 1930s',BB,[('Sams','Sams','',''),('Riley','Riley','',''),('Burroughs & Watts','Burroughs & Watts','',''),('Clare','Clare','','')],dt='playing width · pegs or mushrooms · coin-op')])
dx=K('Dexterity game','A game of physical skill with its own pieces (stacking, balancing, flicking).',JE,t=['Stacking','Pulling','Balancing','Flicking'],
 x=[X('Pick-up sticks','Players lift one stick at a time without moving others; also jackstraws, spillikins or Mikado.','','1734 (earliest English reference)',PS,[('Mikado','','','sticks 17-20 cm, scoring colours'),('Farm tools set','','','about 45 pieces')]),
    X('Jenga','Wooden block tower game: 54 blocks in 18 levels of three.','Oxford Games','1983',JE,[('Launch, London Toy Fair','Leslie Scott','1983',''),('Milton Bradley release','Milton Bradley','1987','US'),('Jenga Xtreme','','',''),('Jenga Giant','Art\'s Ideas','','')]),
    X('KerPlunk','Pull straws from a tube without dropping the marbles.','Ideal','1967',KP,[('Original','Ideal Toy Company','1967','Eddy Goldfarb and Rene Soriano')])],
 m=[['Pick Up Sticks','House of Marbles'],['Tracey Carrooka Pool 8','Tracey'],['Carrooka','Woodestic']])
brands=[B('Garlando','Italy','1954','Mainstream','table football','Italian maker of table football, pool and ping pong tables.',GA),
 B('Bonzini','France','','Specialist','table football','Official ITSF table brand, French style.',TF),
 B('Tornado','United States','','Specialist','table football','Official ITSF table brand, American style.',TF),
 B('Leonhart','','','Specialist','table football','Official ITSF table brand.',TF),
 B('Roberto Sport','','','Specialist','table football','Official ITSF table brand.',TF),
 B('Brunswick','United States','','Heritage manufactory','billiards','Billiards company whose staff created air hockey.',AH),
 B('Jelkes','United Kingdom','','Heritage manufactory','bar billiards','London maker of the first British bar billiards tables.',BB),
 B('Tracey','Canada','','Artisan & independent','crokinole','Builder of World Crokinole Championship boards.',CR),
 B('Surco','India','','Value','carrom','Indian carrom board exporter.',CA),
 B('Precise','India','','Value','carrom','Indian carrom board exporter.',CA),
 B('Uber Games','','','Mainstream','carrom','Carrom board maker in old data.','knowledge' if False else CA)]
brands=[b for b in brands if b['n']!='Uber Games']
trads=[{'n':'Carrom','g':'Traditional games','r':'India','p':'ICF formed 1988','d':'Indian flicking game on a pocketed board, now ICF-governed.','tech':'wooden plywood board with bumpers','mat':'plywood, wood','forms':['Carrom board'],'ctr':['Precise','Surco'],'s':CA},
 {'n':'Crokinole','g':'Traditional games','r':'Ontario, Canada','p':'1876 earliest board','d':'Round-board disc-flicking game, strongest in Ontario.','tech':'polished wood or laminate board','mat':'wood','forms':['Crokinole board'],'ctr':['Tavistock, Ontario','Tracey'],'s':CR}]
write('04_04',[tf,ah,ca,cr,nv,sb,bb,dx],brands,trads,'Added Novuss board, Table shuffleboard, Bar billiards table beyond planned kinds (brief). Pitchnut as archetype of Carrom board. Hilinski and Leonhart details not found on a fetched page; Hilinski left out. Billiards/pool tables left to Sports.')
