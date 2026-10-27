from lib import *
def B(n,c,f,kf,d,s,seg="Heritage manufactory",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
SS=W+"Soy_sauce"
kinds=[
{"n":"Soy sauce","a":"shoyu","d":"Japanese soy sauces that differ by colour, saltiness, wheat share and brewing.","t":["Koikuchi soy sauce","Usukuchi soy sauce","Tamari soy sauce","Saishikomi soy sauce","Shiro soy sauce","organic","namashoyu (unpasteurised)"],"s":SS,
 "m":[["Yamaki Jozo Organic Shoyu","Yamaki Jozo"],["Yugeta Organic Shoyu","Yugeta Shoyu"],["Yamaroku Tsuru-bishio","Yamaroku Shoyu"]],
 "x":[
 X("Koikuchi shoyu","dark soy sauce","The standard Japanese soy sauce, roughly equal soybean and wheat, over 80% of domestic output and from the Kantō region.",SS,[V("Kikkoman","Kikkoman","1917","World's largest shoyu maker, Noda"),V("Yamasa","Yamasa","1645","Choshi, Chiba")],"soybean ≈ wheat"),
 X("Usukuchi shoyu","light soy sauce","Lighter-coloured and saltier shoyu made with amazake, popular in Kansai, about 14% of output.",SS,[V("Higashimaru Usukuchi Shoyu","Higashimaru","","Old-data product")],"light colour"),
 X("Tamari","","Little or no wheat; darker, richer and more viscous, mainly made in Chūbu; wheat-free versions suit gluten avoiders.",SS,[V("San-J Organic Tamari","San-J")],"wheat-free options"),
 X("Saishikomi shoyu","twice-brewed · kanro shoyu","Made with finished koikuchi in place of brine, giving a darker, stronger sauce; about 0.8% of output.",SS,[V("Suehiro Double Brewed Sashimi Soy Sauce","Suehiro Shoyu"),V("Yugeta Double Brewed Shoyu","Yugeta Shoyu")],"double brewed"),
 X("Shiro shoyu","white soy sauce","Mostly wheat with little soybean, pale and sweet, used in Kansai mainly for pickles; about 0.7% of output.",SS,[V("Nitto Jozo White Shiro Tamari","Nitto Jozo")],"pale"),
 ]},
{"n":"Miso and soybean pastes","a":"fermented soybean paste","d":"Fermented soybean paste with or without grain, in Japanese miso and Korean doenjang styles.","t":["rice miso","barley miso","soybean miso","white","red"],"s":W+"Miso","m":[["Chung Jung One Doenjang","Chung Jung One"]],
 "x":[
 X("Hatchō miso","mame miso","Dark grain-free soybean miso from Okazaki, Aichi, with a long maturing time and an astringent, umami flavour.",W+"Miso",[],"soybean only · long aged"),
 X("Shiro miso","white miso","The most widely produced miso, mostly rice and barley with a little soybean, short-fermented, sweet and mild.",W+"Miso",[],"rice koji · short ferment"),
 X("Shinshu miso","Shinshu kome miso","Rice (kome) miso, the common type in eastern Japan and Hokuriku; Shinshu is a named example.",W+"Miso",[],"rice koji"),
 X("Mugi miso","barley miso","Whitish barley miso from Kyushu, western Chūgoku and Shikoku, with a distinctive smell; a reddish version comes from northern Kantō.",W+"Miso",[],"barley koji"),
 X("Sendai miso","","Miso whose soybeans are mashed much more coarsely than in standard soy miso.",W+"Miso",[],"coarse"),
 X("Doenjang","Korean soybean paste","Korean paste mashed from meju bricks after the brine is drawn off as ganjang soy sauce.",W+"Meju",[V("Chung Jung One Doenjang","Chung Jung One")],"meju-based"),
 ]},
{"n":"Gochujang","a":"fermented chilli paste","d":"A fermented paste of chilli, glutinous rice and soybeans used to season.","t":["traditional jar-aged","industrial"],"s":W+"Gochujang","m":[["Sempio Gochujang","Sempio"]],
 "x":[X("Sunchang gochujang","","Regional gochujang from Sunchang County, noted in 18th-century texts and linked to Joseon palace cuisine.",W+"Gochujang",[],"red chilli powder · glutinous rice · meju powder · salt")]},
{"n":"Mirin","a":"","d":"Sweet rice seasoning sold for cooking, hon-mirin and mirin-style seasoning.","t":["hon-mirin (about 14% alcohol)","shio mirin (salted)","mirin-fu seasoning (under 1% alcohol)"],"s":W+"Mirin","m":[["Takara Hon Mirin","Takara (mirin brand)"]]},
{"n":"Cooking sake","a":"ryorishu","d":"Sake made or sold for cooking.","t":["salted","unsalted"],"s":"https://japanesetaste.com/blogs/japanese-taste-blog/all-you-need-to-know-about-cooking-sake-ryorishu","m":[["Fukumitsuya Organic Cooking Sake","Fukumitsuya"],["Morita Ryorishu Cooking Sake","Morita"],["Takara Cooking Sake","Takara (mirin brand)"]]},
{"n":"Dashi and dashi ingredients","a":"","d":"Japanese stock and its ingredients: kombu, katsuobushi, niboshi and instant dashi.","t":["instant granules","liquid"],"s":W+"Dashi",
 "x":[
 X("Kombu","konbu kelp","Dried kelp for dashi, sold by origin: Ma (Hakodate, mild and sweet), Rishiri (clean, for kaiseki), Rausu (rich), Hidaka (mild, cheapest).","https://chefjacooks.com/en/types-of-kombu",[V("Ma kombu","","","Most produced; Hakodate"),V("Rishiri kombu","","","Rishiri Island, northern Hokkaido"),V("Rausu kombu","","","Premium, rich dashi"),V("Hidaka kombu","","","Long ribbons, most affordable")],"origin · thickness"),
 X("Katsuobushi","bonito flakes","Skipjack tuna simmered, smoked and mould-cured; graded arabushi, katsuobushi, karebushi and honkarebushi by repeated curing.",W+"Katsuobushi",[V("Arabushi"),V("Karebushi"),V("Honkarebushi")],"shaved or block"),
 X("Niboshi","iriko","Small dried fish, mostly anchovies, for a strong dashi; heads and entrails removed to avoid bitterness.",W+"Niboshi",[],"anchovy · sardine"),
 ]},
{"n":"Ponzu and tsuyu","a":"mentsuyu","d":"Citrus-and-soy ponzu and dashi-based noodle tsuyu dipping sauces.","t":["ponzu shoyu","mentsuyu (noodle sauce)","concentrate"],"s":W+"List_of_Japanese_condiments"},
{"n":"Furikake","a":"","d":"Dry seasoning sprinkled over rice: dried fish, sesame, seaweed, sugar, salt and often egg, shiso or salmon.","t":["salmon","egg","shiso","nori"],"s":W+"List_of_Japanese_condiments"},
]
brands=[
B("Kikkoman","Japan","1917","soy sauce","Noda, Chiba soy sauce maker formed from eight family firms in 1917; world's largest shoyu producer.",W+"Kikkoman",seg="Mainstream",sig=["Kikkoman koikuchi"]),
B("Yamasa","Japan","1645","soy sauce","Choshi, Chiba soy sauce and seasoning maker.",W+"Yamasa"),
B("Yamaroku Shoyu","Japan","","kioke soy sauce","Shodoshima brewery of fifth-generation Yasuo Yamamoto, brewing in self-made kioke barrels; flagship Tsuru-bishio.","https://www.japan.travel/en/uk/inspiration/one-man-and-his-barrels-yasuo-yamamoto-and-his-mission-to-keep-real-soy-sauce-alive/",seg="Artisan & independent",sig=["Tsuru-bishio"]),
]
trads=[
{"n":"Shōyu brewing of Yuasa","g":"Food & drink","r":"Yuasa, Wakayama, Japan","p":"Edo period onward","d":"Yuasa claims to be the birthplace of Japanese soy sauce, with a soy sauce industry flourishing since the Edo period.","tech":"koji fermentation of soybean and wheat with brine, pressed and aged","mat":"soybean, wheat, salt","forms":["koikuchi shoyu"],"ctr":["Yuasa"],"auth":"Claim of origin is local and not settled","s":"https://en.wikipedia.org/wiki/Yuasa,_Wakayama"},
{"n":"Shōdoshima kioke soy sauce brewing","g":"Food & drink","r":"Shōdoshima, Kagawa, Japan","p":"traditional, about 150 years at Yamaroku","d":"Natural brewing of soy sauce in handmade cedar-and-bamboo kioke barrels, about 1% of Japan's soy sauce.","tech":"Tennen Jōzō Kioke Shikomi: natural wooden-barrel fermentation","mat":"cedar and bamboo barrels, soybean, wheat, salt","forms":["Tsuru-bishio"],"ctr":["Yamaroku Shoyu"],"auth":"Brewed in kioke barrels; barrels can last over 100 years","s":"https://www.japan.travel/en/uk/inspiration/one-man-and-his-barrels-yasuo-yamamoto-and-his-mission-to-keep-real-soy-sauce-alive/"},
{"n":"Korean jang-making","g":"Food & drink","r":"Korea","p":"UNESCO inscribed 2024","d":"Making, keeping and eating jang, the fermented sauces including soybean paste, soy sauce and red chilli paste.","tech":"meju bricks fermented, brine drawn as ganjang, remainder mashed as doenjang","mat":"soybeans, salt, chilli, glutinous rice","forms":["doenjang","ganjang","gochujang"],"ctr":["Sunchang"],"auth":"Family transmission, mother to daughter, in earthenware jars","s":"https://ich.unesco.org/en/RL/knowledge-beliefs-and-practices-related-to-jang-making-in-the-republic-of-korea-01975?RL=01975"},
]
notes="Marukin, Yamasa products, San-J and Higashimaru kept as version names from old data only; Saikyo miso not found on retrieved pages and left out. Rishiri/Rausu/Ma from chefjacooks page. Cooking sake keeps the old source (current blog URL 404). Hondashi not confirmed so omitted. Ponzu and furikake sourced to the List of Japanese condiments."
write("05_02",kinds,brands,trads,notes)
