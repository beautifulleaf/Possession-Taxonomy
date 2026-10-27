import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,s,mk='',y='',v=(),dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
ST=["chokkan (formal upright)","moyogi (informal upright)","shakan (slant)","kengai (cascade)","han-kengai (semi-cascade)","bunjingi (literati)","yose-ue (forest)","ishitsuki (rock-grown)","sekijoju (root-over-rock)","hokidachi (broom)","fukinagashi (windswept)","ikadabuki (raft)",
    "mame (5–15 cm)","shohin (13–20 cm)","komono (15–25 cm)","chumono (41–91 cm)","dai / omono (76–122 cm)","pre-bonsai","finished tree"]
DT="style · size class · age · pot"; MI="https://mistralbonsai.com/tienda/en/103-aankoop-en-levering-van-bonsai-in-belgie-kwaliteits-bonsai-online?page=2"
BO=W+"Bonsai"
kinds=[
 {"n":"Juniper bonsai","a":"","d":"Living juniper trained and sold as a bonsai.","t":ST,"s":MI,"x":[
  X("Shimpaku juniper","Juniperus chinensis 'Shimpaku' · Chinese juniper","Chinese juniper cultivar group that is among the top subjects of Japanese bonsai, prized for deadwood styling.",W+"Juniperus_chinensis",
    v=[("'Itoigawa'","","","most desirable Shimpaku, tight fine foliage; often grafted"),("'Kyushu'","","","")],dt=DT),
  X("Juniperus procumbens 'Nana'","Japanese mat juniper · Japanese garden juniper","Slow-growing prostrate juniper from Japan trained for its contorted trunk lines; RHS Award of Garden Merit.",W+"Juniperus_procumbens",dt=DT),
 ]},
 {"n":"Pine bonsai","a":"","d":"Living pine trained and sold as a bonsai.","t":ST,"s":MI,"x":[
  X("Japanese black pine","Pinus thunbergii · kuromatsu","Classic coastal Japanese pine for bonsai, trained over many years and decandled to build ramification.",W+"Pinus_thunbergii",v=[("'Kotobuki'","","","named black-pine cultivar cited among notable bonsai")],dt=DT),
  X("Japanese white pine","Pinus parviflora · goyomatsu · Pinus pentaphylla","Five-needled Japanese pine, a popular bonsai tree.",W+"Pinus_parviflora",v=[("Pinus pentaphylla var. negishi 'Sandai Shogun'","","","famous historic bonsai")],dt=DT),
 ]},
 {"n":"Maple bonsai","a":"","d":"Living maple (Acer palmatum, A. buergerianum) trained and sold as a bonsai.","t":ST,"s":MI,"x":[
  X("Japanese maple","Acer palmatum · momiji","Deciduous maple, a popular bonsai choice for leaf colour and fine branching.",W+"Acer_palmatum",
    v=[("'Deshojo'","","","bright red spring and autumn foliage, cold-hardy"),("'Arakawa'","","","rough-bark maple sought after for bonsai"),("'Shishigashira'","","","lion's-mane habit, crinkled leaves; AGM")],dt=DT),
  X("Trident maple","Acer buergerianum","East Asian maple that responds well to leaf reduction and ramification, suiting many styles and sizes.",W+"Acer_buergerianum",dt=DT),
 ]},
 {"n":"Elm & zelkova bonsai","a":"Chinese elm bonsai · keyaki bonsai","d":"Living elm or zelkova trained and sold as a bonsai.","t":ST,"s":W+"Ulmus_parvifolia","x":[
  X("Chinese elm","Ulmus parvifolia · lacebark elm","Perhaps the most widely available bonsai, tolerant of pruning and conditions and good for beginners.",W+"Ulmus_parvifolia",
    v=[("'Hokkaido'","","",""),("'Seiju'","","",""),("'Catlin'","","","")],dt=DT),
  X("Japanese zelkova","Zelkova serrata · keyaki","Japanese tree commonly used for bonsai for its shape and colours.",W+"Zelkova_serrata",dt=DT),
 ]},
 {"n":"Satsuki azalea bonsai","a":"satsuki","d":"Living Satsuki azalea trained as a flowering bonsai, usually grown in Kanuma soil.","t":ST,"s":W+"Satsuki_azalea","x":[
  X("Satsuki azalea","Rhododendron indicum hybrids","Japanese cultivar group of Rhododendron that tolerates hard pruning and gives varied flowers in pots.",W+"Satsuki_azalea",
    v=[("'Chinzan'","","",""),("'Kaho'","","",""),("'Gyoten'","","",""),("'Eikan'","","",""),("'Nikko'","","",""),("'Hakurei'","","",""),("'Kinsai'","","","")],dt="flower colour and pattern · "+DT),
 ]},
 {"n":"Flowering & fruiting bonsai","a":"ume bonsai · quince bonsai · wisteria bonsai","d":"Living flowering or fruiting tree or shrub trained as a bonsai, grown for blossom or fruit.","t":ST,"s":W+"Chaenomeles","x":[
  X("Flowering quince","Chaenomeles · japonica","Spring-flowering East Asian shrub suitable for bonsai.",W+"Chaenomeles",v=[("Chaenomeles japonica","","","Japanese quince"),("Chaenomeles speciosa","","","Chinese flowering quince")],dt=DT),
  X("Japanese wisteria","Wisteria floribunda · fuji","Climbing wisteria trained as a bonsai for its hanging flowers, as is Chinese wisteria.",W+"Wisteria_floribunda",dt=DT),
  X("Ume","Prunus mume · Chinese plum · flowering plum","Winter-flowering East Asian plum grown as a miniature tree in penjing.",W+"Prunus_mume",dt=DT),
 ]},
 {"n":"Tropical bonsai","a":"indoor bonsai","d":"Living tropical tree or shrub (Ficus, jade and others) trained and sold as a bonsai, usually kept indoors.","t":ST,"s":MI,"x":[
  X("Ficus microcarpa","Chinese banyan · Ficus retusa (synonym names)","Fig grown as an indoor plant and bonsai specimen.",W+"Ficus_microcarpa",dt=DT),
  X("Fukien tea","Ehretia microphylla · Carmona retusa · Carmona microphylla","Small-leaved tree popular in penjing and bonsai.",W+"Ehretia_microphylla",dt=DT),
  X("Dwarf jade","Portulacaria afra · elephant bush · spekboom","South African succulent popular as a bonsai specimen.",W+"Portulacaria_afra",dt=DT),
  X("Jade plant","Crassula ovata","Succulent used as an indoor bonsai subject.",W+"Crassula_ovata",v=[("'Gollum'","","","'Monstruosa', 'Hobbit'; AGM")],dt=DT),
 ]},
 {"n":"Kokedama","a":"moss ball · 苔玉","d":"Plant grown in a moss-wrapped ball of akadama and peat instead of a pot, often hung.","t":["hanging","tabletop","fern","foliage houseplant","flowering"],"s":W+"Kokedama"},
]
trads=[
 {"n":"Japanese bonsai","g":"Plants & gardens","r":"Japan","p":"12th century to present",
  "d":"Japanese art of growing trained miniature trees in containers, codified in named styles and size classes.",
  "tech":"pruning, wiring, decandling, deadwood carving, repotting into shallow pots","mat":"juniper, pine, maple, elm, azalea; akadama and Kanuma soils",
  "forms":["Juniper bonsai","Pine bonsai","Maple bonsai","Satsuki azalea bonsai"],"ctr":["Ōmiya Bonsai Village, Saitama (from 1925)","Ōmiya Bonsai Art Museum (2010)","Shunkaen Bonsai Museum, Tokyo (Kunio Kobayashi, 2002)","Kokufu-ten exhibition, Ueno (from 1934)"],
  "auth":"exhibition record (Kokufu-ten), age and provenance of the tree","s":BO},
 {"n":"Chinese penjing","g":"Plants & gardens","r":"China (Lingnan, Shanghai, Yangzhou, Suzhou, Sichuan schools)","p":"Tang dynasty to present",
  "d":"Chinese art of miniature trees and landscapes in containers, precursor of bonsai, saikei and hòn non bộ.",
  "tech":"tree penjing, rock landscape penjing, water-and-land penjing; Lingnan clip-and-grow","mat":"trees, rocks, water, figurines",
  "forms":["Tropical bonsai","Flowering & fruiting bonsai"],"ctr":["Longhua nursery, Shanghai","Shanghai Botanical Garden","Wu Yee-sun, Man Lung Garden, Hong Kong"],"auth":"","s":W+"Penjing"},
 {"n":"Hòn non bộ","g":"Plants & gardens","r":"Vietnam","p":"10th century to present",
  "d":"Vietnamese miniature landscapes of rock, plants and water resembling islands and mountains, viewed from all sides.",
  "tech":"rock-built mountain landscapes in water; tiểu cảnh tree scenes; cây kiểng miniature plants","mat":"rock, plants, water, stone or concrete basins, figurines",
  "forms":[],"ctr":[],"auth":"","s":W+"Hòn_non_bộ"},
 {"n":"Saikei","g":"Plants & gardens","r":"Japan","p":"after 1945",
  "d":"Japanese planted landscape of young trees, rocks, soil and ground cover in one shallow tray, founded by Toshio Kawamoto.",
  "tech":"group planting with rock structure in a low tray","mat":"young trees, rocks, ground cover, ceramic tray",
  "forms":[],"ctr":["Meiju-En nursery (Kawamoto family)"],"auth":"","s":W+"Saikei"},
 {"n":"Kokedama","g":"Plants & gardens","r":"Japan","p":"",
  "d":"Japanese moss-ball planting combining the nearai (no-pot) style with bonsai and kusamono.",
  "tech":"ball of wet akadama and keto wrapped in moss and bound with wire or nylon","mat":"akadama, keto peat, moss, wire",
  "forms":["Kokedama"],"ctr":[],"auth":"","s":W+"Kokedama"},
]
w('C3','08_00',{"kinds":kinds,"brands":[],"traditions":trads,"notes":"All four old kinds kept with old sources; Elm & zelkova, Satsuki, Flowering & fruiting and Kokedama added from Wikipedia. Old 'Itoigawa' and 'Kyushu' became versions of Shimpaku; old Pinus pentaphylla merged into Japanese white pine. Styles and size classes as t types (size classes as named on the Wikipedia Bonsai page; 'chuhin' not on any retrieved page so 'chumono' used). Left out for lack of a retrieved page: 'Kishu' juniper, crabapple bonsai, Shunka-en nursery as a brand (Kunio Kobayashi page names only the Shunkaen Bonsai Museum, listed under the Japanese bonsai tradition). No brand entries: no archetype has a maker."})
