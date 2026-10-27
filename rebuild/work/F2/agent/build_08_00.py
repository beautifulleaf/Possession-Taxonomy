import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
SH=W+"Shufa"; IC=W+"Islamic_calligraphy"; SC=W+"Seal_carving"
kinds=[
 {"n":"East Asian calligraphy","a":"brush calligraphy · shufa · shodō · seoye","d":"Writing made as the picture, in brush, by Chinese, Japanese or Korean tradition.",
  "t":["seal script","clerical script","regular script","running (semi-cursive) script","cursive script","hanging scroll","couplet","handscroll","album leaf","fan"],
  "s":"https://www.1stdibs.com/buy/calligraphy-art",
  "x":[
   {"n":"Chinese calligraphy (shufa)","a":"Chinese brush calligraphy","d":"Chinese brush writing in five main scripts, from Qin seal script to Jin-dynasty running and cursive.","mk":"","y":"Qin onward","s":SH,
    "v":[V("Seal script (zhuanshu)","","latter half of 1st millennium BC","Qin standard"),V("Clerical script (lishu)","","Han"),V("Regular script (kaishu)","","Han–Wei, matured c. 7th century"),V("Wang Xizhi, Lantingji Xu","Wang Xizhi","Jin (303–361)","described as the most famous Chinese calligraphic work")],
    "dt":"script · format · seals and inscriptions · mounting · master or later copy"},
   {"n":"Japanese calligraphy (shodō)","a":"shūji · Zen calligraphy","d":"Japanese brush writing, including kana styles and Zen calligraphy.","mk":"","y":"Heian onward","s":W+"Japanese_calligraphy",
    "v":[V("Three Brush Traces (sanseki)","Ono no Michikaze","Heian","with Fujiwara no Sukemasa and Fujiwara no Yukinari; wayō style")],
    "dt":"kana or kanji · Zen statement · mounting"},
   {"n":"Korean calligraphy (seoye)","a":"Chusa style","d":"Korean artistic writing in Hanja and Hangul; Kim Jeong-hui is regarded as Joseon's top calligrapher.","mk":"","y":"Joseon onward","s":W+"Korean_calligraphy",
    "v":[V("Chusa style, perfected in exile on Jeju","Kim Jeong-hui","1786–1856")],
    "dt":"Hanja or Hangul · five scripts · scroll format"}]},
 {"n":"Islamic calligraphy","a":"Arabic calligraphy · Ottoman calligraphy","d":"Calligraphy in Arabic-script languages, made as framed panels, albums and monograms.",
  "t":["thuluth","naskh","nasta'liq","diwani","hilye","qit'a (single-sheet)","levha (panel)","tughra","muraqqa (album)"],
  "s":IC,
  "x":[
   {"n":"Hilye panel","a":"hilya · hilye-i şerif","d":"An Ottoman calligraphic panel describing Muhammad's appearance and character, in a layout attributed to Hâfiz Osman.","mk":"","y":"17th century","s":W+"Hilya",
    "v":[V("Standard layout attributed to Hâfiz Osman","Hâfiz Osman","1642–1698","head station, belly, crescent, corners, belt, skirt")],
    "dt":"central text · corner names of the four caliphs · verse 21:107 · signature in the skirt"},
   {"n":"Hâfiz Osman calligraphy","a":"Hafız Osman","d":"Work of the Istanbul calligrapher who tutored three sultans and revived older scripts from the tradition of Şeyh Hamdullah.","mk":"","y":"1642–1698","s":W+"H%C3%A2fiz_Osman",
    "v":[V("Pupil Yedikuleli Seyyid 'Abdullah Efendi")],
    "dt":"script · signature · attribution to master vs school"},
   {"n":"Tughra","a":"sultan's monogram","d":"A sultan's calligraphic monogram, seal or signature affixed to official documents.","mk":"","y":"Ottoman","s":IC,
    "v":[V("Reformed by Mustafa Râkim","Mustafa Râkim")],
    "dt":"sultan · document type · decoration"}]},
 {"n":"Western calligraphy","a":"lettering art · calligraphic broadside","d":"Calligraphy in the Latin alphabet, valued for expressive letterforms rather than function.",
  "t":["uncial","Carolingian minuscule","blackletter","italic","Foundational hand","broadside","commissioned document","illuminated (see F1)"],
  "s":W+"Western_calligraphy",
  "x":[
   {"n":"Edward Johnston Foundational hand","a":"Johnston calligraphy","d":"The round broad-pen hand devised by Edward Johnston, who led the revival of Western calligraphy around 1900.","mk":"","y":"1899–1944","s":W+"Edward_Johnston",
    "v":[V("Teaching at the Central School, London","Edward Johnston","1899"),V("Writing & Illuminating, & Lettering","Edward Johnston","1906"),V("Johnston typeface for London Underground","Edward Johnston","1913")],
    "dt":"hand · broad-pen · signed manuscript vs reproduction"}]},
 {"n":"Carved seal","a":"seal carving · zhuanke · 篆刻","d":"Script characters carved into a seal of stone or another material as a work of art, sold as the seal or its impressions.",
  "t":["Shoushan stone","Qingtian stone","Balin stone","ivory","bronze","Zhe School","Hui (Wan) School","Hai School","seal impression"],
  "s":"https://en.pinkoi.com/product/NdvAREyp",
  "x":[
   {"n":"Shoushan stone seal","a":"Fujian seal stone","d":"Seals cut from soft Shoushan stone of northern Fujian, used for seals from the Ming.","mk":"","y":"Ming onward","s":W+"Shoushan_stone_carvings",
    "v":[V("Shoushan stone carving","","Southern dynasties onward")],
    "dt":"stone variety · translucency and colour · carver's signature"},
   {"n":"Qingtian stone seal","a":"Zhejiang seal stone","d":"Seals of soft Qingtian stone, popularised with Shoushan by Song scholar-artists.","mk":"","y":"Song onward","s":SC,
    "v":[V("Song scholar-artist seals","","Song")],
    "dt":"stone · side inscription · school"},
   {"n":"Zhe (Xiling) School seal","a":"Xiling seal","d":"Seals in the Zhejiang school, also called Xiling after the Hangzhou society founded in 1904.","mk":"","y":"Ming–Qing; society 1904","s":W+"Xiling_Seal_Art_Society",
    "v":[V("Xiling Seal Engravers' Society founded","","1904","Hangzhou")],
    "dt":"school · carver · side inscription"}]}
]
trad=[
 T("Chinese seal carving schools","Calligraphy & seals","China","Ming and Qing peaks","Seal-cutting schools: Zhe (Xiling), Hui (Wan) and Hai (Shanghai).","cutting designs into stone seal faces","Qingtian, Shoushan and Balin stone",["Carved seal"],["Xiling Seal Engravers' Society, Hangzhou (1904)"],"Carver signature and school style",SC),
 T("Ottoman calligraphy","Calligraphy & seals","Ottoman Empire","15th–19th century","Calligraphy of Ottoman masters such as Şeyh Hamdullah, Hâfiz Osman and Mustafa Râkim.","reed-pen scripts (thuluth, naskh, diwani)","paper, ink",["Hilye panel","Tughra"],["Istanbul"],"Master attribution, signature, layout",IC),
 T("Korean seoye","Calligraphy & seals","Korea","Joseon onward","Korean artistic writing in Hanja and Hangul.","brush","paper, ink",["Korean calligraphy (seoye)"],[],"Master and period",W+"Korean_calligraphy"),
 T("Japanese shodō","Calligraphy & seals","Japan","Heian onward","Japanese brush writing with kana and Zen calligraphy.","brush","paper, ink",["Japanese calligraphy (shodō)"],[],"Master and period",W+"Japanese_calligraphy")]
notes="Old Calligraphy kind kept as East Asian calligraphy; its model entries map as: Chinese and Japanese calligraphy become archetypes, Arabic calligraphy moves to Islamic calligraphy, seal script (篆書) becomes a type. Left out: levha and qit'a (named only as types; page text did not cover them), Western broadsides (no source), Changhua stone (not on the page). Master calligraphers go to the artist register; illuminated manuscripts stay in F1."
json.dump({"kinds":kinds,"brands":[],"traditions":trad,"notes":notes},open('work/F2/shelves/08_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/08_00.tmp','work/F2/shelves/08_00.json')
