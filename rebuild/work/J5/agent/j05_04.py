from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
kinds=[
{"n":"Tomato pasta sauces","a":"","d":"Tomato-based sauces for pasta, in jars, with or without meat.","t":["marinara","arrabbiata","with meat","passata-based"],"s":W+"Marinara_sauce","m":[["Carbone Marinara","Carbone"],["Mezzetta Marinara","Mezzetta"],["Rao's Marinara","Rao's"],["Mutti Salse Pronte","Mutti"],["Dolmio Pasta Sauce","Dolmio"]]},
{"n":"Pesto","a":"","d":"A paste of basil or other herbs with oil and nuts or cheese, jarred or chilled.","t":["Genovese (basil, pine nut)","rosso/trapanese (tomato, almond)","vegan"],"s":W+"Pesto","m":[["Gran Cucina Pesto alla Genovese DOP","Gran Cucina"]],
 "x":[X("Pesto alla Genovese","Genoese pesto","Basil, coarse salt, garlic, Ligurian olive oil, pine nuts and Parmesan or Grana Padano with pecorino; the DOP protects the Genovese basil, not the sauce.",W+"Pesto",[V("Pesto alla Genovese with Basilico Genovese DOP","","","DOP basil from Liguria, recognised 2005, consortium 2008")],"Genovese basil · pine nuts · cheese",y="basil DOP 2005"),
      X("Basilico Genovese DOP","Genovese basil","The Ligurian basil cultivar with Protected Designation of Origin, grown on the maritime slope of Liguria.",W+"Genovese_basil",[],"Genoa, Imperia, Savona",y="DOP"),
      X("Pesto alla siciliana","pesto rosso · trapanese","Sicilian pesto with fresh tomato and almonds and much less basil.",W+"Pesto",[],"tomato · almond")]},
{"n":"Curry paste","a":"","d":"Paste of chillies, aromatics and spices sold to start a curry.","t":["Thai red","Thai green","Thai yellow","Indian","Massaman"],"s":W+"Curry_paste","m":[["Patak's Curry Paste","Patak's"]]},
{"n":"Jarred cooking sauces","a":"simmer sauces · stir-fry sauces","d":"Ready-made curry, stir-fry and simmer sauces in jars, pouches or cans.","t":["curry sauce","stir-fry sauce","simmer sauce","single-serve pouch"],"s":W+"Loyd_Grossman_sauces","m":[["Loyd Grossman Cooking Sauces","Loyd Grossman"]]},
{"n":"Stock cubes and bouillon","a":"","d":"Cubes, powders, pastes and liquids for making stock, from any source.","t":["cube","granules","paste","liquid concentrate"],"s":W+"Bouillon_cube","m":[["Better Than Bouillon Premium Roasted Chicken Base","Better Than Bouillon"],["Knorr Shelf Stable Cubes Chicken Bouillon","Knorr"],["Maggi Chicken Flavor Bouillon Tablets","Maggi"],["Oxo Cubes","Oxo"]]},
{"n":"Gravy granules","a":"instant gravy","d":"Dissolvable powder or granules that make gravy with hot water, first sold by Bisto in 1908.","t":["beef","chicken","vegetable","gluten-free"],"s":W+"Gravy","m":[["Bisto Gravy Granules","Bisto"]]},
{"n":"Liquid seasonings","a":"","d":"Dark savoury seasoning sauces and powders added by the dash, such as Maggi Seasoning and Aromat.","t":["hydrolysed-protein sauce","soy-based aminos","all-purpose powder"],"s":W+"Maggi","m":[["Maggi Seasoning","Maggi"],["Aromat","Knorr"]]},
]
brands=[
B("Rao's","United States","1896","pasta sauce","New York Italian-American restaurant (1896) that has sold jarred sauces since 1992.",W+"Rao's",seg="Premium",sig=["Rao's Marinara"]),
B("Mutti","Italy","1899","tomato products","Family tomato company from Montechiarugolo, Parma; passata, paste, peeled tomatoes and ready sauces.",W+"Mutti_(company)",sig=["Salse Pronte"]),
B("Dolmio","Australia","1985","pasta sauce","Mars pasta sauce brand, sold as Alora in Australia in 1985 and named Dolmio worldwide in 1989.",W+"Dolmio"),
B("Patak's","United Kingdom","1957","curry pastes","Brand started by Shanta and Lakshmishanker Pathak; owned by Associated British Foods since 2007.",W+"Patak's"),
B("Loyd Grossman","United Kingdom","1995","cooking sauces","Premier Foods cooking sauce brand made with the TV personality.",W+"Loyd_Grossman_sauces"),
B("Knorr","Germany","1838","stock cubes","Heilbronn food company founded by Carl Heinrich Theodor Knorr; bouillon cubes from 1912; Aromat developed for its Swiss branch in 1952.",W+"Knorr_(brand)"),
B("Maggi","Switzerland","1869","seasoning sauce","Julius Maggi's firm; bouillon cubes 1908, Maggi seasoning 1886; owned by Nestlé.",W+"Maggi",sig=["Maggi Seasoning"]),
B("Oxo","United Kingdom","1899","stock cubes","Beef stock brand with trademark from 1899 and first cubes in 1910; owned by Premier Foods in the UK.",W+"Oxo_(food)"),
B("Bisto","United Kingdom","1908","gravy","UK gravy brand launched in 1908; granules from 1979; owned by Premier Foods.",W+"Bisto"),
]
notes="Better Than Bouillon, Mae Ploy, Bragg not found on retrieved pages (Better Than Bouillon kept only from old data; no register entry). Mutti, Dolmio, Oxo, Bisto models added from retrieved brand pages. Pesto DOP covers the basil only, recorded as such. No test winners retrieved."
write("05_04",kinds,brands,[],notes)
