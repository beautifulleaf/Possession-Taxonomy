import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
JP=WP+'Jigsaw_puzzle'; RC=WP+'Rubik%27s_Cube'; HY=WP+'Hanayama'; CT='https://www.theculturetrip.com/asia/japan/articles/a-brief-history-of-japanese-puzzle-boxes'
JU=WP+'Jumbo_Games'; TH=WP+'Tower_of_Hanoi'; TG=WP+'Tangram'; BU=WP+'Burr_puzzle'; PB='https://www.hobbyco.com.au/products/180pc-childrens-globe-3d-puzzleball'; WE=WP+'Wentworth_Wooden_Puzzles'; GA=WP+'Gancube'
jig=K('Jigsaw puzzle','A flat picture cut into interlocking pieces, sold by piece count, material and cutting style.',JP,
 t=['Cardboard (die-cut)','Wooden (hand-cut)','Wooden (laser-cut)','Children\'s (4-9 large pieces)','Family (100-550 pieces)','Adult (500-1,000 pieces)','Large (1,500-5,000 pieces)','Puzzle globe'],
 x=[X('Spilsbury dissected map','The first commercial jigsaws, hand-cut wooden maps made to teach geography.','John Spilsbury','c. 1760',JP),
    X('Hand-cut wooden jigsaw','Wooden puzzles cut piece by piece with a fretsaw, the premium collectors\' form.','G. J. Hayter (Victory)','1930s',WE,dt='cutter · whimsy pieces · plywood thickness · piece count'),
    X('Wentworth whimsy puzzle','Laser-cut wooden puzzles with irregular whimsy-shaped pieces and few corner pieces.','Wentworth Wooden Puzzles','1994',WE,[('Laser-cut 3 mm wood','Wentworth Wooden Puzzles','1994','over 250,000 puzzles a year')]),
    X('Wasgij','Adult jigsaw where the solver builds a different scene from the one on the box, guided by clues.','Jumbo Games','1997',JU,dt='piece count · range (Original, Mystery, Destiny)'.replace(' (Original, Mystery, Destiny)','')),
    X('Standard 1,000-piece puzzle','The usual adult format, about 38 x 27 pieces.','','',JP)],
 m=[['Wasgij','Jumbo Games']],r=[['Wasgij','Jumbo Games']])
mech=K('Mechanical puzzle','A puzzle solved by manipulating its parts: twisty puzzles, interlocking burrs, cast disentanglement puzzles, puzzle boxes and sequential-discovery puzzles.',RC,
 a='puzzle box · twisty puzzle · disentanglement puzzle',t=['Twisty cube','Twisty non-cube shape','Interlocking (burr)','Disentanglement','Puzzle box','Sliding-block','Dissection'],
 x=[X("Rubik's Cube",'3x3x3 rotating cube invented by Ernő Rubik as the Magic Cube; the best-selling puzzle ever.',"Rubik's",'1974',RC,
      [('Magic Cube (Budapest)',"Rubik's",'1977','first test batches in Budapest toy shops'),("Ideal Toy Corp. release","Ideal Toy Corp.",'1980','renamed Rubik\'s Cube worldwide'),
       ('Pocket Cube 2x2x2','','', ''),("Rubik's Revenge 4x4x4",'','',''),("Professor's Cube 5x5x5",'','',''),('Megaminx','','','dodecahedron'),('Pyraminx','','','tetrahedron')],dt='order (2x2 to 21x21) · stickered or stickerless · magnets · smart (Bluetooth)'),
    X('Speedcube','Competition-tuned twisty puzzle with springs, magnets and loose tolerances for WCA speedcubing.','Gancube','2014',GA,
      [('GAN356 Air UM','Gancube','2016','first mass-produced cube with magnets in edges and corners'),('GAN356 X','Gancube','2017','adjustable magnets'),('GAN356 i','Gancube','2018','first smart (Bluetooth) cube'),
       ('GAN11 M Pro','Gancube','2020','core-to-corner magnets'),('GAN12 Maglev','Gancube','2021','magnetic levitation'),('GAN13 Maglev','Gancube','2022','edge magnets auto-align layers')],dt='order · magnet strength · maglev · WCA edition'),
    X('Hanayama Cast puzzle','Metal cast disentanglement and lock puzzles, rated 1 (fun) to 6 (grandmaster).','Hanayama','',HY,
      [('Cast Marble','Hanayama','',''),('Cast Infinity','Hanayama','',''),('Cast Quartet','Hanayama','',''),('Cast Coaster','Hanayama','',''),('Cast NEWS','Hanayama','','')],dt='difficulty level 1-6 · designer (e.g. Oskar van Deventer) · finish'),
    X('Japanese puzzle box (himitsu-bako)','Hakone trick box that opens only by a secret sequence of sliding moves, decorated with yosegi marquetry.','','Meiji period (late 1800s)',CT,
      [('Yosegi-zaiku Hakone box','','','credited to Takajiro Ohkawa, Tatsunosuke Okiyama and Mr. Kikukawa')],dt='number of moves (4 to 60+) · yosegi marquetry · size'),
    X('Six-piece burr','Interlocking notched sticks forming three crossed pairs; oldest known burr, also the Chinese cross.','','1698 engraving',BU,
      [('Bill Cutler analysis','','1978','computer analysis published by Martin Gardner'),('Altekruse','','1890','patent'),('Chuck','','1897','patent by Edward Nelson'),('Pagoda burr','','','')],dt='level (moves to remove first piece) · notch pattern · wood'),
    X('Tower of Hanoi','Disk-moving puzzle on three pegs, solved in 2^n - 1 moves.','','1883',TH,[('Lucas / N. Claus de Siam','Édouard Lucas','1883','first presentation'),('Booklet','Édouard Lucas','1889','')],dt='disk count (toy versions about 7-9) · wood or metal'),
    X('Tangram','Seven flat tans rearranged into outline shapes; Chinese in origin.','','late 1700s',TG,[('Exported Chinese sets','','','glass, wood, tortoise shell'),('The Anchor Puzzle','F. Ad. Richter','1891','German edition')],dt='material · box · pattern book')],
 m=[['Katamino','Gigamic'],['Cast Cylinder','Hanayama'],['Cast Hourglass','Hanayama'],['Cast News','Hanayama'],['Cast Quartet','Hanayama'],['Cast Vortex','Hanayama']],r=[['Cast','Hanayama']])
d3=K('3D jigsaw puzzle','Interlocking pieces that assemble into a solid shape such as a globe, building or animal.',JP,a='three-dimensional jigsaw puzzle',
 t=['Plastic snap-together sphere','Wooden','Foam','Puzzle globe'],
 x=[X('Puzzleball','Ravensburger spherical puzzle of curved snap-together plastic pieces, printed with numbers on the back.','Ravensburger','',PB,[('Children\'s Globe 180 pieces','Ravensburger','','20 cm diameter')],dt='piece count (72, 180, 540) · theme · stand')],
 r=[['Puzzleball','Ravensburger']])
brands=[B('Ravensburger','Germany','1883','Mainstream','jigsaws','German game and puzzle publisher; makes jigsaws and Puzzleball.','knowledge'),
 B('Jumbo Games','Netherlands','1853','Mainstream','jigsaws','Dutch puzzle and games company; Falcon is its UK adult puzzle brand and home of Wasgij.','https://en.wikipedia.org/wiki/Jumbo_Games',sig=['Wasgij']),
 B('Wentworth Wooden Puzzles','United Kingdom','1994','Artisan & independent','wooden puzzles','Laser-cut wooden jigsaws with whimsy pieces, founded by Kevin Wentworth Preston.',WE,sig=['Wentworth whimsy puzzle']),
 B('Hanayama','Japan','1933','Specialist','cast puzzles','Japanese maker of metal Cast puzzles; the article\'s founding year conflicts with its 1972 category.',HY,sig=['Hanayama Cast puzzle']),
 B('Gancube','China','2014','Specialist','speedcubes','Guangzhou speedcube maker founded by Jiang Ganyuan.',GA,sig=['Speedcube']),
 B("Rubik's",'Hungary','1974','Heritage manufactory','Rubik\'s Cube',"Brand of Ernő Rubik's cube; bought by Spin Master in 2020.",RC,sig=["Rubik's Cube"]),
 B('Gigamic','France','1990','Specialist','abstract games','French publisher of Katamino.','knowledge')]
trads=[{'n':'Hakone yosegi puzzle box (himitsu-bako)','g':'Woodwork & furniture','r':'Hakone, Japan','p':'Meiji period (late 1800s) onward','d':'Trick boxes opened by a secret sequence of sliding panels, faced in yosegi marquetry.','tech':'yosegi-zaiku wood mosaic, sliding-panel mechanisms','mat':'various coloured woods','forms':['Mechanical puzzle'],'ctr':['Takajiro Ohkawa','Tatsunosuke Okiyama','Kikukawa'],'s':CT}]
write('04_03',[jig,mech,d3],brands,trads,'Dropped: nothing. Wrebbit, Pomegranate, Liberty, Lucas-era makers not confirmed by a retrieved page, left out. Hanayama founding year conflicts on Wikipedia (1933 vs category 1972). Himitsu-bako page fetched via Firecrawl after WebFetch 503.')
