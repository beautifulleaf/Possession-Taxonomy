import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
RM, USPOD = "Royal Mail", "United States Post Office Department"
PH = WP + "Postal_history"; PS = WP + "Postal_stationery"; GL = "https://iomstamps.com/pages/glossary-of-terms"
hist = K("Postal history cover", "Envelope or folded letter collected for what its markings show about rates, routes, carriage and events.", PH,
  a="entire · folded letter · postal history",
  t=["stampless (pre-adhesive) letter", "rate cover", "route cover", "censored mail", "military and field post", "ship and paquebot mail", "railway mail", "registered mail", "express mail", "disaster or wreck cover"],
  x=[X("Stampless letter", "Letter carried before adhesive stamps, rated in manuscript or handstamp.", PH, y="before 1840"),
     X("Censored cover", "Cover opened and resealed by censors, with censor tape and markings.", PH, v=[("Madrid–Paris civil cover", "", "1940", "opened by Spanish and Vichy censors")]),
     X("Balloon mail of the Siege of Paris", "Letters flown out of besieged Paris by balloon.", PH, y="1870"),
     X("Pony Express cover", "Letter carried by the Pony Express across the American West.", PH, y="1860s"),
     X("Military mail cover", "Mail of soldiers and navies, from the Opium Wars to both World Wars.", PH)])
fdc = K("First-day cover", "Cover carrying stamps cancelled on their day of issue, issued by a postal administration or prepared for the purpose.", GL, a="FDC",
  t=["cacheted", "uncacheted", "official first-day postmark", "unofficial city", "postal-administration FDC", "private cachet"],
  x=[X("Penny Black first day", "Covers with the Penny Black used before or on its first official day.", WP + "First_day_of_issue", mk=RM, y="1840",
       v=[("Bath, 2 May 1840", "", "1840", "early use"), ("6 May 1840", "", "1840", "official first day")]),
     X("George Ward Linn Harding cover", "Believed to be the first cacheted first-day cover, for the Harding memorial stamp.", WP + "First_day_of_issue", mk="George Ward Linn", y="1923"),
     X("ArtCraft cachet", "Engraved-style cachets on US first-day covers.", WP + "Cachet", mk="ArtCraft", y="1939–2015"),
     X("Fleetwood cachet", "Major US first-day cover cachet maker.", WP + "Cachet", mk="Fleetwood"),
     X("Artmaster cachet", "Major US first-day cover cachet maker.", WP + "Cachet", mk="Artmaster"),
     X("House of Farnam cachet", "Major US first-day cover cachet maker.", WP + "Cachet", mk="House of Farnam"),
     X("Colorano cachet", "Major US first-day cover cachet maker.", WP + "Cachet", mk="Colorano")])
flight = K("Flight and rocket cover", "Cover flown on a first flight, airship, balloon or rocket, or salvaged from a crash, with flight markings.", WP + "Crash_cover",
  a="aerophilately · first-flight cover · crash cover",
  t=["first-flight cover", "Zeppelin cover", "balloon mail", "rocket mail", "crash or interrupted-flight cover", "catapult mail"],
  x=[X("Zeppelin cover", "Mail carried on German airships, with on-board and flight postmarks.", WP + "Zeppelin_mail", y="1908–1939",
       v=[("Graf Zeppelin flights", "", "1928–1937", "large mail loads"), ("Hindenburg last flight", "", "1937", "17,609 pieces carried")]),
     X("Hindenburg crash cover", "Burnt mail salvaged from the Hindenburg disaster.", WP + "Crash_cover", v=[("Salvaged covers", "", "", "367 recovered")]),
     X("Crash cover", "Mail recovered from an air crash, wreck or other accident, with an explanatory cachet.", WP + "Crash_cover",
       v=[("CAM 24 Indianapolis crash", "", "1929", ""), ("El Al Flight 402", "", "1955", "")]),
     X("Rocket mail cover", "Cover flown in an experimental mail rocket.", WP + "Rocket_mail",
       v=[("Friedrich Schmiedl V-7", "", "", "Austria, 102 pieces"), ("Gerhard Zucker, Scarp", "", "1934", "Scotland; rockets exploded"),
          ("Stephen Smith flights", "", "1934–1944", "India, 80 mail-carrying rockets"), ("USS Barbero missile mail", USPOD, "1959", "Regulus cruise missile")]),
     X("First-flight cover", "Cover carried on an inaugural air route.", PH, v=[("Nassau–Miami", "", "1929", "")])])
pm = K("Postmark and cancellation", "Postal marking that dates an item or cancels its stamp, collected on piece or cover (marcophily).", WP + "Postmark",
  a="cancel · marcophily",
  t=["handstamp", "machine cancel", "slogan postmark", "pictorial postmark", "first-day postmark", "fancy cancel", "railway post office", "maritime", "backstamp"],
  x=[X("Bishop mark", "The first postmark, showing day and month.", WP + "Postmark", mk="General Post Office", y="1661"),
     X("Maltese Cross", "Cross-shaped obliterator used on the first British stamps.", "https://www.gbps.org.uk/displays/imperf-le-cancellations", mk=RM, y="1840",
       v=[("Red ink", RM, "1840", ""), ("Black ink", RM, "1841", "")]),
     X("Barred numeral", "Numbered bar obliterator that replaced the Maltese Cross in Britain.", "https://www.gbps.org.uk/displays/imperf-le-cancellations", mk=RM),
     X("Slogan postmark", "Machine postmark carrying an advertising or public-information slogan.", WP + "Postmark"),
     X("Pictorial postmark", "Illustrated postmark marking a local event or anniversary.", WP + "Postmark")])
maxi = K("Maximum card", "Picture postcard bearing a stamp on the picture side, with stamp, picture and postmark in concordance.", WP + "Maximum_card", a="maxicard · maximaphily")
pnc = K("Philatelic numismatic cover", "Cover issued by a postal administration that carries stamps cancelled for an issue together with a coin or medal mounted in it.", GL, a="PNC")
env = K("Stamped envelope", "Envelope with a printed or embossed stamp issued by a postal administration.", PS, a="postal stationery envelope",
  t=["entire", "cut square", "registration envelope", "embossed", "printed indicium"],
  x=[X("Mulready envelope", "The first postal stationery, with William Mulready's allegorical design, widely lampooned.", WP + "Mulready_stationery", mk=RM, y="1840",
       v=[("1d black envelope and letter sheet", RM, "1840", "engraved by John Thompson"), ("2d blue envelope and letter sheet", RM, "1840", ""),
          ("Mulready caricatures", "private stationers", "1840", "parodies")]),
     X("Embossed penny pink envelope", "British embossed stamped envelope that replaced the Mulready.", WP + "Mulready_stationery", mk=RM, y="1841"),
     X("Nesbitt series", "First US stamped envelopes, made by contractor George F. Nesbitt.", PS, mk=USPOD, y="1853")],
  m=[["Columbian envelopes", USPOD], ["Plimpton series", USPOD]])
card = K("Postal card", "Card with a printed stamp sold by a postal administration, needing no adhesive stamp.", "https://slpost.gov.lk/services/stamps-and-stamped-stationery/", a="postcard with printed stamp",
  t=["single card", "message-reply card", "pictorial card", "official card"],
  x=[X("Korrespondenz-Karte", "The world's first postal card, proposed by Emanuel Herrmann.", WP + "Postal_card", mk="Austro-Hungarian postal administration", y="1869"),
     X("US postal card", "US postal cards issued from 1873, with message-reply cards from 1892.", WP + "Postal_card", mk=USPOD, y="1873",
       v=[("Message-reply card", USPOD, "1892", "")])],
  m=[["Columbian Exposition postal card", USPOD]])
aero = K("Aerogram", "Sheet or card with a printed stamp, issued by a postal administration, that folds and seals to form its own envelope; aerograms, letter sheets and lettercards.",
  "https://slpost.gov.lk/services/stamps-and-stamped-stationery/", a="aerogramme · air letter · letter sheet · lettercard",
  t=["aerogramme", "letter sheet", "lettercard", "forces air letter"],
  x=[X("Iraq aerogramme", "The first issued aerogramme, devised by Major D. W. Gumbley.", WP + "Aerogram", mk="Iraqi postal administration", y="1933"),
     X("Forces air letter (bluey)", "Lightweight self-sealing British forces letter.", WP + "Aerogram", mk=RM),
     X("US Air Letter Sheet", "10-cent US air letter sheet.", WP + "Aerogram", mk=USPOD, y="1947"),
     X("GB Christmas aerogramme", "British Christmas aerogramme.", WP + "Aerogram", mk=RM, y="1967")])
wrap = K("Newspaper wrapper", "Paper band with a printed stamp, issued by a postal administration, to wrap newspapers or printed matter for posting.", PS, a="postal band · wrapper",
  x=[X("US newspaper wrapper", "The first newspaper wrappers.", WP + "Wrapper_(philately)", mk=USPOD, y="1861–1934"),
     X("British newspaper wrapper", "Queen Victoria wrappers and later issues.", WP + "Wrapper_(philately)", mk=RM, y="1870")])
S = "Specialist"
brands = [
 B("ArtCraft", "United States", "1939", "engraved cachets", "US first-day cover cachet maker, active 1939–2015.", WP + "Cachet", seg=S),
 B("Fleetwood", "United States", "", "first-day covers", "US first-day cover cachet maker.", WP + "Cachet", seg=S),
 B("Artmaster", "United States", "", "first-day covers", "US first-day cover cachet maker.", WP + "Cachet", seg=S),
 B("House of Farnam", "United States", "", "first-day covers", "US first-day cover cachet maker.", WP + "Cachet", seg=S),
 B("Colorano", "United States", "", "silk cachets", "US first-day cover cachet maker.", WP + "Cachet", seg=S),
 B("George Ward Linn", "United States", "", "first cacheted FDC", "Philatelist credited with the first cacheted first-day covers (1923).", WP + "First_day_of_issue", seg="Artisan & independent"),
 B("General Post Office", "United Kingdom", "1660", "Bishop mark", "English and later British state postal service, forerunner of Royal Mail.", "knowledge"),
]
save("03_01", [hist, fdc, flight, pm, maxi, pnc, env, card, aero, wrap], brands, [],
 "Postal history, flight/rocket, postmark and maximum-card kinds added from retrieved Wikipedia pages (Postal history, Crash cover, Rocket mail, Zeppelin mail, Postmark, Maximum card) and a GBPS page for the Maltese Cross. "
 "Cachet makers (ArtCraft, Fleetwood, Artmaster, House of Farnam, Colorano) are archetypes of First-day cover. Plimpton envelopes, Columbian envelopes and the Columbian postal card stay as models (no page detail retrieved). "
 "Queen Victoria embossed 1d pink envelope became the 'Embossed penny pink envelope' archetype. Royal Mail and US Post Office Department brand entries are in shelf 03_00.")
