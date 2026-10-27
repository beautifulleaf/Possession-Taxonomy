import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
K="knowledge"
CU="https://www.burton.com/de-at/blogs/the-burton-blog/from-prototype-to-icon-burton-custom-turns-30"
SO="https://www.burton.com/blogs/the-burton-blog/step-on_evolution"
SW="https://en.wikipedia.org/wiki/Splitboard"
OG="https://www.outdoorgearlab.com/topics/snow-sports/best-splitboard?specs=n&sort_field=6"
kinds=[
 {"n":"Snowboard","a":"","d":"Single wide board ridden sideways down snow with both feet bound to it.",
  "t":["camber","rocker","hybrid camber (C2, Flying V)","flat","true twin","directional twin","directional / powder","all-mountain","freestyle / park","freeride","women's","kids'"],
  "s":"https://www.rei.com/c/snowboards",
  "x":[
   X("Custom","Burton's all-mountain board, unveiled in January 1995 for the 1995/96 season; one of the most copied boards.","Burton","1995",CU,
     [("Custom (camber)","Burton","1995",""),("Custom X","Burton","2004",""),("Custom V-Rocker","Burton","2010",""),("Custom Flying V","Burton","2011","rocker between and outside the feet, camber underfoot")],
     "profile · length · wide"),
   X("T.Rice Pro","Travis Rice's pro-model board with Magne-Traction serrated edges.","Lib Tech","2010","https://methodmag.com/industry-news/lib-technologies-introduces-travis-rice-pro-model.html",
     [("T. Rice Pro","Lib Tech","","")],"profile (C2 or camber) · length"),
  ],
  "m":[["Feelbetter","Bataleon"],["Cultivator Flat Top","Burton"],["Spellbinder","Burton"],["Micro Mini","Capita"],["Frontier 2.0","Jones"],["Mountain Twin","Jones"],
       ["Assassin","Salomon"],["Assassin Pro","Salomon"],["Huck Knife Pro","Salomon"],["Sight","Salomon"],["Dancehaul","Salomon"],["Lotus","Salomon"],["Wonder","Salomon"]]},
 {"n":"Snowboard binding","a":"","d":"Non-release binding with highback and straps that fixes a boot to a snowboard.",
  "t":["strap-in","rear-entry","step-on (boot-integrated)","2x4 / 4x4 / channel mount","flex rating"],"s":"https://www.salomon.com/en-us/shop/sports/alpine-skiing.html",
  "x":[
   X("Step On","Burton's strapless system in which matching boots click into the binding at toe and heel.","Burton","",SO,
     [("Rear entry prototype","Burton","1993",""),("Step In","Burton","1999","original step-in binding"),("Step On EST","Burton","2020","")],"needs Step On boots")],
  "m":[["Force","Union"],["Strata","Union"],["Atlas","Union"]]},
 {"n":"Snowboard boot","a":"","d":"Soft or stiff boot made to fit a snowboard binding.","t":["traditional laces","speed lace","Boa dial","flex soft to stiff","Step On compatible"],
  "s":"https://www.salomon.com/en-us/shop/sports/alpine-skiing.html",
  "m":[["Photon","Burton"],["Photon Boa","Burton"],["Photon Step On","Burton"],["Lasso Boa","Ride"]]},
 {"n":"Splitboard","a":"split board","d":"Snowboard that splits into two ski-like halves for climbing and rejoins for descent.","t":["full camber","hybrid","powder shape","puck or track binding interface"],
  "s":"https://www.rei.com/c/winter-traction-devices",
  "x":[
   X("Voile Split Kit","DIY kit to cut and join a snowboard as a splitboard, refined from Brett Kobernik's prototype.","Voile","1994",SW,[],"")],
  "m":[["Solution","Jones"],["Ultralight Stratos","Jones"],["Hovercraft 2.0","Jones"],["Frontier","Jones"],["Transition Finder Split","Korua"],["Goat Pro Carbon","Cardiff"],
       ["Crane Enduro","Cardiff"],["Spartan Ascent","Voile"],["Swift","Never Summer"]]},
]
brands=[
 {"n":"Burton","c":"United States","f":"1977","seg":"Professional & flagship","kf":"snowboards","d":"Snowboard maker founded by Jake Burton Carpenter in Vermont.","sig":["Custom","Step On"],"s":K},
 {"n":"Lib Tech","c":"United States","seg":"Premium","kf":"snowboards","d":"Lib Technologies, Washington-state snowboard maker known for Magne-Traction edges.","sig":["T.Rice Pro"],"s":"https://methodmag.com/industry-news/lib-technologies-introduces-travis-rice-pro-model.html"},
 {"n":"Voile","c":"United States","seg":"Specialist","kf":"splitboards, backcountry","d":"Backcountry gear maker founded by Mark Wariakois; pioneer of splitboards.","sig":["Voile Split Kit"],"s":SW},
 {"n":"Jones","c":"United States","seg":"Premium","kf":"freeride snowboards, splitboards","d":"Jones Snowboards, founded by Jeremy Jones.","s":K},
 {"n":"Union","c":"United States","seg":"Premium","kf":"snowboard bindings","d":"Snowboard binding maker.","s":K},
]
notes=("All 4 old kinds kept. Snowboard: 24 models (17 Salomon, retail skew) cut to Custom and T.Rice Pro archetypes + 13 models; dropped Salomon Bliss, Craft, Highpath, Indicator, "
 "Jetstream, Kickback, No Drama, Oh Yeah, Rumble Fish, Sleepwalker (long-tail SKUs). Bindings, boots and splitboards had no models; added tested models and Step On / Voile Split Kit archetypes. "
 "Not done: Process, Flight Attendant, Capita DOA, GNU, Ride, Nitro lines, Nidecker Supermatic, K2 boots, Spark R&D bindings - no retrieved page gave line facts.")
w('E2','11_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
