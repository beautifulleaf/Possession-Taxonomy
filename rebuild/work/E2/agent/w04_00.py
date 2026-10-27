import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
AD = "adidas"; NK = "Nike"; PU = "Puma"; GI = "Gilbert"; WI = "Wilson Sporting Goods"
WC = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_official_match_balls"
PRED = "https://en.wikipedia.org/wiki/Adidas_Predator"
COPA = "https://en.wikipedia.org/wiki/Adidas_Copa_Mundial"
MERC = "https://www.sneakerfreaker.com/performance/features/how-cristiano-ronaldo-revolutionised-nike-s-mercurial-line"
KING = "https://www.puma-catchup.com/the-history-of-pumas-iconic-football-boot-the-king/"
RB = "https://en.wikipedia.org/wiki/Rugby_ball"
MARA = "https://en.wikipedia.org/wiki/Wellington_Mara"
VT = "https://www.sportsunlimitedinc.com/2025-virginia-tech-football-helmet-ratings.html"
SP = "https://www.sportsunlimitedinc.com/blog/best-football-shoulder-pads-for-2026"
GK = "https://keepersport.net/the-10-most-popular-goalkeeper-gloves-of-2024.html"

football = {"n": "Football", "a": "soccer ball", "d": "Inflated ball made for association football; comes in sizes.",
 "t": ["match ball", "training ball", "futsal ball", "size 3 / 4 / 5"],
 "s": "https://www.rebelsport.com.au/sports/football/soccer-balls?sz=24",
 "x": [
  {"n": "Telstar", "a": "32-panel ball", "d": "Black-and-white 32-panel ball, the first adidas World Cup ball and the template for the classic football look.", "mk": AD, "y": "1970", "s": WC,
   "v": [V("Telstar", AD, "1970", "first 32-panel black-and-white World Cup ball"), V("Telstar Durlast", AD, "1974", "first polyurethane-coated, waterproof"),
         V("Telstar 18", AD, "2018", "tribute; Telstar Mechta in knockouts")],
   "dt": "panel count · leather or synthetic · replica or match grade"},
  {"n": "Tango", "a": "", "d": "Adidas ball family introduced at the 1978 World Cup and also used at Euros and Olympics until 1988.", "mk": AD, "y": "1978", "s": WC,
   "v": [V("Tango", AD, "1978"), V("Tango España", AD, "1982", "last leather World Cup ball"), V("Azteca", AD, "1986", "first fully synthetic World Cup ball")],
   "dt": "leather or synthetic · replica or match grade"},
  {"n": "World Cup official match ball", "a": "", "d": "The adidas ball made for each FIFA World Cup, sold in match and replica grades.", "mk": AD, "y": "1990", "s": WC,
   "v": [V("Etrusco Unico", AD, "1990"), V("Questra", AD, "1994"), V("Tricolore", AD, "1998", "first multicoloured World Cup ball"), V("Fevernova", AD, "2002"),
         V("Teamgeist", AD, "2006"), V("Jabulani", AD, "2010", "criticised for unpredictable flight"), V("Brazuca", AD, "2014", "six thermally bonded panels"),
         V("Al Rihla", AD, "2022", "water-based glues and inks"), V("Trionda", AD, "2026")],
   "dt": "match or replica grade · final-match colourway"}],
 "m": [["Impel Plus 24", "Mitre"], ["Academy Total 90", NK], ["Skills Total 90", NK], ["Phantom", NK], ["Big Cat", PU], ["Messi Club", AD]]}

boot = {"n": "Football boot", "a": "soccer cleat", "d": "Studded or bladed boot made for football; the ground type it suits (FG, AG, SG, MG, TF, IC) is marked on it.",
 "t": ["firm ground (FG)", "soft ground (SG)", "artificial grass (AG)", "turf (TF)", "indoor (IC)", "laceless"],
 "s": "https://www.footballboots.co.uk/?p=33073",
 "x": [
  {"n": "King", "a": "Puma King", "d": "Puma's classic leather boot, worn by Eusébio, Pelé, Cruyff and Maradona.", "mk": PU, "y": "1966", "s": KING,
   "v": [V("King (Eusébio)", PU, "1966", "after the Wembley predecessor; some sources date the first King to 1968"), V("King", PU, "1970", "flatter, lighter; worn by Pelé"),
         V("King Platinum", PU, "2020", "lightest King to date")],
   "dt": "leather upper · stud type · colourway"},
  {"n": "Copa Mundial", "a": "Copa", "d": "Black kangaroo-leather adidas boot with a twelve-stud sole, long called the best-selling football boot.", "mk": AD, "y": "1979", "s": COPA,
   "v": [V("Copa Mundial", AD, "1979", "made in Scheinfeld, Germany"), V("Copa 17.1", AD, "2017"), V("Copa Gloro 17.2", AD, "2017"), V("Copa 19+", AD, "2018", "laceless leather"),
         V("Copa Pure", AD)],
   "dt": "kangaroo or calf leather · FG, SG, AG or indoor sole · colourway"},
  {"n": "Predator", "a": "", "d": "Adidas boot with rubber elements on the upper for grip and swerve, from a concept by Craig Johnston.", "mk": AD, "y": "1994", "s": PRED,
   "v": [V("Predator", AD, "1994"), V("Predator Rapier", AD, "1995"), V("Predator Touch", AD, "1996"), V("Predator Accelerator", AD, "1998"), V("Predator Precision", AD, "2000"),
         V("Predator Mania", AD, "2002"), V("Predator Pulse", AD, "2004"), V("Predator Absolute", AD, "2006"), V("Predator PowerSwerve", AD, "2007"),
         V("Predator X", AD, "2009"), V("AdiPower Predator", AD, "2011"), V("Predator LZ", AD, "2012"), V("Predator Instinct", AD, "2014"),
         V("Predator 18", AD, "2017"), V("Predator 20 Mutator", AD, "2020"), V("Predator 21 Freak", AD, "2021"), V("Predator 22 Edge", AD, "2022"),
         V("Predator 23 Accuracy", AD, "2023"), V("Predator 25", AD, "2025")],
   "dt": "laced or laceless · fold-over tongue · FG/SG/AG · colourway"},
  {"n": "Mercurial", "a": "Mercurial Vapor · Superfly", "d": "Nike's lightweight speed boot, launched for the Brazilian striker Ronaldo and later Cristiano Ronaldo's boot.", "mk": NK, "y": "1998", "s": MERC,
   "v": [V("Mercurial", NK, "1998", "worn by Ronaldo"), V("Mercurial Vapor", NK, "", "early 2000s"), V("Mercurial Vapor SL", NK, "2008", "carbon fibre, 185 g"),
         V("CR Mercurial Vapor SuperFly II", NK, "", "Cristiano Ronaldo's first signature boot"), V("Superfly CR7", NK, "2014", "high collar, Flyknit"),
         V("Mercurial Superfly 360", NK, "2018")],
   "dt": "low or high collar · FG/SG/AG · colourway"}],
 "m": [["Tiempo Maestro", NK], ["Phantom", NK], ["F50 Hyperfast", AD], ["Future Ultimate", PU], ["Ultra Ultimate", PU], ["Furon", "New Balance"], ["Tekela", "New Balance"]],
 "r": [["Mercurial", NK]]}

gk = {"n": "Goalkeeper gloves", "a": "", "d": "Padded latex-palm gloves worn by a football goalkeeper.",
 "t": ["negative cut", "roll finger", "flat palm", "hybrid cut", "finger protection"], "s": GK,
 "m": [["Predator", AD], ["Supergrip", "Uhlsport"], ["Absolutgrip", "Uhlsport"], ["Attrakt", "Reusch"], ["Pure Contact", "Reusch"], ["Future", PU],
       ["Vapor Grip 3", NK], ["Hero", "KEEPERsport"], ["Champ", "KEEPERsport"]]}

goal = {"n": "Football goal", "a": "garden goal", "d": "Goal frame with net for garden or portable use.",
 "t": ["pop-up", "folding", "freestanding steel or uPVC", "rebounder"], "s": "https://www.kingsgrovesports.com.au/cricket/accessories.html"}

rugby = {"n": "Rugby ball", "a": "", "d": "Oval inflated ball made for rugby; comes in official-ball classes and sizes.",
 "t": ["union match ball", "league ball", "sevens ball", "training ball", "size 3 / 4 / 5"],
 "s": "https://www.gilbertrugby.com/blogs/news/the-new-gilbert-rugby-ball-range-for-2026",
 "x": [
  {"n": "Gilbert match ball", "a": "", "d": "Gilbert's union match ball, descended from the balls made for Rugby School from 1823.", "mk": GI, "y": "1823", "s": RB,
   "v": [V("Synergie", GI, "2007", "Rugby World Cup match ball")], "dt": "grip pattern · match or replica grade"}],
 "m": [["G-TR7000", GI], ["G-TR6000", GI], ["Barbarian HD", GI], ["Innovo", GI], ["Advantia", GI], ["Quantum Sevens", GI], ["Rebounder Training Ball", GI]]}

tee = {"n": "Kicking tee", "a": "", "d": "Stand that holds a rugby ball upright for place kicks.", "s": "https://www.gilbertrugby.com/blogs/news/the-new-gilbert-rugby-ball-range-for-2026"}

amf = {"n": "American football", "a": "gridiron ball", "d": "Leather or composite pointed oval ball made for American football.",
 "t": ["leather game ball", "composite", "youth and junior sizes"], "s": MARA,
 "x": [{"n": "The Duke", "a": "", "d": "Wilson's NFL game ball, named after Wellington Mara.", "mk": WI, "y": "1941", "s": MARA,
   "v": [V("The Duke", WI, "1941", "NFL game ball until 1969"), V("The Duke", WI, "2006", "revived for NFL games")], "dt": "leather · official or replica"}]}

helmet = {"n": "American football helmet", "a": "gridiron helmet", "d": "Padded hard-shell helmet with face mask made for American football; rated by Virginia Tech's STAR system.",
 "t": ["varsity / adult", "youth"], "s": VT,
 "m": [["Zero2", "VICIS"], ["Zero2 Trench", "VICIS"], ["F7 2.0", "Schutt"], ["Vengeance Pro LTD", "Schutt"], ["SpeedFlex", "Riddell"]]}

pads = {"n": "American football shoulder pads", "a": "", "d": "Hard-shelled padded harness that protects the shoulders, chest and upper back in American football.",
 "t": ["lineman", "skill position", "all-purpose", "youth"], "s": SP,
 "m": [["Power SPK+", "Riddell"], ["SPK+ Skilled", "Riddell"], ["Standard", "XTech"], ["Skill", "XTech"], ["Super Skill", "XTech"],
       ["SP69", "Douglas"], ["Legacy JD", "Douglas"], ["Razor OL/DL", "Gear Pro-Tec"], ["Razor Skill", "Gear Pro-Tec"]]}

brands = [
 {"n": AD, "c": "Germany", "f": "1949", "seg": "Mainstream", "kf": "football boots, balls", "d": "German sportswear maker; supplier of every World Cup ball since 1970.", "sig": ["Telstar", "Tango", "Copa Mundial", "Predator"], "rel": [PU], "s": "knowledge"},
 {"n": NK, "c": "United States", "seg": "Mainstream", "kf": "football boots", "d": "American sportswear maker.", "sig": ["Mercurial"], "s": "knowledge"},
 {"n": PU, "c": "Germany", "f": "1948", "seg": "Mainstream", "kf": "football boots", "d": "German sportswear maker founded by Rudolf Dassler.", "sig": ["King"], "rel": [AD], "s": "knowledge"},
 {"n": GI, "c": "United Kingdom", "f": "1823", "seg": "Heritage manufactory", "kf": "rugby balls", "d": "Rugby ball maker from Rugby, England, that began supplying Rugby School in 1823.", "sig": ["Gilbert match ball"], "s": RB},
 {"n": "Riddell", "c": "United States", "seg": "Specialist", "kf": "football helmets", "d": "American maker of football helmets and shoulder pads.", "s": "knowledge"},
 {"n": "Schutt", "c": "United States", "seg": "Specialist", "kf": "football helmets", "d": "American maker of football and baseball protective gear.", "rel": ["VICIS"], "s": "knowledge"},
 {"n": "VICIS", "c": "United States", "seg": "Specialist", "kf": "football helmets", "d": "American football-helmet maker known for its deformable outer shell.", "rel": ["Schutt"], "s": "knowledge"},
]

w('04_00', {"kinds": [football, boot, gk, goal, rugby, tee, amf, helmet, pads], "brands": brands, "traditions": [],
 "notes": "All six old kinds kept; American football, American football helmet and American football shoulder pads added as new kinds. Football: archetypes Telstar, Tango and the World Cup match-ball series, with old models trimmed to 6 (dropped Messi Home Club, a near duplicate). Boots: archetypes King, Copa Mundial, Predator and Mercurial; Copa Pure became a Copa version and Mercurial Superfly/Vapor became Mercurial versions. Goalkeeper gloves now cite KEEPERsport's 2024 top 10 instead of the old unrelated page. Rugby: Gilbert archetype from the Rugby ball article; Steeden named there as the league-ball maker but no model page found. Not added for lack of a retrieved page: Nike Flight, Select and Mitre ball histories, Gilbert Match XV, Rhino and Steeden models, Sells gloves. Football goal limited to garden/portable goals."})
