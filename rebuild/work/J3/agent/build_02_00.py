import json, os
W='https://en.wikipedia.org/wiki/'
OLD_S='https://www.stonyfield.com/products/whole-milk-greek-plain-30-oz/'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(z) for z in v],"dt":dt}
def V(n,mk='',y='',d=''):
    o={"n":n}
    if mk: o["mk"]=mk
    if y: o["y"]=y
    if d: o["d"]=d
    return o
yog={"n":"Yoghurt","a":"yogurt · ヨーグルト · curd · dahi · yoğurt · kiselo mlyako","d":"Milk fermented with yoghurt cultures, set or stirred, plain or fruited, eaten with a spoon.",
 "t":["set","stirred","plain","fruit","probiotic","cream-top (kaymaklı)","clay-pot (çömlek)","cow's, sheep's, goat's or buffalo milk"],
 "s":OLD_S,
 "x":[
  X("Bulgarian yoghurt","Bulgarsko kiselo mlyako PDO · Българско кисело мляко · Bulgarian soured milk","Bulgarian soured milk from raw milk fermented with Lactobacillus bulgaricus and Streptococcus thermophilus; EU PDO since 2023.","","PDO 2023",
    "https://www.bta.bg/en/news/496211-bulgarian-yogurt-approved-as-protected-designation-of-origin",
    [V("Bulgarsko kiselo mlyako PDO",y="2023",d="EU-registered original, made in Bulgaria"),
     V("Meiji Bulgaria Yogurt","Meiji","1973",d="Japanese licensed version with Bulgarian starter cultures; launched 1971 as plain yoghurt, renamed 1973"),
     V("Mosilian (Momchilovtsi)","Bright Dairy",d="Chinese Bulgarian-style yoghurt")],
    "milk species · fat · clay pot or plastic tub"),
  X("Matsoni","matzoon · matsun · madzoon · Caspian Sea yoghurt","Armenian and Georgian fermented milk set from a previous batch, mostly cow's milk; Georgian GI since 2012.","","GI (Georgia) 2012",W+"Matzoon",
    [V("Georgian matsoni GI",y="2012"),V("Armenian matsun",d="Armenian GI applied for 2025"),
     V("Colombo madzoon","Colombo and Sons Creamery","1929",d="brought matzoon to New England; brand discontinued 2010")],
    "cow, goat, sheep or buffalo milk"),
  X("Dahi","curd · doi · mosaru · perugu · thayir · mee kiri","Home-style yoghurt of the Indian subcontinent, usually cow's or buffalo milk, set in pots.","","traditional",W+"Dahi_(curd)",
    [V("Buffalo curd (mee kiri)",d="Sri Lankan buffalo-milk curd set in clay pots"),V("Mitha dahi",d="sweetened dahi"),
     V("Mother Dairy Classic Dahi","Mother Dairy"),V("Verka Low Fat Dahi","Punjab Milk Producers Federation (Verka)"),
     V("Milma SET Curd","Kerala Co-operative Milk Marketing Federation (Milma)"),V("Hatsun Curd","Hatsun Agro Product"),
     V("Heritage Probiotic Curd","Heritage Foods"),V("Akshayakalpa Organic Probiotic Curd","Akshayakalpa Organic")],
    "cow or buffalo milk · clay pot or cup · probiotic"),
  X("Mishti doi","sweet curd · lal doi","Bengali sweetened curd made from thickened milk with sugar or jaggery, fermented overnight in earthenware.","","traditional",W+"Mishti_doi",
    [V("Nabadwip lal doi"),V("Bogra doi (Bogurar doi)"),V("Kolkata mishti doi"),
     V("Mother Dairy Mishti Doi","Mother Dairy"),V("Milky Mist Mishti Doi","Milky Mist Dairy Food"),
     V("Mother Dairy Aam Doi","Mother Dairy",d="mango"),V("Igloo Sweet Curd","Igloo Dairy"),
     V("Milk Vita Sweet Yogurt","Milk Vita (Bangladesh Milk Producers' Cooperative Union)")],
    "sugar or date-palm jaggery · clay pot"),
  X("Afyonkarahisar manda yoğurdu","Afyon buffalo yoghurt","Dense porcelain-white yoghurt of Anatolian buffalo milk left after kaymak making; Turkish designation of origin 2021.","","GI 2021",
    "https://kureansiklopedi.com/tr/detay/afyonkarahisar-manda-yogurdu-8c32d",[],"buffalo milk · min. 3% fat, 5% protein"),
  X("Silifke yoğurdu","Silifke yoghurt","Goat's-milk yoghurt of Silifke, Mersin, set and sold in earthenware or metal pails; Turkish GI 2022.","","GI 2022",
    "https://kureansiklopedi.com/tr/detay/silifke-yogurdu-bed67",[V("Goat and cow blend",d="80% cow, 20% goat milk when goat milk is scarce")],"goat milk · earthenware pot"),
  X("Tavas yanık koyun yoğurdu","isli yoğurt · Tavas burnt sheep's yoghurt","Full-fat sheep's-milk yoghurt from Denizli with a caramelised, burnt taste from milk scorched on the pan; Turkish GI 2024.","","GI 2024",
    "https://ci.turkpatent.gov.tr/Files/GeographicalSigns/19dcf49a-1acc-4b1d-986f-ce26ae94eed6.pdf",[V("Tavas süzme",d="strained version")],"sheep milk · cream top · set or strained"),
  X("Pokot ash yoghurt","ash yoghurt","Raw goat's or cow's milk fermented in smoked gourds in West Pokot, Kenya, finished with kromwo tree ash.","","traditional",
    "https://malindikenya.net/en/articles/territory/local-products/the-extraordinary-pokot-ash-yogurt.html",[V("Goat's milk"),V("Cow's milk")],"gourd · grey ash colour"),
  X("Activia","Bio · Bifidus Regularis","Danone's probiotic spoon yoghurt with the Bifidobacterium animalis DN 173 010 strain, launched in France as Bio.","Danone","1987",W+"Activia",
    [V("Bio","Danone","1987",d="original French launch name"),V("Activia","Danone",d="sold in over 70 countries by 2013"),V("AktiBio","Danone","2023",d="Russian renaming")],
    "plain · fruit · fat level"),
 ],
 "m":[["Yoplait","Yoplait"],["Oui","Yoplait"],["Petits Filous","Yoplait"],["Müller Corner","Müller"],["Müllerlight","Müller"],
      ["Danonino","Danone"],["Chunzhen","Mengniu Dairy"],["Ambrosial (Anmuxi)","Yili Group"],["Bifidus Yogurt","Morinaga Milk Industry"],
      ["Megumi megumi","Megmilk Snow Brand"],["Sütaş Tava Yoğurt","Sütaş"],["Eker Kaymaklı Çömlek Yoğurt","Eker Süt Ürünleri"],
      ["Pınar Denge Probiotic Yoghurt","Pınar Süt Ürünleri"],["La Serenísima Yogurísimo","Mastellone Hermanos (La Serenísima)"],
      ["Colanta Yogurt","Colanta"],["Juhayna Stirred Yogurt","Juhayna Food Industries"],["Almarai Vetal Layered Fruit Yoghurt","Almarai"],
      ["Soprole Yogurt Proteína","Soprole"]]}
SY=W+"Strained_yogurt"
strained={"n":"Strained yoghurt","a":"Greek yoghurt · Greek-style yoghurt · süzme yoğurt · kese yoğurdu · hung curd · chakka · yogurt cheese",
 "d":"Yoghurt with most of the whey drained off, giving a thick, concentrated texture.",
 "t":["Greek (made in Greece)","Greek-style","süzme / kese yoğurdu (Turkey)","salcë kosi / salcë shakulli (Albania)","chakka / hung curd (South Asia)","fat-free, low-fat, full-fat"],
 "s":OLD_S,
 "x":[
  X("Fage Total","Total","The first commercial strained yoghurt, cow's milk strained industrially in Greece.","Fage","1975",SY,
    [V("Total (Greece)","Fage","1975"),V("Total (UK)","Fage","1980s",d="brought strained yoghurt to UK shoppers"),V("Total (US)","Fage","1998",d="imported; New York plant from 2008")],
    "fat level · plain or with fruit/honey"),
  X("Greek yoghurt","strained Greek yoghurt","Strained yoghurt made in Greece; in the UK and EU the name 'Greek' is reserved for it.","","",SY,[],"cow or sheep milk · fat level"),
  X("Chobani Greek Yogurt","Chobani","American Greek-style strained yoghurt that helped popularise Greek yoghurt in the US.","Chobani","2007",W+"Chobani",
    [V("Chobani UK 'Greek yogurt'","Chobani","2012",d="US-made; name ruled misleading in UK courts 2013–14")],"fat level · flavours"),
  X("Oikos","Dannon Oikos · Stonyfield Oikos","Greek-style strained yoghurt line now sold by Danone.","Danone","2007",SY,
    [V("Oikos Organic","Stonyfield","2007"),V("Dannon Oikos","Danone","2011")],"fat level · protein"),
 ],
 "m":[["Yoplait Greek 100","Yoplait"],["Lindahls Kvarg","Nestlé"],["Super Thick Kerned Yogurt","Yeo Valley"],
      ["Arslan Süzme Yoğurt","Arslan"],["Eker Süzme Yoğurt","Eker Süt Ürünleri"],["Torku Strained Yogurt","Torku"],["Salcë shakulli",""],
      ["Epigamia Greek Yogurt + Oats & Seed Mix","Drums Food International (Epigamia)"],["Authentikos Greek-style Yoghurt","Clover S.A."],
      ["Itambé Iogurte Grego","Itambé"],["Vigor Iogurte Grego Tradicional","Vigor"],["Milky Mist Greek Yogurt","Milky Mist Dairy Food"],
      ["Akshayakalpa Organic Greek Yoghurt","Akshayakalpa Organic"],["Juhayna Greek Yoghurt","Juhayna Food Industries"],
      ["Greek Yogurt Yopa","Binggrae"],["Honey-flavoured Greek Style Yogurt","Longley Farm"]]}
skyr={"n":"Skyr","a":"Icelandic skyr · Icelandic-style yoghurt","d":"Thick, mild Icelandic cultured skimmed-milk product, technically a fresh sour-milk cheese, eaten like yoghurt.",
 "t":["plain","flavoured","drinkable"],"s":"https://siggis.com/product/plain-nonfat/",
 "x":[
  X("Icelandic skyr","skyr","Traditional Icelandic skyr, recorded in the sagas, now chiefly made by the dairy cooperative Mjólkursamsalan.","Mjólkursamsalan","medieval",W+"Skyr",
    [V("Exported to the US",y="2005",d="sold at Whole Foods Market"),V("Licensed production in Denmark and Scotland",y="2006")],"originally sheep's, now cow's milk"),
  X("siggi's","siggi's skyr","Icelandic-style skyr made in the US by Siggi Hilmarsson's company, high in protein and lower in sugar.","siggi's","2005",W+"Siggi%27s_Dairy",
    [V("siggi's (Lactalis)","siggi's","2018",d="brand bought by Lactalis")],"fat level · fruit flavours"),
  X("Icelandic Provisions","Icelandic Provisions Skyr","Skyr made in North America from heirloom Icelandic cultures with an Icelandic farmer-owned dairy.","Icelandic Provisions","",
    "https://www.icelandicprovisions.com/",[V("Oatmilk Skyr","Icelandic Provisions",d="plant-based version")],"whole or low-fat · flavours"),
  X("Arla Icelandic-style skyr","Arla Skyr","Icelandic-style skyr sold by Arla since 2015.","Arla Foods","2015",SY,[],"plain · flavours"),
 ]}
labneh={"n":"Labneh","a":"labne · labaneh · labni · ymer · ylette","d":"Salted yoghurt strained longer than Greek yoghurt to a thick spread, plus Nordic thick soured milks.",
 "t":["labneh","labneh balls in oil (labaneh biz-zayt)","ymer (Denmark)","ylette (1.5% fat ymer)"],
 "s":"https://www.karoun.com/labneh.html",
 "x":[
  X("Labneh","labne · labaneh · labni","Levantine salted strained yoghurt, thicker than Greek yoghurt, eaten as a spread.","","traditional",SY,
    [V("Labaneh biz-zayt",d="dried labneh balls kept in olive oil, often coated in za'atar or sumac; Lebanon and Palestine")],"plain · with herbs · in oil"),
  X("Ymer","ymer","Danish concentrated fermented skimmed milk, drained of some whey, with more protein than yoghurt.","","1930s","https://en.wikipedia.org/wiki/Ymer_(dairy_product)",
    [V("Ymer",y="1930s"),V("Ylette",d="lighter 1.5% fat version")],"fat level"),
 ],
 "m":[["Al Kazi Labneh with Thyme","Al Kazi"],["Almarai Premium Full Fat Labneh","Almarai"],["Bahçıvan Labne","Bahçıvan Food Industry Trade"],
      ["Eker Labne","Eker Süt Ürünleri"],["Juhayna Turkish Labneh","Juhayna Food Industries"],["Karoun Labne","Karoun Dairies"],
      ["Milla Labneh","Milla Dairy (AgroDairy)"],["Pınar Labneh","Pınar Süt Ürünleri"],["Sütaş Labaneh","Sütaş"],["Teksüt Labne","Teksüt Süt Mamülleri"],["İçim Labneh","İçim"]]}
def B(n,c,f,seg,d,lines,sig,s,rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Fage","Greece","1926","Dairy","Greek dairy company (Filippou Brothers) that made the first commercial strained yoghurt.",["Total"],["Fage Total"],W+"Fage"),
 B("Chobani","United States","2005","Dairy","American strained-yoghurt maker founded by Hamdi Ulukaya, top-selling US Greek yoghurt brand.",["Greek yogurt","oat drinks","creamers"],["Chobani Greek Yogurt"],W+"Chobani"),
 B("siggi's","United States","2005","Dairy","Icelandic-style skyr brand founded in New York by Siggi Hilmarsson, owned by Lactalis since 2018.",["skyr"],["siggi's"],W+"Siggi%27s_Dairy"),
 B("Icelandic Provisions","","","Dairy","Skyr brand made with heirloom Icelandic cultures in partnership with an Icelandic farmer-owned dairy.",["Skyr","Oatmilk Skyr"],["Icelandic Provisions"],"https://www.icelandicprovisions.com/"),
 B("Mjólkursamsalan","Iceland","1927","Dairy cooperative","Iceland's largest dairy company, owned by two farmer cooperatives, and main maker of skyr.",[],["Icelandic skyr"],W+"Mj%C3%B3lkursamsalan"),
 B("Danone","France","1919","Food multinational","French food group that began with Isaac Carasso's yoghurt in Barcelona in 1919.",["Activia","Danonino","Oikos","Alpro"],["Activia","Oikos"],W+"Danone"),
 B("Yoplait","France","1965","Dairy","French yoghurt brand, the world's largest yoghurt franchise, owned by Sodiaal outside the US.",["Petits Filous","Oui","Go-Gurt"],[],W+"Yoplait"),
 B("Müller","Germany","1896","Dairy","Bavarian family dairy group, a leading UK yoghurt brand.",["Müller Corner","Müllerlight","FrütUp / Froop"],[],W+"M%C3%BCller_(company)"),
 B("Meiji","Japan","2009","Food and dairy","Japanese food holding company whose dairy arm makes Meiji Bulgaria Yogurt.",["Meiji Bulgaria Yogurt"],[],W+"Meiji_Holdings"),
 B("Mengniu Dairy","China","1999","Dairy","Chinese dairy company based in Hohhot, Inner Mongolia.",["Chunzhen"],[],W+"Mengniu_Dairy"),
 B("Yili Group","China","1993","Dairy","Chinese dairy group based in Hohhot, Inner Mongolia.",["Ambrosial (Anmuxi)","Satine"],[],W+"Yili_Group"),
 B("Amul","India","1946","Dairy cooperative","Gujarat farmer-owned dairy cooperative behind India's White Revolution, a large curd and yoghurt producer.",[],[],W+"Amul"),
]
trads=[{"n":"Pokot ash yoghurt","g":"Food & drink","r":"West Pokot, Kenya","p":"traditional","d":"Pastoral Pokot method of fermenting raw milk in smoked gourds and finishing it with tree ash.",
 "tech":"raw milk kept at least three days in gourds smoked over kromwo wood, whey drained, shaken, ash added","mat":"goat's or cow's milk, gourd calabashes, kromwo (Ozoroa insignis) ash",
 "forms":["Pokot ash yoghurt"],"ctr":["West Pokot families"],"auth":"light grey colour and aromatic, resinous note from the ash","s":"https://malindikenya.net/en/articles/territory/local-products/the-extraordinary-pokot-ash-yogurt.html"}]
notes=("Yoghurt: 66 SKUs cut to 9 archetypes (Bulgarian PDO, matsoni [matsoni+matzoon merged], dahi, mishti doi, 3 Turkish GI yoghurts, Pokot ash, Activia) with old models placed as versions, plus 18 market-leader models. "
 "Dropped as SKU noise: minor regional/flavour SKUs (e.g. Aarong, Alpina Bon Yurt, Alquería, Arslan Kaymaklı, Danone Japan Aloe, Eker Efsane/Probiyotik, Yomo, Greenfields, LIVO, Ambewela, Tirol, Megmilk Mainichi Honebuto, Morinaga Triple, Nestlé Milkpak, KCC Delite, Go Fruit, Gowardhan, Jane Love, CU Big, Soprole cereal, Tezcanlar, Vita Dahi, Kyodo LKM512, Rushi, Colun, Colanta Buffalo, İçim Yoğurt, Mother Dairy Ultimate/Nutrifit). "
 "Amul kept as brand only: no Amul yoghurt product confirmed on a retrieved page. Ísey skyr left out (only seen in search snippets). Fage Total fat-level versions not confirmed, so omitted. "
 "Strained: Fage Total, Greek, Chobani, Oikos as archetypes; süzme and salcë as types, their SKUs kept as models. Skyr: Icelandic skyr (Mjólkursamsalan) as origin, siggi's, Icelandic Provisions, Arla. Labneh renamed; ymer/ylette as types plus a Ymer archetype; labneh balls as type and version.")
out={"kinds":[yog,strained,skyr,labneh],"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J3/shelves/02_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('written')
