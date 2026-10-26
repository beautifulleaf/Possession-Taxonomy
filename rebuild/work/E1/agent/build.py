import json, os, sys
C = 'E1'
def K(n, d, s, a='', t=None, m=None, r=None, tg=None):
    k = {'n': n, 'a': a, 'd': d}
    if t: k['t'] = t
    if tg: k['tg'] = tg
    k['s'] = s
    if m is not None: k['m'] = m
    if r: k['r'] = r
    return k
def write(job, kinds, notes):
    p = f'work/{C}/shelves/{job}.json'; tmp = p + '.tmp'
    json.dump({'kinds': kinds, 'brands': [], 'traditions': [], 'notes': notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
MOG = 'https://www.mastersofgames.com/cat/indoor/poker.htm'
write('04_05', [
 K('Poker chip set', 'A set of chips, usually in a case, for poker or home casino play.', MOG, t=['Chip set', 'Chip case'],
   m=[['Dal Negro 300 chip Professional Texas Hold em Poker Set', 'Dal Negro'], ['Dal Negro Aspen Poker Set', 'Dal Negro'], ['Fat Cat Replacement Aluminum 500 Count Poker Chip Case', 'Fat Cat']]),
 K('Casino gaming table', 'A table or printed cloth layout for poker, blackjack, craps or baccarat at home.', MOG, t=['Poker table', 'Blackjack table', 'Craps table', 'Table layout cloth']),
 K('Roulette wheel', 'A spinning numbered wheel and ball for playing roulette at home.', 'https://www.mastersofgames.com/cat/table/roulette.htm'),
 K('Card shoe or shuffler', 'A box for dealing cards from several decks, or a device that shuffles them.', 'https://pokerchiplounge.com/products/6-deck-blackjack-shoe', t=['Dealing shoe', 'Card shuffler']),
 K('Bingo set', 'Bingo cards, numbered balls and a cage or drum for drawing numbers or raffle tickets.', 'https://www.mastersofgames.com/cat/indoor/bingo-sets.htm', t=['Bingo set', 'Bingo cage', 'Raffle drum'],
   m=[['Masters Home Bingo Set', 'Masters Traditional Games'], ['Philos Bingo Game (75 balls)', 'Philos']]),
 K('Prize wheel', 'A spinning wheel used to pick a prize or outcome by chance.', 'https://www.mastersofgames.com/cat/fair/wheel-of-fortune-spin-the-wheel.htm', a='wheel of fortune'),
], "Restraint only. Merged Poker chip case into Poker chip set (type), Casino table layout into Casino gaming table (type), Raffle drum into Bingo set (type). Dropped the generic 'Craps layout' entry (not a model). No new kinds or brands.")
CT = 'https://www.canadiantire.ca/en/shop-all/cat/toys-games/pretend-play-DC0002536.html'
write('05_00', [
 K('Play kitchen', "A child's toy kitchen with hob, oven or sink for pretend cooking.", CT),
 K('Play food & cookware set', 'Toy food, pots, pans, dishes or a tea set for pretend cooking and serving.', CT, t=['Play food', 'Toy cookware', 'Tea set']),
 K('Toy shop or tool set', "A child's play shop, tool bench, tool set, play money or toy garden tools for pretend work.", CT, t=['Play shop or till', 'Tool bench or tool set', 'Play money', 'Toy garden tools']),
 K('Dress-up accessory', 'A toy crown, wand, wings or similar piece for dressing up.', 'https://www.bunnings.com.au/2-pack-crown-wand-set-tiara-for-costume-and-dress-ups-multicolour-no-none_p1031016'),
 K('Play make-up set', 'Pretend make-up or a toy beauty salon made for children.', 'https://well.ca/products/melissa-doug-wooden-beauty-salon_121280.html',
   m=[['Melissa & Doug Wooden Beauty Salon Play Set', 'Melissa & Doug']]),
], "Restraint only: kept all five kinds at kind level, tightened definitions, added attribute types. The only model in the old data (Melissa & Doug beauty salon) kept; the brief's other brands (KidKraft, Le Toy Van, Hape, IKEA Duktig) have no models in the old data, so none added.")
BJ = 'https://www.bigjigstoys.co.uk/collections/rattles-teethers'
B = ['baby']
write('06_00', [
 K('Rattle', 'A handheld toy that rattles when shaken, for an infant.', BJ, tg=B,
   m=[['FSC Certified Wooden Roll Rattle', 'Bigjigs Toys'], ['Rainbow Rattle', 'Bigjigs Toys'], ['Rattle Keys', 'Bigjigs Toys'], ['Tiger Tribe Silicone Rattle', 'Tiger Tribe']]),
 K('Activity play mat', 'A padded floor mat, often with an arch of hanging toys, for baby floor play.', 'https://www.thetoyinsider.com/toys/lamaze-4-in-1-play-gym/', a='play gym', tg=B,
   m=[['Lamaze 4-in-1 Play Gym', 'TOMY International']]),
 K('Stacking toy', 'Rings, cups or blocks that a small child stacks.', 'https://www.walmart.com/c/kp/stacking-toys', tg=B, t=['Ring stacker', 'Stacking cups', 'Stacking blocks'],
   m=[['Fisher-Price Rock-a-Stack', 'Fisher-Price'], ['Sassy Stacks of Circles', 'Sassy'], ['Baby Einstein Alpha Stacks', 'Baby Einstein'], ['Learning Resources Stacking Shapes Pegboard', 'Learning Resources']]),
 K('Shape sorter', 'A box or toy with shaped holes and matching pieces to post through them.', 'https://www.walmart.com/c/kp/stacking-toys', tg=B,
   m=[["Fisher-Price Baby's First Blocks", 'Fisher-Price']]),
 K('Activity table', 'A child-height table with built-in toys or sand and water trays for standing play.', 'https://www.wintergreen.ca/toddler-sand-water-table-lc978', tg=B, t=['Activity table', 'Sand and water table']),
 K('Bath toy', 'A toy made to float, pour or squirt in the bath.', 'https://www.bigjigstoys.co.uk/products/sensory-bath-set', tg=B,
   m=[['Bigjigs Sensory Bath Set', 'Bigjigs Toys'], ['Tiger Tribe Bath Shakers', 'Tiger Tribe']]),
], "Restraint only: every kind tagged baby; Bigjigs rattle list trimmed (dropped Honey Bear Rattle and Tiger Tribe Rattle & Stack Blocks). Brief brands Hape has no models in old data, so none added.")
PP = 'https://www.plumplay.co.uk/collections/metal-swings'
write('09_00', [
 K('Swing set', 'A garden frame with swing seats; replacement seats sold alone are a type.', PP, t=['Wooden swing set', 'Metal swing set', 'Replacement swing seat'],
   m=[['Plum Bush Baby Wooden Swing Set', 'Plum Play'], ['Plum Giant Baboon Wooden Swing Set', 'Plum Play'], ['Plum Tamarin Wooden Swing Set', 'Plum Play'], ['Plum Woolly Monkey II Wooden Swing Set', 'Plum Play'], ['Swingan Belt Swing Seat', 'Machrus']],
   r=[['Plum wooden swing sets', 'Plum Play']]),
 K('Slide or climbing frame', 'A garden slide, climbing frame or play centre for children.', PP, t=['Slide', 'Climbing frame', 'Climbing dome', 'Play centre'],
   m=[['Plum Barbary Wooden Playcentre', 'Plum Play'], ['Plum Siamang Wooden Playcentre', 'Plum Play'], ['Plum Metal Climbing Dome Frame', 'Plum Play'], ['Plum Wooden Climbing Cube XL with Swing Arm', 'Plum Play']]),
 K('Garden trampoline', 'An outdoor trampoline for play, larger than an exercise rebounder.', PP, a='play trampoline', m=[['Plum Springsafe Trampoline', 'Plum Play']]),
 K('Playhouse', 'A rigid outdoor play house or treehouse for children.', PP, a='treehouse'),
 K('Sandpit', 'A box or framed pit, often lidded, holding sand for children to play in.', PP, a='sandbox'),
 K('Seesaw', 'A beam pivoted at the centre with a seat at each end, rocked by two children.', 'https://www.diy.ie/departments/plum-premium-seesaw/243015_BQ.prd?hero', m=[['Premium Wooden Seesaw', 'Plum Play']]),
 K('Paddling pool', 'A shallow pool for children, up to about 400 mm of water depth.', 'https://www.walmart.com/c/kp/paddle-pools', t=['Inflatable', 'Rigid'],
   m=[['Intex Mushroom Inflatable Baby Pool', 'Intex'], ['Intex Summer Colors Inflatable Swimming Pool', 'Intex'], ['Intex Whale Kids Inflatable Pool', 'Intex']]),
 K('Inflatable activity toy', 'An inflatable play centre, bouncy castle or water park for the garden.', 'https://www.currys.co.uk/home-and-outdoor/garden-and-outdoors/swimming-pools-and-accessories/inflatable-kids-pools-and-toys', t=['Bouncy castle', 'Inflatable play centre', 'Inflatable water park'],
   m=[['Bestway H2OGO! Jump and Soar Bouncy Castle', 'Bestway'], ['Bestway H2OGO! Beach Bounce Water Park', 'Bestway'], ['Intex Rainbow Ring Inflatable Play Center', 'Intex'], ['Intex Dinoland Inflatable Play Center', 'Intex']]),
 K('Water play toy', 'A toy for the pool, beach or garden water play.', PP,
   m=[['Intex Explorer Pro Inflatable Pool Boat', 'Intex'], ['Nerf Super Soaker Hop & Chomp', 'Nerf'], ['Nerf Super Soaker Stomp & Soak', 'Nerf']], r=[['Super Soaker', 'Nerf']]),
], "Restraint only: Swing seat merged into Swing set as the 'Replacement swing seat' type; Plum swing-set and play-centre lists trimmed to four each; Bestway water-park list trimmed. Brief brands Little Tikes, Springfree and Hedstrom have no models in the old data, so none added.")
