import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F4/agent')
from w import save
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Crucifix & devotional cross","a":"crucifix · devotional cross","d":"Cross, bare or bearing a figure of Christ, made to stand, hang or be held in veneration.",
 "t":["wall crucifix","standing crucifix","hand or pocket cross","carved wood","cast metal"],"s":"https://thecatholicshop.com/collections",
 "x":[
 {"n":"Latin cross crucifix","a":"crux immissa","d":"Cross with a longer lower arm, the usual Catholic and Lutheran crucifix, often with an INRI plate.","mk":"","y":"","s":W+"Latin_cross","dt":"wood or metal · corpus carved or cast · wall or standing"},
 {"n":"San Damiano cross","a":"","d":"Painted icon-style rood cross before which St Francis prayed at Assisi; copied as a Franciscan devotional cross.","mk":"","y":"c. 1100","s":W+"San_Damiano_Cross","v":[{"n":"Original, Basilica of Saint Clare, Assisi","mk":"","y":"c. 1100","d":"Painter unknown; moved from San Damiano in 1257"},{"n":"Copy at San Damiano church","mk":"","y":"","d":"Hangs in the original position"}],"dt":"painted wood panel · replica sizes"},
 {"n":"Tau cross","a":"St Anthony's cross · crux commissa","d":"T-shaped cross, adopted by St Francis as his sign and used by the Antonines.","mk":"","y":"","s":W+"Tau_cross","dt":"wood, olive wood, metal pendant or wall piece"},
 {"n":"Russian Orthodox cross","a":"three-barred cross · Slavonic cross · suppedaneum cross","d":"Cross with three crossbars, the lowest slanted as a footrest; used on Russian Orthodox crucifixes.","mk":"","y":"16th century","s":W+"Russian_Orthodox_cross","dt":"icon-style crucifix · enamel, brass or wood"},
 {"n":"Celtic cross","a":"ringed cross","d":"Latin cross with a ring around the intersection, from Irish and British high crosses; revived in the 19th century.","mk":"","y":"9th-12th century; revived 19th century","s":W+"Celtic_cross","dt":"pewter, silver, stone or wood"}
 ],
 "m":[]},
{"n":"Icon","a":"devotional panel painting","d":"Sacred picture painted on a rigid panel, framed or mounted to stand or hang, chiefly Orthodox and Eastern Catholic.",
 "t":["hand-painted egg tempera","printed on wood","metal-covered (riza or oklad)","travelling icon"],"s":"https://www.holyart.co.uk/religious-items/sacred-icons/greek-icons/byzantine-icon-of-our-lady-of-vladimir-10x8-in-greece",
 "x":[
 {"n":"Hodegetria","a":"Our Lady of the Way","d":"Virgin holding the Christ Child at her side and pointing to him as the source of salvation.","mk":"","y":"10th century spread","s":W+"Hodegetria","v":[{"n":"Smolensk version","mk":"","y":"11th century","d":"Dated by art historians"},{"n":"Lost Constantinople original","mk":"","y":"","d":"Said to be painted by St Luke; disappeared around 1453"}],"dt":"Greek, Russian or Italo-Byzantine style · gilded ground"},
 {"n":"Eleousa","a":"Tenderness · Umilenie","d":"Virgin and Child cheek to cheek; developed from the Hodegetria.","mk":"","y":"","s":W+"Hodegetria","v":[{"n":"Virgin of Vladimir (Vladimir Mother of God)","mk":"","y":"early 12th century","d":"Tempera on panel, painted probably in Constantinople; reached Rus about 1131; the model for countless copies"}],"dt":"panel sizes · gilded halos"},
 {"n":"Christ Pantocrator","a":"Christ the Almighty","d":"Christ shown blessing and holding a Gospel book; the standard Orthodox icon of Christ.","mk":"","y":"6th-7th century (earliest)","s":W+"Christ_Pantocrator","v":[{"n":"Sinai encaustic icon","mk":"","y":"6th-7th century","d":"Earliest surviving, Saint Catherine's Monastery"}],"dt":"half-length · gold ground"},
 {"n":"Theotokos of Kazan","a":"Our Lady of Kazan","d":"Russian Marian icon, recovered in Kazan in 1579; widely copied for homes and wayside shrines.","mk":"","y":"1579 (found)","s":W+"Our_Lady_of_Kazan","v":[{"n":"Original, stolen in 1904","mk":"","y":"1904","d":"Probably destroyed"},{"n":"Vatican copy","mk":"","y":"16th century","d":"Returned to the Russian Orthodox Church in 2004; kept in Kazan"}],"dt":"often with metal riza"}
 ],
 "m":[]},
{"n":"Devotional statue","a":"santo · saint figure","d":"Sculpted figure of a saint, the Virgin or Christ made to be venerated; Hindu murti and Buddha images are listed elsewhere.",
 "t":["Madonna","Sacred Heart","saint","Infant Jesus","carved wood","resin or plaster","dressed (vested) figure"],"s":"https://thecatholicshop.com/collections",
 "x":[
 {"n":"Santo","a":"bulto · santero image","d":"Wooden statue of a saint in the Spanish Catholic tradition; types include bulto, retablo, dressed bastidor and painted detallado.","mk":"","y":"","s":W+"Santo_(art)","v":[{"n":"Bulto","mk":"","y":"","d":"Carved in the round, usually wood"},{"n":"Bastidor","mk":"","y":"","d":"Dressed figure on a lattice frame"},{"n":"Santo Niño de Cebu","mk":"","y":"1521","d":"Earliest recorded vested santo in the Philippines"}],"dt":"cottonwood, pine, santol or batikulin · gesso paint"},
 {"n":"Val Gardena carved saint","a":"Gherdeina sacred sculpture","d":"Hand-carved wooden saint figure from the Val Gardena workshops that supplied churches worldwide.","mk":"","y":"17th century onward","s":W+"Val_Gardena","dt":"lime or Swiss pine · painted or stained"},
 {"n":"Oberammergau carved figure","a":"","d":"Hand-carved religious figure from the Bavarian town with a long woodcarving tradition and a state woodcarving school.","mk":"","y":"","s":W+"Oberammergau","dt":"carved wood · nativity groups, crucifixes, saints"}
 ],
 "m":[]},
{"n":"Nativity set","a":"crib · creche · presepe · belen","d":"Boxed or composed set of figures and a stable showing the birth of Jesus, sold as one set.",
 "t":["figures only","figures with stable","stable only","table-top","life-size"],"s":"https://www.catholiccompany.com/",
 "x":[
 {"n":"Neapolitan presepe","a":"presepio","d":"Elaborate crib set in 18th-century Naples with townspeople and market scenes around the Holy Family.","mk":"","y":"18th century","s":W+"Neapolitan_nativity_scene","v":[{"n":"Via San Gregorio Armeno workshops","mk":"","y":"","d":"Naples street of crib makers"},{"n":"Certosa di San Martino collection","mk":"","y":"","d":"Museum display of historic scenes"}],"dt":"figures in terracotta, wood and cloth"},
 {"n":"Alpine carved crib","a":"","d":"Hand-carved wooden figures from southern Germany, Austria and Trentino-Alto Adige.","mk":"","y":"","s":W+"Nativity_scene","dt":"wood · painted or natural"},
 {"n":"Provencal santon crib","a":"santons","d":"Hand-painted clay figures from Provence, France.","mk":"","y":"","s":W+"Nativity_scene","dt":"painted clay"},
 {"n":"Polish szopka","a":"","d":"Colourful decorative crib shaped like an ornate building.","mk":"","y":"","s":W+"Nativity_scene","dt":"cardboard, foil, wood"},
 {"n":"Filipino belen","a":"","d":"Diorama-style Philippine crib introduced by the Spanish in the 16th century.","mk":"","y":"16th century","s":W+"Nativity_scene","dt":"home or church display"}
 ],
 "m":[]},
{"n":"Home altarpiece & triptych","a":"altarpiece · portable altar","d":"Domestic altarpieces and folding triptychs for private devotion; museum old-master altarpieces belong to Art as paintings.",
 "t":["folding triptych","diptych","carved retablo","icon triptych","travelling altar"],"s":"https://ngv.vic.gov.au/explore/collection/work/3733",
 "x":[{"n":"Triptych","a":"three-panel folding altarpiece","d":"Three hinged panels that fold shut; used for private devotion since the Byzantine period.","mk":"","y":"Byzantine period onward","s":W+"Triptych","v":[{"n":"Byzantine private triptych","mk":"","y":"","d":"Used alongside icons"},{"n":"WWII troop triptychs","mk":"","y":"WWII","d":"About 460 made by 70 artists for troops"}],"dt":"panel, carved or mixed media"}],
 "m":[]},
{"n":"Reliquary","a":"shrine · chasse · theca","d":"Case or container made to hold and show a relic.",
 "t":["casket or chasse","arm or bust reliquary","cross-shaped","monstrance-type","pendant theca"],"s":"https://www.heck-kirchenbedarf.de/kirchenbedarf",
 "x":[{"n":"Chasse reliquary","a":"house-shaped casket","d":"Box shaped like a small church with a pitched roof, often of enamelled gilt copper.","mk":"","y":"12th-14th century","s":W+"Reliquary","v":[{"n":"Limoges enamel chasse","mk":"","y":"12th-14th century","d":"Limoges was the largest production centre"}],"dt":"wood core · copper-gilt plaques · champleve enamel"},
 {"n":"Monstrance-type reliquary","a":"ostensory reliquary","d":"Relic in a rock-crystal or glass capsule on a column, for display.","mk":"","y":"later Middle Ages","s":W+"Reliquary","dt":"silver · crystal capsule"},
 {"n":"Pendant theca","a":"","d":"Brooch-like or pendant container for a tiny relic.","mk":"","y":"","s":W+"Reliquary","dt":"gold, silver, glass window"}],
 "m":[]},
{"n":"Relic","a":"","d":"Body part or belonging of a holy person, or a thing touched to one, kept for veneration.",
 "t":["first class (body part or object of Christ's life)","second class (item the saint used, ex indumentis)","third class (touched a first or second class relic; abolished 2017)","significant (insigni)","non-significant (non insigni)"],"s":"https://www.proantic.com/en/1739763-silver-reliquary-1st-class-relic-st-praxedes-document-coa.html","m":[]}
]
trads=[
{"n":"Orthodox icon painting","g":"Faith traditions","r":"Byzantine world, Russia, Crete","p":"6th century to present","d":"Egg-tempera painting of sacred figures on prepared wooden panels with gold ground, following fixed types.","tech":"egg tempera on gessoed panel, gold leaf","mat":"wood panel, gesso, egg tempera, gold leaf, metal riza","forms":["Hodegetria","Eleousa","Pantocrator","Theotokos of Kazan"],"ctr":["Constantinople","Crete (Candia, Chania)","Novgorod","Moscow","Palekh, Mstyora, Kholuy"],"auth":"Back slats on old panels, tempera craquelure, riza fittings; Cretan painters often signed works.","s":W+"Russian_icons"},
{"n":"Cretan School icon painting","g":"Faith traditions","r":"Crete under Venetian rule","p":"15th-17th century","d":"Post-Byzantine icon school blending Byzantine tradition with Venetian and Flemish influence; many painters signed work.","tech":"egg tempera on panel","mat":"wood panel, gold ground","forms":["icons for export","Virgin and Child"],"ctr":["Candia (Heraklion)","Chania","Venice"],"auth":"Signed works were unusual in Byzantine practice and mark Cretan painters.","s":W+"Cretan_School"},
{"n":"Val Gardena woodcarving","g":"Woodwork & furniture","r":"Val Gardena, South Tyrol","p":"17th century to present","d":"Valley carving trade exporting statues, altars and toys to Catholic churches from the 19th century.","tech":"hand carving, painting and gilding","mat":"Swiss pine, lime","forms":["devotional statues","altars","wooden toys","nativity figures"],"ctr":["Urtijei (Ortisei)","Museum Gherdeina"],"auth":"Check carved back, workshop marks and hand finishing against machine-carved 1950s output.","s":W+"Val_Gardena"},
{"n":"Neapolitan presepe","g":"Faith traditions","r":"Naples, Italy","p":"18th century to present","d":"Crib tradition set in 18th-century Naples with townsfolk, markets and the Holy Family.","tech":"figures modelled and dressed","mat":"terracotta, wood, cloth","forms":["Neapolitan crib figures","scenic presepe"],"ctr":["Via San Gregorio Armeno","Certosa di San Martino"],"auth":"Museum-pattern figures and workshop provenance on San Gregorio Armeno.","s":W+"Neapolitan_nativity_scene"},
{"n":"Santos (Hispanic saint carving)","g":"Woodwork & furniture","r":"Spain, Mexico, Philippines, Puerto Rico, New Mexico","p":"16th century to present","d":"Carved and painted wooden saints made by santeros for homes and churches.","tech":"knife carving, gesso, painting; vested figures dressed","mat":"cottonwood, pine, aspen, santol, batikulin; ivory historically","forms":["bulto","retablo","bastidor","detallado"],"ctr":["Cordova, New Mexico","Cebu and Manila","Cordillera Central, Puerto Rico"],"auth":"Hand-carved wood with gesso paint; modern resin copies are mass-produced.","s":W+"Santo_(art)"}
]
save('00_00',{"kinds":kinds,"brands":[],"traditions":trads,"notes":"Fontanini not included (no retrieved page for the maker). Palekh/Mstera covered as icon centres under Russian_icons. Hindu murti/Buddha images left to other shelves per brief. Kept old sources for carried-over kinds."})
