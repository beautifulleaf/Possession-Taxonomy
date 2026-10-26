import json, os
HF="https://en.wikipedia.org/wiki/Hand_fan"
KS="https://kogeijapan.com/locale/en_US/kyosensu/"
KG="https://kougeihin.jp/en/craft/1411/"
IB="https://www.ibasen.co.jp/en/pages/2304_uchiwa_tradition"
VAL="https://www.craftheritage.world/technique/valencia-fan-making-spain"
WX="https://baike.baidu.com/en/item/Fan%20Making%20Craft%20(Wangxingji%20Fan)/658068"
def X(n,a,d,mk,y,s,v=(),dt=""): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
folding={"n":"Folding fan","a":"sensu · ōgi · zheshan · abanico · éventail","d":"Hand fan of ribs and leaf that pivot at one end and fold closed.",
 "t":["paper leaf","silk leaf","lace leaf","feather","wooden slats","bamboo sticks","bone or horn sticks","hand-painted","printed or lithographed"],
 "s":HF,"x":[
 X("Sensu","ōgi · Japanese folding fan · hariōgi","Japanese pasted fan of paper or silk on bamboo ribs; the folding fan is held to have been invented in Japan.","","6th–9th century",KS,
   [("Kawahori-ōgi","","mid-Heian period","washi on five or six ribs; summer fan"),("Kamisen","","Muromachi period (1336–1573)","bamboo and paper fan"),
    ("Kinusen","","","silk-leaf fan inspired by re-imported European fans"),("Akomeogi","","","court fan named after a court women's garment"),
    ("Mai ōgi","","","dance and Noh fan, ten sticks, thick paper mount often with a family crest"),("Chaōgi","","","tea ceremony fan"),("Shukugisen","","","fan for official events")],
   "leaf paper or silk · ribs madake, hachiku or moso bamboo · gold or silver leaf, hand-painted or woodblock-printed"),
 X("Hiōgi","cypress fan · itaōgi","Japanese fan of thin stacked cypress slats bound with thread, the oldest Japanese fan form.","","877 (oldest dated example, Tōji)",KS,[],"slats cypress, cedar or sandalwood · foil and painted decoration"),
 X("Brisé fan","brisé","Folding fan made only of decorated sticks joined by a ribbon, with no separate leaf; a Chinese innovation.","","",HF,[],"sticks ivory, bone, horn, wood, tortoiseshell or mother-of-pearl · carved, pierced or painted"),
 X("Cockade fan","cocarda fan","Folding fan whose leaf opens through a full 360° circle around its pin.","","",HF,[],"leaf paper or silk · handle guards"),
 X("Spanish abanico","abanico valenciano · Valencian fan","Spanish pleated fan with a painted paper or silk leaf on wood or bone sticks, made mainly around Valencia.","","documented from the 1750s",VAL,[],"leaf laid paper or silk · sticks wood or bone · gouache florals and scenes, hand-painted or lithographed"),
 X("Abaniko","Filipino folding fan","Philippine folding fan of the Spanish colonial period, worn with the baro't saya.","","",
   "https://en.wikipedia.org/wiki/Abaniko",[],"painted art abanikos"),
 X("Hangzhou black paper fan","Wangxingji fan · heizhishan","Chinese folding fan of persimmon-lacquered mulberry paper on brown bamboo ribs, made in some 86 steps.","Wangxingji","1875",WX,
   [("Sandalwood fan","Wangxingji","",""),("Silk fan","Wangxingji","",""),("Opera fan","Wangxingji","",""),("Dance fan","Wangxingji","","")],
   "ribs wild brown bamboo · persimmon-lacquered paper · gold and silver powder, painting, calligraphy · horn rivets"),
 X("War fan","tessen · gunsen · iron fan","Japanese samurai folding fan with iron or metal outer guards, used for signalling and defence.","","Edo period examples (c. 1800–1850)",
   "https://en.wikipedia.org/wiki/Tessen",[("Gunsen","","","folding fan of ordinary warriors, wood or bronze inner spokes"),("Tessen","","","heavy iron outer plates; also solid fan-shaped clubs")],"iron or brass guards · lacquered paper"),
 X("Harisen","slapping fan","Large pleated paper fan kept folded shut, the slapstick prop of manzai comedy.","","","https://en.wikipedia.org/wiki/Harisen",[],"paper"),
 X("Drag fan","performance fan","Oversized folding fan, often 30 cm or more in radius, used for performance.","","",HF,[],"radius 30 cm and over · fabric or paper leaf"),
 ],"m":[]}
folding.pop("m")
rigid={"n":"Rigid fan","a":"fixed fan · flat fan · uchiwa · tuanshan · screen fan","d":"Hand fan with a fixed flat leaf on a handle.",
 "t":["paper","silk","woven palm leaf","feathers","bamboo frame","papier-mâché"],"s":HF,"x":[
 X("Uchiwa","Japanese flat fan","Japanese rigid fan of paper on a bamboo frame, made in regional styles.","","",IB,
   [("Kyō uchiwa","","Edo period (Gosho uchiwa)","sashie construction: ribs and handle separate; 50–100 ribs on fine pieces"),
    ("Marugame uchiwa","","early Edo period","handle and ribs from one piece of bamboo; about 90% of Japan's fans"),
    ("Bōshū uchiwa","","Meiji period","round onadake-bamboo handle and lattice 'window' of split ribs"),
    ("Edo uchiwa","","Edo period","Edo-style fans with ukiyo-e designs")],"paper or silk face · bamboo ribs and handle · printed or painted"),
 X("Tuanshan","gongshan · palace fan · round silk fan","Chinese round or oval silk fan on a bamboo or ivory frame, painted or embroidered.","","Eastern Han dynasty",
   "https://en.wikipedia.org/wiki/Tuanshan",[("Queshan","","","moon-shaped wedding fan held before a bride's face"),("Hexagonal tuanshan","","late Qing","")],"silk · bamboo or ivory frame · painting, calligraphy, embroidery"),
 X("Gunbai","gunbai-uchiwa","Japanese rigid war fan of wood or metal, now carried by sumo referees.","","","https://en.wikipedia.org/wiki/Gunbai",[],"wood, metal-covered wood or solid metal"),
 X("Pamaypay","paypay · buri fan · anahaw fan","Heart-shaped Philippine fan twill-woven from buri or anahaw palm with a looped handle.","","",
   "https://en.wikipedia.org/wiki/Pamaypay",[],"buri or anahaw palm · sawali weave · braided edge"),
 X("Palm-leaf fan","pushan · pukuishan","Chinese fan woven from the leaves and stalks of the Chinese fan palm.","","",HF,[],"Livistona chinensis leaf"),
 X("Feather fan","yushan","Chinese fan of a row of feathers mounted at the end of a handle.","","",HF,[],"feathers · handle"),
 X("Screen fan","éventail à écran","Flat screen of silk, wood, leather or papier-mâché on a fixed handle, used indoors in 18th–19th-century Europe.","","18th–19th century",HF,
   [("Papier-mâché screen fan","Jennens and Bettridge","19th century","Birmingham")],"silk, wood, leather or papier-mâché"),
 X("Bincana","","Odia handheld fan from Odisha, India.","","",HF,[],""),
 ]}
trads=[
 {"n":"Kyō-sensu","g":"Paper, fans & lacquer","r":"Kyoto, Japan (Kyoto, Uji, Kameoka, Nantan)","p":"early Heian period to present; traditional craft 1977",
  "d":"Kyoto folding fans of bamboo ribs and paper or silk, made by many specialist artisans.","tech":"rib splitting and polishing, leaf pasting, gold leaf, hand painting or woodblock printing, folding (some 87 processes)",
  "mat":"madake, hachiku or moso bamboo; washi, silk; cypress, cedar or sandalwood for wooden fans; gold, silver or tin foil",
  "forms":["Sensu","Hiōgi","Mai ōgi","Chaōgi"],"ctr":["Kyoto City","Uji","Kameoka","Nantan"],"auth":"","s":KG},
 {"n":"Kyō uchiwa","g":"Paper, fans & lacquer","r":"Kyoto City and Nantan, Japan","p":"Nanboku-chō roots; Edo-period Gosho uchiwa; traditional craft 1977",
  "d":"Kyoto flat fans whose ribs and handle are made separately, historically painted by court painters.","tech":"sashie construction: ribs inserted into a separate handle","mat":"bamboo, paper",
  "forms":["Uchiwa"],"ctr":["Kyoto City","Nantan"],"auth":"separate handle (sashie); fine pieces have 50–100 ribs","s":IB},
 {"n":"Marugame uchiwa","g":"Paper, fans & lacquer","r":"Marugame, Kagawa, Japan","p":"early Edo period to present; traditional craft 1997",
  "d":"Flat bamboo fans first sold to Kotohira Shrine pilgrims; Marugame now makes most of Japan's uchiwa.","tech":"handle and ribs split from one piece of bamboo; flat-handle style dominant since Meiji",
  "mat":"bamboo, paper, paste","forms":["Uchiwa"],"ctr":["Marugame"],"auth":"one-piece bamboo frame; most output is machine-made plastic, bamboo fans are hand-made","s":"https://www.kensanpin.org/en/product/craft/1006/"},
 {"n":"Bōshū uchiwa","g":"Paper, fans & lacquer","r":"Tateyama and Minamibōsō, Chiba, Japan","p":"Meiji period to present; traditional craft 2003",
  "d":"Chiba flat fans with a round bamboo handle and a lattice 'window' of thread-bound ribs.","tech":"one medake culm split into about 48–64 ribs, interlaced with thread, curved support of madake",
  "mat":"medake and madake bamboo; washi, silk or cotton","forms":["Uchiwa"],"ctr":["Tateyama","Minamibōsō","Funakata","Tomiura"],"auth":"round handle and semicircular lattice window","s":"https://kogeijapan.com/locale/en_US/boshuuchiwa/"},
 {"n":"Valencian fan making","g":"Paper, fans & lacquer","r":"Valencia and l'Horta, incl. Aldaia, Spain","p":"documented from the 1750s; 19th-century export peak",
  "d":"Spain's main fan centre, making painted paper and silk folding fans, about 70% of Spanish output.","tech":"leaf cut and pleated, painted in gouache, mounted on the monture and riveted",
  "mat":"laid paper or silk leaves; wood or bone sticks","forms":["Spanish abanico"],"ctr":["Valencia","Aldaia","Millán workshop","Museo del Abanico de Valencia"],"auth":"","s":VAL},
 {"n":"Hangzhou fan making (Wangxingji)","g":"Paper, fans & lacquer","r":"Hangzhou, Zhejiang, China","p":"1875 to present; national intangible heritage 2008",
  "d":"Hangzhou folding-fan craft, best known for persimmon-lacquered black paper fans.","tech":"some 86 steps: bamboo shaving, lime boiling, heat straightening, pasting, hand-pleating, persimmon-tannin colouring",
  "mat":"wild brown bamboo, Tianmu mulberry paper, Zhuji persimmon lacquer, buffalo-horn rivets","forms":["Hangzhou black paper fan"],"ctr":["Fans Lane, Hangzhou","Wangxingji"],"auth":"","s":WX}]
brands=[
 {"n":"Wangxingji","c":"China","f":"1875","seg":"traditional fan maker","d":"Hangzhou fan house founded by Wang Xingzhai, making over 400 fan varieties.",
  "lines":["black paper fans","sandalwood fans","silk fans","opera and dance fans"],"eras":[],"sig":["Hangzhou black paper fan"],"sc":[],"rel":[],"s":WX},
 {"n":"Duvelleroy","c":"France","f":"1827","seg":"fan house","d":"Paris fan maker founded by Jean-Pierre Duvelleroy, supplier to Queen Victoria; also leather goods.",
  "lines":["fans","leather goods"],"eras":["Jean-Pierre Duvelleroy, from 1827"],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Duvelleroy"},
 {"n":"Ibasen","c":"Japan","f":"1590","seg":"traditional fan shop","d":"Long-established Japanese uchiwa and fan shop that also published ukiyo-e prints in the late Edo period.",
  "lines":["Edo-style uchiwa","sensu"],"eras":[],"sig":["Uchiwa"],"sc":[],"rel":[],"s":IB}]
notes=("Old named forms became archetypes or versions (Abaniko, Akomeogi, Brisé, Cocarda→Cockade fan, Harisen, Hiōgi, Mai ogi, Tessen; Gunbai-uchiwa, Pamaypay, Pushan, Queshan, Screen fan, Tuanshan, Yushan, Bincana). "
 "Left out as ceremonial/liturgical, not sensibly owned: Flabellum, Rhipis (rhipidion), Wumingshan (imperial ceremonial fan) — note for F4 (religious/ceremonial objects). "
 "Battery/hand-cranked mechanical hand fans not added (portable climate, B7). Edo uchiwa kept only as a version: no page confirming a craft designation was retrieved. "
 "Wikipedia 'Uchiwa' URL resolves to Hand fan, so uchiwa cites the Ibasen tradition page. No authenticity markers found for Kyō-sensu, Valencia or Hangzhou.")
out={"kinds":[folding,rigid],"brands":brands,"traditions":trads,"notes":notes}
p="work/A4/shelves/06_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
