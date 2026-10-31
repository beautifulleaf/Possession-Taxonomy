import json,sys,copy
P='out/A1.json'; a=json.load(open(P))
json.dump(a,open('work/SCENES/A1.before_regroup.json','w'),ensure_ascii=False)
S={}; orig={}
for g in a['scenes']:
    for s in g['s']:
        S[s['n'].split(' [')[0]]=s; orig[s['n'].split(' [')[0]]=g['n']
def k(n):
    m=[x for x in S if x==n] or [x for x in S if x.startswith(n)]
    assert len(m)==1,(n,m); return m[0]
# (group, [ (scene, [children]) ])
NEW=[
("Mod, skinhead & ska",[("Mod",[]),("Swinging London boutique fashion",["Peacock Revolution"]),("Skinhead",["Suedehead"]),("Rude boy",[])]),
("Football terraces",[("Casuals (football casual)",[]),("Ultras (football)",[])]),
("Rock'n'roll & rockabilly",[("Teddy Boy",[]),("Greaser",[]),("Rockers (ton-up",[]),("Rockabilly",["Pin-up rockabilly","Psychobilly","Gothabilly"])]),
("Bikers",[("Biker",["Sartorial motorcycling"])]),
("Chicano lineage",[("Zoot suit and pachuco",[]),("Cholo (Chicano)",["Cholombiano"])]),
("Punk",[("Punk",["Crust punk"])]),
("Goth & industrial",[("Goth",["Romantic goth","Nu-goth","Mall goth"]),("Cybergoth",[]),("Rivethead",[])]),
("Metal",[("Heavy metal",[])]),
("Alternative, emo & grunge",[("Emo",["Scene (scene kids)"]),("Grunge",["Kinderwhore"])]),
("Glam & New Romantic",[("Glam rock",[]),("New Romantic",[])]),
("British indie",[("Britpop",[]),("Madchester (baggy)",[]),("Indie sleaze",[])]),
("Bohemian & counterculture",[("Beatnik",[]),("Hippie",[]),("Hipster",[]),("Rastafari style",[])]),
("Regional youth tribes",[("Chav",[]),("UK roadman and grime dress",[]),("Eshay",[]),("Gopnik",[]),("Flaite",[]),("Flogger",[]),("Ah Beng and Ah Lian",[]),("Paninaro",[])]),
("African dandy & township styles",[("La Sape",[]),("Izikhothane",[]),("Pantsula style",[])]),
("Leather & fetish",[("Leather subculture",["Latex and fetish fashion"])]),
("Retro-futurist",[("Steampunk",[])]),
("Hip-hop, street, skate & surf",[("Hip-hop fashion",["B-boy and breaking dress"]),("Streetwear",[]),("Post-Soviet streetwear",[]),("Skate (skater)",[]),("Surf (surfer)",[]),("Reggaetonero",[])]),
("Festival & club",[("Rave",["Gabber","New rave","Tecktonik"]),("Burner and festival fashion",[]),("Berlin techno fashion",[]),("Club kids",[])]),
("Japanese street fashion",[("Harajuku fashion",["Decora","Fairy kei"]),("Lolita",["Classic Lolita","Gothic Lolita","Sweet Lolita","Punk Lolita","Ouji (boy style Lolita)"]),("Gyaru",["Kogal","Ganguro","Hime gyaru","Gyaruo (gal-o)"]),("Red letter fashion (Aka-moji kei)",["Onee-kei (onee gal)","Kireime kei"]),("Visual kei",[]),("Ura-Harajuku (Ura-Hara)",[]),("Street-kei (Japanese street casual)",[]),("Amekaji (American casual, Japan)",["Shibu-kaji (Shibuya casual)","Kire-kaji"]),("Subcul (sabukaru)",[]),("Mori kei (mori girl)",["Dolly kei","Cult Party kei"]),("Girly kei (Larme kei)",[]),("Jirai kei",[]),("Oshare kei",[]),("Bodikon (bodycon)",[]),("Goth punk (Japan)",[]),("Genderless kei",[]),("Takenoko-zoku",[]),("Bosozoku",[]),("Sukeban",[]),("JK uniform fashion",[]),("PEEPS",[])]),
("Heritage, workwear & military",[("Workwear and heritage",["Americana","Western workwear"]),("Japanese denim",[]),("Military surplus and field-jacket wear",[]),("Nautical and marinière style",[]),("Folk and heritage knitwear",[])]),
("Outdoor, technical & sport",[("Athleisure and sportswear",[]),("Gorpcore (outdoor)",[]),("Techwear",[]),("Road cycling culture",[]),("Apres-ski style",[])]),
("Avant-garde & archive",[("Avant-garde fashion",["Belgian and Antwerp avant-garde","Dark artisanal avant-garde"]),("Japanese avant-garde (Paris 1981 designers)",["Karasu-zoku"]),("Archive fashion",["Japanese archive fashion"])]),
("Tailoring & classic",[("Classic tailoring (sartorial)",["Savile Row tailoring","Neapolitan tailoring"]),("Ivy style (Ivy League look)",["Trad (traditional) style","Japanese Ivy (Ametora)","Black Ivy"]),("Preppy",[]),("Old money (quiet luxury)",[]),("British countryside style",[]),("Business casual",[]),("Modern dandy (dandyism)",[])]),
]
used=set()
def mk(name,kids):
    s=S[k(name)]; used.add(k(name)); s=copy.deepcopy(s)
    if kids:
        s['c']=s.get('c',[])+[mk(c,[]) for c in kids]
    return s
out=[{"n":g,"s":[mk(n,c) for n,c in L]} for g,L in NEW]
# remaining groups keep order, minus used scenes; apply in-group nests
NEST={"South Asian ethnic wear":["Sari","Salwar kameez","Lehenga","Kurta and kurti","Pakistani lawn and pret"],"Modest fashion":["Abaya"],"Batik fashion":["Sri Lankan batik and handloom fashion"]}
for p,kids in NEST.items(): used.update(k(c) for c in kids)
for g in a['scenes']:
    rest=[]
    for s in g['s']:
        key=s['n'].split(' [')[0]
        if key in used: continue
        for p,kids in NEST.items():
            if key.startswith(p): s=copy.deepcopy(s); s['c']=s.get('c',[])+[copy.deepcopy(S[k(c)]) for c in kids]
        rest.append(s)
    if rest: out.append({**{x:y for x,y in g.items() if x!='s'},"s":rest})
n=lambda L: sum(1+len(s.get('c',[])) for g in L for s in g['s'])
print('before',n(a['scenes']),'after',n(out))
assert n(a['scenes'])==n(out)
a['scenes']=out
json.dump(a,open(P,'w'),ensure_ascii=False,indent=1)
for g in out: print(g['n'],len(g['s']))
