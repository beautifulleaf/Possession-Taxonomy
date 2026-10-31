import json, os
W = 'https://en.wikipedia.org/wiki/'
CH = W + 'Champagne_(wine)'
DP = W + 'Dom_P%C3%A9rignon_(wine)'
CR = W + 'Cristal_(wine)'
MOET = W + 'Mo%C3%ABt_%26_Chandon'
VC = W + 'Veuve_Clicquot'
KR = W + 'Krug_(Champagne)'
BOL = W + 'Bollinger'
TAI = W + 'Taittinger'
POL = W + 'Pol_Roger'
LR = W + 'Louis_Roederer'
RU = W + 'Ruinart_(Champagne)'
PJ = W + 'Perrier-Jou%C3%ABt'
LP = W + 'Laurent-Perrier'
SAL = W + 'Champagne_Salon'
CHH = W + 'Charles_Heidsieck'
PH = W + 'Piper-Heidsieck'
BS = W + 'Billecart-Salmon'
ADB = W + 'Armand_de_Brignac'
POM = W + 'Pommery'
PHI = W + 'Philipponnat'
SEL = W + 'Jacques_Selosse'
LAN = W + 'Lanson'
MUMM = W + 'G._H._Mumm'
GOS = W + 'Gosset'
DL = W + 'Duval-Leroy'

def X(n, mk, y, s, d, a='', v=None, dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s}
    if v: o['v'] = [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]
    if dt: o['dt'] = dt
    return o

DOSAGE = ['Brut Zero / no added sugar (<3 g/l)', 'Extra Brut (<6 g/l)', 'Brut (<12 g/l)', 'Extra Dry (12–17 g/l)', 'Sec (17–32 g/l)', 'Demi-sec (32–50 g/l)', 'Doux (50 g/l +)']
STYLE = ['Blanc de blancs (Chardonnay only)', 'Blanc de noirs (Pinot noir and/or Meunier)']
PROD = ['House / négociant-manipulant (NM)', 'Grower Champagne / récoltant-manipulant (RM)', 'Cooperative (CM)', "Buyer's own brand (MA)"]
SIZES = 'bottle 75 cl · magnum 1.5 l · jeroboam 3 l · methuselah 6 l · salmanazar 9 l · balthazar 12 l'

nv = {'n': 'Non-vintage Champagne', 'a': 'NV · brut sans année · house brut',
      'd': "Champagne blended from several harvests with reserve wines to keep a consistent house style.",
      't': DOSAGE + STYLE + PROD, 's': 'https://www.wine.com/list/wine/7155',
      'x': [
        X('Moët & Chandon Brut Impérial', 'Moët & Chandon', '1860s', MOET, "The house's non-vintage brut and the best-selling Champagne brand.", 'Moët Impérial',
          v=[('Brut Impérial', 'Moët & Chandon', '1860s', 'original non-vintage brut'), ('Brut Impérial "Be Fabulous"', 'Moët & Chandon', '2006', 'very limited Swarovski-crystal bottle'), ('Ice Impérial', 'Moët & Chandon', '', '')],
          dt='dosage · bottle size (' + SIZES + ')'),
        X('Veuve Clicquot Yellow Label', 'Veuve Clicquot', '1876', VC, "Veuve Clicquot's non-vintage brut, known by the yellow label used since 1876 and trademarked in 1877.", 'Yellow Label Brut',
          v=[('Brut Yellow Label', 'Veuve Clicquot', '1897', 'Brut given the yellow label'), ('Rich', 'Veuve Clicquot', '2015', 'released June 2015'), ('Extra Brut Extra Old', 'Veuve Clicquot', '2017', "the house's first ultra-dry non-vintage")],
          dt='dosage · bottle size'),
        X('Bollinger Special Cuvée', 'Bollinger', '', BOL, "Bollinger's non-vintage brut from Aÿ.",
          v=[('Special Cuvée', 'Bollinger', '', 'non-vintage brut'), ('Special Cuvée 007 Limited Edition', 'Bollinger', '2021', 'for the film No Time To Die')]),
        X('Louis Roederer Brut Premier', 'Louis Roederer', '', LR, "Louis Roederer's non-vintage brut."),
        X('G. H. Mumm Cordon Rouge', 'G. H. Mumm', 'after 1852', MUMM, "Mumm's non-vintage brut, identified by the red sash of the Légion d'honneur on the label.", 'Mumm Cordon Rouge'),
        X('Laurent-Perrier Brut L.P.', 'Laurent-Perrier', '', LP, "Laurent-Perrier's non-vintage brut.", 'La Cuvée',
          v=[('La Cuvée Brut', 'Laurent-Perrier', '', 'current name of the non-vintage brut'), ('Heritage', 'Laurent-Perrier', '', 'non-vintage cuvée')]),
        X('Pol Roger Brut Réserve', 'Pol Roger', '', POL, "Pol Roger's non-vintage brut.",
          v=[('Pure Brut', 'Pol Roger', '', 'non-vintage with no added sugar')]),
        X('Ruinart Blanc de Blancs', 'Ruinart', '', RU, "Ruinart's flagship non-vintage, made entirely from Chardonnay.",
          v=[('R de Ruinart', 'Ruinart', '', 'non-vintage brut, at least 40% Chardonnay and 60% Pinot noir with 25% reserve wines')]),
        X('Lanson Le Black Label Brut', 'Lanson', '', LAN, "Lanson's non-vintage brut.", 'Black Label',
          v=[('Le Black Réserve', 'Lanson', '', 'non-vintage brut'), ('Green Label Organic', 'Lanson', '', 'organic non-vintage')]),
        X('Billecart-Salmon Brut Réserve', 'Billecart-Salmon', '', BS, "Billecart-Salmon's non-vintage brut, aged 36 months in the cellar before release."),
        X('Gosset Grande Réserve Brut', 'Gosset', '', GOS, "Gosset's non-vintage brut."),
        X('Piper-Heidsieck Cuvée Brut', 'Piper-Heidsieck', '', PH, "Piper-Heidsieck's non-vintage brut.",
          v=[('Essentiel Extra Brut', 'Piper-Heidsieck', '', ''), ('Essentiel Blanc de Blancs', 'Piper-Heidsieck', '', ''), ('Essentiel Blanc de Noirs', 'Piper-Heidsieck', '', ''), ('Cuvée Sublime', 'Piper-Heidsieck', '', 'sweeter style')]),
        X('Duval-Leroy Fleur de Champagne', 'Duval-Leroy', '1911', DL, "Duval-Leroy's flagship brut, launched soon after the 1911 crus ranking."),
        X('Jacques Selosse Substance', 'Jacques Selosse', '', SEL, "Grower Champagne from Avize made by a solera system of blended vintages.",
          v=[('Contraste', 'Jacques Selosse', '', 'also made by solera')]),
      ],
      'm': [["Mumm de Cramant", "G. H. Mumm"], ["Drappier Brut Nature", "Drappier"], ["Tsarine", "Chanoine Frères"],
            ["Cuvée des Moines", "Burtin - Besserat de Bellefon"], ["Cattier Blanc de Blancs Brut Premier Cru", "Cattier"],
            ["Canard-Duchene Blanc de Blancs Iconic", "Canard-Duchêne"], ["Jacquart Blanc de Blancs Brut", "Jacquart"],
            ["Philippe Gonet Ter Blanc de Blancs Extra Brut", "Philippe Gonet"], ["Grand Cru Blanc de Blancs", "Boll & Cie"],
            ["Barons de Rothschild Rare Collection Blanc de Blancs Extra Brut", "Barons de Rothschild Champagne"],
            ["Brimoncourt Régence Brut", "Brimoncourt"], ["Champagne Castelnau Brut", "Champagne Castelnau"],
            ["Charles Collin Cuvee Charles Blanc de Blancs Brut", "Charles Collin"],
            ["Prestige des Sacres Cuvée Dynastie Blanc de Blancs Brut", "Prestige des Sacres"],
            ["Saint Réol Brut Grand Cru Ambonnay", "Saint Réol"], ["Médaillon Rouge", "Binet"],
            ["Marks & Spencer Delacourt Blanc de Blancs Brut", "issued by Marks & Spencer"]]}

vin = {'n': 'Vintage Champagne', 'a': 'millésime · millésimé',
       'd': "Champagne made only from one declared harvest and aged at least three years before release.",
       't': DOSAGE + STYLE + PROD, 's': CH,
       'x': [
         X('Veuve Clicquot Vintage', 'Veuve Clicquot', '1810', VC, "Veuve Clicquot's vintage brut; the house's 1810 is the first known vintage Champagne."),
         X('Moët & Chandon Vintage', 'Moët & Chandon', '1842', MOET, "Moët & Chandon's vintage cuvée, first marketed in 1842.", 'Grand Vintage'),
         X('Bollinger La Grande Année', 'Bollinger', '', BOL, "Bollinger's vintage cuvée, made only in declared years."),
         X('Louis Roederer Brut Vintage', 'Louis Roederer', '', LR, "Louis Roederer's vintage brut.",
           v=[('Blanc de Blancs Vintage', 'Louis Roederer', '', 'Chardonnay-only vintage')]),
         X('Pol Roger Blanc de Blancs', 'Pol Roger', '', POL, "Pol Roger's Chardonnay-only vintage cuvée."),
         X('Piper-Heidsieck Vintage', 'Piper-Heidsieck', '', PH, "Piper-Heidsieck's vintage brut.",
           v=[('Vintage 2012', 'Piper-Heidsieck', '2012', ''), ('Vintage 2014', 'Piper-Heidsieck', '2014', ''), ('Vintage 2018', 'Piper-Heidsieck', '2018', ''),
              ('Hors-Série 1971', 'Piper-Heidsieck', '1971', 'late-release old vintage'), ('Hors-Série 1982', 'Piper-Heidsieck', '1982', 'late-release old vintage')]),
         X('Lanson Le Vintage', 'Lanson', '', LAN, "Lanson's vintage brut.", v=[('Le Vintage 2009', 'Lanson', '2009', '')]),
         X('Gosset Grand Millésime Brut', 'Gosset', '', GOS, "Gosset's vintage brut.", v=[('Grand Millésime 2012', 'Gosset', '2012', '')]),
         X('Duval-Leroy Vintage', 'Duval-Leroy', '', DL, "Duval-Leroy's vintage brut.", v=[('Vintage 2004', 'Duval-Leroy', '2004', '')]),
       ],
       'm': [["Avize Grand Cru", "Jacquesson"], ["Vendange", "Mercier"]]}

pre = {'n': 'Prestige cuvée Champagne', 'a': 'tête de cuvée · cuvée de prestige',
       'd': "A house's top-of-the-range Champagne, usually vintage, from its best grapes and long ageing.",
       't': STYLE + ['Single vineyard (clos)', 'Late release / recently disgorged'], 's': CH,
       'x': [
         X('Dom Pérignon', 'Moët & Chandon', '1921', DP, "Moët & Chandon's vintage-only prestige cuvée, first vintage 1921, first sold in 1936.",
           v=[('Dom Pérignon 1921', 'Moët & Chandon', '1921', 'first vintage, released 1936'), ('Dom Pérignon 1947', 'Moët & Chandon', '1947', 'first vintage made separately from the start'),
              ('Plénitude 2 (P2)', 'Moët & Chandon', '', 'second release after longer lees ageing; formerly Œnothèque'),
              ('Plénitude 3 (P3)', 'Moët & Chandon', '', 'third release, very small quantities'),
              ('Œnothèque', 'Moët & Chandon', '', 'former name of late releases, replaced around 2016'),
              ('Dom Pérignon 2008 Legacy Edition', 'Moët & Chandon', '2008', 'chef de cave edition'),
              ('Dom Pérignon 2017', 'Moët & Chandon', '2017', 'latest listed vintage')],
           dt='vintage (48 released) · plénitude · artist editions (e.g. Warhol 2000, Koons 2004, Basquiat 2015) · bottle size'),
         X('Cristal', 'Louis Roederer', '1876', CR, "Louis Roederer's prestige cuvée in a clear flat-bottomed bottle, created for Tsar Alexander II in 1876.",
           v=[('Cristal (commercial release)', 'Louis Roederer', '1945', 'first commercially available'),
              ('Cristal 2000', 'Louis Roederer', '2000', '55% Pinot noir, 45% Chardonnay'),
              ('Cristal 2015', 'Louis Roederer', '2015', '60% Pinot noir, 40% Chardonnay; biodynamic fruit since 2012')],
           dt='vintage · clear lead-glass bottle · gift box'),
         X('Krug Grande Cuvée', 'Krug', '', KR, "Krug's non-vintage flagship, re-created each year from many vintages."),
         X('Krug Vintage', 'Krug', '', KR, "Krug's vintage cuvée.",
           v=[('Krug 2000', 'Krug', '2000', ''), ('Krug 2003', 'Krug', '2003', ''), ('Krug 2004', 'Krug', '2004', ''),
              ('Krug Collection 1989', 'Krug', '1989', 'late-release library vintage')]),
         X('Krug Clos du Mesnil', 'Krug', '1979', KR, "Krug's single-vineyard (clos) cuvée, first vintage 1979, presented 1986.",
           v=[('Clos du Mesnil 1979', 'Krug', '1979', 'first vintage'), ('Clos du Mesnil 2000', 'Krug', '2000', ''), ('Clos du Mesnil 2003', 'Krug', '2003', '')]),
         X("Krug Clos d'Ambonnay", 'Krug', '1995', KR, "Krug's second single-vineyard (clos) cuvée, first vintage 1995, released 2007.",
           v=[("Clos d'Ambonnay 1995", 'Krug', '1995', 'first vintage'), ("Clos d'Ambonnay 1998", 'Krug', '1998', ''), ("Clos d'Ambonnay 2000", 'Krug', '2000', '')]),
         X('Salon Le Mesnil', 'Salon', '1921', SAL, "Single-village blanc de blancs from Le Mesnil-sur-Oger, made only in exceptional years; first commercial vintage 1921.", 'Salon',
           v=[('Salon 1905', 'Salon', '1905', 'first vintage'), ('Salon 1921', 'Salon', '1921', 'first commercial vintage'),
              ('Salon 2008', 'Salon', '2008', 'magnum only'), ('Salon 2015', 'Salon', '2015', 'latest listed vintage')],
           dt='vintage (about 41 released) · bottle or magnum'),
         X('Taittinger Comtes de Champagne', 'Taittinger', '', TAI, "Taittinger's flagship vintage blanc de blancs, 100% Chardonnay."),
         X('Veuve Clicquot La Grande Dame', 'Veuve Clicquot', '1972', VC, "Veuve Clicquot's prestige cuvée, launched in 1972.", 'La Grande Dame'),
         X('Perrier-Jouët Belle Époque', 'Perrier-Jouët', '', PJ, "Perrier-Jouët's prestige cuvée in the bottle painted with Émile Gallé's white anemones.", 'Fleur de Champagne',
           v=[('Gallé anemone magnums', 'Perrier-Jouët', '1902', 'four magnums whose design became the cuvée emblem')]),
         X('Laurent-Perrier Grand Siècle', 'Laurent-Perrier', '', CH, "Laurent-Perrier's prestige cuvée."),
         X('Pol Roger Cuvée Sir Winston Churchill', 'Pol Roger', '1975', POL, "Pol Roger's prestige cuvée named after Churchill; introduced 1984 with the 1975 vintage.", 'Sir Winston Churchill',
           v=[('Sir Winston Churchill 1975', 'Pol Roger', '1975', 'first vintage, magnum only')]),
         X('Dom Ruinart Blanc de Blancs', 'Ruinart', '1959', RU, "Ruinart's all-Chardonnay prestige vintage, first released with the 1959 vintage.", 'Dom Ruinart'),
         X('Bollinger R.D.', 'Bollinger', '', BOL, "Bollinger vintage released after extra lees ageing and recently disgorged (récemment dégorgé).", 'R.D.'),
         X('Bollinger Vieilles Vignes Françaises', 'Bollinger', '1969', BOL, "Bollinger's rarest vintage cuvée, first vintage 1969.", 'VVF'),
         X('Pommery Cuvée Louise', 'Pommery', '', POM, "Pommery's top cuvée.", 'Cuvée Louise'),
         X('Gosset Celebris Extra Brut', 'Gosset', '1988', GOS, "Gosset's prestige extra brut vintage.", 'Celebris',
           v=[('Celebris 1988', 'Gosset', '1988', 'earliest listed vintage'), ('Celebris 1990', 'Gosset', '1990', ''), ('Celebris 1995', 'Gosset', '1995', ''),
              ('Celebris 1998', 'Gosset', '1998', ''), ('Celebris 2002', 'Gosset', '2002', ''), ('Celebris 2007', 'Gosset', '2007', '')]),
         X('Duval-Leroy Femme de Champagne', 'Duval-Leroy', '1990', DL, "Duval-Leroy's prestige vintage, first produced 1990.", 'Cuvée Femme',
           v=[('Femme de Champagne 1995', 'Duval-Leroy', '1995', ''), ('Femme de Champagne 1996', 'Duval-Leroy', '1996', ''), ('Femme de Champagne 2000', 'Duval-Leroy', '2000', '')]),
         X('Philipponnat Clos des Goisses', 'Philipponnat', '', PHI, "Philipponnat's prestige cuvée, among the first single-vineyard Champagnes.", 'Clos des Goisses'),
         X('Billecart-Salmon Cuvée Nicolas-François Billecart', 'Billecart-Salmon', '', BS, "Billecart-Salmon's prestige vintage; the 1959 won 'Champagne of the Millennium' in 1999.",
           v=[('Cuvée Nicolas-François Billecart 1959', 'Billecart-Salmon', '1959', "first place, Champagne of the Millennium 1999")]),
         X('Armand de Brignac Brut Gold', 'Armand de Brignac', '2006', ADB, "Gold-bottled 'Ace of Spades' cuvée produced by Cattier, first bottles 2006.", 'Ace of Spades',
           v=[('Blanc de Blancs', 'Armand de Brignac', '2008', ''), ('Demi-Sec', 'Armand de Brignac', '2015', ''), ('Blanc de Noirs', 'Armand de Brignac', '2015', '')]),
       ],
       'm': [["Blanc des Millénaires", "Charles Heidsieck"], ["Amour de Deutz", "Deutz"], ["Diamant Bleu", "Heidsieck & Co Monopole"],
             ["Noble Cuvée", "Lanson"], ["Palmes d'Or", "Nicolas Feuillatte"], ["Rare Millésime Brut", "Rare Champagne"],
             ["Cuvée des Enchanteleurs", "Henriot"], ["Henriot L'Inattendue Chardonnay Grand Cru", "Henriot"],
             ["Grande Sendrée", "Drappier"], ["Nec Plus Ultra", "Bruno Paillard"], ["Clos St Hilaire", "Billecart-Salmon"],
             ["Clos du Moulin", "Cattier"], ["Cuvée Paradis", "Alfred Gratien"], ["Grande Cuvée", "Ayala"], ["Sourire de Reims", "Abelé"],
             ["Joyau de France", "Boizel"], ["Grande Cuvée Charles VII", "Canard-Duchêne"], ["Commodore", "De Castellane"],
             ["Stradivarius", "De Cazanove"], ["Grand Vin des Princes", "De Venoge"],
             ["De Saint-Gall Orpale Blanc de Blancs Brut Grand Cru", "De Saint-Gall"], ["Covama", "Pannier"], ["Cuvée Lady C.", "Paul Goerg"],
             ["Cuvée Garance", "Thiénot"], ["Cuvée Stanislas", "Thiénot"], ["Coeur de Cuvée", "Vilmart"]]}

ros = {'n': 'Rosé Champagne', 'a': 'pink Champagne · Champagne rosé',
       'd': "Pink Champagne coloured by blending in still red wine or by brief skin contact (saignée).",
       't': ['Rosé d\'assemblage (blended with red wine)', 'Rosé de saignée (skin maceration)', 'Non-vintage', 'Vintage'] + DOSAGE[:3], 's': CH,
       'x': [
         X('Veuve Clicquot Rosé', 'Veuve Clicquot', '1818', VC, "Veuve Clicquot's rosé; the house made the first known blended rosé Champagne in 1818."),
         X('Dom Pérignon Rosé', 'Moët & Chandon', '1959', DP, "The rosé version of Dom Pérignon, first vintage 1959.",
           v=[('Dom Pérignon Rosé 1959', 'Moët & Chandon', '1959', 'first vintage'), ('Dom Pérignon Rosé 1986', 'Moët & Chandon', '1986', 'first rosé vintage with no white made'),
              ('Rosé Œnothèque', 'Moët & Chandon', '', 'late release'), ('Dom Pérignon Rosé 2009', 'Moët & Chandon', '2009', 'latest listed vintage')],
           dt='vintage (28 released) · plénitude'),
         X('Cristal Rosé', 'Louis Roederer', '1974', CR, "Rosé Cristal with more Pinot noir, coloured by saignée; first released with the 1974 vintage."),
         X('Krug Rosé', 'Krug', '1983', KR, "Krug's non-vintage rosé, first presented in 1983."),
         X('Dom Ruinart Rosé', 'Ruinart', '1962', RU, "Prestige rosé: Dom Ruinart blanc de blancs with about 16% red Pinot noir added; first released 1962."),
         X('Ruinart Brut Rosé', 'Ruinart', '', RU, "Ruinart's non-vintage rosé, about 45% Chardonnay and 55% Pinot noir."),
         X('Laurent-Perrier Cuvée Rosé', 'Laurent-Perrier', '', LP, "Laurent-Perrier's non-vintage rosé."),
         X('Taittinger Comtes de Champagne Rosé', 'Taittinger', '', TAI, "Prestige rosé of 70% Pinot noir and 30% Chardonnay."),
         X('Bollinger La Grande Année Rosé', 'Bollinger', '', BOL, "Rosé version of Bollinger's vintage cuvée."),
         X('Pol Roger Rosé Vintage', 'Pol Roger', '', POL, "Pol Roger's vintage rosé."),
         X('Piper-Heidsieck Rosé Sauvage', 'Piper-Heidsieck', '', PH, "Piper-Heidsieck's rosé."),
         X('Gosset Grand Rosé Brut', 'Gosset', '', GOS, "Gosset's non-vintage rosé."),
         X('Lanson Le Rosé', 'Lanson', '', LAN, "Lanson's non-vintage rosé."),
         X('Duval-Leroy Femme de Champagne Rosé', 'Duval-Leroy', '', DL, "Rosé version of Duval-Leroy's prestige cuvée.", v=[('Femme de Champagne Rosé 2006', 'Duval-Leroy', '2006', 'latest listed vintage')]),
         X('Armand de Brignac Rosé', 'Armand de Brignac', '2008', ADB, "Rosé of the Armand de Brignac range, introduced 2008."),
       ],
       'm': [["Rare Champagne Rare Rose", "Rare Champagne"]]}

def B(n, f, seg, d, s, sig, c='France', lines=None, rel=None):
    o = {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 'sig': sig, 's': s}
    if lines: o['lines'] = lines
    if rel: o['rel'] = rel
    return o

H = 'Champagne house (négociant-manipulant)'
brands = [
  B('Moët & Chandon', '1743', H, 'Épernay house founded by Claude Moët; part of LVMH and maker of Dom Pérignon.', MOET, ['Moët & Chandon Brut Impérial', 'Dom Pérignon'], lines=['Brut Impérial', 'Vintage', 'Dom Pérignon'], rel=['Ruinart', 'Krug', 'Veuve Clicquot']),
  B('Veuve Clicquot', '1772', H, 'House built up by Barbe-Nicole Clicquot-Ponsardin after 1805; owned by LVMH.', VC, ['Veuve Clicquot Yellow Label', 'Veuve Clicquot La Grande Dame'], lines=['Yellow Label', 'Vintage', 'Rosé', 'La Grande Dame', 'Rich'], rel=['Moët & Chandon']),
  B('Krug', '1843', H, 'House founded by Joseph Krug; owned by LVMH since 1999.', KR, ['Krug Grande Cuvée', 'Krug Clos du Mesnil'], lines=['Grande Cuvée', 'Rosé', 'Vintage', 'Collection', 'Clos du Mesnil', "Clos d'Ambonnay"], rel=['Moët & Chandon']),
  B('Louis Roederer', '1776', H, 'Family-owned Reims house (Rouzaud family), maker of Cristal.', LR, ['Cristal', 'Louis Roederer Brut Premier'], lines=['Brut Premier', 'Vintage', 'Blanc de Blancs', 'Cristal']),
  B('Bollinger', '1829', H, 'House in Aÿ, family-managed since 1889.', BOL, ['Bollinger Special Cuvée', 'Bollinger R.D.', 'Bollinger Vieilles Vignes Françaises'], lines=['Special Cuvée', 'La Grande Année', 'R.D.', 'Vieilles Vignes Françaises']),
  B('Taittinger', '1734', H, 'Family-run Reims house.', TAI, ['Taittinger Comtes de Champagne']),
  B('Pol Roger', '1849', H, 'House still owned and run by descendants of Pol Roger.', POL, ['Pol Roger Cuvée Sir Winston Churchill'], lines=['Brut Réserve', 'Pure', 'Blanc de Blancs', 'Rosé Vintage', 'Sir Winston Churchill']),
  B('Ruinart', '1729', H, 'Reims house founded by Nicolas Ruinart, the oldest established Champagne house; owned by LVMH.', RU, ['Ruinart Blanc de Blancs', 'Dom Ruinart Blanc de Blancs'], lines=['R de Ruinart', 'Blanc de Blancs', 'Rosé', 'Dom Ruinart'], rel=['Moët & Chandon']),
  B('Perrier-Jouët', '1811', H, 'House founded by Pierre-Nicolas Perrier and Rose Adélaide Jouët; owned by Pernod Ricard.', PJ, ['Perrier-Jouët Belle Époque'], rel=['G. H. Mumm']),
  B('Laurent-Perrier', '1812', H, 'House in Tours-sur-Marne, majority-owned by the de Nonancourt family; also owns Salon and Delamotte.', LP, ['Laurent-Perrier Grand Siècle', 'Laurent-Perrier Cuvée Rosé'], rel=['Salon']),
  B('Salon', '1921', 'Champagne house (single-cuvée)', 'Le Mesnil-sur-Oger house founded by Eugène Aimé Salon, making one vintage blanc de blancs; part of Laurent-Perrier since 1989.', SAL, ['Salon Le Mesnil'], rel=['Laurent-Perrier']),
  B('G. H. Mumm', '1827', H, 'House owned by Pernod Ricard since 2001.', MUMM, ['G. H. Mumm Cordon Rouge'], rel=['Perrier-Jouët']),
  B('Piper-Heidsieck', '1785', H, 'Reims house founded by Florens-Louis Heidsieck; owned by EPI (Descours family) since 2011.', PH, ['Piper-Heidsieck Cuvée Brut'], rel=['Charles Heidsieck']),
  B('Charles Heidsieck', '1851', H, 'House founded in 1851 by Charles Heidsieck, nicknamed "Champagne Charlie" in the US.', CHH, [], rel=['Piper-Heidsieck']),
  B('Billecart-Salmon', '1818', H, 'Family-owned house founded on the marriage of Nicolas François Billecart and Elisabeth Salmon.', BS, ['Billecart-Salmon Cuvée Nicolas-François Billecart']),
  B('Gosset', '1584', H, 'Wine house founded by Pierre Gosset; owned by the Renaud-Cointreau group since 1994.', GOS, ['Gosset Celebris Extra Brut']),
  B('Lanson', '1760', H, 'House founded by François Delamotte; owned by the Lanson-BCC group since 2006.', LAN, ['Lanson Le Black Label Brut']),
  B('Pommery', '1858', H, 'Reims house of the Vranken-Pommery Monopole group; first to sell a brut Champagne, in 1874.', POM, ['Pommery Cuvée Louise']),
  B('Duval-Leroy', '1859', H, 'Family-owned house founded by Edouard Leroy and Jules Duval.', DL, ['Duval-Leroy Femme de Champagne', 'Duval-Leroy Fleur de Champagne']),
  B('Philipponnat', '', H, 'Family house with roots in Champagne dating to 1522.', PHI, ['Philipponnat Clos des Goisses']),
  B('Jacques Selosse', '1950s', 'Grower Champagne (récoltant-manipulant)', 'Avize grower run by Anselme Selosse since 1980; first vintage bottled 1960.', SEL, ['Jacques Selosse Substance']),
  B('Armand de Brignac', '2006', 'Champagne brand', "'Ace of Spades' brand produced by Cattier, owned by Jay-Z and LVMH.", ADB, ['Armand de Brignac Brut Gold']),
]

notes = ("Old k51 (72 models) redistributed by style: icons became archetypes (Dom Pérignon, Cristal, Krug, Comtes de Champagne, La Grande Dame, Belle Époque, Grand Siècle, "
         "Sir Winston Churchill, Dom Ruinart, Cuvée Louise, Celebris, Femme de Champagne, R.D., VVF, Clos du Mesnil, Yellow Label, Brut Impérial, Special Cuvée, LP La Cuvée/Heritage); "
         "the rest kept as flat m in the kind that fits their style. Dropped as duplicates: 'Lanson Noble Brut' (= Noble Cuvée), 'Rare' by Piper-Heidsieck and 'Rare Champagne Brut' "
         "(Rare is now its own label; kept 'Rare Millésime Brut' and 'Rare Rose'), 'Rare Champagne Rare Magnum' (bottle size, not a cuvée), 'Ruinart Rose Brut' and 'Grand Millésime' "
         "(now archetypes). Grand Siècle has no own page fetched; sourced to the Champagne article listing it as a prestige cuvée. Grande Marque status left out (no fetched source). "
         "No brand entries for old-data makers without a fetched page (Abelé, Ayala, Deutz, Henriot, Drappier, Jacquesson, Nicolas Feuillatte etc.). No traditions: Champagne production "
         "is covered by producer and dosage types, not artisan craft.")

out = {'kinds': [nv, vin, pre, ros], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/J7/shelves/02_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('ok', sum(len(k['x']) for k in out['kinds']), 'archetypes', sum(len(k.get('m', [])) for k in out['kinds']), 'm', len(brands), 'brands')
