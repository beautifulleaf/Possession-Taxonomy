import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
NUM = "https://en.numista.com/catalogue/index.php"
STIPEL = "STIPEL"; NYCTA = "New York City Transit Authority"; GAULT = "John Gault"; MEISSEN = "Meissen"; ROSENTHAL = "Rosenthal"
trade = K("Trade token", "Token issued by a merchant or private issuer to be exchanged for goods or a stated value.", NUM, a="good-for piece · store card · tradesman's token",
  t=["store card", "good-for token", "political token", "advertising token", "mule"],
  x=[X("Conder token", "Privately struck British copper halfpennies, pennies and farthings issued by merchants and mines to fill a shortage of small change.", WP + "Conder_token",
       a="18th-century provincial token", y="1787–1802",
       v=[("Parys Mine Company Druid halfpenny", "Parys Mine Company", "1787–1788", "first issue, hooded Druid; Anglesey"),
          ("Soho Mint merchant tokens", "Matthew Boulton", "1788–1790s", "struck by the million at Soho"),
          ("Pidcock's menagerie token", "Gilbert Pidcock", "1790s", "Exeter Change, Strand"),
          ("James Conder's Ipswich token", "James Conder", "1794", "issued by the cataloguer himself"),
          ("Regency token revival", "", "1811–1812", "ended by the 1817 Act")],
       dt="Dalton & Hamer (D&H) number by county · edge lettering · halfpenny, penny, farthing"),
     X("Hard Times token", "American copper or brass cent-sized tokens, often political, struck during the bank crisis and the Panic of 1837.", WP + "Hard_times_token", y="1833–1843",
       v=[("Political tokens", "", "1833–1843", "Second Bank controversy, Jackson in a trunk 1837"),
          ("'Not One Cent' cent imitations", "", "1837", "Merchant's Exchange token HT-293"),
          ("'Am I Not a Woman and a Sister'", "", "1838", "anti-slavery token"),
          ("Feuchtwanger cent", "", "1837", "German silver"),
          ("Store cards", "", "1833–1843", "")],
       dt="Low and Rulau (HT) numbers · copper or brass · large-cent or half-cent size"),
     X("Civil War token", "Private US cent-sized tokens struck when government cents vanished during the Civil War.", WP + "Civil_War_token", y="1861–1864",
       v=[("Store cards", "", "1862–1864", "first by H. A. Ratterman, Cincinnati; Lindenmueller, New York 1863"),
          ("Patriotic tokens", "", "1862–1864", "flag, cannon, USS Monitor"),
          ("Sutler tokens", "", "1861–1864", "rarest; name a unit and its sutler")],
       dt="Fuld number · R-1 to R-10 rarity · copper, brass, white metal"),
     X("German Notgeld tokens", "Emergency token money of German towns, states and firms, including the ceramic pieces of 1917–1923.", "https://www.dhm.de/blog/2024/03/13/making-money-out-of-natural-materials-porcelain-emergency-money/",
       a="Notgeld · porcelain emergency money", y="1917–1923",
       v=[("Rosenthal 10 pfennig", ROSENTHAL, "1917", "first ceramic emergency coin"),
          ("Gotha 50 pfennig", "", "1920", "quartz porcelain"),
          ("Saxony porcelain series", MEISSEN, "1921", "Böttger stoneware, 20 pfennig to 20 marks"),
          ("Zinc and iron coins", "", "", "")],
       dt="issuer town or state · material (porcelain, stoneware, zinc, iron, paper) · denomination")])
transit = K("Transit and toll token", "Token issued to pay one fare or toll on a transit system, road or bridge.", NUM, a="fare token",
  x=[X("New York City subway token", "Brass fare token of the New York subway, introduced when the fare rose to 15 cents.", "https://wnyc.org/story/15-years-ago-subway-token-rode-sunset",
       mk=NYCTA, y="1953", v=[("First token", NYCTA, "1953", "15-cent fare"), ("Last tokens", NYCTA, "2003", "sales ended 12 April 2003")], dt="design series · size")])
adm = K("Admission, communion or voting token", "Token issued to admit the holder to a meeting, place or rite, to record attendance, or to cast a vote, communion tokens included.", NUM,
  a="attendance token · communion token · voting token",
  x=[X("Scottish communion token", "Token, usually pewter, issued by a Scottish church to members fit to take communion; carried abroad by emigrants.", "https://www.mernick.org.uk/thn/tokens/19th/communion_tokens.htm",
       v=[("Church of Scotland tokens", "", "", "parish name and date"), ("Secession and Free Church tokens", "", "", ""), ("Episcopal Church tokens", "", "", ""),
          ("Emigrant churches abroad", "", "", "Ireland, England, Canada, USA, Australia, New Zealand")],
       dt="parish · date · shape · metal")])
wage = K("Wage or ration token", "Token issued to workers as wages or work tally, or as a ration entitlement.", NUM, a="work token · truck token · company scrip",
  t=["mine and plantation token", "hop token", "tally token", "ration token"])
tax = K("Tax token", "Token issued to pay sales tax or another tax in fractions of the smallest coin.", NUM, a="sales tax token · mill token",
  x=[X("US sales tax tokens", "Fractional-cent tokens of 1930s US states, firms and towns for tax on small purchases.", WP + "Sales_tax_token", y="1930s",
       v=[("Missouri 1 mill 'milk top'", "", "1935", "cardboard"), ("Washington 2 mills", "", "1935", "aluminium"), ("Illinois square tokens", "", "", ""),
          ("Plastic tokens", "", "", "issued by the hundred million")],
       dt="state · mill value · cardboard, brass, aluminium, fibre, plastic")])
vend = K("Vending machine token", "Token issued to buy a product or a service from a coin-operated machine that is not a game, such as a dispenser, parking meter, car wash, laundry or telephone.", NUM,
  a="service-machine token", t=["parking token", "car-wash token", "laundry token", "telephone token"],
  x=[X("Gettone telefonico", "Italian telephone token for public phone booths, also used as small change in the 1970s.", WP + "Gettone", mk=STIPEL, y="1927",
       v=[("STIPEL token", STIPEL, "1927", "first issue"), ("Grooved token", "", "1959–1980", "last version; four-digit year-month code"),
          ("Valued 50 lire", "", "to 1980", ""), ("Valued 200 lire", "", "1984–2001", "withdrawn with the euro")],
       dt="date code (e.g. 7805 = May 1978) · maker mark")])
locker = K("Locker and shopping cart token", "Token issued to release a locker, shopping cart or similar deposit mechanism.", NUM, a="deposit token · trolley token",
  t=["shopping-trolley token", "locker token", "keyring trolley coin"],
  x=[X("Supermarket trolley token", "Coin-sized token, usually plastic, that unlocks a deposit-locked shopping trolley; often a promotional giveaway.",
       "https://www.dutchnews.nl/news/2022/08/token-gesture-albert-heijn-abolishes-coin-operated-trolleys/", y="1985",
       v=[("Albert Heijn coin-deposit trolleys", "Albert Heijn", "1985–2022", "Netherlands")], dt="plastic or metal · keyring · advertiser")])
casino = K("Casino chip and gaming token", "Chip, plaque or token issued by a casino for play at its tables or machines, collected as exonumia.", WP + "Casino_chip_collecting",
  a="cheque · casino token · poker chip", t=["casino cheque", "gaming token", "roulette chip", "plaque"],
  x=[X("Casino chip (cheque)", "Casino-specific chip collected by casino, set or denomination and graded from New to Damaged.", WP + "Casino_chip_collecting",
       v=[("$5 Golden Goose chip", "", "", "sold for $75,000 in 2014"), ("$5 Lucky Casino chip", "", "", "sold for $52,500")],
       dt="casino · denomination · colour · mould · inserts and inlay · rarity")])
love = K("Love token and counterstamped coin", "Coin smoothed and hand-engraved with initials or a design as a keepsake, or a coin struck with a private counterstamp.",
  "https://coinweek.com/love-tokens-were-once-popular-valentines-day-gifts", a="engraved coin · counterstamp · countermark", t=["love token", "counterstamped coin"],
  x=[X("Love token", "Coin smoothed on one or both sides and engraved with initials, names or scenes as a romantic gift.", "https://coinweek.com/love-tokens-were-once-popular-valentines-day-gifts",
       y="19th century", v=[("British love tokens", "", "early 19th century", "origin"), ("American love tokens", "", "1860s–1880s", "Liberty Seated dime the favourite host")],
       dt="host coin · initials, message or pictorial engraving · one or both sides")])
encased = K("Encased coin", "Coin or stamp sealed in a metal case, made as emergency money, advertising or a lucky piece.", WP + "John_Gault", a="encased postage stamp · encased cent · lucky penny",
  t=["encased postage stamp", "encased cent"],
  x=[X("Encased postage stamp", "US postage stamp in a brass case with a mica window, used as small change during the Civil War coin shortage.", WP + "John_Gault", mk=GAULT, y="1862",
       v=[("Ayer's advertising cases", GAULT, "1862–1863", "J. C. Ayer, the largest partner"), ("Lord & Taylor", GAULT, "1862–1863", ""), ("Drake's Plantation Bitters", GAULT, "1862–1863", ""),
          ("Silver cases", GAULT, "1862", "first version, abandoned")],
       dt="advertiser · stamp denomination · case metal"),
     X("Encased lucky cent", "Cent pressed into an advertising ring inscribed as a good-luck piece.", "https://www.numismaticnews.net/archive/encased-cent-marks-clubs-35th-anniversary",
       v=[("Jamestown Coin Club 35th anniversary", "", "2010", "1975 cent, 'I Bring Good Luck'")], dt="host coin date · issuer · slogan")])
weight = K("Coin weight", "Weight made to check the weight of one coin denomination on a balance.", NUM, a="coin balance weight", t=["single coin weight", "boxed coin balance with weights", "tumbrel"],
  x=[X("Boxed coin balance with weights", "Cased balance with a set of weights for checking gold coins.", "https://collection.sciencemuseumgroup.org.uk/objects/co57889/coin-balance-and-weights",
       v=[("Titford coin balance", "R. Vandome Titford and Co.", "c. 1850", "London, odd Troy weights")], dt="case · beam · weight set")])
brands = [
 B(STIPEL, "Italy", "", "telephone tokens", "Italian telephone company that introduced the gettone telefonico in 1927.", WP + "Gettone"),
 B(NYCTA, "United States", "1953", "subway tokens", "Public authority that ran the New York subway and issued its fare tokens.", "knowledge"),
 B(GAULT, "United States", "1862", "encased postage", "American entrepreneur who patented the encased postage stamp in 1862.", WP + "John_Gault", seg="Specialist"),
]
save("05_00", [trade, transit, adm, wage, tax, vend, locker, casino, love, encased, weight], brands, [],
 "Notgeld tokens placed under Trade token (local issuers; the porcelain pieces' DHM page is the source); Bavarian-only issues not separately confirmed so the archetype is German-wide. "
 "No archetype added for wage tokens (no page retrieved this session). Casino-chip makers left out: the retrieved page names none. Coin weight moved in from holders as planned.")
