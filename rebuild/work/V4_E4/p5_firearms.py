LR=WP+'List_of_revolvers';LP=WP+'List_of_semi-automatic_pistols';LB=WP+'List_of_bolt-action_rifles';LS=WP+'List_of_shotguns';LV=WP+'Lever-action'
# Single-action revolvers
add('Single-action revolver',rows("""Remington Model 1875|Remington single-action cartridge revolver.|Cartridge era|1875
Remington Model 1890|Remington single-action cartridge revolver.|Cartridge era|1890
Colt Buntline|Colt Single Action Army variant with a long barrel.|Cartridge era|1957
Ruger Blackhawk|Ruger single-action revolver.|Modern|1955
Ruger Bearcat|Small Ruger single-action revolver.|Modern|1958
Freedom Arms Model 83|American single-action revolver for large magnum cartridges.|Modern|1983
Magnum Research BFR|American single-action revolver for large cartridges.|Modern
Beretta Stampede|Italian copy of the Colt Single Action Army.|Modern|2000
Beretta Laramie|Italian single-action revolver.|Modern|2005""",LR))
setg('Single-action revolver','Cartridge era',{'Colt Single Action Army':'Cartridge era'})
KIND['Single-action revolver']['nl']="One entry is a single-action revolver model line; calibres and barrel lengths are versions."
KIND['Single-action revolver']['sel']="Single-action revolvers in the first 100,000 characters of Wikipedia's List of revolvers, to the Ruger Blackhawk; later entries are not read."
# Double-action revolvers
add('Double-action revolver',rows("""Colt Police Positive|Colt double-action revolver.|20th century|1907
Colt Official Police|Colt double-action revolver.|20th century|1908
Colt New Service|Large Colt double-action revolver.|20th century|1898
Colt Detective Special|Short-barrelled Colt double-action revolver.|20th century|1927
Colt Trooper|Colt double-action revolver.|20th century|1953
Colt Cobra|Light Colt double-action revolver.|20th century|1950
Colt Diamondback|Colt double-action revolver.|20th century|1966
Colt Anaconda|Colt large-frame double-action revolver.|20th century|1990
Colt King Cobra|Colt double-action revolver.|20th century|1986
Colt New Police Revolver|Colt double-action revolver.|19th century|1896
Colt M1889|Colt double-action revolver, the first to swing out its cylinder.|19th century|1889
Colt M1892|Colt double-action revolver.|19th century|1892
Colt M1877|Colt double-action revolver.|19th century|1877
Dan Wesson Model 15|American revolver with interchangeable barrels.|20th century|1971
Charter Arms Bulldog|American snub-nosed revolver.|20th century|1973
Ruger GP100|Ruger double-action revolver.|20th century
Korth Combat|German double-action revolver.|20th century|1964
Manurhin MR 73|French double-action revolver.|20th century|1972
Chiappa Rhino|Italian revolver firing from the lowest chamber.|21st century|2010
Mateba Autorevolver|Italian revolver that recoil-cycles its cylinder.|20th century|1997
Enfield No. 2|British service revolver.|20th century|1932
Enfield revolver|British service revolver.|19th century|1880
M1917 revolver|US service revolver.|20th century|1917
Nagant wz. 30|Polish copy of the Nagant revolver.|20th century|1930
New Nambu M60|Japanese double-action revolver.|20th century|1960
Bodeo Model 1889|Italian service revolver.|19th century|1889
Gasser M1870|Austro-Hungarian service revolver.|19th century|1870
M1879 Reichsrevolver|German service revolver.|19th century|1879
Modèle 1892 revolver|French service revolver.|19th century|1892
Mauser C78 zig-zag|German revolver with a zig-zag cylinder groove.|19th century|1878""",LR))
setg('Double-action revolver','20th century',{'Smith & Wesson Model 10':'20th century','Webley revolver':'19th century','Nagant M1895':'19th century','Smith & Wesson Model 36':'20th century','Smith & Wesson Model 29':'20th century','Colt Python':'20th century'})
KIND['Double-action revolver']['xg']='by era'
KIND['Double-action revolver']['nl']="One entry is a double-action revolver model line; marks, barrel lengths and calibres are versions."
KIND['Double-action revolver']['sel']="Colt, Ruger, Dan Wesson, Charter Arms, European and service double-action revolvers in the first 100,000 characters of Wikipedia's List of revolvers (to the Ruger GP100); military-only experiments and the later entries are not read."
add('Percussion revolver',rows("""Colt Paterson|First Colt revolver.|Early percussion|1836
Colt Walker|Large Colt percussion revolver.|Early percussion|1847
Colt Dragoon Revolver|Large Colt percussion revolver.|Early percussion|1848
Colt Army Model 1860|Colt percussion revolver.|Mid percussion|1860
Colt M1861 Navy|Colt percussion revolver.|Mid percussion|1861
Colt Pocket Percussion Revolvers|Small Colt percussion revolvers.|Mid percussion
Colt Model 1855 Sidehammer Pocket Revolver|Colt pocket revolver with a side hammer.|Mid percussion|1855
Remington-Beals Pocket Revolver|Remington pocket percussion revolver.|Mid percussion|1856
Adams revolver|British double-action percussion revolver.|Early percussion|1851
Beaumont–Adams revolver|British double- and single-action percussion revolver.|Mid percussion|1862
Kerr's Patent Revolver|British percussion revolver.|Mid percussion|1859
LeMat Revolver|Confederate percussion revolver with a shotgun barrel.|Mid percussion|1856""",LR))
setg('Percussion revolver','Mid percussion',{'Colt 1851 Navy':'Mid percussion','Remington Model 1858':'Mid percussion'})
KIND['Percussion revolver']['xg']='by era'
KIND['Percussion revolver']['nl']="One entry is a percussion revolver model line; patterns and copies are versions."
KIND['Percussion revolver']['sel']="Percussion revolvers in the first 100,000 characters of Wikipedia's List of revolvers (Colt, Remington, Adams, Kerr, LeMat); later entries are not read."
# Semi-automatic pistols
add('Semi-automatic pistol',rows("""Borchardt C-93|German self-loading pistol with a toggle action.|Early pistols|1893
Bergmann 1896|German blowback pistol.|Early pistols|1896
Bergmann–Bayard pistol|Belgian and German self-loading pistol.|Early pistols|1901
Colt M1900|First Colt self-loading pistol.|Early pistols|1900
Colt M1902|Colt self-loading pistol.|Early pistols|1902
Colt Model 1903 Pocket Hammerless|Slim Colt pocket pistol.|Early pistols|1903
Colt Model 1908 Vest Pocket|Small Colt pocket pistol.|Early pistols|1908
FN M1900|First Browning-designed FN pistol.|Early pistols|1900
FN Model 1910|Belgian Browning pocket pistol.|Early pistols|1910
FN Baby Browning|Small Belgian pocket pistol.|Early pistols|1927
Colt Woodsman|Colt .22 target pistol.|Between the wars|1915
Beretta M1934|Italian service pistol.|Between the wars|1934
ČZ vz. 27|Czechoslovak pistol.|Between the wars|1927
Ballester–Molina|Argentine pistol based on the M1911.|Mid century|1938
Colt Commander|Short Colt M1911.|Mid century|1950
CZ 52|Czechoslovak military pistol.|Mid century|1952
Beretta 950|Small Beretta pocket pistol.|Mid century|1952
Browning Buck Mark|American .22 target pistol.|Late 20th century|1985
Desert Eagle|Large gas-operated pistol for magnum cartridges.|Late 20th century|1979
FN Five-seveN|Belgian pistol for the 5.7×28mm cartridge.|Late 20th century|1998
Beretta Px4 Storm|Italian rotating-barrel pistol.|21st century|2004
Beretta Nano|Beretta compact pistol.|21st century|2011
Beretta APX|Beretta striker-fired pistol.|21st century|2016
FN FNX|Belgian service-type pistol.|21st century|2009
FN 509|FN service-type pistol.|21st century|2015
CZ P-10 C|Czech striker-fired pistol.|21st century|2014""",LP))
for kn in ('Semi-automatic pistol',):
    KIND[kn]['xg']='by era'
    setg(kn,'Late 20th century',{'Mauser C96':'Early pistols','Luger':'Early pistols','M1911':'Early pistols','Walther PP / PPK':'Between the wars','Browning Hi-Power':'Between the wars','CZ 75':'Late 20th century','Beretta 92':'Late 20th century','Glock 17':'Late 20th century','SIG Sauer P226':'Late 20th century','Springfield Armory XD':'21st century','Smith & Wesson M&P':'21st century','SIG Sauer P365':'21st century'})
    KIND[kn]['nl']="One entry is a semi-automatic pistol model line; marks and calibres are versions."
    KIND[kn]['sel']="Pistols in the first 100,000 characters of Wikipedia's List of semi-automatic pistols (to the Glisenti Model 1910), cut to civilian, collector and sporting lines; the rest of the list is not read."
    KIND[kn].pop('m',None)
REMOVED.append(('Semi-automatic pistol',['Beretta APX A1 (became Beretta APX)','EAA Girsan Witness2311','Rock Island Armory RIA 5.0 E','Smith & Wesson Bodyguard 2.0','M&P 22X','SD9 2.0','Springfield Hellcat Pro','Ruger LCP','Taurus GX2','Walther P22 Q','Walther WMP'],'Retail variants not in the fetched list window; removed'))
# Single-shot
add('Single-shot pistol',[],"One entry is a single-shot pistol model.","Models already cited from their own articles; no whole-space list exists.")
KIND['Single-shot pistol'].pop('m',None)
# Rifles
add('Lever-action rifle',rows("""Volcanic pistol|Lever-action repeating pistol, the forerunner of the Henry.|Early repeaters|1855
Colt Ring Rifle|Colt repeating rifle with a ring lever.|Early repeaters|1837
Winchester Model 1895|Winchester box-magazine lever rifle.|Smokeless era|1895
Colt Model 1883 Burgess|Colt lever-action rifle.|Black-powder era|1883
Marlin Model 1881|Marlin lever rifle.|Black-powder era|1881
Marlin Model 1893|Marlin lever rifle developed from the 1881.|Black-powder era|1893
Savage Model 1895|Savage lever rifle with a rotary magazine.|Smokeless era|1895
Savage Model 99|Savage lever rifle, made until 1997.|Smokeless era|1899
Winchester Model 9410|Winchester lever-action .410 shotgun.|Modern|2003
Ruger Model 96|Ruger lever-action rifle.|Modern|1996
Winchester Model 1887|Winchester lever-action shotgun.|Black-powder era|1887""",LV))
setg('Lever-action rifle','Smokeless era',{'Spencer repeating rifle':'Early repeaters','Henry 1860':'Early repeaters','Winchester Model 1866':'Black-powder era','Winchester Model 1873':'Black-powder era','Winchester Model 1894':'Smokeless era','Marlin Model 336':'Modern'})
KIND['Lever-action rifle']['xg']='by era'
KIND['Lever-action rifle']['nl']="One entry is a lever-action firearm model line; marks and calibres are versions."
KIND['Lever-action rifle']['sel']="Every model named in the first 100,000 characters of Wikipedia's Lever-action article; the remainder of the article is not read."
BA=rows("""Dreyse needle gun|Prussian needle-fire bolt rifle.|Black-powder|1841
Berdan rifle|Single-shot rifle of the Berdan system.|Black-powder|1870
Chassepot|French needle rifle.|Black-powder|1866
Mauser Model 1871|First Mauser rifle.|Black-powder|1871
Gewehr 1888|German commission rifle.|Smokeless|1888
Gewehr 98|German Mauser service rifle.|Smokeless|1898
Karabiner 98k|German short Mauser carbine.|Smokeless|1935
Mannlicher M1886|Austro-Hungarian service rifle.|Black-powder|1886
Mannlicher M1888|Austro-Hungarian service rifle.|Smokeless|1888
Mannlicher M1895|Austro-Hungarian straight-pull rifle.|Smokeless|1895
Mannlicher–Schönauer|Austrian rifle with a rotary magazine.|Smokeless|1903
Lebel 1886 rifle|First French smokeless rifle.|Smokeless|1886
Berthier rifle|French rifle with a three-round clip.|Smokeless|1890
MAS-36|French service rifle.|Smokeless|1936
Lee-Metford|British service rifle.|Smokeless|1888
M1917 Enfield rifle|US rifle derived from the British Pattern 14.|Smokeless|1917
Krag–Jørgensen|Norwegian bolt-action rifle.|Smokeless|1889
K31|Swiss straight-pull service rifle.|Smokeless|1933
Carcano|Italian service rifle.|Smokeless|1891
Arisaka Type 38|Japanese service rifle.|Smokeless|1905
Arisaka Type 99|Japanese service rifle.|Smokeless|1939
Murata rifle|First Japanese service rifle.|Black-powder|1880
Ross rifle|Canadian straight-pull rifle.|Smokeless|1903
Remington-Lee|American bolt-action rifle with a box magazine.|Black-powder|1879
Ruger M77|Ruger sporting bolt-action rifle.|Sporting|1968
Ruger American|Ruger low-cost bolt-action rifle.|Sporting|2011
Browning A-Bolt|Browning sporting bolt-action rifle.|Sporting|1985
Howa M1500|Japanese sporting bolt-action rifle.|Sporting|1979
Steyr Scout|Austrian light bolt-action rifle.|Sporting|1998
Accuracy International AWM|British long-range bolt-action rifle.|Precision|1996
M200 Intervention|American long-range bolt-action rifle.|Precision|2001
Zbroyar Z-008|Ukrainian bolt-action rifle.|Sporting
Voere S16|Austrian bolt-action rifle.|Sporting
Spielberg Brno 200F|Czech sporting bolt-action rifle.|Sporting
Kbk wz. 29|Polish Mauser carbine.|Smokeless|1929
vz. 24|Czechoslovak Mauser rifle.|Smokeless|1924
Hanyang 88|Chinese copy of the Gewehr 1888.|Smokeless|1895
Mauser–Vergueiro|Portuguese Mauser-type rifle.|Smokeless|1904
Ishapore 2A1 rifle|Indian rifle based on the Lee-Enfield.|Smokeless|1962
Jungle carbine|Short Lee-Enfield for jungle use.|Smokeless|1944
ArmaLite AR-50|Large-calibre American rifle.|Precision|1999""",LB)
add('Bolt-action rifle',BA)
setg('Bolt-action rifle','Smokeless',{'Dreyse needle gun':'Black-powder','Chassepot':'Black-powder','Mauser 98':'Smokeless','Lee–Enfield':'Smokeless','Mosin–Nagant':'Smokeless','Arisaka Type 30':'Smokeless','Springfield M1903':'Smokeless','Winchester Model 70':'Sporting','Remington Model 700':'Sporting','Tikka T3':'Sporting','Blaser R8':'Sporting'})
KIND['Bolt-action rifle']['xg']='by era'
KIND['Bolt-action rifle']['nl']="One entry is a bolt-action rifle model line; marks and calibres are versions."
KIND['Bolt-action rifle']['sel']="Rifles of Wikipedia's List of bolt-action rifles, cut to service rifles with an established name and to sporting and precision lines; prototypes, kit guns and the Ukrainian tactical rifles of the list are left out. The page notes it is incomplete."
for kn in ('Single-shot rifle','Semi-automatic rifle','Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun','Combination gun','Muzzle-loading pistol','Muzzle-loading shotgun','Musket','Muzzle-loading rifle'):
    KIND[kn]['nl']="One entry is a firearm model line; marks and calibres are versions."
    KIND[kn]['sel']="Model lines named in the first 100,000 characters of Wikipedia's List of shotguns where they apply, or cited from their own articles; no whole-space list of this action exists."
# Shotguns from LS
add('Pump-action shotgun',rows("""Mossberg 590|Mossberg pump shotgun.|Mossberg|
Mossberg Maverick 88|Low-cost Mossberg pump shotgun.|Mossberg|
Ithaca 37|Ithaca pump shotgun.|American pump guns|
Remington Model 10|Early Remington pump shotgun.|American pump guns|
Remington Model 31|Remington pump shotgun.|American pump guns|
Remington Model 17|Remington pump shotgun.|American pump guns|
Remington Spartan 453|Remington-branded pump shotgun.|American pump guns|
Benelli Nova|Benelli pump shotgun.|European pump guns|
Benelli Supernova|Benelli pump shotgun.|European pump guns|
Browning BPS|Browning pump shotgun made in Japan.|European pump guns|
Spencer 1882|Spencer pump shotgun.|American pump guns|
Smith & Wesson Model 3000|Smith & Wesson pump shotgun.|American pump guns|
Kel-Tec KSG|American bullpup pump shotgun.|Modern|""",LS))
add('Semi-automatic shotgun',rows("""Remington Model 1100|Remington gas-operated semi-automatic shotgun.|Remington|
Remington Model 11-87|Remington gas-operated semi-automatic shotgun.|Remington|
Remington Model 11-48|Remington recoil-operated shotgun.|Remington|
Remington Model 11|Remington recoil-operated shotgun based on the Auto-5.|Remington|
Remington Model 58|Remington semi-automatic shotgun.|Remington|
Remington Versa Max|Remington gas-operated semi-automatic shotgun.|Remington|
Remington V3|Remington gas-operated semi-automatic shotgun.|Remington|
Browning Double Automatic Shotgun|Browning two-shot recoil shotgun.|Browning|
Benelli M1|Benelli inertia-driven semi-automatic shotgun.|Benelli|
Benelli Raffaello|Benelli inertia-driven semi-automatic shotgun.|Benelli|
Benelli Vinci|Benelli modular semi-automatic shotgun.|Benelli|
Beretta A303|Beretta gas-operated shotgun.|Beretta|
Beretta AL391|Beretta gas-operated shotgun.|Beretta|
Beretta Xtrema 2|Beretta gas-operated shotgun.|Beretta|
Beretta 1301|Beretta gas-operated shotgun.|Beretta|
Franchi AL-48|Franchi semi-automatic shotgun.|Franchi|
Mossberg 930|Mossberg gas-operated shotgun.|Mossberg|
Ithaca Mag-10|Ithaca 10-gauge semi-automatic shotgun.|Ithaca|
Remington Model SP-10|Remington 10-gauge semi-automatic shotgun.|Remington|
Saiga-12|Russian semi-automatic shotgun.|Russian|""",LS))
add('Over-under shotgun',rows("""Beretta 682|Beretta competition over-under shotgun.|Beretta|
Browning Citori|Browning over-under shotgun made in Japan.|Browning|
Ruger Red Label|Ruger over-under shotgun.|Ruger|
Ruger Gold Label|Ruger side-by-side shotgun.|Ruger|
Blaser F3|German competition over-under shotgun.|Blaser|
Beretta DT-10|Beretta competition over-under shotgun.|Beretta|
Chiappa Triple Crown|Chiappa break-action shotgun.|Chiappa|""",LS))
add('Side-by-side shotgun',rows("""Browning BSS|Browning side-by-side shotgun.|Browning|
Coach gun|Short double-barrelled shotgun of the American West.|Coach gun|
Ithaca Auto & Burglar|Ithaca short side-by-side shotgun.|Ithaca|""",LS))
add('Single-shot shotgun',rows("""H&R Ultraslug Hunter|American single-shot slug shotgun.|H&R|
Cooey 84|Canadian single-shot shotgun.|Cooey|
Snake Charmer|American single-shot snake shotgun.|Snake gun|""",LS))
add('Combination gun',rows("M30 Luftwaffe Drilling|German three-barrel survival gun of the Second World War.|Drilling|1941",LS))
for kn,gd in [('Pump-action shotgun','Pump'),('Semi-automatic shotgun','Semi'),('Over-under shotgun','Ou'),('Side-by-side shotgun','Sxs'),('Single-shot shotgun','Single')]:
    for x in KIND[kn]['x']:
        x['g']=x['n'].split()[0]
    KIND[kn]['xg']='by maker'
    KIND[kn]['sel']="Shotguns of this action in the first 100,000 characters of Wikipedia's List of shotguns (to the SRM Arms Model 1216), cut to sporting and civilian lines; military and tactical shotguns and the later entries are not read."
KIND['Combination gun'].pop('m',None)
