import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s if s.startswith('http') else U+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Profile-picture (PFP) NFT","a":"PFP collection · 1/1 NFT · semi-fungible NFT","d":"One collectible token from a numbered avatar collection, either a single unique piece or an edition issued in several identical copies.","t":["Unique NFT","Multi-edition NFT"],"s":"","x":[
 A("CryptoPunks","Larva Labs","2017","CryptoPunks","The originator of PFP collections: 10,000 algorithmic characters on Ethereum, first free to claim.",[
  ("Original 10,000","Larva Labs","2017","Launched June 2017; 88 Zombies, 24 Apes, 9 Aliens"),
  ("Yuga Labs IP","Yuga Labs","2022","IP bought March 2022, sold to NODE Foundation May 2025")]),
 A("Bored Ape Yacht Club","Yuga Labs","2021","Bored_Ape","10,000 ape NFTs from 172 assets, sold at 0.08 ether in April 2021, with club access and IP rights for holders.",[
  ("Bored Ape Kennel Club","Yuga Labs","",""),("Mutant Ape Yacht Club","Yuga Labs","","Secondary collection via Mutant Serum")]),
 A("Pudgy Penguins","Igloo","2021","Pudgy_Penguins","8,888 penguins launched 22 July 2021, bought with its IP in April 2022 for about $2.5 million.",[("Lil Pudgys","Igloo","","Related collection")]),
 A("Moonbirds","Proof Collective","2022","Kevin_Rose","10,000 pixelated birds from Proof Collective, with $281 million in sales by April 2022.")],
 "m":[["Azuki",""],["Doodles",""],["Meebits",""],["Milady Maker",""],["DeGods",""],["Clone X",""],["Cool Cats",""],["Okay Bears",""],["World of Women",""],["VeeFriends",""],["mfers",""],["Solana Monkey Business",""]]},
{"n":"Generative art NFT","a":"on-chain generative art","d":"A token whose image is produced by a program at the moment of minting, with the code fixed on the blockchain.","t":["Unique NFT","Multi-edition NFT","Curated platform","Fully on-chain"],"s":U+"Generative_art","x":[
 A("Art Blocks","Art Blocks","2020","Generative_art","Platform launched in 2020 by Erick 'Snowfro' Calderon that mints generative art as NFTs on Ethereum.",[("Chromie Squiggle","Snowfro","","First generative collection on Art Blocks")])],
 "m":[["Fidenza","Tyler Hobbs"],["Autoglyphs",""],["Terraforms","Mathcastles"]]},
{"n":"Bitcoin Ordinal inscription","a":"ordinals · inscription","d":"A token recorded on a single satoshi of the Bitcoin blockchain through the ordinals scheme.","t":["Image inscription","Text inscription","Collection inscription"],"s":U+"Non-fungible_token","x":[
 A("Ordinals","Casey Rodarmor","2022","Non-fungible_token","Scheme introduced in December 2022 for placing NFTs on Bitcoin; it pushed up payment fees by February 2023.")],
 "m":[["NodeMonkes",""],["Taproot Wizards",""]]},
{"n":"Virtual land parcel","a":"metaverse land","d":"A plot in a virtual world held as a token that records ownership.","t":["Parcel","Estate","Land with airspace"],"s":U+"Decentraland","x":[
 A("Decentraland","Decentraland","2017","Decentraland","Browser world whose first map, Genesis City, holds 90,601 parcels sold as NFTs for the MANA token.",[
  ("Genesis City parcel","Decentraland","2017","Initial map of 90,601 parcels"),("Parcel sale 2021","Decentraland","2021","Parcels sold from $6,000 to $100,000 in April 2021")]),
 A("The Sandbox land","The Sandbox","2011","The_Sandbox_(company)","Plots of at least 9,216 square metres with airspace to 128 metres, bought with SAND.")]},
{"n":"Game item NFT","a":"in-game asset token","d":"A token that represents an item usable in a game, tradeable outside the game.","t":["Weapon","Character","Cosmetic","Land"],"s":U+"Non-fungible_token","m":[["Age of Rust",""],["Spirit Clash",""],["The Six Dragons",""]]},
{"n":"Blockchain name","a":"ENS name · .eth name","d":"A readable name on a blockchain, such as a .eth name, held as a token and resolving to addresses.","t":["ENS .eth","Subdomain"],"s":"https://ens.readthedocs.io/en/stable/introduction.html","x":[
 A("ENS .eth names","Ethereum Name Service","","https://ens.readthedocs.io/en/stable/introduction.html","Names like alice.eth that map to addresses and content hashes, allocated by a registrar contract.")]},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Larva Labs","Canada","2017","Artisan & independent","CryptoPunks","Two-person studio of Matt Hall and John Watkinson that launched CryptoPunks in June 2017.",U+"CryptoPunks"),
 B("Yuga Labs","United States","","Specialist","Bored Ape Yacht Club","Creator of Bored Ape Yacht Club; owned CryptoPunks IP from 2022 to 2025.",U+"Bored_Ape"),
 B("Art Blocks","United States","2020","Specialist","generative art platform","Platform founded by Erick Calderon that mints generative art on Ethereum.",U+"Generative_art"),
 B("Decentraland","Argentina","2017","Specialist","virtual land","Ethereum virtual world with 90,601 land parcels.",U+"Decentraland"),
 B("The Sandbox","France","2011","Specialist","virtual land","Metaverse platform from Pixowl, selling land plots.",U+"The_Sandbox_(company)"),
 B("Igloo","United States","2022","Specialist","Pudgy Penguins","Parent company of Pudgy Penguins after the April 2022 purchase.",U+"Pudgy_Penguins"),
]
brands=[b for b in brands if b['n']!='Decentraland']+[B("Decentraland","","2017","Specialist","virtual land","Ethereum virtual world with 90,601 land parcels.",U+"Decentraland")]
put('I2','04_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Split the flat NFT list by type. Old collections kept as m only when listed in the brief or old data; Azuki, Doodles, Meebits and others have no retrieved page, so no archetype. Otherside and Autoglyphs, Fidenza details, Taproot Wizards unsourced as archetypes; Fidenza kept in m. Wikipedia has no separate ENS article here, so the ENS docs page is the source. Game item NFT has no archetype; Wikipedia only mentions in-game items generally."})
