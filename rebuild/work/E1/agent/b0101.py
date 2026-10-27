import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
DH = WP + 'Dollhouse'
E = 'Epoch'
house = K("Dolls' house", 'A house or building made at doll scale to be furnished and played in or displayed.',
  'https://calicocritters.com/en-us/catalog/categorieslist.php?category_id=4', a="dollhouse · doll's house",
  t=['1:12 collector scale', '1:16 / 1:18 play scale', '1:6 fashion-doll house', 'Kit or ready-built', 'Hinged front or open back'],
  x=[X('Baby house (cabinet house)', 'Display cabinet house for wealthy adults, the forerunner of the toy dolls\' house.', '', '16th century', DH,
       [('House for Albrecht V of Bavaria', '', '1557', 'earliest recorded European example'), ('Nuremberg houses', '', '', 'Nuremberg led production until WWI'),
        ("Queen Mary's Dolls' House", '', '1924', 'designed by Edwin Lutyens, Windsor Castle'), ("Titania's Palace", '', '', 'Egeskov Castle'),
        ("Colleen Moore's Fairy Castle", '', '', 'Museum of Science and Industry, Chicago')]),
     X("Tri-ang dolls' houses", 'English painted-wood houses from Lines Bros, from Tudor-style houses to rare Modernist designs.', 'Lines Bros', '1915',
       'https://collections.vam.ac.uk/item/O1191359/dolls-house-lines-bros-ltd',
       [("Lines Bros dolls' house (V&A B.127-2010)", 'Lines Bros', '1915', 'circa; two storeys, double bay, electric light'),
        ('Tudor-style houses', 'Lines Bros', '', 'long-running best sellers'), ('Thatched cottages and bungalows', 'Lines Bros', '', ''),
        ('Modernist house', 'Lines Bros', '', 'small run')]),
     X("Lundby", 'Swedish play-scale dolls\' houses, the first with electric lighting.', 'Lundby', '1947', WP + 'Lundby_(company)',
       [('Early house', 'Lundby', '1950s', ''), ('Göteborg (Gothenburg)', 'Lundby', '1959', 'renamed Småland in 2006'), ('Terrace / Flat Roof', 'Lundby', '1966', ''),
        ('Economy', 'Lundby', '', 'unlit Göteborg'), ('Stockholm', 'Lundby', '1975', 'new version 2005'), ('Gotland', 'Lundby', '2008', '')], dt='1:16, now 1:18 · 4-volt lighting'),
     X('Sylvanian Families houses', 'Houses for the flocked animal families, from cottages to manors.', E, '1985', WP + 'Sylvanian_Families',
       [('Red Roof Country Home', E, '', 'from old data'), ('Red Roof Cozy Cottage', E, '', 'from old data'), ('Red Roof Riverside Manor', E, '', 'from old data'),
        ('Red Roof Tower House', E, '', 'from old data'), ('Sweet Raspberry Home', E, '', 'from old data')], a='Calico Critters houses'),
     X("Le Toy Van dolls' houses", "Painted wooden dolls' houses from a family toy business that began with one.", 'Le Toy Van', '', 'https://well.ca/brand/le-toy-van.html?page=5',
       [('Cherry Tree Hall', 'Le Toy Van', '', 'from old data')])])
play = K('Playset', 'Small figures sold with a scene, building or set of accessories for pretend play.',
  'https://calicocritters.com/en-us/catalog/item_detail.php?product_id=2736', a='figure-and-scene playset',
  t=['Figure pack', 'Building or vehicle playset', 'Compact or carry case'],
  x=[X('Playmobil', '7.5 cm smiling figures (1:24) with themed buildings, vehicles and accessories.', 'Playmobil', '1974', WP + 'Playmobil',
       [('Knights', 'Playmobil', '1974', 'first sets'), ('Native Americans', 'Playmobil', '1974', 'first sets'), ('Construction workers', 'Playmobil', '1974', 'first sets'),
        ('Playmobil 1.2.3', 'Playmobil', '', 'chunky toddler line')], a='Klicky', dt='theme · figure · set number'),
     X('Little People', 'Chunky Fisher-Price figures with vehicles and buildings for young children.', 'Fisher-Price', '1959', WP + 'Little_People_(toys)',
       [('#959 Safety School Bus', 'Fisher-Price', '1959', 'early precursor'), ('Nifty Station Wagon', 'Fisher-Price', '1960', 'first Play Family'),
        ('Play Family Barn', 'Fisher-Price', '1968', 'first playset'), ('Play Family dollhouse', 'Fisher-Price', '1969', ''),
        ('Renamed Little People', 'Fisher-Price', '1985', ''), ('Chunkier redesign', 'Fisher-Price', '1991', ''), ('Redesign with arms', 'Fisher-Price', '1996', ''),
        ('Taller figures', 'Fisher-Price', '2013', '')], a='Play Family', tg=None) if False else
     X('Little People', 'Chunky Fisher-Price figures with vehicles and buildings for young children.', 'Fisher-Price', '1959', WP + 'Little_People_(toys)',
       [('#959 Safety School Bus', 'Fisher-Price', '1959', 'early precursor'), ('Nifty Station Wagon', 'Fisher-Price', '1960', 'first Play Family'),
        ('Play Family Barn', 'Fisher-Price', '1968', 'first playset'), ('Play Family dollhouse', 'Fisher-Price', '1969', ''),
        ('Renamed Little People', 'Fisher-Price', '1985', ''), ('Chunkier redesign', 'Fisher-Price', '1991', ''), ('Redesign with arms', 'Fisher-Price', '1996', ''),
        ('Taller figures', 'Fisher-Price', '2013', '')], a='Play Family'),
     X('Sylvanian Families', 'Flocked animal families with shops, villages and accessories.', E, '1985', WP + 'Sylvanian_Families',
       [('Calico Critters', E, '1993', 'North American name'), ('Bakery Shop Starter Set', E, '', 'from old data'), ('Village Cake Shop Starter Set', E, '', 'from old data'),
        ('Village Doctor Starter Set', E, '', 'from old data'), ('Fairy Mushroom House', E, '', 'from old data')], a='Calico Critters'),
     X('Polly Pocket', 'Tiny dolls in a hinged compact that opens into a scene.', 'Bluebird Toys', '1989', WP + 'Polly_Pocket',
       [('Compact playsets', 'Bluebird Toys', '1989', ''), ('Mattel redesign', 'Mattel', '1998', 'larger dolls')])])
mini = K("Dolls' house miniatures", "Scale furniture, fittings and accessories for furnishing a dolls' house, collected as an adult hobby.", DH,
  a='dollhouse miniatures · miniatures', t=['1:12 (one inch)', '1:24 (half scale)', '1:48 and smaller', 'Furniture', 'Lighting and electrics',
  'Wallpaper and flooring', 'Food and accessories', 'Dolls'])
brands = [
 B('Playmobil', 'Germany', '', 'Premium', 'play figures', 'Figure toy system by geobra Brandstätter of Zirndorf, designed by Hans Beck.', WP + 'Playmobil', sig=['Playmobil figure']),
 B('Fisher-Price', 'United States', '', 'Mainstream', 'pre-school toys', 'US pre-school toy maker, owned by Mattel; maker of Little People.', 'knowledge', sig=['Little People'], rel=['Mattel']),
 B('Epoch', 'Japan', '', 'Mainstream', 'Sylvanian Families', 'Japanese toy and game company behind Sylvanian Families / Calico Critters.', WP + 'Sylvanian_Families', sig=['Sylvanian Families']),
 B('Lundby', 'Sweden', '1947', 'Heritage manufactory', "dolls' houses", "Swedish maker of play-scale dolls' houses and furniture.", WP + 'Lundby_(company)'),
 B('Lines Bros', 'United Kingdom', '', 'Heritage manufactory', "Tri-ang toys", "Merton, Surrey toy maker trading as Tri-ang, known for wooden dolls' houses.", 'https://collections.vam.ac.uk/item/O1191359/dolls-house-lines-bros-ltd'),
 B('Le Toy Van', '', '', 'Artisan & independent', "wooden dolls' houses", "Family wooden-toy business founded by Georges Le Van.", 'https://well.ca/brand/le-toy-van.html?page=5'),
 B('KidKraft', 'United States', '', 'Mainstream', "dolls' houses, play kitchens", "Dallas maker of wooden dolls' houses and play kitchens.", 'knowledge'),
]
notes = ("Dolls' house: old Epoch and Le Toy Van models became versions of their archetypes; added baby houses (with museum landmarks), Tri-ang (Lines Bros), Lundby. "
 "Playset: Playmobil, Little People, Sylvanian Families (old models as versions), Polly Pocket. New kind Dolls' house miniatures (scales and item types; no archetypes). "
 "KidKraft has a knowledge-only brand entry; no KidKraft models added (no product page retrieved). Tri-ang No. 65 not added (museum page blocked).")
write('01_01', [house, play, mini], brands, [], notes)
