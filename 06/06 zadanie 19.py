print(f"Unique elements: ",end= " ")
print(f"\nUnique elements: ",end= " ")
l1=[2, 3, 2, 5, 8, 1, 9, 8]
l2=[]
x = 0
for i in l1:
    print(i,end=' ')
    x = l1.count(i)
    if x==1:
        l2.append(i)

for j in l2:
    print(j,end=" ")

