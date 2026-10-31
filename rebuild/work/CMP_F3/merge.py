import json, re, os
P = '/home/user/Possession-Taxonomy/rebuild/out/F3.json'
d = json.load(open(P))
W = 'https://en.wikipedia.org/wiki/'

def kinds():
    out = {}
    def walk(o):
        if isinstance(o, dict):
            if 'x' in o and 'nl' in o:
                out[o['n']] = o
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(d)
    return out
K = kinds()

def norm(s):
    s = s.lower()
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r"\b(the|medal|ribbon|order of|of the|of)\b", '', s)
    return re.sub(r'[^a-z0-9]+', '', s)

def key(e):
    return (norm(e['n']), e.get('g', ''))

def add(kind, entries, order_key=None):
    k = K[kind]
    have = {key(e) for e in k['x']}
    haven = {norm(e['n']) for e in k['x']}
    n_add = 0
    for e in entries:
        e.setdefault('a', ''); e.setdefault('mk', ''); e.setdefault('y', '')
        if key(e) in have or (norm(e['n']) in haven and e.get('g') == next((x.get('g') for x in k['x'] if norm(x['n']) == norm(e['n'])), None)):
            continue
        k['x'].append(e); have.add(key(e)); haven.add(norm(e['n'])); n_add += 1
    # stable sort: group order by first appearance of g, then year, then name
    gorder = {}
    for e in k['x']:
        gorder.setdefault(e.get('g', ''), len(gorder))
    def yr(e):
        m = re.search(r'\d{4}', e.get('y', '') or '')
        return int(m.group()) if m else 9999
    k['x'].sort(key=lambda e: (gorder[e.get('g', '')], yr(e), e['n']))
    return n_add

def cov(kind, text):
    k = K[kind]
    k['sel'] = (k.get('sel', '') + ' ' + text).strip()

def V(n, y='', dd=''):
    return {'n': n, 'mk': '', 'y': y, 'd': dd}

def E(n, g, y, dd, s, mk='', v=None):
    e = {'n': n, 'a': '', 'd': dd, 'mk': mk, 'y': y, 's': s, 'g': g}
    if v: e['v'] = v
    return e

counts = {}
before = {n: len(k['x']) for n, k in K.items()}

# ---- circulation coins
S = W
coins = [
 E('Turkish new lira and kuruş coins', 'Turkey', '2009', 'Coins of 1, 5, 10, 25 and 50 kuruş and 1 lira issued from 1 January 2009.', S+'Turkish_lira', 'Central Bank of the Republic of Türkiye',
   [V('1 kuruş', '2008'), V('5 to 50 kuruş', '2009'), V('1 lira', '2009', 'ring and centre alloys swapped from the earlier design')]),
 E('Turkish 5 lira coin', 'Turkey', '2023', 'Coin of 5 lira issued on 29 October 2023.', S+'Turkish_lira', 'Central Bank of the Republic of Türkiye'),
 E('Saudi qirsh and riyal coinage', 'Saudi Arabia', '1925', 'Coins of the Hejaz and Saudi state from copper quarter and half qirsh of 1925 to silver riyals of 1935.', S+'Saudi_riyal', '',
   [V('Copper 1/4 and 1/2 qirsh', '1925'), V('Cupro-nickel qirsh', '1926'), V('Silver 1/4, 1/2 and 1 riyal', '1935'), V('Cupro-nickel 1/4, 1/2 and 1 qirsh', '1937'), V('Cupro-nickel 2 and 4 qirsh', '1957')]),
 E('Saudi halala coinage', 'Saudi Arabia', '1963', 'Halala and riyal coins from the bronze 1 halala of 1963 to the bimetallic riyal of 1999.', S+'Saudi_riyal', '',
   [V('Bronze 1 halala', '1963'), V('Cupro-nickel 5, 10, 25 and 50 halala', '1972'), V('Cupro-nickel 1 riyal', '1976'), V('Bimetallic 1 riyal', '1999')]),
 E('Saudi riyal current coin series', 'Saudi Arabia', '2016', 'Current coins of 1, 5, 10, 25 and 50 halalas and 1 and 2 riyals.', S+'Saudi_riyal'),
 E('Egyptian piastre coins', 'Egypt', '1984', 'Coins of 5, 10, 20, 25 and 50 piastres issued from 1984 to 2022.', S+'Egyptian_pound', 'Central Bank of Egypt',
   [V('5, 10 and 20 piastres', '1984'), V('25 piastres', '1993'), V('50 piastres', '2005')]),
 E('Egyptian pound coin', 'Egypt', '2005', 'Coin of 1 Egyptian pound minted from 2005 to 2022.', S+'Egyptian_pound', 'Central Bank of Egypt'),
 E('Nigerian kobo coins of 1973', 'Nigeria', '1973', 'First decimal coins: half, 1, 5, 10 and 25 kobo.', S+'Nigerian_naira', 'Central Bank of Nigeria',
   [V('1/2 and 1 kobo (bronze)', '1973'), V('5, 10 and 25 kobo (cupro-nickel)', '1973')]),
 E('Nigerian coins of 1991', 'Nigeria', '1991', 'Steel coins of 1, 10 and 25 kobo plus 50 kobo and 1 naira.', S+'Nigerian_naira', 'Central Bank of Nigeria'),
 E('Nigerian coins of 2006', 'Nigeria', '2007', 'Coins of 50 kobo, 1 naira and 2 naira issued on 28 February 2007.', S+'Nigerian_naira', 'Central Bank of Nigeria'),
 E('South Korean won coins of 1966', 'South Korea', '1966', 'Coins of 1, 5, 10, 50 and 100 won issued 1966 to 1972.', S+'South_Korean_won', 'Bank of Korea'),
 E('South Korean won coins of 1982', 'South Korea', '1982', 'Coins of 1 to 100 won standardised in 1983 plus the 500 won of 1982.', S+'South_Korean_won', 'Bank of Korea'),
 E('Current South Korean won coins', 'South Korea', '2006', 'Current coins of 10, 50, 100 and 500 won; the 10 won was redesigned in 2006.', S+'South_Korean_won', 'Bank of Korea'),
 E('Argentine peso first-series coins', 'Argentina', '1992', 'Coins of 1 to 50 centavos and 1 and 2 pesos introduced in 1992.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine peso second-series coins', 'Argentina', '2017', 'Coins of 1, 2, 5 and 10 pesos issued 2017 to 2018.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine commemorative peso coins', 'Argentina', '1994', 'Circulating commemoratives of 50 centavos and 1, 2 and 5 pesos issued 1994 to 2010.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Indonesian rupiah coins of 2016', 'Indonesia', '2016', 'Coins of 100, 200, 500 and 1,000 rupiah that entered circulation on 19 December 2016.', S+'Indonesian_rupiah', 'Bank Indonesia'),
 E('Indonesian 50 rupiah coin', 'Indonesia', '1999', 'Coin of 50 rupiah issued in 1999 and still legal tender.', S+'Indonesian_rupiah', 'Bank Indonesia'),
 E('Indonesian 1 rupiah coin', 'Indonesia', '1970', 'Coin of 1 rupiah issued in 1970 and still legal tender.', S+'Indonesian_rupiah', 'Bank Indonesia'),
 E('Indonesian rupiah coins of 1991 to 1997', 'Indonesia', '1991', '500 rupiah of 1991 and 1997 and 1,000 rupiah of 1993, withdrawn on 1 December 2023.', S+'Indonesian_rupiah', 'Bank Indonesia'),
]
counts['Circulation coin'] = add('Circulation coin', coins)
cov('Circulation coin', 'Seven further issuers (Turkey, Saudi Arabia, Egypt, Nigeria, South Korea, Argentina, Indonesia) were added from their Wikipedia currency articles so that every world region has circulating series; other issuers are still not covered.')

notes = [
 E('Turkish lira E-9 emission group', 'Turkey', '2009', 'Notes of 5 to 200 lira issued from 1 January 2009; a second 5 lira series followed on 8 April 2013.', S+'Turkish_lira', 'Central Bank of the Republic of Türkiye',
   [V('5 lira', '2009'), V('10, 20, 50 and 100 lira', '2009'), V('200 lira', '2009'), V('5 lira second series', '2013')]),
 E('Hajj pilgrim receipts', 'Saudi Arabia', '1953', 'Receipts of 10, 1 and 5 riyals issued 1953 to 1956 and withdrawn in 1965.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Saudi Arabian Monetary Agency notes of 1961', 'Saudi Arabia', '1961', 'First regular notes of 1, 5, 10, 50 and 100 riyals; 500 riyals followed in 1983.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Saudi fourth series (King Fahd)', 'Saudi Arabia', '1984', 'Notes issued under King Fahd between 1984 and 2007.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Saudi fifth series', 'Saudi Arabia', '2007', 'Notes of 1, 5, 10, 50, 100 and 500 riyals.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Saudi sixth series', 'Saudi Arabia', '2016', 'Notes of 5, 10, 50, 100 and 500 riyals.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Egyptian pound banknotes', 'Egypt', '1978', 'Notes from 25 piastres to 200 pounds, with polymer 10 and 20 pound notes in 2022 and 2023.', S+'Egyptian_pound', 'Central Bank of Egypt',
   [V('1 pound', '1978'), V('5 pounds', '1981'), V('50 pounds', '1993'), V('100 pounds', '1994'), V('200 pounds', '2007'), V('10 pounds polymer', '2022'), V('20 pounds polymer', '2023')]),
 E('Nigerian naira notes of 1999 to 2005', 'Nigeria', '1999', 'Notes of 100, 200, 500 and 1,000 naira issued between 1999 and 2005.', S+'Nigerian_naira', 'Central Bank of Nigeria',
   [V('100 naira', '1999'), V('200 naira', '2000'), V('500 naira', '2001'), V('1,000 naira', '2005')]),
 E('Nigerian naira notes of 2006', 'Nigeria', '2007', 'Notes of 5, 10, 20 and 50 naira issued on 28 February 2007.', S+'Nigerian_naira', 'Central Bank of Nigeria'),
 E('Nigerian naira redesign of 2022', 'Nigeria', '2022', 'Redesigned notes of 200, 500 and 1,000 naira.', S+'Nigerian_naira', 'Central Bank of Nigeria'),
 E('South Korean won notes of 1972 to 1979', 'South Korea', '1972', 'Notes of 500, 1,000, 5,000 and 10,000 won.', S+'South_Korean_won', 'Bank of Korea'),
 E('South Korean won notes of 1983', 'South Korea', '1983', 'Notes of 1,000, 5,000 and 10,000 won, modified in 1994, 2000 and 2002.', S+'South_Korean_won', 'Bank of Korea'),
 E('South Korean won notes of 2006', 'South Korea', '2006', 'Notes of 1,000, 5,000, 10,000 and 50,000 won, with a 2,000 won commemorative in 2017.', S+'South_Korean_won', 'Bank of Korea'),
 E('Argentine Convertibles series', 'Argentina', '1992', 'Notes of 1 to 100 pesos issued in 1992.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine Nuevo diseño series', 'Argentina', '1997', 'Notes of 2 to 100 pesos issued in 1997.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine Tenemos Patria series', 'Argentina', '2013', 'Notes of 5 to 100 pesos issued in 2013.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine Native Fauna series', 'Argentina', '2016', 'Animal-themed notes of 20 to 1,000 pesos issued 2016 to 2018.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Argentine Heroines and Heroes series', 'Argentina', '2022', 'Notes of 1,000 to 20,000 pesos issued 2022 to 2024.', S+'Argentine_peso', 'Central Bank of Argentina'),
 E('Indonesian rupiah notes of 2016', 'Indonesia', '2016', 'Seven-denomination series issued on 19 December 2016.', S+'Indonesian_rupiah', 'Bank Indonesia'),
 E('Indonesian rupiah notes of 2022', 'Indonesia', '2022', 'Notes of 1,000 to 100,000 rupiah issued on 17 August 2022.', S+'Indonesian_rupiah', 'Bank Indonesia'),
]
counts['Circulation banknote'] = add('Circulation banknote', notes)
cov('Circulation banknote', 'Seven further issuers (Turkey, Saudi Arabia, Egypt, Nigeria, South Korea, Argentina, Indonesia) were added from their Wikipedia currency articles; other issuers are still not covered.')
comm = [
 E('Saudi 20 riyal commemorative note', 'Saudi Arabia', '2020', 'Commemorative note of 20 riyals issued in 2020.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Saudi 200 riyal commemorative note', 'Saudi Arabia', '2021', 'Commemorative note of 200 riyals issued in 2021.', S+'Saudi_riyal', 'Saudi Arabian Monetary Agency'),
 E('Indonesian 75,000 rupiah commemorative note', 'Indonesia', '2020', 'Note marking the 75th independence anniversary, issued on 17 August 2020.', S+'Indonesian_rupiah', 'Bank Indonesia'),
]
counts['Commemorative banknote'] = add('Commemorative banknote', comm)

# ---- UK campaign medals
UKS = W + 'British_campaign_medals'
uk = """Naval Gold Medal|1794
Army Gold Cross|1810
Army Gold Medal|1810
Ghuznee Medal|1839
Candahar, Ghuznee, Cabul Medal|1842
Jellalabad Medals|1842
Medal for the Defence of Kelat-i-Ghilzie|1842
China War Medal 1842|1842
Scinde Medal|1843
Gwalior Star|1843
Sutlej Medal|1846
Naval General Service Medal 1847|1847
Military General Service Medal|1847
Punjab Medal|1849
Army of India Medal|1851
India General Service Medal 1854|1854
South Africa Medal 1853|1854
Baltic Medal|1856
Second China War Medal|1861
New Zealand War Medal|1869
Abyssinian War Medal|1869
Canada General Service Medal|1866
Ashantee Medal|1873
South Africa Medal 1877–79|1877
Afghanistan Medal 1878–80|1878
Kabul to Kandahar Star|1880
Egypt Medal|1882
Royal Niger Company's Medal|1886
British South Africa Company Medal|1890
East and West Africa Medal|1892
Central Africa Medal|1895
India Medal 1895|1896
Ashanti Star|1896
Queen's Sudan Medal|1899
East and Central Africa Medal|1899
Queen's Mediterranean Medal|1899
China War Medal 1900|1900
Ashanti Medal 1900|1901
King's South Africa Medal|1902
Africa General Service Medal|1902
Transport Medal|1902
Tibet Medal|1905
Natal Native Rebellion Medal|1906
India General Service Medal 1909|1909
1914 Star|
1914–15 Star|
British War Medal|
Mercantile Marine War Medal|
Victory Medal (United Kingdom)|
Territorial Force War Medal|
Naval General Service Medal 1915|1915
India General Service Medal 1936|1936
1939–1945 Star|
Atlantic Star|
Arctic Star|
Air Crew Europe Star|
Africa Star|
Pacific Star|
Burma Star|
Italy Star|
France and Germany Star|
Defence Medal|
Canadian Volunteer Service Medal|
Newfoundland Volunteer War Service Medal|
War Medal 1939–1945|
Africa Service Medal|
India Service Medal|
New Zealand War Service Medal|
Southern Rhodesia Medal for War Service|
Australia Service Medal|
Korea Medal|1951
Nuclear Test Medal|1952
Rhodesia Medal|1980
South Atlantic Medal|1982
Gulf Medal|1991
Operational Service Medal for Sierra Leone|2000
Operational Service Medal for Afghanistan|2002
Operational Service Medal for the Democratic Republic of Congo|2003
Iraq Medal|2004
Iraq Reconstruction Service Medal|2004
Civilian Service Medal (Afghanistan)|2011
Ebola Medal for Service in West Africa|2014
General Service Medal 2008|2009
Operational Service Medal for Iraq and Syria|2016
Humanitarian Medal|2023
Wider Service Medal|2024"""
ukE = []
for line in uk.splitlines():
    n, y = line.split('|')
    ukE.append(E(n, 'United Kingdom', y, 'British campaign or service medal listed in Wikipedia\'s article on British campaign medals.', UKS))
counts['Campaign medal UK'] = add('Campaign medal', ukE)

# ---- US and foreign awards (Wikipedia list of US armed forces awards)
USS = W + 'Awards_and_decorations_of_the_United_States_Armed_Forces'
def us(names, dd, g='United States', y=''):
    return [E(n, g, y, dd, USS) for n in names]
gall = us(['Navy Distinguished Service Medal', 'Navy and Marine Corps Commendation Medal', 'Navy and Marine Corps Achievement Medal',
           'Air Force Distinguished Service Medal', 'Air and Space Commendation Medal', 'Air and Space Achievement Medal', 'Air Force Combat Action Medal',
           'Coast Guard Distinguished Service Medal', 'Coast Guard Commendation Medal', 'Coast Guard Achievement Medal', "Commandant's Letter of Commendation Ribbon",
           'Certificate of Merit', 'Gold Lifesaving Medal', 'Silver Lifesaving Medal',
           'Presidential Unit Citation', 'Navy Unit Commendation', 'Navy Meritorious Unit Commendation', 'Air Force Gallant Unit Citation', 'Air Force Meritorious Unit Award',
           'Air and Space Outstanding Unit Award', 'Air and Space Organizational Excellence Award', 'Coast Guard Unit Commendation', 'Coast Guard Meritorious Unit Commendation', 'Coast Guard Meritorious Team Commendation'],
          'United States decoration of the Navy, Air Force or Coast Guard listed in Wikipedia\'s article on US armed forces awards.')
gall += us(['Kearny Cross', 'Kearny Medal', 'Butler Medal', 'Gillmore Medal'], 'Unofficial United States decoration listed in Wikipedia\'s article on US armed forces awards.')
vn = ['RVN Army Distinguished Service Order', 'RVN Navy Distinguished Service Order', 'RVN Air Force Distinguished Service Order', 'RVN Military Merit Medal', 'RVN Gallantry Cross',
      'RVN Air Gallantry Cross', 'RVN Navy Gallantry Cross', 'RVN Armed Forces Honor Medal', 'RVN Civil Actions Medal', 'RVN Staff Service Medal', 'RVN Special Service Medal', 'RVN Training Service Medal']
gall += us(vn, 'Award of the Republic of Vietnam that may be worn on a United States uniform, listed in Wikipedia\'s article on US armed forces awards.', 'South Vietnam')
gall += [E(n, g, '', 'Foreign award that may be worn on a United States uniform, listed in Wikipedia\'s article on US armed forces awards.', USS) for n, g in [
    ('Belgian Croix de guerre', 'Belgium'), ('Czechoslovak War Cross 1918', 'Czechoslovakia'), ('Czechoslovak War Cross 1945', 'Czechoslovakia'), ('Military Merit Medal (Haiti)', 'Haiti'),
    ('Medal of Merit (Nicaragua)', 'Nicaragua'), ('Luxembourg War Cross', 'Luxembourg'), ('Aeronautical Merit Cross (Peru)', 'Peru'), ('Cross of Honor (Germany)', 'Germany')]]
counts['Gallantry'] = add('Gallantry and merit decoration', gall)

camp = us(['Navy Expeditionary Medal', 'Marine Corps Expeditionary Medal', 'Antarctica Service Medal', 'Arctic Service Medal', 'Air and Space Campaign Medal', 'Remote Combat Effects Campaign Medal',
           'Nuclear Deterrence Operations Service Medal', 'Air and Space Expeditionary Service Ribbon', 'Coast Guard Arctic Service Medal'],
          'United States campaign or service medal of the Navy, Air Force or Coast Guard listed in Wikipedia\'s article on US armed forces awards.')
camp += [E(n, g, '', 'Foreign or international campaign award that may be worn on a United States uniform, listed in Wikipedia\'s article on US armed forces awards.', USS) for n, g in [
    ('Philippine Defense Medal', 'Philippines'), ('Philippine Liberation Medal', 'Philippines'), ('Philippine Independence Medal', 'Philippines'), ('United Nations Service Medal', 'United Nations'),
    ('United Nations Medal', 'United Nations'), ('Republic of Korea War Service Medal', 'South Korea'), ('RVN Campaign Medal', 'South Vietnam'), ('Kuwait Liberation Medal (Kuwait)', 'Kuwait'),
    ('Kuwait Liberation Medal (Saudi Arabia)', 'Saudi Arabia'), ('Multinational Force and Observers Medal', 'Multinational Force and Observers'),
    ('Inter-American Defense Board Medal', 'Inter-American Defense Board'), ('NATO Medal (Yugoslavia)', 'NATO'), ('NATO Medal (Kosovo)', 'NATO'), ('NATO Medal (Non-Article 5)', 'NATO')]]
counts['Campaign medal US'] = add('Campaign medal', camp)

lsv = us(['Navy Good Conduct Medal', 'Marine Corps Good Conduct Medal', 'Air Force Good Conduct Medal', 'Space Force Good Conduct Medal', 'Coast Guard Good Conduct Medal', 'Coast Guard Reserve Good Conduct Medal',
          'Selected Marine Corps Reserve Medal', 'Sea Service Deployment Ribbon', 'Naval Reserve Sea Service Ribbon', 'Overseas Service Ribbon (Navy and Marine Corps)', 'Air and Space Overseas Short Tour Ribbon',
          'Air and Space Overseas Long Tour Ribbon', 'Air and Space Longevity Service Award', 'Coast Guard Sea Service Ribbon'],
         'United States long-service or good-conduct award listed in Wikipedia\'s article on US armed forces awards.')
counts['Long-service'] = add('Long-service and good-conduct medal', lsv)

orders = [('Order of Abdon Calderón', 'Ecuador'), ('Order of Adolphe of Nassau', 'Luxembourg'), ('Order of the Aztec Eagle', 'Mexico'), ('Order of the British Empire', 'United Kingdom'),
          ('Order of the Bath', 'United Kingdom'), ('Order of the Crown (Belgium)', 'Belgium'), ('Order of Leopold (Belgium)', 'Belgium'), ('Order of Orange-Nassau', 'Netherlands'),
          ('Order of Ouissam Alaouite', 'Morocco'), ('Order of Pao Ting', 'China'), ('Order of Virtuti Militari', 'Poland'), ('Order of the White Eagle (Poland)', 'Poland'),
          ('Order of the White Eagle (Yugoslavia)', 'Yugoslavia'), ('Order of William', 'Netherlands'), ('Khalifiyyeh Order of Bahrain', 'Bahrain'), ('Military Merit Order (United Arab Emirates)', 'United Arab Emirates'),
          ('Order of the Crown of Thailand', 'Thailand'), ('Order of the Date Palm', 'Iraq'), ('Order of May', 'Argentina'), ('Order of the Sword', 'Sweden'), ('Order of Merit of the Federal Republic of Germany', 'Germany'),
          ('Order of Merit of the Italian Republic', 'Italy'), ('Order of National Security Merit', 'South Korea'), ('Order of the Rising Sun', 'Japan'), ('Order of the Southern Cross', 'Brazil')]
counts['Orders'] = add('Order of chivalry or state order', [E(n, g, '', 'Foreign order that may be worn on a United States uniform, listed in Wikipedia\'s article on US armed forces awards.', USS) for n, g in orders])

cov('Campaign medal', "Complete for Wikipedia's article on British campaign medals (every medal named there, 1794 to 2024) and for the Navy, Air Force, Coast Guard and foreign-award sections of Wikipedia's article on US armed forces awards; the Army section was not read.")
cov('Gallantry and merit decoration', "Adds the Navy, Air Force, Coast Guard, unofficial and foreign sections of Wikipedia's article on US armed forces awards (read in full to its end); marksmanship, recruiting and training ribbons are out of scope and the Army and Joint sections were not read.")
cov('Long-service and good-conduct medal', "Adds the good-conduct and service ribbons of the Navy, Air Force and Coast Guard from Wikipedia's article on US armed forces awards; marksmanship, recruiting and training ribbons are out of scope.")
cov('Order of chivalry or state order', "Adds the foreign orders listed in Wikipedia's article on US armed forces awards; other countries' orders are still not covered.")

# ---- Topps base set run
CB = 'https://www.cardboardconnection.com/evolution-topps-baseball-cards-1951-2017/amp'
cnt = {1952:407,1953:274,1954:250,1955:206,1956:342,1957:420,1958:494,1959:572,1960:572,1961:587,1962:598,1963:576,1964:587,1965:598,1966:598,1967:609,1968:598,1969:664,1970:720,1971:752,1972:787,
       1973:660,1974:660,1975:660,1976:660,1977:660,1978:726,1979:726,1980:726,1981:726,1995:660,1996:440,2000:479}
for yv in range(1982, 1993): cnt[yv] = 792
for yv in range(1982, 1993): pass
def era(yv):
    return 'Before 1946' if yv < 1946 else '1946-1979' if yv < 1980 else '1980-1999' if yv < 2000 else '2000 onward'
tp = []
for yv in range(1951, 2025):
    dd = f'Topps flagship baseball set of {yv}' + (f', {cnt[yv]} cards in the Baseball Almanac listing.' if yv in cnt else '.')
    tp.append({'n': f'{yv} Topps', 'a': '', 'd': dd, 'mk': 'Topps', 'y': str(yv), 's': CB, 'g': era(yv)})
counts['Base card'] = add('Base card', tp)
cov('Base card', "Topps flagship baseball set for every year 1951 to 2024 (Cardboard Connection's Topps timeline, 74 of 74 years; card counts from Baseball Almanac where it lists the year); Beckett's page could not be fetched.")

json.dump(d, open(P + '.tmp', 'w'), indent=1, ensure_ascii=False)
os.replace(P + '.tmp', P)
print(counts)
print({n: (before[n], len(K[n]['x'])) for n in before if before[n] != len(K[n]['x'])})
