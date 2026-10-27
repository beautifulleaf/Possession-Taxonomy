import json, os, re, sys
os.chdir('/home/user/Possession-Taxonomy/rebuild')
SEG={'LH':'Luxury house','DS':'Designer','CP':'Contemporary & premium','HW':'Heritage & workwear','JD':'Japanese & denim','SW':'Streetwear','OT':'Outdoor & technical','AT':'Athletic & sportswear','HS':'High street','VB':'Value & basics','BA':'Bespoke & artisan','TD':'Traditional & national dress','SC':'Subculture & alternative'}
SRC={'WOLD':'https://en.wikipedia.org/wiki/List_of_oldest_eyewear_companies','MFA':'https://malefashionadvice.substack.com/p/a-list-of-independent-eyeglass-makers','ON':'https://opticiannow.com/?p=1244',
'WLUG':'https://en.wikipedia.org/wiki/Category:Luggage_manufacturers','WBAG':'https://en.wikipedia.org/wiki/Category:Bags_(fashion)','WEYE':'https://en.wikipedia.org/wiki/Category:Eyewear_brands','WUMB':'https://en.wikipedia.org/wiki/Category:Umbrella_manufacturers',
'WEYUS':'https://en.wikipedia.org/wiki/Category:Eyewear_brands_of_the_United_States','WEYIT':'https://en.wikipedia.org/wiki/Category:Eyewear_brands_of_Italy','WEYFR':'https://en.wikipedia.org/wiki/Category:Eyewear_brands_of_France','WEYUK':'https://en.wikipedia.org/wiki/Category:Eyewear_brands_of_the_United_Kingdom','WEYDE':'https://en.wikipedia.org/wiki/Category:Eyewear_brands_of_Germany',
'FPBAG':'https://www.fashion-press.net/brands/all/bag/?word=all','FPEYE':'https://www.fashion-press.net/brands/all/eyewear/?word=all','FPACC':'https://www.fashion-press.net/brands/all/accessory/?word=s','FPLEA':'https://www.fashion-press.net/brands/all/leather/?word=s',
'GOY1':'https://goodonyou.eco/sustainable-handbags/','GOY2':'https://goodonyou.eco/7-sustainable-and-ethical-bags-we-know-you-will-love','REV':'https://reviewed.com/lifestyle/features/10-top-rated-umbrellas-keep-you-dry-totes-davek','IH':'https://www.insidehook.com/travel/best-umbrellas-review',
'RING':'https://www.ringly.io/discover/best-handbag-brands','RINGW':'https://www.ringly.io/discover/best-wallet-brands','MFW':'https://mensflair.com/luxury-wallet-brands/','MF':'https://mensflair.com/streetwear-brands/','ATLAS':'https://theatlasheart.com/best-luggage-brands/',
'BP':'https://www.backpacker.com/gear/backpacks/page/39/?scope=anon','IMP':'https://www.impericon.com/collections/gothic-bags','FBGYM':'https://www.fashionbeans.com/article/best-gym-bags-for-men/','FBEYE':'https://www.fashionbeans.com/article/best-eyewear-brands/',
'HOMO':'https://www.homofaber.com/en/artisans/hiyoshiya-umbrella-making-japan','YAHOO':'https://uk.news.yahoo.com/handmade-apos-tale-best-bags-114900446.html'}
reg={b['n'].strip().lower():b for b in json.load(open('reader/_brands.json'))['b']}
def k(s): return re.sub(r'[^a-z0-9]','',s.lower().replace('&','and'))
regk={k(n):b['n'] for n,b in reg.items()}
out=[]; warn=[]
for l in open('work/_harvest/A4_work/brands.txt'):
    l=l.rstrip('\n')
    if not l or l.startswith('#'): continue
    n,sg,kf,c,f,s,d=(l.split('|')+['']*7)[:7]
    b={'n':n,'seg':SEG[sg],'kf':kf}
    if c: b['c']=c
    if f: b['f']=f
    if d: b['d']=d
    b['s']='knowledge' if s=='knowledge' else ('https://www.wikidata.org/wiki/'+s[3:] if s.startswith('WD:') else SRC[s])
    r=reg.get(n.lower())
    if r:
        if 'A4' in (r.get('cats') or []): warn.append('ALREADY A4: '+n); continue
        if r.get('seg') in SEG.values(): b['seg']=r['seg']
    elif k(n) in regk: warn.append(f'NEAR-DUP: {n} ~ {regk[k(n)]}')
    out.append(b)
p='work/_harvest/A4.json'
json.dump({'b':out},open(p+'.tmp','w'),ensure_ascii=False,indent=0); os.replace(p+'.tmp',p)
print(len(out),'written'); print('\n'.join(warn))
