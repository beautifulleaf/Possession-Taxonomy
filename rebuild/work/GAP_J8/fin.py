import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
G='Named forms and protected traditions'
IND='https://en.wikipedia.org/wiki/List_of_Indian_sweets_and_desserts'
more=[('Arisa pitha','Fried, jaggery-based','eastern'),('Amriti','Fried, syrup-based','eastern'),('Chandrapuli','Coconut and milk-based','eastern'),('Jaynagarer moa','Fried, rice-based','eastern'),('Kolar bora','Fried, banana-based','eastern'),('Labanga latika','Fried, syrup-based','eastern'),('Lyangcha','Milk-based, fried','eastern'),('Puri khaja','Fried, ghee-based','eastern'),('Sarpuria','Fried, milk-based','eastern'),('Taal-er bora','Fried, fruit-based','eastern'),('Chhena jhili','Fried chhena','eastern'),('Jaangiri','Fried, syrup-based','southern'),('Kozhukkattai','Steamed dumpling','southern'),('Neyyappam','Fried rice cake','southern'),('Palathalikalu','Rice-flour milk','southern'),('Unni appam','Fried rice-banana fritter','southern'),('Dhondas','Baked cake','western'),('Patoleo','Steamed rice-flour parcel','western')]
cov={
'Mithai':"Covers 66 of about 109 rows in Wikipedia's List of Indian sweets and desserts, read to its end; the rest are puddings, drinks, flatbreads, biscuits and variants of listed sweets, out of scope.",
'Wagashi':"Covers 33 of about 39 named types in Wikipedia's Wagashi article, read to its end; the rest are Oshiruko (a soup), Kasutera (held under Castella & sponge cake), Aosashi (no details) and classification groups.",
'Halva':"Covers 27 of about 40 named rows in Wikipedia's Halva article; its variety lists end within the first 100,000 characters and the rest is navigation; the remainder are variants or aliases of held forms.",
'Marzipan':"Covers 20 of about 24 rows in Wikipedia's Marzipan article, read to its end; the rest are aliases or seasonal shapes of held forms.",
'Nougat & turrón':"Covers 15 of about 18 rows in Wikipedia's Nougat article, read to its end; the rest are local-name aliases of Venetian nougat, the French nougat term and fluffy nougat.",
'Baklava & syrup pastries':"Covers 27 of about 55 rows in Wikipedia's Baklava article, read to its end of text; the rest are ancient precursors, regional names and börek-type dishes, out of scope.",
}
NOREF="No complete list exists; follows "
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      n=k['n']
      if n=='Mithai':
        have={e['n'].lower() for e in k['x']}
        for a,c,r in more:
          if a.lower() not in have: k['x'].append({"n":a,"a":"","d":f"{c} sweet of {r} India, listed on Wikipedia's List of Indian sweets and desserts.","mk":"","y":"","s":IND,"v":[],"g":G})
      if n=='Wagashi' and not any(e['n']=='Karakudamono' for e in k['x']):
        k['x'].append({"n":"Karakudamono","a":"","d":"Tang-derived fried confection of the Nara period; listed on Wikipedia's Wagashi article.","mk":"","y":"Nara period","s":"https://en.wikipedia.org/wiki/Wagashi","v":[],"g":G})
      sel=k.get('sel')
      if not sel: continue
      x=len(k['x'])
      if n in cov:
        base=re.split(r' ?This kind holds',sel)[0]
        k['sel']=(base+' '+cov[n]).strip()
      elif n=='Artisan bakery':
        k['sel']=sel.split(' Complete:')[0].rstrip('; ')+" Complete: 219 of 219 in the Loaf Mark licensee list compiled 1 September 2026 (one exact duplicate merged, 218 entries). The Loaf Mark is a licence to use the mark on additive-free loaves, not a certification."
        k['sel']=k['sel'].replace(" Complete: 219 of 219 in the Loaf Mark licensee list compiled 1 September 2026 (one exact duplicate merged, 218 entries). The Loaf Mark is a licence to use the mark on additive-free loaves, not a certification."," The Loaf Mark is a licence to use the mark on additive-free loaves, not a certification. Complete: 219 of 219 in the Loaf Mark licensee list compiled 1 September 2026 (one exact duplicate merged, 218 entries).")
      elif 'no whole-market reference exists' in sel:
        k['sel']=re.sub(r' ?Covers \d+ entries; no whole-market reference exists.*$','',sel)+" No complete list exists; follows the fetched owner-group, champion and market pages named above."
      elif sel.startswith('Brand rows of Wikipedia'):
        base=sel.split(' This kind holds')[0]
        if n=='Countline':
          k['sel']=base+f" Covers {x} of about 365 rows in Wikipedia's List of chocolate bar brands (about 330 rows) and List of bean-to-bar chocolate manufacturers (35 rows); the other chocolate kinds hold the remaining bars, flavour and regional variants are versions, and the rows are shared across this department."
        else:
          k['sel']=base+" No complete list exists; follows the chocolate bar brand and bean-to-bar lists and the group brand pages named above, placed across the department's kinds."
      elif 'List of confectionery brands' in sel and sel.startswith('This kind holds'):
        k['sel']="Brands from the Mars, Mondelēz, Nestlé, Ferrero, Hershey and Haribo group pages, Meiji, Lotte, Morinaga and Glico product pages and the nested rows of Wikipedia's List of confectionery brands. No complete list exists; the Wikipedia list calls itself dynamic and never complete."
      elif 'List of biscuits and cookies' in sel and sel.startswith('This kind holds'):
        k['sel']=sel.split(' Covers ',1)[1][0].upper()+sel.split(' Covers ',1)[1][1:] if False else "Follows "+sel.split(' Covers the ',1)[1].rstrip('.')+". All rows of the List of biscuits and cookies are placed, so that list is complete here; for brands no complete list exists."
      elif 'List of ice cream brands' in sel and sel.startswith('This kind holds'):
        k['sel']="Global and regional brands of The Magnum Ice Cream Company and Froneri and the packaged-ice-cream rows of Wikipedia's List of ice cream brands; parlour and shop chains (Cold Stone, Dairy Queen, Friendly's, Marble Slab, J.P. Licks, Mado and others) and defunct brands are left out as not products. No complete list exists for brands; the Wikipedia list has about 170 packaged rows."
      elif 'named traditional forms from the structure pass' in sel:
        k['sel']=f"Named traditional forms held from the structure pass. No complete list exists; no designation list or reference covers them, so the {x} forms follow the pages cited on each entry."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
