import json, os
W='https://en.wikipedia.org/wiki/'
OLD='https://www.wayfair.com/decor-pillows/sb1/blue-vases-urns-jars-bottles-c215459-a4188~11233.html'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Vase","a":"flower vase · bud vase","d":"Open vessel made to hold cut or artificial flowers or to stand as an ornament.",
 "t":["table vase","floor vase","bud vase","wall vase (flat-backed, hangs on a wall)","tulip vase","glass","crystal","ceramic","porcelain","metal"],
 "s":OLD,"x":[
 X("Aalto vase","Free-form wavy-walled glass vase designed by Alvar and Aino Aalto for a Karhula-Iittala competition.","Iittala","1936",W+"Savoy_Vase",
   [("Original, wood-mould blown","Karhula-Iittala","1936","140 mm; shown at the 1937 Paris World's Fair"),("Current production","Iittala","","smaller sizes pressed, larger seamless")],
   "height from 140 mm · wide range of colours · clear and coloured glass","Savoy vase"),
 X("Fazzoletto","Handkerchief vase whose rim falls in soft folds like a dropped cloth.","Venini","c. 1948",W+"Paolo_Venini",
   [("Original, Paolo Venini and Fulvio Bianconi","Venini","c. 1948",""),("Fazzoletto","Michielotto","","Murano interpretation")],
   "size · single colour, cased or filigree glass","handkerchief vase"),
 X("Bacchantes","Conical vase with a frieze of nude maenads in high relief.","Lalique","1927","https://collections.vam.ac.uk/item/O6692/",
   [("Model 997","Lalique","1928","listed in the Lalique catalogue"),("Amber press-moulded","Lalique","c. 1970","26 cm, iron-oxide yellow")],
   "press-moulded glass · clear, frosted, opalescent, amber"),
 X("Graal vase","Multi-layered cameo glass cut through and cased in clear crystal, then blown to final shape.","Orrefors","1916","https://theglassmuseum.com/orrefors.htm",
   [("First Graal glass, Simon Gate with Knut Bergkvist","Orrefors","1916","")],"layer colours · motif · designer"),
 X("Ariel vase","Overlay glass whose decoration is air trapped in a sandblasted pattern between layers.","Orrefors","1937","https://snl.no/arielglass",
   [("First Ariel, Edvin Öhrström with Gustaf Bergkvist","Orrefors","1937","shown at the 1937 Paris exhibition; 375 pieces made 1937–46")],"motif · colours · designer"),
 X("Moser coloured crystal vase","Hand-cut or engraved Bohemian crystal vase in Moser's named colour glasses.","Moser","1857 onwards","https://en.wikipedia.org/wiki/Moser_(glass_company)",
   [("Heliolite, Alexandrite, Prasemite colour-change glasses","Moser","c. 1929",""),("Royalit","Moser","1930","purple-red"),("Eldor","Moser","1932","golden-yellow"),("Pear vase, Lukáš Jabůrek","Moser","2012","")],
   "colour glass · cutting or engraving · size"),
 X("Delft tulip vase","Tin-glazed earthenware vase or tiered pyramid with a spout for each flower.","","17th century","https://royaldelft.com/en/tulip-pyramid-and-tulip-vase/",
   [("Hand-painted and transfer-printed vases and pyramids","Royal Delft","","13 cm vases to 120 cm pyramids")],"tiers · blue, white, black, multicolour · hand-painted or printed","tulipière · flower pyramid"),
 X("Snowball vase","Porcelain vase encrusted with hundreds of individually modelled, applied snowball blossoms.","Meissen","1739","https://www.lempertz.com/nl/catalogi/lot/1056-2/986-a-rare-early-meissen-porcelain-snowball-vase.html",
   [("Kaendler's first snowball-flower vessel","Meissen","1739","a teapot"),("Neues Palais order for Frederick II","Meissen","1762","")],"applied birds · painted or white blossoms · crossed swords mark","Schneeballen vase"),
 X("Meiping","Chinese plum vase: narrow base, wide rounded shoulder, short narrow neck and small mouth.","","Tang dynasty (618–907)",W+"Meiping",
   [("Truncated form","","Song","Cizhou ware"),("Blue-and-white","","15th century","Jingdezhen porcelain")],"ware · glaze · with or without lid","plum vase"),
 X("Portland vase","Copy of the Roman cameo-glass amphora with white figures on a dark ground.","Wedgwood","1790",W+"Portland_Vase",
   [("First edition jasperware copy","Wedgwood","c. 1790","black and white jasperware"),("Glass copy, engraved by John Northwood","","19th century","now at the Corning Museum of Glass")],"jasperware or cameo glass · colour"),
 X("Iznik-style vessel","Fritware vase, jug or bottle painted under the glaze with Ottoman floral designs.","","late 15th–17th century",W+"Iznik_pottery",
   [("Abraham of Kütahya blue-and-white","","c. 1490–1525",""),("Golden Horn spiral","","c. 1530–1550",""),("Damascus","","c. 1540–1555","sage green and pale purple"),("Rhodian polychrome with bole red","","from c. 1555","")],"form · palette · tulip, carnation, saz-leaf motifs"),
 X("Bohemian cut-glass vase","Clear or cased coloured glass vase decorated by wheel cutting or engraving.","","Baroque period onwards",W+"Bohemian_glass",[],"clear, ruby or cased colour · cutting pattern · engraving"),
 ]},
{"n":"Ginger jar","a":"","d":"Rounded lidded jar made for display.","t":["blue-and-white porcelain","coloured glaze","with or without lid"],"s":OLD,"x":[
 X("Blue-and-white prunus ginger jar","Chinese porcelain jar painted in underglaze cobalt with plum blossom on a cracked-ice ground.","","Kangxi period (1662–1722)","https://www.graysantiques.com/product/chinese-blue-and-white-ginger-jar-kangxi-1662-1722-2",
   [],"size · panels of scholar's objects · lid")]},
{"n":"Apothecary jar","a":"","d":"Straight-sided jar with a lid, often footed, made to stand on display (a jar made to store food is in Kitchen & Dining).","t":["glass","footed","ceramic"],"s":OLD,"x":[
 X("Albarello","Cylindrical, handleless maiolica drug jar with a slightly waisted body.","","15th century (Italy)",W+"Albarello",
   [("Spanish lustreware","","","Manises, Paterna"),("Italian maiolica","","from 15th century","Florence, Venice, Palermo; a trofei, a foglie, a frutti decoration")],"tin-glazed earthenware · about 18–20 cm · decoration","maiolica drug jar")]},
{"n":"Decorative bottle","a":"","d":"Bottle made to be displayed, not to hold a drink.","t":["glass","ceramic","with stopper"],"s":OLD,"x":[
 X("Snuff bottle","Small Chinese bottle with stopper and spoon, now collected for its material and painting.","","late 17th century",W+"Snuff_bottle",
   [("Imperial glassworks bottles","","from 1696","Beijing"),("Inside-painted","","late 19th century","painted through the neck")],"glass, porcelain, jade, quartz, amber, cloisonné"),
 X("Venini stoppered bottle","Murano glass bottle with stopper made as an ornament.","Venini","c. 1949",W+"Paolo_Venini",
   [("Gio Ponti bottle with stopper","Venini","c. 1949",""),("Tapio Wirkkala bottles","Venini","1966","")],"height · colour bands")]},
{"n":"Decorative urn","a":"","d":"Large footed vessel made as an ornament, indoors or in the garden (a cremation urn is in Religious & Ceremonial Objects).","t":["stone","cast stone","metal","ceramic"],"s":OLD,"x":[
 X("Medici vase","Bell-shaped krater with gadrooned lip and relief frieze, copied as a garden urn.","","1st century AD",W+"Medici_Vase",
   [("Coade stone","","from 1771",""),("Bronze and porcelain imitations","Wedgwood","","")],"scale · marble, Coade stone, bronze, porcelain"),
 X("Borghese vase","Marble krater with a Bacchic frieze, often paired with the Medici vase.","","1st century BC",W+"Borghese_Vase",
   [("Coade stone reduced copy","","1770–1771","Stourhead"),("Jasperware","Wedgwood","","")],"scale · marble, alabaster, bronze, Coade stone")]},
{"n":"Decorative bowl","a":"","d":"Bowl made to be looked at or to hold small decorative items (a bowl made to hold food is in Kitchen & Dining).","t":["art glass","ceramic","wood","metal","footed"],"s":"https://www.johnlewis.com/home-garden/decorative-accessories/c60000247"},
{"n":"Glass paperweight","a":"","d":"Heavy glass dome enclosing decoration such as millefiori canes or lampwork flowers.","t":["faceted","overlay","signed and dated cane"],"s":W+"Paperweight","x":[
 X("Millefiori paperweight","Weight enclosing slices of coloured canes that look like tiny flowers.","","1845–1860 (classic period)",W+"Paperweight",
   [("Classic French","Baccarat","1845–1860","some signed B with a date cane, 1846–49"),("Classic French","Saint-Louis","1845–1860",""),("Classic French","Clichy","1845–1860",""),("Close-pack and spaced millefiori","Perthshire Paperweights","from 1968",""),("Studio weights","Caithness Glass","from 1961","")],
   "scattered, patterned, concentric, carpet ground · base cuts"),
 X("Crown paperweight","Hollow weight of twisted coloured and white ribbons radiating from a central floret.","Saint-Louis","classic period",W+"Paperweight",
   [("Crown","Perthshire Paperweights","from 1968","")],"ribbon colours · central cane"),
 X("Lampwork paperweight","Weight enclosing flowers, fruit, animals or butterflies shaped at the torch.","","classic period",W+"Paperweight",
   [("Lampwork","Perthshire Paperweights","from 1968","")],"subject · ground (clear, latticinio)"),
 X("Sulphide paperweight","Weight encasing a ceramic cameo portrait, often commemorative.","","19th century",W+"Paperweight",[],"subject · faceting")]},
]
brands=[
 {"n":"Venini","c":"Italy","f":"1921","seg":"Murano art glass","d":"Murano glassworks founded by Paolo Venini and Giacomo Cappellin.","lines":[],"eras":["Napoleone Martinuzzi, creative direction 1920s","Fulvio Bianconi, c. 1948"],"sig":["Fazzoletto","Venini stoppered bottle"],"sc":[],"rel":[],"s":W+"Paolo_Venini"},
 {"n":"Iittala","c":"Finland","f":"1881","seg":"Design glass and tableware","d":"Finnish glassworks, part of Fiskars since 2007.","lines":["Kastehelmi","Ultima Thule","Birds by Toikka"],"eras":[],"sig":["Aalto vase"],"sc":[],"rel":["Fiskars"],"s":W+"Iittala"},
 {"n":"Lalique","c":"France","f":"1888","seg":"Luxury art glass","d":"Glass house founded by René Lalique; crystal made at Wingen-sur-Moder since 1921.","lines":["vases","perfumes","jewellery"],"eras":["René Lalique, 1888–1945"],"sig":["Bacchantes"],"sc":[],"rel":[],"s":W+"Lalique"},
 {"n":"Orrefors","c":"Sweden","f":"","seg":"Swedish art glass","d":"Småland glassworks known for the Graal and Ariel techniques; part of Orrefors Kosta Boda.","lines":[],"eras":["Simon Gate from 1916","Edward Hald from 1917","Edvin Öhrström from 1936"],"sig":["Graal vase","Ariel vase"],"sc":[],"rel":["Kosta Boda"],"s":"https://theglassmuseum.com/orrefors.htm"},
 {"n":"Kosta Boda","c":"Sweden","f":"1742","seg":"Swedish art glass","d":"Glassworks at Kosta, Småland; owned by Orrefors from 1990 and New Wave Group since 2005.","lines":[],"eras":["Elis Bergh, 1928–1950","Vicke Lindstrand, 1950–1973"],"sig":[],"sc":[],"rel":["Orrefors"],"s":W+"Kosta_Boda"},
 {"n":"Moser","c":"Czech Republic","f":"1857","seg":"Luxury Bohemian crystal","d":"Karlovy Vary crystal maker known for engraved and colour-glass pieces.","lines":[],"eras":["Ludwig Moser, founder"],"sig":["Moser coloured crystal vase"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Moser_(glass_company)"},
 {"n":"Royal Delft","c":"Netherlands","f":"1653","seg":"Delftware","d":"Koninklijke Porceleyne Fles, the Delft pottery still making hand-painted Delft Blue.","lines":[],"eras":[],"sig":["Delft tulip vase"],"sc":[],"rel":[],"s":W+"Royal_Delft"},
 {"n":"Meissen","c":"Germany","f":"1710","seg":"Luxury porcelain","d":"First European hard-paste porcelain factory, marked with crossed swords since 1720.","lines":["Blue Onion"],"eras":["Johann Joachim Kaendler, chief modeller 1733–1775"],"sig":["Snowball vase"],"sc":[],"rel":[],"s":W+"Meissen_porcelain"},
 {"n":"Baccarat","c":"France","f":"1764","seg":"Luxury crystal","d":"Lorraine crystal maker; classic-period millefiori paperweights.","lines":["Harcourt"],"eras":[],"sig":["Millefiori paperweight"],"sc":[],"rel":[],"s":W+"Baccarat_(company)"},
 {"n":"Saint-Louis","c":"France","f":"1586","seg":"Luxury crystal","d":"Lorraine crystal works, owned by Hermès; classic-period paperweights.","lines":[],"eras":[],"sig":["Crown paperweight"],"sc":[],"rel":["Hermès"],"s":"knowledge"},
 {"n":"Caithness Glass","c":"United Kingdom","f":"1961","seg":"Paperweights","d":"Scottish glassworks founded in Wick, specialising in paperweights; owned by Dartington since 2006.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Perthshire Paperweights"],"s":W+"Caithness_Glass"},
 {"n":"Perthshire Paperweights","c":"United Kingdom","f":"1968","seg":"Paperweights","d":"Crieff paperweight works founded by Stuart Drysdale.","lines":[],"eras":[],"sig":["Crown paperweight"],"sc":[],"rel":["Caithness Glass"],"s":"https://scottishantiques.com/paperweights/Perthshire-Paperweights"},
 {"n":"Wedgwood","c":"United Kingdom","f":"1759","seg":"Ceramics","d":"Staffordshire pottery known for jasperware.","lines":["Jasperware"],"eras":[],"sig":["Portland vase"],"sc":[],"rel":[],"s":"knowledge"},
]
T=lambda **k:k
traditions=[
 T(n="Murano glass",g="Ceramics & glass",r="Murano, Venice, Italy",p="from 1291 on Murano; revival 1920s",d="Venetian hot-worked glass, concentrated on Murano since 1291.",tech="hot-working; millefiori, murrine, sommerso, filigrana, calcedonio",mat="soda-lime glass",forms=["Vase","Decorative bottle","Glass paperweight"],ctr=["Venini","Barovier & Toso","Seguso","Salviati"],auth="Artistic Glass Murano trademark (1994); Asian and Eastern European imitations are common",s=W+"Murano_glass"),
 T(n="Bohemian glass",g="Ceramics & glass",r="Bohemia and Silesia, Czech Republic",p="Renaissance onwards; high point 1685–1750",d="Cut, engraved and coloured glass from the Czech lands.",tech="wheel cutting and engraving, cased and coloured glass",mat="potash-lime glass, lead crystal",forms=["Vase","Glass paperweight"],ctr=["Karlovy Vary","Nový Bor","Kamenický Šenov","Moser"],auth="maker marks; early Bohemian crystal contained no lead",s=W+"Bohemian_glass"),
 T(n="French art glass (Lalique)",g="Ceramics & glass",r="France",p="1920s onwards",d="Moulded and frosted art glass in the manner of René Lalique.",tech="press-moulding, frosting, opalescent glass",mat="glass, crystal",forms=["Vase"],ctr=["Lalique, Wingen-sur-Moder"],auth="'R. LALIQUE FRANCE' mark and model number",s="https://collections.vam.ac.uk/item/O6692/"),
 T(n="Swedish art glass",g="Ceramics & glass",r="Småland, Sweden ('Kingdom of Crystal')",p="1910s onwards",d="Art glass from the Småland glassworks, with Orrefors and Kosta as leading houses.",tech="Graal, Ariel, Ravenna and Kraka techniques; engraving",mat="crystal",forms=["Vase"],ctr=["Orrefors","Kosta Boda","Simon Gate","Edward Hald","Edvin Öhrström","Vicke Lindstrand"],auth="engraved signature with technique and number",s="https://theglassmuseum.com/orrefors.htm"),
 T(n="Delftware",g="Ceramics & glass",r="Delft and other Dutch towns",p="from c. 1600; peak 1640–1740",d="Dutch tin-glazed earthenware painted in cobalt blue.",tech="tin glaze over earthenware, painted in metal oxides",mat="blended clays, tin glaze, cobalt",forms=["Vase","Ginger jar"],ctr=["Royal Delft","Royal Tichelaar Makkum","De Grieksche A"],auth="factory marks and monograms from c. 1640; 'Delfts Blauw' mark on Royal Delft",s=W+"Delftware"),
 T(n="Iznik pottery",g="Ceramics & glass",r="İznik, Anatolia",p="late 15th century–1678",d="Ottoman fritware painted under the glaze in cobalt, turquoise and bole red.",tech="underglaze painting on fritware with white slip",mat="quartz frit, cobalt, copper, bole",forms=["Vase","Decorative bottle"],ctr=["İznik","Kütahya"],auth="style sequence: Abraham of Kütahya, Golden Horn, Damascus, Rhodian",s=W+"Iznik_pottery"),
 T(n="Meissen porcelain",g="Ceramics & glass",r="Meissen, Saxony",p="1710 onwards",d="The first European hard-paste porcelain.",tech="hard-paste porcelain, overglaze enamels, underglaze blue",mat="kaolin",forms=["Vase"],ctr=["Meissen","Johann Joachim Kaendler"],auth="crossed swords mark (from 1720), variants help date pieces",s=W+"Meissen_porcelain"),
]
notes=("Lenox French Perle models and range dropped (retail SKUs, not archetypes). Wall vase merged into Vase as a type. "
 "Decorative bowl kept without archetypes (none sourced). Clichy rose and Caithness named designs not added (museum pages blocked); "
 "Orrefors founding year left blank (sources disagree: 1889 vs 1898). Saint-Louis and Wedgwood brand facts from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":traditions,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B4/shelves/00_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
