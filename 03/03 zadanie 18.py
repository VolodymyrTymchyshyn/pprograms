
def coin(n):
    x1=0
    x2=0
    x5=0
    x5=n//5
    x5reszta=n%5
    x2=x5reszta//2
    x2reszta=x5reszta%2
    x1=x2reszta
    return x5,x2,x1
print(coin(15))
    