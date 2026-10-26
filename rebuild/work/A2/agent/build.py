import json, os
P='work/A2/shelves/03_00.json'
LB='https://theluxurycloset.com/blog/2021/03/26/christian-louboutin-pigalle-pumps/'
PEP='https://www.pep.ph/lifestyle/fashion/36049/10-things-to-know-about-the-iconic-louboutin-heels-src-tcph'
TI='https://www.theindustry.fashion/?p=157785'
kinds=[
{"n":"Court shoe","a":"pump","d":"Low-cut, closed shoe with a raised heel and no fastening.",
 "t":["stiletto heel","kitten heel","block heel","platform","pointed toe","almond toe","d'Orsay (open sides)"],
 "s":"https://en.wikipedia.org/wiki/Court_shoe",
 "x":[
  {"n":"Pigalle","a":"","d":"Louboutin's low-cut, high-heeled pointed pump with a short toe box and red lacquered sole, named after the Paris district.",
   "mk":"Christian Louboutin","y":"2004","s":LB,
   "v":[{"n":"Pigalle Follies","mk":"Christian Louboutin","y":"","d":"more revealing side cut, curved shank, tapering heel"},
        {"n":"Pigalle Plato","mk":"Christian Louboutin","y":"","d":"classic shape on a platform"}],
   "dt":"heel heights · black patent, leathers and fabrics · crystal, stud and spike embellishment"},
  {"n":"So Kate","a":"","d":"Pigalle reworked for Kate Moss with a longer pointed toe and a thinner, higher heel.",
   "mk":"Christian Louboutin","y":"","s":PEP,"v":[],"dt":"leathers · colours"},
  {"n":"BB","a":"","d":"Manolo Blahnik's pointed stiletto pump, named after and inspired by Brigitte Bardot's 1950s–60s style.",
   "mk":"Manolo Blahnik","y":"2009","s":"https://thearchives.manoloblahnik.com/wcag/thecraft/pump-pump-01",
   "v":[],"dt":"heel heights · suede, leather and many fabrics · colours"},
  {"n":"Hangisi","a":"","d":"Manolo Blahnik's signature jewelled-buckle pump, worn in blue by Carrie Bradshaw at her wedding in the Sex and the City film.",
   "mk":"Manolo Blahnik","y":"","s":TI,"v":[],"dt":"satin and other fabrics · colours · crystal buckle"},
  {"n":"Belle Vivier","a":"Pilgrim-buckle shoe · Belle de Jour pump","d":"Black pump whose only ornament is a large metal buckle, shown with YSL's Mondrian collection and worn by Catherine Deneuve in Belle de Jour.",
   "mk":"Roger Vivier","y":"1965","s":"https://www.wmagazine.com/fashion/roger-vivier-belle-vivier-shoes-backstory-catherine-deneuve",
   "v":[{"n":"Belle de Jour (film)","mk":"Roger Vivier","y":"1967","d":"worn by Catherine Deneuve; renamed after the film"},
        {"n":"Belle Vivier 60","mk":"Roger Vivier","y":"2026","d":"60th-anniversary pumps, slingbacks and ballet flats (Pizzo, Prato)"}],
   "dt":"patent leather, satin, lace · buckle size and colour · heel height"},
  {"n":"Vara","a":"Vara Bow","d":"Ferragamo's low-heeled round-toe pump with a grosgrain bow and gold logo plaque, created by Fiamma Ferragamo.",
   "mk":"Salvatore Ferragamo","y":"1978","s":"https://philstar.com/lifestyle/ystyle/2010/07/02/589170/take-bow",
   "v":[{"n":"Vara platform pump","mk":"Salvatore Ferragamo","y":"","d":"slender-heeled platform version"}],
   "dt":"low heel · leathers · bow colours"},
  {"n":"Romy","a":"","d":"Jimmy Choo's pointed-toe stiletto pump, a house signature.",
   "mk":"Jimmy Choo","y":"2016","s":"https://luxe.digital/brands/jimmy-choo/","v":[],"dt":"heel heights · leathers, suede, glitter · colours"},
  {"n":"Anouk","a":"","d":"Jimmy Choo's pointed-toe pump, a red-carpet staple.",
   "mk":"Jimmy Choo","y":"","s":"https://luxe.digital/brands/jimmy-choo/","v":[],"dt":"heel heights · leathers · colours"}]},
{"n":"Slingback","a":"","d":"Court-cut shoe held by a strap round the back of the heel rather than fully round the ankle.",
 "t":["kitten heel","block heel","flat slingback","two-tone"],
 "s":"https://en.wikipedia.org/wiki/Slingback",
 "x":[{"n":"Chanel two-tone slingback","a":"Chanel slingback","d":"Beige pump with a black toecap and heel and a back strap, designed with shoemaker Raymond Massaro.",
   "mk":"Chanel","y":"1957","s":"https://collections.vam.ac.uk/item/O1312036",
   "v":[{"n":"Lagerfeld reissue","mk":"Chanel","y":"2015","d":"relaunched by Karl Lagerfeld; some pairs move the CC logo to the heel"}],
   "dt":"beige with black cap · leather, cotton · pearl and logo trims · heel height"}]},
{"n":"Peep-toe shoe","a":"peep-toe pump","d":"Court shoe, slingback or bootie with a small cut-out at the toe.",
 "t":["peep-toe pump","peep-toe slingback","peep-toe platform"],
 "s":"https://en.wikipedia.org/wiki/Peep-toe_shoe"},
{"n":"Ballet flat","a":"ballet pump · ballerina","d":"Flat or near-flat low-cut shoe modelled on a ballet shoe, with a thin sole and shallow vamp.",
 "t":["bow trim","pointed toe","round toe","cap toe"],
 "s":"https://en.wikipedia.org/wiki/Ballet_flat",
 "x":[{"n":"Cendrillon","a":"","d":"Repetto's stitch-and-return ballet flat, made in carmine red for Brigitte Bardot.",
   "mk":"Repetto","y":"1956","s":"https://www.journalduluxe.fr/fr/mode/les-ballerines-cendrillon-de-repetto-une-histoire-qui-commence-au-cinema",
   "v":[{"n":"Bardot original","mk":"Repetto","y":"1956","d":"carmine red, seen in Et Dieu… créa la femme"},
        {"n":"Bow Ballet Flats","mk":"Repetto","y":"","d":"bow-trimmed version"}],
   "dt":"cousu-retourné construction · colours and leathers"},
  {"n":"Chanel two-tone ballerina","a":"Chanel ballet flat","d":"Ballet-flat reinterpretation of Chanel's two-tone shoe, with a contrast toe cap, bow and CC logo.",
   "mk":"Chanel","y":"1985","s":"https://www.thestar.com.my/lifestyle/style/2026/07/25/how-one-fashion-house-made-ballet-flats-a-high-low-wardrobe-staple",
   "v":[],"dt":"beige or colour with contrast cap · patent, quilted leather, denim, snakeskin, pony hair"},
  {"n":"Varina","a":"","d":"Ballerina version of Ferragamo's Vara, keeping the grosgrain bow and gold plaque.",
   "mk":"Salvatore Ferragamo","y":"","s":"https://philstar.com/lifestyle/ystyle/2010/07/02/589170/take-bow","v":[],"dt":"leathers · bow colours"}]},
{"n":"Mary Jane","a":"bar shoe · strap shoe · doll shoe","d":"Closed, low-cut shoe with one or more straps across the instep.",
 "t":["T-bar","Mary Jane pump (heeled)","platform","children's school shoe","buckle or button strap"],
 "tg":["baby"],
 "s":"https://en.wikipedia.org/wiki/Mary_Jane_(shoe)",
 "x":[{"n":"Campari","a":"","d":"Manolo Blahnik's Mary Jane pump, seen in Sex and the City.",
   "mk":"Manolo Blahnik","y":"","s":TI,"v":[],"dt":"heel height · leathers · colours"}],
 "m":[["Ballet Twist","Repetto"],["Georgia","Repetto"],["Rose","Repetto"],["Sonnet","Start-rite"]]}]
brands=[
 {"n":"Christian Louboutin","c":"France","f":"1991","seg":"Luxury shoes","d":"Paris shoe house known for red lacquered soles, first made in 1992–93.","lines":[],"eras":[],"sig":["Pigalle","So Kate"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Christian_Louboutin"},
 {"n":"Manolo Blahnik","c":"United Kingdom","f":"","seg":"Luxury shoes","d":"London shoe house of the Spanish-born designer, selling shoes under his name since 1971.","lines":[],"eras":[],"sig":["BB","Hangisi","Campari"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Manolo_Blahnik"},
 {"n":"Roger Vivier","c":"France","f":"1937","seg":"Luxury shoes","d":"Paris shoe label of the designer credited with the modern stiletto (1954), owned by Tod's since 2000.","lines":[],"eras":["Bruno Frisoni, 2002–2018","Gherardo Felloni, 2018–"],"sig":["Belle Vivier"],"sc":[],"rel":["Tod's"],"s":"https://en.wikipedia.org/wiki/Roger_Vivier_(brand)"},
 {"n":"Jimmy Choo","c":"United Kingdom","f":"1996","seg":"Luxury shoes","d":"London luxury house founded by Jimmy Choo and Tamara Mellon, part of Capri Holdings.","lines":[],"eras":[],"sig":["Romy","Anouk"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Jimmy_Choo_Ltd"},
 {"n":"Repetto","c":"France","f":"1947","seg":"Dance and ballet shoes","d":"Paris dance-shoe maker founded by Rose Repetto, known for the Cendrillon ballet flat.","lines":[],"eras":[],"sig":["Cendrillon"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Repetto"},
 {"n":"Chanel","c":"France","f":"1910","seg":"Luxury fashion house","d":"Paris fashion house whose two-tone shoe dates from 1957.","lines":[],"eras":["Karl Lagerfeld, 1983–2019"],"sig":["Chanel two-tone slingback","Chanel two-tone ballerina"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Salvatore Ferragamo","c":"Italy","f":"1927","seg":"Luxury shoes and fashion","d":"Florence house founded by shoemaker Salvatore Ferragamo.","lines":[],"eras":[],"sig":["Vara","Varina"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Start-rite","c":"United Kingdom","f":"1792","seg":"Children's shoes","d":"Norwich children's shoemaker, first to offer width fittings for children's shoes.","lines":["Sonnet (US)"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Start-rite"}]
notes=("Dropped high-street SKUs Betts Chaps/Jerry/Kendra and Wittner Gabby/Luna (not test winners). 'T-bar sandal' model turned into a T-bar type on Mary Jane. "
 "Repetto Georgiana dropped as near-duplicate of Georgia. Prada Mary Jane not added: no retrieved source. So Kate, Hangisi, Campari, Anouk, Varina years left blank (no retrieved page gave them); "
 "Louboutin, Roger Vivier and Purseblog/Harper's pages were blocked (403), so not used. Kate (2012) / So Kate (2013) dates and Manolo BB heel heights left out.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
tmp=P+'.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
