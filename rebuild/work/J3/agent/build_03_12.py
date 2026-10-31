import json, os
K="https://en.wikipedia.org/wiki/Kashk"
ANU="https://mongoliainstitute.anu.edu.au/content-centre/article/series/white-foods"
MC="https://en.wikipedia.org/wiki/Mongolian_cuisine"
CH="https://en.wikipedia.org/wiki/Chhurpi"
RU="https://en.wikipedia.org/wiki/Rushan_(cheese)"
def A(n,a,d,s,y="",v=(),dt="",mk=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":"","y":"","d":x[1]} for x in v],"dt":dt}
kinds=[
 {"n":"Qurut & jameed","a":"qurut · kurut · kurt · qurt · gurt · khuruud · chortan · shilanch · jameed · dried yoghurt balls",
  "d":"Hard, salted, sour balls or chunks of dried strained yoghurt or buttermilk curd from Central Asia, the Caucasus and the Levant.",
  "t":["balls","strips","chunks","soft to rock-hard","sweetened or unsweetened"],
  "s":K,
  "x":[
   A("Qurut","kurut · kurt · qurt · qūrt (Kazakh) · gurt (Turkmen)","Salted dried balls of strained yoghurt or buttermilk curd, sun-dried for weeks; Turkic Central Asia and Azerbaijan.",K,
     v=[("Qurut balls","Azerbaijani and Central Asian balls, dissolved for soups such as xəngəl and qurutob"),
        ("Qaraqurut (black qurut)","made from drained whey")],
     dt="shape balls, strips, chunks · hardness · salt level · cow, sheep or goat milk"),
   A("Jameed","jamid","Hard dried salted yoghurt of Jordan and the Levant.",K,
     dt="shape balls or cubes · goat, sheep or cow milk · salt level"),
   A("Chortan","","Armenian dried ricotta-like curd made from matzoon.",K,
     dt="shape · hardness"),
  ]},
 {"n":"Kashk","a":"kishk · keshk · keşk · keş · labba · dried whey",
  "d":"Sour dried or liquid yoghurt and whey product of Iran, Turkey, the Levant and Egypt, sometimes fermented with grain.",
  "t":["liquid","dried (soak before use)","powder","grain-based"],
  "s":K,
  "x":[
   A("Iranian kashk","kašk","Thick whitish whey or strained-yoghurt product sold liquid or dried, used in kashk-e bademjan.",K,y="10th century (Arabic cookbooks)",
     dt="liquid jar or dried pieces · salt level"),
   A("Turkish keş","keş peyniri · kurut · taş yoğurt · kuru yoğurt · katık keşi","Salty dried yoghurt product of Turkey; western versions treated as cheese, eastern ones made from whey.",K,
     v=[("Bolu keş","western Turkey; classed as cheese"),("Erzincan, Erzurum and Kars keş","eastern Turkey; made from yoghurt skimmed of butter")],
     dt="region · cheese-like or whey-based"),
   A("Levantine kishk","kishk","Powder of bulgur fermented with milk and laban, dried on rooftops; used on manakish and in soups.",K,
     dt="coarse or fine powder · goat or cow milk"),
   A("Egyptian keshk","keshk","Egyptian fermented dairy and grain keshk in several regional forms.",K,
     v=[("Keshk sa'idi","Upper Egypt"),("Keshk siyami","Coptic fasting version with fermented squash"),("Keshk matrouhi","Marsa Matrouh; goat milk and barley")],
     dt="region · grain (wheat or barley)"),
  ]},
 {"n":"Aaruul","a":"aruul · Mongolian dried curd",
  "d":"Sun-dried hard curd of Mongolia, dried on the ger roof and formed into shapes; part of the 'white foods'.",
  "t":["sweetened or unsweetened","firm and chewy","soft and crumbly"],
  "s":ANU,
  "x":[
   A("Aaruul","aruul","Curd from milk or yoghurt dried in the sun on the ger roof and moulded into shapes; keeps for months.",ANU,
     dt="shape · cow, yak or other milk · sugar or vanilla added"),
   A("Aarts","","Dried curd from sour milk, often mixed with urum; slightly fermented.",ANU,
     dt="dried or fresh · mixed with urum"),
   A("Eezgii","","Roasted dried curds.",MC, dt="roast level"),
  ]},
 {"n":"Chhurpi","a":"durkha · chogo · chugo · Himalayan hard cheese",
  "d":"Himalayan cheese from yak or cow buttermilk curd, eaten soft or smoked and dried into very hard chewing blocks.",
  "t":["soft","hard","yak milk","cow milk","dog chew"],
  "s":CH,
  "x":[
   A("Hard chhurpi","durkha · chogo","Soft chhurpi pressed in a jute bag, cut into cubes and dried over a fire; chewed for up to hours.",CH,
     v=[("Chhurpi dog chew","Nepali export dog treat")],
     dt="cube or bar · yak or cow milk · smoke level"),
   A("Soft chhurpi","","Mild white curd from boiled buttermilk drained in cloth, sometimes fermented; cooked or used in momo and senpen.",CH,
     dt="fresh or fermented"),
  ]},
 {"n":"Rushan","a":"milk fan · rǔshàn · nvxseiz · dried milk-fan cheese",
  "d":"Thin sheets of stretched cow's-milk curd wrapped on rods and air-dried to a shelf-stable fan.",
  "s":RU,
  "x":[
   A("Rushan","milk fan · nvxseiz · yenx seinp","Bai cow's-milk curd stretched into thin sheets on bamboo sticks and dried yellow and leathery; grilled or fried.",RU,
     dt="sheet size · plain · eaten grilled with rose-petal jam or fried"),
  ]},
]
trad=[
 {"n":"Central Asian & Mongolian white foods","g":"Food & drink","r":"Mongolia, Central Asia and the Caucasus",
  "p":"Nomadic pastoral tradition; dried yoghurt recorded in Arabic cookbooks from the 10th century",
  "d":"Pastoral dairy foods (tsagaan idee) eaten fresh in summer and dried into curd and yoghurt balls for winter.",
  "tech":"Churning yoghurt to remove butter, boiling and draining buttermilk curd, shaping and sun-drying for weeks",
  "mat":"Cow, yak, sheep, goat or mare's milk; salt",
  "forms":["Aaruul","Aarts","Eezgii","Qurut","Qaraqurut (black qurut)"],
  "ctr":["Mongolia","Kazakhstan","Kyrgyzstan","Tajikistan","Turkmenistan","Azerbaijan"],
  "auth":"Sun-dried, hand-shaped pieces with texture varying by animal; traditional qurut made from churned buttermilk rather than oven-fermented yoghurt.",
  "s":MC},
 {"n":"Himalayan chhurpi","g":"Food & drink","r":"Nepal, Bhutan, Tibet and Northeast India","p":"Traditional; dog-chew export industry by 2025",
  "d":"Mountain cheesemaking from yak and cow buttermilk, producing soft fresh chhurpi and fire-dried hard chewing cheese.",
  "tech":"Buttermilk boiled, curd drained in cloth, pressed in jute bags, cut into cubes and dried over a fire",
  "mat":"Yak or cow buttermilk",
  "forms":["Soft chhurpi","Hard chhurpi","Chhurpi dog chew"],
  "ctr":["Nepal","Bhutan","Tibet","Northeast India"],
  "auth":"Hard chhurpi is extremely hard and lasts 30 minutes to five hours in the mouth; soft chhurpi is white and mild.",
  "s":CH},
]
notes=("5 kinds, 15 archetypes, 0 brands, 2 traditions. Qurut (k91) and Jameed (k92) merged into 'Qurut & jameed' with Chortan as a third archetype; Aaruul's old model 'Aarts' became an archetype and Eezgii was added. "
 "Kashk now has Iranian, Turkish, Levantine and Egyptian archetypes. Old sources (retail store, Czech blog, nenow, List_of_dairy_products) were replaced by retrieved Wikipedia/ANU pages; en.wikipedia Qurut, Jameed and Aaruul all redirect to the Kashk article. "
 "Left out: brand Kashk Hendessi (the Wikipedia claim is marked citation needed); the mansaf/Karak association for jameed and the Rubing link for rushan (no retrieved page confirms them); dates for each archetype other than kashk.")
out={"kinds":kinds,"brands":[],"traditions":trad,"notes":notes}
p="work/J3/shelves/03_12.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
