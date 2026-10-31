import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
 {"n":"Lime putty","a":"non-hydraulic lime putty · slaked lime putty · air lime","d":"Non-hydraulic slaked lime stored wet as a paste and matured before use as a binder for mortar, plaster and limewash.",
  "t":["Matured lime putty","Hydrated lime powder"],"s":W+"Lime_(material)"},
 {"n":"Natural hydraulic lime","a":"NHL · hydraulic lime","d":"Bagged lime that sets by hydration as well as carbonation, graded by strength for mortars, renders and plasters.",
  "t":["NHL 2 (feebly hydraulic)","NHL 3.5 (moderately hydraulic)","NHL 5 (eminently hydraulic)"],"s":W+"Hydraulic_lime",
  "m":[["NHL 2 / NHL 3.5 / NHL 5","Saint-Astier"]]},
 {"n":"Lime mortar and render","a":"lime plaster · haired lime plaster · lime render · pre-mixed lime mortar","d":"Mortar, render or plaster of lime and sand, sold pre-mixed or mixed on site, for breathable masonry and plastering.",
  "t":["Pointing and bedding mortar","External render","Haired lime plaster","Polished lime plaster"],"s":W+"Lime_mortar",
  "x":[
   {"n":"Haired lime plaster","a":"horsehair plaster","d":"Coarse lime plaster reinforced with animal hair to control shrinkage, traditionally applied over laths or uneven walls.","mk":"","y":"traditional","s":W+"Lime_mortar","v":[],"dt":"hair or fibre type (horsehair, synthetic polypropylene) · base, float and finish coats"},
   {"n":"Tadelakt","a":"","d":"Waterproof Moroccan lime plaster compressed and polished with stones and sealed with olive-oil or black soap.","mk":"","y":"traditional","s":W+"Tadelakt","v":[],"dt":"pigment (deep red traditional) · uses: baths, sinks, walls, floors"},
   {"n":"Venetian plaster","a":"polished plaster · marmorino","d":"Polished finish of slaked lime with marble dust or chips, usually sealed with wax.","mk":"","y":"traditional Italian","s":W+"Venetian_plaster",
    "v":[{"n":"Marmorino","mk":"","y":"","d":"Venetian plaster technique within the polished plaster range"}],"dt":"finish from high polish to textured · marble content · wax seal"}]},
 {"n":"Limewash","a":"lime wash · lime paint","d":"Breathable paint of slaked lime and water, often pigmented, that cures by carbonation on masonry and lime plaster.",
  "s":W+"Whitewash","m":[["Limewash","Ty-Mawr Lime"]]},
 {"n":"Clay plaster","a":"earthen plaster · earth plaster","d":"Plaster of clay and sand, often with plant fibre, used as a breathable, moisture-regulating finish coat.","s":W+"Clay_plaster"},
 {"n":"Distemper","a":"soft distemper · oil-bound distemper · casein distemper","d":"Traditional paint of chalk and pigment bound with glue; soft types are not washable, hard types add casein or linseed oil.",
  "t":["Soft distemper","Hard distemper (casein or oil-bound)"],"s":W+"Distemper_(paint)"},
 {"n":"Linseed oil paint","a":"linoljefärg · Swedish linseed paint","d":"Solvent-free paint of boiled linseed oil and earth pigments, vapour-permeable, used on wooden buildings, windows and joinery.",
  "s":"https://www.raa.se/in-english/kulturkulor-traditional-swedish-colours/",
  "m":[["Linseed oil paint","Ottosson Färgmakeri"],["Linseed oil paint","Gysinge"],["Linseed oil paint","Engwall & Claesson"]]},
 {"n":"Hempcrete","a":"hemplime · hemp-lime · hemp concrete","d":"Insulating biocomposite of hemp shiv, lime binder and water, cast in frames or bought as prefabricated blocks.",
  "t":["Prefabricated hempcrete block","Cast or sprayed hemp-lime mix"],"s":W+"Hempcrete"},
]
brands=[
 {"n":"Saint-Astier","c":"France","f":"1912","seg":"Natural hydraulic lime","d":"French producer of natural hydraulic lime at Saint-Astier, Dordogne, making NHL since 1912.",
  "lines":["NHL and lime","Venetian plasters","Cement-free coloured mortars","Renders","Stone repair mortars","Hemp solutions"],"eras":[],"sig":[],"sc":["Heritage conservation"],"rel":[],"s":"https://www.buildingconservation.com/directory/saint"},
 {"n":"Ty-Mawr Lime","c":"United Kingdom (Wales)","f":"","seg":"Lime and natural building materials","d":"Brecon maker of limewash and lime products, made in Wales using British lime.",
  "lines":["Limewash"],"eras":[],"sig":[],"sc":["Heritage conservation"],"rel":[],"s":"https://greenspec.co.uk/green-products/external-wall-paints/details/ty-mawr-limewash/"},
 {"n":"Gysinge","c":"Sweden","f":"","seg":"Linseed oil paint and building conservation","d":"Swedish building-conservation brand selling solvent-free linseed oil paint, its linseed oil made in the same factory since 1839.",
  "lines":["Linseed oil paint","Linseed oil","Putty","Gysinge soap"],"eras":[],"sig":[],"sc":["Building conservation"],"rel":["Ottosson Färgmakeri"],"s":"https://www.gysinge.com/en/produkt/linseed-oil-paint-red-ochre-natural"},
 {"n":"Ottosson Färgmakeri","c":"Sweden","f":"","seg":"Linseed oil paint","d":"Swedish maker of linseed oil paints from cold-pressed boiled linseed oil and pigments for indoor and outdoor use.",
  "lines":["Linseed oil paint","Antique Indoor"],"eras":[],"sig":[],"sc":["Building conservation"],"rel":["Gysinge"],"s":"https://ovolin.se/en/pages/linoljefarg"},
]
trads=[
 {"n":"Scandinavian linseed oil paint","g":"Woodwork & furniture","r":"Sweden and Scandinavia","p":"1600s–present (revived after post-war decline)","d":"Painting of wooden buildings with linseed oil and earth pigments, first on trim, by the early 1900s on whole facades.",
  "tech":"Thin coats of boiled linseed oil paint brushed onto timber","mat":"Boiled linseed oil, earth and mineral pigments","forms":["Linseed oil paint"],"ctr":["Swedish National Heritage Board (Kulturkulör colour tool, discontinued)"],"auth":"Solvent-free oil-and-pigment recipe; historic colour schemes","s":"https://www.raa.se/in-english/kulturkulor-traditional-swedish-colours/"},
 {"n":"Tadelakt","g":"Masonry & plaster","r":"Morocco","p":"Traditional; revived with riad restoration","d":"Waterproof polished lime plaster of Moroccan hammams, palace and riad bathrooms and qadad roofs.",
  "tech":"Single thick coat compressed and polished with hard stones, sealed with olive-oil soap","mat":"Lime plaster, marble or limestone sand, black or olive-oil soap, pigment","forms":["Lime mortar and render"],"ctr":[],"auth":"Lime rather than Portland cement; stone-polished surface; periodic soap resealing","s":W+"Tadelakt"},
]
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":"New shelf, no old kinds. All 8 planned kinds kept. Hempcrete kept: sold as prefabricated blocks (Wikipedia), though no page confirmed self-build retail specifically. No clay-plaster brand: Clayworks pages blocked (403/405), so not cited. Ty-Mawr founding year (1995) seen only in a search snippet, left out. Saint-Astier founding uses the 1912 date from the retrieved directory page (other sources give 1837/1851). Engwall & Claesson named only as a linseed paint maker on a retailer page, no register entry. Traditions use group 'Masonry & plaster' for tadelakt."}
p='work/C8/shelves/02_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
