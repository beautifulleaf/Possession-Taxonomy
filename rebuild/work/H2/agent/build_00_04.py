import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
 {"n":"Nicotine replacement","a":"nicotine replacement product · NRT · stop-smoking aid",
  "d":"Product that supplies a measured dose of nicotine without tobacco smoke, used to help stop smoking.",
  "t":["patch (transdermal)","chewing gum","lozenge or pastille","mouth spray","inhalator (cartridge)","nasal spray","sublingual tablet"],
  "s":W+"Nicotine_replacement_therapy",
  "m":[["Nicorette gum","Nicorette"],["Nicorette patch","Nicorette"],["Nicorette QuickMist mouth spray","Nicorette"],["Nicorette Inhalator","Nicorette"],["Nicorette Microtab sublingual tablet","Nicorette"],["NicoDerm patch","NicoDerm"],["Nicotinell","Nicotinell"],["Commit lozenge","Commit"],["Nicotex","Nicotex"]]},
 {"n":"Homeopathic single remedy","a":"homeopathic remedy · mono-preparation · single remedy",
  "d":"Registered homeopathic preparation of one starting substance, sold as pills or liquid at a stated dilution; no efficacy claims made here.",
  "t":["lactose pills or pillules","liquid dilution","centesimal potency (C)","decimal potency (D or X)","quintamillesimal potency (Q / LM)"],
  "s":"https://www.naturheilapotheke-badems.de/Einzelmittel-1g",
  "m":[["Boiron mono-preparations","Boiron"]]},
 {"n":"Traditional medicine preparation","a":"traditional remedy · herbal medicine · patent medicine · Kampo extract · Ayurvedic medicine · Unani medicine",
  "d":"Ready-made preparation from a traditional healing system such as Chinese, Kampo, Ayurvedic, Unani or Western herbal medicine; no efficacy claims made here.",
  "t":["TCM patent medicine (teapills, honey pills, powders, granules, plasters, liniments)","Kampo extract granules","Ayurvedic preparation (herbal tablets, bhasma, medicated oils)","Unani preparation","Western herbal medicine with UK THR registration"],
  "s":W+"Chinese_patent_medicine",
  "m":[["Yunnan Baiyao",""],["Wuji Baifeng Wan",""],["Ganmaoling granules",""],["Kakkon-tō extract granules","Tsumura"],["Hajmola digestive tablets","Dabur"],["Pudin Hara","Dabur"],["Safi","Hamdard India"],["Cinkara","Hamdard India"]],
  "r":[["Tong Ren Tang TCM range","Tong Ren Tang"],["Plum Flower patent medicines","Plum Flower"],["Lanzhou Foci (Min Shan) pills","Lanzhou Foci"],["Kracie Kampo range","Kracie"]]},
]
brands=[
 {"n":"Nicorette","c":"Sweden","f":"1978","seg":"Nicotine replacement","d":"First nicotine replacement product, developed by AB Leo; now owned by Kenvue outside the US and Haleon in the US.",
  "lines":["gum","lozenge","patch","QuickMist mouth spray","Inhalator","Microtab","nasal spray"],"eras":["AB Leo, 1978 launch"],"sig":[],"sc":[],"rel":["Nicotinell","NicoDerm"],"s":W+"Nicorette"},
 {"n":"Boiron","c":"France","f":"1932","seg":"Homeopathic preparations","d":"Homeopathic manufacturer founded by Jean and Henri Boiron, based in Messimy; described as the largest in the world.",
  "lines":["mono-preparations","Oscillococcinum","Children's Coldcalm"],"eras":["Acquired Dolisos Laboratories, 2005"],"sig":[],"sc":[],"rel":[],"s":W+"Boiron"},
 {"n":"Tong Ren Tang","c":"China","f":"1669","seg":"Traditional Chinese medicine","d":"Beijing TCM maker and pharmacy chain founded by Yue Xianyang; supplier to the Qing court 1723–1911 and a China Time-honored Brand.",
  "lines":["patent medicines","retail drugstores"],"eras":["Imperial court supplier, 1723–1911"],"sig":[],"sc":[],"rel":[],"s":W+"Tong_Ren_Tang"},
 {"n":"Dabur","c":"India","f":"1884","seg":"Ayurvedic preparations","d":"Indian maker founded in Kolkata by Ayurvedic practitioner S. K. Burman, now based in Ghaziabad.",
  "lines":["Hajmola","Pudin Hara"],"eras":[],"sig":[],"sc":[],"rel":["Hamdard India"],"s":W+"Dabur"},
 {"n":"Hamdard India","c":"India","f":"1906","seg":"Unani preparations","d":"Unani maker founded in Old Delhi by Hakeem Hafiz Abdul Majeed and Ansarullah Tabani; also makes Rooh Afza.",
  "lines":["Safi","Roghan Badam Shirin","Sualin","Joshina","Cinkara"],"eras":[],"sig":[],"sc":[],"rel":["Dabur"],"s":W+"Hamdard_India"},
]
G="Healing traditions"
trads=[
 {"n":"Traditional Chinese medicine","g":G,"r":"China and the Sinosphere","p":"Han dynasty classics (1st c. BCE onward); modern system standardised in the PRC from the 1950s",
  "d":"Chinese healing tradition whose ready-made products are sold as patent medicines; listed here for forms and registration only.",
  "tech":"Herbal formulas made into pills, powders, pastes, extract granules and external plasters","mat":"Plant, animal, fungal and mineral materials",
  "forms":["teapills","honey pills","powders (san)","pastes (gao)","extract granules","plasters and liniments"],
  "ctr":["Tong Ren Tang, Beijing (1669)","Lanzhou Foci","Plum Flower","Sun-Ten, Taiwan"],
  "auth":"Mainland products follow Chinese Pharmacopoeia Vol. 1 monographs; Hong Kong proprietary Chinese medicines carry a registration number HKC-XXXXX; Tong Ren Tang products are often counterfeited.",
  "s":W+"Traditional_Chinese_medicine"},
 {"n":"Ayurveda","g":G,"r":"Indian subcontinent, Nepal, Sri Lanka","p":"Classical texts from the first centuries CE; mineral preparations (rasashastra) after the 11th century",
  "d":"South Asian healing tradition whose preparations are mostly plant-based; listed here for forms and registration only.",
  "tech":"Herbal compounding; rasashastra adds metals and minerals after purification (shodhana)","mat":"Mostly plants; also metals, minerals, oils and fats",
  "forms":["herbal compounds and tablets","bhasma (ash preparations)","medicated oils","madya (fermented preparations)"],
  "ctr":["Ministry of Ayush (2014)","Central Council for Research in Ayurvedic Sciences","Kerala","Rishikesh","Dabur, Kolkata (1884)"],
  "auth":"Indian products must state metallic content; voluntary Ayush Standard Mark (Schedule T GMP) and Ayush Premium Mark (WHO GMP) run by the Quality Council of India since 2009.",
  "s":W+"Ayurveda"},
 {"n":"Kampo","g":G,"r":"Japan","p":"Chinese medicine arrived in the 6th century; extract granules from the 1920s; NHI reimbursement from 1967",
  "d":"Japanese adaptation of Chinese herbal medicine using fixed formulas in standard proportions; listed here for forms and registration only.",
  "tech":"Fixed formulas made into dried decoction extract granules","mat":"Crude herbal drugs listed in the Japanese Pharmacopoeia",
  "forms":["extract granules","tablets","crude-drug decoctions"],
  "ctr":["Tsumura (makes 128 of 148 reimbursed formulas)","Kracie","Japan Society for Oriental Medicine","Keio University Center for Kampo Medicine"],
  "auth":"148 formula extracts approved by Japan's Ministry of Health, Labour and Welfare, each with the same ingredients whichever maker.",
  "s":W+"Kampo"},
 {"n":"Unani","g":G,"r":"South and Central Asia, chiefly India and Pakistan","p":"Greco-Arabic, from Avicenna's Canon of Medicine; in India from the 12th century",
  "d":"Greco-Arabic humoral healing tradition practised in South Asia; listed here for forms and registration only.",
  "tech":"Herbal medicines compounded by hakims, with regimental therapies","mat":"Herbs and minerals",
  "forms":["herbal compound preparations","syrups and tonics","medicated oils"],
  "ctr":["Hamdard, Delhi (1906)","Jamia Hamdard","Tibbia College, Delhi","Central Council for Research in Unani Medicine","National Council for Tibb, Pakistan"],
  "auth":"Regulated in India under the Ministry of Ayush and in Pakistan by the National Council for Tibb; Indian Unani products can carry the voluntary Ayush Mark.",
  "s":W+"Unani_medicine"},
 {"n":"Homeopathy","g":G,"r":"Germany, now worldwide","p":"From 1796 (Samuel Hahnemann)",
  "d":"System of highly diluted preparations devised by Samuel Hahnemann; listed here for forms and registration only.",
  "tech":"Serial dilution on C, D/X or Q scales; drops placed on lactose pills","mat":"Lactose pills, water-alcohol dilutions",
  "forms":["pills and pillules","liquid dilutions","single remedies","combination preparations"],
  "ctr":["Boiron, France","National Institute of Homoeopathy, India (1975)"],
  "auth":"UK Simplified Registration products carry no indications; UK National Rules products may name minor conditions and say 'UK Only'; the US FDA has approved no homeopathic product.",
  "s":"https://gov.uk/guidance/register-a-homeopathic-medicine-or-remedy"},
]
notes=("Kept both old kinds and added Traditional medicine preparation. Nicotine replacement now has 7 types (patch, gum, lozenge, mouth spray, inhalator, nasal spray, sublingual tablet) and 9 models; makers are named only where a page I retrieved names them. "
 "Homeopathic single remedy keeps its old source, with potency scales as types and Boiron as maker. The traditional preparation kind lists named products from the Chinese patent medicine, Kampo, Dabur and Hamdard pages; I gave no maker for Yunnan Baiyao, Wuji Baifeng Wan or Ganmaoling because the page names none. "
 "Five traditions use group 'Healing traditions' and make no efficacy claims. Left out: mainland China NMPA approval-number format and the THR certification-mark details as a tradition entry (the MHRA page was retrieved but not cited: THR products carry a nine-digit number starting THR); "
 "Ayurvedic forms churna/arishta/ghrita and Unani majoon/khamira (not confirmed on a retrieved page); a Tsumura brand entry (no company page retrieved).")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/H2/shelves/00_04.json'; tmp=p+'.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,p)
