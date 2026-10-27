import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from h import v,x,B,W
SS='https://en.wikipedia.org/wiki/Slingshot'; SL='https://en.wikipedia.org/wiki/Sling_(weapon)'; BG='https://en.wikipedia.org/wiki/Blowgun'
FK='https://en.wikipedia.org/wiki/Fukiya'; AN='https://artsandculture.google.com/asset/sling/VwEOvDARQkPfdQ'; WR='https://simple-shot.com/blogs/community/wrist-rocket'
kinds=[
{"n":"Slingshot","a":"catapult","d":"Hand-held fork with elastic bands that launches a small projectile. A toy one is in Toys & Games.",
 "t":["flat bands","latex tubing","wrist-braced","natural wood fork","metal or polymer frame"],"s":"https://www.walmart.com/browse/sports-outdoors/slingshots/4125_546956_4155_6917814",
 "x":[x("Zip-Zip","","by 1918","Early commercial cast-iron slingshot frame.",SS,dt="frame finish · bands"),
  x("Wham-O slingshot","Wham-O","1948","Ash-wood slingshot with flat rubber bands, strong enough for hunting and sold with an arrow rest.",SS,dt="bands · arrow rest"),
  x("Wrist-braced slingshot","","1950s","Slingshot whose brace rests on the forearm to take high draw weights, powered by latex tubing; first made by Howard Ellenburg.",WR,dt="tubing · brace · frame",a="Wrist Rocket")],
 "m":[["Barnett King Rat Black Widow","Barnett"],["Daisy B52","Daisy"],["Daisy F16","Daisy"],["Marksman Laserhawk","Marksman"]]},
{"n":"Sling","a":"shepherd's sling","d":"Pouch between two braided cords, whirled to hurl a stone or sling-bullet when one cord is let go.",
 "t":["hand sling","staff sling","wool","flax or hemp","polyester"],"s":SL,
 "x":[x("Balearic sling","","4th century BC on","Sling of the Balearic Islands, once made of rush or plant fibre and sinew in three lengths; still used in island competitions.",SL,dt="length · fibre"),
  x("Andean sling","","Formative period to present","Braided camelid-fibre sling of the Andes with a wide central cradle and a finger loop, long used by herders.",AN,
   [v("Inca-period sling","","1400–1540","llama or camelid wool; some up to 2.2 m")],"length · fibre · pattern"),
  x("Staff sling","","Antiquity–Middle Ages","Short sling on the end of a wooden staff up to 2 m long, throwing heavier stones further.",SL,dt="staff length",a="stave sling · fustibalus")]},
{"n":"Blowgun","a":"blowpipe","d":"Tube through which a dart is propelled by the breath. A toy one is in Toys & Games.","t":[".40 calibre",".50 calibre",".625 calibre","cane or bamboo","metal or plastic tube"],
 "s":"https://www.bladehq.com/item--Cold-Steel-48-Magnum-Blowgun-Black--69652",
 "x":[x("Fukiya","","","Japanese blowgun about 1.2 m long with no mouthpiece, shot at 10 m targets as a sport.",FK,dt="tube length · paper-cone darts"),
  x("Sumpit","","","Southeast Asian blowpipe of 1.2–1.8 m, often fitted with a metal spearhead.",BG,dt="length · spearhead",a="sumpitan"),
  x("Cherokee blowgun","","","River-cane blowgun 2–3 m long, shooting darts fletched with thistle down or rabbit fur.",BG,dt="length · dart fletching")],
 "m":[["Cold Steel .357 Magnum Blowgun","Cold Steel"]]},
]
brands=[B("Wham-O","United States","1948","Mainstream","toys · slingshots","US toy company that made an ash-wood hunting slingshot.",SS,sig=["Wham-O slingshot"])]
W('06_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Both old kinds kept; Sling added. Old slingshot models kept in m. Saunders/Trumark not named as wrist-brace originator: the slingshot-shooting.de Trumark page timed out (WebFetch and Firecrawl), so the archetype cites simple-shot.com, which credits Howard Ellenburg."})
