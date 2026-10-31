import json,os,re
P='rebuild/out/E5.json'
d=json.load(open(P))
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
def ent(k,n):
    for e in k['x']:
        if e['n']==n: return e
def addv(kn,en,vs):
    e=ent(kind(kn),en); e.setdefault('v',[])
    have={v['n'] for v in e['v']}
    for vn,y,dd in vs:
        if vn not in have: e['v'].append({'n':vn,'mk':e.get('mk',''),'y':y,'d':dd})
W='https://en.wikipedia.org/wiki/'
# boards
k=kind('Arcade system board')
k['x']=[e for e in k['x'] if e['n']!='Taito NESYS']
ent(k,'Taito F3 System').update(y='1993',s='https://arcade-museum.com/Videogame/taito-f3-package-system',d='Taito 32-bit arcade board with swappable cartridges; sold in North America as Cybercore. Arcade Museum dates it 1993.')
ent(k,'Atomiswave').update(y='2002',s='https://www.arcade-museum.com/Videogame/atomiswave')
ent(k,'Mega System 1').update(y='1988',s=W+'P-47:_The_Phantom_Fighter',d='Jaleco arcade board; the earliest game found, P-47, reached Japanese arcades in May 1988.')
ent(k,'Mega System 32').update(y='1994',s='https://arcade-museum.com/Videogame/jaleco-mega-system-32',d='Jaleco cartridge-based arcade board on a V70 processor, produced 1994 to 1997.')
k['x'].append({'n':'Aleck 64','a':'','d':'Nintendo arcade board based on the Nintendo 64, in use from 1998 to 2003.','mk':'Nintendo','y':'1998','s':W+'Nintendo_64','v':[],'dt':'','g':'Nintendo'})
k['x'].sort(key=lambda e:(e.get('g',''),e.get('y') or '9999',e['n']))
k['sel']=k['sel'].replace('except the Williams','except Taito NESYS (an online network, not a board), the Williams').replace('Covers 79 boards','Covers %d boards'%len(k['x']))
k['sel']=k['sel'].replace('(the Konami GX and Taito F3 articles gave 404)','(the Konami GX Wikipedia article gave 404). TIA-MC-1 has no year: searched "TIA-MC-1 Soviet arcade machine year Ekstrema", sources say mid-1980s')
# discs
k=kind('Game disc')
for n,m,y,desc,s in [
 ('Saturn CD-ROM game disc','Sega','1994','CD-ROM disc used for Saturn games; the console launched in Japan in 1994.',W+'Sega_Saturn'),
 ('3DO CD-ROM game disc','3DO Company','1993','CD-ROM disc used for 3DO games, with the Opera file system.',W+'3DO_Interactive_Multiplayer'),
 ('CD-i disc','Philips','1991','Disc in the CD-i (Green Book) format; many full-motion video titles needed the optional MPEG cartridge.',W+'Philips_CD-i'),
 ('PC-FX CD-ROM game disc','NEC','1994','CD-ROM disc used for PC-FX games; the console launched in Japan in December 1994.',W+'PC-FX'),
 ('Neo Geo CD game disc','SNK','1994','CD-ROM disc for the Neo Geo CD, a cheaper medium than the cartridges of the original Neo Geo.',W+'Neo_Geo_CD'),
]:
    if not ent(k,n): k['x'].append({'n':n,'a':'','d':desc,'mk':m,'y':y,'s':s,'v':[],'dt':'','g':m})
k['x'].sort(key=lambda e:(e.get('g',''),e.get('y') or '9999',e['n']))
k['sel']=re.sub(r' No complete list exists.*$','',k['sel']).rstrip()+" Wikipedia's Optical disc article was read to its end (the tail is a navigation box with no console text). No complete list exists; follows those console articles. Dreamcast, Mega-CD, Jaguar CD, Wii U and Switch formats are covered by their own entries or by Disk or CD drive add-on."
# revisions
addv('Home console','Neo Geo CD',[('Neo Geo CD front-loading','1994','Japan only, 25,000 units'),('Neo Geo CD top-loading','','sold worldwide; the article gives no year'),('Neo Geo CDZ','1995','Japan only, double-speed drive')])
addv('Home console','FM Towns Marty',[('FM Towns Marty 2','1994','named in the Wikipedia introduction')])
addv('Home console','Nintendo 64',[('Nintendo 64 Funtastic Series','2000','coloured consoles and controllers, ad campaign year')])
k=kind('Handheld console')
for en,vs in {
 'Cybiko':[('Cybiko Classic','2000','released April 2000'),('Cybiko Xtreme','2001','faster processor, more RAM and a microphone')],
 'Tapwave Zodiac':[('Zodiac 1','2003','32 MB'),('Zodiac 2','2003','128 MB')],
 'Mega Duck':[('Mega Duck WG-108','1993','base unit, also Cougar Boy'),('Cougar Boy','','South American name'),('Mega Duck Super Junior Computer','','German laptop variant by Hartung')],
 'Watara Supervision':[('Quickshot Supervision (QS-800)','','UK and Greece'),('Hartung Supervision (SV-100)','','Germany and Netherlands'),('Magnum Supervision','','US and Europe')],
 'Neo Geo X':[('Neo Geo X Gold Limited Edition','2012','')],
}.items(): addv('Handheld console',en,vs)
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
