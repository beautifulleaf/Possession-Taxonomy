import json,os,sys
S={'A':'https://nstperfume.com/perfume-houses-a-to-b','C':'https://nstperfume.com/perfume-houses-c/','D':'https://nstperfume.com/perfume-houses-d-to-e/','F':'https://nstperfume.com/perfume-houses-f-to-g/','H':'https://nstperfume.com/perfume-houses-h-to-j/','K':'https://nstperfume.com/perfume-houses-k-to-l/','M':'https://nstperfume.com/perfume-houses-m/','N':'https://nstperfume.com/perfume-houses-n-to-o/','P':'https://nstperfume.com/perfume-houses-p/','Q':'https://nstperfume.com/perfume-houses-q-to-r/','S':'https://nstperfume.com/perfume-houses-s/','T':'https://nstperfume.com/perfume-houses-t/','U':'https://nstperfume.com/perfume-houses-u-to-z/','CB':'https://cultbeauty.co.uk/c/fragrance','BN':'https://beautinow.com/all-perfume-brands','SNK':'https://www.spacenk.com/us/fragrance/personal-fragrance','WC':'https://en.wikipedia.org/wiki/Category:Perfume_houses','WN':'https://en.wikipedia.org/wiki/Niche_perfume','FM':'https://www.factmagazines.com/uae/dubai/arabian-perfume-brands','JD':'https://jingdaily.com/posts/chinese-fragrance-brands-documents-to-summer-melt-season','SH':'https://shopee.sg/blog/chinese-perfume-brands/','DV':'https://dailyvanity.sg/news/korean-perfume-brands/','RB':'https://retailboss.co/top-10-designer-dupe-perfume-brands-to-shop/','OI':'https://luxe.outlookindia.com/whats-new/7-homegrown-indian-perfume-brands-that-are-making-scentsational-waves','GS':'https://gestalten.com/blogs/journal/the-oldest-perfumery-in-delhi','K0':'knowledge'}
SEG={'LH':'Luxury house','HM':'Haute maison','IM':'Independent maker','DS':'Designer','PR':'Premium','MS':'Mainstream','VA':'Value','BA':'Bespoke & artisan','TR':'Traditional & regional'}
out='work/_harvest/H4.json'
cur=json.load(open(out))['b'] if os.path.exists(out) else []
have={b['n'].lower() for b in cur}
for ln in open('work/_harvest/H4_work/brands.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln or ln.startswith('#'): continue
    n,sg,kf,c,f,s,d=ln.split('|')
    if n.lower() in have: continue
    b={'n':n,'seg':SEG[sg],'kf':kf}
    if c: b['c']=c
    if f: b['f']=f
    if d: b['d']=d
    b['s']=S[s]; cur.append(b); have.add(n.lower())
json.dump({'b':cur},open(out+'.tmp','w'),ensure_ascii=False,indent=0)
os.replace(out+'.tmp',out); print(len(cur))
