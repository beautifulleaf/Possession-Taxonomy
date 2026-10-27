import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
TOP, PAN, UD, FL, BOW, DON, GOU, ATC = "Topps", "Panini", "Upper Deck", "Fleer", "Bowman", "Donruss", "Goudey", "American Tobacco Company"
BC = WP + "Baseball_card"; EXP = WP + "List_of_most_expensive_sports_cards"; REF = WP + "Refractor_card"
OLD = "https://cardsmithsbreaks.com/full-checklist/2026-topps-chrome-baseball"
DT = "card number · parallel · serial number · grade (PSA, BGS, SGC) · centring"
base = K("Base card", "Standard card of a numbered sports set issued by a card maker.", OLD, a="flagship card · common",
  t=["base", "short print", "variation", "error card", "team card", "checklist"],
  x=[X("1933 Goudey", "Goudey's 240-card 'Big League Chewing Gum' set, the first baseball gum cards.", WP + "Goudey", mk=GOU, y="1933",
       v=[("Babe Ruth #53", GOU, "1933", ""), ("Babe Ruth #149", GOU, "1933", ""), ("Napoleon Lajoie #106", GOU, "1934", "mailed to collectors; not in packs")], dt=DT),
     X("1952 Topps", "Topps's 407-card set, often called the first modern set: colour photos, stats and bios.", WP + "Topps", mk=TOP, y="1952",
       v=[("Mickey Mantle", TOP, "1952", "high-number series; SGC 9.5 sold 2022 for $12.6M")], dt=DT),
     X("Topps flagship", "Topps's annual main baseball set.", WP + "Topps_baseball_card_products", mk=TOP, y="1951",
       v=[("1951 Red Backs and Blue Backs", TOP, "1951", "first Topps baseball"), ("Tiffany sets", TOP, "1984–1991", "limited hobby versions"), ("Factory sets", TOP, "1974", "")]),
     X("1986–87 Fleer basketball", "Fleer's 132-card NBA set with Michael Jordan's rookie card.", WP + "Fleer", mk=FL, y="1986",
       v=[("Michael Jordan", FL, "1986", "rookie card"), ("Michael Jordan All-Star sticker", FL, "1986", "second Jordan rookie")], dt=DT),
     X("1989 Upper Deck", "Upper Deck's first set: glossy stock and an anti-counterfeit hologram.", WP + "Upper_Deck_Company", mk=UD, y="1989",
       v=[("Ken Griffey Jr. #1", UD, "1989", "most-graded card at PSA")]),
     X("Topps Chrome", "Topps chromium-finish set with refractor parallels.", EXP, mk=TOP,
       v=[("Kobe Bryant refractor rookie", TOP, "1996–97", ""), ("Update series", TOP, "", "")]),
     X("Bowman", "Bowman sets, the 1948–52 market leader, revived by Topps for prospects.", WP + "Bowman_(brand)", mk=BOW, y="1948",
       v=[("1948 Bowman", BOW, "1948", ""), ("1951 Bowman Mickey Mantle #253", BOW, "1951", "Mantle rookie"), ("Revived Bowman", TOP, "1989", ""),
          ("Bowman's Best", TOP, "1994", "first Bowman refractors"), ("Bowman Chrome", TOP, "1997", "prospect autographs from 2001"), ("Bowman Draft", TOP, "", "")]),
     X("Topps Finest", "Super-premium Topps set that introduced the refractor.", WP + "Topps_baseball_card_products", mk=TOP, y="1993"),
     X("Stadium Club", "Premium Topps set.", WP + "Topps_baseball_card_products", mk=TOP, y="1991"),
     X("Topps Heritage", "Topps set in the designs of past decades.", WP + "Topps_baseball_card_products", mk=TOP, y="2001"),
     X("Allen & Ginter", "Topps's revival of the 19th-century tobacco brand, mixing sports and non-sports subjects.", WP + "Topps_baseball_card_products", mk=TOP, y="2006"),
     X("Panini Prizm", "Panini's refractor-style line, named Prizm because Refractor is a Topps trademark.", REF, mk=PAN)],
  r=[["Topps Chrome", TOP]])
rookie = K("Rookie card", "First base-set card of a player after reaching the top level of the sport.", WP + "Rookie_card", a="RC",
  t=["RC-logo card", "first licensed prospect card", "rookie parallel", "rookie autograph"],
  x=[X("Mickey Mantle 1951 Bowman", "Mantle's rookie card.", WP + "Rookie_card", mk=BOW, y="1951", v=[("#253", BOW, "1951", "")]),
     X("Michael Jordan 1986–87 Fleer", "The defining modern basketball rookie card.", WP + "Rookie_card", mk=FL, y="1986"),
     X("Ken Griffey Jr. 1989 Upper Deck #1", "Griffey shown in a San Bernardino Spirit uniform.", WP + "Rookie_card", mk=UD, y="1989"),
     X("Wayne Gretzky 1979 O-Pee-Chee", "Gretzky's rookie card from Topps's Canadian licensee.", EXP, mk="O-Pee-Chee", y="1979"),
     X("Young Guns", "Upper Deck's hockey rookie subset.", WP + "Upper_Deck_Company", mk=UD, y="1990–91")])
par = K("Parallel card", "Version of a base card with a different finish, colour or serial number.", REF, a="refractor · Prizm · numbered parallel",
  t=["refractor", "X-fractor", "colour refractor", "Prizm colour", "serial-numbered", "printing plate", "one-of-one", "SuperFractor"],
  x=[X("Refractor", "Rainbow-reflective parallel introduced in 1993 Finest.", REF, mk=TOP, y="1993",
       v=[("Original Finest refractor", TOP, "1993", "unmarked"), ("Colour refractors", TOP, "", "gold, blue, red, orange, green, black"),
          ("X-fractor", TOP, "", "checkerboard; Chrome and Bowman Chrome"), ("Atomic refractor", TOP, "", "Bowman's Best"),
          ("SuperFractor", TOP, "", "1/1, gold spiral")]),
     X("Prizm parallels", "Panini Prizm colour parallels.", EXP, mk=PAN,
       v=[("Gold Prizm", PAN, "", "/10"), ("Black Finite", PAN, "", "1/1"), ("Black Mosaic", PAN, "", "1/1")])])
ins = K("Insert card", "Card inserted at a lower rate than the base set, usually with its own design and theme.", OLD, a="chase card · subset",
  t=["themed insert", "die-cut", "short-printed insert", "case hit"],
  m=[["Future Stars", TOP], ["Hobby Masters", TOP], ["Ultraviolet", TOP], ["Helix", TOP], ["Shadow Etch", TOP], ["Topps Chrome Expose", TOP],
     ["Topps Chrome Champion Refractors", TOP], ["Diamond Moments", TOP]],
  r=[["Topps Chrome", TOP]])
auto = K("Autograph card", "Card signed by the player, on-card or on a sticker, often serial-numbered.", WP + "Bowman_(brand)", a="auto · signed card",
  t=["on-card autograph", "sticker autograph", "cut signature", "dual or triple autograph", "rookie autograph"],
  x=[X("Bowman Chrome prospect autographs", "Autographed prospect cards in Bowman Chrome and Bowman Draft.", WP + "Bowman_(brand)", mk=TOP, y="2001",
       v=[("Mike Trout Draft Prospects SuperFractor auto", TOP, "2009", "1/1"), ("Aaron Judge Draft Pick SuperFractor auto", TOP, "2013", "1/1")])],
  m=[["Chromographs", TOP], ["Topps Chrome Rookie Autographs", TOP], ["Topps Chrome Legends Autographs", TOP], ["75th Diamond Autographs", TOP], ["Ink Strokes", TOP]])
relic = K("Relic and memorabilia card", "Card with a swatch of game-used or player-worn material, often with an autograph (patch auto).", WP + "Upper_Deck_Company",
  a="relic · jersey card · patch card · RPA",
  t=["jersey swatch", "patch", "logoman", "bat or ball piece", "rookie patch autograph (RPA)", "debut patch"],
  x=[X("Upper Deck game-used cards", "The first cards with game-used material.", WP + "Upper_Deck_Company", mk=UD, y="1997"),
     X("Exquisite Collection", "Upper Deck's $500-retail NBA line built on rookie patch autographs.", WP + "Upper_Deck_Company", mk=UD, y="2003–04",
       v=[("LeBron James Rookie Patch Autograph", UD, "2003–04", "/99"), ("Dual Logoman Autographs", UD, "2007–08", "1/1"), ("Emblems of Endorsement", UD, "2008–09", "")]),
     X("National Treasures", "Panini's high-end line of rookie patch autographs and Logoman cards.", EXP, mk=PAN,
       v=[("Stephen Curry Logoman Autograph", PAN, "2009", "1/1"), ("Patrick Mahomes Rookie Patch Auto", PAN, "2017", ""), ("NFL Shield Autographs", PAN, "", "1/1")]),
     X("Topps Chrome MLB Debut Patch", "Patch autograph from the player's debut uniform.", EXP, mk=TOP, v=[("Paul Skenes", TOP, "2024", "1/1")])],
  m=[["Gold Logoman Relics", TOP]])
vint = K("Vintage tobacco and candy card", "Pre-war card issued with cigarettes, candy or gum, catalogued by Burdick's American Card Catalog letters (N, T).", WP + "Cigarette_card",
  a="tobacco card · caramel card · T-card",
  t=["N-series (19th-century tobacco)", "T-series (20th-century tobacco)", "back advertisement variety"],
  x=[X("T206", "American Tobacco Company's White Border set of 524 players.", WP + "T206_Honus_Wagner", mk=ATC, y="1909–1911",
       v=[("Honus Wagner", ATC, "1909", "fewer than 60 known; Piedmont and Sweet Caporal backs"), ("Gretzky Wagner", ATC, "", "PSA 8, later shown trimmed"),
          ("Jumbo Wagner", ATC, "", "miscut; sold 2013"), ("Topps T206 reissue", TOP, "2002", "")], dt="back advertisement · grade"),
     X("Peck & Snyder trade cards", "Sporting-goods trade cards often called the first baseball cards.", BC, mk="Peck & Snyder", y="1868"),
     X("Allen & Ginter tobacco cards", "Among the first cigarette cards.", WP + "Cigarette_card", mk="Allen & Ginter", y="1879")])
box = K("Box card", "Card printed on the box, panel or packaging of another product and cut from it.", "https://www.psacard.com/gradingstandards", a="hand-cut card")
sealed = K("Sealed card product", "Unopened pack, box, blaster, hanger or case of cards.", "https://www.thecardiacs.com/blogs/collecting-basics/the-complete-guide-to-sealed-wax-hobby-boxes-blasters-packs-more",
  a="wax · unopened product", t=["wax pack", "cello pack", "rack pack", "hobby box", "jumbo box", "blaster box", "hanger box", "mega box", "case", "factory set"])
S = "Specialist"
brands = [
 B(TOP, "United States", "1938", "baseball cards", "Brooklyn gum and card maker, the dominant US baseball card brand; owned by Fanatics since 2022.", WP + "Topps", seg=S, lines=["Topps flagship", "Topps Chrome", "Bowman", "Finest", "Stadium Club", "Heritage", "Allen & Ginter"]),
 B(BOW, "United States", "1927", "1948–52 sets", "Philadelphia gum and card maker bought by Topps in 1956; revived as a Topps prospect brand.", WP + "Bowman_(brand)", seg=S),
 B(FL, "United States", "1885", "1986 Fleer basketball", "Philadelphia gum maker and card brand, now owned by Upper Deck.", WP + "Fleer", seg=S),
 B(UD, "United States", "1988", "premium cards, hockey", "California card maker that launched in 1989 and introduced game-used cards.", WP + "Upper_Deck_Company", seg=S, lines=["Exquisite Collection", "Young Guns", "SP Authentic"]),
 B(PAN, "Italy", "1961", "stickers, Prizm", "Modena sticker and card publisher; Panini America (from Donruss, 2009) makes US sports cards.", WP + "Panini_Group", seg=S, lines=["Prizm", "National Treasures", "Donruss"]),
 B(DON, "United States", "", "baseball cards", "US card brand that entered baseball in 1981; bought by Panini in 2009.", BC, seg=S),
 B(GOU, "United States", "1919", "1933 Goudey", "Boston gum maker whose 1933 set began baseball gum cards.", WP + "Goudey", seg=S),
 B(ATC, "United States", "", "T206", "Tobacco company that issued the T206 set.", WP + "T206_Honus_Wagner", seg="Heritage manufactory"),
 B("O-Pee-Chee", "Canada", "", "hockey cards", "Canadian Topps licensee.", WP + "Topps_baseball_card_products", seg=S),
]
save("04_00", [base, rookie, par, ins, auto, relic, vint, box, sealed], brands, [],
 "Organised set → card → parallel → grade. Old 'Insert or autograph card' split: autograph items to Autograph card, Gold Logoman Relics to Relic card, Topps Chrome insert names cut from 26 to 8 representative inserts (Big Ticket Players, Chrome Radiating Rookies, Chrome Rivals, Class of 2026 Cooperstown Calls, Fanatical, Numbers Live Forever, Past to Present, Perspectives, Static Noise, Wild Style, World Series at Night, Wrecking Crew dropped as SKU-level). "
 "1986 Fleer Jordan card number #57 and the '1st Bowman' label not stated on any retrieved page, so not recorded. Box card and sealed product have types only; no vintage wax archetype sourced.")
