l=[15, 8, 31, 47, 2, 19]

maxx=l[0]
minn=l[0]

for i in l:
    if i<minn:
        minn=i
    elif i>maxx:
        maxx=i
        
print(minn,maxx)