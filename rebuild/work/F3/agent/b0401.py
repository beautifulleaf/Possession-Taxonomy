import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
WD = "https://www.wikidata.org/wiki/"
WOTC, MF, KON, BAN, TOP, PAN, MER, IMP = "Wizards of the Coast", "Media Factory", "Konami", "Bandai", "Topps", "Panini", "Merlin", "Impel"
WIL, PLY, OGD, LIE, BB = "W.D. & H.O. Wills", "John Player & Sons", "Ogden's", "Liebig's Extract of Meat Company", "Brooke Bond"
DT = "set · card number · rarity · edition · language · grade (PSA, BGS, CGC)"
tcg = K("Trading-card game single", "Individual card of a collectible card game, collected by set, rarity, edition, language and grade.", WP + "Base_Set_(Pok%C3%A9mon)",
  a="TCG single · CCG card",
  t=["1st edition", "unlimited", "shadowless", "holofoil", "foil", "alternate art", "serialized", "promo", "prize card", "language edition", "sealed booster"],
  x=[X("Pokémon Base Set", "The first Pokémon card set, 102 cards with 16 holofoils.", WP + "Base_Set_(Pok%C3%A9mon)", mk=MF, y="1996",
       v=[("Japanese Base Set", MF, "1996", ""), ("English 1st Edition", WOTC, "1999", "'Edition 1' stamp"), ("Shadowless", WOTC, "1999", "no drop shadow on frame"),
          ("Unlimited", WOTC, "1999", ""), ("Charizard holo", "", "", "art by Mitsuhiro Arita; the key card"), ("Pre-release Raichu", "", "", "error rarity"),
          ("Base Set 2", WOTC, "2000", "130 cards, no 1st Edition")], dt=DT),
     X("Magic: The Gathering Power Nine", "The nine most powerful early Magic cards, printed only in the first sets and on the Reserved List.", WP + "Power_Nine", mk=WOTC, y="1993",
       v=[("Black Lotus", WOTC, "1993", "Alpha CGC 10 sold 2024 for $3M"), ("Ancestral Recall", WOTC, "1993", ""), ("Time Walk", WOTC, "1993", ""), ("Timetwister", WOTC, "1993", ""),
          ("The five Moxen", WOTC, "1993", "Pearl, Sapphire, Jet, Ruby, Emerald"), ("Alpha, Beta and Unlimited printings", WOTC, "1993", "removed from Revised")], dt=DT),
     X("Magic: The Gathering collector versions", "Premium Magic printings sought by collectors.", WP + "Magic:_The_Gathering", mk=WOTC,
       v=[("Foil cards", WOTC, "", ""), ("Secret Lair", WOTC, "2020", "crossover and guest art"), ("Serialized cards", WOTC, "2021", "widely available from The Brothers' War, 2022")]),
     X("Blue-Eyes White Dragon", "Seto Kaiba's signature monster, the iconic Yu-Gi-Oh! card.", WD + "Q12185120", mk=KON),
     X("Yu-Gi-Oh! early English sets", "First English Yu-Gi-Oh! printings distributed by Upper Deck.", WP + "Yu-Gi-Oh!_Trading_Card_Game", mk=KON, y="2002",
       v=[("Upper Deck distribution", "Upper Deck", "2002–2008", "nine-card packs")]),
     X("One Piece Card Game", "Bandai's One Piece card game, a fast-growing collector market.", WP + "One_Piece_Card_Game", mk=BAN, y="2022",
       v=[("Japanese release", BAN, "2022", "8 July"), ("Global release", BAN, "2022", "2 December"), ("Kaido ST04-003 Championship 2023 Winner", BAN, "2023", "prize card")])])
nsp = K("Non-sports trading card", "Trading card of an entertainment, comic, humour or general subject, sold in packs and collected in numbered sets.", WP + "Garbage_Pail_Kids",
  a="entertainment card · non-sport card", t=["base card", "sticker card", "hologram", "foil chase card", "error card", "wax pack"],
  x=[X("Mars Attacks", "Topps's 55-card alien-invasion set, withdrawn after complaints.", WP + "Mars_Attacks", mk=TOP, y="1962",
       v=[("Original set", TOP, "1962", "test-marketed by Bubbles, Inc.; art by Wally Wood and Norman Saunders"), ("Mars Attacks Archives", TOP, "1994", "55 originals plus 45 new")]),
     X("Star Wars (Topps)", "Topps's Star Wars cards, issued since the first film.", WP + "Star_Wars_trading_card", mk=TOP, y="1977",
       v=[("1977 Series 1–5", TOP, "1977", "blue, red, yellow, green, orange borders; 66 cards and 11 stickers each"), ("C-3PO error card", TOP, "1977", ""),
          ("The Empire Strikes Back", TOP, "1980", ""), ("Return of the Jedi", TOP, "1983", ""), ("Star Wars Galaxy", TOP, "1993–2012", ""),
          ("Chrome Archives", TOP, "1999", ""), ("Masterwork", TOP, "2015–2019", "")]),
     X("Garbage Pail Kids", "Topps's gross-out sticker cards parodying Cabbage Patch Kids.", WP + "Garbage_Pail_Kids", mk=TOP, y="1985",
       v=[("Original Series", TOP, "1985", "a and b name variants; art by John Pound"), ("All-New Series", TOP, "2003", ""), ("Chrome", TOP, "2013–14", ""),
          ("30th Anniversary", TOP, "2015", "")]),
     X("Marvel Universe", "Impel's Marvel character cards with stats and holograms.", WP + "Marvel_Universe_Cards", mk=IMP, y="1990",
       v=[("Series I", IMP, "1990", "162 cards and 5 holograms"), ("Series II", IMP, "1991", ""), ("Series III", IMP, "1992", "200 cards"),
          ("Series IV", IMP, "1993", "Marvel 2099 foils"), ("Series V", IMP, "1994", "")]),
     X("Wacky Packages", "Topps parodies of consumer products.", WD + "Q7958819", mk=TOP)])
cig = K("Cigarette and trade card", "Picture card given with tobacco, tea, meat extract or other goods, collected in sets (cartophily).", WP + "Cigarette_card",
  a="cigarette card · tea card · trade card · cartophily", t=["cigarette card", "silk", "tea card", "trade card (chromo)", "album", "complete set", "reprint"],
  x=[X("Wills's cigarette cards", "Sets of Bristol's W.D. & H.O. Wills, the first British card issuer.", WP + "W.D._%26_H.O._Wills", mk=WIL, y="1887",
       v=[("Ships and Sailors", WIL, "1895", "first general-interest set"), ("Cricketers", WIL, "1901", ""), ("Aviation", WIL, "1910", ""), ("Famous Golfers", WIL, "1930", ""),
          ("Air Raid Precautions", WIL, "1938", "")]),
     X("Player's cigarette cards", "Over 200 sets from the Nottingham maker.", WP + "John_Player_%26_Sons", mk=PLY, y="1893",
       v=[("Castles and Abbeys", PLY, "1893", "one of the first"), ("Footballers", PLY, "1926", ""), ("Cricketers", PLY, "1934", "with Don Bradman"),
          ("Motor Cars", PLY, "1936", ""), ("Coronation Series", PLY, "1937", "")]),
     X("Ogden's cigarette cards", "Ogden's sets, including one of the first full-colour sets.", WP + "Cigarette_card", mk=OGD, v=[("Football club colours", OGD, "1906", "")]),
     X("Liebig chromos", "Small themed sets of chromolithographed cards given with Liebig meat extract.", WP + "Liebig%27s_Extract_of_Meat_Company", mk=LIE, y="1872",
       dt="set of about six cards · language edition"),
     X("Brooke Bond tea cards", "Picture cards in Brooke Bond tea packets, many with albums.", WP + "Brooke_Bond", mk=BB, y="1954–1999",
       v=[("British Wild Flowers", BB, "", ""), ("African Wild Life", BB, "", ""), ("Tropical Birds", BB, "", ""), ("History of the Motor Car", BB, "", ""),
          ("Chimps series", BB, "", "last sets")]),
     X("Allen & Ginter tobacco cards", "Among the first cigarette cards, in the US.", WP + "Cigarette_card", mk="Allen & Ginter", y="1879")])
stk = K("Collectible sticker", "Sticker from a numbered series, like Panini's, made to be collected into an album.", "https://madkicks.com/products/2026-panini-fifa-world-cup-soccer-sticker-collection-album",
  t=["sticker", "foil or shiny", "album", "complete set", "update set"],
  x=[X("Panini FIFA World Cup", "Panini's World Cup sticker album, issued for every tournament since 1970.", WP + "Sticker_album", mk=PAN, y="1970",
       v=[("Mexico 70", PAN, "1970", "270 stickers"), ("1974 and 1978", PAN, "", "400 stickers"), ("1982 and 1986", PAN, "", "427"), ("2018", PAN, "2018", "681"),
          ("2026", PAN, "2026", "980")]),
     X("Merlin Premier League", "Official Premier League sticker album, from Merlin's Premier League 94.", WP + "Merlin_Publishing", mk=MER, y="1994",
       v=[("Merlin's Premier League 94", MER, "1994", ""), ("Topps Premier League", TOP, "2008", "renamed"), ("Merlin revival", MER, "2014", "")])],
  m=[["Panini FIFA World Cup Sticker Collection", PAN]])
S = "Specialist"
brands = [
 B(WOTC, "United States", "1990", "Magic: The Gathering", "US game publisher of Magic and the first English Pokémon cards.", WD + "Q1135204", seg=S),
 B(MF, "Japan", "1986", "Pokémon cards", "Japanese publisher of the original Pokémon card game.", WD + "Q520454", seg=S),
 B(KON, "Japan", "1969", "Yu-Gi-Oh!", "Japanese entertainment company, publisher of the Yu-Gi-Oh! card game.", WD + "Q45700", seg="Mainstream"),
 B(BAN, "Japan", "1950", "One Piece Card Game", "Japanese toy and game maker.", WD + "Q507269", seg="Mainstream"),
 B(IMP, "United States", "", "Marvel Universe", "US card publisher, part of SkyBox International.", WP + "Marvel_Universe_Cards", seg=S),
 B(MER, "United Kingdom", "1989", "Premier League stickers", "Milton Keynes sticker publisher, owned by Topps from 1995.", WP + "Merlin_Publishing", seg=S),
 B(WIL, "United Kingdom", "1786", "cigarette cards", "Bristol tobacco firm, a branch of Imperial Tobacco from 1901.", WP + "W.D._%26_H.O._Wills", seg="Heritage manufactory"),
 B(PLY, "United Kingdom", "1877", "cigarette cards", "Nottingham tobacco firm, a branch of Imperial Tobacco from 1901.", WP + "John_Player_%26_Sons", seg="Heritage manufactory"),
 B(OGD, "United Kingdom", "", "cigarette cards", "Liverpool tobacco firm known for early colour card sets.", "knowledge", seg="Heritage manufactory"),
 B(LIE, "United Kingdom", "1865", "Liebig chromos", "Meat-extract maker whose collectable cards began in 1872.", WP + "Liebig%27s_Extract_of_Meat_Company", seg="Heritage manufactory"),
 B(BB, "United Kingdom", "1869", "tea cards", "British tea brand that packed picture cards from 1954 to 1999.", WP + "Brooke_Bond", seg="Mainstream"),
 B("Allen & Ginter", "United States", "", "tobacco cards", "Richmond tobacco firm, an early cigarette-card issuer.", WP + "Cigarette_card", seg="Heritage manufactory"),
]
save("04_01", [tcg, nsp, cig, stk], brands, [],
 "Collector/grading view only; no game rules or deck lists. Legend of Blue Eyes White Dragon (LOB) set and Pokémon card numbers not stated on any retrieved page, so not recorded. "
 "Typhoo and other tea cards, Carreras and Gallaher not added (no retrieved page detail). Brands Topps and Panini are registered in shelf 04_00; Upper Deck in 04_00.")
