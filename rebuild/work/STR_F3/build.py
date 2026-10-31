import json, os, shutil, copy
R = '/home/user/Possession-Taxonomy/rebuild/'
src = json.load(open(R + 'work/STR_F3/bak/F3.json'))

# ---------- index kinds ----------
K = {}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k

renames = {}

# ---------- rename / split ----------
slab = K.pop('Grading slab')
def sub(names):
    return [x for x in slab['x'] if x['n'] in names]
coin_slab = copy.deepcopy(slab)
coin_slab['n'] = 'Graded coin slab'
coin_slab['a'] = 'coin slab · slabbed coin · encapsulated coin'
coin_slab['d'] = 'Sealed, tamper-evident holder in which a grading service encapsulates one coin with its grade label.'
coin_slab['x'] = sub(['PCGS coin slab', 'NGC coin slab', 'ANACS slab'])
note_slab = {'n': 'Graded banknote holder', 'a': 'banknote slab · graded note holder',
             'd': 'Sealed holder in which a grading service encapsulates one banknote with its grade label.',
             's': slab['s'], 'x': sub(['PMG banknote holder', 'PCGS Banknote holder'])}
card_slab = {'n': 'Graded card slab', 'a': 'card slab · slabbed card · graded card',
             'd': 'Sealed, tamper-evident holder in which a grading service encapsulates one trading card with its grade label.',
             's': slab['s'], 'x': sub(['PSA card slab', 'BGS card slab', 'SGC card slab', 'CGC Cards slab'])}
assert len(coin_slab['x']) + len(note_slab['x']) + len(card_slab['x']) == len(slab['x'])
for o in (coin_slab, note_slab, card_slab):
    K[o['n']] = o
renames['Grading slab'] = 'Graded coin slab'

k = K.pop('Odd and curious money')
k['n'] = 'Commodity and primitive money'
k['a'] = 'odd and curious money · primitive money · pre-coin money'
k['d'] = 'Pre-coinage and commodity money, such as manillas, Kissi pennies, cowries and Yap stones.'
K[k['n']] = k
renames['Odd and curious money'] = 'Commodity and primitive money'

# ---------- demote generic archetypes to models ----------
DEMOTE = {
 'Circulation coin': ['Euro definitive coins', 'British pre-decimal silver', 'Deutsche Mark coins', 'Indian rupee coins',
                      'Canadian decimal coins', 'Australian decimal coins', 'Japanese yen coins'],
 'Islamic coin': ['Later dynastic dinars'],
 'Celtic coin': ['Regional tribal coinage'],
 'Circulation banknote': [],
 'Emergency scrip and Notgeld': ['Siege notes'],
 'Replica, prop or counterfeit note': ['Test money'],
 'Definitive stamp': ['Country definitives'],
 'Stamp booklet': ['Luxembourg booklet', 'Early US booklets'],
 'Postal history cover': ['Stampless letter', 'Censored cover', 'Military mail cover'],
 'Flight and rocket cover': ['Crash cover', 'Rocket mail cover', 'First-flight cover'],
 'Postmark and cancellation': ['Slogan postmark', 'Pictorial postmark'],
 'Parallel card': ['Prizm parallels'],
 'Casino chip and gaming token': ['Casino chip (cheque)'],
 'Love token and counterstamped coin': ['Love token'],
 'Coin weight': ['Boxed coin balance with weights'],
 'Challenge coin': ['Military unit challenge coin', 'Presidential challenge coin'],
 'Championship belt': ['Sanctioning-body title belt'],
 'Championship ring': ['Fan replica ring'],
 'Elongated coin': ['Machine pressed penny'],
}
demoted = []
for kn, names in DEMOTE.items():
    kk = K[kn]
    have = {tuple(m) for m in kk.get('m', [])}
    for x in list(kk.get('x', [])):
        if x['n'] in names:
            kk['x'].remove(x)
            mk = x.get('mk', '')
            ent = [x['n'], mk]
            if tuple(ent) not in have:
                kk.setdefault('m', []).append(ent)
                have.add(tuple(ent))
            demoted.append((kn, x['n']))
# duplicates
K['Cigarette and trade card']['x'] = [x for x in K['Cigarette and trade card']['x'] if x['n'] != 'Allen & Ginter tobacco cards']
rk = K['Rookie card']
yg = [x for x in rk['x'] if x['n'] == 'Young Guns']
if yg:
    rk['x'] = [x for x in rk['x'] if x['n'] != 'Young Guns']
    for x in rk['x']:
        if x['n'] == 'Upper Deck Young Guns':
            x['a'] = (x.get('a', '') + ' · Young Guns').strip(' ·')

# ---------- new kinds ----------
SIG = 'https://en.wikipedia.org/wiki/Sigloi'
def arch(n, d, s, mk='', y='', a='', v=None, dt=None):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt: o['dt'] = dt
    return o
NEW = {
 'Achaemenid Persian coin': {
  'n': 'Achaemenid Persian coin', 'a': 'daric · siglos · Persian archer coin',
  'd': 'Gold and silver coin of the Persian Empire, struck from about 520 to 330 BC with the royal archer on the front.',
  's': SIG,
  'x': [arch('Daric', 'Gold coin of the Persian Empire introduced under Darius I, worth 20 sigloi.', SIG, y='c. 510–500 BC'),
        arch('Siglos', 'Silver coin of the Persian Empire paired with the daric as the first two-metal coinage; used to pay mercenaries in Asia Minor.', SIG, y='c. 510–500 BC')]},
 'Postage due stamp': {
  'n': 'Postage due stamp', 'a': 'tax stamp · porto stamp · due label',
  'd': 'Stamp put on underpaid mail by the delivery office to show the extra amount owed, usually a numeral with the words postage due.',
  's': 'https://en.wikipedia.org/wiki/Postage_due',
  'x': [arch('French postage due', 'First official postage due stamps, issued by France and put on mail at the delivery office.', 'https://en.wikipedia.org/wiki/Postage_due', y='1859')]},
 'Official stamp': {
  'n': 'Official stamp', 'a': 'service stamp · departmental stamp · on service',
  'd': 'Postage stamp reserved for government departments and not sold at post offices, issued to control official postage.',
  's': 'https://en.wikipedia.org/wiki/Official_mail',
  'x': [arch('VR official', 'British official stamps for government departments, starting with the 1840 issue.', 'https://en.wikipedia.org/wiki/Official_mail', mk='Royal Mail', y='1840'),
        arch('US departmental stamps', 'Stamps for United States executive departments such as Agriculture, Justice and the Treasury.', 'https://en.wikipedia.org/wiki/Official_mail', y='1873')]},
 'Life-saving medal': {
  'n': 'Life-saving medal', 'a': 'humane society medal · rescue medal · lifesaving award',
  'd': 'Medal given by a state or a humane society to someone who saved or tried to save a life.',
  's': 'https://en.wikipedia.org/wiki/Royal_Humane_Society',
  'x': [arch('Royal Humane Society medals', 'Stanhope gold medal for the most gallant rescue of the year, with silver and bronze medals for risking life to save another.', 'https://en.wikipedia.org/wiki/Royal_Humane_Society', y='1774')]},
 'Wound badge': {
  'n': 'Wound badge', 'a': 'wound decoration · wound medal',
  'd': 'Badge or medal awarded to a soldier wounded in action, in grades by number of wounds.',
  's': 'https://en.wikipedia.org/wiki/Wound_Badge',
  'x': [arch('Wound Badge (Verwundetenabzeichen)', 'German badge created by Wilhelm II and reinstated in 1939: black for one or two wounds, silver for three or four, gold for five or more.', 'https://en.wikipedia.org/wiki/Wound_Badge', y='1918')]},
 'Sealed trading-card game product': {
  'n': 'Sealed trading-card game product', 'a': 'booster pack · booster box · starter deck · sealed TCG',
  'd': 'Unopened pack, box or deck of a card game, kept sealed: a booster pack of random cards, a box of boosters or a pre-built starter deck.',
  's': 'https://en.wikipedia.org/wiki/Booster_pack',
  'tt': [['Unit', ['Booster pack', 'Booster box', 'Starter deck (intro deck)', 'Case']],
         ['Card selection', ['Random cards', 'Pre-built deck']]]},
 'Jeton and gaming counter': {
  'n': 'Jeton and gaming counter', 'a': 'jetton · reckoning counter · whist counter',
  'd': 'Coin-like counter used to reckon sums, to keep score in card games or as play money, not as money.',
  's': 'https://en.wikipedia.org/wiki/Exonumia',
  'tt': [['Use', ['Reckoning counter (jeton)', 'Game counter (whist)', 'Imitation guinea']]]},
 'Geocoin': {
  'n': 'Geocoin', 'a': 'geocaching coin · trackable coin',
  'd': 'Coin-sized token with a tracking code, moved between geocaches by players.',
  's': 'https://en.wikipedia.org/wiki/Exonumia'},
 'Storage box': {
  'n': 'Storage box', 'a': 'coin box · monster box · slab box',
  'd': 'Lidded box for capsuled coins, tubes, graded slabs or cards, from a velvet-lined coin box to a monster box of tubes.',
  's': 'https://bullionstar.com/buy/supplies',
  'tt': [['Holds', ['Capsuled coins', 'Coin tubes (monster box)', 'Graded slabs', 'Trading cards']],
         ['Lining', ['Velvet inlay', 'Foam', 'Plain']]]},
 'Display case and stand': {
  'n': 'Display case and stand', 'a': 'coin stand · showcase louvre · display case',
  'd': 'Stand, upright frame or case that shows a few coins or medals rather than storing a collection.',
  's': 'https://bullionstar.com/buy/supplies',
  'tt': [['Form', ['Table stand', 'Upright showcase louvre', 'Case']],
         ['Material', ['Acrylic', 'Wood']]]},
}
for kn, o in NEW.items():
    o.setdefault('a', ''); K[kn] = o

# ---------- tt (types by named axis), written by hand ----------
TT = {
 'Circulation coin': [['Metal content', ['Silver (junk silver when worn)', 'Gold', 'Copper-nickel', 'Bronze or copper', 'Nickel-brass', 'Steel']],
                      ['Variety', ['Mint-mark variety', 'Die variety', 'Overdate', 'Repunched mint mark']]],
 'Circulating commemorative coin': [['Issue pattern', ['One-off design', 'Annual series', 'Multi-year programme']],
                                    ['Metal', ['Base metal', 'Bimetallic', 'Silver-clad']]],
 'Collector coin': [['Finish', ['Proof', 'Reverse proof', 'Brilliant uncirculated', 'Coloured']],
                    ['Relief and thickness', ['High relief', 'Piedfort']]],
 'Proof or mint set': [['Finish of the coins', ['Proof', 'Mint (uncirculated)', 'Special mint']],
                       ['Metal', ['Base metal', 'Silver', 'Gold']],
                       ['Presentation', ['Prestige case', 'Card holder']]],
 'Mint error coin': [['Strike fault', ['Off-centre strike', 'Double strike', 'Broadstrike', 'Brockage', 'Die cap']],
                     ['Die fault', ['Doubled die', 'Die crack or cud', 'Die clash', 'Mule']],
                     ['Planchet fault', ['Clipped planchet', 'Lamination', 'Wrong planchet']]],
 'Pattern or trial strike': [['Purpose', ['Design pattern', 'Metal trial', 'Die trial']]],
 'Emergency coin': [['Cause', ['Siege piece', 'Necessity coin (Notgeld)']],
                    ['Making', ['Struck', 'Cast or cut-plate']]],
 'Replica or counterfeit coin': [['Intent', ['Contemporary counterfeit', 'Collector forgery', 'Replica', 'Fantasy coin']],
                                 ['Make', ['Plated core (fourrée)', 'Cast copy']]],
 'Ancient Greek coin': [['Metal', ['Electrum', 'Silver', 'Gold', 'Bronze']],
                        ['Period', ['Archaic incuse', 'Classical', 'Hellenistic']],
                        ['Issue', ['Lifetime issue', 'Posthumous issue']]],
 'Achaemenid Persian coin': [['Metal', ['Gold', 'Silver']], ['Issuer', ['Royal issue', 'Satrapal issue']]],
 'Roman Republican coin': [['Making', ['Cast (aes grave)', 'Struck']],
                           ['Variant', ['Serrate (notched edge)', 'Plated (ancient forgery)']]],
 'Roman Imperial coin': [['Metal', ['Gold', 'Silver', 'Billon', 'Bronze or brass']],
                         ['Mint', ['Imperial mint', 'Provincial mint']]],
 'Celtic coin': [['Metal', ['Gold', 'Silver', 'Potin (cast bronze)']],
                 ['Denomination', ['Stater', 'Quarter stater', 'Silver unit']],
                 ['Legend', ['Uninscribed', 'Inscribed']]],
 'Byzantine coin': [['Metal', ['Gold', 'Silver', 'Electrum', 'Billon', 'Copper']],
                    ['Shape', ['Flat', 'Scyphate (cup-shaped)']]],
 'Medieval European hammered coin': [['Denomination', ['Penny', 'Halfpenny', 'Farthing', 'Groat']],
                                     ['Metal', ['Silver', 'Gold']],
                                     ['Form', ['Whole coin', 'Cut halfpenny or farthing']]],
 'Islamic coin': [['Metal', ['Gold (dinar)', 'Silver (dirham)', 'Copper (fals)']],
                  ['Size', ['Whole coin', 'Fraction or multiple']]],
 'Indian coin (ancient to Mughal)': [['Making', ['Punch-marked', 'Die-struck', 'Cast']],
                                     ['Metal', ['Gold', 'Silver', 'Copper']]],
 'Chinese cash coin': [['Metal', ['Cast bronze', 'Iron']],
                       ['Form', ['Round with square hole', 'Hollow-handled spade', 'Flat-handled spade']]],
 'Japanese traditional coin': [['Metal', ['Gold', 'Silver', 'Copper', 'Iron', 'Brass']]],
 'Commodity and primitive money': [['Material', ['Brass', 'Copper', 'Iron', 'Stone', 'Shell']]],
 'Bullion coin': [['Metal', ['Gold', 'Silver', 'Platinum', 'Palladium']],
                  ['Size', ['One ounce', 'Fractional size', 'Multi-ounce']],
                  ['Finish and marking', ['Bullion strike', 'Proof', 'Reverse proof', 'Privy-marked']]],
 'Bullion bar': [['Making', ['Minted bar', 'Cast bar']],
                 ['Divisibility', ['Single bar', 'Divisible bar']],
                 ['Metal', ['Gold', 'Silver', 'Platinum']]],
 'Bullion round': [['Metal', ['Silver', 'Gold', 'Copper']],
                   ['Shape for storage', ['Stacker', 'Standard disc']],
                   ['Finish', ['Plain', 'Antiqued', 'Gilded']]],
 'Circulation banknote': [['Material', ['Paper', 'Polymer', 'Hybrid']],
                          ['Size', ['Large-size', 'Small-size']],
                          ['Serial number', ['Ordinary', 'Star or replacement note', 'Radar or fancy serial number']],
                          ['Variety', ['Signature variety', 'Changeover note']]],
 'Commemorative banknote': [['Material', ['Paper', 'Polymer']], ['Occasion', ['Anniversary', 'Event', 'Person']]],
 'Collector banknote': [['Material', ['Paper', 'Polymer']], ['Sale form', ['Bare note', 'Folder or pack']]],
 'Private and local bank note': [['Status', ['Current', 'Obsolete']],
                                 ['Issuer', ['Commercial bank', 'Local or provincial bank', 'National bank']]],
 'Emergency scrip and Notgeld': [['Material', ['Paper', 'Card', 'Cloth, leather or porcelain']],
                                 ['Form', ['Note', 'Bearer cheque']]],
 'Military and occupation currency': [['Issued for', ['Troop pay (military payment certificate)', 'Occupied territory (occupation currency)']],
                                      ['Marking', ['Plain', 'Overprinted']]],
 'Specimen note': [['Marking', ['SPECIMEN overprint', 'Perforated (perfin)', 'Zero serial number']],
                   ['Stage', ['Colour trial', 'Proof']],
                   ['Presentation', ['Loose', 'Presentation folder or album']]],
 'Error note': [['Printing fault', ['Missing print', 'Ink or offset error']],
                ['Cutting fault', ['Cutting or misalignment error', 'Fold-over']],
                ['Numbering fault', ['Mismatched serial number']]],
 'Replica, prop or counterfeit note': [['Purpose', ['Contemporary counterfeit', 'Facsimile or replica', 'Prop or movie money', 'Test note', 'Souvenir or novelty note', 'Fantasy note']]],
 'Definitive stamp': [['Separation', ['Perforated', 'Imperforate', 'Rouletted']],
                      ['Gum', ['Gummed', 'Self-adhesive']],
                      ['Paper or coating', ['Watermarked', 'Unwatermarked', 'Phosphor-banded']],
                      ['Format', ['Sheet', 'Coil', 'Booklet pane', 'Block or plate block']],
                      ['Printing variety', ['Shade variety']]],
 'Commemorative stamp': [['Format', ['Single', 'Set', 'Se-tenant pair or block']],
                         ['Purpose', ['Semi-postal (charity surcharge)', 'Christmas stamp', 'Joint issue']]],
 'Airmail stamp': [['Issue form', ['Airmail overprint', 'Airmail definitive', 'Airmail commemorative']],
                   ['Postal standing', ['Postage stamp', 'Semi-official airmail label', 'Airmail etiquette (label, not postage)']]],
 'Postage due stamp': [['Application', ['On the letter at the delivery office', 'On the top letter of a bundle']]],
 'Official stamp': [['Making', ['Own design series', 'Overprint on an ordinary stamp']]],
 'Revenue stamp': [['Tax or fee', ['Documentary', 'Court fee', 'Excise (tobacco, alcohol)', 'Playing card', 'Hunting licence']],
                   ['Make', ['Adhesive', 'Embossed']],
                   ['Postal use', ['Fiscal only', 'Postal fiscal (valid for postage)']]],
 'Cinderella and poster stamp': [['Issuer', ['Charity seal', 'Local post', 'Railway letter stamp', 'Telegraph stamp', 'Exhibition label or poster stamp', 'Propaganda label', 'Fantasy or bogus issue']]],
 'Souvenir sheet': [['Contents', ['Single-stamp sheet', 'Multi-stamp sheet']], ['Perforation', ['Perforated', 'Imperforate']]],
 'Stamp booklet': [['Unit', ['Complete booklet', 'Loose pane', 'Advertising pane']],
                   ['Gum', ['Gummed', 'Self-adhesive']],
                   ['Edition', ['Ordinary booklet', 'Prestige booklet']]],
 'Stamp error and variety': [['Printing fault', ['Invert', 'Double impression', 'Misregistration', 'Inverted or missing overprint']],
                             ['Colour fault', ['Colour error', 'Missing colour']],
                             ['Paper or perforation fault', ['Wrong watermark', 'Imperforate error', 'Perforation shift']],
                             ['Design fault', ['Design error', 'Freak']]],
 'Postal history cover': [['Postal rate', ['Stampless (pre-adhesive) letter', 'Rate cover']],
                          ['Route', ['Route cover', 'Ship and paquebot mail', 'Railway mail', 'Disaster or wreck cover']],
                          ['Service', ['Registered mail', 'Express mail']],
                          ['Authority', ['Censored mail', 'Military and field post']]],
 'First-day cover': [['Cachet', ['Cacheted', 'Uncacheted']],
                     ['Postmark', ['Official first-day postmark', 'Unofficial city postmark']],
                     ['Maker', ['Postal-administration cover', 'Private cachet maker']],
                     ['Format', ['Envelope cover', 'Maximum card (maxicard)', 'Philatelic numismatic cover (PNC)']]],
 'Flight and rocket cover': [['Carrier', ['Aeroplane', 'Zeppelin', 'Balloon', 'Rocket', 'Catapult']],
                             ['Event', ['First flight', 'Crash or interrupted flight']]],
 'Postmark and cancellation': [['Method', ['Handstamp', 'Machine cancel']],
                               ['Design', ['Slogan postmark', 'Pictorial postmark', 'Fancy cancel']],
                               ['Place of use', ['Railway post office', 'Maritime']],
                               ['Position', ['Cancel on stamp', 'Backstamp', 'First-day postmark']]],
 'Stamped envelope': [['Form', ['Entire', 'Cut square']],
                      ['Stamp printing', ['Embossed', 'Printed indicium']],
                      ['Service', ['Ordinary', 'Registration envelope']]],
 'Postal card': [['Form', ['Single card', 'Message-reply card']],
                 ['Design', ['Plain', 'Pictorial card']],
                 ['Use', ['Public', 'Official card']]],
 'Aerogram': [['Form', ['Aerogramme', 'Letter sheet', 'Lettercard']], ['Issuer', ['Postal administration', 'Armed forces']]],
 'Base card': [['Print run', ['Base', 'Short print', 'Variation', 'Error card']],
               ['Subject', ['Player card', 'Team card', 'Checklist']],
               ['Format', ['Standard card', 'Box card (hand-cut)']]],
 'Rookie card': [['Marking', ['RC-logo card', 'First licensed prospect card']],
                 ['Version', ['Base rookie', 'Rookie parallel', 'Rookie autograph']]],
 'Insert card': [['Design', ['Themed insert', 'Die-cut']], ['Rarity', ['Common insert', 'Short-printed insert', 'Case hit']]],
 'Parallel card': [['Finish', ['Chromium refractor', 'Coloured foil', 'Patterned']],
                   ['Scarcity', ['Unnumbered', 'Serial-numbered', 'One-of-one']],
                   ['Origin', ['Printing plate']]],
 'Autograph card': [['Signing', ['On-card autograph', 'Sticker autograph', 'Cut signature']],
                    ['Signers', ['Single signer', 'Dual or triple autograph']]],
 'Relic and memorabilia card': [['Material', ['Jersey swatch', 'Patch', 'Bat or ball piece']],
                                ['Marking', ['Logoman', 'Debut patch']],
                                ['Pairing', ['Relic only', 'Patch with autograph']]],
 'Vintage tobacco and candy card': [['Series', ['N-series (19th-century tobacco)', 'T-series (20th-century tobacco)']],
                                    ['Variety', ['Back advertisement variety']]],
 'Cigarette and trade card': [['Material', ['Card', 'Silk']],
                              ['Issued with', ['Cigarettes', 'Tea', 'Other goods (chromo)']],
                              ['Holding', ['Single card', 'Complete set', 'Album']],
                              ['Origin', ['Original', 'Reprint']]],
 'Trading-card game single': [['Edition', ['1st edition', 'Unlimited', 'Shadowless', 'Promo', 'Prize card']],
                              ['Finish', ['Holofoil', 'Foil', 'Alternate art', 'Serialized']],
                              ['Language', ['English', 'Japanese', 'Other languages']]],
 'Non-sports trading card': [['Role in set', ['Base card', 'Sticker card', 'Chase card']],
                             ['Finish', ['Standard', 'Hologram', 'Foil']],
                             ['Fault', ['Error card']]],
 'Collectible sticker': [['Finish', ['Plain', 'Foil or shiny']], ['Holding', ['Loose sticker', 'Complete set', 'Update set']]],
 'Sealed card product': [['Pack', ['Wax pack', 'Cello pack', 'Rack pack']],
                         ['Box', ['Hanger box', 'Blaster box', 'Mega box', 'Hobby box', 'Jumbo box']],
                         ['Case or set', ['Case', 'Factory set']]],
 'Trade token': [['Purpose', ['Store card', 'Good-for token', 'Advertising token', 'Political token']],
                 ['Striking', ['Normal', 'Mule']]],
 'Admission, communion or voting token': [['Admits to', ['Communion', 'Meeting or club', 'Attendance record', 'Vote']]],
 'Service token': [['Service', ['Transit and toll', 'Parking', 'Car wash', 'Laundry', 'Telephone', 'Shopping trolley', 'Locker', 'Sales tax']]],
 'Wage or ration token': [['Issued to', ['Mine and plantation workers', 'Hop pickers', 'Tally for work done', 'Ration entitlement']]],
 'Casino chip and gaming token': [['Form', ['Chip', 'Plaque', 'Slot token']],
                                  ['Game', ['Roulette', 'Cash table', 'Slot machine']]],
 'Love token and counterstamped coin': [['Method', ['Smoothed and hand-engraved', 'Counterstamped']],
                                        ['Purpose', ['Keepsake', 'Merchant mark', 'Official revaluation mark']]],
 'Encased coin': [['Contents', ['Coin', 'Postage stamp']], ['Purpose', ['Emergency money', 'Advertising', 'Lucky piece']]],
 'Coin weight': [['Form', ['Single coin weight', 'Coin balance (tumbrel)']]],
 'Elongated coin': [['Era', ['Oldies (1893–c.1965)', 'Modern (c.1965–1985)', 'Contemporary machine-rolled (1988–)']]],
 'Commemorative medal': [['Making', ['Struck', 'Cast']], ['Form', ['Table medal', 'Wearable medal with ribbon']]],
 'Art medal': [['Making', ['Struck', 'Cast']], ['Form', ['Medal', 'Plaquette']]],
 'Award medal': [['Awarded for', ['Sport', 'School or academic', 'Exhibition prize', "Finishing an event"]]],
 'Souvenir medal': [['Occasion', ['Exposition souvenir', 'Tourist landmark', 'Event souvenir']]],
 'Challenge coin': [['Issuer', ['Military unit', 'Presidential', 'Agency and police', 'Corporate and club']]],
 'Gallantry and merit decoration': [['Award', ['First award', 'With bar (repeat award)', 'Posthumous']],
                                    ['Device', ['With oak leaf clusters or stars', "'V' device"]],
                                    ['Naming', ['Named', 'Unnamed']],
                                    ['Size', ['Full size', 'Miniature']]],
 'Order of chivalry or state order': [['Insignia form', ['Collar', 'Sash badge', 'Neck badge', 'Breast star', 'Breast badge', 'Miniature']],
                                      ['Fitting', ['Screwback', 'Ribbon suspension']],
                                      ['Addition', ['With swords', 'With oak leaves', 'Citation device']],
                                      ['Regime type', ['Empire', 'Restoration', 'Republic']],
                                      ['Presentation', ['With case', 'With document (orden book)']]],
 'Campaign medal': [['Clasps', ['Battle clasp', 'Service clasp', 'No clasp']],
                    ['Naming', ['Named (impressed or engraved)', 'Unnamed']],
                    ['Size', ['Full size', 'Miniature']]],
 'Long-service and good-conduct medal': [['Clasp', ['With clasp or bar', 'Without clasp']]],
 'Medal mounting bar and ribbon': [['Mounting', ['Court mounting', 'Swing mounting']],
                                   ['Item', ['Ribbon bar', 'Medal ribbon', 'Presentation or medal case']]],
 'Trophy or award': [['Form', ['Trophy cup', 'Bowl', 'Tankard', 'Salver', 'Upright award (column, figure, star, obelisk)', 'Plaque', 'Shield', 'Rosette', 'Award ribbon']],
                     ['Keeping', ['Perpetual (passed on each year)', 'Kept by the winner']],
                     ['Material', ['Solid silver', 'Silver-plated', 'Resin or plastic']]],
 'Championship belt': [['Version', ['Title belt', 'Replica championship belt']]],
 'Championship ring': [['Version', ['Team ring', 'Replica ring']]],
 'Graded coin slab': [['Size', ['Standard', 'Oversize or mega holder']],
                      ['Add-on', ['Approval sticker', 'NFC chip', 'None']]],
 'Graded banknote holder': [['Note size', ['Standard note', 'Large-size note']]],
 'Graded card slab': [['Size', ['Standard', 'Oversize']]],
 'Graded comic slab': [['Label colour', ['Universal (blue)', 'Signature Series (yellow)', 'Qualified (green)', 'Restored (purple)']]],
 'Coin and note holder': [['Style', ['Round capsule (direct fit or with ring)', '2x2 flip', '2x2 cardboard (staple or self-adhesive)', 'Currency sleeve', 'Rigid currency holder']],
                          ['Material', ['Acrylic', 'PVC-free vinyl', 'Polyester (Mylar)', 'Card']]],
 'Card holder': [['Rigidity', ['Penny sleeve (soft)', 'Semi-rigid card saver', 'Toploader (rigid)', 'Magnetic one-touch holder', 'Screw-down holder']],
                 ['Thickness rating', ['35 pt', '55 pt', '100 pt and above']]],
 'Stamp mount and hinge': [['Fixing', ['Peelable gummed hinge', 'Mount']],
                           ['Mount back', ['Black-backed clear', 'Clear-backed']],
                           ['Cutting', ['Cut-to-size strip', 'Pre-cut size']],
                           ['Item mounted', ['Single stamp', 'Block or souvenir sheet']]],
 'Stamp album': [['Pages', ['Pre-printed', 'Blank or quadrille']],
                 ['Mounting', ['Hingeless (mounts fitted)', 'Hinged']],
                 ['Binding', ['Ring binder', 'Spring-back', 'Peg binder']],
                 ['Coverage', ['Worldwide', 'One country']]],
 'Stock book': [['Page colour', ['White', 'Black']], ['Strips', ['Glassine', 'Clear']],
                ['Binding', ['Bound', 'Ring']], ['Pocket size', ['A5', 'A4']]],
 'Coin album': [['Format', ['Coin folder', 'Coin board', 'Screw-post album with slides', 'Ring binder with pocket sheets', 'Pocket or flip album', 'Slab album']],
                ['Holds', ['Raw coins', 'Graded slabs']]],
 'Banknote album': [['Pockets per sheet', ['One', 'Two', 'Three']],
                    ['Binding', ['Padded binder with slipcase', 'Standard binder']],
                    ['Holds', ['Raw notes', 'Graded-note holders']],
                    ['Note size', ['Standard', 'Large-note format']]],
 'Card binder': [['Pockets per page', ['4', '9', '12']], ['Loading', ['Top-loading', 'Side-loading']],
                 ['Closure', ['Zip', 'Elastic', 'Open']], ['Binding', ['Ring binder', 'Bound portfolio']]],
 'Sticker album': [['Subject', ['Football league', 'World Cup', 'Entertainment licence']],
                   ['State', ['Empty', 'Part-filled', 'Complete']]],
 'Cover and postcard album': [['Item size', ['First-day cover', '#10 envelope', 'Postcard']],
                              ['Binding', ['Bound sheets', 'Ring binder']],
                              ['Pockets', ['One per side', 'Two per side']]],
 'Collection tray': [['Hole shape', ['Round', 'Square']], ['Lining', ['Velour', 'Felt']],
                     ['Stacking', ['Stackable', 'Single']], ['Holds', ['Loose coins', 'Capsules', 'Slabs']]],
 'Coin cabinet': [['Age', ['Antique', 'Modern']], ['Wood', ['Mahogany', 'Other hardwood']], ['Security', ['Lockable', 'Unlocked']]],
}
for kn, tt in TT.items():
    K[kn]['tt'] = tt
    K[kn].pop('t', None)
for kn, kk in K.items():
    kk.pop('t', None)

# ---------- extra definitions ----------
K['Elongated coin']['d'] = 'Coin rolled flat and embossed with a new design, sold as a souvenir.'
K['Prospect'] = None; del K['Prospect']
K['Rookie card']['d'] = 'First base-set card of a player after reaching the top level of the sport; a pre-debut prospect card is its own marking.'
K['Rookie card']['tt'][0][1].append('Pre-debut prospect card')
K['Vintage tobacco and candy card']['d'] = 'Pre-war American sports and other cards issued with tobacco or candy, catalogued by Burdick letter series (T206, N-series); picture cards from other goods → Cigarette and trade card.'
K['Cigarette and trade card']['d'] = 'Picture card given with cigarettes, tea, meat extract or other goods, collected in sets (cartophily); American tobacco sports issues → Vintage tobacco and candy card.'

# ---------- cross-links ----------
SEE = {
 'Trading-card game single': [['E1', 'Trading card single', 'same card seen as a game piece']],
 'Sealed card product': [['E1', 'Trading card packs & boxes', 'same packs sold to players']],
 'Sealed trading-card game product': [['E1', 'Trading card packs & boxes', 'same packs sold to players']],
 'Cover and postcard album': [['F5', 'Postcard album', 'album for picture postcards']],
 'Postal card': [['F5', 'Picture postcard', 'card posted with an adhesive stamp']],
 'Souvenir medal': [['F4', 'Devotional medal', 'medal worn or kept for faith']],
 'Graded card slab': [['E1', 'Trading card single', 'card seen as a game piece']],
 'Graded comic slab': [['F1', 'Single-issue comic', 'the comic inside the slab']],
 'Emergency scrip and Notgeld': [['F5', 'Share certificate', 'other private paper that is not money']],
 'Storage box': [['F1', 'Comic storage box', 'box for comics']],
}
for kn, sv in SEE.items():
    K[kn]['see'] = sv

# ---------- structure ----------
S = lambda n, t, ax, ks: {'n': n, 't': t, 'ax': ax, 'k': [K[x] for x in ks]}
dep = {dp['n']: dp for dp in src['depts']}
def D(name, t, ax, shelves):
    o = {kk: v for kk, v in dep[name].items() if kk not in ('s',)}
    o['t'] = t; o['ax'] = ax; o['s'] = shelves
    return o

depts = [
 D('Coins',
   'Metal money struck by a state, mint or earlier authority, from ancient coinage to modern mint products, with their errors and imitations; metal sold by weight → Bullion; a token or medal → Exonumia.',
   'Is the coin a normal modern mint product, an irregular or imitation piece, or coinage of an earlier civilisation, and which one?',
   [S('Modern coins', 'Machine-struck coins issued by a modern state or mint to spend, to mark an event, to collect or to sell as a set; a faulty or test strike → Errors, trials & imitations.',
      'kinds by why the mint made it: to spend, to mark an event in circulation, to collect, to sell as a set',
      ['Circulation coin', 'Circulating commemorative coin', 'Collector coin', 'Proof or mint set']),
    S('Errors, trials & imitations', 'Coins that depart from a normal mint issue: faulty strikes, test pieces, makeshift emergency money and copies; a collector coin the mint meant to issue → Modern coins.',
      'kinds by how the piece departs from a normal issue: faulty, test, makeshift, copied',
      ['Mint error coin', 'Pattern or trial strike', 'Emergency coin', 'Replica or counterfeit coin']),
    S('Ancient Mediterranean & Near Eastern coins', 'Coins of the Greek, Persian, Celtic and Roman worlds, from the first electrum issues to the Roman Empire; Byzantine and later coins → Byzantine, medieval & Islamic coins.',
      'kinds by civilisation, earliest first',
      ['Ancient Greek coin', 'Achaemenid Persian coin', 'Celtic coin', 'Roman Republican coin', 'Roman Imperial coin']),
    S('Byzantine, medieval & Islamic coins', 'Hand-struck coins of the Eastern Roman Empire, medieval Europe and Muslim states; Roman Empire coins → Ancient Mediterranean & Near Eastern coins.',
      'kinds by successor tradition, Eastern Roman first',
      ['Byzantine coin', 'Medieval European hammered coin', 'Islamic coin']),
    S('Asian & traditional money', 'Coins of India, China and Japan before the modern mints, and the commodity money that came before or beside coinage, such as manillas and cowries.',
      'kinds by region, then by money that is not coinage',
      ['Indian coin (ancient to Mughal)', 'Chinese cash coin', 'Japanese traditional coin', 'Commodity and primitive money'])]),
 D('Bullion',
   'Gold, silver, platinum or palladium sold by weight and purity as a coin, bar or round; a state coin sold above its metal value → Collector coin in Coins.',
   'What form does the metal take: a legal-tender coin, a bar or a round?',
   [S('Bullion coins, bars & rounds', 'Precious metal in stamped form, priced by metal content: legal-tender coins from a mint, bars of any maker and rounds with no legal-tender status.',
      'kinds by legal status and shape: legal-tender coin, bar, round',
      ['Bullion coin', 'Bullion bar', 'Bullion round'])]),
 D('Banknotes & paper money',
   'Paper, polymer or cloth money with its specimens, errors and copies, collected by issuer, series and denomination; a coin → Coins; a share or bond certificate → F5.',
   'Who issued the note and why: a currency authority for use or collecting, a private or emergency issuer, or a specimen, error or copy?',
   [S('Official issues', 'Notes issued by a currency authority, either to circulate, to mark an event or to sell to collectors; a note from a commercial bank or an army → Private, emergency & military notes.',
      'kinds by purpose of the issue: to circulate, to mark an event, to collect',
      ['Circulation banknote', 'Commemorative banknote', 'Collector banknote']),
    S('Private, emergency & military notes', 'Paper money from issuers that are not a central bank: commercial and local banks, towns and firms in need, and armies.',
      'kinds by issuing authority: a bank, a town or business in need, an army',
      ['Private and local bank note', 'Emergency scrip and Notgeld', 'Military and occupation currency']),
    S('Specimens, errors & copies', 'Notes that depart from a normal issue: pre-issue samples, printing faults and copies made without the issuer.',
      'kinds by how the note departs from a normal issue: pre-issue sample, printing fault, copy',
      ['Specimen note', 'Error note', 'Replica, prop or counterfeit note'])]),
 D('Stamps & postal history',
   'Adhesive stamps, covers and prepaid stationery that went, or could go, through the post; the album that holds them → Albums & storage.',
   'Is the item a stamp on its own, a sheet or booklet of stamps, a cover that has travelled, or stationery with the stamp printed on it?',
   [S('Postage & revenue stamps', 'Single adhesive stamps, sorted by what they pay for; a sheet, booklet or faulty stamp → Sheets, booklets & varieties.',
      'kinds by what the stamp is for: everyday postage, an occasion, air carriage, underpayment, government use, tax, or no postal use',
      ['Definitive stamp', 'Commemorative stamp', 'Airmail stamp', 'Postage due stamp', 'Official stamp', 'Revenue stamp', 'Cinderella and poster stamp']),
    S('Sheets, booklets & varieties', 'Stamps issued as a unit, such as a miniature sheet or booklet, and stamps that differ from the normal issue.',
      'kinds by the unit issued and its faults: sheet, booklet, error',
      ['Souvenir sheet', 'Stamp booklet', 'Stamp error and variety']),
    S('Covers & postal history', 'Envelopes and markings collected for what they show about a journey, a first day, a flight or a postmark; prepaid envelopes → Postal stationery.',
      'kinds by what makes the item collectable: its route, its first day, its flight, its marking',
      ['Postal history cover', 'First-day cover', 'Flight and rocket cover', 'Postmark and cancellation']),
    S('Postal stationery', 'Envelopes, cards and sheets sold by a postal administration with the stamp already printed; a picture postcard with an adhesive stamp → F5.',
      'kinds by form of the prepaid item: envelope, card, folding sheet, wrapper',
      ['Stamped envelope', 'Postal card', 'Aerogram', 'Newspaper wrapper'])]),
 D('Trading cards',
   'Printed cards and stickers made to be collected in sets, with the packs they came in; the game itself → Board, card & table games in Toys; a picture postcard → F5.',
   'Is the card from a sports set, issued with goods, made for a game or a non-sports theme, or a sealed pack?',
   [S('Sports cards', 'Cards from numbered sports sets, told apart by how special the card is within its set; pre-war cards packed with tobacco or candy → Cards issued with goods.',
      'kinds by place in the set: common, first-year, bonus, alternate version, signed, with material',
      ['Base card', 'Rookie card', 'Insert card', 'Parallel card', 'Autograph card', 'Relic and memorabilia card']),
    S('Cards issued with goods', 'Picture cards packed with tobacco, sweets, tea or other goods and collected in sets; modern cards sold in packs of their own → Sports cards.',
      'kinds by the goods and region: American sports cards with tobacco and candy, then general picture cards',
      ['Vintage tobacco and candy card', 'Cigarette and trade card']),
    S('Games, non-sports & stickers', 'Cards and stickers collected for a game or a theme such as film, comics or football rather than a sport set.',
      'kinds by what the item is for: playing a game, a non-sports theme, sticking into an album',
      ['Trading-card game single', 'Non-sports trading card', 'Collectible sticker']),
    S('Sealed products', 'Unopened packs, boxes, decks and cases of cards, kept sealed; an opened or loose card → the card shelves above.',
      'kinds by whose cards: sports and non-sports, or a card game',
      ['Sealed card product', 'Sealed trading-card game product'])]),
 D('Exonumia: tokens & medals',
   'Coin-like pieces that are not state money: tokens, altered coins and medals; a state honour → Orders, decorations & medals; a prize cup, belt or ring → Trophies & awards.',
   'Does the piece stand for a value or right (token), is it a coin altered or used as a tool, or does it mark an event or achievement (medal)?',
   [S('Tokens', 'Pieces issued to stand for goods, a service, wages, entry or play, usually redeemed with the issuer rather than spent anywhere.',
      'kinds by what the token stands for: shop goods, a service, wages, entry, play, a game',
      ['Trade token', 'Service token', 'Wage or ration token', 'Admission, communion or voting token', 'Casino chip and gaming token', 'Jeton and gaming counter', 'Geocoin']),
    S('Altered coins & coin tools', 'Real coins changed by hand or machine, and the weights used to test coins; a coin never altered → Coins.',
      'kinds by what was done to the coin or what it is used for: engraved or stamped, encased, rolled flat, weighed',
      ['Love token and counterstamped coin', 'Encased coin', 'Elongated coin', 'Coin weight']),
    S('Medals', 'Struck or cast pieces that mark an event, a work of art, a prize or membership; a state decoration → Orders, decorations & medals.',
      'kinds by purpose: to mark an event, as a work of art, as a prize, as a keepsake, as proof of membership',
      ['Commemorative medal', 'Art medal', 'Award medal', 'Souvenir medal', 'Challenge coin'])]),
 D('Orders, decorations & medals',
   'Honours given by a state or sovereign for bravery, merit, a campaign, service, a rescue or a wound, with the bars and ribbons used to wear them; a prize medal from a club or school → Exonumia; a cup → Trophies & awards.',
   'What was the honour given for: bravery, rank in an order, a campaign, years of service, a rescue or a wound, and is it the award or its mount?',
   [S('Orders, decorations & medals by type', 'Badges, stars and medals awarded by a state, each type named for what it recognises.',
      'kinds by what the award recognises: bravery, rank in an order, a campaign, years of service, a rescue, a wound',
      ['Gallantry and merit decoration', 'Order of chivalry or state order', 'Campaign medal', 'Long-service and good-conduct medal', 'Life-saving medal', 'Wound badge']),
    S('Ribbons, bars & cases', 'Bars, ribbons and cases made to wear or keep medals, not the award itself.',
      'kinds by what is worn or kept',
      ['Medal mounting bar and ribbon'])]),
 D('Trophies & awards',
   'Prizes presented to winners and champions: cups, upright awards, plaques, championship belts and rings; a small award medal → Exonumia.',
   'Is the prize displayed on a shelf, or worn as a belt or ring?',
   [S('Trophies & awards', 'Prizes for winning a contest, shown on a shelf (cups, plaques, shields) or worn by a champion (belts, rings).',
      'kinds by how the prize is kept: displayed piece, worn belt, worn ring',
      ['Trophy or award', 'Championship belt', 'Championship ring'])]),
 D('Grading, holders & mounts',
   'Slabs, cases and mounts that protect one coin, note, card or stamp; the book or box that stores many → Albums & storage.',
   'Is the item sealed by a grading service, or held in an open holder from which it can be removed?',
   [S('Graded slabs', 'Tamper-evident holders in which a grading service seals one item with its grade; an open case with no grade → Open holders & mounts.',
      'kinds by what is sealed inside: coin, banknote, card, comic',
      ['Graded coin slab', 'Graded banknote holder', 'Graded card slab', 'Graded comic slab']),
    S('Open holders & mounts', 'Capsules, flips, sleeves and mounts that hold one item and can be opened.',
      'kinds by the item held: coin or note, card, stamp',
      ['Coin and note holder', 'Card holder', 'Stamp mount and hinge'])]),
 D('Albums & storage',
   'Books, binders, trays, boxes and cabinets that store or show a whole collection; a holder for one item → Grading, holders & mounts.',
   'Is it pages bound in a book, or loose trays, boxes and cabinets?',
   [S('Albums, binders & stock books', 'Books and binders with pages, pockets or strips for one kind of collectable.',
      'kinds by what the pages hold: stamps, covers, coins, notes, cards, stickers',
      ['Stamp album', 'Stock book', 'Cover and postcard album', 'Coin album', 'Banknote album', 'Card binder', 'Sticker album']),
    S('Trays, boxes & cabinets', 'Unbound storage and display: trays for drawers, boxes for shelves, cabinets and display stands.',
      'kinds by how permanent and public the storage is: tray, box, cabinet, display',
      ['Collection tray', 'Storage box', 'Coin cabinet', 'Display case and stand'])]),
]

# every old kind accounted for
placed = {k['n'] for dp in depts for s in dp['s'] for k in s['k']}
lost = [n for n in K if n not in placed]
assert not lost, lost
for n in ['Grading slab', 'Odd and curious money']: assert n not in placed

out = {kk: v for kk, v in src.items() if kk != 'depts'}
out['ax'] = 'What is the object: a coin, a bar or round of metal, a banknote, a stamp or postal item, a card, a token or medal, a state honour, a prize, or something that holds the others?'
out['key'] = [
 '1. Is it a sealed slab, a case, a sleeve or a mount made to protect one coin, note, card or stamp? → Grading, holders & mounts',
 '2. Is it an album, binder, tray, box or cabinet that stores or shows a collection? → Albums & storage',
 '3. Is it a coin, bar or round of precious metal sold for its metal weight? → Bullion',
 '4. Is it a metal coin issued by a state or mint, or coinage of an earlier age, including errors, patterns and copies? → Coins',
 '5. Is it paper or polymer money, or a specimen, error or copy of it? → Banknotes & paper money',
 '6. Is it a stamp, a stamped envelope or card, or a cover that went through the post? → Stamps & postal history',
 '7. Is it a printed card or sticker from a set, sport or game, or a sealed pack of them? → Trading cards',
 '8. Is it a state honour: an order, decoration, or a campaign, service, life-saving or wound award? → Orders, decorations & medals',
 '9. Is it a prize for winning, such as a cup, belt, ring or plaque? → Trophies & awards',
 '10. Is it a token, an altered coin or a medal that is not a state honour? → Exonumia: tokens & medals',
 '<i>Precedence: a legal-tender bullion coin is Bullion (step 3) before Coins (step 4), but a state coin sold above its metal value is Coins. A graded coin is Coins; its slab alone is step 1. A medal given by a state for service is step 8; one given by a club, school or event is step 10.</i>',
]
out['depts'] = depts
tmp = R + 'out/F3.json.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/F3.json')
rp = R + 'out/F3_renames.json'
json.dump(renames, open(rp + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(rp + '.tmp', rp)
print('demoted', len(demoted)); print('kinds', len(placed))
