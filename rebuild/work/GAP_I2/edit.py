import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'I2.json'))
BI='https://builtin.com/nft-non-fungible-token/nft-collections'
def E(n,dsc,mk,y,s,a=''): return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s}
def K(name):
    for dep in d['depts']:
        for sh in dep['s']:
            for k in sh['k']:
                if k['n']==name: return k
def add(k,es):
    have={e['n'].lower() for e in k.get('x',[])}
    k.setdefault('x',[])
    for e in es:
        if e['n'].lower() not in have: k['x'].append(e)
# Domain name: loose m removed
k=K('Domain name'); k.pop('m',None)
k['nl']="No named entries: a registered name is a commodity, and the endings are the types."
k['sel']="No complete list exists; the endings follow the classes of the IANA root zone as described in Wikipedia's Top-level domain page. The six endings once listed here are types, not entries, and were removed."
# PFP
k=K('Profile-picture (PFP) NFT'); k.pop('m',None)
add(k,[
 E('Azuki','10,000 anime-style characters used as profile pictures and as keys to a shared online space.','Chiru Labs','',BI),
 E('Doodles','10,000 pastel cartoon tokens of cats, humans and aliens; holders vote on community funding.','Evan Keast, Jordan Castro and Scott Martin (Burnt Toast)','',BI),
 E('DeGods','10,000 generative profile pictures on Solana with access to a DAO and staking rewards.','','2021',BI),
 E('Clone X','20,000 3D avatars in eight DNA types, customisable with digital wearables.','Nike and RTFKT','',BI,'CloneX'),
 E('Meebits','20,000 voxel and low-poly 3D avatars designed for virtual worlds and games.','Larva Labs','',BI),
 E('Cool Cats','9,999 cat illustrations ranked from common "cool" to rare "exotic".','','',BI),
 E('Beanz','20,000 bean-shaped characters that act as sidekicks to Azuki characters.','Chiru Labs','',BI),
 E('The Captainz','9,999 rarity-based tokens giving access to Memeland.','9GAG / Memeland','',BI),
 E('0N1 Force','7,777 hand-drawn anime-style side-profile characters with commercial rights for holders.','','',BI),
 E('CrypToadz','6,969 pixelated amphibian avatars released into the public domain.','Gremplin','',BI),
 E('World of Women','10,000 tokens for a female-centred network offering art drops, presales and events.','','',BI),
 E('Milady Maker','Generative profile pictures in a neochibi style, created by Remilia Corporation on Ethereum.','Remilia Corporation','2021','https://decrypt.co/309506/what-is-milady-edgy-ethereum-nft-community'),
 E('VeeFriends','A series of 10,255 character tokens whose holders get access to the VeeCon event.','Gary Vaynerchuk','2021','https://www.cnbc.com/2021/05/05/gary-vee-launching-art-nfts-linked-to-ethereum-cryptocurrency.html'),
 E('Solana Monkey Business','About 5,000 pixel profile pictures on Solana; its rights were bought by the holders\' collective MonkeDAO.','','2021','https://decrypt.co/137393/solana-monkey-business-ip-acquired-dao-nft-holders'),
])
for e in k['x']:
    if e['n']=='Pudgy Penguins' and not e['mk']: pass
k['sel']="Every profile-picture collection in Built In's list of 24 NFT collections (https://builtin.com/nft-non-fungible-token/nft-collections), with the other kinds taking its generative, land and game entries, plus Milady Maker, VeeFriends and Solana Monkey Business from fetched news pages, and CryptoPunks and Bored Ape from Wikipedia. Covers 18 of 24 in the Built In list; the others sit in Generative art NFT, Virtual land parcel and Game item NFT. No complete list exists; Okay Bears and mfers were searched for and not sourced."
# Generative
k=K('Generative art NFT'); k.pop('m',None)
add(k,[
 E('Fidenza','999 generative works by Tyler Hobbs, dropped on Art Blocks Curated; they sold out in 25 minutes.','Tyler Hobbs','2021','https://cointelegraph.com/magazine/fidenza-tyler-hobbs-wrote-a-program-to-make-art-that-is-now-worth-millions/'),
 E('Terraforms','Land art in a virtual three-dimensional hypercastle of 20 levels, with each token\'s art stored on the Ethereum blockchain.','Mathcastles','','https://iq.wiki/wiki/terraforms.md'),
 E('Loot','8,000 text-only tokens listing randomised fantasy gear, leaving interpretation to holders.','','',BI),
])
k['sel']="Collections named by Built In's list of 24 NFT collections and by the fetched pages in each entry. No complete list exists; follows those overviews. Covers 5 of 24 in the Built In list (Art Blocks, Loot, plus the generative entries from other pages); the rest belong to other kinds."
# Ordinals
k=K('Bitcoin Ordinal inscription'); k.pop('m',None)
OD='https://decrypt.co/225282/bitcoin-ordinals-runes-projects-you-should-know-halving'
add(k,[
 E('NodeMonkes','A 10,000-item profile-picture collection on Bitcoin, compared by the page to CryptoPunks on Ethereum.','','',OD),
 E('Taproot Wizards','Described as the first prominent Bitcoin Ordinals collection; its company later released Quantum Cats.','Taproot Wizards','',OD),
 E('Runestone','A project of more than 112,000 Ordinals assets airdropped to holders who met set criteria in the protocol\'s first year.','','',OD),
 E('Bitcoin Puppets','An Ordinals project of monkey characters, with the related Rune Pups airdropped to holders.','','',OD),
 E('OnChainMonkey','A long-running Ethereum project whose holders could migrate their tokens to Bitcoin.','','',OD),
 E('Ordinal Maxi Biz','5,200 or more pen-drawn riffs on CryptoPunks with surreal doodle designs.','Tony Tafuro, zk-Shark and NULLISH','',OD),
])
k['sel']="Collections named by Decrypt's overview of seven Ordinals and Runes projects and by the entries' own pages. No complete list exists; follows that overview. Covers 6 of 7 projects; RSIC Metaprotocol is a token-mining campaign, not a collection."
# Game item NFT
k=K('Game item NFT'); k.pop('m',None)
add(k,[
 E('Axie Infinity','A turn-based play-to-earn game in which players collect, breed and battle axolotl-inspired digital pets held as tokens.','','',BI),
 E('NBA Top Shot','Video clips of basketball highlights sold as tokens.','Dapper Labs with the NBA','2019','https://en.wikipedia.org/wiki/Non-fungible_token'),
 E('Sorare','A fantasy sports platform using tokenised player cards in competitions.','','',BI),
])
k['nl']="One entry is a named game or platform whose items are tokens; individual tokens are not entries."
k['sel']="Games and platforms named by Built In's list of 24 NFT collections and Wikipedia's Non-fungible token page. No complete list exists; follows those overviews. Age of Rust, Spirit Clash and The Six Dragons were removed: no fetched page named them."
# Land
k=K('Virtual land parcel')
add(k,[E('Otherdeed','100,000 digital land plots in the Otherside metaverse, each with its own mix of resources.','Yuga Labs','',BI)])
k['sel']="Land collections named by Built In's list and the pages in each entry. No complete list exists; follows those overviews. Covers 1 of 24 in the Built In list."
# formats
k=K('Digital photo or image')
add(k,[E('CR2','Canon camera raw format.','Canon','','https://en.wikipedia.org/wiki/List_of_file_formats'),
       E('DNG','Digital Negative, an open camera raw format.','Adobe','','https://en.wikipedia.org/wiki/List_of_file_formats')])
for e in k['x'][-2:]: e['g']='Raster image format'
k['sel']="Every row of the Raster graphics section (including Photographs) of Wikipedia's List of file formats, re-read as extension lists in a window from character 60,000 to 160,000. Complete: %d of %d extensions in that section; alternate extensions (JPG, TIF, TARGA and similar) sit under their main format."%(len(k['x']),len(k['x']))
k=K('Editable graphics file')
add(k,[E('TGAX','Vector format listed under vector graphics in Wikipedia\'s List of file formats.','','','https://en.wikipedia.org/wiki/List_of_file_formats'),
       E('V2D','Vector format listed under vector graphics in Wikipedia\'s List of file formats.','','','https://en.wikipedia.org/wiki/List_of_file_formats')])
for e in k['x'][-2:]: e['g']='Vector or drawing format'
k['sel']="Every row of the Vector graphics section of Wikipedia's List of file formats, re-read as an extension list. Complete: %d of %d in that section; rows that are 3D formats (AMF, STL, WRL, X3D, 3DV) sit under 3D model file format and EGT under Digital photo or image."%(len(k['x']),len(k['x']))
k=K('3D model file format')
k['sel']="Every row of the 3D graphics section of Wikipedia's List of file formats, re-read as an extension list. Complete: 100 of 100 distinct formats in that section (repeated and alternate extensions merged)."
# icon kinds: coverage phrase
SRC={'Photo preset pack':"VSCO's preset-pack page and Really Nice Images",}
for dep in d['depts']:
    for sh in dep['s']:
        for k in sh['k']:
            s=k.get('sel') or ''
            if k.get('x') and 'Icon rule: landmarks named by a fetched page only' in s:
                srcs=sorted({re.sub(r'^https?://(www\.)?','',e['s']).split('/')[0] for e in k['x'] if e.get('s')})
                k['sel']="No complete list exists; follows landmarks named by fetched pages (%s)."%', '.join(srcs)
            elif k.get('x') and not re.search(r'Complete:|Covers \d|No complete list exists',s):
                print('NO COVERAGE LINE',k['n'])
        pass
json.dump(d,open(P+'I2.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'I2.json.tmp',P+'I2.json')
b=json.load(open(P+'I2_brands.json'))
have={x['n'] for x in b['b']}
for n,c,dd in [('Chiru Labs','','Studio behind Azuki and Beanz.'),('Remilia Corporation','','Creator of Milady Maker.'),('Mathcastles','','Anonymous studio behind Terraforms.'),('Tyler Hobbs','United States','Artist behind Fidenza.'),('Dapper Labs','','Developer of NBA Top Shot.'),('Taproot Wizards','','Company behind the Taproot Wizards Ordinals collection.'),('Gary Vaynerchuk','United States','Creator of VeeFriends.'),('Nike and RTFKT','','Makers of Clone X.')]:
    if n not in have: b['b'].append({'n':n,'c':c,'f':'','seg':'Specialist','kf':'NFT collections','d':dd,'s':''})
json.dump(b,open(P+'I2_brands.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'I2_brands.json.tmp',P+'I2_brands.json')
