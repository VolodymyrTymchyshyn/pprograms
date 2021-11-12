def un(n):
    #print(1,2,3,end=' ')
    x = '1 2 3 '
    for i in range(1,n):
        if i%i==0:
            if i>3 and i%2!=0 and i%3!=0:
                x += f"{i} "
                #print(i, end=' ')
                
    return x
            
            

print(un(20))


