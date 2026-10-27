import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
CW = 'https://collectorsweekly.com/articles/?p=15309'
AT = 'https://atca-club.org/?p=2256'
robot = K('Toy robot', 'A robot made as a toy for play or display; science experiment kits are in Observing & Measuring.',
  'https://wonderkidstoy.com/collections/coding-and-robotics-toys', a='robot toy',
  t=['Wind-up tin robot', 'Battery-operated robot', 'Interactive pet or companion robot', 'Remote-controlled robot', 'App-controlled robot'],
  x=[X('Lilliput', 'Early wind-up Japanese tin robot, widely called the first tin toy robot.', '', '', CW,
       [('Original', '', '', 'fan-shaped "KT" logo, marked Made in Japan or Japan'), ('Reproduction', '', '', '"Tin Tom Toy" logo, no Japan mark, larger')],
       dt='tinplate · wind-up · original vs reproduction'),
     X('Masudaya "Gang of Five"', 'Five 15-inch skirted battery robots made by Masudaya between 1957 and 1964.', 'Masudaya', '1957', AT,
       [('Radicon Robot', 'Masudaya', '1957', 'first radio-controlled robot of the group'), ('Non-Stop Robot', 'Masudaya', '1959', '"Lavender Robot"'),
        ('Giant Machine Man', 'Masudaya', '', 'red special-order variant; rarest'), ('Giant Sonic Robot', 'Masudaya', '1962', ''),
        ('Target Robot (Shooting Giant Robot)', 'Masudaya', '1964', 'with dart pistol')], dt='tinplate · battery · boxed or unboxed'),
     X('Furby', 'Talking owl-like interactive robot pet that appears to learn speech.', 'Hasbro', '1998', WP + 'Furby',
       [('Furby (Tiger Electronics)', 'Hasbro', '1998', 'designers Dave Hampton and Caleb Chung'), ('Furby Babies', 'Hasbro', '1999', ''),
        ('Emoto-Tronic Furby', 'Hasbro', '2005', ''), ('Furby (third generation)', 'Hasbro', '2012', ''), ('Furby Boom', 'Hasbro', '2013', ''),
        ('Furby Connect', 'Hasbro', '2016', ''), ('Furby (fifth generation)', 'Hasbro', '2023', '')]),
     X('Robosapien', 'Remote-controlled humanoid robot designed by Mark Tilden.', 'WowWee', '2004', WP + 'Robosapien',
       [('Robosapien', 'WowWee', '2004', ''), ('Robosapien Jr.', 'Hasbro', '2005', 'Playskool licence'), ('Robosapien X', 'WowWee', '2014', ''),
        ('Robosapien Blue', 'WowWee', '2014', ''), ('Robosapien Remix', 'WowWee', '2021', '')]),
     X('Cozmo', 'Small forklift-shaped companion robot with an expressive face, run from a phone app.', 'Anki', '2016', WP + 'Cozmo',
       [('Cozmo', 'Anki', '2016', ''), ('Vector', 'Anki', '2018', 'successor'), ('Digital Dream Labs relaunch', 'Digital Dream Labs', '2021', '')])])
code = K('Coding toy', 'A toy that teaches or plays at programming through commands, blocks or an app.',
  'https://www.learningresources.com/item-botleyr-the-coding-robot-2', a='programmable robot · coding robot',
  t=['Screen-free coding robot', 'Floor robot', 'App-coded robot ball', 'Programmable brick kit'],
  x=[X('LEGO Mindstorms', 'Programmable LEGO brick with motors and sensors for building robots.', 'LEGO', '1998', WP + 'Lego_Mindstorms',
       [('Robotics Invention System (RCX)', 'LEGO', '1998', ''), ('NXT', 'LEGO', '2006', ''), ('NXT 2.0', 'LEGO', '2009', ''),
        ('EV3', 'LEGO', '2013', ''), ('Robot Inventor', 'LEGO', '2020', 'last set; line ended 2022'),
        ('Spike Prime', 'LEGO', '2019', 'education successor, not branded Mindstorms')]),
     X('LEGO Boost', 'App-coded LEGO kit with a motorised hub that builds into a robot and other models.', 'LEGO', '2017', 'https://brickfact.com/sets/lego-boost-boost-creative-toolbox-17101',
       [('17101 Creative Toolbox', 'LEGO', '2017', '843 pieces; builds Vernie the Robot')]),
     X('Bee-Bot', 'Bee-shaped floor robot programmed with arrow keys, made for young children.', 'TTS', '', 'https://distributor.tts-group.co.uk/2023/09/bee-bot-the-story-behind-our-tts-developed-award-winning-programmable-robot/',
       [('Bee-Bot (rechargeable)', 'TTS', '', 'up to 200 commands'), ('Blue-Bot', 'TTS', '', 'app-linked sibling')], a='floor robot'),
     X('Cubetto', 'Wooden robot coded by placing blocks on a board, for children from three, without screens.', 'Primo Toys', '2016',
       'https://www.dezeen.com/2016/03/09/cubetto-primo-toys-preschool-children-coding-programming-wooden-robot/amp/'),
     X('Sphero', 'App-controlled and programmable robot ball, later rovers and cars.', 'Sphero', '2011', WP + 'Sphero',
       [('Sphero', 'Sphero', '2011', 'original ball'), ('Sphero 2.0', 'Sphero', '2013', ''), ('BB-8', 'Sphero', '2015', 'Disney licence'),
        ('Sphero SPRK+', 'Sphero', '', 'education'), ('Sphero BOLT', 'Sphero', '', ''), ('Sphero BOLT+', 'Sphero', '', 'LCD screen'),
        ('Sphero Mini', 'Sphero', '', ''), ('Sphero RVR', 'Sphero', '2019', 'rover; later RVR+'), ('Sphero indi', 'Sphero', '', 'for younger learners')])],
  m=[['Botley 2.0 the Coding Robot', 'Learning Resources']])
brands = [
 B('Masudaya', 'Japan', '1724', 'Heritage manufactory', 'tin robots', 'Old Japanese toy company (MT logo) behind the Gang of Five robots.', AT),
 B('Hasbro', 'United States', '', 'Mainstream', 'toys and games', 'US toy and games company; owns Tiger Electronics and Furby.', 'knowledge'),
 B('WowWee', '', '', 'Mainstream', 'robot toys', 'Toy maker of Robosapien and other robot toys.', 'knowledge'),
 B('Anki', 'United States', '', 'Specialist', 'companion robots', 'Robotics start-up behind Cozmo and Vector; assets bought by Digital Dream Labs in 2019.', WP + 'Cozmo'),
 B('Sphero', 'United States', '2010', 'Specialist', 'robot balls', 'Boulder, Colorado maker of programmable robots (formerly Orbotix); bought littleBits in 2019.', WP + 'Sphero'),
 B('TTS', 'United Kingdom', '', 'Specialist', 'classroom resources', 'UK educational supplier that developed Bee-Bot.', 'https://distributor.tts-group.co.uk/2023/09/bee-bot-the-story-behind-our-tts-developed-award-winning-programmable-robot/'),
 B('Primo Toys', 'United Kingdom', '', 'Artisan & independent', 'screen-free coding', 'London maker of the Cubetto wooden coding robot.', 'https://www.dezeen.com/2016/03/09/cubetto-primo-toys-preschool-children-coding-programming-wooden-robot/amp/'),
 B('Learning Resources', 'United States', '', 'Mainstream', 'educational toys', 'US maker of educational toys including the Botley coding robot.', 'knowledge'),
]
notes = ("Both old kinds kept. Toy robot gained archetypes Lilliput, Masudaya Gang of Five, Furby, Robosapien, Cozmo; Coding toy gained LEGO Mindstorms "
 "(with Spike Prime as a version), LEGO Boost, Bee-Bot, Cubetto and Sphero (old Sphero models became versions). Botley stays in m (maker page not retrieved). "
 "Other Japanese tin-robot makers (Yonezawa, Horikawa, Nomura) not added: no page retrieved. LEGO brand entry is in shelf 00_00. Science kits left to their own category.")
write('00_01', [robot, code], brands, [], notes)
