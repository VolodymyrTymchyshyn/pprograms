def month():
    l=["Styczen","February","March","April","May","June","July","August","September","October","November","December"]
    n=int(input("Podaj liczbe: "))
    for i in l:
        i=n
        return l[i-1]
        
    
print(month())
    