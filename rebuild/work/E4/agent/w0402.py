import json, os
CK='https://www.outdoorlife.com/guns/best-gun-cleaning-kits/'; GC='https://www.outdoorlife.com/gear/best-gun-cases/'
HB='https://www.thearmorylife.com/harris-s-brm-m-lok-bipod-review/'; WL='https://www.candlepowerforums.com/threads/sf-x300-vs-streamlight-tlr-1.264084/'
kinds=[
{"n":"Holster","a":"","d":"Case worn on the body to carry a handgun.",
 "t":["inside-the-waistband (IWB)","outside-the-waistband (OWB)","belt slide","paddle","pancake","shoulder","ankle","appendix","chest"],
 "s":"https://blade-tech.com/blogs/news/iwb-vs-owb"},
{"n":"Gun case","a":"rifle case · pistol case · gun slip · gun rug","d":"Hard or soft case for carrying and storing a firearm.",
 "t":["hard case","soft case","gun slip","pistol rug","double-rifle"],"s":GC,
 "m":[["Pelican Vault","Pelican"],["48SG Single Long Gun Case","Boyt"],["Rustrictor","Plano"],["Pistol Rug","Browning"],["Harness Signature Series Shotgun Case","Boyt"],["VTAC Rifle Case","Vertx"]]},
{"n":"Gun cleaning kit","a":"cleaning kit · bore cleaning kit","d":"Set of rods, brushes, patches and solvents for cleaning a firearm's bore and action.",
 "t":["universal","pistol","rifle","shotgun","pull-through"],"s":CK,
 "m":[["Bullseye Box","Shooter's Choice"],["Professional Pistol Cleaning Kit","Otis"],["MSR Cleaning Kit","Otis"],["17-Piece Shotgun Cleaning Kit","Birchwood Casey"],["Krome Stronghold Universal Cleaning Kit","Allen Company"],["No. 9 Solvent","Hoppe's"]]},
{"n":"Weapon light","a":"tactical light · gun light","d":"Light made to mount on a weapon.","t":["pistol","long gun","light/laser combination"],
 "s":"https://www.primaryarms.com/streamlight-tlr-1-hl-long-gun-kit",
 "m":[["TLR-1 HL","Streamlight"],["TLR-1","Streamlight"],["X300","SureFire"]]},
{"n":"Bipod","a":"","d":"Two-legged support made to mount on a weapon.","t":["swivel","fixed","Picatinny","M-Lok","sling-stud"],
 "s":"https://www.optics-trade.eu/en/caldwell-shooting-bipod-sitting-model.html",
 "x":[{"n":"Harris bipod","a":"","d":"Folding spring-leg rifle bipod with notched telescoping legs.","mk":"Harris Bipods","y":"","s":HB,
   "v":[{"n":"S-BRM-MLOK","mk":"Harris Bipods","y":"","d":"swivel, 6–9 in, built-in M-Lok adapter"}],"dt":"leg height · swivel or fixed · attachment"}],
 "m":[["Caldwell Shooting Bipod Sitting Model","Caldwell"]]},
{"n":"Shooting rest","a":"","d":"Support on which a weapon is laid to steady the aim.","t":["front rest","rear bag","lead sled"],
 "s":"https://www.optics-trade.eu/is/caldwell-rock-br-competition-front-shooting-rest.html",
 "m":[["Rock BR Competition Front Rest","Caldwell"]]},
]
K='knowledge'
def b(n,c,f,seg,kf,d,s=K):
    x={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
    if f: x["f"]=f
    return x
brands=[
b("Harris Bipods","United States","","Specialist","bipods","American maker of spring-leg rifle bipods."),
b("Pelican","United States","1976","Premium","protective cases","Californian maker of hard protective cases."),
b("Otis","United States","","Specialist","gun cleaning","Maker of compact gun cleaning kits."),
b("Streamlight","United States","","Mainstream","torches","Pennsylvania maker of torches and weapon lights."),
b("SureFire","United States","","Premium","tactical lights","Californian maker of tactical torches and weapon lights."),
b("Caldwell","United States","","Value","shooting rests","Shooting accessory brand for rests, bipods and targets."),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Holster carry styles (old belt-slide/paddle/pancake 'models') turned into types. New kinds Gun case and Gun cleaning kit sourced from Outdoor Life test roundups (award winners as models). Harris bipod added as archetype (only the S-BRM-MLOK version confirmed). Weapon light adds TLR-1 and X300 from a fetched forum comparison. Gun safes left to Home Safety & Security per plan."}
p='work/E4/shelves/04_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
