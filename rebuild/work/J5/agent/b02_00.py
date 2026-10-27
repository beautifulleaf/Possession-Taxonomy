import json,os
W='https://en.wikipedia.org/wiki/'
k=[
{"n":"Porridge oats","a":"rolled oats","d":"Oats steamed and rolled flat, or cut, to cook as porridge.","s":"https://essentialorganicingredients.com/products/nuts-fruits-cacao-nuts-nut-butters-coconut-desiccated-shredded","t":["Jumbo rolled","Rolled","Quick","Steel-cut (pinhead)","Oatmeal (ground)"],
 "m":[["Quaker Oats","Quaker Oats"],["Flahavan's Progress Oatlets","Flahavan's"]]},
{"n":"Ready-to-eat breakfast cereal","a":"","d":"Cereal eaten cold from the box, in flakes, puffs or biscuits.","s":W+"Breakfast_cereal","t":["Flakes","Puffed","Shredded wheat","Biscuit"],
 "m":[["Corn Flakes","Kellogg's"],["Rice Krispies","Kellogg's"],["Weetabix","Weetabix"],["Shredded Wheat","Post Consumer Brands"],["Cheerios","General Mills"]]},
{"n":"Muesli","a":"","d":"Uncooked rolled oats with fruit and nuts, devised by Bircher-Benner around 1900.","s":W+"Muesli","t":["Fresh (soaked)","Packaged dry","Toasted"],
 "m":[["Alpen","Weetabix"],["Dorset Cereals Muesli","Dorset Cereals"]]},
{"n":"Granola","a":"","d":"Sweetened baked oat cereal with nuts and fruit, descended from Granula of 1863.","s":W+"Granola","t":["Clusters","Loose"]}]
def B(n,c,f,seg,kf,d,s):return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
br=[B("Kellogg's","United States","","Mainstream","corn flakes","Maker of Corn Flakes (1894-95) and Rice Krispies (1928).",W+"Corn_flakes"),
B("Weetabix","United Kingdom","1932","Mainstream","wheat biscuits","English maker of Weetabix and Alpen, owned by Post Holdings.",W+"Weetabix"),
B("Quaker Oats","United States","1877","Mainstream","oats","Oat brand owned by PepsiCo since 2001.",W+"Quaker_Oats_Company"),
B("Flahavan's","Ireland","1785","Heritage manufactory","Irish oats","Family oat miller in Kilmacthomas, Waterford.",W+"Flahavan%27s"),
B("Dorset Cereals","United Kingdom","1989","Premium","muesli","Founded by Terry Crabb, owned by Associated British Foods since 2012.",W+"Dorset_Cereals"),
B("General Mills","United States","","Mainstream","Cheerios","Introduced Cheerioats in 1941.",W+"Cheerios")]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Which?/CHOICE test winners not retrieved so not included. Alpen introduced 1971 by Weetabix. Cereal bars are J8."}
json.dump(out,open('work/J5/shelves/02_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/02_00.tmp','work/J5/shelves/02_00.json')
