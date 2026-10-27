import json, os, sys
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    t = p + '.tmp'
    json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1)
    os.replace(t, p)
B='https://www.bhphotovideo.com/c/buy/Voice-Translators/ci/60047'
w('D2','03_01',{"kinds":[
 {"n":"Electronic dictionary","a":"","d":"Handheld device holding one or more dictionaries for look-up.","s":"https://wafuu.com/en-se/collections/computers-peripherals/products/casio-ex-word-xd-sa4900bu-electronic-dictionary-blue","m":[["Ex-word XD-SA4900","Casio"]]},
 {"n":"Pocket translator","a":"","d":"Handheld device that translates speech or text between languages.","s":B,"m":[["Pocketalk S2","Pocketalk"],["Pocketalk 2 Plus","Pocketalk"],["Translator V4","Vasco"],["Translator Q1","Vasco"],["T1 Handheld Translator","Timekettle"]]},
 {"n":"Translator earbuds","a":"","d":"Pair of earbuds sold for translating speech between languages through a phone app; ordinary earbuds with a translate feature are in Audio & Video.","s":B}],
 "brands":[],"traditions":[],"notes":"All three old kinds kept as planned; models unchanged (already a short market-covering list). No new models added."})
w('D2','07_00',{"kinds":[
 {"n":"Phone case","a":"","d":"Case or cover made to hold and protect one phone model.","s":"https://www.verizon.com/products/phone-accessories/otterbox/","m":[["Defender Series Pro","OtterBox"]],"r":[["Defender","OtterBox"],["OtterBox Commuter Series","OtterBox"],["OtterBox Symmetry Series","OtterBox"]]},
 {"n":"Screen protector","a":"","d":"Film or glass sheet cut to cover the screen of one device.","s":"https://www.shidirect.com/product/50360886/ZAGG-InvisibleShield-Glass-Elite","m":[["InvisibleShield Glass Elite","ZAGG"]]},
 {"n":"Tablet & e-reader case","a":"tablet case · e-reader cover","d":"Case or cover made to hold and protect one tablet or e-reader model.","t":["tablet case","e-reader cover"],"s":"https://www.ldlc.com/en/product/PB00574494.html","m":[["Smart Book Cover EF-BX710","Samsung"],["SleepCover (Clara Colour/BW)","Kobo"]]}],
 "brands":[],"traditions":[],"notes":"Merged Tablet case and E-reader cover into Tablet & e-reader case (kept the tablet case's source). OtterBox ranges kept; no SKU lists added."})
w('D2','07_01',{"kinds":[
 {"n":"Watch strap","a":"watch band · smartwatch strap · band","d":"Replacement strap made for one smartwatch or band.","s":"https://jbhifi.co.nz/products/apple-watch-45mm-sport-loop-cypress","m":[["Sport Loop","Apple"]]},
 {"n":"Stylus","a":"","d":"Pen made for the screen of one range of tablets or phones.","s":"https://marketplace.unl.edu/huskertech/accessories/ipad-accessories","m":[["Apple Pencil Pro","Apple"],["Apple Pencil (2nd generation)","Apple"],["Apple Pencil (1st generation)","Apple"]]},
 {"n":"Tablet keyboard cover","a":"","d":"Cover with a keyboard made for one range of tablets.","s":"https://marketplace.unl.edu/huskertech/accessories/ipad-accessories","m":[["Magic Keyboard for iPad Pro","Apple"],["Smart Keyboard Folio","Apple"],["Slim Folio Keyboard Case","Logitech"]]}],
 "brands":[],"traditions":[],"notes":"All three kinds kept unchanged; lists already short. No new models added."})
w('D2','07_02',{"kinds":[
 {"n":"Phone gimbal","a":"","d":"Motorised handheld stabiliser made for a phone.","s":"https://www.bhphotovideo.com/c/buy/smartphone-gimbal-stabilizers/ci/51774/pn/2","m":[["Osmo Mobile 7","DJI"],["Osmo Mobile SE","DJI"],["Smooth 5S AI Pro","Zhiyun"],["Smooth-Q4","Zhiyun"],["iSteady M7","Hohem"],["iSteady X2","Hohem"],["Flow 2","Insta360"],["Vimble 3","Feiyu"],["Mini-S","Moza"]],"r":[["Osmo Mobile","DJI"],["Smooth","Zhiyun"],["iSteady","Hohem"]]},
 {"n":"Selfie stick","a":"","d":"Extendable pole that holds a phone for self-portraits.","s":"https://www.bhphotovideo.com/c/product/1833072-REG/ulanzi_2888_rmt_01_wireless_bluetooth_extendable.html/specs","m":[["RMT-01","Ulanzi"]]},
 {"n":"Clip-on phone lens","a":"","d":"Add-on lens that clips over a phone camera.","s":"https://www.tomsguide.com/phones/iphones/best-iphone-lenses","m":[["Sandmarc 58mm Telephoto lens","Sandmarc"]]},
 {"n":"Phone microphone","a":"smartphone microphone","d":"Microphone made to plug into or clip onto a phone and record through it; one made for cameras that also takes a phone is in Cameras & Photography or Musical Instruments & Music Gear.","s":"https://www.ldlc.com/en/product/PB00696318.html"}],
 "brands":[],"traditions":[],"notes":"Phone gimbal cut from 17 models to 9: kept the newest and budget model per line (DJI Osmo Mobile, Zhiyun Smooth, Hohem iSteady, Insta360 Flow, plus Feiyu and Moza); dropped older generations Osmo Mobile 6, Smooth-Q3, iSteady M6/Q/V3/XE, VB4, Mini MX. Ranges kept. Other kinds unchanged."})
