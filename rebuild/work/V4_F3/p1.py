from lib import *

BUL = WP + 'List_of_bullion_coins'
REP = []

def bullion(d):
    k = kind(d, 'Bullion coin')
    gm = {'Krugerrand': 'South Africa', 'Canadian Gold Maple Leaf': 'Canada', 'Canadian Silver Maple Leaf': 'Canada',
          'Libertad': 'Mexico', 'Chinese Panda': 'China', 'Australian Gold Nugget': 'Australia',
          'American Gold Eagle': 'United States', 'American Silver Eagle': 'United States', 'Britannia': 'United Kingdom',
          'Vienna Philharmonic': 'Austria', 'Australian Silver Kookaburra': 'Australia', 'Australian Koala': 'Australia',
          'Somalian Elephant': 'Somalia', 'American Buffalo': 'United States', 'Perth Mint Lunar series': 'Australia',
          "Queen's Beasts": 'United Kingdom'}
    setg(k, gm)
    for x in k['x']:
        if x['n'] == 'Libertad': x['s'] = BUL
    def ver(name, extra):
        for x in k['x']:
            if x['n'] == name:
                have = {v['n'] for v in x.get('v', [])}
                for v in extra:
                    if v['n'] not in have: x.setdefault('v', []).append(v)
    ver('Chinese Panda', [V('Palladium Panda', '1989', '0.5 oz, per the bullion list')])
    ver('Vienna Philharmonic', [V('Platinum', '2016', ''), V('Silver', '2008', ''), V('Gold', '1989', '')])
    ver('Britannia', [V('Platinum', '2018', '')])
    ver('Somalian Elephant', [V('Gold', '2004', '.999'), V('Silver', '2004', '.9999')])
    ver('American Buffalo', [V('Gold', '2006', '')])
    ver('Canadian Silver Maple Leaf', [V('Silver', '1988', '.9999')])
    ver('Australian Koala', [V('Platinum Koala', '1988', ''), V('Silver Koala', '2007', '')])
    ver('Australian Silver Kookaburra', [V('Silver', '1990', '')])
    ver('Libertad', [V('Gold .900, .999 from 1991', '1981', ''), V('Silver', '1982', '')])
    def B(n, g, v, d, mk='', a=''):
        return E(n, d, y=min(x['y'] for x in v if x['y']), mk=mk, g=g, s=BUL, v=v, a=a)
    new = [
        B('Dragon', 'Australia', [V('Gold rectangular coin', '2018'), V('Silver', '2018')], 'Perth Mint bullion coin with a dragon design, in gold and silver.', 'Perth Mint'),
        B('Emu', 'Australia', [V('Palladium', '1995')], 'Australian palladium bullion coin.', 'Perth Mint'),
        B('Platinum Platypus', 'Australia', [V('Platinum', '2011')], 'Australian platinum bullion coin.', 'Perth Mint'),
        B('Frigatebird', 'Antigua and Barbuda', [V('Silver', '2021')], 'Silver annual bullion coin of Antigua and Barbuda.'),
        B("Noah's Ark", 'Armenia', [V('Silver', '2011')], 'Silver annual bullion coin of Armenia.'),
        B('Bhutan Lunar', 'Bhutan', [V('Silver', '2016')], 'Silver annual bullion coin of Bhutan.'),
        B('Lost Tiger', 'Cambodia', [V('Silver', '2022')], 'Silver annual bullion coin of Cambodia.'),
        B('Mandrill', 'Cameroon', [V('Silver', '2018')], 'Silver annual bullion coin of Cameroon.'),
        B("World's Wildlife", 'Democratic Republic of the Congo', [V('Silver', '2019')], 'Silver annual bullion coin of the Democratic Republic of the Congo.'),
        B('Silverback Gorilla', 'Republic of the Congo', [V('Silver', '2015')], 'Silver annual bullion coin of the Republic of the Congo.'),
        B('HMS Bounty', 'Cook Islands', [V('Silver', '2020', '.9999')], 'Silver annual bullion coin of the Cook Islands.'),
        B('Giraffe', 'Equatorial Guinea', [V('Silver', '2022')], 'Silver annual bullion coin of Equatorial Guinea.'),
        B('Lady Justice', 'Gibraltar', [V('Silver', '2022')], 'Silver annual bullion coin of Gibraltar.'),
        B('African Leopard', 'Ghana', [V('Silver', '2019')], 'Silver annual bullion coin of Ghana.'),
        B('Emami', 'Iran', [V('Gold', '1980', '.900')], 'Iranian gold bullion coin.'),
        B('Isle of Man Angel', 'Isle of Man', [V('Gold', '1984', '.999'), V('Silver', '1995')], 'Isle of Man bullion coin, in gold and silver.'),
        B('Isle of Man Noble', 'Isle of Man', [V('Platinum', '1983'), V('Silver', '1994')], 'Isle of Man bullion coin, in platinum and silver.'),
        B('Domestic cats', 'Isle of Man', [V('Silver', '1998')], 'Isle of Man silver annual bullion coin.'),
        B('Jerusalem of Gold', 'Israel', [V('Gold', '2010')], 'Israeli gold bullion coin.', 'Israel Mint'),
        B('Snow Leopard', 'Kazakhstan', [V('Silver', '2009')], 'Silver annual bullion coin of Kazakhstan.'),
        B('Tiger', 'Laos', [V('Silver', '2020')], 'Silver annual bullion coin of Laos.'),
        B('Kijang Emas', 'Malaysia', [V('Gold', '2001')], 'Malaysian gold bullion coin.'),
        B('Melita', 'Malta', [V('Gold', '2018', '.999'), V('Silver', '2021')], 'Maltese bullion coin, in gold and silver.'),
        B('Mexican Centenario', 'Mexico', [V('Gold', '1921', '.900')], 'Mexican gold coin first struck in 1921; the bullion list gives its date as 1921.'),
        B('Onza Troy', 'Mexico', [V('Silver', '1949', '.925')], 'Mexican silver ounce coin.'),
        B('Kiwi', 'New Zealand', [V('Gold', '1990'), V('Silver', '1990')], 'New Zealand bullion coin, in gold and silver.'),
        B('Taku (Turtle)', 'Niue and Fiji', [V('Silver', '2010')], 'Silver annual bullion coin issued for Niue and Fiji.'),
        B('Birds of Paradise', 'Papua New Guinea', [V('Silver', '2022')], 'Silver annual bullion coin of Papua New Guinea.'),
        B('Orzeł bielik (Polish Eagle)', 'Poland', [V('Gold', '1995')], 'Polish gold bullion coin.', 'National Bank of Poland'),
        B('Columbus', 'Portugal', [V('Palladium', '1987')], 'Portuguese palladium bullion coin.'),
        B('George the Victorious', 'Russia', [V('Gold', '2006', '.999'), V('Silver (Saint George the Victorious)', '2009')], 'Russian bullion coin, in gold and silver.', 'Central Bank of the Russian Federation'),
        B('Ballerina', 'Russia', [V('Palladium', '1989')], 'Russian palladium bullion coin.'),
        B('African Ounce', 'Rwanda', [V('Silver', '2008')], 'Silver annual bullion coin of Rwanda.'),
        B('Nikola Tesla', 'Serbia', [V('Silver', '2018')], 'Silver annual bullion coin of Serbia.'),
        B('Lion', 'Singapore', [V('Gold', '1990')], 'Singapore gold bullion coin.'),
        B('Big 5', 'South Africa', [V('Gold', '2019')], 'South African gold bullion coin of the Big Five animals.', 'South African Mint'),
        B('Chiwoo Cheonwang', 'South Korea', [V('Silver', '2016')], 'South Korean silver annual bullion coin.'),
        B('Iberian Lynx', 'Spain', [V('Gold', '2021')], 'Spanish gold bullion coin.'),
        B('Archangel Michael', 'Ukraine', [V('Gold', '2011'), V('Silver', '2011', '.9999')], 'Ukrainian bullion coin, in gold and silver.', 'National Bank of Ukraine'),
        B('South Sea Dragon', 'Tuvalu', [V('Rhodium 1 oz', '2018', 'mintage 1,000; Baird & Co')], 'Rhodium bullion coin, the only rhodium entry in the list.', 'Baird & Co'),
        B('Trident', 'Barbados', [V('Silver, four coins', '2017')], 'Limited silver series of four coins.', 'Scottsdale Mint'),
        B('Wildlife series', 'Canada', [V('Silver, six coins', '2011')], 'Limited silver series of six coins.', 'Royal Canadian Mint'),
        B('ZI:SIN (Twelve Guardians)', 'South Korea', [V('Silver, twelve coins', '2017')], 'Limited silver series of twelve coins.', 'KOMSCO'),
        B('Sea creatures', 'Tokelau', [V('Silver, twelve coins', '2014')], 'Limited silver series of twelve coins.', 'Highland Mint'),
        B('30th anniversary of Ukrainian independence', 'Ukraine', [V('Silver, one coin', '2021')], 'One-coin limited silver issue.', 'National Bank of Ukraine Mint'),
        B('America the Beautiful five-ounce silver', 'United States', [V('Silver, 56 coins', '2010')], 'Limited silver series of 56 coins.', 'United States Mint'),
    ]
    # existing Lunar/Queen's Beasts descriptions kept; fix their series mint/year in versions untouched
    add(k, new)
    # drop loose models: all 18 are now entries above or versions
    REP.append(('Bullion coin', 'm all matched to entries', len(k.get('m') or [])))
    k['m'] = []
    # gold lunar range stays as range
    countries = sorted({x['g'] for x in k['x']})
    order(k, countries)
    k['nl'] = 'One entry is a bullion coin series issued by one state or mint; metal variants, sizes and finish changes are versions.'
    k['sel'] = ("Every series in Wikipedia's List of bullion coins (gold, palladium, platinum, rhodium, annual silver and limited silver series), "
                "complete; the gold Sovereign is under Circulation coin; bars and rounds have no whole-space reference and are in their own kinds.")
    k['xg'] = 'by issuing country'

def bars_rounds(d):
    for n in ('Bullion bar', 'Bullion round'):
        k = kind(d, n)
        promote_m(k, REP)
        k['nl'] = 'One entry is a bar or round sold under a refiner or mint brand and product line; weights and finishes are versions.'
        k['sel'] = 'No whole-space reference exists for private refiner products; the list keeps the products named in the earlier catalogue pass and promotes the maker-named models.'
        k['xg'] = 'by refiner or mint'
        for x in k['x']:
            if not x.get('g'): x['g'] = x.get('mk') or ''

# ---------------- circulating coins ----------------
USC = WP + 'Coins_of_the_United_States_dollar'; GBC = WP + 'Coins_of_the_pound_sterling'; EUC = WP + 'Euro_coins'
CAC = WP + 'Coins_of_the_Canadian_dollar'; AUC = WP + 'Coins_of_the_Australian_dollar'; JPY = WP + 'Japanese_yen'
ZAR = WP + 'South_African_rand'; INR = WP + 'Indian_rupee'; RUB = WP + 'Russian_ruble'; BRL = WP + 'Brazilian_real'
CNY = WP + 'Renminbi'; CHF = WP + 'Swiss_franc'; MXN = WP + 'Mexican_peso'

ISSUERS = ['United States', 'Canada', 'Mexico', 'Brazil', 'United Kingdom', 'Eurozone', 'Spain', 'France', 'Austria', 'Switzerland', 'Russia',
           'South Africa', 'India', 'China', 'Japan', 'Australia', 'Other issuers']

def circ(d):
    k = kind(d, 'Circulation coin')
    gm = {'Spanish dollar': 'Spain', 'Maria Theresa thaler': 'Austria', 'Napoléon': 'France', 'Sovereign': 'United Kingdom',
          'Morgan dollar': 'United States', 'Peace dollar': 'United States', 'Walking Liberty half dollar': 'United States',
          'Mercury dime': 'United States', 'Buffalo nickel': 'United States', 'Lincoln cent': 'United States',
          'Standing Liberty quarter': 'United States', 'Barber coinage': 'United States', 'Jefferson nickel': 'United States',
          'Vreneli': 'Switzerland', 'South African Republic pond': 'South Africa', 'Yuan Shikai dollar': 'China',
          '500 yen coin': 'Japan', 'Loonie': 'Canada', 'French Semeuse': 'France', 'Swiss Helvetia coins': 'Switzerland'}
    setg(k, gm)
    # loose models that duplicate new entries are dropped; others promoted
    keep = [m for m in (k.get('m') or []) if m[0] in ('Flying Eagle cent', 'Indian Head cent', 'Liberty Head nickel', 'Franklin half dollar',
            'Flowing Hair dollar', 'Draped Bust dollar')]
    k['m'] = []
    for m in keep:
        k['x'].append(E(m[0], 'US circulation coin type listed by the earlier catalogue pass.', mk=m[1], g='United States', s='https://en.numista.com/catalogue/index.php'))
    REP.append(('Circulation coin', 'm: 6 US types promoted, rest absorbed into the new series entries or dropped', len(keep)))
    new = [
        E('Wheat cent', 'US one-cent coin with wheat ears on the reverse, with steel (1943) and brass (1944-1946) variants.', '1909', 'United States Mint', 'United States', USC,
          [V('Wheat cent', '1909-1958'), V('1943 steel', '1943'), V('1944-1946 brass', '1944')]),
        E('Lincoln Memorial cent', 'US one-cent coin with the Lincoln Memorial reverse.', '1959', 'United States Mint', 'United States', USC,
          [V('Memorial reverse', '1959-2008'), V('Lincoln Bicentennial', '2009'), V('Union shield', '2010')]),
        E('Roosevelt dime', 'US ten-cent coin, in production from 1946.', '1946', 'United States Mint', 'United States', USC, [V('Semiquincentennial', '2026')]),
        E('Washington quarter', 'US quarter dollar with an eagle reverse, 1932-1974 and 1977-1998.', '1932', 'United States Mint', 'United States', USC,
          [V('Eagle reverse', '1932-1974'), V('Bicentennial', '1975-1976'), V('Eagle reverse resumed', '1977-1998'), V('Washington crossing the Delaware', '2021')]),
        E('Kennedy half dollar', 'US half dollar issued since 1964.', '1964', 'United States Mint', 'United States', USC,
          [V('Kennedy half dollar', '1964-1974'), V('Bicentennial', '1975-1976'), V('Kennedy resumed', '1977'), V('Semiquincentennial', '2026')]),
        E('Eisenhower dollar', 'Large US dollar coin of 1971-1978.', '1971', 'United States Mint', 'United States', USC, [V('Bicentennial (Liberty Bell over Moon)', '1975-1976')]),
        E('Susan B. Anthony dollar', 'Small US dollar coin, issued 1979-1981 and 1999.', '1979', 'United States Mint', 'United States', USC),
        E('Sacagawea and Native American dollar', 'US golden-coloured dollar coin, Sacagawea design from 2000 and Native American reverses from 2009.', '2000', 'United States Mint', 'United States', USC,
          [V('Sacagawea', '2000-2008'), V('Native American', '2009')]),
        E('Presidential dollar', 'US dollar coin series with a president on each issue.', '2007', 'United States Mint', 'United States', USC, [V('2007-2016 and 2020 issues', '2007')]),
        E('American Innovation dollar', 'US dollar series planned to run 2018-2032, not currently circulated.', '2018', 'United States Mint', 'United States', USC),
        E('Canadian Victorian decimal coinage', 'Decimal coins of the Province of Canada from 1858 and of the Dominion from 1870 (5, 10, 25 and 50 cents; 1 cent from 1876).', '1858', '', 'Canada', CAC,
          [V('Province of Canada', '1858'), V('Dominion silver', '1870'), V('1 cent', '1876')]),
        E('Voyageur dollar', 'Canadian silver dollar with the voyageur design, first struck for the 1935 Silver Jubilee.', '1935', '', 'Canada', CAC,
          [V('1935 Silver Jubilee', '1935'), V('1937 circulating type', '1937')]),
        E('George VI coinage of 1937', 'Canadian designs of 1937: cent maple twig, nickel beaver, dime Bluenose, quarter caribou, half dollar arms, dollar voyageur.', '1937', '', 'Canada', CAC,
          [V('Tombac wartime nickel', '1942'), V('Maple leaf coinage', '1947')]),
        E('Elizabeth II Canadian coinage', 'Canadian coins under four obverse portraits; sub-dollar coins went to plated steel in 2000.', '1953', 'Royal Canadian Mint', 'Canada', CAC,
          [V('Gillick portrait', '1953'), V('Machin portrait', '1965'), V('Dora dePedery-Hunt portrait', '1990'), V('Blunt portrait', '2003'), V('Plated steel', '2000')]),
        E('Toonie', 'Canadian two-dollar coin with a polar bear, replacing the two-dollar note.', '1996', 'Royal Canadian Mint', 'Canada', CAC),
        E('Charles III Canadian coinage', 'Canadian coins with the King\'s portrait, the loonie first, entering circulation in December 2023.', '2023', 'Royal Canadian Mint', 'Canada', CAC),
        E('Mexican coin series (AA to D)', 'Mexican circulating coin families identified by series letter.', '1970', '', 'Mexico', MXN,
          [V('Series AA', '1970', 'demonetised 1995'), V('Series A', '1984', 'demonetised 1995'), V('Series B nuevo peso', '1992'), V('Series C', '1996'), V('Series D', '2009'), V('Series C1', '2020'), V('Bimetallic state coins ($100)', '2003')]),
        E('Brazilian real coins', 'Coins of the real: two series, from 1994 and from 1998.', '1994', '', 'Brazil', BRL, [V('First series', '1994-1997'), V('Second series', '1998')]),
        E('UK pre-decimal coinage', 'British farthing, threepence, sixpence, shilling, florin and crown in circulation before decimalisation.', '1860', 'Royal Mint', 'United Kingdom', GBC,
          [V('Farthing', '1860-1961'), V('Threepence', '1937-1971'), V('Sixpence', '1947-1980'), V('Shilling', '', 'withdrawn 1990'), V('Florin', '', 'withdrawn 1993'), V('Crown', '1951', 'now commemorative')]),
        E('UK decimal coinage', 'British decimal coins from 1968, with the larger early 5p, 10p and 50p and later redesigns.', '1968', 'Royal Mint', 'United Kingdom', GBC,
          [V('5p and 10p, larger', '1968'), V('50p, larger', '1969'), V('1p and 2p', '1971'), V('20p', '1982'), V('Round £1', '1983', 'to 2016'), V('Smaller 5p', '1990'), V('Smaller 10p', '1992'), V('Copper-plated steel 1p and 2p', '1992'), V('Smaller 50p', '1997'), V('Bimetallic £2', '1997', 'issued 1998')]),
        E('Royal Shield of Arms coinage', 'British coins from 2008 with a shield reverse on 1p to 50p and a round £1.', '2008', 'Royal Mint', 'United Kingdom', GBC, [V('Britannia £2', '2015'), V('Nickel-plated steel 5p and 10p', '2012')]),
        E('Twelve-sided pound', 'British twelve-sided bimetallic £1 coin, in circulation from 28 March 2017.', '2017', 'Royal Mint', 'United Kingdom', GBC),
        E('Charles III coinage', 'British coins with animal and plant reverses, from late 2023 (1p, 2p, 50p and £2 in 2023; £1 in 2024; 5p in 2025; 10p in 2026).', '2023', 'Royal Mint', 'United Kingdom', GBC),
        E('Euro coin', 'The eurozone coin set: a common side and a national side per issuing state.', '1999', '', 'Eurozone', EUC,
          [V('First series, EU-15 map', '1999-2006'), V('Second series, map of Europe', '2007'), V('Revised 1c, 2c and 5c', '2017'), V('Revised 10c, 20c and 50c', '2023')]),
        E('Euro national sides', 'The national side of euro coins, by issuing state and first year of coins shown.', '1999', '', 'Eurozone', EUC,
          [V(c, '1999') for c in ('Belgium', 'Finland', 'France', 'Netherlands', 'Spain')] + [V('Monaco', '2001')] +
          [V(c, '2002') for c in ('Austria', 'Germany', 'Greece', 'Ireland', 'Italy', 'Luxembourg', 'Portugal', 'San Marino', 'Vatican City')]),
        E('Russian Imperial coinage', 'Coins of the Russian Empire from the first silver rubles of 1704, with platinum rubles of 1828-1845.', '1704', '', 'Russia', RUB,
          [V('Silver ruble', '1704'), V('Platinum 3, 6 and 12 rubles', '1828-1845'), V('Gold 5 and 10 rubles', '1886'), V('Gold suspended', '1911')]),
        E('Russian Federation coinage', 'Coins of the post-Soviet ruble: 1992 issues, then the 1997 series with kopecks and rubles.', '1992', '', 'Russia', RUB,
          [V('1992 ruble coins', '1992'), V('1997 series', '1997', 'revised 2009 and 2016'), V('Bimetallic 10 rubles', '2000')]),
        E('South African decimal coinage', 'South African decimal coins from 1961, with later rand coins and a new series announced for 2023.', '1961', 'South African Mint', 'South Africa', ZAR,
          [V('Cents series', '1961'), V('2 cent replaces 2½ cent', '1965'), V('R1', '1967'), V('R2', '1989'), V('R5', '1994'), V('Bimetallic R5', '2004'), V('Fourth decimal series', '2023')]),
        E('Swiss franc circulation coins', 'Swiss franc coins described by denomination: 20 centimes (1939), half franc (1968), 5 centimes (1981).', '1939', 'Swissmint', 'Switzerland', CHF),
        E('East India Company coinage of 1835', 'Uniform coinage of the East India Company in copper, silver and gold mohurs.', '1835', '', 'India', INR, [V('2 annas', '1841'), V('Half pice', '1853')]),
        E('Indian regal coinage', 'Coins of British India with Victoria and later monarchs.', '1862', '', 'India', INR, [V('Last issue, Indian lion reverse', '1946-1947')]),
        E('Coins of the Republic of India', 'Coins of independent India: pre-decimal, naye paise, aluminium, steel and the 2011 and 2019 series.', '1950', '', 'India', INR,
          [V('Pre-decimal', '1950-1957'), V('Naye paise', '1957'), V('Aluminium', '1964'), V('Ferritic steel', '2005-2008'), V('Rupee-sign series', '2011'), V('Bimetallic ₹20 and 2019 series', '2019')]),
        E('Renminbi coins', 'People\'s Republic of China coins, in series by introduction year.', '1955', 'China Mint', 'China', CNY,
          [V('Aluminium fen', '1955'), V('Brass jiao and cupro-nickel yuan', '1980-1985'), V('1991 coinage', '1991'), V('1999-2002 redesign', '1999'), V('Updated jiao, half yuan and yuan', '2019')]),
        E('Meiji yen coinage', 'First yen coins: gold and silver pieces of 1870, copper sen and bronze rin of 1873.', '1870', 'Japan Mint', 'Japan', JPY,
          [V('Gold yen and silver sen', '1870'), V('Copper sen and bronze rin', '1873'), V('Cupronickel 5 sen', '1889'), V('Reduced gold coins', '1897')]),
        E('Postwar yen coins', 'Japanese coins from 1946, from brass 50 sen to cupronickel 100 and 500 yen.', '1946', 'Japan Mint', 'Japan', JPY,
          [V('Holed 5 yen', '1949'), V('Bronze 10 yen', '1951'), V('Aluminium 1 yen', '1955'), V('Silver 100 yen', '1957'), V('Cupronickel 100 yen', '1967'), V('Cupronickel 500 yen', '1982')]),
        E('Australian pre-decimal coinage', 'Halfpenny, penny, threepence, sixpence, shilling, florin and crown before 1966.', '1910', '', 'Australia', AUC),
        E('Australian decimal coinage', 'Coins of 1966 with Stuart Devlin reverses: feathertail glider, lizard, echidna, lyrebird, platypus, arms, kangaroos.', '1966', 'Royal Australian Mint', 'Australia', AUC,
          [V('1c feathertail glider', '1966'), V('5c echidna', '1966'), V('50c arms, 12-sided', '1969'), V('$1 five kangaroos', '1984'), V('$2 Aboriginal elder', '1988')]),
    ]
    add(k, new)
    # Japanese yen m (500 yen coin versions) absorbed
    k['nl'] = 'One entry is a circulating coin type or series issued by one state, with denominations, metals and redesigns as versions.'
    k['sel'] = ("Series by issuer for the issuers whose coin articles were fetched: Wikipedia's coin and currency articles for the United States, United Kingdom, euro area, Canada, Australia, Japan, "
                "Mexico, Brazil, Russia, South Africa, India, China and Switzerland, plus the earlier catalogue-pass historic types (Numista); other issuers are not yet covered.")
    k['xg'] = 'by issuer, then era'
    order(k, ISSUERS)

    k = kind(d, 'Circulating commemorative coin')
    gm = {'50 State quarters': 'United States', '2 euro commemorative coins': 'Eurozone', '47 Prefectures coins': 'Japan', 'US Bicentennial coinage': 'United States',
          'Westward Journey nickels': 'United States', 'Lincoln Bicentennial cents': 'United States', 'Canadian Centennial coins': 'Canada',
          'Canada 150 coins': 'Canada', 'Commemorative loonies': 'Canada'}
    setg(k, gm)
    add(k, [E('America the Beautiful quarters', 'US quarter series of 2010-2021 with national sites on the reverse.', '2010', 'United States Mint', 'United States', USC),
            E('American Women quarters', 'US quarter series of 2022-2025.', '2022', 'United States Mint', 'United States', USC),
            E('Semiquincentennial coins', 'US dime, quarter and half dollar issues for 2026.', '2026', 'United States Mint', 'United States', USC),
            E('District of Columbia and US Territories quarters', 'US quarters of 2009.', '2009', 'United States Mint', 'United States', USC),
            E('German Bundesländer 2 euro series', 'German 2 euro commemoratives: Bundesländer I (2006-2022), Bundesländer II (2023-2038), Unity, Justice and Freedom (from 2025).', '2006', '', 'Eurozone', EUC),
            E('Spanish UNESCO 2 euro series', 'Spanish 2 euro series on World Heritage Sites, begun 2010 and planned to 2058.', '2010', '', 'Eurozone', EUC),
            E('French Olympics 2 euro series', 'French 2 euro commemoratives for the 2024 Summer Olympics.', '2021', '', 'Eurozone', EUC),
            E('Australian commemorative 50 cent coins', 'Commemorative 50c coins have circulated since 1970.', '1970', 'Royal Australian Mint', 'Australia', AUC),
            E('Russian 25-ruble Olympic coins', 'Circulating 25-ruble Olympic commemoratives, from 2011.', '2011', '', 'Russia', RUB)])
    # promote maker-named m: Latvian, Maltese series etc. (Numista pass)
    promote_m(k, REP, s_override='https://en.numista.com/catalogue/index.php')
    for x in k['x']:
        if not x.get('g') or x['g'] == x.get('mk'): x['g'] = 'Other issuers'
    k['nl'] = 'One entry is a circulating commemorative coin programme or issue by one state; denominations are versions.'
    k['sel'] = 'Programmes named in the fetched Wikipedia coin articles for the United States, euro area, Canada, Australia and Russia, plus the earlier catalogue-pass programmes.'
    k['xg'] = 'by issuer'
    order(k, ISSUERS + ['Eurozone'])

    for n in ('Collector coin', 'Proof or mint set'):
        k = kind(d, n)
        promote_m(k, REP, s_override='https://en.numista.com/catalogue/index.php')
        for x in k['x']:
            x['g'] = x.get('g') or x.get('mk') or ''
        k['nl'] = 'One entry is a collector coin or set programme of a mint, sold above face value; years, metals and finishes are versions.'
        k['sel'] = 'No whole-space reference exists; the earlier catalogue pass named these programmes and the maker-named models were promoted.'
        k['xg'] = 'by issuing mint'

# ---------------- banknotes ----------------
def notes(d):
    k = kind(d, 'Circulation banknote')
    gm = {'Bank of England notes': 'United Kingdom', 'Federal Reserve Note': 'United States', 'United States Treasury notes': 'United States',
          'Euro banknotes': 'Eurozone', 'Renminbi series': 'China', 'Bank of Japan series': 'Japan', 'Swiss National Bank series': 'Switzerland',
          'Bank of Canada series': 'Canada', 'Australian decimal notes': 'Australia', 'Banxico families': 'Mexico', 'Zimbabwe dollar notes': 'Zimbabwe'}
    setg(k, gm)
    add(k, [
        E('South African banknote series', 'Eight South African note series from 1961: Van Riebeeck, Big Five, Mandela and Big 5 Families.', '1961', 'South African Reserve Bank', 'South Africa', ZAR,
          [V('First series', '1961'), V('Second', '1966'), V('Third', '1978'), V('Fourth, Big Five', '1992'), V('Fifth, Big Five', '2005'), V('Sixth, Mandela', '2012'), V('Seventh, Mandela Centenary', '2018'), V('Eighth, Big 5 Families', '2023')]),
        E('Russian banknotes', 'Russian paper money from assignation rubles to the 1997 Bank of Russia series.', '1769', '', 'Russia', RUB,
          [V('Assignation rubles', '1769'), V('State credit notes', '1843'), V('Soviet 1961 series', '1961'), V('1992 Bank of Russia notes', '1992'), V('1997 series', '1998', 'released 1 January 1998')]),
        E('Brazilian real banknotes', 'Two note series of the real: 1994-2010 and from 2010.', '1994', '', 'Brazil', BRL,
          [V('First series', '1994'), V('Polymer 10 reais commemorative', '2000'), V('Second series', '2010'), V('200 real note', '2020')]),
        E('Indian banknotes', 'First notes of independent India, the Lion Capital series of 1949, and later rupee notes.', '1949', 'Reserve Bank of India', 'India', INR,
          [V('1 rupee Lion Capital', '1949'), V('500 rupees', '1987'), V('1,000 rupees', '2000')]),
    ])
    # renminbi / swiss versions from fetched pages
    for x in k['x']:
        have = {v['n'] for v in x.get('v', [])}
        if x['n'] == 'Renminbi series' and 'Fifth series' not in have:
            x.setdefault('v', []).append(V('Fifth series', '1999', 'dated 2005, 2015 and 2019'))
    promote_m(k, REP, s_override='https://en.numista.com/catalogue/index.php')
    for x in k['x']:
        if not x.get('g') or x['g'] == x.get('mk'): x['g'] = 'Other issuers'
    k['nl'] = 'One entry is a banknote family or series of one issuer, with denominations or redesigns as versions.'
    k['sel'] = 'Series for the issuers whose Wikipedia currency articles were fetched (United Kingdom, United States, euro area, China, Japan, Switzerland, Canada, Australia, Mexico, South Africa, Russia, Brazil, India), plus the earlier catalogue-pass issuers.'
    k['xg'] = 'by issuer, then era'
    order(k, ISSUERS + ['Zimbabwe'])
    for n in ('Commemorative banknote', 'Collector banknote', 'Private and local bank note', 'Emergency scrip and Notgeld'):
        kk = kind(d, n)
        promote_m(kk, REP, s_override='https://en.numista.com/catalogue/index.php')
        for x in kk.get('x', []):
            x['g'] = x.get('g') or x.get('mk') or 'Other issuers'
        if kk.get('x'):
            kk['nl'] = 'One entry is a banknote series or issue of one issuer; denominations and printings are versions.'
            kk['sel'] = 'No whole-space reference exists; entries come from the earlier catalogue pass (Numista and the issuing banks).'
            kk['xg'] = 'by issuer'
    for n in ('Military and occupation currency', 'Specimen note', 'Replica, prop or counterfeit note'):
        kk = kind(d, n)
        promote_m(kk, REP)
        kk['nl'] = 'One entry is a named issue of military, specimen or imitation paper money; denominations are versions.'
        kk['sel'] = 'No whole-space reference exists; entries are the issues named in the earlier catalogue pass.'

def run(d):
    bullion(d); bars_rounds(d); circ(d); notes(d)
    return REP
