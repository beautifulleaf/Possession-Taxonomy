import json, copy, os, glob
R = '/home/user/Possession-Taxonomy/rebuild/'
d = json.load(open(R + 'work/STR_I2/bak/I2.json'))
K = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
WP = 'https://en.wikipedia.org/wiki/'

def demote(kn, an, to='m'):
    k = K[kn]
    for a in list(k.get('x', [])):
        if a['n'] == an:
            k['x'].remove(a)
            lst = k.setdefault(to, [])
            items = [[a['n'], a.get('mk', '')]] + [[v['n'], v.get('mk', '') or a.get('mk', '')] for v in a.get('v', [])]
            if to == 'r':
                items = items[:1]
            for it in items:
                if it not in lst:
                    lst.append(it)
            return
    raise KeyError((kn, an))

def tt(kn, groups):
    k = K[kn]
    k.pop('t', None)
    k['tt'] = groups

def see(kn, *links):
    K[kn].setdefault('see', []).extend([list(l) for l in links])

# ---- demotions of generic archetypes
for kn, an, to in [
    ('Glove skin', 'CS2 gloves', 'm'), ('Tool and glider skin', 'Fortnite pickaxe and glider', 'm'),
    ('Vehicle skin', 'Rocket League car cosmetics', 'm'), ('Character outfit or skin', 'Dota 2 cosmetic sets', 'm'),
    ('Character outfit or skin', 'Roblox avatar items', 'm'), ('Character outfit or skin', 'Fortnite outfit', 'm'),
    ('Companion or pet', 'Dota 2 courier', 'm'), ('Mount', 'World of Warcraft flying mounts', 'm'),
    ('Housing and décor item', 'Animal Crossing furniture', 'm'), ('Housing and décor item', 'Final Fantasy XIV housing', 'm'),
    ('Housing and décor item', 'Second Life virtual goods', 'm'), ('Housing and décor item', 'Habbo rare furni', 'm'),
    ('In-game sticker, patch or charm', 'CS2 sticker', 'm'), ('In-game sticker, patch or charm', 'CS2 weapon charm', 'm'),
    ('Spray or graffiti', 'CS2 graffiti', 'm'), ('Music kit', 'CS2 music kit', 'm'),
    ('Crate key', 'CS case key', 'm'), ('Loot case, crate or capsule', 'Tournament sticker capsule', 'm'),
    ('Platform profile item', 'Steam animated profile background', 'm'), ('Platform profile item', 'Steam Points Shop game profile', 'm'),
    ('Sewing pattern', "Butterick graded patterns", 'r'), ('Sewing pattern', "McCall's patterns", 'r'),
    ('Sewing pattern', 'Simplicity', 'r'), ('Sewing pattern', 'Burda Style', 'r'),
    ('Knitting or crochet pattern', 'Ravelry pattern store', 'r'),
    ('Sample pack', 'Splice Sounds', 'r'), ('Sample pack', 'Loopmasters packs and Loopcloud', 'r'),
    ('Synth and effect preset pack', 'Serum presets', 'm'), ('HDRI and environment map', 'HDR light probe lighting', 'm'),
    ('Fine-tune or LoRA adapter', None, None)][:-1]:
    demote(kn, an, to)

# ---- Platform profile item split
pp = K.pop('Platform profile item')
xs = {a['n']: a for a in pp.get('x', [])}
STEAM = 'https://steamcommunity.com/tradingcards/faq'
def mk(n, a, dd, s, x=None, m=None):
    k = {'n': n, 'a': a, 'd': dd, 's': s}
    if x: k['x'] = x
    if m: k['m'] = m
    return k
card = mk('Platform trading card', 'Steam trading card · digital card',
          'A digital card that drops or is bought on a platform and is collected into sets to craft badges and profile items.', STEAM, [xs['Steam trading card set']])
badge = mk('Profile badge', 'game badge · pin', 'A badge shown on a platform profile, crafted from a card set or awarded for an event.', STEAM, [xs['Steam game badge']])
bg = mk('Profile background', 'loading screen · animated background', 'An image or looping clip set behind a platform profile or shown as a loading screen.',
        'https://partner.steamgames.com/doc/marketing/pointsshopitems', None, pp['m'])
frame = mk('Avatar and frame', 'avatar frame · profile skin', 'A picture or border worn on a platform profile and shown beside messages.',
           'https://partner.steamgames.com/doc/marketing/pointsshopitems')
emo = mk('Chat emoticon', 'emoji · emote', 'A small picture typed into chat on a platform; some come from trading card sets.', STEAM)
stk = mk('Chat sticker pack', 'messaging stickers', 'A set of large pictures sent in messages, often drawn by one character brand.', 'https://en.wikipedia.org/wiki/Line_Friends', [xs['Line Friends stickers']])
# bg and frame inherit demoted models
bg.pop('m', None)
bg['m'] = [m for m in pp.get('m', []) if 'background' in m[0]]
frame['m'] = [m for m in pp.get('m', []) if 'background' not in m[0]]
for k in (card, badge, bg, frame, emo, stk):
    K[k['n']] = k
tt('Platform trading card', [['Finish', ['Normal', 'Foil']]])
tt('Profile badge', [['Source', ['Crafted from a card set', 'Event award']]])
tt('Profile background', [['Surface', ['Profile background', 'Loading screen']], ['Motion', ['Static', 'Animated']]])
tt('Avatar and frame', [['Part', ['Avatar', 'Avatar frame']]])
tt('Chat emoticon', [['Form', ['Still emoticon', 'Animated emoticon']]])
tt('Chat sticker pack', [['Form', ['Still sticker', 'Animated sticker']]])

# ---- new kinds
K['Pixel and bitmap typeface'] = mk('Pixel and bitmap typeface', 'bitmap font · raster font · pixel font',
    'A face stored as a grid of pixels for each glyph, with a separate set of images for each size and style.', WP + 'Bitmap_font')
tt('Pixel and bitmap typeface', [['Storage', ['Bitmap (raster) font', 'Pixel font for very small sizes']], ['File format', ['PSF', 'PCF']]])
K['Stock video clip'] = mk('Stock video clip', 'stock footage', 'A licensed film or video clip sold for reuse in other work.', WP + 'Stock_footage')
tt('Stock video clip', [['Licence', ['Royalty-free', 'Rights-managed']]])
K['In-game currency'] = mk('In-game currency', 'virtual currency · gems · coins', 'A balance spent inside a game or platform to buy items, keys or passes; some can be bought, others only earned.', WP + 'Virtual_currency')
tt('In-game currency', [['Source', ['Bought with real money', 'Earned in play']], ['Reach', ['Closed to one game', 'Shared across a platform']]])
K['Battle pass'] = mk('Battle pass', 'rewards track · season pass', 'A tiered track of rewards unlocked by play over a season, with a free and a paid version.', WP + 'Battle_pass', [
    {'n': 'Dota 2 Compendium', 'a': '', 'd': "Valve's 2013 event pass sold around The International; the first battle pass.", 'mk': 'Valve', 'y': '2013', 's': WP + 'Battle_pass', 'v': []},
    {'n': 'Fortnite Battle Pass', 'a': '', 'd': 'Season pass that made the model common from 2018.', 'mk': 'Epic Games', 'y': '2018', 's': WP + 'Battle_pass', 'v': []}])
tt('Battle pass', [['Track', ['Free track', 'Premium track']], ['Length', ['Season', 'Event']]])
K['Ticket or membership token'] = mk('Ticket or membership token', 'access pass token · event ticket NFT',
    'A token that proves a right to enter an event or join a private online club.', WP + 'Non-fungible_token')
tt('Ticket or membership token', [['Right', ['Event ticket', 'Access pass', 'Club membership']]])

# ---- tt for existing kinds
tt('Sans-serif typeface', [['Construction', ['Grotesque', 'Neo-grotesque', 'Geometric', 'Humanist']]])
tt('Serif typeface', [['Style class', ['Venetian', 'Garalde', 'Transitional', 'Didone', 'Incised']]])
tt('Slab-serif typeface', [['Slab shape', ['Bracketed (Clarendon style)', 'Unbracketed (geometric)']]])
tt('Script and handwriting typeface', [['Hand', ['Calligraphic', 'Brush', 'Casual handwriting']]])
tt('Display and decorative typeface', [['Treatment', ['Poster', 'Stencil', 'Decorative', 'Inline and shadow']]])
tt('Monospaced and coding typeface', [['Design', ['Typewriter slab', 'Programming with ligatures', 'Terminal bitmap-style']]])
tt('Blackletter typeface', [['Hand', ['Textura', 'Rotunda', 'Schwabacher', 'Fraktur']]])
tt('Non-Latin script typeface', [['Writing system', ['CJK (Chinese, Japanese, Korean)', 'Arabic and Nastaliq', 'Indic scripts', 'Greek and Cyrillic']], ['Coverage', ['Single script', 'Pan-script']]])
tt('Icon and symbol font', [['Content', ['Dingbats', 'Web icon font', 'Colour emoji font']]])

tt('Design template', [['Subject', ['Social media', 'Presentation', 'CV and résumé', 'Print', 'Mockup', 'Website theme']]])
tt('Digital planner', [['Format', ['Hyperlinked PDF', 'Notes-app planner']]])
tt('Stock photo or illustration', [['Content', ['Photo', 'Vector illustration']], ['Licence', ['Royalty-free', 'Rights-managed']]])
tt('Icon set', [['File format', ['ICO (Windows)', 'ICNS (Macintosh)', 'PNG', 'Vector']]])
tt('Brush pack', [['Program', ['Procreate', 'Photoshop ABR', 'Krita']]])
tt('Texture and background pack', [['Content', ['Seamless texture', 'Background', 'Frame']]])
tt('Motion graphics template', [['Program', ['After Effects', 'Premiere Pro MOGRT', 'DaVinci Resolve', 'Final Cut']]])
tt('Photo preset pack', [['App', ['Lightroom desktop', 'Lightroom mobile']], ['Look', ['Film emulation']]])
tt('LUT pack', [['File format', ['CUBE', '3DL']], ['Purpose', ['Film emulation', 'Log-to-Rec.709 conversion']]])
tt('Sewing pattern', [['Delivery', ['Printable PDF (A4/Letter)', 'Copy-shop large format', 'Projector file']], ['Sizing', ['Graded multi-size', 'Single size']]])
tt('Knitting or crochet pattern', [['Notation', ['Chart', 'Written row-by-row']], ['Item', ['Garment', 'Accessory']]])
tt('Cross-stitch or embroidery chart', [['Hand stitching', ['Counted cross-stitch chart', 'Stamped design']], ['Machine file format', ['DST (Tajima and others)', 'PES (Brother, Baby Lock)', 'JEF (Janome)', 'VP3 (Pfaff, Husqvarna Viking)']]])
tt('Papercraft and cutting file', [['Use', ['Cut file for a home cutting machine', 'Vinyl template', 'Printable papercraft (fold and glue)']]])
tt('3D model', [['Content', ['Character', 'Prop', 'Scene']], ['File format', ['OBJ', 'FBX', 'glTF', 'USD']]])
tt('3D-printable model', [['File format', ['STL', '3MF', 'OBJ', 'AMF']]])
tt('Avatar model', [['Dimension', ['3D', '2D']], ['Platform', ['VRM', 'VRChat', 'Live2D']]])
tt('3D material', [['Type', ['PBR texture set', 'Procedural shader']]])
tt('HDRI and environment map', [['Setting', ['Studio', 'Outdoor', 'Interior']]])
tt('Sample pack', [['Content', ['Loops', 'One-shots', 'Construction kit']], ['File format', ['WAV', 'REX']]])
tt('Virtual instrument library', [['Instrument family', ['Orchestral', 'Piano', 'Drums']], ['Player', ['Kontakt format', 'Standalone player']]])
tt('Synth and effect preset pack', [['Loaded into', ['Synthesiser patch', 'Effect chain']]])
tt('MIDI file', [['Standard MIDI File format', ['Type 0 (single track)', 'Type 1 (multi-track)']]])
tt('SoundFont and sample-format bank', [['Format', ['SF2', 'SF3 (OGG compressed)', 'SFZ (plain text)', 'Kontakt NKI', 'GigaStudio']]])
tt('Language model weights', [['File format', ['safetensors', 'GGUF']], ['Precision', ['Full precision', 'Quantised (4-bit, 8-bit)']], ['Training stage', ['Base', 'Instruction-tuned']]])
tt('Image-generation model', [['Training stage', ['Base model', 'Distilled']], ['File format', ['Checkpoint', 'safetensors']]])
tt('Fine-tune or LoRA adapter', [['Method', ['LoRA adapter', 'Full fine-tune', 'Merged checkpoint']], ['Base model', ['Image model', 'Language model']]])
tt('Speech and audio model', [['Task', ['Speech recognition', 'Text-to-speech', 'Music generation']]])

tt('Weapon skin', [['Wear band (Counter-Strike)', ['Factory New', 'Minimal Wear', 'Field-Tested', 'Well-Worn', 'Battle-Scarred']], ['Counter (Counter-Strike)', ['None', 'StatTrak', 'Souvenir']], ['Upgrade (Valorant)', ['Variant colours', 'Animation and finisher levels']]])
tt('Knife skin', [['Finish', ['Vanilla (no finish)', 'Solid and patterned', 'High-gloss anodized', 'Doppler phases']]])
tt('Glove skin', [['Wear band', ['Factory New', 'Minimal Wear', 'Field-Tested', 'Well-Worn', 'Battle-Scarred']]])
tt('Tool and glider skin', [['Item', ['Pickaxe', 'Glider', 'Trail']]])
tt('Vehicle skin', [['Part', ['Car body', 'Wheels', 'Decal', 'Boost', 'Paint finish']], ['Origin', ['In-game design', 'Licensed crossover']]])
tt('Wrap', [['Applied to', ['Weapon', 'Vehicle']]])
tt('Character outfit or skin', [['Source', ['Shop', 'Battle pass', 'Licensed collaboration']]])
tt('Avatar accessory', [['Worn on', ['Back (back bling)', 'Head (hat)', 'Banner']], ['Supply', ['Standard', 'Limited']]])
tt('Emote', [['Motion', ['Dance', 'Gesture']], ['Origin', ['In-game', 'Licensed']]])
tt('Companion or pet', [['Role', ['Minion', 'Collectible pet']], ['Origin', ['Earned in play', 'Promotional']]])
tt('Mount', [['Movement', ['Ground', 'Flying']], ['Origin', ['Earned in play', 'Promotional']]])
tt('Housing and décor item', [['Item', ['Furniture', 'Wallpaper and floor', 'Garden item']], ['Maker', ['Developer-made', 'Player-made virtual good']]])
tt('In-game sticker, patch or charm', [['Subject', ['Team sticker', 'Autograph sticker', 'Agent patch', 'Weapon charm']]])
tt('Spray or graffiti', [['Finish', ['Sealed graffiti', 'Colour tint']]])
tt('Music kit', [['Counter', ['Standard kit', 'StatTrak kit (counts MVPs)']]])
tt('Loot case, crate or capsule', [['Opening', ['Needs a key', 'Opens without a key']], ['Contents', ['Weapon skins', 'Stickers', 'Graffiti', 'Patches', 'Music kits', 'Souvenir weapon skins']]])
tt('Crate key', [['Game', ['Counter-Strike case key', 'Team Fortress 2 key']]])

tt('E-book', [['Layout', ['Reflowable', 'Fixed-layout']], ['File format', ['EPUB', 'Kindle AZW3/KF8 or KFX', 'Mobipocket (MOBI)', 'FictionBook (FB2)', 'Apple Books (iBooks)', 'PDF', 'OpenXPS', 'DjVu scan', 'Plain text or word-processor file (TXT, RTF, DOC, DOCX)']]])
tt('Comic or manga file', [['Archive format', ['CBZ (ZIP)', 'CBR (RAR)', 'CB7 (7z)', 'CBT (TAR)', 'CBA (ACE)']], ['Reading mode', ['Page by page (PDF or EPUB fixed layout)', 'Vertical scroll (webtoon)']]])
tt('Digital sheet music', [['Form', ['Printable PDF score', 'Interactive score in an app']]])
tt('Digital music file', [['Encoding', ['FLAC (lossless)', 'ALAC (lossless)', 'WAV (uncompressed)', 'DSD (high resolution)', 'MP3 (lossy)', 'AAC (lossy)']]])
tt('Audiobook file', [['Rights', ['Open file', 'Locked to an account']], ['Text', ['Abridged', 'Unabridged']]])
tt('Podcast episode file', [['Medium', ['Audio episode', 'Video episode']]])
tt('Digital video', [['Holding', ['MP4 file', 'MKV file', 'Locker entitlement']]])
tt('Digital photo or image', [['Compression', ['Camera raw (DNG and maker formats)', 'Lossy (JPEG, HEIC, WebP, AVIF)', 'Lossless (PNG, TIFF, GIF, BMP)']]])
tt('Editable graphics file', [['Structure', ['Layered raster (PSD, XCF)', 'Vector (SVG, AI, EPS)']]])

K['Domain name']['s'] = WP + 'Top-level_domain'
tt('Domain name', [['Ending', ['Generic (.com, .org, .net)', 'Restricted generic (.name)', 'Sponsored (.edu, .museum)', 'Country-code (.de, .uk)', 'Internationalised country-code']]])
tt('Blockchain name', [['Level', ['Top-level name (.eth)', 'Subdomain']]])
tt('Profile-picture (PFP) NFT', [['Supply', ['Unique', 'Multi-edition']]])
tt('Generative art NFT', [['Supply', ['Unique', 'Multi-edition']], ['Code storage', ['Off-chain', 'Fully on-chain']]])
tt('Bitcoin Ordinal inscription', [['Content', ['Image', 'Text', 'Collection']]])
tt('Virtual land parcel', [['Holding', ['Parcel', 'Estate', 'Land with airspace']]])
tt('Game item NFT', [['Item', ['Weapon', 'Character', 'Cosmetic']]])

# ---- see links
see('Sewing pattern', ('C4', 'Sewing pattern', 'the same pattern on paper'))
see('Knitting or crochet pattern', ('C4', 'Sewing or knitting pattern', 'the same pattern on paper'))
see('3D-printable model', ('D1', '3D printer', 'the machine that prints it'))
see('3D model', ('I1', '3D modelling software', 'the program that edits it'))
see('Sample pack', ('I1', 'Sampler & sample player', 'plays the samples'))
see('Virtual instrument library', ('I1', 'Orchestral sample library', 'sold as software'))
see('Digital sheet music', ('F1', 'Full score', 'printed score'))
see('Digital planner', ('C5', 'Diary or planner', 'paper planner'))
see('Serif typeface', ('I1', 'Font manager', 'software that handles fonts'))
see('Platform trading card', ('F3', 'Non-sports trading card', 'printed card'))
see('Cross-stitch or embroidery chart', ('C4', 'Embroidery machine', 'reads the stitch file'))
see('Audiobook file', ('I3', 'Audiobook subscription', 'rented not owned'))
see('Game item NFT', ('I2', 'Weapon skin', 'the same item held in a game account'))
see('Weapon skin', ('I2', 'Game item NFT', 'the same item as a token'))
see('Virtual land parcel', ('I2', 'Housing and décor item', 'in-game plot without a token'))
see('Digital music file', ('F1', 'Compact disc', 'physical carrier')) if False else None

# ---- layout
def sh(n, t, ax, names):
    return {'n': n, 't': t, 'ax': ax, 'k': [K[x] for x in names]} if ax else {'n': n, 't': t, 'k': [K[x] for x in names]}

L = {}
L['Fonts & typefaces'] = dict(
    t='Letter designs sold as font files under a licence and grouped by how the letters are drawn; a foundry is a brand not a kind; font-management software → I1.',
    ax='How are the letters defined: by how strokes end, by a hand or display purpose, or by a technical use?',
    s=[sh('Serif, sans & slab faces', 'Text faces told apart by how the strokes end: with serifs, without them or with heavy slabs; a face drawn like handwriting → Hand & display faces.', None,
          ['Serif typeface', 'Sans-serif typeface', 'Slab-serif typeface']),
       sh('Hand & display faces', 'Faces drawn from a hand, a brush or a poster; body-text faces → Serif, sans & slab faces.', None,
          ['Script and handwriting typeface', 'Blackletter typeface', 'Display and decorative typeface']),
       sh('Technical & other-script faces', 'Faces made for a technical or non-Latin use: code, small screens, other writing systems, symbols.',
          'kinds by technical purpose: fixed width, pixel grid, another writing system, symbols',
          ['Monospaced and coding typeface', 'Pixel and bitmap typeface', 'Non-Latin script typeface', 'Icon and symbol font'])])
L['Creative assets'] = dict(
    t='Files bought or downloaded to make other work: artwork, presets, patterns, 3D models, sounds and AI weights; the program that uses them → I1; a paper pattern or kit → C4.',
    ax='What does the file go into: a picture or layout, an editing tool, a craft, a 3D scene, a music project or an AI model?',
    s=[sh('Artwork & layouts', 'Ready-made pictures, clips and layouts used in finished work; an editing setting → Presets & motion.',
          'kinds from finished artwork to material for building to layouts to fill in',
          ['Stock photo or illustration', 'Stock video clip', 'Icon set', 'Texture and background pack', 'Design template', 'Digital planner']),
       sh('Presets & motion', 'Saved settings and animated projects loaded into an editing program: paint brushes, photo looks, colour tables, motion graphics.',
          'kinds by the program they load into: paint, photo, colour grade, video timeline',
          ['Brush pack', 'Photo preset pack', 'LUT pack', 'Motion graphics template']),
       sh('Patterns for making', 'Downloadable patterns and cut files for sewing, knitting, stitching and cutting; the paper version → C4.',
          'kinds by the craft the pattern serves: sewing, knitting, stitching, cutting',
          ['Sewing pattern', 'Knitting or crochet pattern', 'Cross-stitch or embroidery chart', 'Papercraft and cutting file']),
       sh('3D assets', 'Files for 3D scenes and 3D printing: models, surfaces and lighting; the printer itself → D1.',
          'kinds by use: scene model, printable mesh, rigged character, surface, lighting',
          ['3D model', '3D-printable model', 'Avatar model', '3D material', 'HDRI and environment map']),
       sh('Music production assets', 'Sounds, instruments and note data loaded into a music program; the program → I1.',
          'kinds by what is loaded: recorded sounds, played instruments, sample banks, patches, note data',
          ['Sample pack', 'Virtual instrument library', 'SoundFont and sample-format bank', 'Synth and effect preset pack', 'MIDI file']),
       sh('AI models', 'Downloadable weights that run on the owner\'s own machine to write, draw or speak.',
          'kinds by output: text, images, adapted weights, speech and audio',
          ['Language model weights', 'Image-generation model', 'Fine-tune or LoRA adapter', 'Speech and audio model'])])
L['Game & platform items'] = dict(
    t='Items, currency and passes held in a game or platform account and tradeable only there or on its market; a token on a blockchain → Domains & tokens; a physical collectible → E-categories.',
    ax='Which part of the game or account does the item belong to: gear, character, match flourish, loot container, profile or balance?',
    s=[sh('Weapon & gear skins', 'Finishes that change the look of a weapon, knife, glove, tool or vehicle; a worn outfit → Character cosmetics.',
          'kinds by what the skin covers: weapon, knife, glove, tool, vehicle, any surface',
          ['Weapon skin', 'Knife skin', 'Glove skin', 'Tool and glider skin', 'Vehicle skin', 'Wrap']),
       sh('Character cosmetics', 'Items that change or accompany a player\'s character: outfit, add-ons, animation, pet, mount or home.',
          'kinds by where the item sits: on the body, worn on top, in motion, beside, ridden, at home',
          ['Character outfit or skin', 'Avatar accessory', 'Emote', 'Companion or pet', 'Mount', 'Housing and décor item']),
       sh('Sprays, stickers & music kits', 'Small flourishes placed on items, walls or the match soundtrack: a sticker or charm on a weapon, a spray, a music kit.',
          None, ['In-game sticker, patch or charm', 'Spray or graffiti', 'Music kit']),
       sh('Cases, crates & keys', 'Containers that open to random items, and the keys that open them; a purchased skin → Weapon & gear skins.',
          None, ['Loot case, crate or capsule', 'Crate key']),
       sh('Platform profile & chat items', 'Collectibles and cosmetics shown on a platform profile or in chat rather than in a match.',
          'kinds by where the item shows: a collected card, a badge, a background, an avatar, chat',
          ['Platform trading card', 'Profile badge', 'Profile background', 'Avatar and frame', 'Chat emoticon', 'Chat sticker pack']),
       sh('Currency & passes', 'Spendable balances and tiered reward tracks kept in an account; a loot container → Cases, crates & keys.',
          None, ['In-game currency', 'Battle pass'])])
L['Personal media files'] = dict(
    t='Books, recordings, video and photos held as files or locker entitlements; formats are attributes; the physical carrier → F1; titles are out of scope.',
    ax='What does the owner do with the file: read it, listen to or watch it, or look at it?',
    s=[sh('E-books & documents', 'Written and printed matter held as a file: a book, a comic or a score.',
          None, ['E-book', 'Comic or manga file', 'Digital sheet music']),
       sh('Music, audio & video', 'Sound and moving pictures held as files or locker entitlements.',
          'kinds by what is heard or seen: music, a spoken book, a spoken episode, a moving picture',
          ['Digital music file', 'Audiobook file', 'Podcast episode file', 'Digital video']),
       sh('Photos & images', 'Pictures held as files: a photograph or an editable graphic.', None,
          ['Digital photo or image', 'Editable graphics file'])])
L['Domains & tokens'] = dict(
    t='Registered names and blockchain tokens that record who owns something; a game item held in an account → Game & platform items.',
    ax='Is the owned thing a readable name or a token that stands for something?',
    s=[sh('Registered names', 'Readable names registered to an owner, in the domain system or on a blockchain.', None, ['Domain name', 'Blockchain name']),
       sh('NFTs & digital collectibles', 'Tokens on a blockchain that stand for an avatar, an artwork, land, a game item or an access right.',
          'kinds by what the token stands for: an avatar, program-made art, a Bitcoin inscription, land, a game item, an access right',
          ['Profile-picture (PFP) NFT', 'Generative art NFT', 'Bitcoin Ordinal inscription', 'Virtual land parcel', 'Game item NFT', 'Ticket or membership token'])])

used = set()
for dp in d['depts']:
    dp.update({'t': L[dp['n']]['t'], 'ax': L[dp['n']]['ax']})
    dp['s'] = L[dp['n']]['s']
    for s in dp['s']:
        for k in s['k']:
            used.add(k['n'])
allk = set(K)
missing = allk - used
assert not missing, missing
d['ax'] = 'What is the file or entitlement for: setting type, making other work, dressing a game or platform account, keeping personal media, or holding a registered name or token?'
d['key'] = [
    '1. Is it a letter design used to set text? → Fonts & typefaces',
    '2. Is it a file bought to make other work (artwork, presets, patterns, 3D models, sounds, AI weights)? → Creative assets',
    '3. Is it an item, currency or pass kept in a game or platform account? → Game & platform items',
    '4. Is it a book, recording, video or photo held as a file or locker entitlement? → Personal media files',
    '5. Is it a registered name or a blockchain token? → Domains & tokens',
    '<i>Precedence: a token for a game item is a Game item NFT (step 5) while the same item inside the account is step 3; a program that uses the files → I1.</i>']

# validate see targets
for k in K.values():
    for c, n, w in k.get('see', []):
        if c == 'I2':
            assert n in K, n
        else:
            r = json.load(open(R + 'reader/%s.json' % c))
            names = {kk['n'] for dd in r['depts'] for ss in dd['s'] for kk in ss['k']}
            if n not in names:
                print('BAD SEE', c, n)
                k['see'] = [x for x in k['see'] if x[1] != n]

json.dump(d, open(R + 'work/STR_I2/I2.new.json', 'w'), ensure_ascii=False, indent=1)
os.replace(R + 'work/STR_I2/I2.new.json', R + 'out/I2.json')
json.dump({'Platform profile item': 'Platform trading card'}, open(R + 'out/I2_renames.json', 'w'), indent=1)
print('ok', len(K))
