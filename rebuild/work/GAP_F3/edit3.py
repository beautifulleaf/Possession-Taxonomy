import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
ks={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh.get('k',[])}
spec={
'Circulation coin':"Covers 20 issuing areas of about 200 in their Wikipedia currency articles, with every world region represented; the other issuers are not added because each needs its own article read and none is a whole-space list.",
'Circulation banknote':"Covers 20 issuing areas of about 200 in their Wikipedia currency articles, with every world region represented; the other issuers are not added because each needs its own article read and none is a whole-space list.",
'Circulating commemorative coin':"Covers the programmes of 5 issuers (United States, euro area, Canada, Australia, Russia) of about 200; the rest are not covered because no whole-space list exists.",
'Definitive stamp':"No complete list exists; covers famous first and regular issues in Wikipedia's List of notable postage stamps and the major administrations only, of about 200 postal administrations; the others are not covered.",
'Gallantry and merit decoration':"Covers the United Kingdom, United States (all services, Army and Joint included), France and Soviet Union lists; Germany's page is only an index and other countries' awards are not covered.",
'Order of chivalry or state order':"Covers the United Kingdom, France, Germany (federal and Bavarian), Soviet Union and Japan lists plus foreign orders worn on US uniforms; other countries' orders are not covered.",
'Campaign medal':"Complete: 86 of 86 in Wikipedia's British campaign medals article (re-read 2026-10-31) and 36 of 36 pages of Wikipedia's category United States campaign medals; France and Soviet Union lists as stated above. Campaign medals of other countries are not covered.",
'Long-service and good-conduct medal':"Covers the United Kingdom and United States awards; other countries are not covered, and no complete list exists.",
'Base card':"Covers the Topps flagship run 1951 to 2025 and the sets named in Wikipedia's Baseball card article; no complete list exists.",
'Trading-card game set':"Covers Pokémon sets to the Mega Evolution series and Magic core sets and expansions of 250 cards or more; Yu-Gi-Oh! and One Piece only from the earlier pass.",
'Commemorative stamp':"No complete list exists; follows the List of notable postage stamps.",
'Official stamp':"No complete list exists; follows the List of notable postage stamps.",
'Revenue stamp':"No complete list exists; follows the List of notable postage stamps.",
'Stamp error and variety':"Complete: the error and rarity rows of Wikipedia's List of notable postage stamps.",
'Vintage tobacco, candy and food card':"No complete list exists; follows Wikipedia's Baseball card article.",
'Bullion coin':"Complete: every series of Wikipedia's List of bullion coins.",
}
for n,line in spec.items():
    k=ks[n]
    s=k['sel'].rstrip()
    if n in('Campaign medal','Base card','Long-service and good-conduct medal','Gallantry and merit decoration','Order of chivalry or state order','Circulation coin','Circulation banknote','Circulating commemorative coin','Definitive stamp','Trading-card game set'):
        # keep text, add the coverage line at the end
        pass
    k['sel']=s+" "+line
for k in ks.values():
    if k.get('x'):
        s=k['sel']
        if not re.search(r'Complete:|Covers |No complete list exists',s):
            k['sel']=re.sub(r'(No whole-space reference exists(?: for [^;]*?)?;)\s*(entries come from|entries are|the earlier)',lambda m:'No complete list exists; follows' if False else m.group(0),s)
            k['sel']=k['sel'].rstrip()+" No complete list exists; follows the overviews named above."
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
# brands
b=json.load(open(P+'F3_brands.json'))
have={x['n'] for x in b['b']}
new=[("Central Bank of the Republic of Türkiye","Turkey","https://en.wikipedia.org/wiki/Turkish_lira"),("Saudi Arabian Monetary Agency","Saudi Arabia","https://en.wikipedia.org/wiki/Saudi_riyal"),("Central Bank of Egypt","Egypt","https://en.wikipedia.org/wiki/Egyptian_pound"),("Central Bank of Nigeria","Nigeria","https://en.wikipedia.org/wiki/Nigerian_naira"),("Bank of Korea","South Korea","https://en.wikipedia.org/wiki/South_Korean_won"),("Central Bank of Argentina","Argentina","https://en.wikipedia.org/wiki/Argentine_peso"),("Bank Indonesia","Indonesia","https://en.wikipedia.org/wiki/Indonesian_rupiah"),("Central Bank of Ireland","Ireland","")]
for n,c,s in new:
    if n not in have: b['b'].append({"n":n,"c":c,"f":"","seg":"Institution & issuer","kf":"currency issuer","d":"Central bank or monetary authority named as issuer in the currency article.","s":s})
json.dump(b,open(P+'F3_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3_brands.json.tmp',P+'F3_brands.json')
