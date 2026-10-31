BW=WP+'Bow_and_arrow'
add('Longbow',rows("Welsh bow|Self bow of Wales, named with the English longbow.|Britain",BW))
add('Flatbow',rows("Stellmoor bow|Pine bow found at Stellmoor in northern Germany, about 8,000 BC.|Europe (prehistoric)|c. 8000 BC",BW))
add('Horse bow',rows("Subeshi culture bow|Composite bow of the Subeshi culture of Xinjiang.|Eurasian steppe|c. 800 BC",BW))
add('Historical crossbow',rows("Austroasiatic crossbow|Crossbow of the Austroasiatic peoples.|Asia",BW))
setg('Longbow',None,{'English longbow':'Britain','American longbow':'North America'})
setg('Flatbow',None,{'Holmegaard bow':'Europe (prehistoric)','Native American flatbow':'North America'})
setg('Yumi',None,{'Miyakonojō bamboo yumi':'Japan'})
setg('Horse bow',None,{'Mongol bow':'Eurasian steppe','Turkish bow':'Anatolia and the Ottoman world','Gakgung':'Korea','Hungarian bow':'Hungary'})
setg('Recurve bow',None,{'Bear Kodiak':'United States'})
setg('Compound bow',None,{'Allen compound bow':'United States'})
setg('Historical crossbow',None,{'Arbalest':'Europe'})
setg('Repeating crossbow','China');setg('Recurve crossbow','Modern');setg('Compound crossbow','Modern')
setg('Sling',None,{'Balearic sling':'Balearic Islands','Andean sling':'Andes'})
setg('Blowgun','Southeast Asia and the Americas',{'Fukiya':'Japan','Sumpit':'Borneo','Cherokee blowgun':'North America'})
setg('Slingshot','Modern'); setg('Arrow','Modern'); setg('Arrowhead','Medieval'); setg('Bow riser','Modern'); setg('Arrow rest','Modern')
for kn in ('Longbow','Flatbow','Yumi','Horse bow'):
    KIND[kn]['xg']='by culture'
for kn in ('Longbow','Flatbow','Yumi','Horse bow','Recurve bow','Compound bow','Historical crossbow','Repeating crossbow','Recurve crossbow','Compound crossbow','Sling','Blowgun','Slingshot','Arrow','Arrowhead','Bow riser','Arrow rest'):
    KIND[kn]['nl']="One entry is a traditional bow or launcher named for its culture, or a long-lived maker's model; versions are regional or dated variants."
    KIND[kn]['sel']="Bows named in Wikipedia's Bow and arrow article (first 100,000 characters) by culture, plus the maker models already cited; no whole-space list of bows exists."
    dropm(kn,'Retail models of archery makers; removed as out of scope') if KIND[kn].get('m') else None
for kn in ('Crossbow bolt','Release aid','Bow sight','Stabiliser','Blowgun'):
    dropm(kn,'Retail models of archery makers; removed as out of scope') if KIND[kn].get('m') else None
# Air guns, ammunition, optics etc: remove retail models
for kn in ('Spring-piston air rifle','CO2 air rifle','PCP air rifle','CO2 air pistol','PCP air pistol','Air-gun pellets','Pneumatic air rifle','Pneumatic air pistol'):
    if KIND[kn].get('m'): dropm(kn,'Retail air-gun models and consumables; no canon names them, removed as out of scope')
    if KIND[kn].get('x'):
        KIND[kn]['nl']="One entry is a long-running air-gun model line; versions are variants or calibres."
        KIND[kn]['sel']="Model lines cited from their own manufacturer or reference pages; there is no whole-space list of air guns."
for kn in ('Primer','Smokeless powder','Black powder','Loose bullet','Muzzle-loading projectile','Reloading press','Reloading die set','Shotshell','Pepper spray','Pepper-ball launcher','Stun gun','Kubotan','Blank-firing pistol','Magazine','Weapon light','Gun case','Gun cleaning kit','Bipod','Shooting rest','Rifle scope','Combination gun','Single-shot pistol','Single-shot rifle','Muzzle-loading shotgun','Muzzle-loading rifle','Semi-automatic pistol','Soft ballistic vest','Hard armour plate','Stab-resistant vest','Deactivated ordnance','Brigandine','Gauntlet','Plate armour harness','Japanese armour','Round shield','Rimfire cartridge','Centrefire handgun cartridge','Centrefire rifle cartridge'):
    if KIND[kn].get('m') and kn not in('Semi-automatic pistol','Combination gun','Rifle scope','Gauntlet','Brigandine','Japanese armour','Plate armour harness','Soft ballistic vest','Deactivated ordnance','Rimfire cartridge','Centrefire handgun cartridge','Centrefire rifle cartridge'):
        dropm(kn,'Retail products or consumables; no canon names them, removed as out of scope')
