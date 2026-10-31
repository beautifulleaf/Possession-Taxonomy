import json, os
W='https://en.wikipedia.org/wiki/'
OX=W+'Oxford_shoe'; BR=W+'Brogue_shoe'; DE=W+'Derby_shoe'; MO=W+'Monk_shoe'; SA=W+'Saddle_shoe'
CON='hand-welted, Goodyear or Blake construction · last and toe shape · calf, suede, shell cordovan · single or double leather sole, rubber sole'
def X(n,a,d,mk,y,s,v=(),dt=CON): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(v),"dt":dt}
def V(n,mk,y,d): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Oxford","a":"balmoral (US usage)","d":"Lace-up shoe with the eyelet tabs stitched under the vamp (closed lacing).","t":["evening (patent) Oxford"],"s":OX,
 "x":[
  X("Cap-toe Oxford","straight-cap Oxford","Oxford with a separate stitched toe cap; the best-known and most formal everyday Oxford.","","", OX,[
    V("Consul","Church's","1945","Cap-toe Oxford named after the diplomats who wore it"),
    V("Hallam","Crockett & Jones","","Five-eyelet straight-cap Oxford on the 348 last; best-selling Main Line shoe"),
    V("Park Avenue","Allen Edmonds","","Cap-toe balmoral on the 65 last, 360-degree Goodyear welt")]),
  X("Plain-toe Oxford","","Oxford with no toe cap or decoration.","","",OX),
  X("Wholecut","whole-cut Oxford","Oxford cut from a single piece of leather with one back seam.","","",OX,[
    V("Alessandro","Berluti","","One-piece upper cut and shaped by hand; the house's iconic model")]),
  X("Adelaide Oxford","U-throat Oxford","Oxford whose lacing facing is a separate U-shaped piece set into the vamp.","","",
    "https://theshoesnobblog.com/what-is-an-adelaide-oxford-a-guide-to-this-elegant-shoe-style/",[
    V("St James","Gaziano & Girling","","Credited with popularising the Adelaide"),
    V("Westbourne","Crockett & Jones","","Adelaide Oxford")],CON+' · plain, cap-toe or wingtip Adelaide'),
  X("Quarter brogue","","Cap-toe Oxford with perforations only along the cap seam; the most formal brogue.","","",BR),
  X("Semi-brogue","half brogue","Straight toe cap with perforated edge plus a medallion on the toe.","John Lobb","early 1900s",BR,[
    V("Philip II","John Lobb","","Five-eyelet half-brogue Oxford on the 7000 last"),
    V("Westfield","Crockett & Jones","","Five-eyelet half-brogue Oxford on the 341 last")]),
  X("Full brogue","wingtip","Wing-shaped perforated toe cap running down both sides, with a medallion.","","",BR,dt=CON+' · austerity (unperforated) and blind brogue variants'),
  X("Balmoral","","Oxford whose vamp and quarters meet the eyestays at one horizontal seam, often with a toe cap.","","",OX),
  X("Spectator","co-respondent shoe · two-tone brogue","Two-tone full-brogue Oxford, usually white body with black or tan caps.","","",
    "https://www.gentlemansgazette.com/how-to-wear-spectator-shoes/",dt='colour pairing (white/black, white/tan) · Oxford, derby or monk base · broguing')],
 "m":[["Chelsea","Edward Green"],["City II","John Lobb"],["Diplomat","Church's"],["Dubai","Church's"],["Harrington R","Cheaney"],["James","George Cleverley"]]},
{"n":"Derby","a":"blucher (US) · gibson","d":"Lace-up shoe with the eyelet quarters stitched on top of the vamp (open lacing).","s":DE,
 "x":[
  X("Plain derby","","Derby with a plain vamp and no toe cap or decoration.","","1850s",DE),
  X("Norwegian split-toe derby","Norwegian · split-toe derby","Derby with a hand-sewn apron joined edge to edge by a vertical seam at the toe.","","1920s",
    "https://www.edwardgreen.com/discovery/dover",[
    V("Dover","Edward Green","1920s","Hand-sewn split-toe derby on 202, 303 and 606 lasts; lined or unlined")],'lasts · calf, suede, grain · lined or unlined · leather or rubber sole'),
  X("Moc-toe derby","apron derby","Derby with a moccasin-style stitched apron toe, typically Norwegian-welted on a rubber sole.","","",
    "https://www.drakes.com/en-dk/products/paraboot-michael-bordeaux-leather-derby-shoe",[
    V("Michael","Paraboot","","Moccasin-toe derby, Norwegian welt, made in France")],'Norwegian welt · grained or oiled leather · rubber sole'),
  X("Longwing blucher","American brogue · longwing derby","Full-brogue derby whose wings run the length of the shoe to meet at the heel.","","1970s (US peak)",BR,[
    V("Longwing blucher","Alden","","Barrie last, Horween Color 8 shell cordovan, double leather sole")]),
  X("Country brogue derby","country shoe","Heavy full-brogue derby with storm welt and bellows tongue for outdoor wear.","","",
    "https://trickers.com/products/bourton-country-shoe-black",[
    V("Bourton","Tricker's","","Country brogue derby on last 4444, storm welt, leather or Dainite sole")],'storm welt · double leather or Dainite sole · calf, grain, suede'),
  X("Gillie","ghillie brogue","Tongueless full brogue with long laces wrapped round the ankle; worn with Highland dress.","","",BR),
  X("Buck","white buck · bucks","Derby with a buckskin, suede or nubuck upper, classically light with a red sole.","","",DE,dt='white, dirty buck, brown · red brick sole')],
 "m":[["Chambord","Paraboot"],["Harlyn","John Lobb"],["Shannon","Church's"],["Murton","Cheaney"],["Woodbridge","Church's"],["Drake","Loake"],["Robert","Tricker's"]]},
{"n":"Monk strap","a":"monk shoe","d":"Laceless shoe closed by one or more buckled straps across the instep.","s":MO,
 "x":[
  X("Single monk","","Monk shoe with one buckled strap, often with a cap toe.","Edward Green","late 19th century",MO),
  X("Double monk","","Monk shoe with two buckled straps.","","",MO,[
    V("Felsted","Grenson","","Double monk"),V("Lucca","Taft","","Double monk")])],
 "m":[["Chris","Cobbler Union"],["Francis","Cobbler Union"],["Thomas","George Cleverley"],["William","Paraboot"]]},
{"n":"Saddle shoe","a":"saddle oxford","d":"Low-heeled lace-up with a contrasting saddle-shaped panel across the instep.","s":SA,
 "x":[X("Saddle oxford","two-tone saddle shoe","White leather lace-up with a black, brown or navy saddle; created as an indoor sports shoe.","Spalding","1906",
    "https://www.atomretro.com/blog/the-history-of-saddle-shoes/",[V("Sadie","Eastland","","Women's saddle oxford")],
    'saddle colour (black, brown, navy) · leather or suede · rubber or leather sole · golf cleats')]}
]
def B(n,c,f,seg,d,sig,s,lines=(),rel=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":["classic menswear"],"rel":list(rel),"s":s}
brands=[
 B("Edward Green","England","1890","luxury Goodyear-welted","Northampton maker of high-end men's shoes, credited with innovating the monk shoe; known for the Dover.",["Single monk","Norwegian split-toe derby"],"knowledge",rel=["John Lobb","Gaziano & Girling"]),
 B("Crockett & Jones","England","1879","premium Goodyear-welted","Family-owned Northampton shoemaker with Main Line and Hand Grade ranges.",["Cap-toe Oxford","Semi-brogue","Adelaide Oxford"],"knowledge",["Main Line","Hand Grade"],["Church's","Edward Green"]),
 B("Alden","United States","1884","premium American","Massachusetts shoemaker founded by Charles H. Alden, known for shell cordovan and the Indy boot.",["Longwing blucher"],W+"Alden_Shoe_Company",rel=["Allen Edmonds"]),
 B("John Lobb","England","","luxury and bespoke","Name shared by the London bespoke bootmaker and the Hermès-owned ready-to-wear house making shoes in Northampton; credited with the semi-brogue.",["Semi-brogue"],"knowledge",rel=["Edward Green","Berluti"]),
 B("Church's","England","1873","premium Goodyear-welted","Northampton shoemaker founded by the Church family, owned by Prada since 1999.",["Cap-toe Oxford"],W+"Church%27s",rel=["Crockett & Jones","Tricker's"]),
 B("Tricker's","England","1829","country and heritage","Northampton maker of country shoes and boots.",["Country brogue derby"],"knowledge",rel=["Church's"]),
 B("Allen Edmonds","United States","1922","American mainstream premium","Wisconsin shoemaker founded by Elbert W. Allen, owned by Caleres since 2016; maker of the Park Avenue.",["Cap-toe Oxford"],W+"Allen_Edmonds",rel=["Alden"]),
 B("Paraboot","France","","Norwegian-welted casual","French maker of Norwegian-welted shoes with in-house rubber soles, made at Izeaux.",["Moc-toe derby"],"https://desirabilitylab.com/backfill/backfill-2023-14-paraboot-chambord-derby-shoes"),
 B("Berluti","France","1895","luxury","Paris shoemaker founded by Alessandro Berluti, owned by LVMH since 1993; known for patinas and the Alessandro wholecut.",["Wholecut"],W+"Berluti"),
 B("Gaziano & Girling","England","","luxury and bespoke","English maker of high-end ready-to-wear and bespoke shoes whose St James helped popularise the Adelaide.",["Adelaide Oxford"],"knowledge",rel=["Edward Green"]),
 B("Carmina","Spain","","premium Goodyear-welted","Inca, Mallorca shoemaker from a shoemaking family dating to 1866, known for shell cordovan.",[],"https://therake.com/stories/carmina-majorcan-shoemaker",rel=["Meermin"]),
 B("Cheaney","England","1886","premium Goodyear-welted","Northamptonshire shoemaker based in Desborough.",[],"knowledge",rel=["Church's"]),
 B("Loake","England","1880","mid-price Goodyear-welted","Family-owned Kettering shoemaker.",[],"knowledge",rel=["Cheaney"]),
 B("Meermin","Spain","","value Goodyear-welted","Mallorca-based maker of affordable Goodyear-welted shoes.",[],"knowledge",rel=["Carmina"]),
 B("Vass","Hungary","","handmade Hungarian","Budapest shoemaker known for Hungarian-style handmade shoes.",[],"knowledge",rel=["Saint Crispin's"]),
 B("Saint Crispin's","Romania","","luxury handmade","Handmade shoe workshop in Romania.",[],"knowledge",rel=["Vass"]),
 B("George Cleverley","England","","bespoke","London bespoke shoemaker also offering ready-to-wear.",[],"knowledge",rel=["John Lobb"]),
 B("Spalding","United States","","sporting goods","American sporting-goods maker credited with the saddle shoe in 1906.",["Saddle oxford"],"https://www.atomretro.com/blog/the-history-of-saddle-shoes/"),
]
for b in brands: b['sc']=["classic menswear"] if b['n']!="Spalding" else ["Ivy and preppy","sport"]
notes=("Dropped retail-SKU models from DapperFam (Lorenzo, Vero), Giovanni (Mattias, Nico), Belvedere (Chapo, Colombo) and Giorgio Venturi (Monk Elite) per brief. "
 "Kind sources replaced by Wikipedia pages. Models kept in flat m where a retrieved page did not confirm their archetype (e.g. EG Chelsea, JL City II, Church's Diplomat and Shannon, Paraboot Chambord). "
 "Left out for lack of a retrieved source: triple monk, Alden 990 code (Leffot page gives no number), Alden Indy (a boot, belongs to boots shelf), Church's Grafton, Carmina/Cheaney/Loake/Meermin/Vass/Saint Crispin's model names. "
 "Construction is a detail axis (dt), not a kind. church-footwear.com and pradagroup.com returned 503, allenedmonds.ca and otokomaeken 403; not retried. "
 "Several register entries use s=knowledge with founding years only where reliably known.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A2/shelves/02_00.json'
os.makedirs(os.path.dirname(p),exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('ok')
