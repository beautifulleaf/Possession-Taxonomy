import json,os,re
P='rebuild/out/J10.json'
d=json.load(open(P))
kinds={K['n']:K for D in d['depts'] for S in D['s'] for K in S['k']}
KM={'Straight Virginia':'Virginia blend','Virginia Based':'Virginia blend','Virginia/Perique':'Virginia/Perique blend','Virginia/Latakia':'English & Balkan blend','English':'English & Balkan blend','Balkan':'English & Balkan blend','Scottish':'English & Balkan blend','Virginia/Burley':'Burley blend','Burley Based':'Burley blend','Aromatic':'Aromatic blend','Cavendish Based':'Aromatic blend','Oriental':'Oriental blend'}
T=lambda t:{'Straight Virginia':'straight Virginia','Virginia Based':'Virginia-based','Virginia/Perique':'Virginia and Perique','Virginia/Latakia':'Virginia and Latakia','English':'English','Balkan':'Balkan','Scottish':'Scottish','Virginia/Burley':'Virginia and Burley','Burley Based':'Burley-based','Aromatic':'aromatic','Cavendish Based':'Cavendish-based','Oriental':'Oriental'}[t]
SG='https://www.tobaccoreviews.com/brand/51/samuel-gawith'
PE='https://www.tobaccoreviews.com/brand/45/peterson//'
CD='https://www.tobaccoreviews.com/brand/15/cornell-diehl//'
MB='https://www.tobaccoreviews.com/brand/36/mac-baren//'
rows=[]
def P_(src,mk,cty,text,minr):
    for line in text.strip().split('\n'):
        n,t,r=[x.strip() for x in line.split('|')]
        if t in KM and int(r)>=minr: rows.append((src,mk,cty,n,t,int(r)))
P_(SG,'Samuel Gawith','United Kingdom',"""1792 Flake|Virginia Based|461
B.S. Flake (Brown Sugar Flake)|Virginia Based|41
Balkan Flake|Virginia/Latakia|208
Best Brown Flake|Straight Virginia|302
Black XX Twist (Rope)|Straight Virginia|157
Black Cherry|Aromatic|43
Bothy Flake|Virginia/Latakia|50
Bracken Flake|Virginia/Burley|106
Brown No. 4|Virginia Based|143
Cabbie's Mixture|Virginia/Perique|96
Cannon Plug|Aromatic|49
Celtic Talisman|Aromatic|91
Chocolate Flake|Virginia Based|205
Commonwealth Mixture|Virginia/Latakia|212
English Summer Flake|Straight Virginia|29
Firedance Flake|Aromatic|142
Full Virginia Flake|Straight Virginia|618
Golden Glow|Straight Virginia|110
Grousemoor|Aromatic|239
Kendal Cream Deluxe Flake|Virginia/Burley|171
Kendal Plug|Straight Virginia|53
Lakeland Dark|Virginia/Burley|45
Navy Flake|Virginia/Latakia|169
Perfection|English|144
Sam's Flake|Oriental|92
Scottish Autumn Flake|Straight Virginia|42
Skiff Mixture|Balkan|236
Squadron Leader|English|551
St. James Flake|Virginia/Perique|211
Westmorland Mixture|English|53
Winter Time Flake|Virginia/Latakia|30
Full Virginia Plug|Straight Virginia|28
Scotch Cut Mixture|Scottish|27""",1)
P_(PE,'Peterson','Ireland',"""Peterson Perfect Plug|Virginia/Burley|183
Connoisseur's Choice|Aromatic|179
De Luxe Navy Rolls|Virginia/Perique|219
Early Morning Pipe|English|620
Elizabethan Mixture|Virginia/Perique|293
Flake|Straight Virginia|238
Hyde Park|Virginia/Burley|105
Irish Cask|Aromatic|257
Irish Flake|Burley Based|457
Irish Whiskey|Virginia/Burley|151
Luxury Blend|Aromatic|108
My Mixture 965|English|638
Nightcap|English|692
Old Dublin|English|305
Sherlock Holmes|Virginia Based|266
Standard Mixture|English|215
Sunset Breeze|Aromatic|199
Sweet Killarney|Aromatic|170
The Royal Yacht|Straight Virginia|444
University Flake|Virginia/Burley|444""",1)
P_(MB,'Mac Baren','Denmark',"""7 Seas Regular Blend|Aromatic|118
7 Seas Royal Blend|Aromatic|100
Amphora Full Aroma|Aromatic|227
Amphora Original Blend|Burley Based|125
Black Ambrosia|Aromatic|117
Burley London Blend|Burley Based|158
Capstan Original Navy Cut|Straight Virginia|230
Cube|Aromatic|97
Dark Twist Roll Cake|Virginia Based|220
HH Acadian Perique|Virginia/Perique|107
HH Bold Kentucky|Virginia/Burley|116
HH Mature Virginia|Virginia Based|108
HH Old Dark Fired|Virginia/Burley|253
HH Vintage Syrian|Balkan|233
Mixture: Scottish Blend|Aromatic|413
Navy Flake|Burley Based|344
Original Choice|Aromatic|135
Plumcake|Aromatic|302
Presbyterian Mixture|English|314
St. Bruno Flake|Aromatic|179
Three Nuns|Virginia/Burley|242
Vanilla Cream Flake|Aromatic|135
Vanilla Cream Loose Cut|Aromatic|325
Virginia Flake|Straight Virginia|116
Virginia No. 1|Straight Virginia|285
Golden Blend|Burley Based|99""",1)
P_(CD,'Cornell & Diehl','United States',"""Autumn Evening|Aromatic|335
Bayou Morning|Virginia/Perique|159
Bayou Morning Flake|Virginia/Perique|103
Billy Budd|English|145
Bow-Legged Bear|English|83
Briar Fox|Virginia Based|184
Epiphany|English|151
Exhausted Rooster|Virginia/Burley|103
Haunted Bookshop|Burley Based|301
Kajun Kake|Virginia/Perique|126
Mississippi Mud|English|101
Night Train|Virginia/Burley|90
Crooner|Burley Based|128
Bayou Night|English|98""",1)
have={e['n'].lower() for K in kinds.values() for e in K.get('x',[])}
cnt={}
for src,mk,cty,n,t,r in rows:
    name=n
    if name.lower() in have:
        # same name different maker -> qualify
        name=f"{mk} {n}"
        if name.lower() in have: continue
    have.add(name.lower())
    K=kinds[KM[t]]
    K['x'].append({'n':name,'a':'','d':f"{T(t).capitalize()} pipe blend by {mk}; TobaccoReviews lists it with {r} reviews.",'mk':mk,'y':'','s':src,'cty':cty})
    cnt[K['n']]=cnt.get(K['n'],0)+1
for k in cnt:
    K=kinds[k]
    K['sel']=K['sel'].rstrip()+" Added from TobaccoReviews brand pages for Samuel Gawith (122 blends), Peterson (82), Mac Baren (131) and Cornell & Diehl (386; first 100,000 characters read): blends with enough reviews to be a settled product (about 30 or more for Gawith, 90 or more for the others). Covers the most-reviewed blends of those four makers; Gawith Hoggarth, G.L. Pease, Sutliff, Davidoff, Orlik and Captain Black brand pages were not read."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P); print(cnt,len(rows))
