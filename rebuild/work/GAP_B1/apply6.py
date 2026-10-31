import json,os
P='rebuild/out/B1.json'
d=json.load(open(P))
S='https://homenewsnow.com/blog/2026/06/22/home-news-now-125-furniture-bedding-retailers-2025-nos-1-25/'
rows=[('Ashley Store','$6,257.3 million'),('Wayfair','$5,955.0 million'),('Amazon','$5,700.0 million'),('Mattress Firm','$3,582.0 million'),('Walmart','$3,520.0 million'),('Costco','$3,500.0 million'),('Rooms To Go','$3,278.1 million'),('Williams Sonoma','$2,900.0 million'),('Ikea','$2,810.0 million'),('RH','$2,335.0 million'),('La-Z-Boy Furniture','$1,421.5 million'),('Sleep Number','$1,270.0 million')]
dep={dp['n']:dp for dp in d['depts']}
a=dep['Sofas & armchairs']; b=dep['Beds & mattresses']; c=dep['Chairs, stools & benches']
have={(m['mkt'],m['who']) for m in a['ms']}
for w,s in rows:
    if w in('Mattress Firm','Sleep Number'): continue
    if ('US furniture and bedding retail',w) in have: continue
    a['ms'].append({"mkt":"US furniture and bedding retail","who":w,"share":s,"yr":2025,"s":S,"note":"US furniture and bedding sales, Home News Now 125 ranking (estimates); rank "+str([r[0] for r in rows].index(w)+1)})
for w,s in rows:
    if w in('Mattress Firm','Sleep Number'):
        b['ms'].append({"mkt":"US furniture and bedding retail","who":w,"share":s,"yr":2025,"s":S,"note":"US furniture and bedding sales, Home News Now 125 ranking (estimates); rank "+str([r[0] for r in rows].index(w)+1)})
c['ms']=[{"mkt":"Office furniture ownership","who":"HNI Corporation","share":"US$2.2 billion (price paid for Steelcase)","yr":2025,"s":"https://en.wikipedia.org/wiki/Steelcase","note":"acquisition announced 2025 and closed December 2025"}]
c['msum']="Office seating is led by a few office-furniture groups. MillerKnoll holds Herman Miller and Knoll; HNI bought Steelcase in December 2025. The figure shown is a deal price, not market share."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
