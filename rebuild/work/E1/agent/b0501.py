import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
NE=WP+'Nerf'; SS=WP+'Super_Soaker'; GB=WP+'Gel_blaster'
fd=K('Foam dart blaster','A toy blaster that fires foam darts, balls or discs; slingshot and blowgun toys are types.',NE,a='dart blaster · Nerf blaster',
 t=['Spring-powered (single shot)','Flywheel (motorised)','Clip or drum fed','Pistol','Rifle','Bolt-action','Mega (large dart)','Modulus (modular)','Gel blaster (water-bead)','Slingshot toy','Blowgun toy','Third-party (Dart Zone, X-Shot)'],
 x=[X('Nerf N-Strike','Nerf\'s first big blaster line, launched 2004 and refreshed as N-Strike Elite in 2012.','Nerf','2004',NE,[('N-Strike Elite','Nerf','2012','update of N-Strike')]),
    X('Nerf Zombie Strike','Blaster line for Humans vs. Zombies fans.','Nerf','2013',NE),
    X('Nerf Rival','Older-user line firing High Impact Rounds.','Nerf','2015',NE),
    X('Nerf Ultra','Line with a proprietary dart design.','Nerf','2019',NE),
    X('Gel blaster','Airsoft-style toy gun firing 7-8 mm water beads, usually spring-piston with an electric motor.','','late 2010s',GB,[('Bottom-mounted motorised magazine','','2016','drove its popularity'),('Gas blowback','','2020','')],dt='power source · magazine · bead size')],
 m=[['Nerf Elite 2.0 Ace SD-1','Nerf'],['Nerf Elite 2.0 Quadfire QS-4','Nerf'],['Nerf Elite 2.0 Technician DS-2','Nerf'],['Nerf Elite Rebel Ops Doom Cannon','Nerf'],['Nerf Loadout Galactic Commander','Nerf']],r=[['Nerf Elite','Nerf'],['Nerf Loadout','Nerf']])
wb=K('Water blaster','Toy guns and pump blasters that squirt water.',SS,a='water gun · soaker · squirt gun',
 t=['Piston pumper','Pressurised reservoir','Air-pressure chamber','Spring-powered','Motorised','Constant Pressure System (CPS)','Backpack'],
 x=[X('Super Soaker','Pressurised-air water gun invented by Lonnie Johnson; first sold as Power Drencher.','Larami','1990',SS,
      [('Power Drencher','Larami','1990','first version, little advertising'),('Super Soaker 50','Larami','1991','renamed with TV ads; about two million sold'),('Constant Pressure System','Larami','1996','CPS line'),('Quick Blast','Hasbro','2008',''),('Flash Blast','Hasbro','2013','')],dt='tank size · pump type · range')],
 m=[['Nerf Super Soaker Dunk-Fill Freedom','Nerf'],['Nerf Super Soaker Flip Fill','Nerf'],['Nerf Super Soaker Power Drench','Nerf']],r=[['Super Soaker','Nerf']])
sw=K('Toy sword','Play swords, axes and daggers of foam, plastic or wood; LARP foam weapons only when sold as toys.','https://gdfb.co.uk/kids-toy-swords-and-lances-310-c.asp',a='play sword · foam sword',
 t=['Foam sword','Foam axe','Foam dagger','Plastic sword','Wooden sword','Shield and sword set','Light-up'],
 m=[['Nerf Nebula Ranger foam blade','Nerf'],['Nerf Shadowstrike Warrior Foam Daggers','Nerf'],['Nerf Storm Rage Thunderbeast Axe','Nerf']],r=[['Nerf N-Force','Nerf']])
brands=[B('Nerf','United States','1969','Mainstream','foam blasters','Foam toy brand created by Parker Brothers, now Hasbro; first foam dart blaster in 1992.',NE,sig=['Nerf N-Strike','Nerf Rival'],rel=['Hasbro','Larami']),
 B('Larami','United States','','Mainstream','water guns','Maker of the Power Drencher/Super Soaker; bought by Hasbro in 1995, closed 2002.',SS,sig=['Super Soaker']),
 B('Hasbro','United States','1923','Mainstream','toys and games','Owner of Nerf since buying Tonka in 1991.','knowledge'),
 B('Zuru','New Zealand','','Mainstream','X-Shot blasters','Maker of X-Shot toy blasters, a retail brand of gel and foam blasters.',GB)]
write('05_01',[fd,wb,sw],brands,[],'Merged "Other toy weapons" into the three kinds; slingshot/blowgun/gel/Dart Zone/X-Shot as types. Mega and Modulus listed as types only: no retrievable page (fan wiki returned 402). Dart Zone brand not attested, left out. No sourced toy-sword archetype; N-Force kept as range from old data. Nerf first-dart-blaster date per Wikipedia (1992).')
