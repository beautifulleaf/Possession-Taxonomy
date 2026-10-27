import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from h import v,x,B,W
w=lambda t:'https://en.wikipedia.org/wiki/'+t
OK=w('Okinawan_kobud%C5%8D'); GU=w('Gun_(staff)'); QS=w('Quarterstaff'); JO=w('Jo_(weapon)'); BS=w('Baston_(weapon)'); NU=w('Nunchaku'); TF=w('Tonfa')
SA=w('Sai_(weapon)'); KM=w('Kama_(weapon)'); TS=w('Three-section_staff'); RD=w('Rope_dart'); CW=w('Chain_whip')
kinds=[
{"n":"Staff","a":"bō · gùn · kon · quarterstaff","d":"Long wooden staff, about the user's height or more, used as a weapon and in martial arts training.",
 "t":["bō","gùn","quarterstaff","hanbō (short)","tapered","non-tapered","wood","rattan","carbon fibre (competition)"],"s":"https://www.battlemerchant.com/en/training-staff-polypropylen",
 "x":[x("Rokushakubō","","","Okinawan six-foot staff, often tapered at the ends and traditionally of red or white oak; the 'king' of kobudō weapons.",OK,dt="oak · taper · length",a="bō · kon"),
  x("Gun","","","Chinese staff about the user's height, thick at the base and thinner at the tip; one of the four major wushu weapons.",GU,
   [v("Bailangan","","","northern staff used in gunshu"),v("Nangun","","1992","southern staff event in competitive wushu")],"waxwood, rattan or carbon · length",a="gùn · côn"),
  x("Quarterstaff","","16th century on","English hardwood staff of 6–9 ft, sometimes tipped with metal; now used in stage combat and historical fencing.",QS,dt="length · wood · ferrule")],
 "m":[["Cold Steel Training Staff","Cold Steel"]]},
{"n":"Jō","a":"jo staff","d":"Japanese wooden staff about 1.27 m long, used in jōdō and aiki-jō.","t":["jōdō","aiki-jō"],"s":JO},
{"n":"Escrima sticks","a":"baston · kali sticks · arnis sticks · yantok","d":"Pair or single stick of rattan or hardwood, about 66–76 cm long, used in Filipino martial arts.","t":["rattan","kamagong","bahi","fibreglass, plastic or aluminium"],"s":BS},
{"n":"Nunchaku","a":"nunchucks · chainsticks","d":"Two short sticks joined by a cord or chain.","t":["octagonal","round","cord (himo)","chain (kusari)","foam training"],"s":"https://www.awma.com/collections/nunchaku-nunchucks",
 "m":[["Speedchuck",""]]},
{"n":"Tonfa","a":"tunkua","d":"Baton with a side handle set at right angles to the shaft, used in pairs.","t":["oak","polymer"],"s":"https://www.awma.com/training-weapons-main/training-weapons/tonfas-tong-fa-tuifa"},
{"n":"Sai","a":"pronged truncheon","d":"Metal truncheon with a central rod and two curved side prongs, used in pairs.","t":["standard","manji sai"],"s":"https://www.awma.com/pages/bo-staff",
 "x":[x("Manji sai","","","Sai with one side prong reversed, developed by Taira Shinken.",SA,dt="prong length · grip wrap")]},
{"n":"Kama","a":"fighting sickle","d":"Short-handled sickle blade made as a weapon, often used in pairs. A garden sickle is in Garden & Grounds.","t":["sharp","blunt training (kata kai)"],"s":"https://www.awma.com/pages/bo-staff"},
{"n":"Three-section staff","a":"sanjiegun · sansetsukon","d":"Three staff sections joined end to end by chains or cords.","t":["wood","rattan or bamboo","aluminium"],"s":"https://www.awma.com/pages/bo-staff"},
{"n":"Rope dart","a":"shéng biāo · jōhyō","d":"Dart or blade on the end of a long rope, swung and cast.","t":["rope dart","meteor hammer"],"s":"https://centurymartialarts.com/products/rope-dart"},
{"n":"Chain whip","a":"soft whip","d":"Jointed steel segments ending in a dart, swung as a whip.","t":["nine-section","seven-section","three-section"],"s":"https://wle.com/products/copy-of-9-section-chain-whip"},
]
W('07_02',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Merged Bo staff and Chinese staff into Staff (bō, gùn, quarterstaff as types and archetypes). Added Jō and Escrima sticks. Old placeholder model 'Speedchuck' (no maker) kept. Police side-handle baton (PR-24) left out of Tonfa (institutional; see Self-defence Baton). Facts sourced from Wikipedia articles fetched this session."})
