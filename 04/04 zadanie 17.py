def define():
    n=input("Podaj tekst: ")
    k=0
    for i in n:
        if i=="e":
            k+=1
    return k
        
print(define())