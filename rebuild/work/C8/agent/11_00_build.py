import json, os
LBS="https://en.wikipedia.org/wiki/List_of_battery_sizes"
kinds=[
{"n":"Household battery","a":"AA · AAA · C · D · 9 V · PP3 · R6 · LR6 · R03 · R14 · R20 · 6LR61 · 6F22 · penlight · Mignon",
 "d":"Standard cylindrical or 9 V primary or rechargeable battery for household devices.",
 "t":["AA (R6/LR6)","AAA (R03/LR03)","C (R14/LR14)","D (R20/LR20)","9 V (PP3, 6LR61/6F22)","Alkaline","Lithium (FR6/FR03)","NiMH rechargeable (HR6/HR03)","Zinc–carbon"],
 "s":LBS,
 "m":[["Duracell Coppertop AA","Duracell"],["Duracell Plus AA","Duracell"],["Duracell Optimum AA","Duracell"],["Duracell Ultra Power AA","Duracell"],
      ["Energizer Max AA","Energizer"],["Energizer Max Plus AA","Energizer"],["Energizer Ultimate Lithium AA","Energizer"],["Energizer Recharge Maxi AA","Energizer"],
      ["Panasonic Eneloop Pro AA","Panasonic"],["Panasonic Evolta AA","Panasonic"],["Varta Longlife Power AA","VARTA"],["GP Ultra Plus G-Tech AA","GP Batteries"]],
 "r":[["Coppertop","Duracell"],["Plus","Duracell"],["Optimum","Duracell"],["Procell","Duracell"],["Max","Energizer"],["Max Plus","Energizer"],["Ultimate Lithium","Energizer"],["Recharge","Energizer"],["Eneloop","Panasonic"],["Evolta","Panasonic"],["Longlife","VARTA"],["Recyko","GP Batteries"]]},
{"n":"Coin cell","a":"button cell · watch battery · CR2032 · LR44",
 "d":"Small flat button or coin cell for watches, remotes, keys and scales.",
 "t":["CR2032","CR2025","CR2016","CR2450","LR44 / AG13 / A76 / 357","377 (silver oxide watch cell)","Lithium","Alkaline","Silver oxide","Zinc–air (hearing aid)"],
 "s":"https://en.wikipedia.org/wiki/Button_cell"},
{"n":"Specialty battery","a":"CR123A · CR17345 · A23 · 23A · MN21 · 8LR932 · lantern battery · 4R25",
 "d":"Less common primary battery sizes for torches, cameras, key fobs, alarms and lanterns.",
 "t":["CR123A (3 V lithium)","CR2 (3 V lithium)","A23 (12 V alkaline)","4LR44 (6 V)","6 V lantern (4R25, spring or screw terminals)","4.5 V flat pack (3R12)"],
 "s":LBS},
{"n":"Battery charger","a":"AA charger · NiMH charger · smart charger",
 "d":"Charger for loose standard cells such as AA, AAA and 18650.",
 "t":["Basic overnight charger","Fast charger","Smart charger-analyser","USB-powered charger"],
 "s":"https://www.adorama.com/l/Home-Electronics/Batteries-and-Power-Supply/Household-Batteries-and-Accessories/Sanyo~Household-Battery-Chargers",
 "m":[["Panasonic Eneloop Pro BQ-CC63 8-slot charger","Panasonic"],["Panasonic BQ-CC65 4-slot charger","Panasonic"],["Duracell CEF14 4 hours Battery Charger","Duracell"],["Varta Universal Battery Charger","VARTA"],["Maha MH-C980 Turbo Charger-Analyzer","Maha"],["Maha PowerEx MH-C808M","Maha"],["Maha PowerEx MH-C204W","Maha"],["Jupio USB Octo Battery Charger","Jupio"],["Power2000 XP-UNV","Power2000"]],
 "r":[["Eneloop","Panasonic"]]},
{"n":"Sealed lead-acid battery","a":"SLA · VRLA · AGM battery · gel battery",
 "d":"Maintenance-free sealed lead-acid block sold loose, usually 6 V or 12 V, for UPS units, alarms and mobility scooters.",
 "t":["6 V","12 V","AGM","Gel"],
 "s":"https://en.wikipedia.org/wiki/VRLA_battery"}]
brands=[
{"n":"Duracell","c":"United States","f":"1924","seg":"Mass-market batteries","d":"Battery maker that began as the P. R. Mallory Company; owned by Berkshire Hathaway since 2016.","lines":["Coppertop","Plus","Ultra","Optimum","Procell","Quantum"],"s":"https://en.wikipedia.org/wiki/Duracell"},
{"n":"Energizer","c":"United States","f":"2000","seg":"Mass-market batteries","d":"Battery company spun off from Ralston Purina in 2000; also owns Eveready and Rayovac.","lines":["Max","Max Plus","Ultimate Lithium","Recharge","Eveready"],"rel":["VARTA"],"s":"https://en.wikipedia.org/wiki/Energizer_Holdings"},
{"n":"Panasonic","c":"Japan","f":"1918","seg":"Electronics and batteries","d":"Japanese electronics group whose battery brands include Eneloop low self-discharge NiMH cells, launched by Sanyo in 2005.","lines":["Eneloop","Eneloop Pro","Eneloop Lite","Evolta","Pro Power"],"s":"https://en.wikipedia.org/wiki/Panasonic"},
{"n":"VARTA","c":"Germany","f":"1887","seg":"Batteries","d":"German battery maker from Ellwangen producing household, rechargeable, coin and microbatteries.","lines":["Longlife","Longlife Power","Longlife Max Power"],"rel":["Energizer"],"s":"https://en.wikipedia.org/wiki/VARTA"},
{"n":"GP Batteries","c":"Hong Kong","f":"1964","seg":"Batteries","d":"Hong Kong battery maker selling GP and GP Recyko rechargeable cells.","lines":["Ultra Alkaline","Ultra Plus G-Tech","Lithium","Recyko"],"s":"https://en.wikipedia.org/wiki/GP_Batteries"}]
notes=("Merged AA/AAA/C/D/9 V into Household battery (sizes and chemistries as types) and CR123A/A23/6 V lantern into Specialty battery. "
"Household battery models: old data plus market brands from the Which? batteries test list (https://www.which.co.uk/reviews/batteries) and the Consumer Reports test reported by KATU "
"(Energizer Ultimate Lithium top overall, Duracell Ultra Power top alkaline; 2012 test). Current Which? Best Buy labels are members-only, so no Which? winner could be named. "
"Coin-cell old model rows (no makers) became size types. Charger models kept from old data (duplicates none). No models for specialty or SLA batteries (no retrieved source). "
"Dropped the old council/Bunnings/eBay retail sources in favour of Wikipedia pages. No traditions (not an artisan area). Supermarket own brands (Aldi, Lidl, Tesco, Amazon Basics) appear in Which? tests but were left out as non-market-covering.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/C8/shelves/11_00.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
