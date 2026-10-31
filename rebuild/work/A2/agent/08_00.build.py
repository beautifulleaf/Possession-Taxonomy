import json, os
W='https://en.wikipedia.org/wiki/'
SC='https://theshoecareshop.com/blogs/articles/saphir-medaille-dor-vs-saphir-beaute-du-cuir-shoe-polish'
kinds=[
{"n":"Shoe polish and conditioner","a":"shoe polish · boot polish · shoe cream · shoe wax · blacking","d":"Wax, cream or conditioner that colours, feeds and shines leather shoes, or a spray that waterproofs them.",
 "t":["wax polish (tin)","cream polish","liquid polish","leather conditioner","mirror-gloss wax","waterproofing spray","dubbin"],
 "s":W+"Shoe_polish",
 "x":[
  {"n":"Kiwi tin polish","a":"Kiwi boot polish","d":"Wax boot polish in a flat round tin, first marketed in Melbourne and spread worldwide by First World War armies.","mk":"Kiwi","y":"1906","s":W+"Kiwi_(shoe_polish)",
   "v":[{"n":"Kiwi Dark Tan","mk":"Kiwi","y":"1908","d":"added conditioning and water-resistant agents"},{"n":"KIWI Shoe Polish","mk":"Kiwi","y":"","d":"current tin range"}],"dt":"colours · tin sizes"},
  {"n":"Renovateur","a":"Saphir Renovateur","d":"Saphir's beeswax and apricot-oil leather conditioner that cleans, nourishes and shines; awarded the Médaille d'Or in Paris in 1925.","mk":"Saphir","y":"1925","s":"https://au.saphir.com/products/renovateur",
   "v":[{"n":"Médaille d'Or Renovateur","mk":"Saphir","y":"","d":"premium line"},{"n":"Beauté du Cuir Renovateur","mk":"Saphir","y":"","d":"standard line"}],"dt":"50 ml and 250 ml jars · smooth fine leathers"},
  {"n":"Pâte de Luxe","a":"Saphir wax polish","d":"Saphir's beeswax-based hard wax polish used to build a high shine on toe caps.","mk":"Saphir","y":"","s":SC,
   "v":[{"n":"Médaille d'Or Pâte de Luxe","mk":"Saphir","y":"","d":"premium line with montan and carnauba waxes"},{"n":"Beauté du Cuir Pâte de Luxe","mk":"Saphir","y":"","d":"more affordable line"}],"dt":"colours · neutral · tin sizes"},
  {"n":"Pommadier cream","a":"Saphir shoe cream","d":"Saphir Médaille d'Or's nourishing coloured shoe cream with shea butter and mink oil.","mk":"Saphir","y":"","s":SC,
   "v":[{"n":"Crème Surfine","mk":"Saphir","y":"","d":"Beauté du Cuir counterpart with almond oil, no shea butter"}],"dt":"colours · 75 ml jar"}],
 "m":[["Mirror Gloss","Saphir"],["KIWI Instant Shine & Protect","Kiwi"],["KIWI Shoe Waterproofer Protector","Kiwi"],["Crep Protect spray","Crep Protect"]],
 "r":[["Médaille d'Or","Saphir"],["Beauté du Cuir","Saphir"],["KIWI shoe care","Kiwi"]]},
{"n":"Shoe cleaner","a":"sneaker cleaner · suede cleaner","d":"Liquid, foam or kit made to clean shoe uppers and soles, including suede and sneakers.",
 "t":["sneaker cleaning solution","suede and nubuck cleaner","foam cleaner","cleaning wipes","saddle soap"],
 "s":"https://kiwi-polish.com/",
 "x":[{"n":"Jason Markk Essential Kit","a":"","d":"Sneaker-care starter kit of a bottle of Premium Deep Cleaner and a firm-bristle brush, said to clean about 100 pairs.","mk":"Jason Markk","y":"","s":"https://sneakeressentials.nl/en/products/jason-markk-essential-kit",
   "v":[],"dt":"118 ml bottle · standard or premium brush"}],
 "m":[["KIWI Suede Shoe Cleaner","Kiwi"],["Crep Protect cleaner","Crep Protect"]]},
{"n":"Shoe brush","a":"shoe-shine brush · dauber · applicator brush","d":"Brush for applying polish, buffing to a shine or cleaning shoes.",
 "t":["horsehair shine brush","applicator (dauber)","boar-bristle brush","goat-hair finishing brush","synthetic scrub brush","crêpe suede brush"],
 "s":"https://www.theshoecareshop.com/pages/different-types-of-shoe-shine-brushes",
 "m":[["Médaille d'Or shine brush","Saphir"],["Médaille d'Or applicator brush","Saphir"],["Suede crêpe brush","Saphir"]]},
{"n":"Shoe-shine kit","a":"shoe-care valet · shoe-shine box","d":"Set of polishes, brushes and cloth, often in a wooden valet box.",
 "t":["wooden valet box","travel kit","starter kit"],
 "s":"https://kirbyallison.com/collections/shoe-care-shoeshine-kits/products/saphir-shoeshine-starter-kit",
 "x":[{"n":"Saphir shoe care valet","a":"","d":"Wooden valet with two horsehair applicators, two horsehair shine brushes, a cotton cloth, and one cream and one wax polish.","mk":"Saphir","y":"","s":"https://theshoecareshop.com/products/shoe-care-valet-saphir-walnut",
   "v":[{"n":"Saphir set","mk":"Saphir","y":"","d":"Crème Surfine and Pâte de Luxe"},{"n":"Médaille d'Or set","mk":"Saphir","y":"","d":"Pommadier cream and Pâte de Luxe"}],"dt":"walnut or burlwood · black or neutral polish"}],
 "m":[["Saphir Shoeshine Starter Kit","Kirby Allison"]]},
{"n":"Shoe tree","a":"shoe stretcher form · boot tree","d":"Form that holds a shoe in shape and absorbs moisture when it is not worn.",
 "t":["cedar","beech or lacquered wood","plastic or metal (travel)","boot tree"],
 "s":W+"Shoe_tree_(device)",
 "x":[
  {"n":"Lasted shoe tree","a":"bespoke tree","d":"Tree made on the same last as the shoes it accompanies; the highest grade.","mk":"","y":"","s":W+"Shoe_tree_(device)","v":[],"dt":"made per last · usually wood"},
  {"n":"Split-toe shoe tree","a":"single-tube tree","d":"Generic single-tube tree whose split toe is spread by a spring; most popular in the United States.","mk":"","y":"","s":W+"Shoe_tree_(device)",
   "v":[{"n":"Wellington Cedar Shoe Tree","mk":"Kirby Allison","y":"","d":"cedar"},{"n":"Sir Beecs Cedar Shoe Tree","mk":"Sir Beecs","y":"","d":"cedar"}],"dt":"cedar or other softwood · sizes"},
  {"n":"Twin-tube shoe tree","a":"","d":"Generic tree with two adjustable tubes; most popular in England and Europe.","mk":"","y":"","s":W+"Shoe_tree_(device)","v":[],"dt":"wood · sizes"},
  {"n":"Spring shoe tree","a":"","d":"Cheapest wooden tree with a heel knob on a spring rod instead of a full heel; often used for high heels.","mk":"","y":"","s":W+"Shoe_tree_(device)","v":[],"dt":"wood or plastic"}],
 "m":[["ULTRA Shoe Tree","Kirby Allison"],["Wellington Balmoral Cedar Boot Tree","Kirby Allison"]]},
{"n":"Shoe horn","a":"shoehorn · chausse-pied","d":"Curved tool that helps the heel slide into a shoe.",
 "t":["horn","metal","wood","plastic","long-handled","travel"],
 "s":W+"Shoehorn",
 "x":[
  {"n":"Tip End shoe horn","a":"","d":"Abbeyhorn's hand-made natural cow-horn shoehorn that tapers from a wide end to a pointed tip.","mk":"Abbeyhorn","y":"","s":"https://doublemonk.com/products/tip-end-shoe-horn-24",
   "v":[{"n":"24-inch","mk":"Abbeyhorn","y":"","d":"long-handled"}],"dt":"lengths · horn colour and pattern vary"},
  {"n":"Mindum engraved shoehorn","a":"","d":"English horn shoehorns signed and dated by Robert Mindum, engraved with owners' names and heraldic, geometric and floral designs.","mk":"","y":"1593–1613","s":W+"Shoehorn","v":[],"dt":"antique · horn · engraved"}],
 "m":[["Médaille d'Or natural horn shoe horn","Saphir"]]}]
brands=[
{"n":"Kiwi","c":"Australia","f":"1906","seg":"Mass-market shoe care","d":"Shoe polish brand founded in Melbourne by William Ramsay and Hamilton McKellar; owned by S. C. Johnson since 2011.","lines":["KIWI shoe care"],"eras":["Sara Lee, 1984–2011","S. C. Johnson, 2011–"],"sig":["Kiwi tin polish"],"sc":[],"rel":[],"s":W+"Kiwi_(shoe_polish)"},
{"n":"Saphir","c":"France","f":"","seg":"Premium shoe care","d":"French leather-care maker, part of the Avel group; its Renovateur won the Médaille d'Or in Paris in 1925.","lines":["Médaille d'Or","Beauté du Cuir"],"eras":[],"sig":["Renovateur","Pâte de Luxe","Pommadier cream"],"sc":[],"rel":[],"s":"https://au.saphir.com/products/renovateur"},
{"n":"Abbeyhorn","c":"United Kingdom","f":"1749","seg":"Horn goods","d":"Horn works founded in Bewdley by the Humpherson family, now in Kendal, making hand-made horn shoehorns.","lines":[],"eras":[],"sig":["Tip End shoe horn"],"sc":[],"rel":[],"s":"https://doublemonk.com/products/tip-end-shoe-horn-24"},
{"n":"Jason Markk","c":"United States","f":"2007","seg":"Sneaker care","d":"Los Angeles sneaker-care brand of cleaners, kits and repellents.","lines":[],"eras":[],"sig":["Jason Markk Essential Kit"],"sc":[],"rel":["Crep Protect"],"s":"knowledge"},
{"n":"Crep Protect","c":"United Kingdom","f":"2012","seg":"Sneaker care","d":"UK sneaker-care brand founded by the brothers Imran, Nohman and Rizwan Ahmed, known for its protector spray.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Jason Markk"],"s":"https://insideretail.co.nz/2023/09/05/from-nanotech-to-sneakers-how-crep-protect-is-disrupting-footwear-care/"}]
notes=("Kept all four old kinds (polish renamed 'Shoe polish and conditioner'); added Shoe brush and Shoe-shine kit. Saphir maker names unified as 'Saphir' (lines Médaille d'Or / Beauté du Cuir). "
 "Left out for lack of a retrieved page: Collonil, Tarrago, Boot Black, Famaco, Lincoln, Venetian Shoe Cream, Reshoevn8r, lasted trees by C&J/Edward Green/Saphir/Woodlore; Jason Markk founding facts from knowledge. "
 "Blocked fetches: solefeed.com and toddsnyder.com (403), lemilemagazine (404). Insoles, laces etc. belong to the sibling shelf.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/A2/shelves/08_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
