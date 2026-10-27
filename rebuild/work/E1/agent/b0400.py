import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
ST = WP + 'Staunton_chess_set'; JQ = WP + 'Jaques_of_London'; DU = WP + 'Dubrovnik_chess_set'; LW = WP + 'Lewis_chessmen'; GE = WP + 'Go_equipment'
TK = 'https://kogeijapan.com/locale/en_US/tendoshogikoma/'; XQ = WP + 'Xiangqi'; MJ = 'https://sloperama.com/mjfaq/types.html'; BG = WP + 'Backgammon'
DO = WP + 'Dominoes'; MC = WP + 'List_of_mancala_games'; RV = WP + 'Reversi'; CC = WP + 'Chess_clock'; MOG = 'https://www.mastersofgames.com/cat/chess-draughts/chess-clocks.htm'
chess = K('Chess set', 'A board and pieces for chess.', 'https://www.mastersofgames.com/cat/board/chess-sets.htm', a='chessmen',
  t=['Wood', 'Weighted plastic', 'Metal', 'Bone or ivory (antique)', 'King height', 'Board with set', 'Folding or travel set', 'Magnetic set', 'Electronic board'],
  x=[X('Lewis chessmen', 'Twelfth-century Norse chessmen carved mostly from walrus ivory, found on the Isle of Lewis.', '', '1150–1200', LW,
       [('Isle of Lewis chess set', '', '', 'museum-shop replica in wood or plastic (old data)')]),
     X('Staunton', 'The standard tournament pattern: turned pieces with a horse-head knight, registered by Nathaniel Cooke and sold by Jaques.', 'Jaques of London', '1849', ST,
       [('Jaques original', 'Jaques of London', '1849', 'on sale 29 September 1849; first 500 numbered and signed by Howard Staunton'), ('Staunton chess set', '', '', 'generic Staunton pattern (old data)'), ('Plastic Staunton', '', '', 'modern club and tournament sets')],
       a='Staunton pattern', dt='king height · wood (boxwood, ebony, rosewood) · weighting · knight carving'),
     X('Régence', 'French pattern named after the Café de la Régence in Paris.', '', '', ST),
     X('St George', 'English pre-Staunton pattern.', '', '', ST),
     X('Barleycorn', 'English pattern with barley-ear decoration.', '', '', ST),
     X('Dubrovnik', 'Abstract pattern without religious symbols, designed for the 1950 Dubrovnik Olympiad and praised by Fischer.', '', '1950', DU,
       [('Olympiad original', 'Subozan', '1950', 'by Pero Poček; about 50 sets'), ('Maurović redesign', '', '1960s', 'made in Zagreb'), ('Siegen set', '', '1970', 'for the 19th Olympiad, sleeker knight'),
        ('House of Staunton reproduction', 'House of Staunton', '2014', ''), ('Chess Bazaar reproduction', 'Chess Bazaar', '2015', '')])])
go = K('Go set', 'A board, black and white stones and bowls for go.', 'https://www.mastersofgames.com/cat/board/go.htm', a='goban · go stones · weiqi · baduk',
  t=['19×19 board', '13×13 board', '9×9 board', 'Table board', 'Floor board with legs', 'Folding board', 'Lens-shaped (Japanese/Korean) stones', 'Flat-bottomed (Chinese) stones', 'Glass stones', 'Plastic stones', 'Stone bowls'],
  x=[X('Kaya floor goban', 'Thick wooden floor board in kaya, the most valued board wood.', '', '', GE, [('Spruce, katsura or agathis board', '', '', 'cheaper traditional woods')], dt='wood · thickness · legs'),
     X('Slate-and-clamshell stones', 'Traditional Japanese and Korean stones: slate for black, clamshell for white.', '', '', GE, [('Size 32–33', '', '', 'common thicknesses'), ('Size 36', '', '', 'professional thickness')]),
     X('Yunzi stones', 'Chinese sintered stones first made in the Tang dynasty.', '', 'Tang dynasty', GE)])
shogi = K('Shogi set', 'A board and pieces for shogi.', 'https://www.mastersofgames.com/cat/board/shogi.htm', a='koma · shogi-ban',
  t=['Printed pieces', 'Wooden board', 'Folding board', 'Boxwood pieces'],
  x=[X('Tendo koma', 'Hand-made shogi pieces from Tendo, Yamagata, designated a Japanese traditional craft in 1996.', '', 'late Edo period', TK,
       [('Kaki-goma', '', '', 'characters brushed in lacquer'), ('Hori-goma', '', '', 'carved and lacquer-filled'), ('Hori-ume-goma', '', '', 'carved, filled level'), ('Moriage-goma', '', '', 'raised lacquer characters')],
       dt='wood (boxwood, magnolia, maple) · lettering style · calligrapher')])
xq = K('Xiangqi set', 'A board of nine by ten lines with a river, and 32 lettered disc pieces in red and black, for Chinese chess.', XQ, a='Chinese chess',
  t=['Paper or cloth board', 'Wooden board', 'Plastic pieces', 'Wooden pieces', 'Jade, horn or bone pieces', 'Engraved characters'])
mj = K('Mahjong set', 'A set of mahjong tiles with dice and markers.', 'https://www.mastersofgames.com/cat/table/mah-jong.htm', a='mahjong tile set · mah-jongg',
  t=['Melamine or plastic tiles', 'Bone and bamboo', 'Bakelite or catalin', 'Racks', 'Case'],
  x=[X('Modern Chinese set', '144 tiles with Chinese characters only.', '', '', MJ),
     X('Hong Kong set', '144 large, heavy tiles in four trays, with chips and dice.', '', '', MJ),
     X('Japanese riichi set', '144 small thick tiles with four red fives, no racks, with counting sticks.', '', '', MJ),
     X('American set', '152 tiles with eight jokers, Western indices and racks, for National Mah Jongg League play.', '', '', MJ,
       [('Mah-Lowe catalin set', '', '1950s–60s', 'yellow tiles, too few jokers for modern play')]),
     X('1920s bone-and-bamboo export set', 'Chinese export set of bone faces on bamboo backs, often with Western indices.', '', '1920s', MJ),
     X('Vietnamese set', 'Large tiles with special joker tiles.', '', '', MJ)],
  m=[['Dal Negro Grand Mah Jong set', 'Dal Negro']])
bg = K('Backgammon set', 'A board with checkers, dice and doubling cube for backgammon.', 'https://www.mastersofgames.com/cat/board/backgammon.htm', a='tables · tavla · nardy',
  t=['Folding case board', 'Inlaid wooden board', 'Leather board', 'Tournament size (44 × 55 cm and up)', 'Doubling cube', 'Precision dice', 'Dice cups'],
  x=[X('Damascus inlaid board', 'Wooden backgammon board with mother-of-pearl and wood inlay, a speciality of Damascus.', '', '', BG)])
dr = K('Draughts set', 'A board and discs for draughts (checkers).', 'https://www.mastersofgames.com/cat/board/draughts-checkers.htm', a='checkers', t=['8×8 board', '10×10 board', 'Wooden pieces', 'Plastic pieces'])
dm = K('Domino set', 'A set of domino tiles.', 'https://www.mastersofgames.com/cat/table/dominoes.htm', a='dominoes',
  t=['Double-six (28 tiles)', 'Double-nine (55 tiles)', 'Double-12 (91 tiles)', 'Double-15 (136 tiles)', 'Double-18 (190 tiles)', 'Bone or hardwood', 'Plastic', 'Coloured pips', 'Box'],
  m=[['Mexican Train dominoes', '']])
mc = K('Mancala board', 'A board of pits with seeds or stones for sowing games such as oware and bao.', MC, a='count-and-capture board · sowing board',
  t=['2 × 6 pits', '2 × 7 pits', '4 × 8 pits', 'Folding board', 'Stores at the ends'],
  x=[X('Oware board', 'Two rows of six pits; the national game of Ghana.', '', '', MC),
     X('Bao board', 'Four rows of eight pits, played in Kenya and Tanzania.', '', '', MC),
     X('Congkak board', 'Two rows of seven pits with stores, from Indonesia and Malaysia.', '', '', MC)])
rv = K('Reversi set', 'A board and two-sided discs for reversi; Othello is a branded version.', 'https://www.mastersofgames.com/cat/board/othello-reversi.htm', a='Othello',
  t=['8×8 board', '64 two-sided discs', 'Wooden', 'Plastic'],
  x=[X('Reversi', 'Victorian game on an uncheckered 8×8 board with two-sided discs.', '', '1883', RV, [('Ravensburger edition', 'Ravensburger', '1893', '')]),
     X('Othello', 'Reversi with a fixed starting position, patented by Goro Hasegawa.', 'Tsukuda Original', '1973', RV,
       [('Hasegawa patent', '', '1971', ''), ('Tsukuda Original launch', 'Tsukuda Original', '1973', 'Japan'), ('MegaHouse', 'MegaHouse', '', 'owns rights outside Japan'), ('Othello', '', '', 'old data')])],
  m=[['Rombol wooden Reversi game', 'Rombol']])
gc = K('Game clock', 'A two-sided clock, mechanical or digital, timing each player\'s moves in chess, go or other board games.', 'https://www.chesshouse.com/collections/chess-clocks/style-best-seller',
  a='chess clock · game timer', t=['Mechanical (analogue)', 'Digital', 'Increment (Fischer)', 'Delay', 'Byo-yomi', 'Hourglass'],
  x=[X('Mechanical chess clock', 'Two linked clock faces with falling flags, stopped and started by push buttons.', '', '1883', CC,
       [('Thomas Bright Wilson clock', '', '1883', 'first used at London 1883'), ('GARDE Classic', 'Garde', '', 'cedar case, German movement')]),
     X('Digital chess clock', 'Electronic clock with sudden-death, increment and delay modes.', '', '1975', CC,
       [('First commercial model', '', '1975', 'Meshi and Ponsor patent'), ('DGT 2010', 'DGT', '', 'official FIDE clock'), ('GARDE Start', 'Garde', '', 'one AA battery')]),
     X('Fischer clock', 'Adds a fixed time after each move; patented by Bobby Fischer.', '', '1988', CC, [('Fischer–Spassky match', '', '1992', 'first use')]),
     X('Byo-yomi timer', 'Clock giving overtime periods for go and shogi.', 'DGT', '', MOG, [('DGT 1005', 'DGT', '', '')])],
  m=[['DGT 1001', 'DGT'], ['DGT 1002', 'DGT'], ['DGT North American', 'DGT'], ['ZMF-II', 'ZMF'], ['Master Quartz Chess Clock', '']])
KN = 'knowledge'
brands = [
 B('Jaques of London', 'United Kingdom', '1795', 'Heritage manufactory', 'Staunton chess', 'Family games maker founded by Thomas Jaques; first sold the Staunton chessmen.', JQ, sig=['Staunton'], sc=['chess', 'croquet']),
 B('DGT', 'Netherlands', '', 'Professional & flagship', 'chess clocks', 'Dutch maker of digital chess clocks and electronic boards, including the FIDE clock.', KN, sig=['Digital chess clock', 'Byo-yomi timer']),
 B('Garde', 'Germany', '', 'Heritage manufactory', 'mechanical chess clocks', 'German chess-clock brand with mechanical and digital clocks.', MOG),
 B('Dal Negro', 'Italy', '', 'Heritage manufactory', 'playing cards, games', 'Italian maker of playing cards and game sets.', KN),
 B('Tsukuda Original', 'Japan', '', 'Mainstream', 'Othello', 'Japanese toy company that launched Othello in 1973.', RV, sig=['Othello'], rel=['MegaHouse']),
 B('MegaHouse', 'Japan', '', 'Mainstream', 'Othello', 'Japanese toy company holding Othello rights outside Japan.', RV, rel=['Tsukuda Original']),
 B('Ravensburger', 'Germany', '1883', 'Mainstream', 'games, puzzles', 'German games and puzzle publisher.', KN),
]
G = 'Games & play'
trads = [
 {'n': 'Staunton chessmen making', 'g': G, 'r': 'England (London)', 'p': '1849–present', 'd': 'Turning and carving of Staunton-pattern chessmen in boxwood and ebony, begun by Jaques of London.', 'tech': 'lathe turning, hand-carved knights, weighting', 'mat': 'boxwood, ebony, ivory (antique)',
  'forms': ['Staunton'], 'ctr': ['Jaques of London'], 'auth': 'Jaques stamp and box label; early sets numbered and signed by Staunton', 's': ST},
 {'n': 'Norse walrus-ivory chessmen', 'g': G, 'r': 'Norway (Trondheim), Scandinavia', 'p': '12th century', 'd': 'Medieval figurative chessmen carved in walrus ivory and whale tooth, best known from the Lewis hoard.', 'tech': 'figurative ivory carving', 'mat': 'walrus ivory, whale tooth',
  'forms': ['Lewis chessmen'], 'ctr': ['Trondheim'], 'auth': 'originals are in the British Museum and National Museum of Scotland; most sets are replicas', 's': LW},
 {'n': 'Go equipment making', 'g': G, 'r': 'Japan, Korea, China', 'p': 'Tang dynasty onward', 'd': 'Making of solid-wood go boards, slate-and-shell or yunzi stones and turned bowls.', 'tech': 'board sawing and line-marking, stone grinding, bowl turning', 'mat': 'kaya, katsura, slate, clamshell, yunzi, mulberry',
  'forms': ['Kaya floor goban', 'Slate-and-clamshell stones', 'Yunzi stones'], 'auth': 'board wood species and grain; true slate and shell rather than glass', 's': GE},
 {'n': 'Tendo shogi koma', 'g': G, 'r': 'Tendo and Murayama, Yamagata, Japan', 'p': 'late Edo period–present', 'd': 'Hand-made shogi pieces, designated a Japanese traditional craft on 8 April 1996.', 'tech': 'brushed, carved and raised lacquer characters', 'mat': 'boxwood, magnolia, maple, spindle tree, urushi lacquer',
  'forms': ['Tendo koma'], 'ctr': ['Tendo'], 'auth': 'boxwood from Mikurajima or Satsuma for top pieces; style (kaki, hori, hori-ume, moriage)', 's': TK},
 {'n': 'Xiangqi set making', 'g': G, 'r': 'China', 'p': 'Southern Song dynasty onward', 'd': 'Engraved disc pieces and lined boards for Chinese chess.', 'tech': 'engraving and inking characters on discs', 'mat': 'wood, horn, bone, ivory, jade, plastic',
  'forms': ['Xiangqi set'], 'auth': 'material of pieces; carved rather than printed characters', 's': XQ},
 {'n': 'Mahjong tile making', 'g': G, 'r': 'China, Hong Kong, Japan, United States', 'p': '1920s–present', 'd': 'Carved and painted mahjong tiles, from 1920s bone-and-bamboo export sets to modern regional sets.', 'tech': 'carving and painting tile faces; dovetailing bone to bamboo', 'mat': 'bone, bamboo, catalin, melamine',
  'forms': ['1920s bone-and-bamboo export set', 'American set', 'Japanese riichi set', 'Hong Kong set'], 'auth': 'tile count, joker and flower tiles, bone-and-bamboo dovetail', 's': MJ},
 {'n': 'Damascus inlaid game boards', 'g': G, 'r': 'Damascus, Syria', 'p': '', 'd': 'Inlaid wooden boards for backgammon and other tables games.', 'tech': 'marquetry and mother-of-pearl inlay', 'mat': 'wood, mother-of-pearl',
  'forms': ['Damascus inlaid board'], 'ctr': ['Damascus'], 's': BG},
]
notes = ("Chess clock and Game clock merged (old models kept in m; Garde and DGT as versions). Chess archetypes: Lewis, Staunton, Régence, St George, Barleycorn, Dubrovnik; Soviet, Selenus and Isle-of-Lewis makers not added (no detailed page). "
 "Go archetypes from the Go equipment article (Hyuga stones not on a fetched page). Mahjong archetypes follow the Sloperama set-type FAQ. New kinds Xiangqi set and Mancala board sourced from Wikipedia. BHB clock dropped (retailer page 404). "
 "Brands DGT, Dal Negro, Ravensburger from knowledge (no founding years where unsure). Seven traditions added.")
write('04_00', [chess, go, shogi, xq, mj, bg, dr, dm, mc, rv, gc], brands, trads, notes)
