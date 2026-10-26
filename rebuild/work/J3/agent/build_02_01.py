import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Kefir","a":"milk kefir · kephir · кефир","d":"Tart, slightly fizzy milk fermented with kefir grains, a culture of bacteria and yeasts.",
  "t":["plain","flavoured","cow's milk","goat's milk","low-fat / non-fat","organic"],"s":W+"Kefir",
  "x":[X("Grain kefir","traditional kefir · Caucasian kefir","Milk fermented 12–24 hours with reusable kefir grains, then strained; the grains grow and are reused.","","North Caucasus; ancient (Bronze Age finds c. 3,600 years old)",W+"Kefir",
     [("Lifeway Kefir","Lifeway Foods","","US kefir range: low-fat, non-fat, Greek, organic and low-carb, in many flavours"),
      ("Biotiful Kefir Drink","Biotiful Gut Health","2012","UK kefir drinks; the brand was founded in London in 2012")],
     "milk: cow, goat, sheep · raw or pasteurised · plain or flavoured")],
  "m":[["Eker Kefir","Eker Süt Ürünleri"],["Pınar Kefir","Pınar Süt Ürünleri"],["Kaf Kefir","Sütaş"],["Torku Kefir","Torku"],["İçim Kefir Plain","İçim"],["Milla Kefir","Milla Dairy (AgroDairy)"]]},
 {"n":"Drinking yoghurt & ayran","a":"drinking yogurt · ayran · doogh · lassi · laban","d":"Yoghurt thinned with water or milk into a drink, salted as in ayran and doogh or sweet and fruity as in lassi.",
  "t":["salted","sweet","fruit-flavoured","carbonated","with mint or herbs","churned (frothy)"],"s":"https://www.sutas.com/sutas-ayran-1-l",
  "x":[X("Ayran","chalap · ayryan","Cold savoury drink of yoghurt, water and salt, developed by Central Asian Turkic peoples.","","Central Asia; attested c. 1000 CE",W+"Ayran",
     [("Yayık ayranı","","","Churned, very frothy Turkish ayran from eastern Turkey"),("Sütaş Ayran","Sütaş","",""),("Pınar Ayran","Pınar",""," "),("Eker Ayran","Eker Süt Ürünleri","",""),("İçim Bottled Ayran","İçim","",""),("Torku Bottled Ayran","Torku","",""),("İtimat Ayran","İtimat Peynircilik Süt ve Süt Ürünleri","",""),("Danish Ayran","Danish Dairy Farm","","")],
     "salted · still or carbonated · plain or with mint"),
   X("Doogh","dugh","Cold savoury Persian drink of fermented milk, yoghurt or buttermilk with water and salt, sometimes with herb extracts.","","Ancient Persia",W+"Doogh",(),"salted · herbs such as thyme"),
   X("Lassi","","Smoothie-like Punjabi drink of yoghurt blended with water and spices or sugar, traditionally from buffalo-milk yoghurt.","","Punjab",W+"Lassi",
     [("Namkeen lassi","","","Salted, with black pepper and cumin"),("Meethi lassi","","","Sweet, with cardamom, rosewater and saffron"),("Mango lassi","","","Fruit lassi"),("Verka Plain Lassi","Punjab Milk Producers Federation (Verka)","",""),("Vita Plain Lassi","Vita (Haryana state dairy)","","")],
     "salted, spiced, sweet or fruit · served in a clay kulhar")],
  "m":[["Almarai Fresh Laban","Almarai"]]},
 {"n":"Buttermilk","a":"cultured buttermilk · chaas · chhachh · yayık ayranı","d":"Thin sour liquid left from churning cultured cream, or milk cultured to resemble it, drunk or used in cooking.",
  "t":["cultured buttermilk","traditional churned buttermilk","chaas / chhach","spiced (masala)","low-fat"],"s":W+"Buttermilk",
  "x":[X("Cultured buttermilk","","Pasteurised milk thickened by lactic acid bacteria; sold commercially in the United States since the 1920s.","","1920s (US)",W+"Buttermilk",
     [("Natural Cultured Buttermilk","Longley Farm","","")],"fat level · liquid or dried"),
   X("Traditional buttermilk","churned buttermilk","Thin liquid with under 0.5% fat left after churning butter from naturally cultured cream.","","traditional",W+"Buttermilk",(),"South Asia, Middle East, parts of Europe"),
   X("Chaas","chhas · chhachh · mattha · majjige · moru · ghol · taak","Salted South Asian drink of yoghurt churned with cold water, often spiced with cumin, ginger, chilli or curry leaves.","","Indian subcontinent",W+"Chaas",
     [("Amul Masala Chaas","Amul","","Best-selling bottled chaas"),("Amul High Protein Buttermilk","Amul","",""),("Mother Dairy Chach","Mother Dairy","",""),("Vita Chhach","Vita (Haryana state dairy)","",""),("Milma Kattimoru","Kerala Co-operative Milk Marketing Federation (Milma)","","Kerala spiced buttermilk")],
     "plain, masala, mint or rose flavour")]},
 {"n":"Soured milk","a":"mesophilic cultured milk · filmjölk · viili · piimä · amasi · maas · kulturmelk · súrmjólk","d":"Milk fermented whole at room temperature into a mild, thick or ropy drink or spoonable food; not buttermilk.",
  "t":["drinkable","spoonable","ropy / long","probiotic","flavoured","low-fat"],"s":W+"Fermented_milk_products",
  "x":[X("Filmjölk","fil","Swedish milk fermented with Lactococcus lactis and Leuconostoc into a thick, mildly sour, buttery product.","","Sweden; first commercial 1931",W+"Filmj%C3%B6lk",
     [("Filmjölk","Arla Foods","1931","First commercial filmjölk"),("Långfil","Arla Foods","1965","Stringy, elastic variant"),("A-fil","Arla Foods","1984","Probiotic, with L. acidophilus"),("Flavoured filmjölk","Arla Foods","1997","Strawberry first")],
     "fat 0.5–3% · plain or flavoured"),
   X("Viili","","Finnish and Swedish ropy fermented milk with a velvety surface of the fungus Geotrichum candidum.","","Nordic countries",W+"Viili",[("Old Style Viili","Valio","","")],"plain or flavoured · spoonable"),
   X("Piimä","","Finnish sour milk similar to buttermilk, drunk by the glass with meals.","","Finland","https://finland.fi/life-society/demystifying-finnish-dairy-food/",[("Piimä","Valio","","")],"drinkable · fat level"),
   X("Amasi","maas · emasi · mafi","Thick, strongly sour curdled milk of Southern Africa, traditionally fermented in a calabash or hide sack.","","Southern Africa; pre-colonial",W+"Amasi",
     [("Clover Maas","Clover S.A.","",""),("First Choice Full Cream Amasi","Woodlands Dairy","","")],"full cream or low-fat · drunk or poured over pap"),
   X("Colombian kumis","kumis colombiano","Sour, creamy Colombian drink of cow's milk fermented for hours or days, sweetened before serving.","","Colombia","https://mycolombianrecipes.com/?p=9264",
     [("Alpina Kumis","Alpina Productos Alimenticios","",""),("Colanta Kumis","Colanta","","")],"cup or bottle · sweetened")],
  "m":[["KCC Mala","New Kenya Co-operative Creameries (New KCC)"]]},
 {"n":"Probiotic cultured drink","a":"probiotic shot · lactic acid bacteria drink","d":"Small sweetened bottle of milk fermented with a named probiotic bacterial strain, drunk daily.",
  "t":["original","reduced sugar / light","high-count"],"s":W+"Yakult",
  "x":[X("Yakult","","Japanese probiotic milk drink fermented with Lacticaseibacillus casei Shirota, developed by Minoru Shirota.","Yakult Honsha","1935",W+"Yakult",
     [("Yakult","Yakult Honsha","1935","Original"),("Yakult LIGHT","Yakult Honsha","2004","Lower sugar; launched in Australia, stevia from 2017"),("Yakult 1000","Yakult Honsha","","Version advertised from 2020")],"original or light · strain L. casei Shirota"),
   X("Actimel","DanActive","Danone's probiotic yoghurt-type drink with Lactobacillus casei, first sold in Belgium.","Danone","1994",W+"Actimel",
     [("Actimel","Danone","1994","Belgium launch"),("DanActive","Danone","","Name in the United States and Canada")],"plain or flavoured"),
   X("Vifit","","Dutch drinking yoghurt with the probiotic L. rhamnosus GG (Gorbach & Goldin), fortified with vitamins.","FrieslandCampina","","https://www.plus.nl/product/vifit-drink-rode-vruchten-pak-500-ml-169235",
     [("Vifit Drink rode vruchten","FrieslandCampina","","500 ml pack, 0.8% fat")],"fruit flavours · 500 ml and 1 l packs")]},
 {"n":"Kumys","a":"kumis · koumiss · airag · kymyz","d":"Mildly alcoholic fermented mare's milk of the Central Asian steppes, made with a liquid starter of lactobacilli and yeasts.",
  "t":["mare's milk","cow's milk (industrial)"],"s":W+"Kumis",
  "x":[X("Kumis","airag · kumyz · cosmos","Mare's milk fermented to 0.7–2.5% alcohol, central to Turkic and Mongolic steppe peoples.","","5th century BC (Herodotus)",W+"Kumis",(),"mare's milk or adjusted cow's milk · alcohol 0.7–2.5%")]},
 {"n":"Ryazhenka","a":"fermented baked milk · ryazhanka · varenets","d":"Milk baked for hours until browned, then fermented to a thick, caramel-tasting drink or spoonable product.",
  "t":["ryazhenka","varenets","fat 1–8.9%"],"s":W+"Ryazhenka",
  "x":[X("Ryazhenka","ryazhanka · Ukrainian ryazhenka","Milk simmered at least eight hours until browned, then cultured; caramel flavour and creamy colour.","","Ukraine",W+"Ryazhenka",(),"GOST 31455-2012 · fat 3.5–4% typical"),
   X("Varenets","stewler · simmeler","Russian baked milk fermented with sour cream or Streptococcus thermophilus; distinct from ryazhenka under GOST.","","Russia",W+"Varenets",(),"GOST R 53508-2009 · fat 0.5–8.9%")]},
]
for k in kinds:
    for x in k.get("x",[]):
        for v in x["v"]:
            v["d"]=v["d"].strip()
brands=[
 {"n":"Yakult Honsha","c":"Japan","f":"1955","seg":"Probiotic drinks","d":"Tokyo company making Yakult, founded on Minoru Shirota's lactic acid bacterium; Danone is its largest shareholder.","lines":["Yakult"],"eras":[],"sig":["Yakult"],"sc":[],"rel":["Danone"],"s":W+"Yakult_Honsha"},
 {"n":"Danone","c":"France","f":"1919","seg":"Dairy and plant-based foods","d":"French food multinational begun by Isaac Carasso as a yoghurt brand in Barcelona.","lines":["Activia","Alpro","Actimel"],"eras":[],"sig":["Actimel"],"sc":[],"rel":["Yakult Honsha"],"s":W+"Danone"},
 {"n":"FrieslandCampina","c":"Netherlands","f":"2008","seg":"Dairy cooperative","d":"Dutch dairy cooperative formed by the merger of Friesland Foods and Campina, based in Amersfoort.","lines":["Friesche Vlag","Campina","Mona","Vifit"],"eras":[],"sig":["Vifit"],"sc":[],"rel":[],"s":W+"FrieslandCampina"},
 {"n":"Lifeway Foods","c":"United States","f":"1986","seg":"Kefir","d":"Illinois kefir maker founded by Michael Smolyansky, with kefir as its flagship product.","lines":["Kefir"],"eras":[],"sig":["Grain kefir"],"sc":[],"rel":[],"s":W+"Lifeway_Foods"},
 {"n":"Biotiful Gut Health","c":"United Kingdom","f":"2012","seg":"Kefir","d":"London kefir brand founded by Natasha Bowes, making kefir drinks, kefir yoghurts and kids' kefir.","lines":["Kefir drinks","Kefir Protein"],"eras":[],"sig":["Grain kefir"],"sc":[],"rel":[],"s":"https://www.foodmanufacture.co.uk/Article/2024/10/03/A-day-in-the-life-of-Biotiful-Gut-Health-CEO-Natasha-Bowes"},
 {"n":"Arla Foods","c":"Denmark","f":"2000","seg":"Dairy cooperative","d":"Danish-Swedish farmer-owned dairy cooperative formed from Arla and MD Foods; introduced commercial filmjölk in 1931.","lines":["Arla","Lurpak","Puck","Castello"],"eras":[],"sig":["Filmjölk"],"sc":[],"rel":[],"s":W+"Arla_Foods"},
 {"n":"Valio","c":"Finland","f":"1905","seg":"Dairy cooperative","d":"Finnish dairy company founded by 17 co-operative dairies, owned by dairy cooperatives.","lines":["Koskenlaskija","Finlandia","Oddlygood"],"eras":[],"sig":["Viili","Piimä"],"sc":[],"rel":[],"s":W+"Valio"},
]
G="Food & drink"
trads=[
 {"n":"Caucasian kefir","g":G,"r":"North Caucasus","p":"Ancient; kefir found in Bronze Age graves c. 3,600 years old","d":"Grain-fermented milk of North Caucasian, notably Circassian, tradition that spread through the Soviet Union and worldwide.","tech":"2–5% kefir grains in milk for 12–24 hours at 20–25 °C, then strained and reused","mat":"cow's, goat's or sheep's milk, traditionally raw","forms":["Kefir"],"ctr":["Circassian cuisine"],"auth":"Made with living kefir grains (bacteria and yeasts in a kefiran matrix), not only a powdered starter","s":W+"Kefir"},
 {"n":"Nordic soured milks","g":G,"r":"Sweden, Finland, Norway, Iceland","p":"Traditional; commercial filmjölk from 1931","d":"Room-temperature fermented milks of the Nordic countries, from thick filmjölk to ropy viili and drinkable piimä.","tech":"Mesophilic fermentation with Lactococcus lactis and Leuconostoc; Geotrichum candidum on viili","mat":"cow's milk","forms":["Filmjölk","Långfil","Viili","Piimä"],"ctr":["Arla Foods","Valio"],"auth":"Mesophilic cultures give a mild, buttery sourness; viili has a velvety mould surface","s":W+"Filmj%C3%B6lk"},
 {"n":"Central Asian kumys","g":G,"r":"Central and East Asian steppes","p":"Described by Herodotus (5th century BC) and William of Rubruck (13th century)","d":"Fermented mare's milk of Kazakh, Kyrgyz, Bashkir, Kalmyk, Mongol and Yakut peoples.","tech":"Liquid starter of lactobacilli and yeasts; mildly alcoholic (0.7–2.5%)","mat":"mare's milk","forms":["Kumys"],"ctr":["Kazakhs","Kyrgyz","Bashkirs","Mongols","Yakuts"],"auth":"Made from mare's milk; industrial versions use cow's milk adjusted with sucrose or whey","s":W+"Kumis"},
 {"n":"Southern African amasi","g":G,"r":"Southern Africa","p":"Pre-colonial to present","d":"Thick sour milk of Zulu, Xhosa, Ndebele, Swazi and Sotho tradition, eaten over maize porridge.","tech":"Unpasteurised milk fermented one to five days in a smoked calabash or hide sack, whey drained","mat":"cow's milk","forms":["Soured milk"],"ctr":["South Africa","Zimbabwe","Lesotho"],"auth":"Traditional amasi is calabash-fermented raw milk; commercial versions use Lactococcus lactis on pasteurised milk","s":W+"Amasi"},
]
notes=("Kept all 6 old kinds; added NEW Probiotic cultured drink (Yakult originator, Actimel, Vifit). Old exclusion of sweetened drinks dropped: sweet and fruit lassi are versions/types. "
 "Colombian kumis (cow's milk) placed under Soured milk, not Kumys. Left out: Armenian tan (no page retrieved; Wikipedia 404), shubat and pitkäpiimä (not confirmed on a fetched page), bhang lassi (cannabis), Calpis (soft drink), water kefir (not dairy), Chalap/Ayran/Doogh/Lassi generic model rows (now archetypes). "
 "No Amul, Sütaş or Alpina register entries (no brand page fetched). Most version years unknown and left blank.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J3/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
