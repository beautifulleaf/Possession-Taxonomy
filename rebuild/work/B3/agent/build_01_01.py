import json, os
CH="https://en.wikipedia.org/wiki/Chandelier"
MU="https://en.wikipedia.org/wiki/Murano_glass"
BO="https://en.wikipedia.org/wiki/Bohemian_glass"
BL="https://www.1stdibs.com/blogs/the-study/?p=346629"
X=[
 {"n":"Maria Theresa chandelier","a":"Maria-Theresa · Marie-Thérèse","d":"Bohemian style with no central baluster: curved flat metal arms between moulded glass sections joined by glass rosettes.","mk":"","y":"18th century","s":CH,"v":[],"dt":"arm count · tiers · clear or coloured glass · drops and festoons"},
 {"n":"Murano chandelier","a":"Venetian chandelier · ciocca · Ca' Rezzonico style","d":"Venetian glass chandelier of hand-shaped flowers and leaves on glass arms; the ornate bouquet type is the ciocca.","mk":"","y":"18th century (Giuseppe Briati)","s":MU,
  "v":[{"n":"Briati chandelier, Ca' Rezzonico","mk":"","y":"mid-18th century","d":"ornate ciocca chandelier by Giuseppe Briati, Venice"},
       {"n":"Taif","mk":"Barovier & Toso","y":"","d":"modern Murano chandelier"},
       {"n":"Mood Taif","mk":"Barovier & Toso","y":"","d":"variant of Taif"},
       {"n":"Cascade","mk":"Mazzega","y":"","d":"modern Murano chandelier"}],
  "dt":"arm count · clear, coloured or gilt glass · flowers, leaves, pendants · hollow arms for wiring (late 19th c. on)"},
 {"n":"Bohemian crystal chandelier","a":"Czech crystal chandelier","d":"Cut lead or potash crystal chandelier from Bohemia, hung with cut drops and prisms.","mk":"","y":"18th century onward","s":BO,
  "v":[{"n":"First electric chandeliers (Redoutensäle, Vienna)","mk":"J. & L. Lobmeyr","y":"1880s","d":"developed with Thomas Edison"},
       {"n":"Kamenický Šenov chandeliers","mk":"Preciosa","y":"1724 tradition","d":"chandelier making begun by Josef Palme, continued by Preciosa Lighting"}],
  "dt":"lights · tiers · cut drops, prisms, festoons · brass or gilt frame"},
 {"n":"Zénith","a":"Baccarat Zenith","d":"Baccarat's all-crystal chandelier with a cut-crystal central column, prisms, pendants and one red octagonal crystal.","mk":"Baccarat","y":"c. 1850","s":"https://www.baccarat.com/en_us/creations/iconic-collections/zenith",
  "v":[{"n":"Zénith Black (Darkside)","mk":"Baccarat","y":"2005","d":"black crystal version, Philippe Starck"},
       {"n":"Zénith Short 24L","mk":"Baccarat","y":"","d":"current clear version"},
       {"n":"Zénith Nomade","mk":"Baccarat","y":"","d":"6- and 8-light version"},
       {"n":"Nervous Zénith 37L","mk":"Baccarat","y":"","d":"limited edition"},
       {"n":"Étrange Zénith Deers 15L","mk":"Baccarat","y":"","d":"limited edition"}],
  "dt":"6–48 lights · clear, black, coloured crystal"},
 {"n":"Dutch brass chandelier","a":"Flemish brass chandelier","d":"Brass chandelier with a bulbous baluster and arms curving down around a large low-hung ball, often topped by an eagle.","mk":"","y":"15th–17th century","s":CH,"v":[],"dt":"arm count · tiers · finial (double-headed eagle) · polished or patinated brass"},
 {"n":"Tent-and-bag chandelier","a":"Regency chandelier · waterfall · wedding cake","d":"English Regency form with a tent of drop strings above and a bag of icicle drops below.","mk":"","y":"after 1811","s":CH,"v":[],"dt":"drop count (to over 1,000) · gilt or brass frame · candle or electric"},
 {"n":"Genoese beaded chandelier","a":"Genoa chandelier","d":"Chandelier dressed in strings of small glass beads, made in Genoa.","mk":"","y":"","s":CH,"v":[],"dt":"bead colour · arm count"},
 {"n":"Birdcage chandelier","a":"cage chandelier","d":"Chandelier whose central stem is replaced by a metal cage, leaving the centre clear.","mk":"","y":"18th century (France)","s":CH,"v":[],"dt":"cage shape · drops · gilt bronze or iron"},
 {"n":"Wheel chandelier","a":"corona · crown chandelier · couronne de lumière","d":"Circular crown-shaped hoop of lights, first iron coronas, later large Romanesque wheels in churches.","mk":"","y":"9th–12th century","s":CH,
  "v":[{"n":"Barbarossa Chandelier","mk":"","y":"12th century","d":"Aachen Cathedral"},{"n":"Hezilo and Azelin chandeliers","mk":"","y":"11th century","d":"Hildesheim Cathedral"}],"dt":"diameter · iron, brass or gilt copper · candle count"},
 {"n":"Polycandelon","a":"polykandelon · polycandela","d":"Flat circular Byzantine frame of oil lamps hung on chains, used in churches, synagogues and homes (faith form; see F4).","mk":"","y":"late antiquity–Byzantine","s":CH,"v":[],"dt":"bronze or iron · number of lamp holes"},
 {"n":"Panikadilo","a":"Orthodox church chandelier","d":"Gothic candelabrum-style chandelier hung from the dome of a Greek Orthodox church (faith form; see F4).","mk":"","y":"","s":CH,"v":[],"dt":"tiers · brass or bronze · candles or bulbs"},
 {"n":"Lusterweibchen","a":"Leuchterweibchen · antler chandelier","d":"German chandelier of deer or reindeer antlers carrying a carved wooden figure.","mk":"","y":"late 14th century","s":"https://en.wikipedia.org/wiki/Lusterweibchen",
  "v":[{"n":"Dragon chandelier","mk":"","y":"16th century","d":"Veit Stoss after a drawing by Albrecht Dürer, Germanisches Nationalmuseum"}],"dt":"antler type · figure (woman, mermaid, Diana, arms) · painted or plain wood"},
 {"n":"Sputnik chandelier","a":"Fireworks · starburst chandelier","d":"Mid-century chandelier of many arms radiating from a central sphere, each ending in a bare bulb.","mk":"Arteluce","y":"1939 sketch; produced early 1950s","s":BL,
  "v":[{"n":"Model 2003 'Fireworks'","mk":"Arteluce","y":"early 1950s","d":"Gino Sarfatti original"},{"n":"Sputnik","mk":"Giovanni Dalla Fina","y":"","d":"contemporary version"}],"dt":"arm count · brass, chrome or black · bulb or shade"},
 {"n":"Metropolitan Opera chandelier","a":"Met chandelier · Lobmeyr starburst","d":"Starburst crystal chandelier designed for the Metropolitan Opera House, New York.","mk":"J. & L. Lobmeyr","y":"1966","s":BL,
  "v":[{"n":"Met Opera House chandeliers","mk":"J. & L. Lobmeyr","y":"1966","d":"Hans Harald Rath after a sketch by Tadeusz Leski; Swarovski crystals"}],"dt":"diameter · crystal spheres · gilt rods"},
 {"n":"Poliedri","a":"Poliedro","d":"Chandelier of many identical faceted Murano glass elements hung on a painted metal frame.","mk":"Venini","y":"1958","s":"https://www.incollect.com/node/612421",
  "v":[{"n":"Poliedri, Carlo Scarpa design","mk":"Venini","y":"1958","d":"Poliedro patented by Scarpa; clear, taupe, blue glass"}],"dt":"height · element count · glass colour"},
 {"n":"Heracleum","a":"","d":"LED chandelier of slim metal stems carrying polycarbonate lens 'leaves', modelled on the Heracleum plant.","mk":"Moooi","y":"2011","s":"https://www.designboom.com/design/bertjan-pot-heracleum-for-moooi/",
  "v":[{"n":"Heracleum (original)","mk":"Moooi","y":"2011","d":"Bertjan Pot; 63 LEDs; nickel or copper"},{"n":"Heracleum III","mk":"Moooi","y":"","d":"later version"}],"dt":"round or linear · nickel, copper finishes"},
]
kind={"n":"Chandelier","a":"lustre · gasolier · electrolier","d":"Branched or tiered hanging fitting that carries several light sources, lit by electricity, gas, oil or candles.",
 "t":["crystal","glass","brass","wrought iron","beaded","antler","LED"],
 "s":"https://www.lights.co.uk/c/indoor-lighting/chandeliers","x":X,
 "m":[["Diamante","Venini"],["Hermitage","Groenensteyn"],["Tere chandelier","Design VA"],["Palace","Maytoni"],["Zaragoza","Maytoni"],["Bella","Maytoni"],["Marnia","Lindby"],["Eugenia","Lucande"]]}
B=[
 {"n":"Baccarat","c":"France","f":"1764","seg":"Luxury crystal","d":"French crystal house in Baccarat, Lorraine, making chandeliers since 1824.","lines":["Zénith"],"eras":["Philippe Starck Darkside collection, 2005"],"sig":["Zénith"],"sc":[],"rel":["J. & L. Lobmeyr"],"s":"https://en.wikipedia.org/wiki/Baccarat_(company)"},
 {"n":"J. & L. Lobmeyr","c":"Austria","f":"1823","seg":"Luxury crystal","d":"Family-owned Viennese glass and chandelier maker; co-developed the first electric chandeliers with Edison.","lines":[],"eras":["Josef Lobmeyr, from 1823","Stefan Rath, from 1917"],"sig":["Metropolitan Opera chandelier","Bohemian crystal chandelier"],"sc":[],"rel":["Baccarat"],"s":"https://en.wikipedia.org/wiki/J._%26_L._Lobmeyr"},
 {"n":"Barovier & Toso","c":"Italy","f":"","seg":"Murano glass lighting","d":"Murano glassworks of the Barovier family (recorded from 1324), named Barovier&Toso since 1942.","lines":["Taif"],"eras":["Ercole Barovier, design lead from 1927","Luca Nichetto, artistic director from 2025"],"sig":["Murano chandelier"],"sc":[],"rel":["Venini","Seguso"],"s":"https://en.wikipedia.org/wiki/Barovier_%26_Toso"},
 {"n":"Venini","c":"Italy","f":"1921","seg":"Murano art glass","d":"Murano glassworks founded by Paolo Venini and Giacomo Cappellin; owned by Damiani since 2016.","lines":[],"eras":["Napoleone Martinuzzi, creative direction","Carlo Scarpa, designer"],"sig":["Poliedri"],"sc":[],"rel":["Barovier & Toso","Seguso"],"s":"https://en.wikipedia.org/wiki/Paolo_Venini"},
 {"n":"Seguso","c":"Italy","f":"1933","seg":"Murano art glass","d":"Murano furnace founded as Seguso Vetri d'Arte; sold in 1974 and bought back by the family in 2007.","lines":["Seguso Viro"],"eras":[],"sig":["Murano chandelier"],"sc":[],"rel":["Venini","Barovier & Toso"],"s":"https://www.incollect.com/artists/seguso-murano-glass"},
 {"n":"Preciosa","c":"Czech Republic","f":"","seg":"Bohemian crystal lighting","d":"Czech crystal company whose Preciosa Lighting continues chandelier making in Kamenický Šenov.","lines":["Preciosa Lighting"],"eras":[],"sig":["Bohemian crystal chandelier"],"sc":[],"rel":["J. & L. Lobmeyr"],"s":"https://crystalvalley.cz/en/blog/svetlo-na-kolejich"},
 {"n":"Arteluce","c":"Italy","f":"1939","seg":"Design lighting","d":"Lighting company founded by Gino Sarfatti; maker of the original Sputnik-type model 2003.","lines":[],"eras":["Gino Sarfatti, 1939 onward"],"sig":["Sputnik chandelier"],"sc":[],"rel":[],"s":BL},
 {"n":"Moooi","c":"Netherlands","f":"","seg":"Design lighting and furniture","d":"Dutch design brand producing Bertjan Pot's Heracleum.","lines":["Heracleum"],"eras":[],"sig":["Heracleum"],"sc":[],"rel":[],"s":"https://www.designboom.com/design/bertjan-pot-heracleum-for-moooi/"},
]
T=[
 {"n":"Murano glass","g":"Ceramics & glass","r":"Murano, Venetian lagoon, Italy","p":"glassmaking confined to Murano from 1291; peak 15th–16th c.; revivals after 1866 and in the 1920s","d":"Venetian hot-worked soda glass, including chandeliers of hand-shaped flowers and leaves.","tech":"hot-working, filigrana, murrine, sommerso, gilding and enamel","mat":"soda-lime glass, cristallo, lattimo, aventurine","forms":["Murano chandelier","Poliedri","mirrors","beads"],"ctr":["Barovier & Toso","Venini","Seguso","Salviati","Giuseppe Briati"],"auth":"'Artistic Glass Murano' trademark (1994) certifies Murano manufacture; Asian and Eastern European imitations are common.","s":MU},
 {"n":"Bohemian crystal","g":"Ceramics & glass","r":"Bohemia and Silesia, Czech Republic","p":"from c. 1250; high Baroque fame 1685–1750; chandelier industry from 1724","d":"Clear potash and lead crystal, cut and engraved, including the Maria Theresa and crystal chandelier.","tech":"hand-cutting, wheel engraving, blowing, enamel painting","mat":"potash-chalk glass, lead crystal","forms":["Maria Theresa chandelier","Bohemian crystal chandelier","vases","beads"],"ctr":["Kamenický Šenov","Nový Bor","Jablonec nad Nisou","Moser","Preciosa"],"auth":"EU 'lead crystal' needs at least 24% lead oxide; lower-lead pieces are 'crystal glass'.","s":BO},
]
notes=("Dropped from old m: PH Academy Lamp and range 'PH lamps' (Louis Poulsen pendants; belong on the Pendants shelf, ranges once); "
 "retail house-brand SKUs Lindby Elanova/Finnick/Lumiel, Lucande Solveig (lights.co.uk skew, trimmed to a few market examples). "
 "Old maker-free style names became archetypes; Sputnik (Giovanni Dalla Fina), Taif/Mood Taif and Cascade, Poliedri, Heracleum III became versions. "
 "Polycandelon and Panikadilo are faith forms to cross-link with F4. Chandelier crystals stay in Shades & parts. "
 "No dedicated pages fetched for Genoese, Dutch brass, tent-and-bag, birdcage, Maria Theresa, polycandelon, panikadilo: all sourced to the Wikipedia Chandelier article. "
 "Not added: Venini Diamante details, Baccarat Zénith designer variants beyond the fetched Baccarat page (Hayon, Flou, Charleston unconfirmed), founding years for Barovier & Toso, Preciosa and Moooi (sources differ or not retrieved).")
out={"kinds":[kind],"brands":B,"traditions":T,"notes":notes}
p="work/B3/shelves/01_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
