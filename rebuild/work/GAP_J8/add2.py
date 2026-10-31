import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
def f(mkt,who,share,yr,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
LZ='https://www.leinetal24.de/verbraucher/anteile-gummibaerchen-mogelpackung-lidl-preiserhoehungen-haribo-umsatz-zr-92686139.html'
DH='https://www.dhnet.be/conso/consommation/2018/11/27/du-neuf-sur-le-marche-du-bonbon-dont-les-belges-sont-fous-carambar-croque-lutti-pour-concurrencer-haribo-infographie-YR7X5JQOAVCGVM77DE2KYEU73Y/'
UK='https://www.confectionerynews.com/Article/2017/03/13/Uelker-sets-geographic-expansion-plans-with-new-parent-pladis/'
WD='https://web.de/magazine/ratgeber/finanzen-verbraucher/aldi-co-handelsmarken-verdraengen-milka-ritter-sport-42259620'
BJ='https://braziljournal.com/8kuh'
A={'Sweets & confectionery':[
 f("German gummy and fruit-gum sweets","Haribo","56.1 %",2023,LZ,"sales share as reported by Lebensmittelzeitung in November 2023; measure not stated"),
 f("German gummy and fruit-gum sweets","Storck","11 %",2023,LZ,"same report"),
 f("German gummy and fruit-gum sweets","Katjes","9.6 %",2023,LZ,"same report"),
 f("German gummy and fruit-gum sweets","Trolli","4.7 %",2023,LZ,"same report"),
 f("French sweets","Haribo","37.7 %",2018,DH,"article of 27 November 2018; year and source of the figure not stated"),
 f("French sweets","Carambar & Co","14.5 %",2018,DH,"same article"),
 f("French sweets","Lutti","12.7 %",2018,DH,"same article")],
 'Biscuits & crackers':[
 f("Turkish biscuits","Ülker","33.3 %",2016,UK,"number two; sales volume, Nielsen"),
 f("Saudi Arabian biscuits","Ülker","18 %",2016,UK,"number two; Nielsen"),
 f("Egyptian biscuits","Ülker","11 %",2016,UK,"number three; sales volume, Nielsen")],
 'Chocolate':[
 f("Turkish chocolate","Ülker","42.1 %",2016,UK,"volume share, Nielsen; leader"),
 f("German bar chocolate","Private label (Handelsmarken)","34.5 %",2025,WD,"Circana via Lebensmittel Zeitung; above Milka and Ritter Sport combined for the first time")],
 'Bread & bakery':[
 f("Brazilian bread","Grupo Bimbo with Wickbold","about 37 %",2025,BJ,"projected share after the Wickbold deal; Panco second at about 18 %; measure and source of the share not named")]}
for dp in d['depts']:
  if dp['n'] in A: dp['ms']=dp.get('ms',[])+A[dp['n']]
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
