import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
O="https://www.babeland.com/sex-toys/c/3000/vibrators/"
kinds=[
{"n":"Rabbit vibrator","a":"dual-action vibrator","d":"Insertable vibrator with an external arm that stimulates the clitoris at the same time.","t":["Rotating shaft","Thrusting","App-controlled"],"m":[["Rabbit Pearl","Vibratex"],["Rampant Rabbit","Ann Summers"],["Jack Rabbit","CPLC"]],"r":[["Rabbit Pearl line","Vibratex"]],"s":O},
{"n":"Insertable vibrator","a":"G-spot vibrator · realistic vibrator","d":"Vibrator made to be inserted, with a curved or straight shaft; a curved tip reaches the front vaginal wall.","t":["G-spot curve","Straight classic","Realistic shaft","Silicone"],"m":[["Arc G-Spot Vibrator","Dame"]],"s":O},
{"n":"Couples vibrator","a":"","d":"Vibrator made to be worn or used by two partners at once during intercourse.","t":["Wearable C-shape","Remote control","App control"],"m":[["We-Vibe 4 Plus","We-Vibe"]],"s":O},
{"n":"Egg vibrator","a":"love egg · 跳蛋","d":"Small egg-shaped insertable vibrator, wired or wireless; it may be worn.","t":["Wired","Wireless remote","App-controlled"],"m":[["Ella Neo","SVAKOM"],["Jive 2","We-Vibe"]],"s":"https://www.orion.de/katalog/sextoys/vibro-eier"},
{"n":"Anal vibrator","a":"","d":"Vibrating anal insertable with a flared base that is not a prostate massager.","t":["Flared base","Plug-shaped","Wireless"],"s":"https://www.orion.de/katalog/sextoys/anal-toys"},
{"n":"Glans vibrator","a":"","d":"Vibrating device that holds or wraps the head of the penis.","t":["Hands-free","Handheld"],"s":"https://www.orion.de/katalog/sextoys/masturbatoren"},
]
brands=[
 {"n":"Ann Summers","c":"United Kingdom","f":"","seg":"Own-label & retailer","kf":"party retail","d":"UK party and retail company whose Rampant Rabbit followed the original dual-action design.","s":U+"Rabbit_vibrator"},
]
put('H3','00_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Adam & Eve (Siren's Embrace) and The One (Rabbit, Thrusting Rabbit, G-Spot Vibe) padding dropped. Realistic vibrator merged into Insertable vibrator as a type; G-spot vibrator is the other type. Rabbit models from the Rabbit vibrator page (Rabbit Pearl 1984 Vibratex, Rampant Rabbit, Jack Rabbit). We-Vibe 4 Plus is the 2014 app-connected couples model per the We-Vibe page. Lovense, LELO, Satisfyer entries are in the first shelf. No models for anal or glans vibrators: none retrieved. Neutral wording."})
