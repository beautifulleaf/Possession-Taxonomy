from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
FS=W+"Fish_sauce"
kinds=[
{"n":"Fish sauce","a":"nuoc mam · nam pla · patis","d":"The liquid drawn from salted, fermented fish, graded by nitrogen content (°N).","t":["Vietnamese nước mắm","Thai nam pla","Filipino patis","first-press","high °N (30+)"],"s":FS,"m":[["Red Boat Fish Sauce","Red Boat"],["Three Crabs Fish Sauce","3 Crabs"],["Megachef Fish Sauce","Mega Chef"]],
 "x":[
 X("Phú Quốc fish sauce","Phu Quoc nước mắm","Vietnamese anchovy sauce from Phú Quốc island, EU Protected Designation of Origin in 2012, the first from Southeast Asia.",W+"Phu_Quoc_fish_sauce",[V("Red Boat Fish Sauce","Red Boat","2011","Black anchovies and sea salt only, first pressings; sold from 2011")],"anchovy · wooden barrels",y="PDO 2012"),
 X("Phan Thiết fish sauce","","Sauce from Phan Thiết, identified in the article as the birthplace of Vietnamese fish sauce, with a fish sauce museum.",FS,[V("Hòn Phan Thiết","","","Popular US brand named in the article")],"anchovy"),
 X("Colatura di alici di Cetara","colatura","Clear amber anchovy sauce from Cetara on the Amalfi Coast, fermented in chestnut barrels, PDO in 2020; Italian relative of Roman garum.",W+"Colatura_di_alici",[],"salted anchovies · terzigni barrels",y="PDO 2020"),
 ]},
{"n":"Oyster sauce and hoisin sauce","a":"","d":"Thick dark Chinese cooking sauces of oyster extract or of fermented soybeans.","t":["oyster sauce","hoisin (haixian) sauce","vegetarian oyster-flavour"],"s":W+"Lee_Kum_Kee","m":[["Kikkoman Hoisin Sauce","Kikkoman"],["Lee Kum Kee Premium Oyster Flavored Sauce","Lee Kum Kee"]],
 "x":[X("Lee Kum Kee oyster sauce","","Hong Kong company's Cantonese oyster sauce, marketed from 1888 in Guangdong by Lee Kum Sheung.",W+"Lee_Kum_Kee",[V("Premium Oyster Flavored Sauce","Lee Kum Kee")],"oyster extract",mk="Lee Kum Kee",y="1888")]},
{"n":"Doubanjiang","a":"broad-bean chilli paste","d":"A fermented paste of broad beans and chilli used to season.","t":["Pixian","plain","with oil"],"s":W+"Doubanjiang","m":[["Lintao Pixian Chili Bean Sauce","Lintao Pixian"]],
 "x":[X("Pixian doubanjiang","Pixian chilli bean paste","Sichuan broad-bean chilli paste from Pixian (now Pidu, Chengdu), a protected GI, fermented for months to over three years.",W+"Doubanjiang",[V("Premium"),V("Grade I"),V("Grade II")],"broad beans · erjingtiao chilli · sun-fermented",y="GI")]},
{"n":"Black bean sauce and douchi","a":"fermented black beans","d":"Salted fermented black soybeans (douchi) and the sauce made from them with garlic and soy sauce.","t":["whole douchi","black bean sauce","with garlic"],"s":W+"Douchi"},
{"n":"Shaoxing and Chinese cooking wine","a":"Shaoxing wine · huangjiu","d":"Rice wine made or sold for cooking, notably Shaoxing huangjiu; cooking grades often carry added salt.","t":["Shaoxing huangjiu","cooking grade (salted)","drinking grade"],"s":W+"Shaoxing_wine","m":[["Shaoxing cooking wine",""]]},
{"n":"Fermented bean curd","a":"furu · sufu","d":"Tofu cubes fermented in brine, white, red (with red yeast rice) or stinky.","t":["white","red (nam yu)","stinky","spicy","drunken"],"s":W+"Fermented_bean_curd","m":[["Wangzhihe Fermented Spicy Bean Curd","Wang Zhi He"]]},
{"n":"XO sauce","a":"","d":"Hong Kong relish of dried scallop, chilli, Jinhua ham, dried shrimp and garlic in oil, developed in the 1980s.","t":["seafood","chilli"],"s":W+"XO_sauce","m":[]},
{"n":"Shrimp paste","a":"belacan · terasi · kapi · bagoong","d":"Fermented paste of tiny Acetes shrimp from Malaysia (belacan), Indonesia (terasi), Thailand (kapi) and the Philippines (bagoong).","t":["belacan (pressed cakes)","terasi (blocks or powder)","kapi (Thai)","bagoong alamang (Filipino)"],"s":W+"Shrimp_paste","m":[]},
{"n":"Kecap manis","a":"sweet soy sauce","d":"Thick Indonesian soy sauce sweetened with up to 50% palm sugar and often spiced with star anise or clove.","t":["ABC","Bango"],"s":W+"Sweet_soy_sauce","m":[["Kecap Manis ABC","ABC"],["Kecap Bango","Bango"]]},
{"n":"Tamarind paste","a":"","d":"Sour paste or concentrate of tamarind pulp used in curries, chutneys, sauces and drinks.","t":["paste","concentrate","block pulp"],"s":W+"Tamarind","m":[]},
]
brands=[
B("Red Boat","Vietnam","2006","fish sauce","Phú Quốc fish sauce brand; founder Cuong Pham bought a family operation in 2006 and incorporated Viet Phu in California in 2011.",W+"Red_Boat",seg="Premium",sig=["Red Boat Fish Sauce"]),
B("Lee Kum Kee","China","1888","oyster sauce","Hong Kong sauce maker with over 300 products, founded by Lee Kum Sheung in 1888.",W+"Lee_Kum_Kee",sig=["Premium Oyster Flavored Sauce"]),
B("Wangzhihe","China","1669","fermented bean curd","Beijing condiment maker and China Time-honored Brand, known for fermented bean curd.",W+"Wangzhihe",seg="Heritage manufactory"),
]
notes="Squid brand not found on retrieved pages (omitted); Megachef/3 Crabs/Hòn Phan Thiết named by Fish sauce page. Yangjiang douchi, Juan Cheng doubanjiang not found. Brand register covers Red Boat, Lee Kum Kee, Wangzhihe. Kikkoman hoisin kept from old data. No traditions added."
write("05_03",kinds,brands,[],notes)
