import json, os
W='https://en.wikipedia.org/wiki/'
JS=W+'Japanese_saw'; JC=W+'Japanese_chisel'; PT=W+'Plane_(tool)'; SU=W+'Sumitsubo'
CV='https://covingtonandsons.com/2020/05/30/the-japanese-gennou-handle-part-4-the-varieties-of-gennou-kataguchi-ryoguchi-daruma/'
WH='https://workshopheaven.com/gyokucho-japanese-210mm-ryoba-and-240mm-dozuki-saw-set/'
MZ='https://www.japanesetools.com.au/collections/smoothing-planes/products/chizoku-hiraganna-plane-by-mizuno-san-42mm'
TB='https://japanesetools.com.au/products/tachibana-65mm-hikohki-ganna'
DI='https://www.dictum.com/en/japanese-planes-baeh/small-smoothing-plane-717097'
ZF='https://www.silverhandstore.com/products/zetsaw-flush-s-145-kugihiki-nokogiri-japanese-saw'
ZD='https://www.silverhandstore.com/products/zetsaw-dozuki-fine-150-dozuki-nokogiri-japanese-saw'
WC='https://www.woodcraft.com/blogs/woodcarving/japanese-woodworking-chisels'
SH='https://www.timbecon.com.au/collections/japanese-tools/products/shinwa-sashigane-square-30cm-with-metal-stop'
MA='https://www.knivesandstones.com.au/pages/maker/masuda-kiridashi-factory'
KG='https://kogeijapan.com/locale/en_US/banshumikiuchihamono/'
LV='https://www.leevalley.com/en-us/shop/tools/hand-tools/saws/japanese'
def X(n,d,s,mk='',a='',y='',v=None,dt=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',d='',y=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Kanna (Japanese plane)","a":"kanna · Japanese plane · pull plane","d":"Japanese plane with a wooden block and a laminated blade wedged into it, cutting on the pull stroke.","s":"https://www.dictum.com/en/japanese-planes-baeh/small-smoothing-plane-717097",
  "t":["white paper steel (shirogami) blade","blue paper steel (aogami) blade","white oak block","blade width (42–70 mm and up)"],
  "x":[X("Hira-ganna","Standard flat-soled Japanese smoothing plane, adjusted by tapping the blade or block with a small hammer.",MZ,a="hiraganna · smoothing plane",
        v=[V("Chizoku hiraganna","Seisuke Mizuno","hand-forged blue paper #1 blade; long, tall block; Niigata"),V("Mamehiraganna","","shorter 42–48 mm hira-ganna ('mame' = small)"),V("Small Smoothing Plane 717097","DICTUM","white paper steel, Japanese white oak block, 40° bed")],
        dt="blade width · steel (shirogami, aogami) · block wood and length"),
       X("Shiage-ganna","Finishing plane taking a lighter shaving than a Western smoother, pulled with both hands.",PT,a="polishing plane · finishing plane"),
       X("Hikōki-ganna","Winged thicknessing plane whose sliding wings set the cut height for planing stock to repeatable thickness.",TB,a="hikohki-ganna · aeroplane plane",
        v=[V("65 mm Hikohki-ganna","Tachibana","blue paper #1 blade by smith Takeo Nakano; bamboo hold-down bar")],dt="")]},
 {"n":"Ryoba saw","a":"double-edged Japanese pull saw","d":"Thin Japanese hand saw with crosscut teeth on one edge and rip teeth on the other, cutting on the pull stroke.","s":LV,
  "t":["240 mm (general carpentry)","270 mm (larger work)","replaceable blade (kaeba)","traditional fixed blade"],
  "x":[X("Ryoba","Multi-purpose pull saw with crosscut and rip edges on one blade.",JS,
        v=[V("Bluehard Ryoba 210 mm","Gyokucho","replaceable blade S-649")],dt="blade length · tooth pitch · handle (rattan or plastic)"),
       X("Azebiki","Small ryoba with a convex blade that can start a cut in the middle of a board, for mortises, grooves and sliding dovetails.",JS)]},
 {"n":"Dozuki saw","a":"backed Japanese pull saw","d":"Japanese pull saw whose thin fine-toothed blade is stiffened by a steel back, for joinery.","s":LV,
  "t":["dovetail (rip) teeth","tenon (crosscut) teeth","replaceable blade","traditional fixed blade"],
  "x":[X("Dozuki","Backsaw with a much thinner blade than a Western backsaw, for tenons and dovetails.",JS,
        v=[V("373 professional dozuki 240 mm","Gyokucho","25.4 tpi; replacement blade S-370"),V("Dozuki Fine 150","Z-Saw","Zetsaw 07103; 0.3 mm blade, 25 tpi, rattan handle"),
           V("Dozuki-Me Tenon Saw","Z-Saw",""),V("Ikedame Dovetail Saw","Z-Saw",""),V("Tatebiki Dovetail Saw","Shokunin","")],
        dt="blade length · tooth pitch · blade thickness")]},
 {"n":"Kataba saw","a":"single-edged Japanese pull saw","d":"Japanese pull saw with teeth on one edge only and no back, for deeper crosscuts and rips than a dozuki allows.","s":"https://www.woodcraft.com/collections/japanese-handsaws",
  "t":["crosscut","rip","combination teeth"],
  "x":[X("Kataba","Single-edged pull saw, easy to use with a saw guide, for larger work or flush cutting.",JS)]},
 {"n":"Flush-cut saw","a":"kugihiki · azebiki · flush-cut pull saw","d":"Japanese pull saw with a flexible blade and unset teeth that cuts flush against a surface.","s":LV,
  "x":[X("Kugihiki","Thin flexible flush-cut saw with unset teeth on one side, for trimming dowels and tenons flush.",JS,
        v=[V("Zetsaw Flush S-145","Z-Saw","150 mm cut, 21 tpi, zero-set teeth, replaceable blade"),
           V("Detail Flush-Cutting Saw","Veritas","Western interpretation"),V("Double-Edge Flush-Cutting Saw","Veritas","Western interpretation")],dt="blade length · single or double edge")]},
 {"n":"Genno (Japanese hammer)","a":"genno · gennou · Japanese carpenter's hammer","d":"Japanese hammer with two striking faces, one flat and one slightly convex, on a hand-fitted wooden handle.","s":"https://www.axminstertools.com/hand-tools/hammers-mallets-punches/japanese-hammers",
  "t":["round, oval, square or octagonal face","head weight","handle wood"],
  "x":[X("Ryōguchi genno","Standard symmetrical double-faced genno, one face flat and one slightly domed; most common in eastern Japan.",CV,a="ryouguchi"),
       X("Kataguchi genno","Genno with one slightly domed face and the other end tapering to a small square face for setting nails.",CV),
       X("Daruma genno","Shorter, fatter variation of the ryōguchi genno at the same weight.",CV),
       X("Funate genno","Shipwright's genno especially suited to nailing; common in western Japan and Hokkaido.",CV,a="boat-hand genno · Iwakuni style"),
       X("Yamakichi genno","Stubbier, heavier hybrid of ryōguchi and funate styles, suited to chisel work.",CV,
        v=[V("Yamakichi original","Yamakichi","Kyushu blacksmith who developed the style"),V("Kosaburo pattern","Kosaburo","modified for Tokyo customers with Yamakichi's permission")])],
  "m":[["Hakkaku genno","Ice Bear"]]},
 {"n":"Nomi (Japanese chisel)","a":"nomi · Japanese chisel","d":"Japanese chisel with a hard steel edge laminated to softer iron, a hollow back and usually a hooped handle for striking.","s":JC,
  "t":["white paper steel","blue paper steel","tang or socket","hooped (struck) or push"],
  "x":[X("Oire-nomi","The most common Japanese chisel: thin bench chisel with a hooped handle, in the widest range of widths.",JC,a="bench chisel · 'rabbeting chisel'"),
       X("Atsu-nomi","Thick, strong striking chisel for large joints, resembling a butt chisel.",WC),
       X("Mukōmachi-nomi","Narrow mortise chisel with the neck as thick as the edge, struck to cut small mortises.",WC,a="mukomachi · mortise chisel"),
       X("Shinogi-nomi","Chisel with bevelled sides for cutting dovetails.",JC,a="dovetail chisel"),
       X("Tsuki-nomi","Long two-handed paring push chisel with a low-angle blade.",WC,a="paring chisel · usu-nomi"),
       X("Kote-nomi","Crank-necked paring push chisel with an offset blade for long housing joints.",WC)]},
 {"n":"Sumitsubo (ink line)","a":"sumitsubo · Japanese ink line","d":"Japanese carpenter's reel whose cord draws ink from a cotton-filled well and is snapped to mark long straight lines.","s":SU,
  "t":["traditional carved wooden","modern plastic","decorated ceremonial (topping-out)"]},
 {"n":"Sashigane (carpenter's square)","a":"sashigane · Japanese square","d":"Thin flexible steel L-square used by Japanese carpenters for layout, often with special scales.","s":SH,
  "t":["flat body","profiled body (thinner edges for ink)","metric","with metal stop","calculated scales (square-root, pi)"],
  "m":[["Sashigane square 30 cm with metal stop","Shinwa"]]},
 {"n":"Kiridashi","a":"kiridashi kogatana · Japanese marking knife","d":"Small Japanese single-bevel knife for marking, whittling and general woodworking cuts.","s":MA,
  "t":["left or right bevel","kurouchi finish","tsuchime finish","damascus (kitaeji)","white 2 or blue 1 steel"],
  "m":[["Kiridashi","Masuda"]]},
]
brands=[
 {"n":"Gyokucho","c":"Japan","f":"","seg":"Japanese saws","d":"Japanese maker of Razorsaw replaceable-blade pull saws.","lines":["Razorsaw"],"eras":[],"sig":["Ryoba","Dozuki"],"sc":["woodworking"],"rel":["Z-Saw"],"s":WH},
 {"n":"Z-Saw","c":"Japan","f":"","seg":"Japanese saws","d":"Zetsaw brand of Okada Hardware Mfg., pioneer of replaceable handsaw blades and impulse-hardened teeth.","lines":["Zetsaw"],"eras":[],"sig":["Dozuki","Kugihiki"],"sc":["woodworking"],"rel":["Gyokucho"],"s":ZF},
 {"n":"Seisuke Mizuno","c":"Japan","f":"","seg":"hand-forged kanna","d":"Niigata smith who hand-makes kanna such as the Chizoku hira-ganna.","lines":["Chizoku"],"eras":[],"sig":["Hira-ganna"],"sc":["woodworking"],"rel":[],"s":MZ},
 {"n":"Tachibana","c":"Japan","f":"","seg":"Japanese planes","d":"Maker of Japanese hand planes using traditional kanna-making methods.","lines":[],"eras":[],"sig":["Hikōki-ganna"],"sc":["woodworking"],"rel":[],"s":TB},
 {"n":"DICTUM","c":"Germany","f":"","seg":"woodworking tools retailer and brand","d":"Plattling-based tool house selling Japanese tools under its own name.","lines":[],"eras":[],"sig":[],"sc":["woodworking"],"rel":[],"s":DI},
 {"n":"Shinwa","c":"Japan","f":"","seg":"measuring tools","d":"Japanese maker of rules and squares including sashigane.","lines":[],"eras":[],"sig":[],"sc":["woodworking"],"rel":[],"s":SH},
 {"n":"Masuda","c":"Japan","f":"early Shōwa period","seg":"kiridashi smith","d":"Sanjo, Niigata kiridashi workshop, now run by second-generation smith Yoshihide Masuda.","lines":[],"eras":["Takeshi Masuda","Yoshihide Masuda"],"sig":[],"sc":["woodworking"],"rel":[],"s":MA},
 {"n":"Veritas","c":"Canada","f":"","seg":"woodworking hand tools","d":"Lee Valley's own tool brand, making Western versions of many hand tools.","lines":[],"eras":[],"sig":[],"sc":["woodworking"],"rel":[],"s":"knowledge"},
]
trads=[{"n":"Banshu Miki forged blades","g":"Metal & blades","r":"Miki City, Hyōgo, Japan","p":"Edo period onward (wide ripsaws from 1763)","d":"Miki smithing tradition of carpentry blades—saws, chisels, planes, knives and large construction tools.",
 "tech":"forge-welding carbon steel to iron with borax flux, forging, annealing in straw ash, water quench, two-stage tempering, polishing","mat":"iron and carbon steel",
 "forms":["Ryoba saw","Nomi (Japanese chisel)","Kanna (Japanese plane)","Kiridashi"],"ctr":["Miki City","Miki Hardware Museum"],"auth":"laminated hard-steel edge on softer iron; smith's stamp","s":KG}]
notes=("All six old kinds kept (Japanese plane renamed Kanna); four new kinds sourced. Western flush-cut saws (Veritas) kept as versions of Kugihiki noted 'Western interpretation'. "
 "Left out for lack of a retrieved source: kiwa-ganna, tataki-nomi as a named type (striking chisels covered by oire/atsu/mukomachi), Koyamaichi, Matsumura, Tasai makers, Echigo-Sanjo tradition entry, Banshu Miki official designation year, mawashibiki saw. "
 "Shokunin and Ice Bear models from old data kept; no register entries for them (facts unconfirmed). Wikidata was rate-limited (429).")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/C1/shelves/01_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
SEG={"Gyokucho":"Specialist","Z-Saw":"Specialist","Seisuke Mizuno":"Artisan & independent","Tachibana":"Artisan & independent","DICTUM":"Own-label & retailer","Shinwa":"Specialist","Masuda":"Artisan & independent","Veritas":"Premium"}
for b in brands: b["kf"]=b["seg"]; b["seg"]=SEG[b["n"]]
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
