import json, os
def X(n,d,mk,y,s,v=(),dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
BK='https://en.wikipedia.org/wiki/Bokken'; SG='https://www.seidoshop.com/pages/guide-iaito'; KB='https://www.seidoshop.com/products/kotobuki-bokken'
kinds=[
{"n":"Martial arts uniform","a":"keikogi · dōgi · judogi · karategi","d":"Cotton jacket and trousers worn for training in judo, karate and similar arts.",
 "t":["judogi","karategi","BJJ gi","dobok","single weave","double weave","heavy double weave (IJF)","IJF approved (red label)","white or blue","belt (obi) by rank"],
 "s":"https://www.fitshop.gr/boxing-and-martial-arts/judo-jiu-jitsu/page-2/",
 "x":[X("Mizuno Yusho","Mizuno's IJF-approved competition judogi, designed in Osaka.","Mizuno","","https://www.katsudo.sk/en/products/mizuno-ju-kimono-yusho-iii-ijf-750g-white",[("Yusho III IJF","Mizuno","","750 g/m², 80% cotton, 20% polyester")],"white or blue · sizes"),
      X("adidas Champion","Heavyweight IJF-approved competition judogi sold as separate jacket and trousers.","adidas","","https://www.budoonline.co.uk/pages/judo-gi-buying-guide",[("J-IJF Champion II","adidas","",""),("J-IJF Champion III","adidas","","")],"white or blue"),
      X("Tokaido karategi","Karate uniform from the first karate-uniform company, refined with Japan Karate Association instructors.","Tokaido","1958","https://en.wikipedia.org/wiki/Tokaido_(company)",[("Standard (kata)","Tokaido","","training and kata"),("Kumite","Tokaido","","lighter, for sparring")],"custom tailoring for 3rd dan and above"),
      X("Shureido K-10","Heavyweight karategi of Japanese No. 10 duck canvas from Okinawa, with a slight blue tinge when new.","Shureido","","https://www.martialtalk.com/threads/shureido-gi-question.140090/",[("New Wave 3 (NW-3)","Shureido","","heavy poly-cotton, for kata"),("NW-2","Shureido","","medium"),("NW-1","Shureido","","light")],"traditional or tournament cut")],
 "m":[["Shiai","Mizuno"],["Keiko","Mizuno"],["Kodomo Plus","Mizuno"],["J350","adidas"],["J250","adidas"],["Fuji","Fighterz"],["Tori Gold","Fighterz"],["Atlanta","Kappa"],["Competition 730","Olympus Sport"],["Nippon 2","Olympus Sport"],["Entori","Rage"]]},
{"n":"Kendo armour","a":"bogu","d":"Protective armour set made for kendo (head guard, gloves, breastplate and waist guard).",
 "t":["men (head guard)","kote (gloves)","dō (breastplate)","tare (waist guard)","hand-stitched (tezashi)","machine-stitched","stitch spacing in bu (e.g. 2 bu)"],
 "s":"https://global.bushizo.com/collections/26",
 "m":[["2bu tezashi bogu set","Maruyama Kendo Supply"]]},
{"n":"Shinai","a":"","d":"Practice sword of bamboo or carbon staves made for kendo sparring.",
 "t":["bamboo","carbon","sizes by age"],
 "s":"https://global.bushizo.com/collections/26",
 "m":[["Josui","Nishinippon Budogu"],["Homare","Nishinippon Budogu"],["Kuniyoshinosaku","Nishinippon Budogu"],["Kousen","Nishinippon Budogu"],["Hyosen","Nishinippon Budogu"]]},
{"n":"Bokken","a":"bokutō","d":"Solid wooden sword made for kendo and other Japanese sword-art practice.",
 "t":["white oak","red oak","biwa","hickory","daitō (long)","shōtō / kodachi (short)","tantō","suburitō (heavy, for solo cuts)","kendo kata set (tachi and kodachi)"],
 "s":"https://www.katsudo.sk/en/products/dax-practice-sword-bokken-standard-red-oak",
 "x":[X("Standard bokken","First standardised bokken, created by Aramaki Yasuo with the All Japan Kendo Federation in the 1950s.","Aramaki Workshop","1950s",BK,[("Kotobuki Bokken","Aramaki Workshop","2017","chevroned spine, extra-long kissaki; made for Seido")],"white oak, red oak or buna · 101.5 cm")],
 "m":[["Standard Bokken","DAX"]]},
{"n":"Iaito","a":"iaitō","d":"Unsharpened metal practice sword, usually of aluminium-zinc alloy, used for iaidō.",
 "t":["aluminium-zinc alloy","steel (outside Japan)","daitō","wakizashi","blade length by height","mock hamon"],
 "s":"https://en.wikipedia.org/wiki/Iait%C5%8D",
 "x":[X("Minosaka iaito","Japanese iaito with a bubble-free cast alloy blade and wide choice of tsuba and koshirae.","Minosaka","",SG,
        [("Tokusei","Minosaka","","entry model"),("Jidai","Minosaka","","entry model"),("Hon Koshirae","Minosaka","","heavy, for high grades"),("Toppei Koshirae","Minosaka","",""),("Shinto Higo Koshirae","Minosaka","",""),("Tensho Koshirae","Minosaka","","")],"blade length · tsuba · tsukaito cotton, silk or leather")],
 "m":[["Iaido sword","Tozando"]]},
{"n":"Hakama","a":"","d":"Pleated divided trousers worn over a keikogi in kendo, iaidō, aikido and kyūdō.",
 "t":["umanori (divided)","andon (undivided)","seven pleats","cotton","polyester","silk"],
 "s":"https://en.wikipedia.org/wiki/Hakama"},
{"n":"Wushu practice weapon","a":"","d":"Blunt or unsharpened wushu sword, broadsword, staff or spear made for practice or competition.",
 "t":["jian (straight sword)","dao (broadsword)","nandao (southern broadsword)","taiji jian","gun (staff; white wax wood or carbon fibre)","nangun (southern staff)","qiang (spear)","taiji fan"],
 "s":"https://jinli.treepl.co/catalogs/iwuf-approved-competition-steel-broadsword-dao"},
]
K='knowledge'
brands=[
 {"n":"Mizuno","c":"Japan","f":"1906","seg":"Mainstream","kf":"sports equipment","d":"Osaka sports company making IJF-approved judogi.","lines":["Yusho","Shiai","Keiko"],"eras":[],"sig":["Mizuno Yusho"],"sc":["judo"],"rel":[],"s":K},
 {"n":"adidas","c":"Germany","f":"1949","seg":"Mainstream","kf":"sportswear","d":"German sportswear company with an IJF-approved judogi range.","lines":["Champion","J350","J250"],"eras":[],"sig":["adidas Champion"],"sc":["judo"],"rel":[],"s":K},
 {"n":"Tokaido","c":"Japan","f":"1958","seg":"Heritage manufactory","kf":"karate uniforms","d":"Tokyo maker founded by Shizuo Sugiura as the first karate-uniform company, linked to the JKA.","lines":[],"eras":["Shizuo Sugiura, from 1958","Sugiura brothers"],"sig":["Tokaido karategi"],"sc":["karate","Shotokan"],"rel":["Shureido"],"s":"https://en.wikipedia.org/wiki/Tokaido_(company)"},
 {"n":"Shureido","c":"Japan","f":"","seg":"Heritage manufactory","kf":"karate uniforms","d":"Okinawan maker of heavyweight canvas karategi, favoured in Okinawan styles.","lines":["K-10","New Wave"],"eras":[],"sig":["Shureido K-10"],"sc":["karate","Okinawan karate"],"rel":["Tokaido"],"s":"https://www.martialtalk.com/threads/shureido-gi-question.140090/"},
 {"n":"Aramaki Workshop","c":"Japan","f":"","seg":"Artisan & independent","kf":"wooden practice weapons","d":"Traditional wooden-weapon workshop in Miyakonojō, Kyushu, run by master Aramaki Yasuo.","lines":["Kotobuki"],"eras":[],"sig":["Standard bokken"],"sc":["kendo","aikido"],"rel":[],"s":KB},
 {"n":"Minosaka","c":"Japan","f":"","seg":"Specialist","kf":"iaito","d":"Japanese iaito maker using a proprietary bubble-free alloy casting.","lines":["Tokusei","Jidai","Hon Koshirae"],"eras":[],"sig":["Minosaka iaito"],"sc":["iaidō"],"rel":[],"s":SG},
 {"n":"Nishinippon Budogu","c":"Japan","f":"","seg":"Specialist","kf":"shinai","d":"Kendo equipment maker producing bamboo shinai in-house from domestic bamboo.","lines":["Josui","Homare"],"eras":[],"sig":[],"sc":["kendo"],"rel":[],"s":"https://global.bushizo.com/collections/26"},
 {"n":"Tozando","c":"Japan","f":"","seg":"Specialist","kf":"budo equipment","d":"Kyoto shop selling Japanese swords and iaido practice swords.","lines":[],"eras":[],"sig":[],"sc":["kendo","iaidō"],"rel":[],"s":"https://www.insidekyoto.com/shop-tozando-northern-higashiyama"},
]
trads=[{"n":"Miyakonojō bokken making","g":"Woodwork & furniture","r":"Miyakonojō, Kyushu, Japan","p":"early 20th century – present","d":"Workshop tradition that formalised Japanese wooden-sword making; four workshops remain.","tech":"hand-shaping and oil-polishing hardwood swords","mat":"white oak, red oak, biwa, buna","forms":["Bokken"],"ctr":["Aramaki Workshop (Aramaki Yasuo)"],"auth":"","s":BK}]
notes=("Judo uniform renamed Martial arts uniform (judogi, karategi, BJJ gi, dobok and belts as t). All 5 old kinds kept; Iaito and Hakama added. "
 "Kusakura and Fuji Mae left out (no retrieved page). Kendo bogu kept at kind level with types; only the Maruyama set was named on a retrieved page. Wushu weapons as t from Wikipedia 'Sport wushu'. "
 "Mizuno, adidas founding facts from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/13_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
