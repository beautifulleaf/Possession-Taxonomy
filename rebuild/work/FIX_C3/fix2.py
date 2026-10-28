import json,re,copy
R='/home/user/Possession-Taxonomy/rebuild/'
c3=json.load(open(R+'out/C3.json'))
W='https://en.wikipedia.org/wiki/'
shelves={s['n']:s for dp in c3['depts'] for s in dp['s']}
depts={dp['n']:dp for dp in c3['depts']}
kinds={k['n']:(s,k) for dp in c3['depts'] for s in dp['s'] for k in s['k']}
def arch(n,d,s,mk='',y='',a='',v=None,dt=''):
    o={'n':n,'d':d,'s':s}
    for kk,vv in (('mk',mk),('y',y),('a',a),('dt',dt)):
        if vv:o[kk]=vv
    if v:o['v']=v
    return o
log=[]
# ---- C3-1 new kinds
def add(shelf,n,d,s,x=None,t=None,a=''):
    k={'n':n,'d':d,'s':s}
    if a:k['a']=a
    if t:k['t']=t
    k['x']=x or []
    shelves[shelf]['k'].append(k);kinds[n]=(shelves[shelf],k)
H=W+'Helleborus'
add('Perennials & grasses','Hellebore','Hardy evergreen perennial (Helleborus) flowering in winter and early spring; hybrids and species are collected.',H,[
 arch('Helleborus × hybridus','Lenten rose hybrids, the main garden hellebore group, from H. orientalis and relatives.',H,a='Lenten rose · H. orientalis'),
 arch('Helleborus niger','Christmas rose, a white-flowered winter species.',H,a='Christmas rose · black hellebore'),
 arch('Helleborus argutifolius','Corsican hellebore, with green flowers and spiny leaves.',H,a='Corsican hellebore'),
 arch('Helleborus foetidus','Stinking hellebore, with green bell flowers.',H,a='stinking hellebore · setterwort'),
 arch('Helleborus × nigercors','Hybrid of H. niger and H. argutifolius.',H),
 arch('Helleborus × sternii','Hybrid of H. argutifolius and H. lividus.',H),
 arch('Helleborus × ballardiae','Hybrid of H. niger and H. lividus.',H),
 arch('Helleborus × ericsmithii','Hybrid of H. niger and H. × sternii.',H)],
 t=['single','double','anemone-centred','picotee','spotted'],a='Helleborus · Lenten rose · Christmas rose')
A=W+'Agapanthus'
add('Perennials & grasses','Agapanthus','Clump-forming South African perennial with blue or white flower globes; evergreen and deciduous forms.',A,[
 arch('Agapanthus praecox','Evergreen species, widely grown in mild climates.',A),
 arch('Agapanthus africanus','Type species of the genus, native to South Africa.',A),
 arch('Agapanthus campanulatus','Deciduous bell agapanthus, among the hardier species.',A,a='African bluebell'),
 arch('Agapanthus inapertus','Drakensberg agapanthus with drooping flowers.',A,a='drooping agapanthus'),
 arch('Agapanthus caulescens','Species from South Africa.',A),
 arch("Agapanthus coddii","Codd's agapanthus, a blue-flowered species.",A)],t=['evergreen','deciduous','dwarf','white'],a='African lily · lily of the Nile')
P=W+'Primula_auricula'
add('Perennials & grasses','Auricula','Alpine primula (Primula auricula) and its florists\' hybrids, grown in pots or borders.',P,[
 arch('Primula auricula','The mountain species of central European rocks from which garden auriculas descend.',P,a='bear\'s ear · mountain cowslip')],t=['show','alpine','border','double'],a='Primula auricula · bear\'s ear')
C=W+'Chrysanthemum'
add('Perennials & grasses','Garden chrysanthemum','Autumn-flowering perennial chrysanthemum grown in borders, pots or for exhibition, as opposed to cut stems.',C,
 t=['incurve','reflex','spider','pompon','anemone','single','spoon','quill','decorative'],a='garden mum · exhibition chrysanthemum')
B=W+'Bougainvillea'
add('Shrubs, trees & climbers','Bougainvillea','Tender woody climber with papery coloured bracts, grown outdoors in warm climates or under glass.',B,[
 arch('Bougainvillea glabra','Paper flower, one of the first species introduced to Europe.',B,a='paper flower'),
 arch('Bougainvillea spectabilis','Species long confused with B. glabra, introduced to Europe early.',B),
 arch('Bougainvillea × buttiana','Garden hybrid of B. glabra and B. peruviana, source of many cultivars.',B),
 arch("'San Diego Red'",'Cultivar holding an RHS Award of Garden Merit.',B),
 arch("'Mary Palmer's Enchantment'",'Cultivar holding an RHS Award of Garden Merit.',B)],t=['climber','shrub','dwarf','variegated'])
M=W+'Mandevilla'
add('Shrubs, trees & climbers','Mandevilla','Tender twining climber with trumpet flowers, grown in pots outdoors in summer or under glass.',M,[
 arch('Mandevilla sanderi','Species used to develop many garden hybrids.',M,a='Brazilian jasmine'),
 arch('Mandevilla splendens','Species used to develop many garden hybrids.',M),
 arch('Mandevilla × amabilis','Hybrid from which many garden cultivars derive.',M,v=[{'n':"'Alice du Pont'",'d':'RHS Award of Garden Merit'}]),
 arch("Sundaville Cream Pink ('Sunparapibra')",'Mandevilla cultivar holding an RHS Award of Garden Merit.',M)],a='Dipladenia')
for nm,ar in (('Hedging & topiary plant',None),):
    BX=W+'Buxus_sempervirens';YW=W+'Taxus_baccata';BE=W+'Fagus_sylvatica'
    add('Shrubs, trees & climbers','Hedging & topiary plant','Clipped evergreen or marcescent shrub sold for formal hedges, edging and topiary.',BX,[
     arch('Box (Buxus sempervirens)','Common box, evergreen, tolerates close shearing; threatened by box tree moth.',BX,a='boxwood',v=[{'n':"'Elegantissima'"},{'n':"'Vardar Valley'"},{'n':"'Marginata'"}]),
     arch('Yew (Taxus baccata)','Dense dark evergreen with slow growth, widely used for formal hedges and topiary.',YW,v=[{'n':"'Fastigiata' (Irish yew)",'d':'RHS Award of Garden Merit'},{'n':"'Standishii'",'d':'RHS Award of Garden Merit'},{'n':"'Icicle'",'d':'RHS Award of Garden Merit'},{'n':"'Repandens'",'d':'RHS Award of Garden Merit'}]),
     arch('European beech (Fagus sylvatica)','Deciduous hedge whose clipped leaves stay on through winter.',BE,v=[{'n':"'Purpurea' (copper beech)"},{'n':"'Atropurpurea'"}])],
     t=['box','yew','beech','bare-root','potted','root-balled'],a='hedge plant · topiary · box hedging')
Dk=W+'Dicksonia'
add('Shrubs, trees & climbers','Tree fern','Tall fern with a fibrous trunk, sold as a cut trunk or potted plant for sheltered gardens.',Dk,[
 arch('Dicksonia antarctica','Soft tree fern, the commonest garden tree fern.',Dk,a='soft tree fern'),
 arch('Dicksonia fibrosa','Woolly tree fern.',Dk,a='woolly tree fern'),
 arch('Dicksonia squarrosa','Rough or slender tree fern.',Dk,a='rough tree fern')],a='Dicksonia')
T=W+'Trachycarpus'
add('Shrubs, trees & climbers','Hardy palm','Fan palm (Trachycarpus) tolerant of frost, grown in temperate gardens and pots.',T,[
 arch('Trachycarpus fortunei','Chusan palm, the commonest cultivated species and northernmost naturally growing palm.',T,a='Chusan palm · windmill palm'),
 arch('Trachycarpus takil','Probably hardier than T. fortunei; from north-west India and Nepal.',T),
 arch('Trachycarpus princeps','Species from Yunnan, China.',T),
 arch('Trachycarpus oreophilus','Species from north-west Thailand and Manipur.',T),
 arch('Trachycarpus nanus','Dwarf species from China, under a metre tall.',T)],a='Trachycarpus · windmill palm')
Cl=W+'Clivia'
add('Flowering houseplants','Clivia','Evergreen South African bulbous plant with orange or yellow flower clusters, kept as a houseplant.',Cl,[
 arch('Clivia miniata','The most widely cultivated species, flowers from deep red-orange to pale yellow.',Cl,a='bush lily'),
 arch('Clivia nobilis','Type species, described by John Lindley in 1828.',Cl),
 arch('Clivia gardenii','Species that flowers in autumn.',Cl),
 arch('Clivia caulescens','Species that flowers in late winter and spring.',Cl),
 arch('Clivia mirabilis','Low-light species from the Western Cape, named in 2000.',Cl),
 arch('Clivia robusta','Species named in 2004.',Cl),
 arch("Clivia 'Variegata'",'Cultivar with variegated leaves.',Cl)],t=['orange','yellow','variegated'],a='bush lily · Natal lily')
F=W+'Fritillaria'
add('Bulbs, corms & tubers','Fritillaria bulb','Dormant bulb of a fritillary, sold dry for autumn planting.',F,[
 arch('Fritillaria meleagris',"Snake's head fritillary.",F),
 arch('Fritillaria imperialis','Crown imperial.',F),
 arch('Fritillaria persica','Persian fritillary.',F),
 arch('Fritillaria pallidiflora','Siberian fritillary.',F),
 arch('Fritillaria pyrenaica','Pyrenean fritillary.',F),
 arch('Fritillaria acmopetala','Pointed-petal fritillary.',F)],t=['loose bulbs','pre-packed'],a='fritillary')
G=W+'Gladiolus'
add('Bulbs, corms & tubers','Gladiolus corm','Dormant gladiolus corm sold for spring planting, tender large-flowered or hardier small types.',G,[
 arch('Grandiflorus hybrids','Tetraploid hybrids with giant flower spikes.',G),
 arch('Primulinus hybrids','A main hybrid group from crossing four or five species.',G),
 arch('Nanus hybrids','Small hybrids hardy to at least -15 C.',G),
 arch('Gladiolus × byzantinus','Natural and artificial hybrid species.',G)],t=['loose corms','pre-packed','top size'],a='sword lily')
Ra=W+'Ranunculus_asiaticus'
add('Bulbs, corms & tubers','Ranunculus tuber','Dry claw-shaped tuber of the Persian buttercup (Ranunculus asiaticus) sold for planting.',Ra,[
 arch("'Bloomingdale'",'Double-flowered Persian buttercup cultivar.',Ra),
 arch("'Tecolote'",'Double-flowered Persian buttercup cultivar.',Ra),
 arch("'Picotee'",'Persian buttercup cultivar.',Ra),
 arch("'Pot Dwarf'",'Compact Persian buttercup cultivar.',Ra)],t=['loose tubers','pre-packed','double'],a='Persian buttercup')
Fr=W+'Freesia'
add('Bulbs, corms & tubers','Freesia corm','Dormant freesia corm sold for planting; fragrant garden freesias are hybrids of several species.',Fr,[
 arch('Freesia refracta','Cape species naturalised in several countries; a parent of garden freesias.',Fr),
 arch('Freesia leichtlinii','Cape species naturalised in Corsica, California and elsewhere.',Fr),
 arch('Freesia corymbosa','Cape species.',Fr),
 arch('Freesia grandiflora','Species from tropical and south-east Africa.',Fr)],t=['loose corms','pre-packed','single','double'])
# ---- C3-2 cannabis
CS=W+'Cannabis_strain'
kinds['Cannabis plant'][1]['x'].insert(0,arch('Skunk','Strong-smelling sativa-indica hybrids that began in the early 1980s in the United States and were developed by Dutch growers.',CS,a='Skunk strains'))
# ---- C3-4 placeholders -> flatten versions
vague={'RHS AGM Sarracenia cultivars','Registered Heliamphora cultivars','Variegated cultivars','US apricot cultivars','Runner bean cultivars',"Collectors' AGM cultivars",'RHS group examples'}
nflat=0;nflatk=0
def isph(n):return n.startswith('Other ') or n in vague
def flatten(k,keep_idx=None):
    global nflat
    out=[]
    for x in k.get('x',[]):
        if isph(x['n']):
            for v in x.get('v',[]):
                out.append(arch(v['n'],(v.get('d') or x['d']),x['s'],mk=v.get('mk',''),y=v.get('y',''),dt=x.get('dt','')));nflat+=1
        else:out.append(x)
    k['x']=out
for dp in c3['depts']:
    for s in dp['s']:
        for k in s['k']:
            if any(isph(x['n']) for x in k.get('x',[])):flatten(k)
# ---- C3-5 shared types
bon=depts['Bonsai']
styles=None
for s in bon['s']:
    for k in s['k']:
        if len(k.get('t',[]))==19:
            styles=styles or k['t'];k.pop('t')
bon['note']=(bon.get('note','')+' Styles apply to any bonsai: '+'; '.join(styles)+'.').strip()
seed_t={'packet','open-pollinated','F1 hybrid','heirloom','organic','pelleted'}
sd=depts['Seeds, bulbs & cuttings']
for k in shelves['Seeds & cuttings']['k']:
    if 'packet' in (k.get('t') or []):k['t']=[t for t in k['t'] if t not in seed_t]
    if not k.get('t'):k.pop('t',None)
sd['note']=(sd.get('note','')+' Seed packets come as packet, open-pollinated, F1 hybrid, heirloom, organic or pelleted; those attributes apply to every seed kind.').strip()
# christmas tree merge
xs=shelves['Christmas trees']
old=xs['k'];xs['k']=[]
XT=W+'Christmas_tree'
sp=[('Nordmann fir','Abies nordmanniana'),('Fraser fir','Abies fraseri'),('Noble fir','Abies procera'),('Norway spruce','Picea abies'),('Blue spruce','Picea pungens')]
xa=[]
for k in old:
    pass
xa=[arch('Norway spruce (Picea abies)','The original Christmas tree, generally the cheapest.',XT,a='Norway spruce'),
    arch('Nordmann fir (Abies nordmanniana)','Fir sold as a Christmas tree.',XT,a='Nordmann fir'),
    arch('Noble fir (Abies procera)','Fir sold as a Christmas tree.',XT,a='Noble fir'),
    arch('Fraser fir (Abies fraseri)','Fir sold as a Christmas tree.',XT,a='Fraser fir'),
    arch('Blue spruce (Picea pungens)','Blue-needled spruce sold as a Christmas tree.',[k for k in old if k['n']=='Blue spruce'][0]['s'],a='Blue spruce'),
    arch('Scots pine (Pinus sylvestris)','Pine sold as a Christmas tree.',XT),
    arch('Douglas fir (Pseudotsuga menziesii)','Conifer sold as a Christmas tree.',XT)]
xs['k'].append({'n':'Christmas tree','d':'Real conifer sold for Christmas, cut, pot-grown or rooted; the species is the choice buyers compare.','s':XT,'t':['cut','pot-grown','rooted'],'x':xa,'a':'real Christmas tree'})
# ---- C3-6 roses: flatten groups
def flat_rose(k):
    out=[];types=list(k.get('t',[]))
    for x in k.get('x',[]):
        if x.get('v'):
            for v in x['v']:
                out.append(arch(v['n'],(f"{x['n']}: {v['d']}" if v.get('d') else f"Named rose in the {x['n'].lower()} group."),x['s'],mk=v.get('mk',''),y=v.get('y',''),dt=x.get('dt','')))
            g=x['n']
            if g not in types and len(g)<40:types.append(g)
        elif re.search(r'roses$|series$',x['n']):
            if x['n'] not in types:types.append(x['n'])
        else:out.append(x)
    k['x']=out;k['t']=types
flat_rose(kinds['Old garden rose'][1]);flat_rose(kinds['Shrub rose'][1])
# ---- C3-7 duplicates plant vs seed
def nm(n):return re.sub(r'[^a-z0-9]','',n.lower())
for plant,seed in (('Tomato plant','Tomato seed'),('Chilli plant','Chilli & pepper seed')):
    sx={nm(x['n']) for x in kinds[seed][1]['x']}
    kinds[plant][1]['x']=[x for x in kinds[plant][1]['x'] if nm(x['n']) not in sx]
    log.append((plant,'kept non-duplicates'))
    kinds[plant][1]['d']=kinds[plant][1]['d'].rstrip('.')+'; cultivars are listed under '+seed+'.'
json.dump(c3,open(R+'out/C3.json.tmp','w'),ensure_ascii=False,indent=1)
print('flattened',nflat,log)
