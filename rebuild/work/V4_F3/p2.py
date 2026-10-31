from lib import *

REP = []
ST = WP + 'List_of_notable_postage_stamps'
UKO = WP + 'Orders,_decorations,_and_medals_of_the_United_Kingdom'
USA = WP + 'Awards_and_decorations_of_the_United_States_Armed_Forces'
FRA = WP + 'Orders,_decorations,_and_medals_of_France'
SOV = WP + 'Orders,_decorations,_and_medals_of_the_Soviet_Union'
JPN = WP + 'Orders,_decorations,_and_medals_of_Japan'
GER = WP + 'Orders,_decorations,_and_medals_of_Germany'

def S(n, g, y='', d='', v=None, role=None, a=''):
    return E(n, d or 'Stamp named in the list of notable postage stamps.', y=y, g=g, s=ST, v=v, role=role, a=a)

def stamps(d):
    # ---- definitives and first issues
    k = kind(d, 'Definitive stamp')
    gm = {'Penny Black': 'United Kingdom', 'Two Penny Blue': 'United Kingdom', 'Penny Red': 'United Kingdom', 'Penny Lilac': 'United Kingdom',
          'Basel Dove': 'Switzerland', "Bull's Eye": 'Brazil', 'Mauritius "Post Office"': 'Mauritius', 'Hawaiian Missionaries': 'Hawaii',
          'Cape Triangular': 'Cape of Good Hope', 'Large Queens': 'Canada', 'Small Queens': 'Canada', 'Admiral issue': 'Canada',
          'Germania': 'Germany', 'Semeuse': 'France', 'Marianne': 'France', 'Washington–Franklin Issues': 'United States',
          'Presidential Issue (Prexies)': 'United States', 'Liberty Issue': 'United States', 'Wilding series': 'United Kingdom',
          'Machin series': 'United Kingdom', 'Chalon head': 'Victoria (Australia)', 'Uganda Cowries': 'Uganda', 'Scinde Dawk': 'India'}
    setg(k, gm)
    for x in k['x']:
        if x['n'] == 'Penny Black': x['role'] = 'origin'
        if x['n'] == 'Scinde Dawk': x['role'] = 'origin'
        if x['n'] in ('Penny Black', 'Two Penny Blue', "Bull's Eye", 'Basel Dove', 'Mauritius "Post Office"', 'Uganda Cowries', 'Scinde Dawk', 'Penny Red', 'Penny Lilac'):
            x['s'] = ST
    # promote loose definitive models
    promote_m(k, REP, s_override='https://en.wikipedia.org/wiki/Postage_stamp')
    for x in k['x']:
        x['g'] = x.get('g') or x.get('mk') or 'Other administrations'
    new = [
        S('Ceres', 'France', '', "France's first stamp.", role='origin'),
        S('Leopold with the Epaulettes', 'Belgium', '1849', "Belgium's first stamp series, named for the king's epaulettes."),
        S('Canada 12d black', 'Canada', '', 'Early Canadian stamp named in the notable-stamps list.'),
        S('One kreuzer black', 'Bavaria', '1849', 'First German postage stamp, issued in Bavaria.', role='origin'),
        S('Sachsen 3 Pfennige red', 'Saxony', '', 'Second German state stamp; Saxony was the second state to issue.'),
        S('Yacht issue', 'Germany', '', 'Common design used for the German colonies.'),
        S('Zürich 4 and 6', 'Switzerland', '', 'Early Swiss cantonal stamps.'),
        S('Double Geneva', 'Switzerland', '', 'Early Swiss cantonal stamp.'),
        S('Halfpenny Yellow', 'Malta', '1860', "Malta's first stamp."),
        S('Melita issue', 'Malta', '1922', 'Issue commemorating Malta\'s self-government, 1922-26.'),
        S('Moldavian Bull\'s Heads', 'Romania', '1858', 'Stamps of the principality of Moldavia.'),
        S('First stamp of the Russian Empire', 'Russia', '1857', "The empire's first stamp."),
        S('Edward VII 2d Tyrian plum', 'United Kingdom', '1910', 'Withdrawn before issue, though one was used.'),
        S('Postal Union Congress £1', 'United Kingdom', '1929', 'High-value issue named in the notable-stamps list.'),
        S('Irish 2d coil stamp', 'Ireland', '1935', 'Coil stamp named in the notable-stamps list.'),
        S('Gronchi Rosa', 'Italy', '', 'Italian stamp named in the notable-stamps list.'),
        S('Jamaica 1956-58 £1 chocolate and violet', 'Jamaica', '1956', 'High-value Jamaican definitive.'),
        S('St. Louis Bears', 'United States', '1845', 'US postmaster\'s provisional of St Louis.'),
        S('New York Postmaster\'s Provisional', 'United States', '1845', 'US postmaster\'s provisional.'),
        S('Alexandria "Blue Boy"', 'United States', '1847', 'Alexandria postmaster\'s provisional; unique, and an entire.'),
        S('Lady McLeod', 'Trinidad', '', 'Private local post stamp.'),
        S('Black Swan', 'Western Australia', '', 'Early Western Australian stamp.'),
        S('Dull Rose', 'Ceylon', '1859', 'Ceylon\'s 4 pence stamp, considered its most valuable.'),
        S('Sicilian Error of Color', 'Kingdom of the Two Sicilies', '', 'Colour error of the Two Sicilies.'),
        S('Vineta provisional', 'Germany', '', 'Unauthorised provisional issue.'),
        S('Moldavia Bull\'s Heads', 'Romania', '1858', ''),
    ]
    new = [e for e in new if e['n'] != "Moldavia Bull's Heads"]
    add(k, new)
    for x in k['x']:
        if x['n'] == 'Penny Black': pass
    k['nl'] = 'One entry is a definitive or first-issue stamp series of one postal administration; printings and papers are versions.'
    k['sel'] = ("Famous issues from Wikipedia's List of notable postage stamps that are first or regular issues, plus the definitive series of major administrations "
                "from the earlier catalogue pass; definitive series of other administrations are not yet covered.")
    k['xg'] = 'by postal administration'
    order(k, sorted({x['g'] for x in k['x']}))

    # ---- errors, varieties and rarities
    k = kind(d, 'Stamp error and variety')
    gm = {'Inverted Jenny': 'United States', 'Treskilling Yellow': 'Sweden', 'British Guiana 1c magenta': 'British Guiana',
          'Inverted Swan': 'Western Australia', 'Dag Hammarskjöld invert': 'United States', 'Baden 9 kreuzer error': 'Baden',
          'Whole Country is Red': 'China'}
    setg(k, gm)
    for x in k['x']:
        if x['n'] in ('Inverted Jenny', 'Treskilling Yellow', 'British Guiana 1c magenta'):
            x['role'] = 'landmark'; x['s'] = ST
        if x['n'] in ('Inverted Swan', 'Dag Hammarskjöld invert', 'Baden 9 kreuzer error', 'Whole Country is Red'): x['s'] = ST
    add(k, [
        S('Inverted Dendermonde', 'Belgium', '1920', 'Inverted-design error.'),
        S('Inverted Head Four Annas', 'India', '', 'Error stamp with an inverted head.'),
        S('Jamaica 1 shilling inverted frame', 'Jamaica', '', 'Frame-inversion error.'),
        S('Pan-American invert', 'United States', '1901', 'Printing error.'),
        S('Pagsanjan Falls', 'United States', '1932', 'Printing error.'),
        S('CIA invert', 'United States', '1979', 'Modern error.'),
        S('Legends of the West error', 'United States', '1994', 'Printing error showing the wrong individual.'),
        S('Statue of Liberty Forever stamp', 'United States', '2011', 'Largest run of an error on a US stamp, at 10.5 billion.'),
        S('1c Z grill', 'United States', '1868', 'The rarest US stamp.'),
        S('Lost Continental', 'United States', '1875', '24c Winfield Scott stamp.'),
        S('Black Bull', 'United States', '1898', 'The dollar value of the 1898 Trans-Mississippi Issue.'),
        S('HMS Glasgow error', 'Falkland Islands', '', 'Error stamp.'),
        S('70r Red Army Soldier error', 'Russia', '1922', 'Perforation error; four imperforate specimens are known.'),
        S('Lake Taupo 4d invert', 'New Zealand', '1904', 'Only one copy is known.'),
        S('Canada 2c Large Queen on laid paper', 'Canada', '', 'The rarest Canadian stamp.'),
        S('Buenos Aires 1p "In Ps" tête-bêche pair', 'State of Buenos Aires', '1859', 'Tête-bêche pair.'),
        S('Ferrer block of 15', 'Uruguay', '1856', 'Unique block of the 80c green.'),
    ])
    for x in k['x']:
        if not x.get('g'): x['g'] = 'Other administrations'
    k['nl'] = 'One entry is a named stamp error, variety or rarity; the sheet position or printing is a version where the list gives it.'
    k['sel'] = "Error and rarity entries of Wikipedia's List of notable postage stamps, plus the earlier catalogue-pass errors; the list is complete for its scope."
    k['xg'] = 'by postal administration'
    order(k, sorted({x['g'] for x in k['x']}))

    # ---- commemoratives, official, revenue, cinderella, essays
    k = kind(d, 'Commemorative stamp')
    setg(k, {'Columbian Issue': 'United States', 'Zeppelin issues': 'United States'})
    add(k, [S('Saint Paul 10s black', 'Malta', '1919', 'One of Malta\'s rarest stamps.'),
            S('Jamaica 6d abolition of slavery', 'Jamaica', '', 'Commemorates the abolition of slavery.'),
            S('Jamaica 1968 human rights stamps', 'Jamaica', '1968', 'Human rights commemoratives.'),
            S('Golden Monkey', 'China', '1980', 'Chinese zodiac stamp.')])
    promote_m(k, REP, s_override='https://en.wikipedia.org/wiki/Postage_stamp')
    for x in k['x']: x['g'] = x.get('g') or x.get('mk') or 'Other administrations'
    k['nl'] = 'One entry is a commemorative stamp or set of one postal administration.'
    k['sel'] = 'Commemoratives named in the List of notable postage stamps and the earlier catalogue pass.'
    k['xg'] = 'by postal administration'
    k = kind(d, 'Official stamp')
    setg(k, {'VR official': 'United Kingdom', 'US departmental stamps': 'United States'})
    add(k, [S('Indian 10 rupee Gandhi service stamp', 'India', '', 'Ten rupee Mahatma Gandhi stamp overprinted SERVICE.')])
    k['nl'] = 'One entry is an official or service stamp issue.'
    k['sel'] = 'Official issues named in the List of notable postage stamps and the earlier catalogue pass.'
    k['xg'] = 'by postal administration'
    k = kind(d, 'Revenue stamp')
    add(k, [S('Red Revenues', 'China', '1897', 'Provisional stamps issued under the Qing dynasty.')])
    promote_m(k, REP, s_override='https://en.wikipedia.org/wiki/Revenue_stamp')
    for x in k['x']: x['g'] = x.get('g') or x.get('mk') or 'Other administrations'
    for x in k['x']:
        if x['n'] == 'Federal Duck Stamp': x['g'] = 'United States'
    k['nl'] = 'One entry is a revenue, fiscal or duty stamp issue.'
    k['sel'] = 'Revenue issues named in the List of notable postage stamps and the earlier catalogue pass.'
    k['xg'] = 'by authority'
    k = kind(d, 'Cinderella and poster stamp')
    add(k, [S('Prince Consort Essay', 'United Kingdom', '1851', "Printer's sample, surface-printed.")])
    k['nl'] = 'One entry is a non-postal stamp such as a seal, local-post or poster stamp, or a stamp essay.'
    k['sel'] = 'Entries from the earlier catalogue pass and the List of notable postage stamps; no whole-space reference exists for cinderellas.'
    k['xg'] = 'by origin'
    for x in k['x']: x['g'] = x.get('g') or 'Other'
    for n in ('Airmail stamp', 'Postage due stamp', 'Souvenir sheet'):
        kk = kind(d, n)
        promote_m(kk, REP, s_override='https://en.wikipedia.org/wiki/Postage_stamp')
        for x in kk['x']: x['g'] = x.get('g') or x.get('mk') or 'Other administrations'
        kk['nl'] = 'One entry is a named issue of this stamp type.'
        kk['sel'] = 'Entries from the earlier catalogue pass; no whole-space reference exists.'
        kk['xg'] = 'by postal administration'
    kk = kind(d, 'Stamp booklet')
    promote_m(kk, REP, s_override='https://en.wikipedia.org/wiki/Postage_stamp')
    for x in kk['x']: x['g'] = x.get('g') or x.get('mk') or 'Other administrations'
    kk['nl'] = 'One entry is a named booklet series.'
    kk['sel'] = 'Maker-named booklet series from the earlier catalogue pass; no whole-space reference exists.'
    kk['xg'] = 'by postal administration'
    for n in ('Postal history cover', 'First-day cover', 'Flight and rocket cover', 'Postmark and cancellation', 'Stamped envelope', 'Postal card', 'Aerogram', 'Newspaper wrapper'):
        kk = kind(d, n)
        promote_m(kk, REP, s_override='https://en.wikipedia.org/wiki/Postal_history')
        for x in kk.get('x', []): x['g'] = x.get('g') or x.get('mk') or ''
        if kk.get('x'):
            kk['nl'] = 'One entry is a named cover type, postmark, series of postal stationery or event cover.'
            kk['sel'] = 'No whole-space reference exists for postal history; entries come from the earlier catalogue pass.'

# ---------------- orders, decorations & medals ----------------
def O(n, g, y, d, s, v=None, role=None):
    return E(n, d, y=y, g=g, s=s, v=v, role=role)

def medals(d):
    k = kind(d, 'Order of chivalry or state order')
    # disambiguate nothing yet; set g on existing
    gm = {'Order of the Garter': 'United Kingdom', 'Order of the Bath': 'United Kingdom', 'Order of St Michael and St George': 'United Kingdom',
          'Royal Victorian Order': 'United Kingdom', 'Order of the British Empire': 'United Kingdom', 'Legion of Honour': 'France',
          'Pour le Mérite': 'Germany', 'Order of the Red Eagle': 'Germany', 'Order of Saint George': 'Russia', 'Order of Lenin': 'Soviet Union',
          'Order of the Red Star': 'Soviet Union', 'Order of the Patriotic War': 'Soviet Union', 'Order of the Rising Sun': 'Japan',
          'Order of the Sacred Treasure': 'Japan', 'Order of the Golden Fleece': 'Spain and Austria', 'Order of the Elephant': 'Denmark'}
    setg(k, gm)
    new = [
        O('Order of the Thistle', 'United Kingdom', '1687', 'Scottish order of chivalry.', UKO),
        O('Order of Merit', 'United Kingdom', '1902', 'British order of merit.', UKO),
        O('Order of the Companions of Honour', 'United Kingdom', '1917', 'British order for national service.', UKO),
        O('Imperial Service Order', 'United Kingdom', '1902', 'British order for civil servants.', UKO),
        O('Order of St John', 'United Kingdom', '1888', 'Most Venerable Order of the Hospital of St John of Jerusalem.', UKO),
        O('Order of St Patrick', 'United Kingdom', '1783', 'Irish order, dormant.', UKO),
        O('Order of the Star of India', 'United Kingdom', '1861', 'Order of British India, dormant.', UKO),
        O('Order of the Indian Empire', 'United Kingdom', '1878', 'Order of British India, dormant.', UKO),
        O('Imperial Order of the Crown of India', 'United Kingdom', '1878', 'Order for women of British India, dormant.', UKO),
        O('Order of Burma', 'United Kingdom', '1940', 'Order of British Burma, dormant.', UKO),
        O('Royal Guelphic Order', 'United Kingdom', '1815', 'Hanoverian order no longer associated with the British monarch.', UKO),
        O('National Order of Merit', 'France', '', 'French national order.', FRA),
        O('Order of Liberation', 'France', '', 'French national order.', FRA),
        O('Order of Academic Palms', 'France', '', 'French ministerial order.', FRA),
        O('Order of Arts and Letters', 'France', '', 'French ministerial order.', FRA),
        O('Order of Agricultural Merit', 'France', '', 'French ministerial order.', FRA),
        O('Order of Maritime Merit', 'France', '', 'French ministerial order.', FRA),
        O('Order of Tahiti Nui', 'France', '', 'French territorial order.', FRA),
        O('Order of the Holy Spirit', 'France', '', 'Royal order, abolished or dormant.', FRA),
        O('Order of Saint Michael', 'France', '', 'Royal order, abolished or dormant.', FRA),
        O('Order of Saint Louis', 'France', '', 'Royal order, abolished or dormant.', FRA),
        O('Order of the Federal Republic of Germany', 'Germany', '', 'Order of Merit of the Federal Republic of Germany, the federal order.', GER),
        O('Bavarian Maximilian Order for Science and Art', 'Germany', '', 'Bavarian order.', GER),
        O('Order of Victory', 'Soviet Union', '1943', 'Soviet military order.', SOV),
        O('Order of the Red Banner', 'Soviet Union', '1918', 'Soviet military order.', SOV),
        O('Order of Alexander Nevsky', 'Soviet Union', '1942', 'Soviet military order.', SOV),
        O('Order of Suvorov', 'Soviet Union', '1942', 'Soviet military order in three classes.', SOV),
        O('Order of Kutuzov', 'Soviet Union', '1942', 'Soviet military order; 3rd class 1943.', SOV),
        O('Order of Bogdan Khmelnitsky', 'Soviet Union', '1943', 'Soviet military order in three classes.', SOV),
        O('Order of Glory', 'Soviet Union', '1943', 'Soviet military order in three classes.', SOV),
        O('Order of Ushakov', 'Soviet Union', '1944', 'Soviet naval order.', SOV),
        O('Order of Nakhimov', 'Soviet Union', '1944', 'Soviet naval order.', SOV),
        O('Order for Service to the Homeland in the Armed Forces of the USSR', 'Soviet Union', '1974', 'Soviet military order in three classes.', SOV),
        O('Order of the October Revolution', 'Soviet Union', '1967', 'Soviet military and civil order.', SOV),
        O('Order of Friendship of Peoples', 'Soviet Union', '1972', 'Soviet military and civil order.', SOV),
        O('Order of the Red Banner of Labour', 'Soviet Union', '1928', 'Soviet civil order.', SOV),
        O('Order of the Badge of Honour', 'Soviet Union', '1935', 'Soviet civil order.', SOV),
        O('Order of Maternal Glory', 'Soviet Union', '1944', 'Soviet civil order in three classes.', SOV),
        O('Order of Labour Glory', 'Soviet Union', '1974', 'Soviet civil order in three classes.', SOV),
        O('Order for Personal Courage', 'Soviet Union', '1988', 'Soviet civil order.', SOV),
        O('Supreme Order of the Chrysanthemum', 'Japan', '1876', 'Highest Japanese order.', JPN),
        O('Order of the Paulownia Flowers', 'Japan', '1888', 'Established as a Special Grand Cordon of the Rising Sun; separate order from 2003.', JPN),
        O('Order of Culture', 'Japan', '1937', 'Japanese order for cultural achievement.', JPN),
        O('Order of the Precious Crown', 'Japan', '1888', 'Japanese order in classes named Peony, Butterfly, Wisteria, Apricot and Ripple.', JPN),
        O('Medals of Honour', 'Japan', '1881', 'Japanese medals with six ribbon colours: red, green, yellow, purple, blue, dark blue.', JPN),
    ]
    for x in k['x']:
        if x['n'] == 'Order of the Rising Sun': x['y'] = '1875'; x['s'] = JPN
        if x['n'] == 'Order of the Sacred Treasure': x['y'] = x.get('y') or '1888'; x['s'] = JPN
        if x['n'] == 'Order of the Garter': x['y'] = '1348'; x['s'] = UKO; x['role'] = 'origin'
        if x['n'] == 'Order of the Bath': x['y'] = '1725'
        if x['n'] == 'Order of Lenin': x['y'] = '1930'
    add(k, new)
    promote_m(k, REP, s_override=UKO)
    for x in k['x']:
        if x['n'] == 'Order of the Chrysanthemum': x['n'] = 'Order of the Chrysanthemum'
        x['g'] = x.get('g') or x.get('mk') or 'Other'
    k['nl'] = 'One entry is a state order or order of chivalry of one country, with its classes as versions.'
    k['sel'] = ("By country from the fetched Wikipedia lists: United Kingdom, France, Germany (federal and Bavarian orders only; the page indexes other articles), Soviet Union, Japan; "
                "United States has no orders. Other countries are not yet covered.")
    k['xg'] = 'by country'
    order(k, ['United Kingdom', 'France', 'Germany', 'Soviet Union', 'Russia', 'Japan', 'Spain and Austria', 'Denmark', 'Other'])

    # gallantry and merit decorations
    k = kind(d, 'Gallantry and merit decoration')
    for x in k['x']:
        if x['n'] == 'Distinguished Service Cross' and 'United_Kingdom' in x.get('s', ''):
            x['n'] = 'Distinguished Service Cross (United Kingdom)'
        elif x['n'] == 'Distinguished Service Cross':
            x['n'] = 'Distinguished Service Cross (United States)'
    gm = {'Victoria Cross': 'United Kingdom', 'George Cross': 'United Kingdom', 'Distinguished Service Order': 'United Kingdom',
          'Distinguished Service Cross (United Kingdom)': 'United Kingdom', 'Albert Medal': 'United Kingdom', 'Medal of Honor': 'United States',
          'Distinguished Service Cross (United States)': 'United States', 'Navy Cross': 'United States', 'Silver Star': 'United States',
          'Legion of Merit': 'United States', 'Bronze Star Medal': 'United States', 'Purple Heart': 'United States',
          'Médaille militaire': 'France', 'Croix de guerre 1914–1918': 'France', 'Iron Cross': 'Germany', 'Hero of the Soviet Union': 'Soviet Union',
          'Order of the Golden Kite': 'Japan'}
    setg(k, gm)
    for x in k['x']:
        if x['n'] == 'Victoria Cross': x['y'] = '1856'; x['s'] = UKO; x['role'] = 'landmark'
        if x['n'] == 'George Cross': x['y'] = '1940'; x['s'] = UKO
        if x['n'] == 'Medal of Honor': x['role'] = 'landmark'; x['s'] = USA
        if x['n'] == 'Distinguished Service Order': x['y'] = '1886'; x['s'] = UKO
        if x['n'] in ('Navy Cross', 'Silver Star', 'Legion of Merit', 'Bronze Star Medal', 'Purple Heart', 'Distinguished Service Cross (United States)'): x['s'] = USA
        if x['n'] == 'Hero of the Soviet Union': x['y'] = '1934'; x['s'] = SOV
    new = [
        O('Conspicuous Gallantry Cross', 'United Kingdom', '1993', 'British decoration for gallantry.', UKO),
        O('Royal Red Cross', 'United Kingdom', '1883', 'British decoration for nursing.', UKO),
        O('Military Cross', 'United Kingdom', '1914', 'British decoration for gallantry.', UKO),
        O('Distinguished Flying Cross (United Kingdom)', 'United Kingdom', '1918', 'British decoration for aerial gallantry.', UKO),
        O('Air Force Cross (United Kingdom)', 'United Kingdom', '1918', 'British decoration for aerial gallantry.', UKO),
        O('Indian Order of Merit', 'United Kingdom', '1837', 'British Indian decoration, inactive.', UKO),
        O('Kaisar-i-Hind Medal', 'United Kingdom', '1900', 'British Indian public service medal, inactive.', UKO),
        O('George Medal', 'United Kingdom', '', 'British medal for gallantry.', UKO),
        O('Distinguished Conduct Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('Conspicuous Gallantry Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('Distinguished Service Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('Military Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('Distinguished Flying Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('Air Force Medal', 'United Kingdom', '', 'British medal, in abeyance.', UKO),
        O('British Empire Medal', 'United Kingdom', '', 'Medal incorporated into the Order of the British Empire in 2012.', UKO),
        O('Elizabeth Cross', 'United Kingdom', '2009', 'Memorial emblem approved in 2009.', UKO),
        O('Air Force Cross (United States)', 'United States', '', 'US personal decoration.', USA),
        O('Coast Guard Cross', 'United States', '', 'US personal decoration.', USA),
        O('Distinguished Flying Cross (United States)', 'United States', '', 'US personal decoration.', USA),
        O('Soldier\'s Medal', 'United States', '', 'US personal decoration for non-combat heroism.', USA),
        O('Navy and Marine Corps Medal', 'United States', '', 'US personal decoration.', USA),
        O('Airman\'s Medal', 'United States', '', 'US personal decoration.', USA),
        O('Coast Guard Medal', 'United States', '', 'US personal decoration.', USA),
        O('Air Medal', 'United States', '', 'US personal decoration.', USA),
        O('Aerial Achievement Medal', 'United States', '', 'US personal decoration.', USA),
        O('Meritorious Service Medal (United States)', 'United States', '', 'US personal decoration.', USA),
        O('Defense Distinguished Service Medal', 'United States', '', 'US personal decoration.', USA),
        O('Defense Superior Service Medal', 'United States', '', 'US personal decoration.', USA),
        O('Army Commendation Medal', 'United States', '', 'US personal decoration.', USA),
        O('Army Achievement Medal', 'United States', '', 'US personal decoration.', USA),
        O('Combat Action Ribbon', 'United States', '', 'US Navy combat action ribbon.', USA),
        O('Military Medal (France)', 'France', '', 'French military decoration.', FRA),
        O('Croix de guerre 1939–1945', 'France', '', 'French war cross for 1939-1945.', FRA),
        O('Cross for Military Valour', 'France', '', 'French military decoration.', FRA),
        O('Resistance Medal', 'France', '', 'French military decoration.', FRA),
        O('Aeronautical Medal', 'France', '', 'French military decoration.', FRA),
        O('Medal for the War Wounded', 'France', '', 'French military decoration.', FRA),
        O('Honour medal for courage and devotion', 'France', '', 'French reward for acts of courage.', FRA),
        O('Medal for Courage (Soviet Union)', 'Soviet Union', '1938', 'Soviet military medal.', SOV),
        O('Medal for Battle Merit', 'Soviet Union', '1938', 'Soviet military medal.', SOV),
        O('Ushakov Medal', 'Soviet Union', '1944', 'Soviet naval medal.', SOV),
        O('Nakhimov Medal', 'Soviet Union', '1944', 'Soviet naval medal.', SOV),
        O('Partisan of the Patriotic War medal', 'Soviet Union', '1943', 'Soviet medal in two classes.', SOV),
        O('Hero of Socialist Labour', 'Soviet Union', '1938', 'Soviet honorary title.', SOV),
        O('Marshal\'s Star', 'Soviet Union', '1940', 'Soviet honorary title.', SOV),
        O('Mother Heroine', 'Soviet Union', '1944', 'Soviet honorary title.', SOV),
    ]
    add(k, new)
    promote_m(k, REP, s_override=UKO)
    k['m'] = []
    for x in k['x']:
        x['g'] = x.get('g') or x.get('mk') or 'Other'
    k['nl'] = 'One entry is a gallantry, merit or honorary distinction of one country, with its classes as versions.'
    k['sel'] = ("By country from the fetched lists: United Kingdom decorations and medals, United States personal decorations (current awards), France military decorations, "
                "Soviet honorary titles and military medals; Germany is an index page only.")
    k['xg'] = 'by country'
    order(k, ['United Kingdom', 'United States', 'France', 'Germany', 'Soviet Union', 'Japan', 'Other'])

    k = kind(d, 'Campaign medal')
    setg(k, {}, default='United Kingdom')
    for x in k['x']:
        n = x['n']
        if any(w in n for w in ('Civil War', 'World War I Victory', 'Vietnam', 'theatre')): x['g'] = 'United States'
        if 'Vietnam Service' in n or 'World War I Victory' in n or 'Civil War' in n: x['g'] = 'United States'
    add(k, [
        O('Mexican Border Service Medal', 'United States', '', 'US medal, inactive.', USA),
        O('Spanish Campaign Medal', 'United States', '', 'US Spanish-American War medal, inactive.', USA),
        O('Philippine Campaign Medal', 'United States', '', 'US Philippine-American War medal, inactive.', USA),
        O('Army of Occupation Medal', 'United States', '', 'US post-war occupation medal, inactive.', USA),
        O('Korean Service Medal', 'United States', '', 'US Korean War medal, inactive.', USA),
        O('Afghanistan Campaign Medal', 'United States', '', 'US medal, inactive.', USA),
        O('Iraq Campaign Medal', 'United States', '', 'US medal, inactive.', USA),
        O('Armed Forces Expeditionary Medal', 'United States', '', 'US expeditionary medal.', USA),
        O('Global War on Terrorism Expeditionary Medal', 'United States', '', 'US expeditionary medal.', USA),
        O('American Campaign Medal', 'United States', '', 'US World War II campaign medal.', USA),
        O('Asiatic-Pacific Campaign Medal', 'United States', '', 'US World War II campaign medal.', USA),
        O('European-African-Middle Eastern Campaign Medal', 'United States', '', 'US World War II campaign medal.', USA),
        O('Commemorative medal of the 1859 Italian Campaign', 'France', '1859', 'French commemorative campaign medal.', FRA),
        O('Colonial Medal', 'France', '', 'French commemorative campaign medal.', FRA),
        O('1914–1918 Inter-Allied Victory medal', 'France', '', 'French commemorative medal.', FRA),
        O('Dardanelles campaign medal', 'France', '', 'French commemorative medal.', FRA),
        O('1939–1945 Commemorative war medal', 'France', '', 'French commemorative medal.', FRA),
        O('Indochina Campaign commemorative medal', 'France', '', 'French commemorative medal.', FRA),
        O('Medal for the Defence of Leningrad', 'Soviet Union', '1942', 'Soviet defensive campaign medal.', SOV),
    ])
    promote_m(k, REP, s_override=UKO)
    for x in k['x']: x['g'] = x.get('g') or 'Other'
    k['nl'] = 'One entry is a campaign or commemorative service medal of one country; clasps and bars are versions.'
    k['sel'] = 'By country from the fetched lists: United States inactive campaign medals, France commemorative medals, Soviet defensive campaign medals, and the earlier-pass British medals (the fetched UK page was cut before its campaign section).'
    k['xg'] = 'by country'
    order(k, ['United Kingdom', 'United States', 'France', 'Soviet Union', 'Other'])

    k = kind(d, 'Long-service and good-conduct medal')
    for x in k['x']: x['g'] = 'United Kingdom' if 'Army Long' in x['n'] or 'Territorial' in x['n'] or 'Meritorious' in x['n'] else 'United States'
    add(k, [O('Navy Good Conduct Medal', 'United States', '', 'US good conduct medal of one of the services (Army, Navy, Air Force, Space Force, Marine Corps, Coast Guard).', USA),
            O('Prisoner of War Medal', 'United States', '', 'US service award.', USA)])
    k['nl'] = 'One entry is a long-service or good-conduct medal of one country.'
    k['sel'] = 'The earlier catalogue pass plus the US service awards of the fetched list; no whole-space reference exists.'
    k['xg'] = 'by country'
    for n in ('Life-saving medal', 'Wound badge'):
        kk = kind(d, n)
        for x in kk['x']: x['g'] = 'United Kingdom' if 'Humane' in x['n'] else 'Germany'
        kk['nl'] = 'One entry is a life-saving medal or wound badge of one country.'
        kk['sel'] = 'Entries from the earlier catalogue pass; no whole-space reference exists.'
        kk['xg'] = 'by country'

def run(d):
    stamps(d); medals(d)
    return REP
