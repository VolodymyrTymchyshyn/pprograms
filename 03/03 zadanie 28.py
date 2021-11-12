x = 0
y = 1

l = "0 1"

for i in range(10):
    l +=str( int(l[-1])+int(l[-3]))
    l += ' '
print(l)