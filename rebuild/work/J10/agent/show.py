import sys
t=open(f'/home/user/Possession-Taxonomy/rebuild/work/J10/prompts/{sys.argv[1]}.txt').read()
i=t.index('YOUR SHELF'); j=t.index('OUTPUT:')
print(t[i:j])
