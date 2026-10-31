import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
ER='https://www.expertreviews.co.uk/technology/batteries-charging/best-power-bank'
MW='https://www.macworld.com/article/668980/best-magsafe-chargers.html'
JP='https://www.macworld.com/article/3056166/mophie-juice-pack-review.html'
kinds=[
 {"n":"Power bank","a":"portable charger · battery pack · MagSafe power bank · Qi2 power bank","d":"Rechargeable battery pack for charging phones and other devices on the go.",
  "t":["pocket (5,000–10,000 mAh)","20,000 mAh","high-capacity laptop (25,000 mAh+)","magnetic (MagSafe / Qi2)","built-in cable"],"s":ER,
  "m":[["Prime A110A","Anker"],["Nexode PB771","Ugreen"],["SnapGo Air","INIU"],["10 Mini","Cuktech"],["Laptop Power Bank (A1695)","Anker"],["A1383","Anker"],["BI-B64","INIU"],["PPAP20K","Baseus"],["BoostCharge Pro 5K magnetic power bank","Belkin"],["MagGo Power Bank 10K","Anker"]],
  "r":[["Anker Prime","Anker"],["MagGo","Anker"],["Nexode","Ugreen"]]},
 {"n":"Charging dock","a":"charging puck · charging stand · wireless charger","d":"Pad, puck, stand or dock that charges one or more devices, often wirelessly.","t":["puck / pad","stand","2-in-1","3-in-1","watch dock"],"s":MW,
  "m":[["MagSafe Charger","Apple"],["Zolo Wireless Charger (Magnetic, Pad)","Anker"],["UltraCharge Magnetic Charger Pad 25W","Belkin"],["HaloLock Kickstand Wireless Charger","ESR"],["MagGo Qi2 Wireless Charger Stand","Anker"],["MagFlow Magnetic Wireless Charging Pad 25W","Ugreen"],["2-in-1 Foldable Qi2 Wireless Charging Stand","Satechi"],["BoostCharge Pro 2-in-1 Wireless Charging Dock with MagSafe 15W","Belkin"],["UltraCharge Pro 3-in-1","Belkin"],["3-in-1 Wireless Charge Stand","Mophie"],["HyperJuice Qi2 Puck Stand","Hyper"],["W9 Stand","elago"]]},
 {"n":"Phone battery case","a":"battery case · charging case","d":"Phone case with a built-in battery that charges the phone.","s":JP,
  "m":[["Juice Pack for iPhone 17 Pro","Mophie"],["Juice Pack for iPhone 16","Mophie"],["Juice Pack Access","Mophie"]],"r":[["mophie Juice Pack","Mophie"]]},
]
def B(n,c,f,seg,kf,d,lines=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":"knowledge"}
    if lines: b["lines"]=lines
    return b
brands=[
 B("Anker","China","2011","Mainstream","power banks, chargers","Market-leading maker of power banks and chargers.",["Anker Prime","MagGo","Zolo"]),
 B("Belkin","United States","1983","Premium","chargers, accessories","American maker of chargers and phone accessories.",["BoostCharge","UltraCharge"]),
 B("Ugreen","China","2012","Mainstream","chargers, cables","Chinese maker of chargers, power banks and cables.",["Nexode","MagFlow"]),
 B("Baseus","China","","Value","chargers","Chinese maker of low-cost chargers and power banks."),
 B("INIU","China","","Value","power banks","Chinese maker of budget power banks."),
 B("Mophie","United States","","Premium","battery cases","American maker of battery cases and power banks, now owned by Zagg.",["Juice Pack"]),
 B("Apple","United States","1976","Premium","iPhone accessories","Maker of the MagSafe charger for its own devices."),
]
w('D2','06_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Anker skew fixed: Power bank cut from 11 Anker models to 10 across Anker, Ugreen, INIU, Cuktech, Baseus and Belkin, led by Expert Reviews (Oct 2026) test winners and techtest.org picks; dropped Anker 621/622/633, MagGo 2 Pro, Nano 5K MagGo, Prime 20K/26K, Zolo 20K/10K and 20K 87W duplicates; capacity and magnetic now types. Power bank had no source; now Expert Reviews. Charging dock widened with Macworld's MagSafe/Qi2 picks (old Hyper and elago kept). Phone battery case kept with Mophie Juice Pack (Macworld review); few other makers remain. Wirecutter could not be fetched (blocked, Firecrawl unsupported); no RTINGS or Which? power bank page found, so Samsung models not added."})
