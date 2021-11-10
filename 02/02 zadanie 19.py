import math
a=int(input("Podaj piersza strone: "))
b=int(input("Podaj druga strone: "))
c=int(input("Podaj trzecia strone: "))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Powierzchnia tego trójkąta jest równa: {S}")