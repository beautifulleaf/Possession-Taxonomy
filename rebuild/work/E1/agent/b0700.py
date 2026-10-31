import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
YY=WP+'Yo-yo'; BB=WP+'Beyblade_(franchise)'; KD=WP+'Kendama'; FR=WP+'Frisbee'; AE=WP+'Aerobie'; PI=WP+'Pop_it'; BG=WP+'Beigoma'; HS=WP+'Hand_spinner'; KI=WP+'Kite'; BR=WP+'Bubble_ring'; UB=WP+'Utility_ball'; SB=WP+'Stress_ball'; SQ=WP+'Squishy'; SU=WP+'Super_Ball'; SW='https://sweetskendamas.com/pages/about-sweets-kendamas'
yo=K('Yo-yo','A spool on a string, spun down and back up by the hand.',YY,t=['Responsive (0A)','Unresponsive (1A)','Looping (2A)','Two-handed (3A)','Off-string (4A)','Freehand (5A)','Fixed axle','Transaxle','Ball-bearing','Novelty or tin'],
 x=[X('Flores looped-string yo-yo','Pedro Flores added a looped slip-string for stable tricks and opened a Santa Barbara factory in 1928.','Pedro Flores','1928',YY),
    X('Duncan yo-yo','Donald F. Duncan bought the Flores company around 1929 and sold the craze worldwide.','Duncan Toys','c. 1929',YY,[('Luck, Wisconsin factory','Duncan Toys','1946',''),('TV comeback campaign','Duncan Toys','1962','')]),
    X('Ball-bearing yo-yo','Bearing in the axle gives long spins and unresponsive play; SKF made novelty ones in 1984.','','1990',YY,[('SB-2 (Tom Kuhn)','','1990','first successful ball-bearing yo-yo')],dt='bearing type · shape (butterfly) · response · material')],
 m=[['Schylling Tin Yo-Yo','Schylling']])
tp=K('Spinning top','A top spun by hand, string or launcher, including battle tops.',BB,a='battle top · beigoma',t=['Hand-spun','String-pulled peg top','Launcher battle top','Humming top','Dreidel'],
 x=[X('Beigoma','Traditional Japanese metal battle top, about 3 cm, that inspired Beyblade; descended from sand-filled shells.','','Edo period (17th century)',BG),
    X('Beyblade','Launcher-spun battling top line from Takara Tomy, in four generations.','Takara Tomy','1999',BB,
      [('Original Beyblade','Takara','1999','plastic tops, anime to 2004'),('Metal Fusion','Takara Tomy','2008','metal components'),('Beyblade Burst','Takara Tomy','2015','released 18 July 2015'),('Beyblade X','Takara Tomy','2023','toys released 15 July 2023')],dt='generation · layer/chip/driver parts · launcher')])
kd=K('Kendama','Japanese cup-and-ball skill toy with a spiked handle, cups and a string-tied ball.',KD,t=['Competition (Japan Kendama Association style)','Beginner','Wood finish / paint','Rubber-coated'],
 x=[X('Ekusa three-cup kendama','Modern shape credited to Hamagatsu Ekusa in Kure; Hatsukaichi is its birthplace.','','1919',KD,[('Jisugetsu ball','','1919','Ekusa')]),
    X('S-type and F-type','Competition models made at the Japan Kendama Association\'s request.','','1975',KD,[('S-type (Hideo Shinma)','','1975','first competition-style model'),('F-type / F16 (Issei Fujiwara)','','1978',''),('F16-2','','2001','string hole moved off-centre')]),
    X('Sweets Kendamas','US brand founded by Matt Jorgenson, part of the modern western kendama scene.','Sweets Kendamas','2010',SW)],
 r=[['Sweets','Sweets Kendamas']])
fd=K('Toy flying disc','A disc thrown as a toy.',FR,a='flying disc · Frisbee',t=['Plastic toy disc','Foam disc','Flying ring','Ultimate disc','Disc golf disc','Freestyle disc'],
 x=[X('Pluto Platter / Frisbee','Fred Morrison\'s plastic disc, sold to Wham-O in 1957 and named Frisbee.','Wham-O','1957',FR,[('Flyin-Saucer','Morrison and Franscioni','1948',''),('Pluto Platter','Fred Morrison','1955',''),('Frisbee name','Wham-O','1957','after Frisbie Pie Company tins'),('Redesign by Ed Headrick','Wham-O','1964','')]),
    X('Aerobie flying ring','Thin ring with a spoiler rim, stable over a wide range of speeds; 13-inch Aerobie Pro.','Aerobie','1984',AE,[('Skyro','Alan Adler','1970s','predecessor'),('Pro ring Guinness throw 383 m','Aerobie','1986','Scott Zimmerman'),('Pro ring 406 m','Aerobie','2003','Erin Hemmings')])],
 m=[['Aerobie Pro Ring','Aerobie'],['Wham-O Classic Frisbee','Wham-O'],['Wham-O Frisbee All Sport Disc','Wham-O'],['Wham-O Frisbee Heavyweight','Wham-O']],r=[['Frisbee','Wham-O']])
ki=K('Toy kite','A kite made as a toy that cannot do a sport kite\'s job.',KI,t=['Diamond','Delta','Sled','Box','Fighter','Parafoil','Character kite','Inflatable single-line'],
 x=[X('Delta kite','Triangular single-line kite, a popular easy-flying shape.','','',KI),X('Diamond kite','Classic two-stick kite, usually with a tail for stability.','','',KI)])
tbl=K('Toy ball','A ball made as a toy, not to a regulation standard.',UB,t=['Playground (utility) ball','Bouncy ball','Foam ball','Koosh ball','Spaldeen'],
 x=[X('Utility ball','Inflated playground ball, about 8.5 in, first made by Voit after the Second World War.','Voit','late 1940s',UB,dt='diameter 8.5 in · PVC or rubber · ribbed'),
    X('Super Ball','Polybutadiene rubber ball invented by Norman Stingley in 1964 and sold by Wham-O from 1965.','Wham-O','1965',SU,[('Over six million sold','Wham-O','1965','by December')])],
 m=[['Hedstrom Franklin Playground Ball','Hedstrom']])
tb=K('Bubble toy','A bubble-blowing toy.',BR,t=['Wand and bottle','Bubble ring','Giant-bubble wand','Bubble machine'],
 x=[X('Bubble ring','Ring-on-a-stem on a bottle cap, which replaced the bubble pipe.','','mid-20th century',BR)],r=[['Gazillion Bubbles','Gazillion Bubbles']])
fi=K('Fidget toy','A small handheld toy for fidgeting; shape variants do not make kinds.',HS,a='fidget',t=['Fidget cube','Fidget spinner','Stress ball','Pop-it','Squishy','Infinity cube','Spinner ring','Fidget keychain'],
 x=[X('Fidget spinner','Three-lobed spinner on a central ball bearing; boomed in 2017.','','2016',HS,[('Torqbar (Scott McCoskery)','','2014','provisional patent May 2016'),('Hettinger spinning toy patent','','1993','filed May 1993, issued 1997; no central bearing')],dt='lobes · bearing · metal or plastic'),
    X('Pop it','Silicone bubble board; mechanical design by Theo and Ora Coster.','Theora Concepts','1975',PI,[('FoxMind silicone Pop It','FoxMind','2009',''),('US Target launch','FoxMind / Buffalo Games','2019','')]),
    X('Squishy','Slow-rising foam or rubber squeeze toy, from Japan, in the US from 2017.','','2017',SQ,[('Mochi squishy','','','silicone, animal or food shapes')]),
    X('Stress ball','Squeezable ball up to about 7 cm in foam, bean bag or silicone.','','',SB)])
brands=[B('Wham-O','United States','','Mainstream','Frisbee, Super Ball','Toy maker that named and sold the Frisbee and the Super Ball.',FR,sig=['Pluto Platter / Frisbee']),
 B('Aerobie','United States','1984','Specialist','flying rings','Alan Adler\'s flying-ring company, sold to Swimways in 2017.',AE,sig=['Aerobie flying ring']),
 B('Duncan Toys','United States','','Heritage manufactory','yo-yos','Yo-yo maker that bought Flores around 1929; sold to Flambeau in 1968.',YY,sig=['Duncan yo-yo']),
 B('Pedro Flores','United States','1928','Heritage manufactory','yo-yo','Flores yo-yo company of Santa Barbara.',YY),
 B('Takara Tomy','Japan','2006','Mainstream','Beyblade, Plarail','Japanese toy maker formed when Takara merged with Tomy in 2006.',BB,sig=['Beyblade']),
 B('Takara','Japan','','Mainstream','Beyblade','Original developer of Beyblade before the 2006 merger.',BB),
 B('Sweets Kendamas','United States','2010','Specialist','kendama','US kendama company founded by Matt Jorgenson.',SW,sig=['Sweets Kendamas']),
 B('Voit','United States','','Heritage manufactory','playground balls','American maker of the first utility balls.',UB),
 B('Schylling','United States','','Mainstream','tin toys','Maker of the tin yo-yo in old data.','knowledge' if False else YY),
 B('Hedstrom','United States','','Mainstream','playground balls','Maker named in old data.',UB)]
brands=[b for b in brands if b['n'] not in ('Schylling','Hedstrom')]
trads=[{'n':'Kendama','g':'Games & play','r':'Hiroshima, Japan','p':'1919 modern form','d':'Japanese cup-and-ball skill toy; modern shape from Hatsukaichi.','tech':'turned wood','mat':'wood','forms':['Kendama'],'ctr':['Hatsukaichi','Kure'],'s':KD},
 {'n':'Beigoma','g':'Games & play','r':'Japan','p':'Edo period onward','d':'Metal battle tops, ancestors of Beyblade.','tech':'cast metal, formerly sand-filled shell','mat':'lead, cast metal','forms':['Spinning top'],'s':BG}]
write('07_00',[yo,tp,kd,fd,ki,tbl,tb,fi],brands,trads,'Left out: Duncan Imperial/Butterfly, YoYoFactory, Yumu kendama, Wham-O/Duncan founding facts and Fidget Cube (no retrievable page confirming them). Toy ball, bubble toy: Gazillion kept as range from old data. Merged all old fidget kinds into Fidget toy with types. Kite: no toy-specific page; kite types from Kite article only. Toy flying disc/kite fine.')
