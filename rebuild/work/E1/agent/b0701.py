import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
TB=WP+'Toy_piano'; SC=WP+'Schoenhut_Piano_Company'; CH='https://connecticuthistory.org/?p=43390'; MM=WP+'Marvin%27s_Magic'
MB1='https://mechanicalbanks.org/sy/s-2006-2010/2006-09.htm'; MB2='https://mechanicalbanks.org/sy/s-1982-1990/1988-08.htm'; MP='https://www.museumofplay.org/?p=8589'; PI=WP+'Pi%C3%B1ata'
ti=K('Toy musical instrument',"An instrument made as a toy that cannot do a real, tuned instrument's job, including pull-along musical toys; real instruments are in Musical Instruments & Music Gear.",TB,a='musical pull-toy · toy piano · toy xylophone',
 t=['Toy piano','Toy xylophone or glockenspiel','Rhythm set','Pull-along musical toy','Wooden','Plastic'],
 x=[X('Schoenhut toy piano','Metal-bar toy piano that replaced glass bars; made in Philadelphia since 1872.','Schoenhut','1872',SC,[('Albert Schoenhut metal bars','Schoenhut','','more durable than glass bars'),('Over 40 styles','Schoenhut','1935','50 cents to $25'),('O. Schoenhut, Inc.','Schoenhut','1936',''),('Schoenhut Piano Company revival','Schoenhut','1997','')],dt='octaves (1-3) · upright or grand · keys · wood or plastic'),
    X('Mid-century player toy pianos','Toy pianos with player mechanisms.','J. Chein & Company','1950s',TB,[('PianoLodeon','J. Chein & Company','1950s',''),('Tuneyville Player Piano','Tomy','1960s','organ-style pipes and plastic discs')])],
 m=[['Rhythm Makers Wooden Musical Instruments Set','Bigjigs Toys'],['Mini Rhythm Makers Natural Wooden Musical Instrument Set','Bigjigs Toys'],['Bigjigs Pull Along Xylophone','Bigjigs Toys']])
ms=K('Magic set','A set of tricks and props for conjuring.',CH,a='magic kit · conjuring set',t=['Beginner box','Hat or case set','Deluxe cabinet','Card trick set','Mind-reading set'],
 x=[X('Mysto Magic','Boxed magic sets sold by Gilbert\'s Mysto Manufacturing Company, formed while he was at Yale.','Mysto Manufacturing Company','',CH,[('Renamed A. C. Gilbert Co.','A. C. Gilbert','1916','Erector set from 1913')]),
    X('Marvin\'s Magic sets','UK magic-set company with ranges such as Magic Made Easy and Mind-Blowing Magic.',"Marvin's Magic",'1987',MM,[('Magic Made Easy',"Marvin's Magic",'',''),('Mind-Blowing Magic',"Marvin's Magic",'',''),('Ultimate Magic Collection',"Marvin's Magic",'','')])],
 m=[["Marvin's Magic Magic Hat","Marvin's Magic"]])
mb=K('Mechanical bank','A money bank with a mechanical action, collected as cast-iron antiques.',MP,a='cast-iron bank',
 t=['Cast iron original','Reproduction','Late tin bank','Coin-in-hand action','Lever action'],
 x=[X('Trick Dog','Dog jumps through a hoop into a barrel; patented by Daniel Cooke of Camden, 1888.','Shepard Hardware Company','1888',MB1,
      [('Design Patent 18,489','Daniel Cooke','1888','31 July'),('Shepard original','Shepard Hardware Company','late 1800s','two-screw base'),('Hubley six-part base','Hubley Manufacturing Company','c. 1906','brass twist pins'),('Hubley one-piece base','Hubley Manufacturing Company','c. 1920-1930','')],dt='maker · base construction · colour scheme · original or reproduction (about 1/8 in shorter)'),
    X('Eagle and Eaglets','Patriotic bank designed by Charles M. Henn of Chicago and cast by Stevens.','J. and E. Stevens Co.','1883',MB2,[('Patent 271,200','Charles M. Henn','1883','23 January'),('Light green and tan-brown colourways','J. and E. Stevens Co.','','differ only in base'),('Reproductions','','','base about 1/8 in shorter')]),
    X('Uncle Sam bank','Shepard Hardware cast-iron bank, a collecting staple.','Shepard Hardware Company','c. 1895',MP),
    X('Tammany Hall bank','Stevens bank satirising Boss Tweed; coin placed in right hand drops behind left arm.','J. and E. Stevens Co.','1875',MP),
    X('First cast-iron mechanical bank','Stevens made the earliest known cast-iron mechanical bank.','J. and E. Stevens Co.','1869',MP)],
 m=[['Elephant and Three Clowns','J. and E. Stevens Co.'],['Jumbo Elephant','J. and E. Stevens Co.'],['Light of Asia','J. and E. Stevens Co.'],['Trick Elephant','Hubley Manufacturing Company'],['Elephant with Tusks on Wheels','Kyser and Rex'],['Elephant Howdah Man Pops Up','Enterprise Manufacturing Company'],['Baby Elephant Opens at X O Clock','Charles A. Bailey']])
pn=K('Piñata','A hollow figure filled with sweets, broken at a party.',PI,t=['Papier-mâché','Clay pot (traditional)','Seven-point star','Character piñata','Pull-string'],
 x=[X('Mexican star piñata','Seven-point star said to stand for the seven deadly sins; used at Las Posadas.','','1586 (Acolman)',PI,[('Acolman','','1586','first evangelism use in local records')],dt='shape · clay or papier-mâché · filling')],
 m=[['Amscan Champagne Bottle Pinata','Amscan']])
tl=K('Toy light','A torch or nightlight shaped as a toy.','https://www.hope-education.co.uk/product/fe00057652',t=['Projector torch','Nightlight','Glow toy','Animal-shaped'],
 m=[['Brainstorm Toys Funny Animals Torch and Projector','Brainstorm Toys']])
brands=[B('Schoenhut','United States','1872','Heritage manufactory','toy pianos','Philadelphia maker of toy pianos, founded by Albert Schoenhut.',SC,sig=['Schoenhut toy piano']),
 B("Marvin's Magic",'United Kingdom','1987','Mainstream','magic sets','London magic-set company led by Marvin Berglas.',MM,sig=["Marvin's Magic sets"]),
 B('A. C. Gilbert Company','United States','','Heritage manufactory','Erector, Mysto Magic','New Haven toy company that began as Mysto Manufacturing.',CH,sig=['Mysto Magic']),
 B('J. and E. Stevens Co.','United States','','Heritage manufactory','cast-iron banks','Cromwell, Connecticut maker of the first cast-iron mechanical bank in 1869.',MP,sig=['Eagle and Eaglets','Tammany Hall bank']),
 B('Shepard Hardware Company','United States','','Heritage manufactory','cast-iron banks','Buffalo, New York maker of Trick Dog and Uncle Sam banks.',MB1,sig=['Trick Dog','Uncle Sam bank']),
 B('Hubley Manufacturing Company','United States','','Heritage manufactory','cast-iron toys','Lancaster, Pennsylvania maker that took over the Trick Dog patterns.',MB1)]
trads=[{'n':'Mexican piñata','g':'Festival & craft','r':'Mexico (Acolman)','p':'16th century onward','d':'Party figure of clay or papier-mâché broken for treats; linked to Las Posadas.','tech':'papier-mâché over balloon or clay pot','mat':'clay, paper, cardboard','forms':['Piñata'],'ctr':['Acolman'],'s':PI}]
write('07_01',[ti,ms,mb,pn,tl],brands,trads,'Merged Musical pull-toy into Toy musical instrument. Mechanical bank dates only where a retrieved page gives them; Uncle Sam date from Museum of Play (c. 1895) only. Kyser & Rex not described by a retrieved page, kept only as old-data maker. Toy light: no sourced archetype. Founding years for Stevens, Shepard, Hubley not given by retrieved pages, left blank. Mysto year omitted (not on fetched page).')
