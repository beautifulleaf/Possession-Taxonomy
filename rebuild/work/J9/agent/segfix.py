SEG={"Fentimans":"Premium","Vefa":"Heritage manufactory","GT's Living Foods":"Specialist","Remedy Drinks":"Specialist","Deka":"Mainstream",
"Royal Unibrew":"Mainstream","Compañía Cervecera de Puerto Rico":"Mainstream","Bundaberg Brewed Drinks":"Premium","Pago":"Premium","Rauch":"Mainstream",
"Rubicon":"Specialist","Vita Coco":"Specialist","Nuun":"Specialist","Liquid I.V.":"Specialist","CytoSport":"Specialist","Taisho Pharmaceutical":"Heritage manufactory",
"Otsuka Pharmaceutical":"Mainstream","Living Essentials":"Specialist","Brauerei Loscher":"Heritage manufactory","Celsius Holdings":"Mainstream","SunnyD":"Value","Capri-Sun":"Mainstream"}
def fix(B):
    for b in B:
        if b.get("seg") and b["seg"] not in ("Professional & flagship","Premium","Mainstream","Value","Heritage manufactory","Artisan & independent","Specialist","Own-label & retailer","Institution & issuer"):
            b["kf"]=b["seg"].lower(); b["seg"]=SEG.get(b["n"],"Mainstream")
    return B
