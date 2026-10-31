import json,os
P='rebuild/out/J10.json'
d=json.load(open(P))
kinds={K['n']:K for D in d['depts'] for S in D['s'] for K in S['k']}
T='https://www.tobaccoreviews.com/blend/'
def e(n,d_,mk,s,y='',cty=''):
    return {'n':n,'a':'','d':d_,'mk':mk,'y':y,'s':s,'cty':cty}
O=kinds['Oriental blend']
O['x']=[e('Pure Izmir Turkish Leaf','Pure Oriental (Izmir Turkish) leaf in rough ribbon cut, no flavouring.','Samuel Gawith',T+'5236/samuel-gawith-pure-izmir-turkish-leaf',cty='United Kingdom'),
e('Izmir Turkish','Pure Izmir Oriental in ribbon cut, no flavouring.','Cornell & Diehl',T+'6822/cornell-diehl-izmir-turkish',cty='United States'),
e('Classic Samsun','Oriental and Virginia blend with Samsun leaf as the featured Oriental, coarse cut, no flavouring.','McClelland Tobacco Company',T+'2892/mcclelland-classic-samsun/',cty='United States'),
e('Turkish Export (No. 84)','Sun-cured Turkish Samsun blended with Virginia, fine ribbon in bulk and shag in pouches.','Peter Stokkebye',T+'2078/peter-stokkebye-turkish-export-no84/',cty='Denmark')]
O['nl']='One entry is a pipe-tobacco blend built on Oriental (Turkish) leaf, sold under its own name.'
O['sel']='No complete list exists; follows the TobaccoReviews blend pages for four Oriental blends of different makers. Covers 4 blends; other Oriental blends exist on that site but were not fetched.'
K=kinds['Kizami']
R='https://rebornpipes.com/2012/11/09/kiseru-pipes-a-unique-experience-but-if-you-blink-you-will-miss-it/'
K['x']=[e('Koiki','Japanese-grown kizami tobacco in small 10-gram packs, launched in 1985; name means old style.','Koiki',R,'1985','Japan'),
e('Takarabune','Kizami with a shag-like cut, blended in Belgium and sold in 20-gram packs; name means treasure ship.','Takarabune',R,'','Belgium'),
e('Yamabuki','Pipe tobacco imported from China by Nippon Monopoly; a competitor when Koiki launched.','Yamabuki',R,'','China'),
e('Kikyo','Japanese pipe tobacco of the 1970s, production ended 1979.','Kikyo',R,'','Japan')]
K['nl']='One entry is a kizami (finely shredded Japanese) tobacco brand sold under its own name.'
K['sel']='No complete list exists; follows one hobbyist page (Reborn Pipes, kiseru article and comments). Covers 4 brands that page names; JT or other maker pages were not fetched, so owners are not stated.'
kinds['Dokha']['sel']='No entries: no fetched page names a dokha product with a maker. Searched: Wikipedia Dokha page names only retailers.'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
