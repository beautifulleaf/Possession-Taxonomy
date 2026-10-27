import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
TB = WP + 'Teddy_bear'; ST = WP + 'Steiff'; MT = WP + 'Merrythought'
JC = WP + 'Jellycat'; JB = 'https://sendatoy.com.au/blogs/news/history-of-jellycat-worlds-most-beloved-soft-toy-brand'
def T(n, g, r, p, d, tech, mat, forms, ctr, auth, s):
    return {'n': n, 'g': g, 'r': r, 'p': p, 'd': d, 'tech': tech, 'mat': mat, 'forms': forms, 'ctr': ctr, 'auth': auth, 's': s}
teddy = K('Teddy bear', 'A stuffed toy bear, classically jointed and covered in mohair, named after Theodore Roosevelt.', TB,
  a='teddy · bear', t=['Jointed mohair bear', 'Unjointed plush bear', 'Artist or limited-edition bear', 'Replica of an antique bear', 'Musical or dangling bear'],
  x=[X('Steiff jointed bear', 'Jointed plush bear designed by Richard Steiff, the first with movable arms and legs, marked by a button in the ear.', 'Steiff', '1902', ST,
       [('55 PB', 'Steiff', '1902', 'original design; no example survives, replica at the Steiff Museum, Giengen'),
        ('Button in ear', 'Steiff', '1904', 'trademark tag devised by Franz Steiff against counterfeits'),
        ('Teddy Girl', 'Steiff', '1904', 'sold for $165,000 at auction in 1994'),
        ('Black Titanic mourning bear', 'Steiff', '1912', 'black bears made after the sinking'),
        ('Harlequin bear', 'Steiff', '1925', 'circa; Christie\'s estimate £50,000–80,000'),
        ('My First Steiff Teddy Bear', 'Steiff', '', 'from old data'), ('Honey Teddy Bear', 'Steiff', '', 'from old data'),
        ('Paddy Teddy Bear', 'Steiff', '', 'from old data'), ('Jimmy Teddy Bear in Suitcase', 'Steiff', '', 'from old data'),
        ('Charly Dangling Teddy Bear', 'Steiff', '', 'from old data')], a='Steiff teddy', dt='size · mohair colour · jointing · button and tag type'),
     X("Teddy's bear (Michtom)", "Bear cub made by Morris Michtom after Berryman's 1902 Roosevelt cartoon, which led to the Ideal toy company.", 'Ideal Toy Company', '1902', TB,
       [("Teddy's bear", 'Ideal Toy Company', '1902', 'shown in Michtom\'s New York shop window')]),
     X('Merrythought bears', 'Handmade mohair bears from the last traditional teddy factory in Britain, at Ironbridge.', 'Merrythought', '1930', MT,
       [('Magnet', 'Merrythought', '1931', 'circa; first Merrythought bear, M series'), ('Punkinhead', 'Merrythought', '1948', ''),
        ('Cheeky', 'Merrythought', '1957', 'still produced'), ('Mr Whoppit', 'Merrythought', '', "Donald Campbell's mascot"),
        ('Hope Bear', 'Merrythought', '2001', 'World Trade Center fund'), ('Heathcliff', 'Merrythought', '2004', 'edition of 100, black mohair')]),
     X('Gund bears', 'Soft American teddy bears, Gund\'s core line since the early 20th century.', 'Gund', '1898', WP + 'Gund',
       [('Snuffles', 'Gund', '1981', 'crescent-moon design; longest-running Gund bear'), ('Signature Collection', 'Gund', '1980s', 'collectible bears')]),
     X('Storybook bears', 'Teddy bears modelled on bears from children\'s books and comics, made under licence by many makers.', '', '1920', TB,
       [('Rupert Bear', '', '1920', 'Daily Express strip'), ('Winnie-the-Pooh', '', '1926', "based on Christopher Robin Milne's bear"),
        ('Paddington Bear', '', '1958', "inspired by a teddy Michael Bond bought"), ('Corduroy', '', '1968', 'picture book')])])
plush = K('Plush toy', 'A stuffed fabric toy of an animal, character or object, other than a teddy bear.', WP + 'Stuffed_toy',
  a='stuffed animal · soft toy · cuddly toy · plushie', t=['Animal', 'Licensed character', 'Bean-filled', 'Clip-on or bag charm', 'Pillow plush', 'Comforter'],
  x=[X('Beanie Babies', 'Small pellet-filled animals with heart swing tags and names, the 1990s collecting craze.', 'Ty', '1993', WP + 'Beanie_Babies',
       [('Original nine', 'Ty', '1993', 'Legs the Frog, Squealer the Pig, Spot the Dog, Flash the Dolphin, Splash the Whale, Chocolate the Moose, Patti the Platypus, Brownie the Bear, Pinchers the Lobster'),
        ('Poem swing tags', 'Ty', '1996', 'tags with poem and birthday'), ('Teenie Beanies', 'Ty', '1996', "miniatures with McDonald's Happy Meals")],
       dt='character · tag generation · tush tag · colour variant'),
     X('Care Bears', 'Pastel bears each with a symbol on the tummy, from greeting-card art.', 'American Greetings', '1981', WP + 'Care_Bears',
       [('Kenner plush', 'Kenner', '1983', 'first toys; ten original bears incl. Tenderheart, Cheer, Grumpy, Funshine'), ('Care Bear Cousins', 'Kenner', '1984', 'other animals'),
        ('Relaunch', 'Play Along', '2002', '13-inch plush'), ('Hasbro line', 'Hasbro', '2010', ''), ('Just Play line', 'Just Play', '2014', ''), ('Basic Fun line', 'Basic Fun', '2019', '')]),
     X('Jellycat Bashful Bunny', 'Long-eared soft bunny in many colours and sizes, the London brand\'s best-known design.', 'Jellycat', '2000s', JB,
       [('Bashful Bunny', 'Jellycat', '2000s', 'early 2000s'), ('Amuseables', 'Jellycat', '', 'smiling foods and objects'), ('Slackajack Monkey', 'Jellycat', '', 'longest-serving design')],
       dt='colour · size'),
     X('Squishmallows', 'Round, very soft marshmallow-like plush characters with names and backstories.', 'Kelly Toys', '2017', WP + 'Squishmallows',
       [('Squishmallows', 'Kelly Toys', '2017', 'sizes from 3.5-inch clip-on to 24-inch'), ('HugMees', 'Kelly Toys', '', ''), ('Stackables', 'Kelly Toys', '', ''),
        ('FuzzAMallows', 'Kelly Toys', '', ''), ('Squish-Doos', 'Kelly Toys', '', ''), ('Micromallows', 'Kelly Toys', '', '')], dt='character · size · sub-line'),
     X('Webkinz', 'Plush pets with a code that unlocks a virtual version online.', 'Ganz', '2005', WP + 'Stuffed_toy')])
puppet = K('Puppet', 'A figure worked by the hand, rods or strings to act out play.', 'https://folkmanis.com/cat-256-1-14/all-puppets.htm',
  a='hand puppet · marionette', t=['Hand or glove puppet', 'Finger puppet', 'Rod puppet', 'Marionette (string puppet)', 'Shadow puppet', 'Sock puppet', 'Ventriloquist dummy', 'Puppet theatre or booth'],
  x=[X('Punch and Judy', 'English glove-puppet show with Mr Punch, Judy, the Baby, Constable and Crocodile, played from a booth.', '', '1662', WP + 'Punch_and_Judy',
       [('Marionette Punch', '', '1662', 'seen by Pepys at Covent Garden'), ('Glove-puppet Punch', '', '18th century', 'later 18th century'), ('Seaside booth', '', '20th century', 'red-and-white striped')],
       dt='character set · booth · swazzle'),
     X('Czech marionette', 'Carved wooden string marionettes of the Czech travelling puppeteers.', '', '18th century', 'https://unima.idu.cz/en/history-of-czech-puppetry/',
       [('Travelling family theatres', '', '19th century', 'Kopecký and other families'), ('Spejbl and Hurvínek', '', '', "Josef Skupa's Plzeň theatre")]),
     X('Bunraku puppet', 'Large Japanese puppet with a carved wooden head, worked by three puppeteers.', '', '17th century', WP + 'Bunraku'),
     X('Wayang kulit', 'Flat, punched and painted hide shadow puppet on horn rods, from Java and Bali.', '', '', WP + 'Wayang_kulit',
       [('Wayang golek', '', '', 'three-dimensional wooden rod puppet'), ('Wayang klitik', '', '', 'flat wooden puppet')])])
brands = [
 B('Steiff', 'Germany', '1880', 'Heritage manufactory', 'teddy bears', 'Giengen plush maker founded by Margarete Steiff, maker of the first jointed teddy bear.', ST, sig=['Steiff jointed bear'], rel=['Ravensburger']),
 B('Merrythought', 'United Kingdom', '1930', 'Heritage manufactory', 'mohair bears', 'Family-owned Ironbridge, Shropshire maker of handmade mohair teddy bears.', MT, sig=['Merrythought bears']),
 B('Gund', 'United States', '1898', 'Mainstream', 'teddy bears', 'New York-founded plush maker now in Edison, New Jersey, owned by Spin Master since 2018.', WP + 'Gund', sig=['Gund bears']),
 B('Ideal Toy Company', 'United States', '', 'Heritage manufactory', "Teddy's bear", "New York toy company founded by Morris Michtom after his 1902 Teddy's bear.", TB),
 B('Ty', 'United States', '1986', 'Mainstream', 'Beanie Babies', "Ty Warner's plush company, maker of Beanie Babies.", WP + 'Beanie_Babies', sig=['Beanie Babies']),
 B('American Greetings', 'United States', '', 'Mainstream', 'greeting cards', 'Greeting-card company that created the Care Bears characters.', WP + 'Care_Bears', sig=['Care Bears']),
 B('Kenner', 'United States', '', 'Mainstream', 'licensed toys', 'US toy maker of the first Care Bears plush.', WP + 'Care_Bears'),
 B('Jellycat', 'United Kingdom', '1999', 'Premium', 'soft toys', 'London soft-toy brand founded by Thomas and William Gatacre.', JC, sig=['Jellycat Bashful Bunny']),
 B('Kelly Toys', 'United States', '1986', 'Mainstream', 'Squishmallows', 'Los Angeles plush maker of Squishmallows, owned by Jazwares since 2020.', WP + 'Squishmallows', sig=['Squishmallows']),
 B('Ganz', 'Canada', '', 'Mainstream', 'Webkinz', 'Toy and gift company behind Webkinz.', 'knowledge', sig=['Webkinz']),
]
trads = [
 T('Punch and Judy', 'Toys & puppetry', 'England', '1662 to present', 'Seaside and street glove-puppet show descended from the Neapolitan Pulcinella.',
   'carved and painted glove puppets; booth; swazzle voice', 'wood, cloth', ['Puppet'], ['Covent Garden', 'English seaside resorts'], 'hand-carved heads; traditional character set', WP + 'Punch_and_Judy'),
 T('Czech marionette puppetry', 'Toys & puppetry', 'Bohemia (Czech lands)', 'late 18th century to present', 'Travelling family marionette theatres, with figures carved by church sculptors.',
   'wood carving, string marionettes', 'wood', ['Puppet'], ['Kopecký family', 'Matěj Kopecký', 'Josef Skupa, Plzeň'], 'hand-carved wooden heads and limbs in Baroque style', 'https://unima.idu.cz/en/history-of-czech-puppetry/'),
 T('Bunraku', 'Toys & puppetry', 'Osaka, Japan', '17th century to present', 'Japanese puppet theatre with large puppets each worked by three puppeteers.',
   'carved kashira heads, three-person manipulation', 'wood, human hair, cloth', ['Puppet'], ['National Bunraku Theatre, Osaka', 'Awaji'], 'specialist-carved wooden kashira', WP + 'Bunraku'),
 T('Wayang kulit', 'Toys & puppetry', 'Java and Bali, Indonesia', 'late 1st millennium CE to present', 'Shadow puppet theatre of punched and painted hide figures, played by a dalang with gamelan; UNESCO 2003.',
   'cutting and punching rawhide with tatah, painting, horn handles', 'water buffalo or goat hide, horn, bamboo', ['Puppet'], ['Sukawati, Bali'], 'fine punched hide, horn rods, hand painting', WP + 'Wayang_kulit'),
]
notes = ("Teddy bear split from Plush toy as its own kind; old Steiff models became versions of the Steiff jointed bear archetype. Pop Mart vinyl-face plush ranges (Labubu/THE MONSTERS, MOLLY etc.) and Kidrobot Labbit "
 "left out here for the Designer toy shelf (vinyl-face figures, not plush). Puppet keeps old s; added glove, rod, marionette, shadow types and four tradition archetypes. "
 "Hermann, Build-A-Bear, Vermont Teddy Bear and Folkmanis not given archetypes (no models confirmed); Jellycat Bashful Bunny year only 'early 2000s'.")
write('01_02', [teddy, plush, puppet], brands, trads, notes)
