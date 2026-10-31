import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Solid body doll","a":"love doll","d":"Life-size body replica of solid silicone or TPE on an internal frame, made for sexual use.","t":["Platinum-cure silicone","TPE","Foam core","Articulated skeleton"],"m":[["RealDoll","Abyss Creations"],["Alice 159 A","FunWest Doll"],["Akiyama S40","Irontech Doll"],["Alara R11","Real Lady"]],"r":[["Orient Industry high-end silicone dolls","Orient Industry"]],"s":"https://artisan-dolls-online.lovable.app/dolls/bianca-163cm"},
{"n":"Stationary masturbator","a":"torso masturbator · breast-type masturbator","d":"Large, heavy masturbator moulded as a torso, lower body or breast form without head or limbs, made to rest on a surface.","t":["Torso","Breast-form"],"m":[["Puniana DX","Outvision"]],"s":"https://www.e-nls.com/disp_ca_hole.php"},
{"n":"Inflatable doll","a":"","d":"Inflatable life-size body replica made for sexual use, usually with three openings.","t":["Vinyl","Latex"],"s":"https://www.orion.de/katalog/sextoys/puppen"},
]
brands=[
 {"n":"Abyss Creations","c":"United States","f":"1996","seg":"Premium","kf":"RealDoll","d":"Las Vegas maker of RealDoll, with a posable skeleton under silicone; now a Realbotix subsidiary.","s":U+"RealDoll"},
 {"n":"Orient Industry","c":"Japan","f":"","seg":"Premium","kf":"high-end silicone","d":"Japanese maker regarded as a leading high-end silicone doll builder.","s":U+"Sex_doll"},
]
put('H3','04_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Stationary torso and breast-form merged as types. Bianca (Ultimate Fantasy Dolls) dropped; RealDoll (Abyss Creations) added from its Wikipedia page, with Orient Industry as a range. WM Doll and Sino Doll are not on a retrieved page, so omitted. Material facts (tin versus platinum silicone, TPE common since about 2012, inflatables in vinyl or latex) come from the Sex doll page. Neutral definitions."})
