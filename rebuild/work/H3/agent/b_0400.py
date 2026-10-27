import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
M="https://www.orion.de/katalog/sextoys/masturbatoren"; P="https://www.orion.de/katalog/sextoys/penisringe"
kinds=[
{"n":"Handheld masturbator","a":"onahole · オナホール · 飛機杯 · stroker","d":"Reusable sleeve with an inner channel, held in the hand. Weight, inner texture and the opening it imitates vary.","t":["Reusable, splits open for washing","Sleeve in a case","Textured channel"],"m":[["FLIP 360","TENGA"],["FLIP FLEXY","TENGA"],["POCKET TENGA","TENGA"],["Fleshlight sleeve","Fleshlight"]],"r":[["FLIP","TENGA"]],"s":M},
{"n":"Disposable masturbator","a":"single-use sleeve","d":"Single-use sleeve in a closed shell, made to be used once and thrown away.","t":["Cup","Egg"],"m":[["Egg Gear","TENGA"]],"s":"https://www.yohohongkong.com/en-us/product/155134-Tenga-Egg-Gear-Masturbator-single-use"},
{"n":"Penis ring","a":"cock ring · 鎖精環 · 持久環 · Penisringe","d":"Ring worn at the base of the penis, or the penis and testicles, to keep an erection. Some vibrate.","t":["Silicone","Steel","Adjustable","Vibrating","Scrotum strap","Triple ring"],"s":P},
{"n":"Penis sleeve","a":"extension","d":"Open sleeve worn over the penis to add length, girth or texture.","t":["Silicone","Textured"],"s":P},
]
brands=[
 {"n":"Doc Johnson","c":"United States","f":"1976","seg":"Mainstream","kf":"novelty and sexual health","d":"North Hollywood company founded by Reuben Sturman, with its own factory.","s":U+"Doc_Johnson"},
]
put('H3','04_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Scrotum strap merged into Penis ring as a type; vibrating ring a type. TENGA FLIP, Egg and Cup lines kept (Wikipedia page confirms Cup and Egg are disposable, Flip reusable and splits open). Fleshlight added as a leader. Oxballs, LELO Tor, Lovehoney and Fun Factory rings not on a retrieved page for rings, so no models. Cock ring page gave purpose and risk notes only. Neutral wording."})
