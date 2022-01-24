x=[4,2,8,4,7,9,5]
l=[]
for i in x:
    if i%2==0:
        k=i
        l.append(k)
for j in x:
    if j%2!=0:
        p=j
        l.append(j)
print(l)


