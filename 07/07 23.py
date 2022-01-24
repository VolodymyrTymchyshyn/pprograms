def tabl(a):
    k=len(a)
    if k%2!=0:
        c=int(k/2+1)
    else:
        c=int(k/2)
    ret=a[c-1]
    return(ret)
print(tabl([6,8,3,1,0,5,7]))
