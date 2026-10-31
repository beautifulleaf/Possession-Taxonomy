import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'I2.json'))
def K(name):
    for dep in d['depts']:
        for sh in dep['s']:
            for k in sh['k']:
                if k['n']==name: return k
A='https://aiwiki.ai/wiki/text-to-image_models/raw'
def V(n,mk,y,dd=''): return {"n":n,"mk":mk,"y":y,"d":dd}
def E(n,dsc,mk,y,s,g=None,v=None):
    e={"n":n,"a":"","d":dsc,"mk":mk,"y":y,"s":s}
    if g: e['g']=g
    if v: e['v']=v
    return e
k=K('Image-generation model')
sd=k['x'][0]; fl=k['x'][1]
have={v['n'] for v in sd['v']}
for n,y in [('Stable Cascade','2024'),('Stable Diffusion 3','2024'),('Stable Diffusion 3.5','2024')]:
    if n not in have: sd['v'].append(V(n,'Stability AI',y,'Open weights, per the aiwiki.ai overview'))
for n,y in [('FLUX.1 Kontext','2025'),('FLUX.2','2025')]:
    if not any(v['n']==n for v in fl['v']): fl['v'].append(V(n,'Black Forest Labs',y,'Open variants exist alongside closed Pro tiers'))
names={e['n'] for e in k['x']}
for e in [E('Hunyuan-DiT','Open text-to-image model from Tencent, released 2024.','Tencent','2024',A,'Tencent'),
 E('Janus-Pro','Open multimodal model from DeepSeek that also generates images, released 2025.','DeepSeek','2025',A,'DeepSeek'),
 E('HiDream-I1','Open text-to-image model from HiDream AI, released 2025.','HiDream AI','2025',A,'HiDream AI'),
 E('Qwen-Image','Open text-to-image model from Alibaba under the Apache 2.0 licence, released 2025.','Alibaba','2025',A,'Alibaba'),
 E('PixArt-Alpha','Open text-to-image model released 2023; the overview does not name its lab.','','2023',A,'Lab not stated')]:
    if e['n'] not in names: k['x'].append(e)
k['sel']="Open-weight image families in the aiwiki.ai overview of text-to-image models (https://aiwiki.ai/wiki/text-to-image_models/raw), grouped by lab. Complete: 7 of 7 open-weight families in that overview; closed services (DALL-E, Imagen, Midjourney, Ideogram, Recraft, Seedream) are not owned files, and Kolors, Sana and Lumina-mGPT were left out because the page states no licence."
k=K('Speech and audio model')
k['sel']="No complete list exists; follows the one fetched page in the entry. Searched: open speech model lists; no page naming open speech models with licences was found."
k=K('Blockchain name')
P2='https://paragraph.com/@droomdroom/best-10-decentralized-domain-name-services'
have={e['n'] for e in k['x']}
for n,dd in [('Unstoppable Domains','Naming service with no renewal fees and tools for decentralised websites.'),
 ('Stacks naming','Links names directly to Bitcoin addresses and supports decentralised websites.'),
 ('Emercoin EmerDNS','Domain registration on the Emercoin blockchain focused on reliability and security.'),
 ('Arweave Name System','Connects readable names to permanent data on the Arweave network.'),
 ('RIF Name Service','Naming service on the RSK network with cross-network interoperability.'),
 ('Handshake','Auctions top-level domains to keep ownership decentralised.'),
 ('PeerName','Interface for managing domains across several blockchains.'),
 ('Diode','Decentralised identity naming service.'),
 ('Proton Naming Service','Naming within the Proton ecosystem with an emphasis on privacy.')]:
    if n not in have: k['x'].append({"n":n,"a":"","d":dd,"mk":"","y":"","s":P2})
k['sel']="Naming services in the Paragraph overview of ten decentralised domain-name services (https://paragraph.com/@droomdroom/best-10-decentralized-domain-name-services). Complete: 10 of 10 services in that overview; no whole-space list exists beyond it."
json.dump(d,open(P+'I2.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'I2.json.tmp',P+'I2.json')
