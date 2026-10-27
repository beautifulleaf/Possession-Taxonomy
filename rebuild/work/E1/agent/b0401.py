import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
FR = WP + 'French-suited_playing_cards'; GE = WP + 'German-suited_playing_cards'; IT = WP + 'Italian_playing_cards'; BI = WP + 'Bicycle_Playing_Cards'
FO = 'https://www.wopc.co.uk/spain/fournier/index'; TA = 'https://www.wopc.co.uk/austria/tarok/'; HA = WP + 'Hanafuda'; PI = WP + 'Piatnik'; DI = 'https://www.mrob.com/pub/math/dice.html'
ED = ['Standard edition', 'First edition', 'Deluxe or collector\'s edition', 'Kickstarter all-in or pledge edition', 'Expansion', 'Promo pieces', 'Complete', 'Incomplete or missing pieces', 'Sealed']
bg = K('Board game', 'A published game on a board or in a box with its own pieces; includes a spirit board made as a board game.', 'https://mastersofgames.com/cat/board/zaroc.htm',
  a='boxed board game · tabletop game', t=ED + ['Family game', 'Strategy (hobby) game', 'Party game', 'Travel edition', 'Spirit board'])
cg = K('Card game', 'A published card game with its own special cards.', 'https://mastersofgames.com/cat/board/zaroc.htm', a='proprietary card game', t=ED + ['Deck-building game', 'Party card game'])
pc = K('Playing cards', 'A deck of regional-pattern playing cards (French-, German-, Spanish- or Italian-suited, tarock and French-tarot packs) sold for card play; size does not make a different kind.',
  'https://www.mastersofgames.com/cat/indoor/casino.htm', a='standard playing-card deck · pack of cards',
  t=['52-card (with jokers)', '32-card piquet', '36-card', '40-card', '48-card', '54-card tarock', 'Poker size', 'Bridge size', 'Patience size', 'Jumbo index', 'Plastic', 'Linen or air-cushion finish', 'Double-ended courts', 'Corner indices'],
  x=[X('English (Anglo-American) pattern', 'The international French-suited pattern, from Rouen cards reworked in England; the standard 52-card deck.', '', '19th century', FR,
       [('Goodall reworking', 'Charles Goodall and Son', '19th century', 'redrew the Rouen-derived courts')]),
     X('Bicycle Rider Back', 'Back design No. 63 of Bicycle cards, the most popular back design.', 'United States Playing Card Company', '1887', BI,
       [('Old Fan', 'United States Playing Card Company', '1885–1894', 'first Bicycle back'), ('Wheel No. 1', 'United States Playing Card Company', '1887–1907', '')], dt='back colour (red, blue) · finish · index'),
     X('Paris pattern', 'French national pattern.', '', '', FR),
     X('Belgian-Genoese pattern', 'Belgian national pattern, also used in the Balkans, North Africa and the Middle East.', '', '', FR),
     X('Russian pattern', 'French-suited pattern of the former Russian Empire, finalised by Adolf Charlemagne.', '', '', FR),
     X('Vienna pattern', 'French-suited pattern of Austria and Bohemia, current version made by Piatnik.', 'Piatnik', '1885', FR,
       [('Vienna pattern (ex-Lyon)', '', '', 'old data'), ('Neumayer Type A design', '', '1885', 'basis of the current version')]),
     X('Nordic pattern', 'Danish-born pattern now printed for Finland by Piatnik.', 'Dondorf', '1895', FR, [('Dondorf original', 'Dondorf', '1895', 'for Adolph Wulff')]),
     X('Bavarian pattern', 'German-suited 36-card pattern of Bavaria.', 'F.X. Schmid', '', GE),
     X('Saxon pattern', 'German-suited 32-card pattern of Saxony and Thuringia.', 'ASS Altenburger', '', GE),
     X('Salzburg pattern', 'Single-headed German-suited Austrian pattern.', '', '', GE, [('Salzburger pattern', '', '', 'old data')]),
     X('Tell pattern', 'Double-German Hungarian pattern with William Tell scenes, made by Piatnik since 1865.', 'Piatnik', '1865', GE, [('József Schneider original', '', '', 'Pest')]),
     X('Triestine pattern', 'Italian-suited pattern of Trieste.', '', '', IT, [('Triestine pattern', '', '', 'old data')]),
     X('Napoletane pattern', 'Spanish-suited Italian pattern of Naples.', '', '', IT),
     X('Castilian pattern', 'Spanish-suited standard pattern drawn for Heraclio Fournier.', 'Heraclio Fournier', '1877', FO,
       [('Soubrier design', 'Heraclio Fournier', '1877', 'by Emilio Soubrier'), ('Rius revision', 'Heraclio Fournier', 'about 1887', 'by Augusto Rius'), ('Naipe Nacional', 'Heraclio Fournier', '1938', '')]),
     X('Industrie und Glück tarock', 'Austrian tarock with rural scenes on the trumps and an eagle on Trump II.', 'Piatnik', 'c.1905–1910', TA,
       [('Stencil-coloured Piatnik deck', 'Piatnik', 'c.1910', ''), ('Chromolithographed Piatnik deck', 'Piatnik', '1936', ''), ('Adametz edition', 'Franz Adametz', '1948', ''), ('Industrie und Glueck Tarock', '', '', 'old data')]),
     X('Tarocco Piemontese', 'Italian tarot pack for tarocchi games.', 'Dal Negro', '', IT)],
  m=[['El Jokey', 'Piatnik'], ['Vienna Melange', 'Piatnik']])
hf = K('Hanafuda deck', 'A 48-card Japanese or Korean flower-card deck.', 'https://nintendo.com/us/store/products/hanafuda-cards-mario-red-119579', a='flower-card deck · hanafuda · hwatu',
  t=['Paper (Japanese)', 'Plastic (Korean hwatu)', 'Themed edition'],
  x=[X('Nintendo hanafuda', 'Hanafuda from the company founded to make them by hand.', 'Nintendo', '1889', HA),
     X('Oishi Tengudo hanafuda', 'Hanafuda from the long-standing maker founded in 1800.', 'Oishi Tengudo', '1800', HA),
     X('Hwatu', 'Korean plastic flower cards with November and December suits swapped.', '', '', HA)])
tg = K('Tile game', 'A published game played with its own tiles.', 'https://mastersofgames.com/cat/board/zaroc.htm', a='proprietary tile game', t=ED + ['Letter tiles', 'Number tiles', 'Tile racks'])
dg = K('Dice game', 'A published game played mainly with its own dice.', 'https://www.walmart.com/browse/games-puzzles/dice-games/4171_4191_3010025', a='proprietary dice game', t=ED + ['Shut-the-box tray', 'Dice cup', 'Score pad'])
ds = K('Dice set', 'A set of polyhedral, casino or poker dice sold as a set.', 'https://www.mastersofgames.com/cat/indoor/dice-games.htm', a='polyhedral dice · RPG dice',
  t=['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'Percentile d10 (00–90)', 'Precision casino dice', 'Poker dice', 'Resin', 'Metal', 'Gemstone', 'Dice bag or tray'],
  x=[X('Polyhedral RPG dice set', 'The role-playing set of d4, d6, d8, d10, d12, d20 and percentile die.', '', '1970s', DI,
       [('Original D&D set', '', '', 'd4, d6, d8, d12 and d20 numbered 0–9 twice'), ('Seven-dice set', '', '', 'adds d10 and percentile d10'), ('Zocchihedron d100', '', '', 'single hundred-sided die')])],
  m=[['Poker dice set', '']])
rp = K('Replacement game pieces', 'Spare or add-on pieces made for a game, including game money sold for one game.', 'https://www.mastersofgames.com/cat/table/crokinole.htm', a='game accessories · spare parts',
  t=['Pawns and tokens', 'Game money', 'Spare cards', 'Spare dice', 'Board or insert', 'Upgrade components'])
KN = 'knowledge'
brands = [
 B('Piatnik', 'Austria', '1824', 'Heritage manufactory', 'playing cards, tarock', 'Viennese maker of playing cards, games and puzzles.', PI, lines=['Tarock', 'Bridge', 'Schnapsen'], sig=['Vienna pattern', 'Tell pattern', 'Industrie und Glück tarock']),
 B('United States Playing Card Company', 'United States', '1894', 'Mainstream', 'Bicycle cards', 'Erlanger, Kentucky maker of Bicycle playing cards.', BI, lines=['Bicycle'], sig=['Bicycle Rider Back']),
 B('Heraclio Fournier', 'Spain', '1868', 'Heritage manufactory', 'Spanish-suited cards', 'Vitoria playing-card maker, now part of Cartamundi.', FO, sig=['Castilian pattern'], rel=['Cartamundi']),
 B('Cartamundi', 'Belgium', '1970', 'Mainstream', 'playing cards', 'Belgian playing-card maker that owns Fournier.', KN, rel=['Heraclio Fournier']),
 B('Modiano', 'Italy', '1868', 'Heritage manufactory', 'Italian and poker cards', 'Trieste playing-card maker.', KN),
 B('Dal Negro', 'Italy', '', 'Heritage manufactory', 'playing cards, games', 'Italian maker of regional playing cards and tarocchi.', IT, sig=['Tarocco Piemontese']),
 B('ASS Altenburger', 'Germany', '', 'Mainstream', 'German-suited cards', 'Altenburg playing-card maker.', GE, sig=['Saxon pattern']),
 B('F.X. Schmid', 'Germany', '', 'Heritage manufactory', 'Bavarian cards', 'Bavarian playing-card maker.', GE, sig=['Bavarian pattern']),
 B('Nintendo', 'Japan', '1889', 'Mainstream', 'hanafuda, video games', 'Japanese company founded by Fusajiro Yamauchi to make hand-crafted hanafuda.', HA, sig=['Nintendo hanafuda']),
 B('Oishi Tengudo', 'Japan', '1800', 'Heritage manufactory', 'hanafuda', 'Long-standing Japanese card maker.', HA, sig=['Oishi Tengudo hanafuda']),
 B('Hasbro', 'United States', '1923', 'Mainstream', 'board games', 'US toy and board-game publisher.', KN),
 B('Kosmos', 'Germany', '1822', 'Mainstream', 'board games', 'Stuttgart publisher of games and science kits (Franckh-Kosmos).', KN),
 B('Ravensburger', 'Germany', '1883', 'Mainstream', 'games, puzzles', 'German games and puzzle publisher.', KN),
 B('Asmodee', 'France', '1995', 'Mainstream', 'hobby board games', 'French board-game publisher and distributor.', KN),
 B('Z-Man Games', 'United States', '1999', 'Specialist', 'hobby board games', 'Hobby board-game publisher.', KN),
]
G = 'Games & play'
trads = [
 {'n': 'Hanafuda making', 'g': G, 'r': 'Japan', 'p': '1816 onward (hana awase); 1889 Nintendo', 'd': 'Small, thick, stiff 48-card flower decks in twelve month suits.', 'tech': 'printing on stiff layered card', 'mat': 'paper card; plastic in Korea',
  'forms': ['Nintendo hanafuda', 'Oishi Tengudo hanafuda'], 'ctr': ['Nintendo', 'Oishi Tengudo'], 's': HA},
 {'n': 'Austrian tarock card making', 'g': G, 'r': 'Vienna, Austria', 'p': '19th century–present', 'd': 'Vienna-made French-suited tarock packs with genre-scene trumps, led by the Industrie und Glück pattern.', 'tech': 'stencil colouring, later chromolithography', 'mat': 'card',
  'forms': ['Industrie und Glück tarock'], 'ctr': ['Piatnik', 'Franz Adametz'], 'auth': 'maker address and tax stamp on the Ace of Hearts date a pack', 's': TA},
]
notes = ("Titles are out of scope: all title model lists dropped (board game 39, card game 1, tile game 3, dice game 6; including makers Alea, Frosted Games, Game Factory, Kosmos, Loki, Pegasus, Schmidt, Unexpected Games, Gamewright, PlayMonster, The Op). "
 "Board, card, tile and dice games now carry edition-type and completeness types; publishers (Hasbro, Kosmos, Ravensburger, Asmodee, Z-Man) in the brand register from knowledge. "
 "Playing cards by regional pattern as archetypes (French-, German-, Italian-, Spanish-suited, tarock) with old patterns as versions. Not added: Swiss pattern, Spanish National pattern name, casino precision dice archetype (no fetched page). Bicycle registered under its maker USPCC.")
write('04_01', [bg, cg, pc, hf, tg, dg, ds, rp], brands, trads, notes)
