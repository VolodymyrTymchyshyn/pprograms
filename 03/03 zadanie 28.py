def fib(n):
    a=0
    b=1 #pierwszy i drugi wyraz 0 i 1
    for i in range(n-1): #petla ktora oblicza n-ty wyraz ciagu
        a,b=b,a+b
    return a # zwracana wartosc n-ty wyrazu
print(fib(5))
