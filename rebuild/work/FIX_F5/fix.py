import json,os
P='out/'
d=json.load(open(P+'F5.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
    raise KeyError(n)
def rm(n):
    dp,s,i,k=find(n); s['k'].pop(i); return k
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
def shelf(dn,sn,new=False):
    dp=dept(dn)
    for s in dp['s']:
        if s['n']==sn: return s
    s={'n':sn,'k':[]}; dp['s'].append(s); return s
def A(n,dsc,s,mk='',y='',a='',v=None,dt=''):
    return {'n':n,'a':a,'d':dsc,'mk':mk,'y':y,'s':s,'v':v or [],'dt':dt}
WP='https://en.wikipedia.org/wiki/'
# F5-5 duplicates
for n in ['Daguerreotype','Ambrotype','Tintype','Instant print','Posted envelope','Home film reel','Home videotape']: rm(n)
lt=find('Letter')[3]; lt['x']=[x for x in lt['x'] if x['n']!='Aerogramme']
find('Novelty postcard')[3]['x']=[]
nb=find('Written-in notebook')[3]; nb['x']=[]
nb['d']=nb['d']+' Commonplace books are catalogued in F1 Manuscript book.'
# F5-3 merges
for n in ['Snapshot']: rm(n)
find('Photographic print')[3]['t'].append('snapshot (vernacular family print)')
rm('Scrapbook'); find('Photo album')[3]['t'].append('scrapbook')
find('Photo album')[3]['a']='scrapbook · family album'
old={n:rm(n) for n in ['National identity card','Driving licence','Visa','Residence permit','Citizenship certificate','Social security card']}
idsh=find('Passport')[1]
idsh['k'].append({'n':'Identity document','a':'ID card · national identity card · driving licence · visa · residence permit · citizenship certificate · social security card','d':'Card or paper issued by a state to prove who the holder is, what they may do or where they may live.','t':['national identity card','driving licence','visa','residence permit','citizenship certificate','social security card'],'s':old['National identity card']['s']})
gsh=find('Gift card')[1]
lc=rm('Loyalty card'); g=rm('Gift card'); gc=rm('Gift certificate'); mc=rm('Membership card')
gsh['k'].insert(0,{'n':'Gift & membership card','a':'gift card · gift certificate · membership card · loyalty card','d':'Card or certificate holding prepaid value, discounts or membership rights, issued by a retailer or club.','t':['gift card','gift certificate','membership card','loyalty card'],'s':g['s'],'m':lc['m']})
ws=find('Deed')[1]
srcs=[rm(n)['s'] for n in ['Will','Tax paper','House plans','School report']]
pn=rm('Promissory note')
ws['k'].append({'n':'Household & legal papers','a':'will · tax paper · house plans · school report · promissory note','d':'Papers kept at home for the household: wills, tax records, house plans, school reports and promissory notes.','t':['will','tax paper','house plans','school report','promissory note'],'s':srcs[0]})
# F5-1 autographs
au=find('Autograph')[3]
AC=WP+'Autograph_collecting'
au['x']=[
 A('Signed photograph','Photograph signed by its subject; dealers abbreviate it SP or PS.',AC,dt='size · inscription · subject pose · photographer credit'),
 A('Cut signature','Signature clipped from a letter or document and mounted; collectors warn of clipped signatures glued onto engraved portraits.',AC,a='clipped signature',dt='cut from document or letter · mount · date'),
 A('White House card','Card printed "Executive Mansion" or "The White House" and signed by a president; Hayes is popularly credited with introducing it, Grant by some.',"https://www.shapell.org/manuscript/president-rutherford-b-hayes-invents-executive-mansion-card/",y='1870s',a='Executive Mansion card',v=[{'n':'Hayes Executive Mansion card','mk':'','y':'1878','d':'dated 13 December 1878'}],dt='president · printed heading · signed or autopen'),
 A('Signed first-day cover','First-day cover signed by an astronaut, aviator or other notable; first-day covers themselves are catalogued in F3.','https://www.rrauction.com/PastAuctionItem/3421938',a='autographed FDC',dt='signer · cachet · cancellation · flown or not'),
]
au['t']+=['PSA/DNA authentication','JSA authentication','Beckett authentication','seller certificate of authenticity']
sh=shelf('Letters, autographs & manuscripts','Letters & autographs')
sh['k'].insert(1,{'n':'Signed & game-used memorabilia','a':'sports memorabilia · signed ball · game-worn jersey','d':'Ball, bat, jersey or similar object signed by, or worn or used in play by, a notable person.','t':['signed ball','signed bat','game-worn jersey','game-used ball','PSA/DNA, JSA or Beckett authentication','seller certificate of authenticity'],'s':WP+'Sports_memorabilia','x':[
 A('Signed ball or bat','Ball or bat signed by one or more players; clubhouse signatures by staff are a known fake source.',AC,dt='signer(s) · single or team-signed · sweet spot placement'),
 A('Game-worn jersey','Shirt worn in play by a named athlete; collectors prefer unwashed examples, and match-worn signed shirts sell higher.',WP+'Sports_memorabilia',v=[{'n':'Babe Ruth Yankees 1932 World Series jersey','mk':'','y':'1932','d':'sold for $24.12 million in 2024'}],dt='athlete · season · match · signed or unsigned'),
 A('Game-used ball','Ball used in a record or notable play, such as the one hit for a 70th home run in 1998.',WP+'Sports_memorabilia',y='1998',dt='event · provenance'),
]})
# F5-2 ephemera
eshA=shelf('Paper ephemera','Drink, tobacco & table ephemera')
eshB=shelf('Paper ephemera','Badges, cinema & press paper')
eshA['k']+=[
 {'n':'Beer mat','a':'coaster · drink coaster · beer coaster','d':'Absorbent card or pulp mat for resting a drink, printed with a brewery or drink brand; collecting is tegestology.','t':['printed card','wood pulp','brewery advertising','commemorative set'],'s':WP+'Beer_mat','x':[
  A('Friedrich Horn cardboard coaster','First cardboard coaster, made by the German printer Friedrich Horn.',WP+'Beer_mat',mk='Friedrich Horn',y='1880'),
  A('Sputh wood-pulp coaster','First wood-pulp coaster, made by Robert Sputh of Dresden.',WP+'Beer_mat',y='1892'),
  A('Watney\'s pale ale mat','Coaster used by Watney\'s brewery to advertise its pale ale, introducing coasters to the United Kingdom.',WP+'Beer_mat',mk="Watney's",y='1920'),
  A('Quarmby Promotions mat','Printed coaster from Quarmby Promotions of Milnsbridge, a packaging company founded in 1872; coaster production closed in 2009.',WP+'Beer_mat',mk='Quarmby Promotions',y='1931'),
 ]},
 {'n':'Cigar band','a':'cigar label · vitolphilia','d':'Paper or foil loop around a cigar naming the brand or variety; collecting is vitolphilia.','t':['pictorial Golden Age band','utilitarian band','foil band'],'s':WP+'Cigar_band','x':[
  A('Bock-style signed band','Early band credited to cigarmaker Gustave Bock, paper rings bearing his signature on cigars exported to Europe.',WP+'Cigar_band',y='1830s'),
  A('Golden Age pictorial band','Bright pictorial band of the period 1890–1920 when printing advances produced elaborate cigar art.',WP+'Cigar_band',y='1890–1920'),
 ]},
 {'n':'Sugar packet','a':'sugar sachet · sucrology','d':'Single-serving paper packet of sugar or sweetener from a restaurant, hotel or airline; collecting is sucrology.','t':['restaurant packet','airline packet','hotel packet','sweetener packet'],'s':WP+'Sugar_packet','x':[
  A('Sweet \'N Low packet','Pink sweetener packet from the business founded by Benjamin Eisenstadt, credited with inventing the sugar packet.',WP+'Sugar_packet',mk='Cumberland Packing',dt='design · issuer · country'),
 ]},
 {'n':'Matchbook cover','a':'matchcover','d':'Printed cardboard folder holding matches joined at the base, collected as phillumeny.','t':['advertising cover','commemorative cover'],'s':WP+'Matchbox','x':[
  A('Advertising matchbook','Matchbook whose cover carries a business or product advertisement; popular in the 1960s to 1980s hobby.',WP+'Phillumeny',dt='advertiser · cover design · strike')
 ]},
]
eshB['k']+=[
 {'n':'Pinback button','a':'pin-back button · campaign button · badge','d':'Metal disc with a printed image or slogan and a pin fastener on the back; political, advertising and premium types.','t':['campaign button','corporate advertising button','premium button','open-back','closed-back'],'s':WP+'Pin-back_button','x':[
  A('Whitehead & Hoag celluloid button','Celluloid-covered button with a pin anchored to the back, patented by Whitehead & Hoag.',WP+'Pin-back_button',mk='Whitehead & Hoag',y='1896'),
  A('Yellow Kid button','Buttons featuring The Yellow Kid, given as prizes with gum or tobacco.',WP+'Pin-back_button',y='1898'),
  A('Pep cereal button','Button prizes in Kellogg\'s Pep cereal; a full set had 90 buttons in five series.',WP+'Pin-back_button',mk="Kellogg's",y='1945'),
 ]},
 {'n':'Lobby card','a':'front of house card','d':'Small film promotion card, usually 11 × 14 in, issued in sets of eight scenes for display in cinema lobbies.','t':['11 × 14 in','8 × 10 in (pre-1930)','jumbo 14 × 17 in','UK front of house card'],'s':WP+'Lobby_card','x':[
  A('Standard 11 × 14 in lobby card','Eight-card set of scenes from a film; the US standard size.',WP+'Lobby_card',dt='set or single · studio · film year'),
  A('National Screen Service lobby card','Cards printed and distributed by National Screen Service, the main US film-paper supplier from 1940 to 1984.',WP+'Lobby_card',mk='National Screen Service',y='1940–1984'),
 ]},
 {'n':'Press kit','a':'media kit · press pack','d':'Pre-packaged folder of promotional material given to the media, such as a film or band kit with photos and press release.','t':['film press kit','band press kit','electronic press kit'],'s':WP+'Press_kit','x':[
  A('Electronic press kit','Press kit delivered on disk or online; the Sneakers (1992) kit came on a floppy disk and the first online EPK is dated 1995.',WP+'Press_kit',y='1992–1995')
 ]},
]
# matchbox label archetypes
ml=find('Matchbox label')[3]
ml['x']=[A('Matchbox label','Printed paper label on a matchbox; chemical-match labels in collections date from 1810–1815.',WP+'Phillumeny',y='1810–1815',dt='maker · country · series · box size'),
         A('Matchbook cover','Printed cover of a matchbook; the hobby peaked from the 1960s to the 1980s.',WP+'Phillumeny',dt='advertiser · design')]
ml['d']='Printed label from a matchbox, collected as phillumeny; matchbook covers are a separate kind.'
ml['t']=[t for t in ml['t'] if t!='matchbook cover']
ml['a']='phillumeny label'
json.dump(d,open('out/F5.tmp','w'),indent=1,ensure_ascii=False)
os.replace('out/F5.tmp','out/F5.json')
# brands
bj=json.load(open(P+'F5_brands.json')); b=bj['b']; have={x['n'].lower() for x in b}
def B(n,c,f,seg,kf,dsc,s,**kw):
    if n.lower() in have: return
    b.append({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dsc,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,**kw})
B('Friedrich Horn','Germany','','Heritage manufactory','beer mats','German printing company that introduced the first cardboard coaster in 1880.',WP+'Beer_mat')
B("Watney's",'United Kingdom','','Heritage manufactory','beer mats',"Brewery that introduced coasters to the United Kingdom in 1920 to advertise its pale ale.",WP+'Beer_mat')
B('Quarmby Promotions','United Kingdom','1872','Heritage manufactory','beer mats','Packaging company of Milnsbridge that began making coasters in 1931 and ended coaster production in 2009.',WP+'Beer_mat')
B('Whitehead & Hoag','United States','','Heritage manufactory','pinback buttons','New Jersey company whose 1896 patent covered a badge pin or button with the pin anchored to the back.',WP+'Pin-back_button')
B('Cumberland Packing','United States','','Heritage manufactory','sugar packets','Company founded by Benjamin Eisenstadt, inventor of the sugar packet, known for Sweet \'N Low.',WP+'Sugar_packet')
B('National Screen Service','United States','','Specialist','film paper','Main US printer and distributor of studio posters and lobby cards from 1940 to the mid-1980s.',WP+'Lobby_card')
B("Kellogg's",'','','Mainstream','cereal premiums',"Cereal maker whose 1945 Pep cereal packed button prizes.",WP+'Pin-back_button')
n=0
for x in b:
    if x.get('kf')=='transit card' and not x.get('stub'): x['stub']=True; n+=1
print('stubs',n,len(b))
json.dump(bj,open(P+'F5_brands.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'F5_brands.tmp',P+'F5_brands.json')
