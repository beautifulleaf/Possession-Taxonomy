import json, os
W = 'https://en.wikipedia.org/wiki/'
BT = W + 'Buffalo_Trace_Distillery'; PVW = W + 'Pappy_Van_Winkle%27s_Family_Reserve'; MM = W + 'Maker%27s_Mark'
WT = W + 'Wild_Turkey_(bourbon)'; JB = W + 'Jim_Beam'; OF = W + 'Old_Forester'; JD = W + 'Jack_Daniel%27s'
GD = W + 'George_Dickel'; TW = W + 'Tennessee_whiskey'; FR = W + 'Four_Roses'; WR = W + 'Woodford_Reserve'
HH = W + 'Heaven_Hill'; RW = W + 'Rye_whiskey'; WP = W + 'WhistlePig'; OO = W + 'Old_Overholt'; BU = W + 'Bulleit_Bourbon'
MI = W + 'Michter%27s'; CW = W + 'Corn_whiskey'; BW = W + 'Bourbon_whiskey'; WL = W + 'Westland_Distillery'
ST = W + 'Stranahan%27s_Colorado_Whiskey'; WW = W + 'Wheat_whiskey'; SZ = W + 'Sazerac_Company'; BL = W + 'Blanton%27s'
EC = W + 'Elijah_Craig_(bourbon)'; EW = W + 'Evan_Williams_(bourbon)'; RY = W + 'Rebel_Yell_(bourbon)'
TTB = 'https://www.ttb.gov/public-information/featured-stories/ttb-establishes-american-single-malt-whisky-standard-identity'


def X(n, d, mk, y, s, v=(), dt='', a=''):
    return {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s,
            'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v], 'dt': dt}

BTD = 'Buffalo Trace Distillery'
bourbon = {
 'n': 'Bourbon', 'a': 'Kentucky straight bourbon · bourbon whiskey',
 'd': 'American whiskey from a mash of at least 51% corn, aged in new charred oak containers.',
 't': ['Straight bourbon (2+ years)', 'Bottled-in-bond (one season, 4+ years, 100 proof)', 'Small batch', 'Single barrel',
       'Barrel proof / cask strength', 'Wheated mash bill', 'High-rye mash bill'],
 's': BW,
 'x': [
  X('Old Forester', 'The first bourbon sold only in sealed bottles; rye-rich mash bill.', 'Brown-Forman', '1870', OF,
    [('Old Forester Classic', 'Brown-Forman', '', '86 proof'), ('Old Forester Signature', 'Brown-Forman', '', '100 proof'),
     ('1870 Original Batch', 'Brown-Forman', '', 'Whisky Row series'), ('1897 Bottled in Bond', 'Brown-Forman', '', 'Whisky Row series'),
     ('1910 Old Fine Whisky', 'Brown-Forman', '', 'Whisky Row series'), ('1920 Prohibition Style', 'Brown-Forman', '2016', '115 proof'),
     ('Birthday Bourbon', 'Brown-Forman', '2002', 'annual release')], 'proof 86–115 · Whisky Row series'),
  X('Buffalo Trace', 'Flagship straight bourbon of the Frankfort distillery.', BTD, '1999', BT, [], 'straight bourbon'),
  X('Pappy Van Winkle', 'Long-aged wheated bourbon, the most sought-after allocated bottle.', 'Van Winkle', '2002 (made at Buffalo Trace)', PVW,
    [("Pappy Van Winkle's Family Reserve 15 Year", 'Van Winkle', '', '107 proof'), ("Pappy Van Winkle's Family Reserve 20 Year", 'Van Winkle', '', '90.4 proof'),
     ("Pappy Van Winkle's Family Reserve 23 Year", 'Van Winkle', '', '95.6 proof'), ('Old Rip Van Winkle 10 Year', 'Van Winkle', '', 'related brand'),
     ('Van Winkle Special Reserve 12 Year Lot B', 'Van Winkle', '', '')], 'age 10–23 years · wheated', 'Pappy · Van Winkle'),
  X('W. L. Weller', 'Wheated bourbon line sharing its mash bill family with Van Winkle.', BTD, '', BT,
    [('W. L. Weller Antique 107', BTD, '', ''), ('W. L. Weller 12 Year', BTD, '', ''), ('W. L. Weller Single Barrel', BTD, '', ''),
     ('W. L. Weller Full Proof', BTD, '', 'old data')], 'wheated · proof and age'),
  X("Maker's Mark", 'Wheated bourbon (no rye) sealed in red wax.', "Maker's Mark", '1958', MM,
    [("Maker's Mark", "Maker's Mark", '1958', '90 proof'), ("Maker's 46", "Maker's Mark", '', 'seared French oak staves, 47% ABV'),
     ("Maker's Mark Cask Strength", "Maker's Mark", '2014', 'about 106–116 proof'), ("Maker's Mark 101", "Maker's Mark", '2018', 'duty-free first')],
    'wheated mash bill · red wax seal'),
  X("Blanton's", 'First modern bourbon marketed as single barrel; racehorse stopper.', BTD, '1984', BL,
    [("Blanton's Original Single Barrel", BTD, '1984', '93 proof'), ("Blanton's Gold", BTD, '', '103 proof'),
     ("Blanton's Straight From the Barrel", BTD, '', 'cask strength'), ("Blanton's Special Reserve", BTD, '', '80 proof, export only')],
    'single barrel · eight stopper letters'),
  X('Wild Turkey 101', 'High-proof Kentucky bourbon from Lawrenceburg.', 'Wild Turkey', '1942', WT,
    [('Wild Turkey 81', 'Wild Turkey', '', ''), ('Wild Turkey Rare Breed', 'Wild Turkey', '', ''), ('Wild Turkey Kentucky Spirit', 'Wild Turkey', '', ''),
     ("Russell's Reserve", 'Wild Turkey', '', '6, 10, 13, 15 year and single barrel')], 'proof 81–101 · Russell\'s Reserve line'),
  X("Booker's", "Beam's first uncut, straight-from-the-barrel bourbon.", 'Jim Beam', '1988', JB, [], 'aged 6+ years · 120–129.2 proof'),
  X('Jim Beam', 'High-volume Kentucky bourbon from Clermont.', 'Jim Beam', '', JB,
    [('Jim Beam White Label', 'Jim Beam', '', ''), ('Jim Beam Black', 'Jim Beam', '', '7 years, 90 proof'), ("Jim Beam Devil's Cut", 'Jim Beam', '2011', 'barrel-rinse')], ''),
  X('Knob Creek', 'Nine-year, 100-proof bourbon in the Beam small-batch range.', 'Jim Beam', '', JB,
    [('Knob Creek Single Barrel', 'Jim Beam', '', '120 proof')], ''),
  X("Baker's", 'Seven-year, 107-proof Beam bourbon.', 'Jim Beam', '', JB),
  X("Basil Hayden's", 'Lighter 80-proof bourbon on the Old Grand-Dad high-rye mash bill.', 'Jim Beam', '', JB),
  X('Old Grand-Dad', 'High-rye bourbon brand, Beam-owned since 1987.', 'Jim Beam', '', JB),
  X('Four Roses', 'Ten recipes from two mash bills and five yeasts.', 'Four Roses', '1888', FR,
    [('Four Roses Bourbon', 'Four Roses', '', '80 proof'), ('Four Roses Small Batch', 'Four Roses', '', '90 proof'),
     ('Four Roses Single Barrel', 'Four Roses', '', '100 proof'), ('Four Roses Small Batch Select', 'Four Roses', '2019', '104 proof')],
    'recipe (mash bill × yeast) · proof'),
  X('Woodford Reserve', 'Small-batch bourbon blending pot- and column-still spirit.', 'Brown-Forman', '1996', WR,
    [('Woodford Reserve Double Oaked', 'Brown-Forman', '', ''), ("Woodford Reserve Master's Collection", 'Brown-Forman', '', 'limited')], ''),
  X('Evan Williams', "Heaven Hill's mass-market bourbon.", 'Heaven Hill', '1957', EW,
    [('Evan Williams Black Label', 'Heaven Hill', '', '86 proof'), ('Evan Williams White Label', 'Heaven Hill', '', 'bottled in bond'),
     ('Evan Williams Single Barrel', 'Heaven Hill', '', 'vintage-dated'), ('Evan Williams 1783', 'Heaven Hill', '', '86 proof')], ''),
  X('Elijah Craig', 'Heaven Hill small-batch bourbon; Barrel Proof batches collected by code.', 'Heaven Hill', '1986', EC,
    [('Elijah Craig Small Batch', 'Heaven Hill', '', '94 proof'), ('Elijah Craig Barrel Proof', 'Heaven Hill', '2013', 'three batches a year, e.g. C924'),
     ('Elijah Craig 18 Year Single Barrel', 'Heaven Hill', '', ''), ('Elijah Craig 23 Year Single Barrel', 'Heaven Hill', '', '')], 'batch code · age'),
  X('Larceny', 'Wheated Heaven Hill bourbon.', 'Heaven Hill', '', HH, [('Larceny Barrel Proof C925', 'Heaven Hill', '', 'old data')]),
  X('Eagle Rare', 'Straight bourbon with a 17-year Antique Collection release.', BTD, '', BT, [('Eagle Rare 17 Year', BTD, '', 'Antique Collection')]),
  X('George T. Stagg', 'Barrel-proof bourbon named for an earlier name of the distillery.', BTD, '', BT, [('Stagg Jr.', BTD, '', '')]),
  X('Col. E. H. Taylor', 'Small batch, single barrel and barrel proof line.', BTD, '', BT, [('E.H. Taylor Jr. Small Batch', BTD, '', 'old data')]),
  X('Bulleit Bourbon', 'High-rye bourbon (about 28% rye).', 'Diageo', '1995', BU,
    [('Bulleit 10 Year', 'Diageo', '', '91.2 proof'), ('Bulleit Barrel Strength', 'Diageo', '', '118–125 proof')]),
  X('Rebel Yell', 'Wheated Stitzel-Weller-lineage bourbon, renamed Rebel in 2020.', 'MGP Ingredients', '1936', RY, [], '80 proof'),
  X('1792', 'Barton 1792 distillery bourbon.', 'Sazerac Company', '', SZ, [('1792 Small Batch', 'Sazerac Company', '', 'old data')]),
 ],
 'm': [['15 STARS Kentucke County Straight 6 YO', '15 STARS'], ['ASW Distillery Fiddler Encore Georgia Oak', 'ASW Distillery'],
       ['Bardstown Bourbon Company Lochs of Jura Barrel 10 YO', 'Bardstown Bourbon Company'], ['Belle Meade Reserve 11 YO Cask Strength', 'Belle Meade'],
       ['Frank August Case Study 05 Wheated Reserve', 'Frank August'], ['Frey Ranch Straight Bourbon', 'Frey Ranch'],
       ['Kentucky Beau', 'Heaven Hill'], ['New Riff Bottled-In-Bond', 'New Riff'], ['O.K.I. Bourbon 15 Year Old', 'O.K.I. Bourbon'],
       ['Rabbit Hole Dareringer PX Sherry Cask', 'Rabbit Hole'], ['Redemption Straight Bourbon', 'Redemption'], ['Safai Bourbon 8 Year Old', 'Safai'],
       ['Whiskey Tree Wheated Bourbon', 'Seven Three Distilling'], ['Starlight Distillery Single Barrel Bourbon', 'Starlight Distillery'],
       ['Old Bardstown Bottled in Bond 4 YO', 'Willett'], ["Noah's Mill Small Batch", 'Willett'], ["Rowan's Creek", 'Willett'], ['Johnny Drum', 'Willett'],
       ['Ancient Age', BTD], ['Rock Hill Farms', BTD], ['Old Charter', BTD], ['Old Taylor', BTD],
       ['Very Old Barton', 'Sazerac Company'], ['Kentucky Gentleman', 'Sazerac Company'], ['Ezra Brooks', ''], ['Kentucky Tavern', '']],
}
tenn = {
 'n': 'Tennessee whiskey', 'a': 'Tennessee whisky',
 'd': 'Straight bourbon-style whiskey made in Tennessee and filtered through maple charcoal (Lincoln County Process) before ageing.',
 't': ['Single barrel', 'Bottled-in-bond'], 's': TW,
 'x': [
  X("Jack Daniel's Old No. 7", 'Black-label charcoal-mellowed whiskey from Lynchburg.', 'Brown-Forman', '', JD,
    [("Jack Daniel's Single Barrel", 'Brown-Forman', '1997', '94 proof'), ("Jack Daniel's Bottled-in-Bond", 'Brown-Forman', '', '100 proof'),
     ("Jack Daniel's Sinatra Select", 'Brown-Forman', '', '90 proof')], 'proof 80–100', 'Black Label · JD'),
  X('Gentleman Jack', "Jack Daniel's whiskey charcoal-filtered twice.", 'Brown-Forman', '', JD, [], '80 proof'),
  X('George Dickel', "Chill-filtered Cascade Hollow whisky spelt the Scottish way.", 'Diageo', '1964', GD,
    [('George Dickel Old No. 8', 'Diageo', '', 'black label, 80 proof'), ('George Dickel Superior No. 12', 'Diageo', '', '90 proof'),
     ('George Dickel Barrel Select', 'Diageo', '', '')], 'numbered labels · proof'),
 ],
 'm': [['Uncle Nearest Premium Whiskey', 'Uncle Nearest'], ["Benjamin Prichard's", "Benjamin Prichard's"],
       ["Nelson's Green Brier", "Nelson's Green Brier Distillery"], ['Chattanooga Whiskey', 'Chattanooga Whiskey Company']],
}
rye = {
 'n': 'Rye whiskey', 'a': 'rye · straight rye',
 'd': 'Whiskey from a mash of at least 51% rye, aged in new charred oak in the US.',
 't': ['Straight rye', 'Bottled-in-bond', 'Pennsylvania / Monongahela style', 'Maryland style', 'Barrel proof'], 's': RW,
 'x': [
  X('Old Overholt', "America's oldest continually maintained whiskey brand; Monongahela rye heritage.", 'A. Overholt & Co.', '1810', OO,
    [('Old Overholt', 'A. Overholt & Co.', '', '4 years, 86 proof'), ('Old Overholt Bottled in Bond', 'A. Overholt & Co.', '2017', '100 proof'),
     ('A. Overholt Monongahela Mash', 'A. Overholt & Co.', '2024', '80% rye, 20% malted barley')]),
  X('Rittenhouse', 'Heaven Hill bottled-in-bond rye, a bartender standard.', 'Heaven Hill', '', RW,
    [('Rittenhouse Bottled-in-Bond Rye 100 Proof', 'Heaven Hill', '', 'old data')]),
  X('Sazerac Rye', 'Straight rye named after the New Orleans coffee house.', 'Sazerac Company', '', BT,
    [('Sazerac 18 Year Old', 'Sazerac Company', '', 'Antique Collection'), ('Thomas H. Handy', BTD, '', 'barrel-proof rye, Antique Collection')]),
  X('WhistlePig', 'Vermont rye brand begun with aged Canadian rye.', 'WhistlePig', '2010', WP,
    [('WhistlePig 10 Year Small Batch', 'WhistlePig', '2015', ''), ('WhistlePig 12 Year Old World Cask Finish', 'WhistlePig', '', 'Port, Sauternes, Madeira'),
     ('WhistlePig 15 Year Estate Oak', 'WhistlePig', '', ''), ('WhistlePig Boss Hog', 'WhistlePig', '2013', 'annual single-barrel edition'),
     ('WhistlePig PiggyBack 6 Year', 'WhistlePig', '', ''), ('WhistlePig FarmStock', 'WhistlePig', '2017', '')], 'age · finish · annual Boss Hog edition'),
  X('Bulleit Rye', '95% rye mash bill, distilled by MGP in Indiana.', 'Diageo', '2011', BU),
  X("Michter's", 'Revived Pennsylvania name now made in Kentucky.', "Michter's", '2004 (Kentucky)', MI,
    [("Michter's US No.1 Rye", "Michter's", '', 'old data')]),
 ],
 'm': [['Pikesville Rye', 'Heaven Hill'], ['Van Winkle Family Reserve Rye 13 Year', 'Van Winkle'], ['Knob Creek Rye', 'Jim Beam'], ['Jim Beam Rye', 'Jim Beam'],
       ['George Dickel Rye', 'Diageo'], ["Jack Daniel's Tennessee Rye", 'Brown-Forman'], ['Woodford Reserve Straight Rye', 'Brown-Forman'],
       ['High West Rye', ''], ['Templeton Rye', ''], ["George Washington's Rye", ''], ["Leopold Bro's Maryland-style Rye", ''],
       ['Wigle Reserve Pennsylvania Straight Rye', ''], ['Copper Fox Rye', ''], ['Roundstone Rye', ''], ['Town Branch Rye', ''],
       ['Never Say Die Rye Whiskey', 'Never Say Die'], ['Wenzel Whiskey Rectifier Rye', 'Wenzel Whiskey'],
       ['Greenbanks Tasmanian Whisky Co. Rye Cask 027', 'Greenbanks Tasmanian Whisky Co.'], ['Siderit PX Cask Rye', 'Siderit']],
}
wheat = {
 'n': 'Wheat whiskey', 'a': 'wheat whisky · straight wheat whiskey',
 'd': 'Whiskey from a mash of at least 51% wheat; distinct from wheated bourbon.', 't': ['Straight wheat whiskey'], 's': WW,
 'x': [X('Bernheim Original', "Heaven Hill's straight wheat whiskey, the best-known mass-market example.", 'Heaven Hill', '', HH,
         [('Bernheim Straight Wheat Whiskey', 'Heaven Hill', '', 'old data')])],
 'm': [['Woodford Reserve Wheat Whiskey', 'Brown-Forman'], ['Daniel Weller Emmer Wheat', BTD], ['Old Elk', 'Old Elk'], ['Dry Fly', 'Dry Fly'], ['Middle West', 'Middle West']],
}
corn = {
 'n': 'Corn whiskey', 'a': 'corn whisky',
 'd': 'Whiskey from a mash of at least 80% corn, unaged or aged in used or uncharred oak.', 't': ['Unaged / white', 'Bottled-in-bond', 'Mason-jar moonshine style'], 's': CW,
 'x': [X('Mellow Corn', 'Heaven Hill bottled-in-bond corn whiskey.', 'Heaven Hill', '', HH),
       X('Georgia Moon', 'Unaged corn whiskey sold in a mason jar.', 'Heaven Hill', '', CW)],
 'm': [['George Dickel No. 1 Foundation Recipe', 'Diageo'], ['Black Jack Classic', 'Black Jack'], ['Dancing Goat Distillery The Spaniard', 'Dancing Goat Distillery'],
       ['Kings County Corn Whiskey', 'Kings County'], ['Midnight Moon', ''], ['Ole Smoky', ''], ['Platte Valley', ''], ['The Gonzales Corn Whiskey', '']],
}
asm = {
 'n': 'American single malt whiskey', 'a': 'American single malt whisky',
 'd': 'US whisky from 100% malted barley, distilled at one distillery and aged in oak casks of up to 700 litres.', 't': ['Straight (2+ years)', 'Peated', 'Cask-finished'], 's': TTB,
 'x': [X('Westland', 'Seattle single malt built on local barley and Garryana oak editions.', 'Westland Distillery', '2011', WL,
         [('Westland Flagship', 'Westland Distillery', '', '40 months, 46% ABV'), ('Westland Solum Edition 3', 'Westland Distillery', '', ''),
          ('Westland Colere Edition 4', 'Westland Distillery', '', ''), ('Westland Garryana Edition 9', 'Westland Distillery', '', '5 years')], 'edition series · cask'),
       X("Stranahan's", 'Colorado single malt from Denver, first bottled 2006.', "Stranahan's", '2004', ST,
         [("Stranahan's Original", "Stranahan's", '', ''), ("Stranahan's Diamond Peak", "Stranahan's", '', ''), ("Stranahan's Sherry Cask", "Stranahan's", '2017', ''),
          ("Stranahan's Blue Peak", "Stranahan's", '', ''), ("Stranahan's Snowflake", "Stranahan's", '', 'distillery exclusive')])],
}


def B(n, c, f, seg, d, s, lines=(), sig=(), rel=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': s}

brands = [
 B(BTD, 'United States', '', 'Kentucky distillery', 'Frankfort, Kentucky distillery owned by Sazerac Company since 1992.', BT,
   ['Buffalo Trace', 'Antique Collection', 'W. L. Weller', 'Eagle Rare', 'Col. E. H. Taylor'], ['Buffalo Trace', "Blanton's", 'W. L. Weller', 'George T. Stagg'], ['Sazerac Company', 'Van Winkle']),
 B('Van Winkle', 'United States', '', 'Allocated bourbon', 'Family brand (Old Rip Van Winkle Distillery) made at Buffalo Trace since 2002.', PVW,
   ["Pappy Van Winkle's Family Reserve", 'Old Rip Van Winkle', 'Van Winkle Special Reserve'], ['Pappy Van Winkle'], [BTD]),
 B("Maker's Mark", 'United States', '1953', 'Premium bourbon', 'Loretto, Kentucky distiller of wheated bourbon; Suntory Global Spirits.', MM, [], ["Maker's Mark"]),
 B('Wild Turkey', 'United States', '1942', 'Bourbon & rye', 'Lawrenceburg, Kentucky distillery owned by Campari Group since 2009.', WT, ["Russell's Reserve"], ['Wild Turkey 101']),
 B('Jim Beam', 'United States', 'c. 1795', 'Bourbon distiller', 'Clermont, Kentucky distiller owned by Suntory Global Spirits.', JB,
   ['Small Batch Bourbon Collection'], ["Booker's", 'Knob Creek', "Basil Hayden's"], ['A. Overholt & Co.']),
 B('Brown-Forman', 'United States', '1870', 'Spirits group', 'Louisville spirits company behind Old Forester, Woodford Reserve and Jack Daniel\'s.', 'knowledge',
   ['Old Forester', 'Woodford Reserve', "Jack Daniel's"], ['Old Forester', "Jack Daniel's Old No. 7"]),
 B('Four Roses', 'United States', '1888', 'Bourbon distiller', 'Lawrenceburg, Kentucky distillery owned by Kirin since 2002.', FR, [], ['Four Roses']),
 B('Heaven Hill', 'United States', '1935', 'Family-owned distiller', 'Bardstown, Kentucky family distiller with Bernheim distillery in Louisville.', HH,
   ['Evan Williams', 'Elijah Craig', 'Larceny', 'Rittenhouse', 'Mellow Corn'], ['Evan Williams', 'Elijah Craig', 'Bernheim Original']),
 B('Sazerac Company', 'United States', '1869', 'Spirits group', 'Privately held spirits company owning Buffalo Trace and Barton 1792.', SZ,
   ['1792', 'Very Old Barton', 'Sazerac Rye'], ['Sazerac Rye'], [BTD]),
 B('Diageo', 'United Kingdom', '1997', 'Spirits group', 'Multinational drinks group owning Bulleit and George Dickel.', 'knowledge', ['Bulleit', 'George Dickel']),
 B('MGP Ingredients', 'United States', '', 'Distiller & brand owner', 'Owner of Rebel (Rebel Yell) after acquiring Luxco in 2021.', RY, [], ['Rebel Yell']),
 B('A. Overholt & Co.', 'United States', '1810', 'Rye whiskey', 'Old Overholt brand owner, a Suntory Global Spirits subsidiary.', OO, [], ['Old Overholt'], ['Jim Beam']),
 B('WhistlePig', 'United States', '2007', 'Craft rye', 'Shoreham, Vermont rye whiskey producer founded by Raj Bhakta.', WP, [], ['WhistlePig']),
 B("Michter's", 'United States', '', 'Bourbon & rye', 'Pennsylvania-origin whiskey name made in Kentucky since 2004 (Chatham Imports).', MI, [], ["Michter's"]),
 B('Westland Distillery', 'United States', '2011', 'American single malt', 'Seattle single malt distillery owned by Rémy Cointreau.', WL, [], ['Westland']),
 B("Stranahan's", 'United States', '2004', 'American single malt', 'Denver single malt whiskey producer owned by Proximo Spirits since 2010.', ST, [], ["Stranahan's"]),
]
out = {'kinds': [bourbon, tenn, rye, wheat, corn, asm], 'brands': brands, 'traditions': [],
       'notes': ('Bourbon: 59 old SKUs folded into 24 archetypes plus 26 leftover models; dropped Ten High (a blended whiskey per Sazerac page), '
                 'Lasso Motel DARTS Cigarette Blend (novelty SKU), duplicate Willett/O.K.I./Rabbit Hole/Redemption/Starlight SKUs and second Weller entry. '
                 "Jack Daniel's Tennessee Honey left out (a liqueur). Non-US ryes (Greenbanks, Siderit) kept in Rye m pending a world-whisky home. "
                 'No Balcones/High West archetypes (pages 404 or not fetched). Kind sources switched from retailer pages to Wikipedia/TTB. No traditions needed.')}
p = 'work/J7/shelves/05_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
