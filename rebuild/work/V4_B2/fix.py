import json,os,re
P='rebuild/out/B2.json'
d=json.load(open(P))
new={
'Persian rug':"Complete: 24 of 24 rug-type pages in Category:Persian_rugs_and_carpets (Arak is held as Sultanabad, Sarouk's two pages as one entry; Turkmen rug is held under Central Asian rugs); Kurdish rugs, Lilihan, Mamluk and Pictorial carpet come from other fetched pages, and Mehraban was removed for lack of a fetched page.",
'Caucasian rug':"Complete: 17 of 17 rug-type pages in Category:Azerbaijani_rugs_and_carpets (Aghajly, Chul and Shahsevan are held elsewhere; Ganja rugs is held as Gendje), plus Armenian carpet and Caucasian dragon carpets.",
'Anatolian rug':"Complete: 8 of 8 rug-type pages in Category:Turkish_rugs_and_carpets (Konya, Bergama, Early Anatolian animal carpets, Hereke, Lotto, Milas, Ushak, Yürük), plus Isparta and Mamluk carpets from other fetched pages.",
'Central Asian rug':"Covers 5 of about 6 in Category:Turkic_rugs_and_carpets and the Rugs and carpets category (Turkmen rug, Yomut, Asmalyk, Chul, Uzbek carpet); the Uzbekistani subcategory page list was not fetched.",
'Afghan & Baluch rug':"Complete: 2 of 2 rug-type pages in Category:Afghan_rugs_and_carpets (Afghan rug, War rug), with Chul and Turkmen rug held under Central Asian rugs and the Baluchi rug page added.",
'Indian & Pakistani rug':"Complete: 4 of 4 pile-rug pages in the Indian and Pakistani categories (Amritsar, Kashmiri rug, Mughal carpets, Pakistani rug); flatweave pages are held under Flatweave rug.",
'Moroccan rug':"Covers 7 of an open set; Berber carpet and Margoum had no retrievable article text and are not added.",
'Rya rug':"Covers 3 of an open set.",
'Tibetan rug':"Covers 3 of an open set.",
'Chinese rug':"Covers 4 of an open set.",
'Flatweave rug':"Covers 10 of 11 flatweave pages in the Rugs and carpets, Oriental rugs and Indian rugs categories; Khes had no retrievable text. Zili and Rölakan are kept from the earlier pass.",
'Navajo rug':"Covers 12 of an open set.",'Hooked rug':"Covers 3 of an open set.",'Felt rug':"Covers 2 of an open set."}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n'] in new:
        t=k['sel']; i=min([m.start() for m in re.finditer(r'(Complete|Covers) ',t)] or [len(t)])
        # cut at first coverage sentence
        k['sel']=(t[:i].rstrip()+' '+new[k['n']]).strip()
      if k['n']=='Flatweave rug': k['sel']=k['sel'].replace('Complete: 12 of 12','')
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
