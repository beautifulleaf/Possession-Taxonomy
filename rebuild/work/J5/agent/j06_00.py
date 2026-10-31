from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
SM=W+"San_Marzano_tomato"
kinds=[
{"n":"Tinned tomatoes","a":"canned tomatoes","d":"Peeled tomatoes tinned whole or chopped; the variants differ only by the cut.","t":["Whole peeled tomatoes","Chopped tomatoes"],"s":SM,"m":[["Cento Certified San Marzano Whole Peeled Tomatoes","Cento Fine Foods"],["Mutti Polpa Finely Chopped Tomatoes","Mutti"]],
 "x":[X("San Marzano dell'Agro Sarnese-Nocerino DOP","San Marzano tomatoes","PDO plum tomato grown in the Sarno Valley near Naples; canned fruit may use the PDO name and EU emblem.",SM,[],"whole peeled in tin",y="PDO"),
      X("Pomodorino del Piennolo del Vesuvio DOP","Piennolo","PDO grape tomato from 18 municipalities around Vesuvius, PDO granted 2009, stored in hung clusters.",W+"Pomodorino_del_Piennolo_del_Vesuvio",[],"winter tomato",y="PDO 2009")]},
{"n":"Tomato purée and paste","a":"","d":"Concentrated tomato purée or paste; paste is thicker, often sold double-strength in tubes.","t":["paste","purée","double concentrate tube"],"s":W+"Tomato_paste","m":[["Mutti Double Concentrate Tomato Paste Tube","Mutti"]]},
{"n":"Passata","a":"","d":"Sieved raw tomato pulp, strained of seeds and skins, heat-processed in the pack.","t":["smooth","with basil","rustic"],"s":W+"Tomato_pur%C3%A9e","m":[["Mutti Tomato Passata","Mutti"]]},
{"n":"Tinned beans and pulses","a":"canned beans","d":"Pre-cooked beans and pulses packed in water, salt or sauce, including baked beans.","t":["plain in brine","no salt added","pork and beans"],"s":W+"Canned_beans","m":[],
 "x":[X("Baked beans in tomato sauce","Heinz Beanz","Canned haricot beans in tomato sauce, steamed rather than baked; Heinz sold them from 1895 and in the UK from 1901.",W+"Heinz_Baked_Beans",[V("Heinz Baked Beans","Heinz","1895","Sold as Heinz Beanz in the UK; produced in Harlesden since 1928")],"haricot beans · tomato sauce",mk="Heinz",y="1895"),
      X("New England baked beans","Boston baked beans","US canned style sweetened with maple syrup or molasses, traditionally cooked with salt pork.",W+"Baked_beans",[],"sweet")]},
{"n":"Tinned soup","a":"canned soup","d":"Condensed soup that needs water or ready-to-eat single-strength soup in a can.","t":["condensed","ready-to-eat"],"s":W+"Instant_soup","m":[["Campbell's Condensed Soup","Campbell's"]],
 "x":[X("Campbell's condensed soup","","Concentrated canned soup developed by John T. Dorrance in 1899 to cut shipping weight.",W+"John_Thompson_Dorrance",[V("Condensed tomato","Campbell's")],"dilute with water",mk="Campbell's",y="1899")]},
{"n":"Tinned sweetcorn","a":"canned corn","d":"Sweetcorn kernels, heat-processed in the pack.","t":["whole kernel","creamed","no salt added"],"s":W+"Sweet_corn","m":[["Del Monte Golden Sweet Whole Kernel Corn","Del Monte"],["Green Giant Whole Kernel Sweet Corn","Green Giant"]]},
{"n":"Tinned vegetables","a":"canned vegetables","d":"Peas, green beans, carrots and other vegetables heat-processed in a can.","t":["peas","green beans","carrots","mixed"],"s":W+"Green_Giant","m":[["Green Giant Canned Vegetables","Green Giant"],["Del Monte Canned Vegetables","Del Monte"]]},
{"n":"Tinned fruit","a":"canned fruit","d":"Fruit in syrup or juice, such as peaches, pears, pineapple and fruit cocktail.","t":["in syrup","in juice","fruit cocktail","fruit salad"],"s":W+"Fruit_salad","m":[["Del Monte Canned Peaches","Del Monte"]]},
{"n":"Coconut milk and cream","a":"","d":"Pressed milk or cream of coconut flesh, sold in a tin or carton for cooking; coconut drinks are in Dairy, Eggs & Alternatives.","t":["milk","cream (about 4:1 coconut to water)","light"],"s":W+"Coconut_cream","m":[["Chaokoh Coconut Milk","Chaokoh"]]},
]
brands=[
B("Campbell's","United States","1869","condensed soup","Joseph Campbell Preserve Company, renamed Campbell's Soup Company in 1921; condensed soup from 1899.",W+"John_Thompson_Dorrance"),
B("Del Monte","United States","1892","canned fruit and vegetables","California canning brand; the Del Monte name was chosen in 1892 for canned peaches.",W+"Del_Monte_Foods"),
B("Green Giant","United States","1903","canned peas and corn","Minnesota Valley Canning Company brand; Green Giant name from 1925; now owned by Seneca Foods.",W+"Green_Giant"),
]
brands[0]["f"]=""
notes="Cento, La Valle and Chaokoh kept from old data only (no retrieved page); Campbell's founding year not confirmed so left blank. Heinz is registered on shelf 05_00. Tinned vegetables, fruit and soup models are brand-level (Green Giant, Del Monte, Campbell's) from retrieved company pages, not SKUs."
write("06_00",kinds,brands,[],notes)
