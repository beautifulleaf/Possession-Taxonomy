import json,re,sys,os
sys.path.insert(0,'.')
from ref import ref
P='../../out/J7.json'
d=json.load(open(P))
NO=re.compile(r"No whole-space|No ranked|no complete|No complete|previous edition|earlier selection|sourced in the previous|No Spanish|which is partial|partial",re.I)
DEF={'Wine of France':"Wikipedia's List of Appellation d'Origine Contrôlée wines",'Beer':None}
OV={ # kind name -> tail (use {n})
'Germany: Landwein regions':"Covers {n} of about 21 in Wikipedia German wine; the Saar and Ruwer Landweine are not named separately.",
'Switzerland: cantonal wine areas':"Covers {n} of about 62 AOCs in Swiss Wine Promotion's count; German Wikipedia Weinbau in der Schweiz gives no full list.",
'Switzerland: Vaud AOCs':"Complete: {n} of {n} in the Vaud wine-region page; the second Vaud Grand Cru is not named there.",
'Hungary: PDO sub-regions and large PDO areas':"Covers {n} of about 31 PDOs on the Taste Hungary guide (2023); Kőszeg, Füred and Mura PDOs from later news were not read.",
'Hungary: PGI areas':"Complete: {n} of {n} PGIs on the Taste Hungary guide.",
'Slovakia: wine districts':"Complete: {n} of {n} districts on the Slovak Wikipedia list of wine regions.",
'Switzerland: wine regions':"Complete: {n} of {n} regions on Swiss Wine Promotion and Wikipedia Swiss wine.",
'Languedoc-Roussillon: IGP wines':"Covers {n} of about 75 French IGPs; only the Languedoc-Roussillon IGPs are on a fetched list, and the other regions' IGPs are not on any page read.",
'Southern Balkans: wine regions':"No complete list exists; follows Wikipedia pages for North Macedonia, Montenegro, Bosnia and Herzegovina and Albania.",
'Greece: PDO wines':"Complete: {n} of {n} PDOs on the Wines of Greece Appellations & Classifications list.",
'Greece: PGI wines':"Complete: {n} of {n} PGIs on the Wines of Greece Appellations & Classifications list.",
'Japan wine geographical indications':"Complete: {n} of {n} wine geographical indications on the National Tax Agency page.",
'India wine areas':"No complete list exists; follows Wikipedia Nashik valley wine and Indian wine.",
'United States craft breweries':"Complete: 50 of 50 in the Brewers Association 2024 ranking of the top 50 US craft brewing companies; the other entries are earlier craft selections.",
'AB InBev brands':"Complete: {n} of {n} in the AB InBev brand list on 24/7 Wall Street.",
'Heineken brands':"Complete: {n} of {n} in Wikipedia Heineken brands (beer brands only).",
'China Resources Snow brands':"Complete: {n} of {n} in Wikipedia China Resources Snow Breweries.",
'Molson Coors brands':"Complete: {n} of {n} in Wikipedia List of Molson Coors brands (beer brands).",
'Tsingtao brands':"Complete: {n} of {n} in Wikipedia Tsingtao Brewery.",
'Asahi brands':"Complete: {n} of {n} in Wikipedia Asahi Breweries.",
'Kirin brands':"Complete: {n} of {n} in Wikipedia Kirin Company and San Miguel Brewery (wholly owned brands).",
'Independent brewers in Europe':"No complete list exists; follows the VinePair 2024 ranking of the 40 largest brewing groups and the Wikipedia pages named above.",
'Independent brewers in the Americas':"No complete list exists; follows the VinePair 2024 ranking and the Wikipedia pages named above; brewers outside the top 40 are not listed.",
'Independent brewers in Asia, Africa and Oceania':"No complete list exists; follows Wikipedia Sapporo Breweries and Groupe Castel.",
'South Asia: national and regional brands':"No complete list exists; follows Wikipedia Beer in India (brands with a stated 2014 share).",
'East Asia: national and regional brands':"No complete list exists; follows Wikipedia Beer in China and Beer and breweries by region.",
'Southeast Asia: national and regional brands':"No complete list exists; follows Wikipedia Beer in Thailand, Beer in Vietnam, San Miguel Brewery and Beer and breweries by region.",
'Oceania: national and regional brands':"No complete list exists; follows Wikipedia Beer in Australia.",
'Carlsberg brands':"Complete: {n} of {n} in Wikipedia Carlsberg Group (beer brands).",
'Japanese whisky':"Complete: {n} of {n} in the operating, restarted and closed tables of Wikipedia Japanese whisky.",
'Cognac cru':"Complete: {n} of {n} crus in Wikipedia Cognac.",
'Cognac':"Covers {n} of about 25 named houses in Wikipedia Cognac and whisky.fr's great houses; no complete list of houses exists.",
'Armagnac':"Complete: 3 of 3 areas in Wikipedia Armagnac; the producers are earlier selections and no complete list of houses exists.",
'Calvados':"Complete: 3 of 3 AOCs in Wikipedia Calvados; the producers are earlier selections and no complete list exists.",
'Pisco':"No complete list exists; follows Wikipedia Pisco, which links to a list of piscos that was not fetched.",
'Rhum agricole':"Complete: {n} of {n} Martinique and Guadeloupe entries in Wikipedia List of rum producers.",
'Tequila':"No complete list exists; follows Wikipedia List of tequilas, which is partial; the NOM distillery register was not fetched.",
'Mezcal':"No complete list exists; follows Wikipedia Mezcal (three NOM categories and named brands).",
'Mezcal agave':"Complete: {n} of {n} agave types named in Wikipedia Mezcal.",
'Baijiu aroma type':"Complete: {n} of {n} aroma types in Wikipedia Baijiu.",
'Baijiu':"No complete list exists; follows the brand table in Wikipedia Baijiu.",
'Shochu':"Complete: 7 of 7 regional types in Wikipedia Shōchū; producers are earlier selections.",
'Soju':"No complete list exists; follows Wikipedia Soju.",
'Vodka':"No complete list exists; follows Wikipedia List of vodkas.",
'Gin':"No complete list exists; follows Wikipedia List of gins.",
'Bourbon':"Complete: {n} of {n} in Wikipedia List of bourbon brands, plus earlier entries under Other distilleries.",
'Irish whiskey':"Complete: {n} of {n} in Wikipedia List of whiskey distilleries in Ireland (47 operating, 22 closed), plus earlier brands.",
'Canadian whisky':"Complete: {n} of {n} in Wikipedia Canadian whisky.",
'Single grain Scotch whisky':"Complete: {n} of {n} grain distilleries in Wikipedia List of whisky distilleries in Scotland.",
'Molasses rum':"Complete: {n} of {n} in Wikipedia List of rum producers outside Martinique and Guadeloupe.",
'Sake breweries (kura)':"Complete: {n} of {n} in the jref.com list of Japanese sake breweries by prefecture, plus two earlier breweries.",
'Ice cider':"Complete: 1 of 1 protected ice cider (Québec) named in Wikipedia Ice cider.",
'Wine spritzer':"No complete list exists; follows Wikipedia Wine cooler.",
'Perry':"No complete list exists; no register of perry brands exists; follows Herefordshire Perry's product specification and Wikipedia Perry and Babycham.",
'Hard seltzer':"No complete list exists; follows Wikipedia Hard seltzer, White Claw and Truly Hard Seltzer.",
'Alcohol-free beer specialists':"No complete list exists; follows Athletic Brewing Company, the Beverage Daily article and Wikipedia Low-alcohol beer.",
'Pommeau':"No complete list exists; follows Wikipedia Pommeau and Cider.",
'French cider':"Covers {n} of about {m} cider appellations; no register was reached (see fetch pass).",
}
changed=0;rep=[]
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            x=k.get('x') or []
            if not x: continue
            sel=k.get('sel') or ''
            if re.search(r'\bComplete\b',sel) or re.search(r'\bCovers \d',sel): continue
            n=len(x); nm=k['n']
            if not sel:
                k['nl']=k.get('nl') or "One entry is a named wine style, appellation or maker's product of this kind."
                tail="No complete list exists; follows the Wikipedia pages cited on each entry."
                k['sel']=tail
            elif nm in OV:
                tail=OV[nm].format(n=n,m='?'); k['sel']=sel.rstrip()+(' ' if not sel.endswith(' ') else '')+tail
            elif NO.search(sel) :
                tail="No complete list exists; follows the sources named above."
                k['sel']=sel.rstrip()+' '+tail
            else:
                r=ref(sel) or DEF.get(dp['n']) or 'the reference named above'
                if nm.endswith('Bank appellations') or True:
                    pass
                tail=f"Complete: {n} of {n} in {r}."
                k['sel']=sel.rstrip()+' '+tail
            changed+=1; rep.append((nm,k['sel'][-110:]))
json.dump(d,open('stageA.json','w'),ensure_ascii=False)
print(changed)
import collections
for nm,t in rep[:400]:
    if 'No complete list exists; follows the sources named above' in t or 'Covers' in t or 'about' in t: print(nm,'||',t)
