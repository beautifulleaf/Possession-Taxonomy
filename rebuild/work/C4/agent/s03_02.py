import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
DM=W+'DMC_(company)'; ET=W+'Embroidery_thread'; SA='https://www.suespargo.com/blog/techniques-4/sashiko-22'; QS='https://thequiltshow.com/quiltipedia/what-is-sashiko'
EV='https://www.willowfabrics.com/blog/post/what-is-evenweave-fabric-jobelan-lugana-and-murano-compared'; JB=W+'Jacobean_embroidery'; WW=W+'Whitework_embroidery'; PU='https://pieceworkmagazine.com/long-thread-podcast-amy-oxford-oxford-punch-needle/'; KA=W+'Kantha'
kinds=[
{"n":"Embroidery floss","a":"stranded cotton · mouliné","d":"Divisible stranded thread made for hand embroidery and cross stitch.","s":"https://www.dickblick.com/categories/crafts/textile-arts/",
 "t":["6-strand cotton","silk floss","variegated","metallic","matte cotton","glow-in-the-dark"],
 "x":[X("Mouliné Spécial","DMC",DM,"DMC's six-strand cotton floss, the standard for cross-stitch; DMC was founded in Mulhouse in 1746 and bought Anchor in 2023.","",dt="6 strands · colour numbers"),
      X("Anchor floss","Anchor",DM,"Thread brand acquired by DMC from the MEZ Crafts Group in 2023.","",dt="")],
 "m":[["Cotton Embroidery Floss","DMC"]]},
{"n":"Pearl cotton and tapestry wool","a":"perle cotton · crewel wool · Persian yarn","d":"Twisted thread or wool not divided into strands, made for hand embroidery and needlepoint.","s":"https://www.dmc.com/US/en/products/cebelia-yarn",
 "t":["perle cotton No. 3 to 16","crewel wool (2-ply)","tapestry yarn (4-ply)","Persian yarn (3-strand)","matte cotton"],
 "x":[X("Perle cotton","",ET,"Glossy 2-ply cotton thread in sizes from No. 3 (heaviest) to No. 16 (finest).","",dt="No. 3-16"),
      X("Crewel wool","",ET,"Fine 2-ply wool used for delicate surface embroidery and Jacobean crewel work.","",dt="2-ply wool"),
      X("Tapestry yarn","",ET,"Tightly twisted 4-ply yarn whose strands cannot be separated, used for needlepoint.","",dt="4-ply")]},
{"n":"Needlecraft cloth","a":"Aida · evenweave · needlepoint canvas","d":"Counted-thread cloth or canvas made for hand stitching.","s":"https://www.hobbycraft.co.uk/sewing/cross-stitch/cross-stitch-fabric",
 "t":["Aida (11, 14, 16, 18 count)","evenweave (25, 28, 32 count)","linen","needlepoint canvas","waste canvas"],
 "x":[X("Lugana","Zweigart",EV,"Zweigart evenweave of about 52% cotton and 48% modal, usually 25-count; stitched over two threads.","",v=[("Murano","32-count version of the Lugana family")],dt="25-count · cotton-modal"),
      X("Jobelan","",EV,"Cotton-modal evenweave of about 51% cotton and 49% modal, most often 28-count.","",dt="28-count")],
 "m":[["Aida cloth",""]]},
{"n":"Sashiko thread and needles","a":"sashiko cotton · sashiko cloth","d":"Thick cotton thread, long needles and printed cloth for Japanese running-stitch sashiko.","s":SA,
 "t":["thin thread","thick thread","kogin thread","pre-printed indigo cloth","long needles","big-eye needles"],
 "x":[X("Sashiko thread","Daruma",SA,"Japanese maker founded in 1901 with three 100% cotton weights: Thin (about size 12 perle), Thick (size 8) and Kogin (size 5).","1901",v=[("Thin","about size 12 perle"),("Thick","about size 8 perle"),("Kogin","about size 5 perle")],dt="100% cotton · made in Japan"),
      X("Sashiko thread","Olympus",SA,"Japanese 100% cotton sashiko thread with smooth stitch and matte finish; solids and variegated colours.","",dt="matte"),
      X("Sashiko needles","Tulip",SA,"Assorted short and long sets, Big Eye Thin and Thick, and Kogin needles with thin rounded points.","",dt="long, thick, oval eye")]},
{"n":"Tapestry and embroidery needle","a":"","d":"Large-eyed hand needle made for stitching with yarn or floss.","s":"https://www.dickblick.com/categories/crafts/textile-arts/","t":["tapestry (blunt)","embroidery (sharp)","chenille","crewel"],"m":[]},
{"n":"Embroidery hoop","a":"","d":"Pair of rings that holds cloth taut for hand stitching.","s":"https://www.hobbycraft.co.uk/sewing/embroidery/hoops-frames","t":["wooden","plastic","spring-tension","scroll frame","Q-snap"],"m":[]},
{"n":"Punch needle","a":"","d":"Hollow needle tool made for punching yarn or floss loops through cloth.","s":"https://www.hobbycraft.co.uk/knitting-crochet",
 "t":["rug-hooking punch needle","embroidery punch needle","adjustable loop height"],
 "x":[X("Oxford Punch Needle","Oxford Company",PU,"Wood-handled punch needle with a contoured grip developed by Amy Oxford; her Oxford Company dates from 1995.","1995",dt="contoured wood handle")],"m":[]},
{"n":"Needlecraft and yarn kit","a":"cross-stitch kit · embroidery kit · knitting kit · crochet kit · needle-felting kit","d":"Kit with cloth or yarn, floss, needle or hook and a pattern for one project, sold as one set.","s":"https://www.dickblick.com/categories/crafts/jewelry-making/",
 "t":["cross-stitch kit","embroidery kit","needlepoint kit","knitting kit","crochet and amigurumi kit","needle-felting kit"],
 "m":[["The Masters Collection Cross Stitch Kits","DMC"]]},
]
brands=[
B("DMC","France","1746","Heritage manufactory","embroidery thread","Mulhouse firm founded by Jean-Henri Dollfus; bought Anchor in 2023.",s=DM,sig=["Mouliné Spécial","Anchor floss"],lines=["Mouliné","Perle","Cebelia"]),
B("Anchor","","","Mainstream","embroidery floss","Thread brand acquired by DMC from MEZ Crafts Group in 2023.",s=DM,rel=["DMC"]),
B("Zweigart","Germany","","Specialist","counted-thread cloth","Maker of Lugana, Murano and Aida cloths.",s=EV,sig=["Lugana"]),
B("Daruma","Japan","1901","Heritage manufactory","sashiko thread","Japanese maker of 100% cotton sashiko thread.",s=SA,sig=["Sashiko thread"]),
B("Olympus","Japan","","Heritage manufactory","sashiko thread","Japanese maker of cotton sashiko thread.",s=SA),
B("Tulip","Japan","","Premium","needles","Japanese needle company with sashiko and Kogin needles.",s=SA),
B("Oxford Company","United States","1995","Specialist","punch needle","Company founded by Amy Oxford to sell punch needle supplies and teaching.",s=PU,sig=["Oxford Punch Needle"]),
]
trad=[
{"n":"Sashiko and boro","g":"Textiles & rugs","r":"Japan","p":"Edo period (1603-1867) onward","d":"Sashiko is Japanese running-stitch reinforcement that became decoration; boro is the patched cloth it mended.","tech":"Repeating or interlocking running stitches in thick cotton thread.","mat":"White cotton thread on indigo cloth; linen","forms":["Sashiko","Boro","Kogin"],"ctr":["Northern Japan"],"auth":"","s":QS},
{"n":"Crewelwork (Jacobean embroidery)","g":"Textiles & rugs","r":"England","p":"early 17th century (reign of James I)","d":"Wool embroidery on linen with tree-of-life and fanciful plant and animal motifs, used for hangings and bed curtains.","tech":"Two-ply wool worked in a variety of stitches on linen or linen-cotton twill.","mat":"Crewel wool; linen","forms":["Bed curtains","Hangings","Jackets"],"ctr":[],"auth":"","s":JB},
{"n":"Hardanger embroidery","g":"Textiles & rugs","r":"Hardanger, Norway","p":"","d":"Norwegian counted whitework with drawn-thread openings in geometric designs.","tech":"Counted drawn-thread whitework worked on white linen.","mat":"White linen, matching thread","forms":["Hardangersøm"],"ctr":["Hardanger"],"auth":"","s":WW},
{"n":"Kantha","g":"Textiles & rugs","r":"Bengal (Bangladesh and eastern India)","p":"","d":"Running-stitch embroidery in which layers of old cloth are quilted together.","tech":"Simple running stitches, often covering the whole cloth for a wavy texture.","mat":"Old saris and dhotis; cotton and silk thread","forms":["Nakshi kantha","Lepkantha","Sujni kantha"],"ctr":["West Bengal","Tripura","Odisha","Santiniketan"],"auth":"","s":KA},
]
write('03_02',kinds,brands,trad,"Oliver Twist punch needle not found (left out; Oxford Punch Needle used instead). Appleton crewel wool, Zweigart Aida specifics left out (no retrieved page). Needlecraft kits merged (both old kinds). Sashiko page for boro folded into one tradition.")
