import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
NUM = "https://en.numista.com/catalogue/index.php"
RM, MDP, MACO, FM = "Royal Mint", "Monnaie de Paris", "Medallic Art Company", "The Franklin Mint"
SCD = "https://www.whitmanexpo.com/?p=3910"
QVJ = WP + "Queen_Victoria_Golden_Jubilee_Medal"
comm = K("Commemorative medal", "Medal struck to mark an event, person or anniversary, such as a coronation, jubilee, birth or visit.", NUM, a="historical medal",
  t=["struck", "cast", "table medal", "wearable medal with ribbon"],
  x=[X("British coronation and jubilee medals", "Official royal medals for coronations and jubilees, issued in metals by rank and worn with a ribbon.", QVJ,
       y="1809–2023", v=[("George III Jubilee Medal", "", "1809", ""), ("Queen Victoria Golden Jubilee Medal", "", "1887", "gold, silver, bronze by rank; Boehm and Emptmayer"),
          ("Diamond Jubilee Medal", "", "1897", "or '1897' bar on the 1887 medal"), ("Edward VII Coronation Medal", "", "1902", ""), ("George V Coronation Medal", "", "1911", ""),
          ("George V Silver Jubilee Medal", "", "1935", ""), ("George VI Coronation Medal", "", "1937", ""),
          ("Elizabeth II Coronation Medal", RM, "1953", "Cecil Thomas; 129,051 awarded"), ("Silver Jubilee Medal", "", "1977", ""), ("Golden Jubilee Medal", "", "2002", ""),
          ("Diamond Jubilee Medal", "", "2012", ""), ("Platinum Jubilee Medal", "", "2022", ""), ("Charles III Coronation Medal", "", "2023", "")],
       dt="metal (gold, silver, bronze) · police and mayors' versions · ribbon"),
     X("So-called dollar", "US historical medal about the size of a silver dollar (33–45 mm), half of them for fairs and expositions.", SCD,
       v=[("Erie Canal completion", "", "1826", ""), ("Crystal Palace medal", "", "1853", ""), ("Transcontinental Railroad completion", "", "1869", ""),
          ("World's Columbian Exposition", "", "1893", "Chicago"), ("McCormick Reaper Centennial", "", "1931", ""), ("Boy Scouts 50th-anniversary Jamboree", "", "1960", ""),
          ("Pony Express centennial", "", "1961", "")],
       dt="Hibler–Kappen or Shevlin number · gold, silver, bronze, aluminium, gutta-percha · rarity R-1 to R-10"),
     X("Franklin Mint medals", "Privately minted gold and silver commemorative medals and medallions, the firm's first product line.", WP + "The_Franklin_Mint", mk=FM, y="1964",
       v=[("Nobel Prizes medal", FM, "1975", "")], dt="series · sterling or gold · proof finish")])
art = K("Art medal", "Medal or plaquette struck or cast as a work of medallic art.", NUM, a="plaquette · medallic sculpture", t=["struck medal", "cast medal", "plaquette"],
  x=[X("French Art Nouveau medals and plaquettes", "Rimless pictorial medals and rectangular plaquettes of the French medallic revival led by Roty and Chaplain.", WP + "Oscar_Roty",
       y="1867–1911",
       v=[("Roty's Naudet medal", "Oscar Roty", "1867", "first rimless design"), ("Roty medals", "Oscar Roty", "", "Patria, Lens Mining Company, Panama canal"),
          ("Chaplain's presidential portraits", "Jules-Clément Chaplain", "1877–1899", "Mac-Mahon to Loubet"),
          ("Chaplain's Nicholas II visit medal", "Jules-Clément Chaplain", "1896", ""), ("Chaplain's Victor Hugo medal", "Jules-Clément Chaplain", "1902", "")],
       dt="medallist · struck or cast · bronze or silver · plaquette or round"),
     X("Society of Medalists issues", "Annual subscription art medals by American sculptors, struck by the Medallic Art Company.", WP + "Medallic_Art_Company", mk=MACO, y="1930",
       v=[("Society of Medalists", MACO, "1930–1995", "annual issues"), ("Hall of Fame for Great Americans", MACO, "1963–1975", "96 medals by 42 sculptors"),
          ("National Parks Centennial Series", MACO, "1972", "37 medals by Frank Hagel"), ("Hudson-Fulton Medal", MACO, "1909", "Circle of Friends of the Medallion")],
       dt="issue number · sculptor · bronze or silver")])
award = K("Award medal", "Disc medal given for achievement in sport, school, military or other competition, finisher's medals included.", NUM, a="finisher's medal · prize medal",
  t=["sport", "school or academic", "exhibition prize", "finisher's medal"],
  x=[X("Olympic medal", "Gold, silver or bronze medal for the top three in an Olympic event, plus participation and commemorative medals.", WP + "Olympic_medal", y="1896",
       v=[("Athens 1896", "", "1896", "silver for winners; Chaplain"), ("Paris 1900", "", "1900", "rectangular; Frédérique Vernon"), ("St Louis 1904", "", "1904", "first gold-silver-bronze; solid gold to 1912"),
          ("London 1908 and Stockholm 1912", "", "1908–1912", "Bertram Mackennal"), ("Cassioli 'Trionfo'", "", "1928–2000", "Nike obverse"), ("Munich 1972 reverse", "", "1972", "Gerhard Marcks"),
          ("Athens 2004 obverse", "", "2004", "Elena Votsi; still in use"), ("Participation medal", "", "", "every athlete"), ("Commemorative medal", "", "", "athletes, staff, officials")],
       dt="Games and year · Summer or Winter · gold, silver, bronze · sport")])
souv = K("Souvenir medal", "Souvenir piece struck for a place or event and sold to visitors.", NUM, a="tourist medal · exposition souvenir",
  t=["exposition souvenir", "tourist landmark medal", "event souvenir"])
elong = K("Elongated coin", "Coin rolled flat and embossed with a new design, sold as a souvenir.", WP + "Elongated_coin", a="pressed penny · smashed penny",
  t=["oldies (1893–c.1965)", "modern (c.1965–1985)", "contemporary machine-rolled (1988–)"],
  x=[X("World's fair elongated cent", "Elongated cent rolled at a national fair, the first type of elongated coin.", WP + "Elongated_coin", y="1893",
       v=[("World's Columbian Exposition", "", "1893", "Chicago; first US elongateds"), ("Pan-American Exposition", "", "1901", "Charles Damm")], dt="host coin · fair"),
     X("Machine pressed penny", "Souvenir elongated coin from a coin-operated rolling machine at a museum, zoo or theme park.", WP + "Elongated_coin", y="1979",
       v=[("'I Love Oregon'", "", "1979", "first coin-op vendor, Meier & Frank"), ("Mickey Mouse Rays", "", "1987", "first Disneyland machine, Centex"),
          ("Stand-alone commercial machines", "", "1988", "Randy and Earl Vaughn, Dayton")], dt="host coin (pre-1982 cent preferred) · location · die")])
chal = K("Challenge coin", "Coin-shaped medal issued to members of a unit, club or organisation.", "https://signaturecoins.com/army-challenge-coins/", a="membership medal · unit coin",
  t=["military unit", "presidential", "agency and police", "corporate and club"],
  x=[X("Military unit challenge coin", "Medallion with a unit's insignia carried to prove membership or given by commanders as a recognition award.", WP + "Challenge_coin",
       v=[("17th Infantry Regiment coin", "", "1950–1958", "oldest surviving"), ("427 Squadron MGM lion coin", "", "1943", "Canada"),
          ("Air Force airman's coin", "", "", "basic training graduates")], dt="unit · enamel colours · shape · numbered"),
     X("Presidential challenge coin", "Challenge coin given by a US president.", WP + "Challenge_coin", y="late 1990s",
       v=[("Clinton coins", "", "1990s", ""), ("Obama coin", "", "", ""), ("Trump coin", "", "", "no presidential seal"), ("Biden coin", "", "", "")])])
brands = [
 B(RM, "United Kingdom", "886", "coins and medals", "The United Kingdom's state mint.", "knowledge"),
 B(MDP, "France", "864", "coins and art medals", "French state mint; production moved to Pessac in 1973, the Paris site keeps the museum.", "https://www.gracesguide.co.uk/Monnaie_de_Paris"),
 B(MACO, "United States", "1903", "art medals", "Private US mint founded by Henri Weil; Society of Medalists, Pulitzer and inaugural medals.", WP + "Medallic_Art_Company", seg="Heritage manufactory"),
 B(FM, "United States", "1964", "collector medals", "Private mint founded by Joseph Segel in Pennsylvania, later a die-cast and collectibles brand.", WP + "The_Franklin_Mint", seg="Mainstream"),
]
save("05_01", [comm, art, award, souv, elong, chal], brands, [],
 "Elongated coin split from Souvenir medal's alias as planned. Royal coronation and jubilee medals are archetyped here as commemoratives; they also appear in British long-service and orders context only by cross-link. "
 "Monnaie de Paris kept in the register as a medal maker; no named Paris Mint art-medal series retrieved, so the Roty/Chaplain archetype carries no mint mk. Hibler–Kappen numbers not added (catalogue page not retrieved).")
