import re, json
from lib import *

REP = []
BBC = WP + 'Baseball_card'
POK = WP + 'List_of_Pok%C3%A9mon_Trading_Card_Game_sets'
MTG = WP + 'List_of_Magic:_The_Gathering_sets'
ERAS = ['Before 1946', '1946-1979', '1980-1999', '2000 onward']

def era(x):
    m = re.search(r'(1[89]\d\d|20\d\d)', str(x.get('y', ''))) or re.search(r'(1[89]\d\d|20\d\d)', x['n'])
    if not m: return '2000 onward'
    y = int(m.group(1))
    return ERAS[0] if y < 1946 else ERAS[1] if y < 1980 else ERAS[2] if y < 2000 else ERAS[3]

def B(n, y, d, mk='', v=None, role=None):
    return E(n, d, y=y, mk=mk, s=BBC, v=v, role=role)

def sports(d):
    k = kind(d, 'Base card')
    add(k, [
        B('1909-1911 E90-1 American Caramel', '1909', 'Caramel-company baseball set of the period.', 'American Caramel'),
        B('1911 Zee Nut', '1911', 'Card set introduced by a confectionery brand.', 'Zee Nut'),
        B('1914 Cracker Jack', '1914', 'First of two Cracker Jack issues, with major and Federal League players.', 'Cracker Jack'),
        B('1933 World Wide Gum', '1933', 'Montreal issue closely resembling Goudey.', 'World Wide Gum'),
        B('1948 Bowman', '1948', 'Set with which Bowman resumed US card production; the major producer to 1952.', 'Bowman'),
        B('1948 Leaf', '1948', 'Leaf Candy Company set; the company left the card industry by 1950.', 'Leaf'),
        B('1948 Topps Magic Photos', '1948', 'Topps issue four years before its first traditional set.', 'Topps'),
        B('1951 Bowman', '1951', "Set holding Mickey Mantle's true rookie card.", 'Bowman'),
        B('1959 Fleer Ted Williams', '1959', "Fleer's national set built on an exclusive Williams contract.", 'Fleer'),
        B('1960 Fleer Baseball Greats', '1960', 'Set of retired players after Williams retired.', 'Fleer'),
        B('1963 Fleer', '1963', 'Failed 67-card set of active players, most of whom were under Topps contracts.', 'Fleer'),
        B('1965 O-Pee-Chee', '1965', 'Canadian licensed Topps sets from 1965; French text was added in 1970.', 'O-Pee-Chee'),
        B('Topps Venezuela', '1959', 'Licensed Topps sets in Spanish, including winter league players, 1959-1977.', 'Topps'),
        B('1976 TCMA / SSPC', '1976', '630-card Major League set sold mainly by mail order.', 'TCMA'),
        B('1981 Fleer', '1981', "One of the first challengers to Topps after court rulings.", 'Fleer'),
        B('1981 Donruss', '1981', 'The other challenger, with a jigsaw puzzle piece in each pack.', 'Donruss'),
        B('1984 Donruss', '1984', 'Popular set with the Don Mattingly rookie card.', 'Donruss'),
        B('1985-1988 Leaf (Canada)', '1985', 'Bilingual Canadian version of Donruss sets.', 'Leaf'),
        B('1988 Score', '1988', 'Entry of Score into the market, later Pinnacle Brands.', 'Score'),
        B('1989 Bowman revival', '1989', 'Topps reissue of the Bowman name.', 'Topps'),
        B('1990 Futera', '1990', 'First Australian baseball cards, for the Australian Baseball League.', 'Futera'),
        B('1990 Leaf', '1990', 'Premium brand of Donruss.', 'Donruss'),
        B('1991 Fleer Ultra', '1991', 'Premium Fleer brand.', 'Fleer'),
        B('1992 Pinnacle', '1992', 'Premium brand of Score.', 'Score'),
        B('1993 Fleer Flair', '1993', 'Super-premium set.', 'Fleer'),
        B('1987-1988 Topps UK', '1987', 'Two unsuccessful series for British audiences.', 'Topps'),
        B('2012-2013 Select Australia', '2012', 'Australian team sets.', 'Select'),
        B('2013-2014 Dingo', '2013', 'Australian team sets.', 'Dingo'),
        B('2021 Topps NPB', '2021', 'Japanese league cards in the same design as MLB releases.', 'Topps'),
    ])
    for x in k['x']:
        if x['n'] in ('1933 Goudey', '1952 Topps'):
            x['role'] = 'landmark'; x['s'] = BBC
        if x['n'] == '1989 Upper Deck': x['role'] = 'landmark'; x['s'] = BBC
        if x['n'] == 'Topps Finest' and not x.get('v'): x['s'] = BBC
    promote_m(k, REP)
    for x in k['x']: x['g'] = era(x)
    k['nl'] = 'One entry is a trading-card set or brand line issued under one publisher and year or brand; named card numbers are versions only where a source names them.'
    k['sel'] = ("Sets and brands named in Wikipedia's Baseball card article (1888 to 2021), plus the earlier catalogue-pass flagship sets across baseball, basketball, football, hockey and "
                "football (soccer) lines; the Beckett Topps history could not be fetched, so the full year-by-year Topps run is not covered.")
    k['xg'] = 'by era of issue'
    order(k, ERAS)

    k = kind(d, 'Vintage tobacco and candy card')
    k['n'] = 'Vintage tobacco, candy and food card'
    add(k, [
        B('Goodwin Champions', '1888', 'Cigarette card of King Kelly; an early use of chromolithography for multicolour player images.', 'Goodwin'),
        B('Breisch-Williams', '1903', 'First major set of the 20th century, issued by a Pennsylvania confectionery company.', 'Breisch-Williams'),
        B('1909 Cabañas', '1909', 'Among the earliest Cuban sets.', 'Cabañas'),
        B('1912 Imperial Tobacco', '1912', 'Among the earliest Canadian sets.', 'Imperial Tobacco'),
        B('1927 York Caramel', '1927', 'York, Pennsylvania set that restarted production after a lull.', 'York Caramel'),
        B('1922-1923 American Caramel', '1922', 'Return of the company as a producer.', 'American Caramel'),
        B('1928 Yuengling, Harrington, Sweetman and Tharp ice cream cards', '1928', 'Four ice cream companies issuing cards like the York Caramel set.', ''),
        B('1960-1963 Post Cereal', '1960', 'Cards printed on cereal packaging.', 'Post'),
        B('1962-1963 Jell-O', '1962', 'Cards on dessert packaging.', 'Jell-O'),
        B('Kellogg\'s 3-D', '1970', '3D cards inserted with cereal, 1970s.', "Kellogg's"),
        B('Hostess', '1970', 'Cards printed on baked-goods packages, 1970s.', 'Hostess'),
    ])
    for x in k['x']:
        if x['n'] == 'T206':
            x['role'] = 'landmark'; x['s'] = BBC
            if not x.get('y'): x['y'] = '1909'
    for x in k['x']: x['g'] = era(x)
    k['nl'] = 'One entry is a card set issued with tobacco, sweets, snacks or other goods.'
    k['sel'] = "Sets named in Wikipedia's Baseball card article (tobacco, caramel, ice cream, cereal and bakery issues) plus the earlier catalogue-pass T206 and Allen & Ginter lines."
    k['xg'] = 'by era of issue'
    order(k, ERAS)
    kk = kind(d, 'Cigarette and trade card')
    for x in kk['x']: x['g'] = 'Britain and Europe'
    kk['nl'] = 'One entry is a cigarette or trade-card series by one issuer; series are versions where the maker numbered them.'
    kk['sel'] = 'No whole-space reference exists; entries come from the earlier catalogue pass (Wills, Player, Ogden, Liebig, Brooke Bond).'
    kk['xg'] = 'by region'

    k = kind(d, 'Insert card')
    add(k, [B('Donruss Diamond Kings', '1992', 'Gold-foil insert cards that drove the chase for inserts.', 'Donruss'),
            B('Fleer All-Stars and Rookie Sensations', '1992', 'Gold-foil insert cards.', 'Fleer')])
    k = kind(d, 'Parallel card')
    add(k, [B('Topps Gold', '1992', 'Gold-foil parallel of each base-set card.', 'Topps'),
            B('Topps Tiffany', '1984', 'Premium parallel versions sold only as box sets at hobby shops.', 'Topps'),
            B('Fleer Flair Showcase Masterpieces', '1997', 'The first one-of-one cards.', 'Fleer'),
            B('Topps Finest refractors', '1993', 'First set to use refractors.', 'Topps')])
    for x in k['x']:
        if x['n'] == 'Refractor': x['s'] = BBC
    for n in ('Rookie card', 'Insert card', 'Parallel card', 'Autograph card', 'Relic and memorabilia card'):
        kk = kind(d, n)
        promote_m(kk, REP)
        for x in kk['x']: x['g'] = era(x)
        kk['nl'] = {'Rookie card': 'One entry is a named rookie card, one player in one set.',
                    'Insert card': 'One entry is an insert set or line.', 'Parallel card': 'One entry is a parallel line or finish.',
                    'Autograph card': 'One entry is an autograph set or line.', 'Relic and memorabilia card': 'One entry is a relic or memorabilia set or line.'}[n]
        kk['sel'] = "Lines named in Wikipedia's Baseball card article plus the earlier catalogue pass; no whole-space reference exists below set level."
        kk['xg'] = 'by era of issue'
        order(kk, ERAS)

def tcg(d):
    sec = section(d, 'Trading cards', 'Games, non-sports & stickers')
    # move set-level entries out of the singles kind
    single = kind(d, 'Trading-card game single')
    moved = [x for x in single['x'] if x['n'] in ('Pokémon Base Set', 'Yu-Gi-Oh! early English sets', 'One Piece Card Game')]
    single['x'] = [x for x in single['x'] if x not in moved]
    pok = [
        ('First generation (1998-2000)', [('1998 Pokémon Demo Game Plastic Pack', 1998), ('Jungle', 1999), ('Fossil', 1999), ('Base Set 2', 2000), ('Team Rocket', 2000), ('Gym Heroes', 2000), ('Gym Challenge', 2000)]),
        ('Second generation (2000-2003)', [('Neo Genesis', 2000), ('Neo Discovery', 2001), ('Southern Islands', ''), ('Neo Revelation', 2001), ('Neo Destiny', 2002), ('Legendary Collection', 2002), ('Expedition Base Set', 2002), ('Aquapolis', 2003), ('Skyridge', 2003)]),
        ('Third generation, EX era (2003-2007)', [('EX Ruby and Sapphire', 2003), ('EX Sandstorm', 2003), ('EX Dragon', 2003), ('EX Team Magma vs Team Aqua', 2004), ('EX Hidden Legends', 2004), ('EX FireRed and LeafGreen', 2004), ('EX Team Rocket Returns', 2004), ('EX Deoxys', 2005), ('EX Emerald', 2005), ('EX Unseen Forces', 2005), ('EX Delta Species', 2005), ('EX Legend Maker', 2006), ('EX Holon Phantoms', 2006), ('EX Crystal Guardians', 2006), ('EX Dragon Frontiers', 2006), ('EX Power Keepers', 2007)]),
        ('Fourth generation, Diamond & Pearl to HeartGold & SoulSilver (2007-2011)', [('Diamond and Pearl Base Set', 2007), ('Diamond and Pearl Mysterious Treasures', 2007), ('Diamond and Pearl Secret Wonders', 2007), ('Diamond and Pearl Great Encounters', 2008), ('Diamond and Pearl Majestic Dawn', 2008), ('Diamond and Pearl Legends Awakened', 2008), ('Diamond and Pearl Stormfront', 2008), ('Platinum Base Set', 2009), ('Platinum Rising Rivals', 2009), ('Platinum Supreme Victors', 2009), ('Platinum Arceus', 2009), ('HeartGold & SoulSilver', ''), ('HS Unleashed', ''), ('HS Undaunted', ''), ('HS Triumphant', ''), ('Call of Legends', ''), ('Lost Link', '')]),
        ('Fifth generation, Black & White (2011-2013)', [('Black & White', 2011), ('Black & White Emerging Powers', 2011), ('Black & White Noble Victories', 2011), ('Black & White Next Destinies', 2012), ('Black & White Dark Explorers', 2012), ('Black & White Dragons Exalted', 2012), ('Black & White Dragon Vault', 2012), ('Black & White Boundaries Crossed', 2012), ('Black & White Plasma Storm', 2013), ('Black & White Plasma Freeze', 2013), ('Black & White Plasma Blast', 2013), ('Black & White Legendary Treasures', 2013)]),
        ('Sixth generation, XY (2013-2016)', [('XY Kalos Starter Set', 2013), ('XY', 2014), ('XY Flashfire', 2014), ('XY Furious Fists', 2014), ('XY Phantom Forces', 2014), ('XY Primal Clash', 2015), ('XY Double Crisis', 2015), ('XY Roaring Skies', 2015), ('XY Ancient Origins', 2015), ('XY BREAKthrough', 2015), ('XY BREAKpoint', 2016), ('XY Generations', 2016), ('XY Fates Collide', 2016), ('XY Steam Siege', 2016), ('XY Evolutions', 2016)]),
        ('Seventh generation, Sun & Moon (2017-2019)', [('Sun & Moon', 2017), ('Sun & Moon Guardians Rising', 2017), ('Sun & Moon Burning Shadows', 2017), ('Sun & Moon Shining Legends', 2017), ('Sun & Moon Crimson Invasion', 2017), ('Sun & Moon Ultra Prism', 2018), ('Sun & Moon Forbidden Light', 2018), ('Sun & Moon Celestial Storm', 2018), ('Dragon Majesty', 2018), ('Sun & Moon Lost Thunder', 2018), ('Sun & Moon Team Up', 2019), ('Detective Pikachu', 2019), ('Sun & Moon Unbroken Bonds', 2019), ('Sun & Moon Unified Minds', 2019), ('Hidden Fates', 2019), ('Sun & Moon Cosmic Eclipse', 2019)]),
        ('Sword & Shield (2020-2023)', [('Sword & Shield', 2020), ('Sword & Shield Rebel Clash', 2020), ('Sword & Shield Darkness Ablaze', 2020), ("Champion's Path", 2020), ('Sword & Shield Vivid Voltage', 2020), ('Shining Fates', 2021), ('Sword & Shield Battle Styles', 2021), ('Sword & Shield Chilling Reign', 2021), ('Sword & Shield Evolving Skies', 2021), ('Celebrations', 2021), ('Sword & Shield Fusion Strike', 2021), ('Sword & Shield Brilliant Stars', 2022), ('Sword & Shield Astral Radiance', 2022), ('Pokémon GO', 2022), ('Sword & Shield Lost Origin', 2022), ('Sword & Shield Silver Tempest', 2022), ('Crown Zenith', 2023)]),
        ('Scarlet & Violet (2023-2025)', [('Scarlet & Violet', 2023), ('Scarlet & Violet Paldea Evolved', 2023), ('Scarlet & Violet Obsidian Flames', 2023), ('Scarlet & Violet 151', 2023), ('Scarlet & Violet Paradox Rift', 2023), ('Scarlet & Violet Paldean Fates', 2024), ('Scarlet & Violet Temporal Forces', 2024), ('Scarlet & Violet Twilight Masquerade', 2024), ('Scarlet & Violet Shrouded Fable', 2024), ('Scarlet & Violet Stellar Crown', 2024), ('Scarlet & Violet Surging Sparks', 2024), ('Scarlet & Violet Prismatic Evolutions', 2025), ('Scarlet & Violet Journey Together', 2025), ('Scarlet & Violet Destined Rivals', 2025), ('Scarlet & Violet Black Bolt and White Flare', 2025)]),
        ('Mega Evolution (2025 onward)', [('Mega Evolution', 2025), ('Mega Evolution Phantasmal Flames', 2025), ('Mega Evolution Ascended Heroes', 2026), ('Mega Evolution Perfect Order', 2026), ('Mega Evolution Chaos Rising', 2026), ('Mega Evolution Pitch Black', 2026)]),
    ]
    new = []
    for g, rows in pok:
        for n, y in rows:
            new.append(E('Pokémon ' + n if not n.startswith('Pokémon') and not n.startswith('1998') else n,
                         'Pokémon Trading Card Game set.' , y=y, mk='Wizards of the Coast' if g.startswith(('First', 'Second')) else '',
                         g='Pokémon: ' + g, s=POK))
    for x in moved:
        x['g'] = 'Pokémon: First generation (1998-2000)' if x['n'] == 'Pokémon Base Set' else ('Yu-Gi-Oh!' if x['n'].startswith('Yu') else 'One Piece')
        if x['n'] == 'Pokémon Base Set': x['y'] = '1999'; x['s'] = POK
    mtg = [('Alpha', 1993, 'Core'), ('Beta', 1993, 'Core'), ('Unlimited', 1993, 'Core'), ('Revised', 1994, 'Core'), ('Fourth Edition', 1995, 'Core'), ('Fifth Edition', 1997, 'Core'),
           ('Classic Sixth Edition', 1999, 'Core'), ('Seventh Edition', 2001, 'Core'), ('Eighth Edition', 2003, 'Core'), ('Ninth Edition', 2005, 'Core'), ('Tenth Edition', 2007, 'Core'),
           ('Magic 2010', 2009, 'Core'), ('Magic 2011', 2010, 'Core'), ('Magic 2012', 2011, 'Core'), ('Magic 2013', 2012, 'Core'), ('Magic 2014', 2013, 'Core'), ('Magic 2015', 2014, 'Core'),
           ('Magic Origins', 2015, 'Core'), ('Core Set 2019', 2018, 'Core'), ('Core Set 2020', 2019, 'Core'), ('Core Set 2021', 2020, 'Core'), ('Foundations', 2024, 'Core')]
    exp = {1995: ['Ice Age'], 1996: ['Mirage'], 1997: ['Tempest'], 1998: ["Urza's Saga"], 1999: ['Mercadian Masques'], 2000: ['Invasion'], 2001: ['Odyssey'], 2002: ['Onslaught'],
           2003: ['Mirrodin'], 2004: ['Champions of Kamigawa'], 2005: ['Ravnica: City of Guilds'], 2006: ['Time Spiral'], 2007: ['Lorwyn'], 2008: ['Shadowmoor'],
           2011: ['Innistrad'], 2012: ['Return to Ravnica'], 2014: ['Khans of Tarkir'], 2015: ['Battle for Zendikar'], 2016: ['Shadows over Innistrad', 'Kaladesh'],
           2017: ['Amonkhet', 'Ixalan'], 2018: ['Dominaria', 'Guilds of Ravnica'], 2019: ['Ravnica Allegiance', 'War of the Spark', 'Throne of Eldraine', 'Theros Beyond Death'],
           2020: ['Ikoria: Lair of Behemoths', 'Zendikar Rising'],
           2021: ['Kaldheim', 'Strixhaven', 'Adventures in the Forgotten Realms', 'Innistrad: Midnight Hunt', 'Innistrad: Crimson Vow', 'Kamigawa: Neon Dynasty'],
           2022: ['Streets of New Capenna', 'Dominaria United', "The Brothers' War", 'Phyrexia: All Will Be One'],
           2023: ['March of the Machine', 'Wilds of Eldraine', 'The Lost Caverns of Ixalan', 'Murders at Karlov Manor'],
           2024: ['Outlaws of Thunder Junction', 'Bloomburrow', 'Duskmourn: House of Horror'],
           2025: ['Aetherdrift', 'Tarkir: Dragonstorm', 'Final Fantasy', 'Edge of Eternities', 'Avatar: The Last Airbender', "Marvel's Spider-Man"],
           2026: ['Lorwyn Eclipsed', 'Secrets of Strixhaven', 'Marvel Super Heroes']}
    for n, y, t in mtg:
        new.append(E('Magic: ' + n, 'Magic: The Gathering core set.', y=y, mk='Wizards of the Coast', g='Magic: The Gathering core sets', s=MTG,
                     role='origin' if n == 'Alpha' else None))
    for y, ns in sorted(exp.items()):
        for n in ns:
            new.append(E('Magic: ' + n, 'Magic: The Gathering large expansion (250 cards or more).', y=y, mk='Wizards of the Coast', g='Magic: The Gathering large expansions', s=MTG))
    kset = {'n': 'Trading-card game set', 'a': 'TCG set · expansion', 'd': 'Complete set or expansion of a trading-card game, collected as a whole or by sealed product.',
            's': POK, 'x': moved + new, 'tt': [['Print run', ['First edition', 'Unlimited', 'Reprint']], ['Language', ['English', 'Japanese', 'Other']]],
            'nl': 'One entry is a released set or expansion of one trading-card game; sealed-product types and print runs are attributes.',
            'sel': ("Pokémon Trading Card Game sets from Wikipedia's list (first to Mega Evolution series, English-language sets); Magic: The Gathering core sets and expansions of 250 cards or more "
                    "from Wikipedia's list (the early sets under 250 cards, supplements and Commander products are out of scope); Yu-Gi-Oh! and One Piece from the earlier pass."),
            'xg': 'by game, then series', 'see': [['C1', 'Game systems and trading-card games']], 'm': [], 'r': []}
    # drop invalid 'see' reference unless valid
    kset.pop('see')
    if not any(k['n'] == kset['n'] for k in sec['k']):
        idx = [k['n'] for k in sec['k']].index('Trading-card game single') + 1
        sec['k'].insert(idx, kset)
    single['nl'] = 'One entry is a named single card or a group of printings of one card.'
    single['sel'] = 'The earlier catalogue pass; no whole-space reference exists for single cards.'
    single['xg'] = 'by game'
    for x in single['x']: x['g'] = 'Magic: The Gathering' if x['n'].startswith('Magic') else 'Yu-Gi-Oh!' if 'Eyes' in x['n'] else 'Pokémon'
    for n in ('Non-sports trading card', 'Collectible sticker'):
        kk = kind(d, n)
        promote_m(kk, REP)
        for x in kk['x']: x['g'] = x.get('g') or x.get('mk') or ''
        kk['nl'] = 'One entry is a non-sports card or sticker set or line by one publisher.'
        kk['sel'] = 'No whole-space reference exists; entries come from the earlier catalogue pass.'
        kk['xg'] = 'by publisher'

def generic(d):
    notes = {
        'Coins': ('One entry is a named coin type, series or tradition of one issuer or civilisation; mint marks and years are versions.',
                  'No whole-space reference exists; entries come from the earlier catalogue pass (Wikipedia coin articles and Numista).'),
        'Exonumia: tokens & medals': ('One entry is a named token, altered-coin or medal series; dates and issuers are versions.',
                                     'No whole-space reference exists; entries come from the earlier catalogue pass.'),
        'Orders, decorations & medals': ('One entry is a named order, decoration or medal of one country.', 'By country from the fetched Wikipedia lists.'),
        'Trophies & awards': ('One entry is a named trophy, belt or ring.', 'No whole-space reference exists; entries come from the earlier catalogue pass.'),
        'Grading, holders & mounts': ('One entry is a grading service slab or a holder brand; label tiers and generations are versions.',
                                      'The grading-services register (PCGS, NGC, PMG, PSA, BGS, SGC, CGC, ANACS) in F3_brands.json and the earlier catalogue pass.'),
        'Albums & storage': ('One entry is an album, binder or cabinet brand line; formats are versions.', 'No whole-space reference exists; entries come from the earlier catalogue pass.'),
        'Banknotes & paper money': ('One entry is a named note series.', 'See the kind.'),
        'Stamps & postal history': ('One entry is a named stamp, cover or postal item.', 'See the kind.'),
        'Trading cards': ('One entry is a named card set or line.', 'See the kind.'),
        'Bullion': ('One entry is a named bullion product.', 'See the kind.'),
    }
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k.get('m'): promote_m(k, REP)
                if k.get('x') and not k.get('nl'):
                    k['nl'], k['sel'] = notes[dp['n']] if dp['n'] in notes else ('One entry is a named item of this kind.', 'See the kind.')
                if k.get('x') and not k.get('xg'):
                    gs = {x.get('g') for x in k['x'] if x.get('g')}
                    if gs: k['xg'] = 'by issuer, maker or country'
                    for x in k['x']:
                        if not x.get('g') and x.get('mk'): x['g'] = x['mk']
                if k.get('x'):
                    gs = [x.get('g') for x in k['x'] if x.get('g')]
                    if gs and not k.get('xg'): k['xg'] = 'by maker'

def files(d):
    # renames
    p = W + '/out/F3_renames.json'
    r = json.load(open(W + '/work/V4_F3/bak/F3_renames.json'))
    r['Vintage tobacco and candy card'] = 'Vintage tobacco, candy and food card'
    json.dump(r, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
    # brands
    bp = W + '/out/F3_brands.json'
    b = json.load(open(W + '/work/V4_F3/bak/F3_brands.json'))
    have = {x['n'].casefold() for x in b['b']}
    def nb(n, c, seg, kf, dd, s):
        if n.casefold() in have: return
        b['b'].append({'n': n, 'c': c, 'f': '', 'seg': seg, 'kf': kf, 'd': dd, 's': s}); have.add(n.casefold())
    for n, kf in [('Cracker Jack', 'baseball cards 1914'), ('Zee Nut', 'baseball cards 1911'), ('Score', 'baseball cards 1988'), ('Pinnacle', 'premium cards 1992'),
                  ('Futera', 'Australian baseball cards 1990'), ('TCMA', 'SSPC 1976 set'), ('Hostess', 'baked-goods cards'), ("Kellogg's", '3-D cards'),
                  ('Post', 'cereal cards 1960-1963'), ('Jell-O', 'dessert cards 1962-1963'), ('American Caramel', 'E90-1 set'), ('York Caramel', '1927 set'),
                  ('World Wide Gum', '1933 Montreal set'), ('The Pokémon Company', 'Pokémon Trading Card Game'), ('Select', 'Australian team sets'), ('Dingo', 'Australian team sets')]:
        nb(n, '', 'Heritage manufactory', kf, 'Card or card-package publisher named in the baseball card article.', BBC)
    for n, c in [('Israel Mint', 'Israel'), ('Baird & Co', 'United Kingdom'), ('KOMSCO', 'South Korea'), ('Highland Mint', 'United States'),
                 ('National Bank of Poland', 'Poland'), ('Central Bank of the Russian Federation', 'Russia'), ('National Bank of Ukraine', 'Ukraine'),
                 ('Royal Australian Mint', 'Australia'), ('Reserve Bank of India', 'India'), ('South African Reserve Bank', 'South Africa')]:
        nb(n, c if n != 'Baird & Co' and n != 'Highland Mint' else '', 'Institution & issuer', 'bullion or currency issuer', 'Issuer named by the bullion list or currency articles.', 'https://en.wikipedia.org/wiki/List_of_bullion_coins')
    b['b'].sort(key=lambda x: x['n'].casefold())
    json.dump(b, open(bp + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(bp + '.tmp', bp)

def run(d):
    sports(d); tcg(d); generic(d); files(d)
    return REP
