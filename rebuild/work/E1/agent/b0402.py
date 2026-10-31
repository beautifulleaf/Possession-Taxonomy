import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
MTG = WP + 'Magic:_The_Gathering'; PBS = WP + 'Base_Set_(Pok%C3%A9mon)'; YGO = WP + 'Yu-Gi-Oh!_Trading_Card_Game'; FAB = WP + 'Flesh_and_Blood_(card_game)'; OP = WP + 'One_Piece_Card_Game'
LOR = 'https://techraptor.net/games/disney-lorcana'; W40 = WP + 'Warhammer_40,000:_Rogue_Trader'; AOS = WP + 'Warhammer_Age_of_Sigmar'; BA = WP + 'Bolt_Action_(wargame)'; XW = WP + 'Star_Wars:_X-Wing_Second_Edition'
BC = 'https://bardsandcards.com/blogs/news/complete-guide-card-sleeves-deck-boxes-tcg-storage'; CB = 'https://comicbook.com/gear/product-news/best-card-binders-pokemon-tcg/'; PM = 'https://geekydomain.com/products/celestial-tcg-playmat-standard-24-14-card-game-mat-geeky-domain'
pk = K('Trading card packs & boxes', 'A sealed pack, box, tin or ready-made deck of a trading card game, such as a booster pack, booster box, collection box, tin, or starter or structure deck.',
  'https://cardcosmos.de/en/collections/the-pokemon-company-international?page=18', a='sealed product · booster pack · booster box · starter deck · structure deck',
  t=['Booster pack', 'Booster box', 'Starter or structure deck', 'Preconstructed (Commander) deck', 'Tin', 'Collection or gift box', 'Japanese-language', 'English-language', 'First edition print'],
  x=[X('Magic: The Gathering', 'The first collectible card game, from Wizards of the Coast.', 'Wizards of the Coast', '1993', MTG,
       [('15-card booster pack', 'Wizards of the Coast', '1993', 'one rare, three uncommons'), ('Commander precon decks', 'Wizards of the Coast', '', 'with most sets since Ikoria'), ('Play Booster', 'Wizards of the Coast', '2024', 'from Murders at Karlov Manor'),
        ('Secret Lair', 'Wizards of the Coast', '', 'crossover promo drops'), ('Jumpstart', 'Wizards of the Coast', '', '')], dt='set · pack type · language · first or later printing'),
     X('Pokémon Trading Card Game', 'Card game based on the Pokémon video games, first published by Media Factory in Japan.', 'Media Factory', '1996', PBS,
       [('Base Set (Japan)', 'Media Factory', '1996', '1st Starter & Expansion Pack, 20 October'), ('Base Set (US)', 'Wizards of the Coast', '1999', '102 cards'), ('Base Set 2', 'Wizards of the Coast', '2000', '130 cards')]),
     X('Yu-Gi-Oh! Trading Card Game', 'Konami card game based on the Duel Monsters game in the manga.', 'Konami', '1999', YGO,
       [('Official Card Game', 'Konami', '1999', 'Japan'), ('TCG', 'Konami', '2002', 'North America, first via Upper Deck'), ('Speed Duel', 'Konami', '2019', ''), ('Collectible tins', 'Konami', '', '')]),
     X('Flesh and Blood', 'New Zealand trading card game designed by James White.', 'Legend Story Studios', '2019', FAB,
       [('Welcome to Rathe', 'Legend Story Studios', '2019', 'first set, 226 cards'), ('First Edition and Unlimited', 'Legend Story Studios', '', 'cold-foil first editions; later a single model')]),
     X('One Piece Card Game', 'Bandai card game covering the whole One Piece series.', 'Bandai', '2022', OP, [('Japanese release', 'Bandai', '2022', '8 July'), ('Global release', 'Bandai', '2022', '2 December; four starter decks')]),
     X('Disney Lorcana', 'Disney-character card game from Ravensburger.', 'Ravensburger', '2023', LOR, [('The First Chapter', 'Ravensburger', '2023', '18 August in hobby stores')])])
sg = K('Trading card single', 'A single card of a trading card game; a graded card stays here, but one particular card is an individual item and not listed as a kind.', 'https://cardcosmos.de/en/collections/the-pokemon-company-international?page=18',
  a='single card', t=['Common', 'Uncommon', 'Rare', 'Foil or holo', 'First edition', 'Unlimited', 'Promo', 'Language', 'Raw', 'Graded (see collecting view)'],
  x=[X('Pokémon Base Set printings', 'The three printings of the first English Pokémon set that collectors tell apart.', 'Wizards of the Coast', '1999', PBS,
       [('1st Edition', 'Wizards of the Coast', '1999', 'Edition 1 stamp'), ('Shadowless', 'Wizards of the Coast', '1999', 'first Unlimited print, no frame shadow'), ('Unlimited', 'Wizards of the Coast', '', 'corrected later print')])])
ss = K('Miniatures game starter set', 'A box with miniatures, rules and accessories to start a miniatures game.', 'https://nobleknight.com/P/2148065632/Warhammer-40000-Starter-Set',
  t=['Two-player starter', 'Core set', 'Edition launch box', 'Pre-painted miniatures', 'Unpainted plastic kits'],
  x=[X('Warhammer 40,000', 'Games Workshop\'s science-fiction miniatures wargame.', 'Games Workshop', '1987', W40,
       [('Rogue Trader', 'Games Workshop', '1987', 'first edition, Games Day, October'), ('Warhammer 40,000 Starter Set', 'Games Workshop', '', 'old data')], dt='edition · factions in the box'),
     X('Warhammer Age of Sigmar', 'Fantasy miniatures wargame that replaced Warhammer Fantasy Battle.', 'Games Workshop', '2015', AOS,
       [('1st edition', 'Games Workshop', '2015', ''), ('2nd edition', 'Games Workshop', '2018', ''), ('3rd edition', 'Games Workshop', '2021', 'June'), ('4th edition', 'Games Workshop', '2024', 'July'), ('Dominion', 'Games Workshop', '', 'starter set'), ('Skaventide', 'Games Workshop', '', 'starter set')]),
     X('Bolt Action', 'Second World War 28 mm wargame by Cavatore and Priestley.', 'Warlord Games', '2012', BA,
       [('2nd edition', 'Warlord Games', '2016', ''), ('3rd edition', 'Warlord Games', '2024', ''), ('Island Assault', 'Warlord Games', '', 'starter set'), ("A Gentleman's War", 'Warlord Games', '', 'starter set')]),
     X('Star Wars: X-Wing', 'Pre-painted starfighter dogfighting game.', 'Fantasy Flight Games', '2018', XW,
       [('Second Edition core set', 'Fantasy Flight Games', '2018', 'T-65 X-Wing and two TIE fighters'), ('Atomic Mass Games line', 'Atomic Mass Games', '2020', 'development ended June 2024')])],
  r=[['Warhammer 40,000', 'Games Workshop']])
ab = K('Miniatures game army box', 'A box of miniatures making up a unit or army for a miniatures game; faction boxes are examples.', 'https://www.nobleknight.com/P/2148098523/Combat-Patrol---Adeptus-Mechanicus',
  a='army or unit box · faction box', t=['Unit box', 'Combat Patrol or starter army', 'Battleforce or army deal', 'Character model', 'Ship or vehicle expansion'],
  m=[['Combat Patrol: Adeptus Mechanicus', 'Games Workshop']], r=[['Warhammer 40,000', 'Games Workshop']])
sl = K('Card sleeve', 'A protective sleeve for individual playing or trading cards.', BC, a='card protector',
  t=['Standard (63 × 88 mm)', 'Small / Japanese (62 × 89 mm)', 'Inner (perfect-fit)', 'Outer', 'Matte', 'Gloss', 'Art-backed'],
  x=[X('Dragon Shield sleeves', 'Matte opaque-backed sleeves, the most recommended line.', 'Arcane Tinmen', '', BC,
       [('Matte', 'Arcane Tinmen', '', ''), ('Non-Glare', 'Arcane Tinmen', '', 'tournament favourite'), ('Perfect Fit', 'Arcane Tinmen', '', 'thin inner sleeve')]),
     X('KMC Hyper Matte', 'Silky, slightly thinner Japanese sleeves, good for double-sleeving.', 'KMC', '', BC),
     X('Gamegenic sleeves', 'Value-pack sleeves.', 'Gamegenic', '', BC, [('Value Pack (200)', 'Gamegenic', '', '')])],
  r=[['Dragon Shield sleeves', 'Arcane Tinmen']])
db = K('Deck box', 'A box made to hold a deck of cards.', BC, t=['Snap-top', 'Magnetic', 'Commander (100+)', 'With dice tray'],
  m=[['Gamegenic Sidekick', 'Gamegenic'], ['Gamegenic Watchtower', 'Gamegenic'], ['Ultimate Guard Boulder', 'Ultimate Guard'], ['Ultra Pro Satin Tower', 'Ultra PRO']])
pb = K('Playmat & card binder', 'A cloth-topped rubber mat for playing cards on, or a binder of pocket pages for storing a card collection.', PM, a='playmat · play mat · card binder · card album',
  t=['Playmat 24 × 14 in', 'Neoprene or rubber base', 'Stitched edges', 'Mat tube', '9-pocket pages', '4- and 12-pocket pages', 'Side-loading pockets', 'Zip binder', 'Ring binder'],
  x=[X('Ultimate Guard Zipfolio', 'Zipped card portfolio in several capacities.', 'Ultimate Guard', '', CB, [('Zipfolio 160', 'Ultimate Guard', '', '8-pocket'), ('Zipfolio 360', 'Ultimate Guard', '', '18-pocket'), ('Zipfolio 480', 'Ultimate Guard', '', '24-pocket')]),
     X('Vault X Exo-Tec zip binder', 'Zipped binder with side-loading pockets.', 'Vault X', '', CB, [('9-Pocket', 'Vault X', '', '360 cards'), ('12-Pocket', 'Vault X', '', '480 cards')]),
     X('Dragon Shield Card Codex', 'Side-loading card portfolio.', 'Arcane Tinmen', '', CB, [('Card Codex 576', 'Arcane Tinmen', '', '24 per page')])])
KN = 'knowledge'
brands = [
 B('Wizards of the Coast', 'United States', '1990', 'Mainstream', 'Magic: The Gathering', 'US game publisher of Magic, owned by Hasbro since 1999.', MTG, sig=['Magic: The Gathering'], rel=['Hasbro']),
 B('Media Factory', 'Japan', '', 'Mainstream', 'Pokémon TCG (Japan)', 'Japanese publisher that first issued the Pokémon card game.', PBS, sig=['Pokémon Trading Card Game']),
 B('Konami', 'Japan', '1969', 'Mainstream', 'Yu-Gi-Oh! TCG', 'Japanese entertainment company that publishes Yu-Gi-Oh!', YGO, sig=['Yu-Gi-Oh! Trading Card Game']),
 B('Legend Story Studios', 'New Zealand', '', 'Specialist', 'Flesh and Blood', 'Independent Auckland studio behind Flesh and Blood.', FAB, sig=['Flesh and Blood']),
 B('Bandai', 'Japan', '1950', 'Mainstream', 'Gunpla, card games', 'Japanese toy company.', OP, sig=['One Piece Card Game']),
 B('Ravensburger', 'Germany', '1883', 'Mainstream', 'games, puzzles', 'German games and puzzle publisher.', KN, sig=['Disney Lorcana']),
 B('Games Workshop', 'United Kingdom', '1975', 'Mainstream', 'Warhammer', 'Nottingham maker of Warhammer miniatures games.', KN, sig=['Warhammer 40,000', 'Warhammer Age of Sigmar']),
 B('Warlord Games', 'United Kingdom', '', 'Specialist', 'historical wargames', 'British maker of Bolt Action and other wargames.', BA, sig=['Bolt Action']),
 B('Fantasy Flight Games', 'United States', '', 'Mainstream', 'licensed board and miniatures games', 'US games publisher.', XW, sig=['Star Wars: X-Wing']),
 B('Atomic Mass Games', 'United States', '', 'Specialist', 'Star Wars and Marvel miniatures', 'Miniatures games studio.', XW),
 B('Arcane Tinmen', 'Denmark', '', 'Specialist', 'Dragon Shield sleeves', 'Danish maker of Dragon Shield card accessories.', KN, lines=['Dragon Shield'], sig=['Dragon Shield sleeves', 'Dragon Shield Card Codex']),
 B('KMC', 'Japan', '', 'Specialist', 'card sleeves', 'Japanese card-sleeve maker (Kyowa Multi Color).', BC, sig=['KMC Hyper Matte']),
 B('Gamegenic', '', '', 'Specialist', 'sleeves, deck boxes', 'Card-game accessory brand.', BC, sig=['Gamegenic sleeves']),
 B('Ultimate Guard', '', '', 'Specialist', 'deck boxes, binders', 'Card-game accessory brand.', BC, sig=['Ultimate Guard Zipfolio']),
 B('Ultra PRO', 'United States', '', 'Mainstream', 'sleeves, binders', 'US maker of card protection and storage.', CB),
 B('Vault X', '', '', 'Specialist', 'binders', 'Card binder brand.', CB, sig=['Vault X Exo-Tec zip binder']),
]
notes = ("Game view only; grading and collecting stay in F3 (cross-link). Game systems are archetypes with product-type and first-release versions; no card-title lists. "
 "Old sleeve models became versions of Dragon Shield, KMC and Gamegenic archetypes; deck boxes kept as m. New kind Playmat & card binder. Maker name 'KMC (Kyowa Multi Color)' shortened to KMC and 'Ultra PRO International' to Ultra PRO. "
 "Not added: Marvel Crisis Protocol (no page retrieved), Yu-Gi-Oh! first set name, AoS Spearhead.")
write('04_02', [pk, sg, ss, ab, sl, db, pb], brands, [], notes)
