import csv,sys
S={'P':'Professional & flagship','Pr':'Premium','M':'Mainstream','V':'Value','H':'Heritage manufactory','A':'Artisan & independent','S':'Specialist','O':'Own-label & retailer','I':'Institution & issuer'}
D="""ARS|P|pruning shears
ARS Corporation|P|pruning shears
Alfa Forni|Pr|pizza ovens
Alitex|Pr|greenhouses
Allen Manufacturing Company|H|hex keys
Allett|S|cylinder mowers
Allis-Chalmers|H|tractors
Altendorf|P|sliding table saws
Anaglypta|H|relief wallpaper
Annie Sloan Interiors|S|chalk paint
Anthura|S|anthuriums
Associated Manufacturers Company|H|farm engines
Australian Char|M|barbecue briquettes
Aveling & Porter|H|steamrollers
BCS|S|walking tractors
Bahco|P|hand tools
Behr|M|house paint
Benjamin Moore|Pr|house paint
Bessey|P|clamps
Big Green Egg|P|kamado grills
Big K|M|charcoal
Black & Decker|M|power tools
Blackstone|M|outdoor griddles
Blackstone & Co|H|oil engines
Blue Spruce Toolworks|A|marking knives
Bolinder|H|semi-diesel engines
Bondhus|S|hex keys
Broil King|M|gas grills
Brown & Sharpe|H|micrometers
Bulldog Tools|H|forged spades
Burgon & Ball|H|garden shears
Carlisle Brass|M|door furniture
Carron Company|H|cast iron
Case|H|steam engines
Caterpillar|P|crawler tractors
Channellock|Pr|pliers
Char-Broil|V|gas grills
Charles Burrell & Sons|H|showman's engines
Clayton & Shuttleworth|H|threshing machines
Cletrac|H|crawler tractors
Clifton|Pr|hand planes
Cobb|S|portable grills
CobraHead|A|hand weeders
Cole & Son|H|wallpaper
Condor Tool & Knife|Pr|machetes
Costa Farms|M|houseplants
Craven Dunnill|H|encaustic tiles
Crescent|M|adjustable wrenches
Crown Paints|M|house paint
Cultivar|A|greenhouses
Darlac|M|garden tools
David Brown|H|tractors
DeWalt|P|power tools
DeWit|A|forged garden tools
Delta|M|woodworking machinery
Deutz|M|tractors
Dibleys Nurseries|A|streptocarpus
Disston|H|handsaws
Dremel|M|rotary tools
Dulux|M|house paint
Duracell|M|batteries
EGO|Pr|cordless garden tools
ELU|H|plunge routers
EVE Energy|M|battery cells
Echo|P|chainsaws
Eclipse|M|hacksaws
Edward Elwell|H|edge tools
Eicher|H|tractors
Elite|M|greenhouses
Energizer|M|batteries
Erin Pottery|A|bonsai pots
FSB|Pr|door handles
Fairbanks-Morse|H|farm engines
Falci|S|scythes
Farma|S|forestry trailers
Farrow & Ball|Pr|heritage paint
Fein|P|multi-tools
Felco|P|secateurs
Felder|P|woodworking machinery
Fendt|P|tractors
Ferguson|H|tractors
Festool|P|power tools
First Tunnels|S|polytunnels
Flymo|M|hover mowers
Fontana Forni|Pr|wood-fired ovens
Fordson|H|tractors
Freund Victoria|M|spades
GP Batteries|V|batteries
Gabriel Ash|Pr|cedar greenhouses
Gardena|M|watering systems
Gedore|P|spanners
Glaser|S|wheel hoes
Glen-Drake Toolworks|A|marking gauges
Gozney|Pr|pizza ovens
Gramercy Tools|A|hand tools
Guillouard|H|watering cans
Gyozan|A|bonsai pots
Gysinge|S|linseed oil paint
HOPPE|M|door handles
Hakki Pilke|P|firewood processors
Hammer|M|woodworking machinery
Hanomag|H|tractors
Harris|M|paint brushes
Hart-Parr|H|early tractors
Hartley Botanic|Pr|glasshouses
Haws|H|watering cans
Hayter|Pr|lawn mowers
Heidelberg Materials|M|cement
Hercules Gas Engine Company|H|hit-and-miss engines
Hilti|P|construction tools
Holcim|M|cement
Holt|H|crawler tractors
Husqvarna|P|chainsaws
Imacasa|M|machetes
Interapid|P|test indicators
International Harvester|H|farmall tractors
Irwin|M|clamps
Isabelia|A|bonsai pots
Ivel Agricultural Motors|H|early tractors
Japa|S|firewood processors
John Deere|M|tractors
John Fowler & Co.|H|ploughing engines
Jorgensen|M|clamps
Joseph Bentley|M|stainless spades
Joshua Roth|S|bonsai tools
Juliana|Pr|greenhouses
Kamado Joe|Pr|kamado grills
Kaneshin|S|bonsai tools
Kesla|S|forestry cranes
Kikuwa|S|bonsai tools
Kingsford|M|charcoal briquettes
Kioti|V|compact tractors
Klein Tools|P|electricians' tools
Knew Concepts|A|fret saws
Knipex|P|pliers
Krumpholz|A|forged spades
Kubota|M|compact tractors
LG Energy Solution|M|lithium-ion cells
LS Tractor|V|compact tractors
Ladda|S|aglaonema
Laguna|Pr|bandsaws
Lamello|P|biscuit joiners
Landini|M|tractors
Lanz|H|bulldog tractors
LazyLawn|M|artificial grass
Lechuza|Pr|self-watering planters
Lie-Nielsen Toolworks|P|hand planes
Lincrusta|H|relief wallcovering
Little Greene|Pr|heritage paint
Logosol|S|chainsaw mills
London Brick Company|H|fletton bricks
Louisiana Grills|M|pellet grills
Lufkin|M|measuring tapes
M.K. Mole and Son|H|locking pliers
Mahindra|V|tractors
Makita|P|power tools
Mantis|S|small tillers
Marshall, Sons & Co.|H|traction engines
Marshalls|M|paving
Marshalltown|P|trowels
Masakuni|P|bonsai tools
Massey Ferguson|M|tractors
Massey-Harris|H|farm machinery
Maw & Co|H|encaustic tiles
Meadow Creature|A|broadforks
Metabo|P|power tools
Millers Falls|H|hand drills
Milwaukee|P|power tools
Minimax|M|combination machines
Mintons|H|tiles
Mitutoyo|P|micrometers
Molicel|S|high-power cells
Montana Cans|S|spray paint
Montana Colors|S|spray paint
Moore & Wright|H|micrometers
Morris & Co.|H|block-printed wallpaper
Morris of Dunsford|A|billhooks
Murata|M|battery cells
Namgrass|M|artificial grass
Napoleon|Pr|gas grills
New Holland|M|tractors
Niwaki|O|japanese garden tools
Norris|H|infill planes
North Bros.|H|yankee screwdrivers
Norwood|M|portable sawmills
Nuffield|H|tractors
Officine Egidio Brugola|H|hex keys
Okatsune|P|secateurs
Oklahoma Joe's|M|offset smokers
Ooni|M|pizza ovens
Original LÖWE|P|anvil secateurs
Ottosson Färgmakeri|S|linseed oil paint
PB Swiss Tools|P|screwdrivers
Palms|S|forestry trailers
Pasquali|S|two-wheel tractors
Paul Ecke Ranch|S|poinsettias
Petters Limited|H|stationary engines
Pit Boss|V|pellet grills
Porsche-Diesel|H|tractors
Posch|S|firewood processors
Powermatic|P|woodworking machinery
Purdy|Pr|paint brushes
Quangsheng|V|hand planes
R A Lister and Company|H|stationary engines
Ransomes|H|lawn mowers
Ransomes, Sims & Jefferies|H|ploughs
Record|H|vices
Record Power|M|woodworking machinery
Reiho|A|bonsai pots
Rhino|Pr|greenhouses
Richard Hornsby & Sons|H|oil engines
Ridgid|M|pipe tools
Rinaldi|S|billhooks
Robland|M|combination machines
Royal Delft|H|delftware
Royal Tichelaar Makkum|H|tin-glazed pottery
Rubi|P|tile cutters
Rust-Oleum|M|protective coatings
Ryobi|M|diy power tools
SAME|M|tractors
STIHL|P|chainsaws
Saint-Astier|S|hydraulic lime
Samsung SDI|M|lithium-ion cells
SawStop|P|safety table saws
Scalamandré|Pr|wallpaper and fabric
Scheppach|V|woodworking machinery
Schröckenfux|H|scythes
Sherwin-Williams|M|paint
Shinwa|M|rules and squares
Silky|P|pruning saws
Sjöbergs|M|workbenches
Smart Pot|S|fabric pots
Snap-on|P|automotive tools
Sneeboer|A|forged garden tools
Spear & Jackson|M|garden tools
Starrett|P|precision measuring
Stover Manufacturing and Engine Company|H|farm engines
Straight|M|water butts
TESA|P|precision measuring
Tajfun|S|forestry winches
Terrateck|S|wheel hoes
Thomas Flinn & Co|H|backsaws
TigerTurf|M|synthetic turf
Timorous Beasties|A|wallpaper
Tina|S|grafting knives
Tobisho|A|forged secateurs
Traeger|M|pellet grills
Trend|S|router cutters
Ty-Mawr Lime|S|lime products
Uniforest|S|forestry winches
Uriarte Talavera|H|talavera pottery
Ursus|H|tractors
VARTA|M|batteries
Valspar|M|house paint
VegTrug|M|raised beds
Veritas|Pr|hand planes
Vermeer|P|stump grinders
Victa|M|rotary mowers
Wagner|M|paint sprayers
Walsall Studio Ceramics|A|bonsai pots
Waterloo Gasoline Engine Company|H|waterloo boy tractors
Weber|M|kettle grills
Wera|P|screwdrivers
Whichford Pottery|A|terracotta pots
Wiha|P|screwdrivers
Wolseley Sheep Shearing Machine Company|H|shearing machines
Wood-Mizer|P|band sawmills
Worx|M|cordless tools
Yamaaki|A|bonsai pots
Yoder Smokers|Pr|offset smokers
Zetor|V|tractors
Zuber & Cie|H|panoramic wallpaper
de Gournay|Pr|hand-painted wallpaper"""
G=sys.argv[1]
rows=[l.split('|') for l in D.splitlines()]
with open(f'{G}.map.tsv.tmp','w',encoding='utf-8') as f:
    f.write('name\tseg\tkf\n')
    for n,s,k in rows: f.write(f'{n}\t{S[s]}\t{k}\n')
import os; os.replace(f'{G}.map.tsv.tmp',f'{G}.map.tsv')
