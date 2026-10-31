import json,os
W='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(W+'out/I2.json')); B=json.load(open(W+'out/I2_brands.json'))
K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
wp=lambda t:'https://en.wikipedia.org/wiki/'+t
def A(n,mk,y,s,d_,v=None,dt=None,a=''):
    x={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s,'v':[{'n':i[0],'mk':i[1] if len(i)>1 else mk,'y':i[2] if len(i)>2 else '','d':''} for i in (v or [])]}
    if dt: x['dt']=dt
    return x
def add(kind,items):
    ex={x['n'] for x in K[kind].get('x',[])}
    K[kind].setdefault('x',[]).extend(i for i in items if i['n'] not in ex)
# I2-7 removals
for kn in ('3D model','3D material','HDRI and environment map'):
    K[kn]['x']=[x for x in K[kn]['x'] if x['n'] not in('Poly Haven','Quixel Megascans')]
K['Virtual instrument library']['x']=[x for x in K['Virtual instrument library']['x'] if x['n']!='Kontakt']
# I2-6 mk fixes
for k in K.values():
    for x in k.get('x',[]):
        if x.get('mk')=='Google': x['mk']='Google Fonts'
# I2-1 typefaces
add('Sans-serif typeface',[
 A('DIN 1451','Deutsches Institut für Normung','1931',wp('DIN_1451'),'German standards-body lettering for signs and technical drawing, later widely digitised.',[('FF DIN',''),('Bahnschrift','Microsoft'),('Neue DIN','')],'Vox-ATypI: grotesque sans-serif · official standard 1936'),
 A('Johnston','Edward Johnston','1916',wp('Johnston_(typeface)'),'Humanist sans commissioned by Frank Pick for the London Underground.',[('New Johnston',''),('Johnston 100',''),('P22 Underground','')],'Vox-ATypI: humanist sans-serif · commissioned 1913'),
 A('Franklin Gothic','Morris Fuller Benton','1902',wp('Franklin_Gothic'),'American grotesque from ATF with a family of related Gothics.',[('Alternate Gothic','American Type Founders','1903'),('News Gothic','American Type Founders','1908'),('ITC Franklin Gothic','International Typeface Corporation','1980'),('Libre Franklin','Impallari Type')],'Vox-ATypI: grotesque'),
 A('Optima','Hermann Zapf','1958',wp('Optima'),'Flared humanist sans without true serifs, released by Stempel.',[('Optima nova','','2002'),('Zapf Humanist 601','Bitstream')],'Vox-ATypI: humanist sans-serif'),
 A('Arial','Monotype','1982',wp('Arial'),'Neo-grotesque designed by Robin Nicholas and Patricia Saunders as a metric-compatible alternative to Helvetica.',[('Arial Black',''),('Arial Narrow',''),('Arial Rounded MT Bold',''),('Arial Nova','')],'Vox-ATypI: neo-grotesque'),
 A('Avenir','Adrian Frutiger','1988',wp('Avenir_(typeface)'),'Geometric sans by Adrian Frutiger for Linotype, designed 1987.',[('Avenir Next',''),('Avenir Next Rounded','','2012')],'Vox-ATypI: geometric sans-serif'),
 A('Myriad','Adobe','1992',wp('Myriad_(typeface)'),'Humanist sans by Robert Slimbach and Carol Twombly for Adobe.',[('Myriad Pro',''),('Myriad Web',''),('Myriad Set Pro','')],'Vox-ATypI: humanist sans-serif'),
 A('Verdana','Microsoft','1996',wp('Verdana'),'Wide humanist screen face by Matthew Carter, hinted for small pixel sizes.',[('Verdana Pro',''),('Verdana Ref','')],'Vox-ATypI: humanist sans-serif'),
 A('San Francisco','Apple','',wp('San_Francisco_(typeface)'),'Apple\'s sans-serif system face for its devices.',None,'Apple corporate typeface'),
 A('Template Gothic','Barry Deck','1991',wp('Template_Gothic'),'Experimental sans from Emigre, designed 1989 by Barry Deck.',None,'released 1991'),
 A('Graphik','Commercial Type','',wp('Canela_(typeface)'),'Sans-serif family from Commercial Type, listed on its foundry page.',None,None),
])
add('Serif typeface',[
 A('Centaur','Bruce Rogers','1929',wp('Centaur_(typeface)'),'Venetian old-style serif drawn by Bruce Rogers in 1914; italic by Frederic Warde.',[('Centaur (Monotype)','Monotype'),('Metropolitan',''),('Museum',''),('Coelacanth','')],'Vox-ATypI: Venetian old-style · created 1914'),
 A('Bembo','Monotype','1929',wp('Bembo'),'Monotype revival of a roman cut c. 1495 by Francesco Griffo for Aldus Manutius.',[('Bembo Book',''),('Bembo Titling','')],'Vox-ATypI: Garalde old-style · Monotype series 270'),
 A('Plantin','Monotype','1913',wp('Plantin_(typeface)'),'Old-style serif loosely following 16th-century Robert Granjon types.',[('Plantin Infant',''),('News Plantin',''),('Nonesuch Plantin','')],None),
 A('Didot','Firmin Didot','',wp('Didot_(typeface)'),'High-contrast modern serif from Firmin Didot, with many digital revivals.',[('Linotype Didot','Linotype'),('HFJ Didot','Hoefler & Co.'),('Ambroise','')],'Vox-ATypI: Didone · letters developed 1784–1811'),
 A('Palatino','Hermann Zapf','1949',wp('Palatino'),'Old-style serif by Hermann Zapf for Stempel, some sources give 1950.',[('Palatino Linotype','Linotype'),('Palatino Nova','Linotype'),('Aldus','')],'Vox-ATypI: old-style'),
 A('Georgia','Matthew Carter','1996',wp('Georgia_(typeface)'),'Screen serif by Matthew Carter for Microsoft, designed 1993.',[('Georgia Pro','Font Bureau'),('Georgia Ref','')],'transitional'),
 A('Minion','Robert Slimbach','1990',wp('Minion_(typeface)'),'Garalde text serif by Robert Slimbach for Adobe.',[('Minion Pro',''),('Minion 3','Adobe','2018')],'Vox-ATypI: Garalde old-style'),
 A('Trajan','Carol Twombly','1989',wp('Trajan_(typeface)'),'Capitals-only incised serif for Adobe, with Trajan Sans as a companion.',[('Trajan Pro',''),('Trajan Pro 3',''),('Trajan Sans','')],'Vox-ATypI: incised'),
 A('Mrs Eaves','Zuzana Licko','1996',wp('Mrs_Eaves'),'Transitional serif by Zuzana Licko for Emigre, based on Baskerville.',[('Mrs Eaves XL',''),('Mr Eaves','')],None),
])
add('Slab-serif typeface',[
 A('Memphis','Stempel','1929',wp('Memphis_(typeface)'),'Geometric slab serif by Rudolf Wolf for Stempel.',[('Geometric Slabserif 703','Bitstream')],None),
 A('Archer','Hoefler & Co.','2001',wp('Archer_(typeface)'),'Slab serif by Tobias Frere-Jones and Jonathan Hoefler.',None,None)])
add('Script and handwriting typeface',[
 A('Brush Script','American Type Founders','1942',wp('Brush_Script'),'Casual connecting script by Robert E. Smith for ATF.',None,None),
 A('Mistral','Roger Excoffon','1953',wp('Mistral_(typeface)'),'Casual script by Roger Excoffon for Fonderie Olive.',[('Staccato 222','')],None)])
add('Display and decorative typeface',[
 A('Cooper Black','Oswald Bruce Cooper','1922',wp('Cooper_Black'),'Ultra-bold rounded serif by Oswald Bruce Cooper for Barnhart Brothers & Spindler.',[('Cooper Hilite',''),('Ludlow Black','')],None),
 A('Broadway','American Type Founders','1928',wp('Broadway_(typeface)'),'Art Deco display face by Morris Fuller Benton for ATF.',[('Broadway Engraved','')],'Vox-ATypI: display'),
 A('Copperplate Gothic','American Type Founders','1901',wp('Copperplate_Gothic'),'Small-serif capitals face by Frederic W. Goudy for ATF.',None,None)])
add('Monospaced and coding typeface',[
 A('OCR-A','American Type Founders','1968',wp('OCR-A'),'Machine-readable face commissioned by ANSI, issued 1966.',[('OCR-A Extended','')],None),
 A('Monaco','Apple','1984',wp('Monaco_(typeface)'),'Apple monospace face by Susan Kare, Kris Holmes and Charles Bigelow.',None,'created 1983'),
 A('Consolas','Microsoft','2006',wp('Consolas'),'Coding monospace by Lucas de Groot for Microsoft.',None,None),
 A('Fira','bBox Type','2013',wp('Fira_(typeface)'),'Open-licence family by Erik Spiekermann and others, including Fira Mono and Fira Code.',[('Fira Sans',''),('Fira Mono',''),('Fira Code','')],'SIL Open Font License'),
 A('JetBrains Mono','JetBrains','2020',wp('JetBrains_Mono'),'Coding typeface released by JetBrains under Apache 2.0.',None,None)])
K['Monospaced and coding typeface']['m']=[m for m in K['Monospaced and coding typeface']['m'] if m[0] not in('Consolas','Fira Code')]
add('Blackletter typeface',[
 A('Schwabacher','','15th century',wp('Schwabacher'),'Blackletter from Gothic Textualis; oldest known use 1472, Augsburg.',None,'dominant in Germany c. 1480–1530'),
 A('Textura','','15th century',wp('Blackletter'),'Dense blackletter form of Gutenberg\'s 42-line Bible.',None,'grades prescissa, quadrata, semi-quadrata')])
K['Serif typeface']['t']=['Venetian','Garalde','Transitional','Didone','Incised']
# I2-2 game items
add('Avatar accessory',[
 A('Partyhat (RuneScape)','Jagex','2001','https://runescape.wiki/w/Party_hat','Discontinued Christmas-cracker hats, a trading status symbol.',[('Golden partyhat','Jagex','2021'),('Black partyhat','Jagex','2023')],'original six: blue, green, purple, red, yellow, white'),
 A('Unusual (Team Fortress 2)','Valve','','https://wiki.teamfortress.com/wiki/Unusual','Rarest cosmetic quality, carrying particle effects; opened from crates.',None,'effect classes: Standard, Summer, Scream Fortress, Smissmas'),
 A('Roblox Limited','Roblox','','https://en.wikipedia.org/wiki/Roblox','Limited-supply avatar items resold at market-set prices.',None,'tradeable official items only')])
add('Companion or pet',[A('Dota 2 courier','Valve','','https://en.wikipedia.org/wiki/Dota_2','Cosmetic couriers, including promotional tie-ins.',[('Chocobo courier','Square Enix','2015'),('Amaterasu','Capcom','2017')],None)])
add('Housing and décor item',[A('Habbo rare furni','Sulake','',wp('Habbo'),'Rare furniture bought with diamonds and traded among users.',None,None)])
# I2-3 merge platform profile kinds
names=['Platform trading card','Badge or pin','Profile background','Profile avatar or frame','Loading screen','Chat emoticon','Messaging sticker pack']
shelf=[s for dp in d['depts'] for s in dp['s'] if s['n']=='Platform profile & chat items'][0]
xs=[x for n in names for x in K[n].get('x',[])]
new={'n':'Platform profile item','a':'Steam trading card · badge · profile background · avatar frame · emoticon · sticker pack','d':'A cosmetic or collectible item kept on a game or messaging platform account and shown on a profile or in chat.','t':['Trading card','Badge or pin','Profile background','Avatar or frame','Loading screen','Chat emoticon','Sticker pack'],'s':'https://steamcommunity.com/tradingcards/faq','x':xs}
shelf['k']=[new]
# I2-4
K['Digital photo or image']['t']=['camera raw (DNG and maker formats)','lossy (JPEG, HEIC, WebP, AVIF)','lossless (PNG, TIFF, GIF, BMP)']
dn=K['Domain name']; dn['m']=[m for m in dn['m'] if m[0] in('.com','.net','.org','.io','.ai','.co.uk')]
# brands
have={b['n'].lower() for b in B['b']}
def br(n,seg,kf,c='',f='',s='',d_=''):
    if n.lower() in have: return
    have.add(n.lower()); B['b'].append({'n':n,'c':c,'f':f,'seg':seg,'d':d_ or kf,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':kf})
D='Artisan & independent'; H='Heritage manufactory'; P='Professional & flagship'
for n,k in [('Hermann Zapf','Palatino, Optima'),('Claude Garamond','Garamond'),('William Caslon I','Caslon'),('John Baskerville','Baskerville'),('Giambattista Bodoni','Bodoni'),('Adrian Frutiger','Univers, Frutiger'),('Rasmus Andersson','Inter'),('Firmin Didot','Didot'),('Bruce Rogers','Centaur'),('Edward Johnston','Johnston'),('Morris Fuller Benton','Franklin Gothic'),('Oswald Bruce Cooper','Cooper Black'),('Carol Twombly','Trajan'),('Matthew Carter','Georgia, Verdana'),('Robert Slimbach','Minion'),('Roger Excoffon','Mistral'),('Barry Deck','Template Gothic'),('Zuzana Licko','Mrs Eaves')]: br(n,D,'type designer: '+k)
for n,k in [('Haas Type Foundry','Helvetica'),('Bauersche Gießerei','Futura'),('Berthold','Akzidenz-Grotesk'),('Deberny & Peignot','Univers'),('Thorowgood & Co.','Clarendon'),('Stempel','Memphis, Palatino'),('American Type Founders','Franklin Gothic, Broadway'),('Barnhart Brothers & Spindler','Cooper Black')]: br(n,H,'historic type foundry: '+k)
br('Commercial Type',P,'editorial type','United States','2007',wp('Canela_(typeface)'))
for n,k in [('Google Fonts','open fonts'),('IBM','Courier'),('Apple','San Francisco, Monaco'),('bBox Type','Fira'),('JetBrains','JetBrains Mono'),('Jagex','RuneScape'),('Sulake','Habbo')]: br(n,P,k)
for n,k in [('Casey Rodarmor','Ordinals'),('Creative Tools','Bohlen-Pierce MIDI'),('E-mu Systems and Creative Labs','SoundFont'),('Ethereum Name Service','.eth names'),('Greg Turk and Marc Levoy','Stanford bunny'),('Live2D Ltd.','Live2D'),('MIDI Manufacturers Association','MIDI'),('Martin Newell','Utah teapot'),('Paul Debevec','HDR light probes'),('Proof Collective','Moonbirds')]: br(n,D,k)
for p,o in ((W+'out/I2.json',d),(W+'out/I2_brands.json',B)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
