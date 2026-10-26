import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Face moisturiser","a":"face cream · moisturising cream · face lotion · emulsion · 乳液","d":"Leave-on cream or lotion that softens and hydrates the skin of the face.",
 "t":["cream","lotion / emulsion (nyūeki)","gel-cream","night cream","tinted moisturiser (see Foundation)"],
 "s":"https://us.oliveyoung.com/categories/D01",
 "x":[
  X("Crème de la Mer","The Moisturizing Cream · La Mer cream","Luxury cream built on the fermented sea-kelp 'Miracle Broth' that Dr Max Huber developed after lab-accident burns.","La Mer","","https://www.cremedelamer.com/heritage",dt="jar sizes"),
  X("Clinique Dramatically Different Moisturizing Lotion","DDML · 'the yellow one'","Silky yellow lotion that is the moisturiser step of Clinique's 3-step routine.","Clinique","1968 (3-step routine launch)","https://www.clinique.co.uk/thewink/cult-classic/dramatically-different-moisturizing-lotion",
    [("Dramatically Different Moisturizing Lotion+","Clinique","","current barrier-strengthening formula")],"15–200 ml bottles and pump"),
  X("CeraVe Moisturizing Cream","CeraVe cream · CeraVe tub","Fragrance-free cream of ceramides, glycerin and petrolatum; the dermatologist-brand pick for dry and eczema-prone skin.","CeraVe","2005 onwards (brand launch)","https://en.wikipedia.org/wiki/CeraVe",dt="tub and pump sizes · face and body"),
  X("Weleda Skin Food","Skin Food Original Ultra-Rich Cream","Rich all-over cream with a rosemary, calendula, chamomile and pansy infusion, sold since 1926.","Weleda","1926","https://www.weleda.com/campaigns/100-years-skin-food",
    [("Skin Food Original Ultra-Rich Cream","Weleda","1926","the original tube"),("Skin Food Light Nourishing Cream","Weleda","","lighter texture"),("Skin Food Body Butter","Weleda","","body version"),("Skin Food Body Lotion","Weleda","","body lotion")],"tube sizes · face and body"),
  X("Embryolisse Lait-Crème Concentré","Embryolisse cream","Multi-use milky cream from a Paris hospital dermatologist, adopted by make-up artists as a primer-moisturiser.","Embryolisse","1950","https://us.embryolisse.com/blogs/beautiful-skincare-tips/for-more-than-70-years-embryolisse-has-strived-to-make-natural-beauty-easier-more-effective-enjoyable-and-accessible",dt="tube sizes"),
  X("Clé de Peau Beauté La Crème","The Cream","Ultra-luxury night cream with the brand's 'Skin-Empowering Illuminator' complex and over 60 ingredients.","Clé de Peau Beauté","brand founded 1982","https://www.cultbeauty.co.uk/p/cle-de-peau-beaute-la-creme-various-sizes/13316735",dt="30 ml and 50 ml jars"),
  X("Olay Regenerist Micro-Sculpting Cream","Regenerist cream","Mass-market anti-ageing cream with amino-peptides; Allure Readers' Choice drugstore moisturiser 2008.","Olay","by 2008 (Allure award)","https://well.ca/products/olay-regenerist-micro-sculpting_5455.html",dt="50 ml jar · fragrance-free and night versions"),
 ],
 "m":[["Atobarrier365 Cream","AESTURA"],["Ceramide Ato Concentrate Cream","ILLIYOON"],["Advanced Pro-Collagen+ Peptide Cream","Medik8"],["Pro-Collagen Peptide Plumping Moisturizer","Paula's Choice"],["Silky Fit Emulsion","Koh To Ka"],["Serum Veil Emulsion","ONE BY KOSE"]]},
{"n":"Eye cream","a":"eye balm · eye gel","d":"Light cream, gel or balm for the thin skin around the eyes.","t":["cream","gel","balm","roll-on"],
 "s":"https://cultbeauty.co.uk/c/skin-care/eyes/creams",
 "x":[X("Kiehl's Creamy Eye Treatment with Avocado","Kiehl's avocado eye cream","Rich fragrance-free eye cream of avocado oil, shea butter and beta-carotene.","Kiehl's","","https://www.mecca.com/en-au/kiehls/creamy-eye-treatment-with-avocado-14g-I-041308/",dt="14 g and 28 g jars")],
 "m":[["Vital Perfection Uplifting and Firming Advanced Eye Cream","Shiseido"],["'Spresso Energizing Eye Balms","TULA"]]},
{"n":"Body lotion & butter","a":"body lotion · body cream · body butter · all-purpose cream","d":"Leave-on lotion, cream or butter for moisturising the skin of the body.",
 "t":["lotion","cream","butter","all-purpose balm"],"s":"https://dermfnd.org/p/vaseline-intensive-care-essential-healing-lotion/",
 "x":[
  X("Nivea Creme","Nivea blue tin","All-purpose white cream sold since 1911 as the first stable water-in-oil emulsion; blue tin since 1925.","Nivea","1911","https://en.wikipedia.org/wiki/Nivea",
    [("Blue-tin relaunch","Nivea","1925","blue tin with white logo")],"tin and tube sizes"),
  X("Elizabeth Arden Eight Hour Cream","Eight Hour Cream Skin Protectant","Petrolatum balm with vitamin E and salicylic acid used for dry patches, lips and cuticles.","Elizabeth Arden","1930s","http://www.beaut.ie/beauty/080808-a-history-of-eight-hour-cream-5775",
    [("Eight Hour Cream Hand Cream","Elizabeth Arden","","later hand version"),("Eight Hour Cream Body Lotion","Elizabeth Arden","","later body version")],"tube sizes · scented and fragrance-free"),
  X("Vaseline Intensive Care lotion","Vaseline lotion","Drugstore body lotion line pairing glycerin with petrolatum, sold in pump bottles.","Vaseline","","https://dermfnd.org/p/vaseline-intensive-care-essential-healing-lotion/",
    [("Intensive Care Essential Healing Lotion","Vaseline","2010","oat extract, light scent")],"pump bottle sizes · variants by skin need"),
  X("Palmer's Cocoa Butter Formula","Palmer's cocoa butter","Cocoa-butter creams and lotions, also sold for stretch marks.","Palmer's","1970s","https://www.chemistdirect.co.uk/palmers-the-history-of-palmers",dt="jar, tube and bottle · cream, lotion, stick"),
 ]},
{"n":"Body oil","a":"dry oil · massage oil","d":"Oil applied to the skin to moisturise it, add sheen or for massage.",
 "t":["dry oil","shimmer oil","massage oil","scar & stretch-mark oil"],"s":"https://www.thebodyshop.com.au/collections/massage-body-oils",
 "x":[
  X("Nuxe Huile Prodigieuse","Prodigious oil","Multi-purpose plant-based dry oil for face, body and hair, sold in pharmacies.","Nuxe","1991","https://us.nuxe.com/pages/our-history",dt="100 ml bottle · roll-on"),
  X("Bio-Oil Skincare Oil","Bio-Oil","Light oil first sold for dry skin, now widely used on scars and stretch marks.","Bio-Oil","1987","https://refinery29.com/en-us/bio-oil-uses",dt="bottle sizes · natural version"),
 ],
 "m":[["Chance Eau Tendre Body Oil","Chanel"],["Polynesian Monoi Radiance Oil","The Body Shop"]]},
{"n":"Hand cream","a":"hand lotion","d":"Moisturiser for the hands, often also for nails and cuticles.","t":["cream","lotion","hand & nail cream","concentrated / barrier cream"],
 "s":"https://checkout.ozhairandbeauty.com/collections/hand-creams?page=2",
 "x":[
  X("Neutrogena Norwegian Formula Hand Cream","Norwegian Formula","Glycerin-rich hand cream line for dry, chapped hands.","Neutrogena","","https://www.neutrogena.co.uk/hand-and-body/hand-creams/norwegian-formula-hand-nail-cream",
    [("Norwegian Formula Hand & Nail Cream","Neutrogena","","adds panthenol for nails and cuticles")],"tube sizes · scented and fragrance-free"),
  X("L'Occitane Shea Butter Hand Cream","Shea hand cream","Hand cream with 20% shea butter sourced from women's cooperatives in Burkina Faso and Ghana.","L'Occitane en Provence","","https://cew.org/award/shea-butter-hand-cream-2024/",dt="30 ml and 150 ml tubes"),
 ]},
]
def B(n,c,f,seg,d,lines,eras,sig,sc,rel,s): return dict(n=n,c=c,f=f,seg=seg,d=d,lines=lines,eras=eras,sig=sig,sc=sc,rel=rel,s=s)
brands=[
 B("La Mer","","","Luxury skincare","Skincare house built on Dr Max Huber's fermented sea-kelp 'Miracle Broth'.",["The Moisturizing Cream"],["Dr Max Huber (founder)"],["Crème de la Mer"],["Luxury skincare"],["Clé de Peau Beauté"],"https://www.cremedelamer.com/heritage"),
 B("Clé de Peau Beauté","Japan","1982","Luxury skincare and make-up","Shiseido's luxury line, given a French name to draw on France's beauty associations.",["La Crème"],["Shiseido (owner)"],["Clé de Peau Beauté La Crème"],["Luxury skincare"],["Shiseido","La Mer"],W+"Cl%C3%A9_de_Peau_Beaut%C3%A9"),
 B("Shiseido","Japan","1872","Cosmetics group, prestige and mass","Tokyo cosmetics company founded as a pharmacy by Arinobu Fukuhara; entered cosmetics with Eudermine in 1897.",["Eudermine","Vital Perfection"],["Arinobu Fukuhara (founder, 1872)"],["Eudermine"],["Japanese skincare"],["Clé de Peau Beauté","NARS"],W+"Shiseido"),
 B("Nivea","Germany","1911","Mass skin and body care","Beiersdorf's skin-care brand, launched with Nivea Creme in 1911.",["Nivea Creme","Labello"],["Beiersdorf AG (owner)"],["Nivea Creme"],["Everyday body care"],["Eucerin"],W+"Nivea"),
 B("Kiehl's","United States","1851","Premium skincare","New York skincare brand that began as an East Village homeopathic pharmacy; owned by L'Oréal since 2000.",["Creme de Corps","Blue Astringent Herbal Lotion"],["L'Oréal (owner since 2000)"],["Kiehl's Creamy Eye Treatment with Avocado"],["Apothecary skincare"],["CeraVe"],W+"Kiehl%27s"),
 B("Weleda","Switzerland","1921","Natural skincare and anthroposophic medicine","Arlesheim company founded by Rudolf Steiner and Ita Wegman, making natural cosmetics and remedies.",["Skin Food","Baby and mother care"],["Rudolf Steiner and Ita Wegman (founders)"],["Weleda Skin Food"],["Natural skincare"],[],W+"Weleda"),
 B("Olay","United States","1952","Mass skincare","Procter & Gamble skincare brand that began in South Africa as Oil of Olay, a pink fluid by Graham Wulff.",["Oil of Olay","Regenerist"],["Graham Wulff (founder)","Procter & Gamble (owner)"],["Olay Regenerist Micro-Sculpting Cream"],["Drugstore skincare"],["Nivea","Neutrogena"],W+"Olay"),
 B("Elizabeth Arden","United States","1910","Prestige skincare and fragrance","Cosmetics company founded as the Red Door salon on Fifth Avenue; owned by Revlon since 2016.",["Eight Hour Cream"],["Elizabeth Arden (founder)","Revlon (owner since 2016)"],["Elizabeth Arden Eight Hour Cream"],["Classic beauty counter"],[],W+"Elizabeth_Arden,_Inc."),
 B("Clinique","United States","1968","Prestige dermatologist-led skincare","Estée Lauder brand that launched at Saks Fifth Avenue in 1968 with a 3-step routine.",["3-step routine","Moisture Surge"],["Estée Lauder Companies (owner)"],["Clinique Dramatically Different Moisturizing Lotion"],["Beauty counter"],["La Mer"],W+"Clinique"),
 B("Embryolisse","France","1950","Pharmacy skincare","Family-owned French brand whose milky cream began with a Paris hospital dermatologist.",["Lait-Crème Concentré"],[],["Embryolisse Lait-Crème Concentré"],["French pharmacy skincare","Make-up artist kits"],["Nuxe"],"https://us.embryolisse.com/blogs/beautiful-skincare-tips/for-more-than-70-years-embryolisse-has-strived-to-make-natural-beauty-easier-more-effective-enjoyable-and-accessible"),
 B("Neutrogena","United States","1930","Mass skincare","Skincare brand founded as Natone by Emanuel Stolaroff; part of Johnson & Johnson from 1994, now Kenvue.",["Norwegian Formula","Hydro Boost"],["Emanuel Stolaroff (founder)","Kenvue (owner)"],["Neutrogena Norwegian Formula Hand Cream"],["Drugstore skincare"],["Olay"],W+"Neutrogena"),
 B("L'Occitane en Provence","France","1976","Premium body care and fragrance","Manosque company founded by Olivier Baussan; sources shea butter from Burkina Faso cooperatives since the 1980s.",["Shea butter range"],["Olivier Baussan (founder)"],["L'Occitane Shea Butter Hand Cream"],["Gift and body care"],[],W+"L%27Occitane_en_Provence"),
 B("Vaseline","United States","1872","Mass body care","Petroleum-jelly brand of Robert Chesebrough, owned by Unilever since 1987.",["Petroleum jelly","Intensive Care"],["Robert Chesebrough (inventor)","Unilever (owner since 1987)"],["Vaseline Intensive Care lotion"],["Drugstore body care"],["Nivea"],W+"Vaseline"),
 B("Palmer's","United States","1840","Mass body care","Family-owned brand of E.T. Browne Drug Co., known for cocoa-butter skincare since the 1970s.",["Cocoa Butter Formula"],["Arnold Neis (owner from 1971)"],["Palmer's Cocoa Butter Formula"],["Stretch-mark care"],["Bio-Oil"],"https://uk.palmers.com/pages/company"),
 B("Nuxe","France","early 1990s","Pharmacy skincare","Paris brand built by Aliza Jabès on a natural-cosmetics lab; sells in pharmacies.",["Huile Prodigieuse","Nuxe Sun"],["Aliza Jabès (founder)"],["Nuxe Huile Prodigieuse"],["French pharmacy skincare"],["Embryolisse"],"https://us.nuxe.com/pages/our-history"),
 B("Bio-Oil","South Africa","1987","Mass skincare","Skincare oil developed by chemist Dieter Beier at Union Swiss in South Africa.",["Bio-Oil Skincare Oil"],["Dieter Beier (creator)","Letschert brothers (from 2000)"],["Bio-Oil Skincare Oil"],["Scar and stretch-mark care"],["Palmer's"],"https://refinery29.com/en-us/bio-oil-uses"),
]
notes=("Merged Moisturising cream + Lotion into Face moisturiser (lotion/emulsion as a type). Dropped as SKU noise: Anua PDRN cream, Centellian24 Madeca, S.NATURE Aqua Squalane (face); CYKLAR oil, three of four The Body Shop oils and the repeated 'Spa of the World' range (body oil); evolvetogether Taormina (hand cream). Olay Regenerist moved from m to an archetype. "
 "CeraVe brand entry not repeated (already in the register from shelf 00_00). Left out for lack of a retrievable source: launch year for Crème de la Mer, Clé de Peau La Crème's own launch year, Kiehl's eye cream year, Clinique DDML exact launch year; Neutrogena Norwegian Formula history. No traditions needed for this shelf. No independent test-winner pages retrieved, so no extra tier models added.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/H1/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
