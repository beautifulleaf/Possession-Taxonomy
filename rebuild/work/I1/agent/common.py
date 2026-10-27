import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/I1/agent')
from put import put
WP='https://en.wikipedia.org/wiki/'
M=lambda *a:[list(x) for x in a]
def V(n,mk='',y='',d=''):
    v={'n':n}
    if mk: v['mk']=mk
    if y: v['y']=y
    if d: v['d']=d
    return v
def A(n,d,s,v,mk='',y='',a='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v}
    if dt: x['dt']=dt
    return x
def B(n,c,f,seg,kf,d,**k):
    return dict({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':d,'s':'knowledge'},**k)
BR={
 'Microsoft':B('Microsoft','United States','1975','Mainstream','Windows, Office','American software company behind Windows and Office.'),
 'Apple':B('Apple','United States','1976','Premium','Mac, iPhone','American hardware and software company.'),
 'Google':B('Google','United States','1998','Mainstream','search, Android','American company behind Search, Android and Workspace.'),
 'Adobe':B('Adobe','United States','1982','Professional & flagship','creative software, PDF','American maker of Acrobat and the Creative Cloud apps.'),
}
