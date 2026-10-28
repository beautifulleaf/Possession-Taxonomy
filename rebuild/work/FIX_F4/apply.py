import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F4.json'))
def find(name):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==name: return dp,s,i,k
    raise KeyError(name)
def rm(name):
    dp,s,i,k=find(name); s['k'].pop(i); return k
def shelf(dept,sn):
    for dp in d['depts']:
        if dp['n']==dept:
            for s in dp['s']:
                if s['n']==sn: return s
    raise KeyError(sn)
def arch(n,s,dsc,mk='',y='',a='',dt='',v=None):
    o={'n':n,'a':a,'d':dsc,'mk':mk,'y':y,'s':s}
    if dt:o['dt']=dt
    o['v']=v or []
    return o
W='https://en.wikipedia.org/wiki/'
# F4-5 junk m rows (all makerless m rows), applied last except converted ones
# ---- F4-1 sacred text copy
sh={'n':'Sacred text copies','k':[{
 'n':'Sacred text copy','a':'scripture copy · holy book · prayer book',
 'd':'Physical copy of a scripture or prayer text kept for devotion. Editions and texts are in Literature.',
 't':['family Bible','mushaf','gutka and pothi','folding sutra book','Esther scroll'],
 'tg':['Christian','Islamic','Sikh','Buddhist','Jewish'],'s':W+'Mushaf',
 'x':[
  arch('Family Bible',W+'Family_Bible','Bible handed down through a family.',dt='binding · size · illustrated or plain'),
  arch('Mushaf','%sMushaf'%W,'Written or printed physical copy of the Qur\'an, as distinct from its recitation.',a='Qur\'an copy',
       v=[{'n':'Mushaf al-Tajwid','mk':'','y':'','d':'Printed edition with coloured letters to aid reading with tajwid'},
          {'n':'Medina Quran','mk':'','y':'','d':'Modern printed edition'}],dt='script · size · binding · case'),
  arch('Gutka','https://en.wikipedia.org/wiki/Nitnem','Small Sikh prayer book of chosen hymns; Nitnem is read from a gutka or the wider pothi.',a='Nitnem gutka',
       v=[{'n':'Sundar Gutka','mk':'','y':'','d':'Larger gutka with many compositions, common in Sikh households'},
          {'n':'Panj Granthi','mk':'','y':'','d':'Gutka drawn from five main scriptures of the Guru Granth Sahib'},
          {'n':'Das Granthi','mk':'','y':'','d':'Gutka drawn from main scriptures of the Dasam Granth'}],dt='size · binding · rumala cover'),
  arch('Orihon sutra book',W+'Orihon','Accordion-folded paper strip used in Japan, widely for printing Buddhist sutras.',a='folding book',y='from Tang-dynasty China',dt='paper · covers · folds'),
  arch('Megillat Esther','https://www.muzeummost.cz/en/detail/megilat-esther-scroll-of-esther','Handwritten parchment scroll of the Book of Esther, rolled on a wooden stick and read at Purim.',a='Esther scroll · megillah',dt='parchment strips · script · roller · case'),
 ]}]}
d['depts'][[x['n'] for x in d['depts']].index('Scriptures, scrolls & holders')]['s'].insert(0,sh)
# ---- F4-2 murti, yantra, magic tools, small kinds
dp,s,i,k=find('Murti')
old=k['x']
def mu(n,dsc,v=None): return arch(n,W+'Murti',dsc,v=v)
gan=arch('Ganesha murti',W+'Ganesha','Image of the elephant-headed Hindu deity invoked at the start of rites; common in homes and at festivals.',a='Ganapati · Vinayaka',
  v=[{'n':'Ganesh Chaturthi clay idol','mk':'','y':'','d':'Clay image brought home for the festival and immersed in water at its end'}],dt='clay · brass · marble · size')
nat=[a for a in old if a['n']=='Nataraja'][0]
rest=[a for a in old if a['n']!='Nataraja']
k['x']=[gan,nat,mu('Lakshmi murti','Image of the goddess of wealth, one of the peaceful (saumya) forms.'),mu('Durga murti','Image of the warrior goddess Durga.'),
  mu('Saraswati murti','Image of the goddess of learning, one of the peaceful (saumya) forms.'),mu('Kali murti','Image of Kali in her fierce (ugra) form.')]+rest
dp,s,i,k=find('Siddhachakra yantra')
s['k'][i]={'n':'Yantra','a':'sacred diagram · yantra plate','d':'Geometric diagram worshipped as a form of the divine, engraved on metal plates or built in three dimensions.',
 't':['brass plate','silver or copper plate','Meru (three-dimensional)','small central Navapada'],'tg':['Hindu','Jain'],'s':W+'Sri_Yantra',
 'x':[arch('Sri Yantra',W+'Sri_Yantra','Nine interlocking triangles around a central point, surrounded by lotus petals and an earth square; centre of Shri Vidya worship.',a='Shri Yantra · Sri Chakra',
      v=[{'n':'Flat plate','mk':'','y':'','d':'Two-dimensional diagram, the standard form'},{'n':'Maha Meru','mk':'','y':'','d':'Three-dimensional projection of the Sri Chakra'}],dt='engraved metal · size'),
      arch('Siddhachakra',W+'Siddhachakra','Jain diagram of nine elements on a lotus, worshipped on brass or silver plates.',a='Navapada · Navadevta',dt='brass plate · silver or copper plate')],'m':[]}
tools=shelf('Tarot & divination','Ritual-magic tools')
tools['k']+= [
 {'n':'Wand','a':'ritual wand','d':'Thin rod held in ritual magic and Wicca to invite and direct forces; gentler than the athame.','t':['wood (oak, hazel)','metal','bone or stone','crystal-tipped'],'s':W+'Wand'},
 {'n':'Cauldron','a':'ritual cauldron','d':'Cast-iron pot used on a Wiccan altar to burn incense or petitions and to stand for the Goddess.','t':['cast iron','bronze','with lid','tripod'],'s':W+'Cauldron'},
 {'n':'Book of Shadows','a':'grimoire · Wiccan book','d':'Book of ritual instructions and spells used in Wicca; also a personal journal of rituals.','t':['coven copy','personal journal','bound blank book'],'s':W+'Book_of_Shadows',
  'x':[arch('Gardnerian Book of Shadows',W+'Book_of_Shadows','Text introduced by Gerald Gardner to his Bricket Wood coven in the 1950s and rewritten by Doreen Valiente.',a='British Traditional Wicca',y='1950s',dt='hand-copied by initiates')]}]
for k_ in tools['k'][-3:]: k_['tg']=['Wiccan']
img=shelf('Images, altars & shrines','Crosses, statues & images')
img['k']+=[
 {'n':'Palm cross','a':'woven palm cross','d':'Small cross woven from a blessed palm frond and given out on Palm Sunday.','t':['woven palm','wooden'],'tg':['Christian'],'s':W+'Palm_Sunday'},
 {'n':'Pysanka','a':'Ukrainian Easter egg · pisanka','d':'Egg decorated by writing a design in beeswax and dyeing in stages; a Slavic Easter custom.','t':['hen egg','goose egg','wooden egg','drop-pull','etched'],'tg':['Christian'],'s':W+'Pysanka'}]
ch=shelf('Prayer & devotion aids','Medals, charms & talismans')
ch['k']+=[
 {'n':'Gau box','a':'ghau · Tibetan amulet box','d':'Portable Tibetan shrine worn or carried to hold relics, prayers or protective items.','t':['copper','gold-plated','wood','with deity statue'],'tg':['Buddhist'],'s':'https://enlightenmentthangka.com/products/tibetan-wood-ghau-box'},
 {'n':'Dreamcatcher','a':'spider web charm · asabikeshiinh','d':'Willow hoop with a woven web, hung over a cradle or bed as a protective charm; Anishinaabe in origin.','t':['willow and sinew','pan-Indian craft','feathers and beads'],'tg':['Native American'],'s':W+'Dreamcatcher'}]
# ---- F4-4 merges
def merge(names,new,pos_from):
    dp,s,i,k=find(pos_from); ks=[rm(n) for n in names if True]
    return s,i
# bells
bs=shelf('Prayer & devotion aids','Bells, wheels & sound instruments')
a=rm('Altar hand bell'); b=rm('Standing bowl bell'); c=rm('Tingsha')
idx=[x['n'] for x in bs['k']]
bs['k'].insert(0,{'n':'Altar bell & chime','a':'hand bell · sanctus bell · ghanta · rin · tingsha','d':'Hand bell, standing bowl bell or paired tingsha cymbals rung in a rite. Ones made for music are in Musical Instruments & Music Gear.',
 't':['sanctus (sacring) bell','puja ghanta','drilbu','table rin','large temple rin','tingsha pair','with cushion'],'tg':['Christian','Hindu','Buddhist'],'s':a['s'],'x':a['x'],'m':[]})
# holy water
hs=shelf('Ritual vessels & implements','Holy-water goods'); 
f=rm('Holy-water font'); rm('Holy-water bottle'); rm('Aspergillum')
hs['k'].insert(0,{'n':'Holy-water vessel','a':'stoup · font · aspergillum · holy-water bottle','d':'Vessel or sprinkler for holy water: wall-hung stoup, font, bottle or aspergillum.',
 't':['wall-hung stoup','home font','glass or plastic bottle','souvenir shrine bottle','metal sprinkler','brush','pocket sprinkler'],'tg':['Christian'],'s':f['s'],'m':[]})
# candles
cs=shelf('Light, incense & offerings','Candles & wreaths')
dc=rm('Devotional candle'); pc=rm('Paschal candle'); hc=rm('Havdalah candle'); yc=rm('Yahrzeit candle')
cs['k'].insert(0,{'n':'Ritual candle','a':dc['a'],'d':'Candle made for a rite or devotion: altar, votive, vigil, paschal, havdalah and memorial types.',
 't':dc['t']+['paschal','havdalah braided'],'tg':['Christian','Jewish'],'s':dc['s'],
 'x':dc['x']+[arch('Paschal candle',pc['s'],'Large candle blessed and lit at Easter, marked with cross, alpha and omega, year and five grains.',a=pc['a'],dt='beeswax · oil-filled shell · stand'),
  arch('Havdalah candle',hc['s'],'Braided multi-wick candle lit at the close of the Sabbath.',a=hc['a'],dt='braided · plain · two-wick'),
  arch('Yahrzeit candle',yc['s'],'Long-burning memorial candle in a glass, lit on the anniversary of a death and on festivals.',a=yc['a'],dt='24, 48, 72-hour · seven-day shiva candle')],'m':[]})
# worn
ws=shelf('Prayer & devotion aids','Articles of faith worn')
kara=rm('Kara'); rm('Kanga'); kir=rm('Kirpan')
ws['k'].append({'n':'Worn article of faith','a':'Five Ks · kara · kanga · kirpan','d':'Item a Khalsa Sikh wears: steel bangle (kara), small comb (kanga) or small blade (kirpan). The weapon form is in Weapons.',
 't':['plain steel kara','kara with engraved khanda','wooden kanga','small iron or steel kirpan','gatra strap carrier'],'tg':['Sikh'],'s':kara['s'],'m':[]})
# dowsing
ds=shelf('Tarot & divination','Divination tools')
p=rm('Divination pendulum'); r=rm('Dowsing rod')
ds['k'].append({'n':'Dowsing tool','a':'pendulum · divining rod','d':'Pendulum, forked rod or pair of L-rods held for dowsing or divination. One sold as a survey or pipe-finding tool is in Tools & Workshop Equipment.',
 't':['crystal pendulum','brass pendulum','wooden pendulum','forked stick','L-rods'],'s':r['s'],'m':[]})
# ---- F4-3 tarot
dp,s,i,k=find('Tarot deck')
X={a['n']:a for a in k['x']}
LS='https://aeclectic.net/tarot/cards/lo-scarabeo.shtml'; US='https://aeclectic.net/tarot/cards/us-games.shtml'
mar=X['Tarot de Marseille']
mar['v'].insert(1,{'n':'Ancient Tarot of Marseilles','mk':'Lo Scarabeo','y':'','d':'Reproduction of the 1760 Conver deck'})
mar['v'].insert(2,{'n':'Tarot of Marseilles (Burdel)','mk':'Lo Scarabeo','y':'1751','d':'Reproduction of Claude Burdel\'s cards'})
vis=X['Visconti-Sforza tarot']
vis['v'].append({'n':'Tarot of Visconti Grand Trumps','mk':'Lo Scarabeo','y':'','d':'Majors-only edition of the Visconti tarot'})
ind=arch('Independent artist tarot',US,'Deck designed and illustrated by one artist outside the three historic pattern lineages, sold under a publisher line.',a='artist deck',
 v=[{'n':'Aquarian Tarot','mk':'U.S. Games Systems','y':'1970s','d':'David Palladini\'s art deco deck'},
    {'n':'The Wild Unknown Tarot','mk':'HarperOne','y':'2016','d':'Kim Krans; boxed edition'},
    {'n':'Everyday Witch Tarot','mk':'Llewellyn','y':'','d':'78 scenes of black-hatted witches'},
    {'n':'Tarot of the White Cats','mk':'Lo Scarabeo','y':'','d':'Also sold as a mini'}]+
   [{'n':n,'mk':'','y':'','d':''} for n in ['Isomorphic Tarot','Lightseer\'s Tarot','Mary-El Tarot','Modern Witch Tarot','Mythic Tarot','Osho Zen Tarot']],dt='artist · publisher line · size · box')
k['x']=[mar,X['Rider-Waite-Smith tarot'],X['Thoth tarot'],vis,X['Sola Busca tarot'],ind]
k['m']=[]
k['t']=['standard 78 cards','pocket size','reproduction','independent artist deck']
dp,s,i,k=find('Oracle deck')
HH='https://aeclectic.net/tarot/cards/hay-house.shtml'
k['x']=[k['x'][0],
 arch('Hay House oracle line',HH,'Publisher line of angel, faerie and guidance oracle decks, many by Doreen Virtue.',mk='Hay House',
  v=[{'n':n,'mk':'Hay House','y':'','d':dd} for n,dd in [('Angel Therapy Oracle Cards','Doreen Virtue'),('Archangel Oracle','Doreen Virtue'),('Ascended Masters Oracle','Doreen Virtue'),('Healing with the Faeries Oracle','Doreen Virtue'),('Earth Magic Oracle Cards','Steven Farmer'),('Fool\'s Wisdom Oracle','Sonia Choquette')]],dt='card count · guidebook · box'),
 arch('Independent artist oracle',HH,'Oracle deck from a single author or artist, not part of a publisher line.',a='artist oracle',
  v=[{'n':n,'mk':'','y':'','d':''} for n in ['Faeries Oracle','Goddess Oracle','Mythic Oracle','The Burning Serpent Oracle','Universal Wisdom Oracle','Wild Spirit Wisdom Oracle','Wisdom of the Oracle']])]
k['m']=[]
# ---- F4-7 cross-links
_,_,_,k=find('Calligraphy wall panel'); k['d']='Framed Qur\'anic or devotional calligraphy made for the home. Calligraphy as art, including hilye panels, is in Art.'
_,_,_,k=find('Thangka & scroll painting'); k['d']=k['d']+' Thangka as painting is also in Art.'
# ---- F4-5 delete all remaining makerless m rows
n=0
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if 'm' in k:
        new=[m for m in k['m'] if m[1]]; n+=len(k['m'])-len(new); k['m']=new
print('deleted m',n)
json.dump(d,open(P+'F4.tmp','w'),ensure_ascii=False,indent=1)
# brands
b=json.load(open(P+'F4_brands.json'))
for nm,kf,ds,src in [('Hay House','spiritual publishing','Publisher of oracle decks by Doreen Virtue, Colette Baron-Reid, Steven Farmer and Sonia Choquette.',HH),
  ('HarperOne','mind-body-spirit books','Publisher of The Wild Unknown Tarot by Kim Krans (2016).','https://hennesseyingalls.com/book/9780062466594')]:
    b['b'].append({'n':nm,'c':'','f':'','seg':'Specialist' if nm=='Hay House' else 'Mainstream','kf':kf,'d':ds,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':src})
json.dump(b,open(P+'F4_brands.tmp','w'),ensure_ascii=False,indent=1)
