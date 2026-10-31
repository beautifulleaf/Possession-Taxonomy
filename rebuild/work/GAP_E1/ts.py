import json
names="""A Call To Arms|Accurate|Adventure Force|Andrea Miniatures|Airfix|Almark|Armourfast|Atlantic (company)|Aurora Plastics Corporation|Armies In Plastic|Barcelona Universal Models (BUM)|Barclay|Benbros|Bergen Toy & Novelty Co.|Beton|Billy V|Britains|BMC Toys|Brevett|Burlington Equestrian Models|Caesar|CBG Mignot|Chota Sahib|Chialu|Classic Toy Soldiers|Co.Ma.|Coates and Shin|The Corps|Crescent Toys|Dorset Toy soldiers|Dapol|Dark Dream Studio|Deetail|Ducal|Dulcop|Durso|Eagle Games|Eduard|Elastolin|Elite Force|Emhar|Ente Scambi Coloniali Internazionali (ESCI)|Expeditionary force|Evolution|First To Fight|Fleurbaix Toy Soldiers|Fujimi|Fun Little Toys|Figurart|GerMan|Giant|Greenbrier International|Gulliver|Hasegawa|HaT|Hegemony|Heller|Herald Miniatures|Hero Force|Heyde|Ideal Toy Company|IMEX|Italeri|Jack Scruby|John Hill & Company|Joyin|Kienel|King And Country|Kombat|Liberty Imports|Little Legion|Legio|Linear-A|Linear-B|Leyla|Lineol|Lone Star Toys|Louis Marx and Company|Lucky Toys|LW|Manoil|Mars|Matchbox|Metch|Miniart|MM|Model Kasten|Model Products Corporation (MPC)|Mountford Military Models|Monogram|Nexus|Odemar|Orion|Osul|Panzer vs Tanks|Pegasus|Plastic Soldier Company (PSC)|Pobeda|Preiser|Prince August|Prince August Q|Quiralu|RedBox|Rose|Rosedale|Revell|Schylling|SCS Direct|Studio Paris Art|Sanderson|Strelets|Trophy Miniatures of Wales|T-Model|Tamiya|Testor's|Timpo Toys|Tim Mee Toys|Toxso|Toymendous|Toysmith|Tragik|Trico|True Heroes|T.S.S.D.|Ultima Ratio|Under Two Flags|Universal Plastics|Valdemar|Valiant|Vertunni|Wend-Al|warhansa|Waterloo 1815|WowToyz|Ykreol|Zvezda""".split('|')
d=json.load(open('rebuild/out/E1.json'))
allx=set()
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x') or []: allx.add(e['n'].lower())
miss=[n for n in names if n.lower() not in allx]
print(len(names),len(miss)); print(miss)
