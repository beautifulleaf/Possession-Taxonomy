import json,os,sys,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_J2/bak/J2.json'))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(K),
  arch=sum(len(k.get('x',[])) for k in K.values()))
# tt
TT={}
for line in open(R+'work/STR_J2/tt.txt'):
    line=line.strip()
    if not line: continue
    n,rest=line.split(' :: ')
    TT[n]=[[g.split(': ')[0],[x.strip() for x in g.split(': ',1)[1].split(';')]] for g in rest.split(' || ')]
# renames
K['Flatfish & skate']['n']='Flatfish'; K['Flatfish']=K.pop('Flatfish & skate')
K['Flatfish']['a']='Heilbutt · Scholle · plaice · sole'
K['Flatfish']['d']='Raw flatfish such as sole, turbot, plaice and halibut, sold whole or as fillets.'
S='https://en.wikipedia.org/wiki/List_of_types_of_seafood'
def new(n,a,dd,s,**kw):
    k=dict(n=n,a=a,d=dd,s=s); k.update(kw); K[n]=k
new('Skate & ray','skate wings · ray wings · Rochen','Raw skate or ray wings, sold whole or skinned.',S)
new('Shad','Alosa · ilish · allis shad','Raw shad, an oily herring-family fish that runs from sea into rivers, sold whole or as fillets.',S)
new('Pacific saury','sanma · Cololabis saira · mackerel pike','Raw Pacific saury, a slim oily fish sold whole, fresh or frozen.',S)
new('Lamprey','lamproie · lampreia','Raw lamprey, an eel-like jawless fish, sold fresh or frozen, whole or in pieces.',S)
new('Olympia oyster','Ostrea lurida · Olympia','Petite, round-shelled native oyster of the US West Coast, farmed in Washington and sold live.','https://discoverwcseafood.msi.ucsb.edu/species/olympia-oysters')
new('Barnacle','percebes · goose barnacle','Barnacles eaten as seafood, sold live or cooked.',S)
new('Jellyfish','','Jellyfish eaten as seafood, usually sold salted or shredded.',S)
new('Sea squirt','tunicate · sea pineapple · piure','Sea squirts eaten as seafood, such as sea pineapple, piure and sea fig.',S)
SF='https://en.wikipedia.org/wiki/Smoked_fish'
new('Smoked halibut','','Halibut cold-smoked and sliced in delicatessens, or hot-smoked as pieces.',SF)
new('Smoked sable','sable · smoked black cod · sablefish','Sablefish hot-smoked, a delicatessen fish often eaten with bagels.','https://en.wikipedia.org/wiki/Smoked_sable')
new('Smoked whitefish','','Whitefish smoked, usually hot, sold whole or in fillets, a common US delicatessen fish.',SF)
new('Smoked sturgeon','','Sturgeon cold-smoked and sliced in delicatessens, or hot-smoked as pieces.',SF)
new('Whitefish roe','golden whitefish caviar','Small golden eggs of whitefish, cured and sold as a caviar substitute.','https://marxfood.com/?p=8922')
new('Himono','dried fish · Japanese dried fish','Japanese fish salted, soaked in brine and dried, usually overnight, then grilled.','https://en.wikipedia.org/wiki/Himono')
new('Bombay duck','bummalo · bombil · Harpadon nehereus','Lizardfish of Indo-Pacific waters, usually sold dried, though fresh fish also appear in markets.','https://en.wikipedia.org/wiki/Bombay_duck')
new('Hanpen','','Pale, mild Japanese fish-paste cake in squares, triangles or circles, simmered in oden.','https://en.wikipedia.org/wiki/Hanpen')
new('Otak-otak','otah','South-east Asian ground fish mixed with spices, wrapped in leaves and steamed or grilled.','https://en.wikipedia.org/wiki/Otah')
K['Satsuma-age']['a']=K['Satsuma-age']['a']+' · eomuk · odeng'
# demotions
DEMOTE={
'Kumamoto oyster':['West Coast Kumamoto'],'Sydney rock oyster':['New South Wales estuary rock oyster'],
'Langoustine':['Creel-caught langoustine'],'Brown crab':['British Isles brown crab'],'Dungeness crab':['Pacific coast Dungeness crab'],
'Stone crab':['Florida stone crab claws'],
'Smoked salmon':['Petrossian smoked salmon','Burren Smokehouse smoked organic salmon','Ummera smoked organic salmon','Belvelly hung-smoked salmon','Severn & Wye smoked salmon'],
'Gravlax':['Scandinavian gravad lax'],
'Tinned tuna':['Rio Mare','John West tuna','StarKist tuna','Herpac bluefin tuna'],
'Bonito del Norte':['Ortiz Bonito del Norte','Conservas Albo bonito','Olasagasti white tuna','Carmelo tuna fillets','Angelachu bonito del norte'],
'Tinned sardines':['Connétable sardines','Ramón Peña sardinillas','Pinhais sardines'],
'Tinned mackerel':['Takagi Shoten saba'],'Tinned sprats & brisling':['King Oscar brisling'],
'Tinned anchovies':['Ortiz anchovies','Don Bocarte anchovy fillets','Nardín beech-smoked anchovies'],
'Tinned mussels':['Galician mussels in escabeche'],'Tinned cockles':['Espinaler berberechos'],'Tinned scallops':['Zamburiñas in salsa'],
'Tinned oysters':['Bevans canned oysters','Chicken of the Sea oysters'],'Tinned eel':['Comur eel in pickled sauce'],
'Sturgeon caviar':['Hybrid sturgeon'],'Fish cake':['British potato fishcake']}
# dropped because alias or tt already carries the name
DROP={'Red king crab':'King crab','Ventresca':'Tinned tuna','Golbaengi':'Tinned whelk or conch','Räucheraal':'Smoked eel','Schillerlocke':'Smoked dogfish belly','Tinapang bangus':'Smoked milkfish','Kanikama':'Crab stick','Boquerones en vinagre':'Marinated anchovies','Jarred gefilte fish':'Gefilte fish','Sweet and peppery styles':'Gefilte fish','Honkarebushi':'Katsuobushi','Arabushi':'Katsuobushi','Karebushi':'Katsuobushi','Hwangtae':'Dried pollock','Bugeo':'Dried pollock'}
demoted=[];dropped=[]
for kn,names in DEMOTE.items():
    k=K[kn]
    for nm in names:
        a=[x for x in k['x'] if x['n']==nm]; assert a,(kn,nm)
        k['x']=[x for x in k['x'] if x['n']!=nm]
        k.setdefault('m',[]).append([nm,a[0].get('mk','')]); demoted.append((kn,nm))
for nm,kn in DROP.items():
    k=K[kn] if kn in K else None
    if kn=='King crab': k=K['King crab']
    a=[x for x in k.get('x',[]) if x['n']==nm]; assert a,(kn,nm)
    k['x']=[x for x in k['x'] if x['n']!=nm]; dropped.append((kn,nm))
# alias carries
def addalias(kn,al):
    k=K[kn]; 
    if al.lower() not in k.get('a','').lower(): k['a']=(k.get('a','')+' · '+al).strip(' ·')
addalias('King crab','red king crab'); addalias('Tinned whelk or conch','golbaengi'); addalias('Smoked eel','Räucheraal')
addalias('Crab stick','kanikama')
# structure
def sh(n,t,ax,names): return dict(n=n,t=t,ax=ax,k=names)
D=[]
D.append(dict(n='Fresh & frozen fish',
 t='Finned fish sold raw, chilled or frozen, whole or cut; fish that is smoked, salted, tinned or turned into roe goes to its own department, and shellfish → Shellfish & crustaceans.',
 ax='Which family or water does the fish come from: salmon, cod, open sea, flat, coastal, deep sea or fresh water?',
 sh=[
 sh('Salmon & trout','Salmon, trout and char, wild or farmed, sold whole, in fillets or in portions; smoked or cured salmon → Smoked salmon & gravlax.',None,['Atlantic salmon','Pacific salmon','Trout & char']),
 sh('Cod family & white fish','Cold-water white fish with mild flaky flesh, mostly cod relatives; salted or dried cod → Salted fish and Dried fish, tinned cod → Tinned tuna, salmon & other fish.','kinds by closeness to true cod: cod and haddock, pollock and whiting, hakes, then other white fish',['Cod & haddock','Pollock, saithe & whiting','Hake, hoki & ling','Regional white fish']),
 sh('Oily & open-sea fish','Fast-swimming open-sea fish with rich or firm flesh, from tuna to sardines; smoked, tinned or salted forms → their own departments.','kinds by size, from large open-sea hunters to small shoaling fish',['Tuna','Swordfish & marlin','Amberjack, yellowtail & mahi-mahi','Mackerel & horse mackerel','Pacific saury','Herring','Shad','Sardine','Anchovy, sprat & whitebait']),
 sh('Flatfish, rays & sharks','Flatfish, skate and ray wings, and shark or dogfish, sold whole, in pieces or as fillets; round bony sea fish → Coastal & reef fish.',None,['Flatfish','Skate & ray','Shark & dogfish']),
 sh('Coastal & reef fish','Firm white fish of warm and temperate shores, such as sea bass, bream, snapper and mullet, sold whole or as fillets; deep-water species → Deep-sea & bottom fish.','kinds by family: basses and groupers, breams and snappers, mullets, then other market fish',['Sea bass & grouper','Sea bream & snapper','Red mullet, gurnard & John Dory','Grey mullet & milkfish','Pomfret, croaker & Asian market fish']),
 sh('Deep-sea & bottom fish','Fish caught in deep or cold water or on the sea floor, sold as tails, fillets or steaks; cod relatives → Cod family & white fish.',None,['Monkfish','Deep-sea fish']),
 sh('Freshwater & river fish','Fish raised or caught in rivers and lakes, plus eel and lamprey that migrate between sea and river; sturgeon caviar → Caviar & roe.','kinds by family: tilapia, catfish, carp, pike and perch, whitefish, sturgeon, then eel and lamprey',['Tilapia','Catfish, pangasius & snakehead','Carp','Pike, perch & zander','Whitefish & vendace','Sturgeon','Eel','Lamprey']),
 ]))
D.append(dict(n='Shellfish & crustaceans',
 t='Oysters, other molluscs, crustaceans, squid and similar sea animals sold live, raw or cooked; dried → Dried shellfish & squid, tinned → Tinned shellfish & squid.',
 ax='Which kind of animal is it: oyster, other two-shell mollusc, snail, crab, lobster, prawn, or squid and similar?',
 sh=[
 sh('Oysters','Oysters sold live in the shell, on the half shell or shucked and named by species and growing area; tinned oysters → Tinned shellfish & squid.','kinds by oyster species, from the most farmed to local natives',['Pacific oyster','Native flat oyster','Eastern oyster','Olympia oyster','Kumamoto oyster','Sydney rock oyster']),
 sh('Mussels, clams & scallops','Two-shelled molluscs other than oysters, sold live in the shell or as meat; tinned versions → Tinned shellfish & squid.','kinds by shell shape: mussels, clams, razor clams, cockles, then scallops',['Mussel','Clam','Razor clam','Cockle','Scallop']),
 sh('Snails & abalone','Single-shelled molluscs: abalone, whelks, sea and freshwater snails and land snails, sold in the shell or as meat.','kinds by habitat: abalone and whelk of the sea, other water snails, then land snails',['Abalone','Whelk','Sea & freshwater snails','Land snail']),
 sh('Crabs','Crabs sold whole, as claws or legs, or as picked meat; tinned crab meat → Tinned shellfish & squid.','kinds by crab and its waters: cold-sea crabs, temperate-coast crabs, then warm-water and freshwater crabs',['King crab','Snow crab','Brown crab','Dungeness crab','Blue crab','Stone crab','Mud crab','Chinese mitten crab']),
 sh('Lobsters, crayfish & barnacles','Lobsters and lobster-like crustaceans sold live, cooked or as tails, plus crayfish and barnacles; prawns → Prawns & shrimp.','kinds by claws and size: clawed lobster, spiny lobster, langoustine, squat lobster, then crayfish and barnacles',['Lobster','Spiny lobster','Langoustine','Squat lobster','Crayfish','Barnacle']),
 sh('Prawns & shrimp','Prawns and shrimp sold raw or cooked, whole or peeled and graded by count; dried shrimp → Dried shellfish & squid.','kinds by species, from the most farmed warm-water prawns to small cold-water and freshwater ones',['Whiteleg shrimp','Tiger prawn','King & banana prawn','Northern prawn','Argentine red shrimp','Gulf shrimp','Spot prawn','Brown shrimp','Giant freshwater prawn']),
 sh('Squid, octopus & other sea animals','Squid, octopus, cuttlefish, sea urchins, sea cucumbers, jellyfish and sea squirts, plus mixed packs; dried squid → Dried shellfish & squid.','kinds by animal group: cephalopods, spiny-skinned animals, jellyfish and sea squirts, then mixes',['Squid','Octopus','Cuttlefish','Sea urchin','Sea cucumber','Jellyfish','Sea squirt','Seafood mix']),
 ]))
D.append(dict(n='Smoked fish',
 t='Fish preserved by smoke, plus salmon cured in salt and sugar and sold with it, ready to eat; tinned smoked fish → Tinned & jarred fish, raw fish → Fresh & frozen fish.',
 ax='Which fish is smoked: salmon, a sea fish, or a freshwater or migratory fish?',
 sh=[
 sh('Smoked salmon & gravlax','Salmon cured in salt and smoked cold or hot, or cured without smoke as gravlax; raw salmon → Salmon & trout.',None,['Smoked salmon','Hot-smoked salmon','Gravlax']),
 sh('Smoked sea fish','Herring, haddock, mackerel, halibut and other sea fish smoked whole, split or in fillets; smoked salmon → Smoked salmon & gravlax.','kinds by fish group: herring and sprats, cod family, mackerel, flatfish, deep-sea fish, then tropical fish and sharks',['Kipper & smoked herring','Smoked sprats','Smoked haddock','Smoked mackerel','Smoked halibut','Smoked sable','Smoked milkfish','Smoked dogfish belly']),
 sh('Smoked freshwater & migratory fish','Trout, whitefish, eel, shad and sturgeon smoked whole, in fillets or in slices; smoked salmon → Smoked salmon & gravlax.','kinds by fish: trout and whitefish, then eel and shad, then sturgeon',['Smoked trout','Smoked whitefish','Smoked eel','Smoked shad','Smoked sturgeon']),
 ]))
D.append(dict(n='Tinned & jarred fish',
 t='Fish and shellfish cooked or marinated and sealed in a tin, jar or tub to keep; raw fish → Fresh & frozen fish, fish smoked and sold fresh → Smoked fish.',
 ax='What is in the container: a large fish, a small oily fish, a vinegar-marinated fish or a shellfish?',
 sh=[
 sh('Tinned tuna, salmon & other fish','Large fish packed in tins or jars: tuna, salmon, white fish, eel and cod liver; sardines and other small fish → Tinned sardines & small fish.','kinds by fish, from tuna through salmon and white fish to eel and liver',['Tinned tuna','Bonito del Norte','Tinned salmon & trout','Tinned white fish','Tinned eel','Tinned cod liver']),
 sh('Tinned sardines & small fish','Sardines, mackerel, sprats, herring, anchovies and saury packed in tins or jars in oil, sauce or salt; vinegar-marinated fish → Marinated fish.','kinds by fish, from sardines through mackerel and herring relatives to anchovies',['Tinned sardines','Tinned mackerel','Tinned horse mackerel','Tinned sprats & brisling','Tinned herring','Tinned saury','Tinned anchovies']),
 sh('Marinated fish','Fish marinated in vinegar, oil or sauce and sold chilled in a jar or tub; salt-cured anchovies in oil → Tinned sardines & small fish.',None,['Marinated herring','Marinated anchovies','Vinegar-marinated sea bream']),
 sh('Tinned shellfish & squid','Mussels, cockles, clams, scallops, oysters, crab, octopus, squid and sea snails cooked and packed in tins or jars; raw shellfish → Shellfish & crustaceans.','kinds by animal: two-shelled molluscs, then sea snails, then cephalopods, then crab',['Tinned mussels','Tinned cockles','Tinned clams','Tinned razor clams','Tinned scallops','Tinned oysters','Tinned abalone','Tinned whelk or conch','Tinned octopus','Tinned squid','Tinned crab meat']),
 ]))
D.append(dict(n='Caviar & roe',
 t='Fish eggs sold as separate grains, whole sacs or dried pouches, from sturgeon caviar to salmon and cod roe; sea urchin gonads (uni) → Squid, octopus & other sea animals.',
 ax='How are the eggs sold: as sturgeon caviar, as loose eggs of other fish, or as whole sacs and pouches?',
 sh=[
 sh('Sturgeon & paddlefish caviar','Salted roe of sturgeon, paddlefish and bowfin, sold as separate grains or pressed and listed by species; roe of other fish → Loose roe of other fish.',None,['Sturgeon caviar','American roe']),
 sh('Loose roe of other fish','Separate small eggs of salmon, trout, whitefish, vendace, lumpfish, flying fish and capelin, cured or dyed; whole sacs → Roe sacs & pouches.','kinds by egg size, from large salmon eggs to tiny capelin eggs',['Salmon roe','Trout roe','Whitefish roe','Vendace roe','Lumpfish roe','Flying-fish roe','Capelin roe']),
 sh('Roe sacs & pouches','Roe kept in its membrane, fresh, salted, smoked or dried: herring, pollock and cod roe, and pressed bottarga; loose eggs → Loose roe of other fish.','kinds by cure, from fresh and lightly salted sacs to dried pouches',['Herring roe','Pollock roe','Cod roe','Bottarga']),
 ]))
D.append(dict(n='Salted, dried & fermented fish',
 t='Fish and shellfish kept by salting, drying or fermenting and sold to be soaked, shaved or cooked, or eaten as they are; smoked → Smoked fish, tinned → Tinned & jarred fish.',
 ax='How is it kept: salted, fermented, dried as fish, or dried as shellfish and squid?',
 sh=[
 sh('Salted fish','Fish cured in salt and sold whole, in loins or in fillets, to soak or eat as it is; unsalted air-dried cod → Dried fish.',None,['Salt cod','Salted herring & matjes','Mojama']),
 sh('Fermented fish','Whole fish or seafood preserved by fermentation and eaten as the fish itself; a fermented sauce or paste → Fish sauce in J5.',None,['Fermented fish','Salted fermented seafood']),
 sh('Dried fish','Fish dried hard in air, smoke or sun and sold whole, shaved or shredded; dried shellfish → Dried shellfish & squid.','kinds by use: soaked and cooked, shaved or simmered for stock, grilled, eaten as a snack, or rehydrated as an ingredient',['Stockfish','Katsuobushi','Niboshi','Himono','Dried pollock','Dried filefish','Dried rockfish','Bombay duck','Fish maw','Dried shark fin','Fish floss']),
 sh('Dried shellfish & squid','Shellfish and squid dried whole or in pieces and sold by count or size to rehydrate or cook; raw → Shellfish & crustaceans.','kinds by animal: molluscs, then sea cucumber, then shrimp, then squid',['Dried abalone','Dried scallop','Dried oyster','Dried sea cucumber','Dried shrimp','Dried squid & cuttlefish']),
 ]))
D.append(dict(n='Fish cakes, fingers & surimi',
 t='Processed fish made from paste, coated pieces or patties, sold chilled, frozen or jarred; whole fish that is smoked or tinned → their own departments.',
 ax='How is the fish made up: a paste cooked into cakes, a paste shaped into sticks or balls, coated pieces, or a patty or spread?',
 sh=[
 sh('Fish-paste cakes','Springy cakes of fish paste steamed, boiled, grilled or fried, from Japan and South-east Asia; sticks, balls and sausages of paste → Fish-paste sticks, balls & sausages.','kinds by how the paste is cooked: steamed, boiled, grilled, fried, then leaf-wrapped',['Kamaboko','Hanpen','Chikuwa','Satsuma-age','Otak-otak']),
 sh('Fish-paste sticks, balls & sausages','Fish paste shaped into imitation crab sticks, balls or sausages, not coated or filled; cakes steamed or fried from paste → Fish-paste cakes.',None,['Crab stick','Fish ball','Fish sausage']),
 sh('Coated fish','Pieces or minced blocks of fish in crumb or batter, sold frozen; plain fillets → Fresh & frozen fish.',None,['Fish fingers','Breaded & battered fish']),
 sh('Patties & spreads','Western fish patties, poached gefilte fish and fish pâtés, sold to cook or to cut; Asian paste cakes → Fish-paste cakes.',None,['Fish cake','Gefilte fish','Fish pâté & rillettes']),
 ]))
oldD={x['n']:x for x in d['depts']}
used=set()
out=[]
for dd in D:
    o=oldD[dd['n']]
    ndp={'n':dd['n'],'mode':o.get('mode'),'note':o.get('note'),'b':o.get('b',[]),'t':dd['t'],'ax':dd['ax'],'s':[]}
    if not ndp['note']: del ndp['note']
    for s in dd['sh']:
        ks=[]
        for n in s['k']:
            k=K[n]; used.add(n)
            assert n in TT,n
            k['tt']=TT[n]; k.pop('t',None)
            ks.append(k)
        sd={'n':s['n'],'t':s['t']}
        if s['ax']: sd['ax']=s['ax']
        elif len(s['k'])>3: raise SystemExit('need ax '+s['n'])
        sd['k']=ks; ndp['s'].append(sd)
    out.append(ndp)
left=set(K)-used; assert not left,left
# see links
SEE={
'Atlantic salmon':[('Smoked salmon','cured and smoked'),('Gravlax','cured, not smoked')],
'Smoked salmon':[('Atlantic salmon','the raw fish')],
'Trout & char':[('Smoked trout','smoked'),('Trout roe','the eggs')],
'Cod & haddock':[('Salt cod','salted cod'),('Stockfish','air-dried cod'),('Smoked haddock','smoked haddock')],
'Pollock, saithe & whiting':[('Dried pollock','Korean dried pollock'),('Pollock roe','the roe')],
'Tuna':[('Tinned tuna','tinned'),('Mojama','salt-dried tuna loin'),('Katsuobushi','dried skipjack')],
'Tinned tuna':[('Tuna','the raw fish')],
'Mackerel & horse mackerel':[('Smoked mackerel','smoked'),('Tinned mackerel','tinned')],
'Herring':[('Kipper & smoked herring','smoked'),('Marinated herring','jarred, marinated'),('Salted herring & matjes','salted'),('Herring roe','the roe')],
'Sardine':[('Tinned sardines','tinned')],
'Anchovy, sprat & whitebait':[('Tinned anchovies','tinned and salted'),('Marinated anchovies','marinated'),('Niboshi','dried anchovies')],
'Pacific saury':[('Tinned saury','tinned'),('Himono','dried in Japan')],
'Shad':[('Smoked shad','smoked')],
'Flatfish':[('Smoked halibut','smoked halibut')],
'Deep-sea fish':[('Smoked sable','smoked sablefish')],
'Grey mullet & milkfish':[('Bottarga','mullet roe pouch'),('Smoked milkfish','smoked')],
'Eel':[('Smoked eel','smoked'),('Tinned eel','tinned')],
'Sturgeon':[('Sturgeon caviar','the roe'),('Smoked sturgeon','smoked')],
'Whitefish & vendace':[('Smoked whitefish','smoked'),('Vendace roe','the roe'),('Whitefish roe','the roe')],
'Pacific oyster':[('Tinned oysters','tinned'),('Dried oyster','dried')],
'Mussel':[('Tinned mussels','tinned')],
'Scallop':[('Tinned scallops','tinned'),('Dried scallop','dried adductor')],
'Abalone':[('Tinned abalone','tinned'),('Dried abalone','dried')],
'Squid':[('Tinned squid','tinned'),('Dried squid & cuttlefish','dried')],
'Octopus':[('Tinned octopus','tinned')],
'Sea cucumber':[('Dried sea cucumber','dried')],
'Whiteleg shrimp':[('Dried shrimp','dried')],
'Sea urchin':[('Salted fermented seafood','salted urchin and other shiokara')],
'Kamaboko':[('Crab stick','imitation crab from paste')],
'Crab stick':[('Kamaboko','paste cake')],
'Salted fermented seafood':[('J5|Fish sauce','sauce, not whole seafood')],
'Katsuobushi':[('J5|Dashi and dashi ingredients','stock base')],
'Niboshi':[('J5|Dashi and dashi ingredients','stock base')],
'Tinned cod liver':[('H2|Omega-3 oil','oil supplement')],
'Cod roe':[('Fish pâté & rillettes','taramasalata spread')],
'Fish pâté & rillettes':[('Cod roe','taramasalata base')],
}
def exists(code,name):
    if code=='J2': return name in K
    r=json.load(open(R+'reader/%s.json'%code))
    return any(k['n']==name for dp in r['depts'] for s in dp['s'] for k in s['k'])
nsee=0
for kn,lst in SEE.items():
    k=K[kn]; k['see']=[]
    for tgt,why in lst:
        if '|' in tgt: code,nm=tgt.split('|')
        else: code,nm='J2',tgt
        assert exists(code,nm),(code,nm)
        k['see'].append([code,nm,why]); nsee+=1
d['depts']=out
d['ax']='How is the fish or seafood made ready for sale: raw, smoked, tinned, as roe, salted or dried, or ground into a paste product?'
d['key']=['1. Is it the eggs of a fish, as separate grains, sacs or a dried pouch? → Caviar & roe',
'2. Is it ground fish paste, or fish in crumb or batter, or a patty, ball or spread made from fish? → Fish cakes, fingers & surimi',
'3. Is it cooked or marinated and sealed in a tin, jar or tub? → Tinned & jarred fish',
'4. Is it smoked, or salmon cured in salt and sugar as gravlax? → Smoked fish',
'5. Is it kept by salting, drying or fermenting, whether fish, shellfish or squid? → Salted, dried & fermented fish',
'6. Is it a shellfish, crustacean, mollusc, squid or other sea animal sold raw, live or cooked? → Shellfish & crustaceans',
'7. Is it a raw or frozen finned fish? → Fresh & frozen fish',
'<i>Precedence: roe in any form goes to step 1 first; a smoked fish sealed in a tin is tinned (step 3); a dried shellfish is step 5, not step 6; a fish-paste cake is step 2, not step 3.</i>']
d['lead']='Fish and seafood bought to eat at home, from fresh market species and shellfish to smoked fish, conservas, caviar, cured and dried fish and fish cakes; organised by product form, then by the family of fish or animal, with named origins, houses and grades where buyers compare them.'
tmp=R+'out/J2.json.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/J2.json')
json.dump({'Flatfish & skate':'Flatfish'},open(R+'out/J2_renames.json','w'),ensure_ascii=False,indent=1)
after=dict(depts=len(out),shelves=sum(len(x['s']) for x in out),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))
print(before,after,'see',nsee,'demoted',len(demoted),'dropped',len(dropped))
