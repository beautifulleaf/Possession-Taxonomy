import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':W+s,'v':[dict(zip(('n','mk','y','d'),t)) for t in v]}
    if dt: x['dt']=dt
    return x
old=json.load(open('work/D1/agent/00_01.old.json'))
allm={tuple(m) for k in old for m in k.get('m',[])}
def M(l):
    bad=[m for m in l if tuple(m) not in allm]
    assert not bad,bad
    return [list(m) for m in l]
os_={k['n']:k.get('s') for k in old}
kinds=[
 {'n':'Tower PC','a':'tower desktop PC','d':'Complete desktop computer in a tower case, with the parts fitted.','t':['prebuilt gaming','workstation','office'],'s':os_['Tower PC'],
  'x':[
   X('Mac Pro','Apple','2006','Mac_Pro','Apple\'s expandable professional desktop, successor to the Power Mac G5.',
     [('Mac Pro tower','Apple','2006','Intel Xeon, Power Mac G5 case'),('Mac Pro cylinder','Apple','2013','compact cylinder, nicknamed "trash can"'),('Mac Pro lattice tower','Apple','2019','return to a tower with lattice front'),('Mac Pro (Apple silicon)','Apple','2023','M2 Ultra in the 2019 chassis')],dt='tower or rack-mount'),
   X('Alienware Aurora','Alienware','','Alienware','Alienware\'s mainstream gaming tower, refreshed as numbered R revisions.',
     [('Aurora R1','Alienware','','X58, factory liquid cooling'),('Aurora R2','Alienware','','first Alienware desktop in retail chains'),('Aurora R4','Alienware','','quad-channel memory'),('Aurora R5','Alienware','2016','tool-less redesigned case'),('Aurora R6','Alienware','2017',''),('Aurora R9','Alienware','2019',''),('Aurora R12','Alienware','2021',''),('Aurora R13','Alienware','2021','larger chassis, clear side panel'),('Aurora R15','Alienware','2022','')]),
   X('HP Z workstation','HP','2009','HP_Z','HP\'s desktop workstation family for engineering and creative work.',
     [('Z400 / Z600 / Z800','HP','2009','first generation'),('Z420 / Z620 / Z820','HP','2012',''),('Z4 / Z6 / Z8 G4','HP','2017',''),('Z2 Mini G3','HP','2016','mini workstation'),('Z8 Fury G5','HP','2023','')]),
  ],
  'm':M([["Alienware Area-51","Alienware"],["Dell Pro Tower","Dell"],["Dell Tower Plus","Dell"],["Precision 3680","Dell"],["Precision 5860","Dell"],["Precision 7960","Dell"],["Endeavor Pro5600","Epson"]])},
 {'n':'All-in-one PC','a':'AIO','d':'Complete computer with the screen and the computer in one body.','s':os_['All-in-one PC'],
  'x':[X('iMac','Apple','1998','IMac','Apple\'s all-in-one desktop, from the translucent CRT original to slim Apple silicon models.',
     [('iMac G3','Apple','1998','translucent coloured CRT'),('iMac G4','Apple','2002','LCD on a movable arm over a dome base'),('iMac G5','Apple','2004','computer behind the screen'),('iMac (Intel polycarbonate)','Apple','2006',''),('iMac (aluminium)','Apple','2007',''),('iMac (unibody)','Apple','2009',''),('iMac (slim unibody)','Apple','2012',''),('iMac with Retina display','Apple','2014','4K and 5K'),('iMac 24-inch (Apple silicon)','Apple','2021','M1, then later M chips; colours')],dt='screen 15–27 in · colours')],
  'm':M([["Dell 24 All-in-One","Dell"],["Dell 27 All-in-One","Dell"],["Dell Pro 24 All-in-One","Dell"],["Spectre One","HP"]])},
 {'n':'Mini PC','a':'','d':'Complete desktop computer in a small box, sold as a ready machine.','s':os_['Mini PC'],
  'x':[X('Mac mini','Apple','2005','Mac_mini','Apple\'s small screenless desktop.',
     [('Mac mini G4','Apple','2005','PowerPC'),('Mac mini (Intel)','Apple','2006',''),('Mac mini (unibody)','Apple','2010','thin aluminium'),('Mac mini 2018','Apple','2018','space grey'),('Mac mini M1','Apple','2020','first Apple silicon'),('Mac mini M2','Apple','2023','M2 and M2 Pro'),('Mac mini M4','Apple','2024','much smaller redesign')]),
       X('Mac Studio','Apple','2022','Mac_Studio','Compact high-performance Apple desktop between Mac mini and Mac Pro.',
     [('Mac Studio M1 Max / M1 Ultra','Apple','2022',''),('Mac Studio M2 Max / M2 Ultra','Apple','2023',''),('Mac Studio M4 Max / M3 Ultra','Apple','2025',''),('Mac Studio M5 Max / M5 Ultra','Apple','2026','')])],
  'm':M([["SEi12","Beelink"],["SEi13 Pro","Beelink"],["A7","Geekom"],["XT12 Pro","Geekom"],["Venus UM690","Minisforum"],["Mercury UM780","Minisforum"],["Dell Pro Micro","Dell"],["IdeaCentre Mini","Lenovo"]])},
 {'n':'Small-form-factor desktop','a':'SFF PC · low-profile desktop · desktop-case PC','d':'Complete desktop computer in a compact or low horizontal case, often set under the monitor or behind it.','t':['SFF','USFF / micro','desktop case'],'s':os_['Low-profile desktop PC'],
  'x':[X('Dell OptiPlex','Dell','1993','Dell_OptiPlex','Dell\'s business desktop line in tower, small, micro and all-in-one forms, folded into Dell Pro in 2025.',
     [('OptiPlex GX1','Dell','1998',''),('OptiPlex 745 / 755','Dell','2006',''),('OptiPlex 960 / 980','Dell','2008–2010',''),('OptiPlex 7010 / 9020','Dell','2012–2013','widely used refurbished'),('OptiPlex 7080','Dell','2020',''),('Dell Pro desktops','Dell','2025','successor name')],dt='MT · SFF · Micro · AIO')],
  'm':M([["Compaq Evo D510","Compaq"],["Compaq Evo D310","Compaq"]])},
 {'n':'Barebone kit','a':'','d':'Case, board and power supply sold as the body of a machine, to which the buyer adds the rest.','s':os_['Barebone kit'],
  'x':[X('Intel NUC','Intel','2013','Next_Unit_of_Computing','Intel\'s 4 × 4-inch barebone kit that defined the modern mini PC; licensed to ASUS since 2023.',
     [('NUC (first kits)','Intel','2013',''),('Skull Canyon (6th gen)','Intel','2016','larger case, Thunderbolt 3'),('Hades Canyon (8th gen)','Intel','2018','Intel CPU with Radeon graphics'),('NUC Pro','ASUS','','ASUS-made after 2023'),('NUC Essential','ASUS',''),],a='Next Unit of Computing')],
  'm':M([["DeskMini X300","ASRock"],["DeskMini B660","ASRock"],["DeskMeet B660","ASRock"],["Cubi 5","MSI"],["UM880 Pro","Minisforum"]])},
 {'n':'Home server','a':'homelab server · rack-mount server · tower server','d':'Server computer, in a tower, compact box or 19-inch rack chassis, kept at home for storage, virtual machines or a homelab.','t':['micro server','tower server','rack-mount (1U–4U)'],'s':os_['Rack-mount server'],
  'x':[X('HPE ProLiant MicroServer','HPE','','HP_ProLiant','Compact, low-power entry ProLiant server popular for home offices and homelabs.',[('ProLiant MicroServer N36L','HPE','','')]),
       X('Dell PowerEdge','Dell','1994','Dell_PowerEdge','Dell\'s server line, coded R (rack), T (tower) or M (blade) with generation in the number.',[('PowerEdge R260','Dell','',''),('PowerEdge R360','Dell','',''),('PowerEdge R760','Dell','','')])],
  'm':M([["ProLiant DL20 Gen11","HPE"],["ThinkSystem SR630 V3","Lenovo"]])},
]
K='knowledge'
brands=[
 dict(n='Apple',c='United States',f='1976',seg='Premium',kf='Mac computers',d='Californian maker of Mac computers, iPhone and iPad.',lines=['iMac','Mac mini','Mac Studio','Mac Pro'],sig=['iMac','Mac mini','Mac Pro'],s=K),
 dict(n='Alienware',c='United States',f='1996',seg='Premium',kf='gaming PCs',d='Miami gaming-PC maker founded by Nelson Gonzalez and Alex Aguila, owned by Dell since 2006.',lines=['Aurora','Area-51'],sig=['Alienware Aurora'],rel=['Dell'],s=W+'Alienware'),
 dict(n='Dell',c='United States',f='1984',seg='Mainstream',kf='direct-sold PCs',d='Texan PC maker selling consumer and business desktops, laptops and servers.',lines=['OptiPlex','Precision','PowerEdge','Dell Pro'],sig=['Dell OptiPlex','Dell PowerEdge'],rel=['Alienware'],s=K),
 dict(n='HP',c='United States',f='1939',seg='Mainstream',kf='PCs and printers',d='American maker of PCs and printers.',lines=['Z workstations','Spectre','Omen'],sig=['HP Z workstation'],rel=['HPE'],s=K),
 dict(n='HPE',c='United States',f='2015',seg='Professional & flagship',kf='servers',d='Hewlett Packard Enterprise, the server and networking company split from HP in 2015.',lines=['ProLiant'],sig=['HPE ProLiant MicroServer'],rel=['HP'],s=K),
 dict(n='Intel',c='United States',f='1968',seg='Professional & flagship',kf='processors',d='American chipmaker that also sold NUC mini-PC kits.',lines=['NUC'],sig=['Intel NUC'],rel=['ASUS'],s=K),
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'Archetypes from retrieved Wikipedia pages: Mac Pro, Alienware Aurora, HP Z, iMac, Mac mini, Mac Studio, Dell OptiPlex, Intel NUC, HPE ProLiant MicroServer, Dell PowerEdge. Tower list cut from 74 to 7 models: Dell Precision SKU run trimmed to current models; DECpc, Compaq ProSignia and Epson Endeavor MR7300 dropped as dated SKU noise. Low-profile desktop renamed Small-form-factor desktop: Amiga 1000/1500/2000/2500/3000/4000 and Atari Mega/Mega STE/TT030 go to the Vintage computers shelf (Vintage desktop computer); DECpc LP/LPv/LPx runs dropped. Rack-mount server renamed Home server and cut to two lines with a few homelab-relevant models; enterprise SKU runs (PowerEdge R6xx/R7xx, ThinkSystem, Supermicro) dropped by the scope rule. Tower and AIO models remain Dell-heavy because the old data was a Dell harvest and no new models were researched. MicroServer generation list not given on the retrieved page, so only N36L (named there) is listed; Mac Pro "cheese grater" nickname not on the page, so not used.'}
p='work/D1/shelves/00_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
