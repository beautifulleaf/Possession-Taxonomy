import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
O="https://www.babeland.com/sex-toys/c/3000/vibrators/"
kinds=[
{"n":"Air-pulse stimulator","a":"clitoral air-pulse stimulator · suction stimulator","d":"Stimulator that works with pulses of air or suction over the clitoris, without contact pressure. Some are worn, some are not.","t":["Handheld","Wearable","Rechargeable","Waterproof"],
 "m":[["Womanizer W100","Womanizer"],["Womanizer OG","Womanizer"],["Womanizer Premium Eco","Womanizer"],["Womanizer Blend","Womanizer"],["Satisfyer Pro 2","Satisfyer"]],"r":[["Pleasure Air Technology","Womanizer"]],"s":O},
{"n":"Suction pump","a":"external suction pump","d":"Hand or powered vacuum pump with a cup placed over the vulva or nipples.","t":["Hand pump","Powered pump","Cup size"],"s":O},
{"n":"Penis pump","a":"vacuum pump","d":"Cylinder placed over the penis with a hand or powered vacuum pump. One whose maker states a medical (erectile) purpose is in Health, Medical & Mobility.","t":["Hand pump","Electric pump","Water (hydro) pump","Bulb pump"],"s":"https://www.orion.de/katalog/sextoys/penisringe"},
]
put('H3','01_00',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Womanizer shown as air-pulse leader from its Wikipedia page (2014, Pleasure Air Technology, Lovehoney Group); the page does not say it originated the category, so no claim of 'originator' is made. Satisfyer Pro 2 kept from old data. LELO Sona and We-Vibe Melt not named on any retrieved page, so left out. Penis pump types are from the brief and the erectile dysfunction page (vacuum devices, medical versus novelty pumps); medical pumps remain in Health. Brands Womanizer and Satisfyer are in the vibrator shelf."})
