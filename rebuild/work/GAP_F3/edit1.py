import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
W='https://en.wikipedia.org/wiki/'
def kind(n):
    for dp in d['depts']:
        for sh in dp['s']:
            for k in sh.get('k',[]):
                if k['n']==n: return k
def add(k,rows):
    have={e['n'].lower() for e in k['x']}
    c=0
    for n,y,dsc,page,g in rows:
        if n.lower() in have: continue
        k['x'].append({"n":n,"a":"","d":dsc,"mk":"","y":y,"s":W+page,"v":[],"g":g}); c+=1
    return c
US='United States'
camp=[
("Indian Campaign Medal","1907","Army medal, authorised retroactively, for service in conflicts with Native Americans between 1865 and 1891.","Indian_Campaign_Medal",US),
("Army of Cuban Occupation Medal","1915","Medal for garrison duty in Cuba between 1898 and 1902, after the Spanish-American War.","Army_of_Cuban_Occupation_Medal",US),
("Army of Puerto Rican Occupation Medal","1919","Retrospective Army medal for occupation duty in Puerto Rico in 1898.","Army_of_Puerto_Rican_Occupation_Medal",US),
("China Campaign Medal","1905","Army medal for service in China with the China Relief Expedition, 20 June 1900 to 27 May 1901.","China_Campaign_Medal",US),
("China Relief Expedition Medal","1908","Navy and Marine Corps medal for service in China during the Boxer Rebellion, 1900 to 1901.","China_Relief_Expedition_Medal",US),
("Mexican Service Medal","1917","Medal for service against Mexican forces in engagements between 1911 and 1919.","Mexican_Service_Medal",US),
("Dominican Campaign Medal","1921","Navy and Marine Corps medal for duty in the Dominican Republic between 5 May and 4 December 1916.","Dominican_Campaign_Medal",US),
("Haitian Campaign Medal","1917","Navy and Marine Corps medal for the occupation of Haiti; a second version of 1921 covers 1919 to 1920.","Haitian_Campaign_Medal",US),
("Nicaraguan Campaign Medal","1913","Navy and Marine Corps medal for amphibious actions in Nicaragua from 29 July to 14 November 1912.","Nicaraguan_Campaign_Medal",US),
("Second Nicaraguan Campaign Medal","1929","Navy medal for service in Nicaragua and nearby naval operations from 1926 to 1933.","Second_Nicaraguan_Campaign_Medal",US),
("Philippine Congressional Medal","1906","Medal for Army soldiers who volunteered to serve in the Philippine-American War.","Philippine_Congressional_Medal",US),
("West Indies Campaign Medal","1908","Navy and Marine Corps medal for sea duty in the West Indies, May to August 1898.","West_Indies_Campaign_Medal",US),
("Sampson Medal","1901","Navy and Marine Corps medal for service in Rear Admiral Sampson's fleet in Cuban waters in 1898.","Sampson_Medal",US),
("Cuban Pacification Medal","1909","Obsolete Navy medal for service ashore in Cuba or on listed ships during 1906 to 1909.","Cuban_Pacification_Medal",US),
("American Defense Service Medal","1941","Medal for active-duty service before the attack on Pearl Harbor, 8 September 1939 to 7 December 1941.","American_Defense_Service_Medal",US),
("World War II Victory Medal","1945","Medal given to anyone in uniform from 7 December 1941 to 31 December 1946.","World_War_II_Victory_Medal_(United_States)",US),
("Army of Occupation of Germany Medal","1941","Army medal for service in Germany or Austria-Hungary from November 1918 to July 1923.","Army_of_Occupation_of_Germany_Medal",US),
("National Defense Service Medal","1953","Service medal for any member serving in one of four designated periods between 1950 and 2022; no combat needed.","National_Defense_Service_Medal",US),
("Korea Defense Service Medal","2002","Service medal for 30 consecutive or 60 non-consecutive days supporting South Korea's defence.","Korea_Defense_Service_Medal",US),
("Kosovo Campaign Medal","2000","Campaign medal for service in Kosovo from 24 March 1999 to 31 December 2013.","Kosovo_Campaign_Medal",US),
("Southwest Asia Service Medal","1991","Campaign medal for the Persian Gulf War and afterward, August 1990 to November 1995.","Southwest_Asia_Service_Medal",US),
("Inherent Resolve Campaign Medal","2016","Medal for service in Iraq or Syria, applied retroactively to 15 June 2014.","Inherent_Resolve_Campaign_Medal",US),
("Global War on Terrorism Service Medal","2003","Service medal for support of counter-terrorism efforts since 11 September 2001.","Global_War_on_Terrorism_Service_Medal",US),
("Armed Forces Service Medal","1996","Service medal for designated high-impact operations that involved no combat with foreign forces.","Armed_Forces_Service_Medal",US),
("Humanitarian Service Medal","1977","Medal for members who distinguish themselves in designated humanitarian missions such as disaster relief.","Humanitarian_Service_Medal",US),
("Merchant Marine Pacific War Zone Medal","1944","Medal for seamen on War Shipping Administration vessels in the Pacific War Zone, 1941 to 1946.","Merchant_Marine_Pacific_War_Zone_Medal",US),
("Merchant Marine Atlantic War Zone Medal","1944","Ribbon of 1944 (medal added 1992) for crews in the Atlantic War Zone, 7 December 1941 to 8 November 1945.","Merchant_Marine_Atlantic_War_Zone_Medal",US),
("Merchant Marine Mediterranean-Middle East War Zone Medal","1944","Medal for crews of War Shipping Administration ships in the Mediterranean-Middle East war zone, 1941 to 1945.","Merchant_Marine_Mediterranean-Middle_East_War_Zone_Medal",US),
("Coast and Geodetic Survey Atlantic War Zone Medal","1945","Ribbon of 1945 (medal authorised 1988) for survey personnel who served in or just after World War II.","Coast_and_Geodetic_Survey_Atlantic_War_Zone_Medal",US),
("Coast and Geodetic Survey Pacific War Zone Medal","1945","Ribbon of 1945 (medal authorised 1988) for survey personnel in the Pacific War Zone in World War II.","Coast_and_Geodetic_Survey_Pacific_War_Zone_Medal",US),
("Public Health Service Global Health Campaign Medal","","Public Health Service medal for contributions to a Global Health initiative mission outside the United States.","Public_Health_Service_Global_Health_Campaign_Medal",US),
("Public Health Service COVID-19 Pandemic Campaign Medal","2020","Public Health Service medal for those who supported the national COVID-19 response.","Public_Health_Service_COVID-19_Pandemic_Campaign_Medal",US),
("Public Health Service Ebola Campaign Medal","","Public Health Service medal for service in an international Ebola response on or after 31 March 2014.","Public_Health_Service_Ebola_Campaign_Medal",US),
("Public Health Service Smallpox Eradication Campaign Ribbon","","Public Health Service ribbon for smallpox eradication service, 1 January 1966 to 26 October 1977.","Public_Health_Service_Smallpox_Eradication_Campaign_Ribbon",US),
]
ck=kind('Campaign medal'); nc=add(ck,camp)
gal=[
("Valorous Unit Award","1966","Army unit award ranking just below the Presidential Unit Citation, for exceptional bravery against an armed enemy.","Valorous_Unit_Award",US),
("Army Superior Unit Award","1985","Army peacetime unit award for outstanding meritorious performance on a difficult and challenging mission.","Army_Superior_Unit_Award",US),
("Army Meritorious Unit Commendation","1946","Army unit award for units that served with distinction for six months or more against an armed enemy.","Meritorious_Unit_Commendation",US),
("Joint Meritorious Unit Award","1981","Defense Department award for multi-service units with outstanding achievement in combat or national emergencies.","Joint_Meritorious_Unit_Award",US),
("Joint Service Commendation Medal","","Defense Department version of the Commendation Medal for heroism or meritorious service in joint assignments.","Joint_Service_Commendation_Medal",US),
("Joint Service Achievement Medal","1983","Defense Department version of the Achievement Medal, one of the branch-specific series begun in 1961.","Joint_Service_Achievement_Medal",US),
("Defense Meritorious Service Medal","1977","Defense Department award for meritorious service in joint assignments, below the Defense Superior Service Medal.","Defense_Meritorious_Service_Medal",US),
("Homeland Security Distinguished Service Medal","2003","Homeland Security award to armed forces members, equal to the Defense Distinguished Service Medal.","Homeland_Security_Distinguished_Service_Medal",US),
("Army Reserve Components Achievement Medal","","Army award for Reserve Component members, listed in the article on Department of the Army awards.","Awards_and_decorations_of_the_United_States_Department_of_the_Army",US),
]
gk=kind('Gallantry and merit decoration'); ng=add(gk,gal)
ls=[
("Army Good Conduct Medal","","Army version of the good conduct medal for three years of service without disciplinary infractions.","Army_Good_Conduct_Medal",US),
("Armed Forces Reserve Medal","1950","Service medal for reserve component members, with hourglass devices for years of service.","Armed_Forces_Reserve_Medal",US),
("Army Overseas Service Ribbon","1981","Army ribbon for completed overseas tours of duty.","Army_Overseas_Service_Ribbon",US),
("Military Outstanding Volunteer Service Medal","1993","Medal for service members who make significant unpaid contributions to their civilian communities.","Military_Outstanding_Volunteer_Service_Medal",US),
]
lk=kind('Long-service and good-conduct medal'); nl=add(lk,ls)
# sel lines
ck['sel']=ck['sel'].replace("the Army section was not read.","the Army section was read through the Department of the Army awards article, the inter-service awards article and the Wikipedia category United States campaign medals (36 pages): Complete: every campaign medal of that category not already held is now an entry (the category's three Public Health Service and two Coast and Geodetic Survey medals included); Army marksmanship, recruiting and training ribbons are out of scope.")
gk['sel']=gk['sel'].replace("and the Army and Joint sections were not read.","and the Army and Joint awards read through the Department of the Army awards and inter-service awards articles; Army and Joint decorations and unit awards are now entries.")
lk['sel']=lk['sel'].rstrip()+" Army good-conduct and overseas-service ribbons and the Armed Forces Reserve Medal were added from their Wikipedia articles."
# g for missing
G={'2013 James Joyce €10 coin':'Central Bank of Ireland','2000 Australian dollar and ten cent mule':'Royal Australian Mint',
'Pavia siege money':'Holy Roman Empire','Leiden siege coins':'Dutch Republic','Newark siege pieces':'England','Pontefract siege pieces':'England','Scarborough siege pieces':'England','Carlisle siege pieces':'England','Westphalian Notgeld coins':'Germany',
'Supermarket trolley token':'Various makers','US sales tax tokens':'Various makers','Encased lucky cent':'Various makers','British coronation and jubilee medals':'Various makers','So-called dollar':'Various makers','French Art Nouveau medals and plaquettes':'France','Mahogany collector\'s cabinet':'Various makers','Handmade coin cabinet':'Various makers'}
ng2=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh.get('k',[]):
            if 'xg' in k:
                for e in k['x']:
                    if 'g' not in e and e['n'] in G: e['g']=G[e['n']]; ng2+=1
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
print(nc,ng,nl,ng2)
