import json,os
def load(j): return json.load(open(f'work/I2/shelves/{j}.json'))
def save(j,d):
    p=f'work/I2/shelves/{j}.json'; t=p+'.tmp'
    json.dump(d,open(t,'w'),indent=1,ensure_ascii=False); os.replace(t,p)
def kind(d,n): return next(k for k in d['kinds'] if k['n']==n)
def addx(d,kn,x):
    k=kind(d,kn); k.setdefault('x',[])
    if not any(a['n']==x['n'] for a in k['x']): k['x'].append(x)
def A(n,d,mk,y,s,v=None,a='',dt=None):
    r={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: r["dt"]=dt
    return r
def V(n,mk,y,d): return {"n":n,"mk":mk,"y":y,"d":d}
def addb(d,b):
    if not any(x['n']==b['n'] for x in d['brands']): d['brands'].append(b)
def note(d,t): d['notes']=d['notes']+' | Deepening pass: '+t

# 02_00
d=load('02_00')
SD='https://steamdb.com/it/skins/cs2/m4a4/m4a4-howl'
addx(d,'Weapon skin',A('M4A4 | Howl','Contraband-grade M4A4 skin, the top rarity tier, no longer obtainable from cases; float 0.00-0.40 so only Factory New to Well-Worn exist.','Valve','',SD,dt='wear 0.00-0.40 · Factory New to Well-Worn · StatTrak'))
addx(d,'Weapon skin',A('AWP | Asiimov','Covert AWP skin from the Phoenix Collection, designed by Coridium and released with the Operation Phoenix Weapon Case on 20 February 2014.','Valve','2014','https://csgoskins.gg/items/awp-asiimov',[V('StatTrak Asiimov','Valve','2014','StatTrak variant'),V('Souvenir Asiimov','Valve','2014','Souvenir variant')],dt='wear 0.18-1.00 · Field-Tested to Battle-Scarred'))
addx(d,'Weapon skin',A('Elderflame','Valorant dragon-themed weapon collection released 10 July 2020, sold as a 9,900 VP bundle with fire, scale and smoke effects and special animations.','Riot Games','2020','https://www.gameinformer.com/2020/07/08/elite-dragon-weapons-come-to-valorant-this-week'))
addx(d,'Weapon skin',A('Oni','Valorant samurai-demon collection; the 2.0 line began with Episode 6 Act 2 on 7 March, about 7,100 VP, with Vandal, Bulldog, Ares, Frenzy and a katana.','Riot Games','','https://www.ggrecon.com/guides/valorant-oni-skinline-new-skins/',[V('Oni 2.0','Riot Games','2023','Vandal, Bulldog, Ares, Frenzy and Onimaru Kunitsuna katana; variants Gold/Black, Pink/Mint, Blue/White')]))
addx(d,'Weapon skin',A('Glitchpop','Valorant cyberpunk collection that went on sale with Act II in August 2020: Frenzy, Judge, Bulldog, Odin and a knife.','Riot Games','2020','https://upcomer.com/riot-reveals-glitchpop-skin-line-in-valorant'))
addx(d,'Weapon skin',A('Kuronami','Valorant collection released 9 January 2024 with Patch 8.0 for 9,500 VP: Sheriff, Spectre, Vandal, Marshal and the Kuronami no Yaiba melee.','Riot Games','2024','https://thespike.gg/valorant/skins/valorant-kuronami-bundle',dt='variants purple · white · black'))
addx(d,'Vehicle skin',A('Dominus','Rocket League car body released 13 August 2015 in the Supersonic Fury DLC Pack, later free to all players; its hitbox is used by other cars.','Psyonix','2015','https://rocketleague.fandom.com/wiki/Dominus',[V('Supersonic Fury DLC Pack','Psyonix','2015','Original paid source'),V('Painted Dominus','Psyonix','','Import and Exotic rarities')],dt='painted variants · Import · Exotic'))
note(d,'added archetypes M4A4 Howl, AWP Asiimov, Valorant Elderflame, Oni, Glitchpop, Kuronami, and Rocket League Dominus (Vehicle skin) from fetched pages; no models trimmed. Valorant pages came from news sites (gameinformer, ggrecon, upcomer, thespike) since fandom pages were blocked. Oni details are for the 2.0 line only; Howl page gives no collection or year.')
save('02_00',d)

# 02_01
d=load('02_01')
addx(d,'Character outfit or skin',A('Renegade Raider','Chapter 1 Fortnite outfit long regarded as one of the rarest skins; reskinned later as Renegade Runner.','Epic Games','','https://esports.gg/news/fortnite/renegade-runner-who-is-the-infamous-fortnite-skin',[V('Renegade Runner','Epic Games','','Robotic-themed variation of the original')]))
T='https://techguided.com/top-10-rarest-mounts-in-wow/'
for n,dd in [("Ashes of Al'ar","Rare phoenix mount dropped by Kael'thas Sunstrider in The Eye (Burning Crusade), listed at about 1.7% drop rate."),
 ("Thundering Cobalt Cloud Serpent","Mists of Pandaria rare drop from Nalak the Storm Lord on the Isle of Thunder, estimated 0.02% drop rate."),
 ("Solar Spirehawk","Draenor rare drop from Rukhmar in the Spires of Arak, about 0.2% drop rate."),
 ("Prestigious Midnight Courser","Legion PvP mount earned by reaching Honor level 250 (originally Prestige level 25).")]:
    addx(d,'Mount',A(n,dd,'Blizzard Entertainment','',T))
note(d,'added Renegade Raider (esports.gg page, year not stated) and four World of Warcraft rare mounts from the techguided list. Drop rates are snapshots. Black Knight, Skull Trooper, League skin lines and Roblox Dominus still unsourced.')
save('02_01',d)

# 01_00
d=load('01_00')
P='https://www.vsco.co/features/photo-filters/preset-packs'
addx(d,'Photo preset pack',A('VSCO Film','Film-emulation preset packs for Adobe Lightroom recreating Kodak, Fuji, Agfa and Ilford stocks, with (-), (+) and (++) strengths; also built natively for Capture One.','VSCO','',P,[V('Film 01','VSCO','',''),V('Film 02','VSCO','',''),V('Film 05','VSCO','',''),V('Film 07','VSCO','',''),V('VSCO Film for Capture One','VSCO','','Styles and camera profiles for Capture One')],dt='film stock · strength (-, +, ++) · host app'))
addx(d,'Photo preset pack',A('RNI All Films','Presets and profiles for Lightroom and Photoshop ACR, plus Capture One styles, built from real film emulsions.','RNI','','https://reallyniceimages.com',[V('RNI All Films 4','RNI','',''),V('RNI All Films 5','RNI','','')]))
addb(d,{"n":"VSCO","c":"","f":"","seg":"Specialist","kf":"film presets","d":"Maker of film-emulation preset packs for Lightroom and Capture One.","s":P})
addb(d,{"n":"RNI","c":"","f":"","seg":"Specialist","kf":"film presets","d":"Really Nice Images, maker of film-emulsion presets, profiles and iOS apps.","s":"https://reallyniceimages.com"})
note(d,'added VSCO Film and RNI All Films archetypes plus brand entries from the vendor pages.')
save('01_00',d)

# 01_01
d=load('01_01')
addx(d,'Sewing pattern',A('Burda Style','German pattern brand grown out of the Burda magazine, sold as multi-size paper envelopes and printable PDFs.','Burda','','https://www.sewdirect.com/product/burda-6305/'))
addb(d,{"n":"Burda","c":"Germany","f":"","seg":"Mainstream","kf":"sewing patterns","d":"German pattern brand that grew out of the Burda magazine.","s":"https://www.sewdirect.com/product/burda-6305/"})
note(d,'added Burda Style archetype and brand from a retailer page (Sewdirect); founding year not stated.')
save('01_01',d)

# 01_02
d=load('01_02')
PH='https://polyhaven.com/about-contact'; QX='https://www.fab.com/sellers/Quixel%20Megascans/about'
pd="Free public library of HDRIs, textures and 3D models released under CC0, funded mainly by Patreon donors and sponsors."
qd="Photogrammetry asset library; Quixel is part of Epic and Megascans is now sold exclusively on Fab."
for kn in ['3D material','HDRI and environment map','3D model']:
    addx(d,kn,A('Poly Haven',pd,'Poly Haven','',PH))
for kn in ['3D material','3D model']:
    addx(d,kn,A('Quixel Megascans',qd,'Quixel','',QX))
addb(d,{"n":"Poly Haven","c":"","f":"","seg":"Specialist","kf":"free CC0 assets","d":"Free library of HDRIs, textures and models under CC0.","s":PH})
addb(d,{"n":"Quixel","c":"","f":"","seg":"Specialist","kf":"Megascans","d":"Part of Epic; maker of the Megascans photogrammetry library.","s":QX})
note(d,'added Poly Haven and Quixel Megascans archetypes (and brands) from their own pages; VRChat base bodies still unsourced.')
save('01_02',d)

# 01_04
d=load('01_04')
sd=next(x for x in kind(d,'Image-generation model')['x'] if x['n']=='Stable Diffusion')
if not sd['v']: sd['v'].append(V('SDXL 1.0','Stability AI','2023','28 Jul 2023 (cgpress), text-to-image with a fine-tuning option; April 2023 beta before it'))
note(d,'added SDXL 1.0 as a version of Stable Diffusion from the cgpress release article.')
save('01_04',d)

# 04_01
d=load('04_01')
addx(d,'Generative art NFT',A('Autoglyphs','512 generative artworks by Larva Labs, launched 2019, the first art project both generated and stored entirely on-chain.','Larva Labs','2019','https://www.larvalabs.com/autoglyphs'))
note(d,'added Autoglyphs as archetype from the Larva Labs page (kept in m too).')
save('04_01',d)
