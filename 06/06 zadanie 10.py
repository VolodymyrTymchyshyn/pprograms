def suma(array):
    s=0
    for i in array:
        s+=i
    return s

print(suma([2,5,7,8]))
def array2str(array):
    p=" "
    for i in array:
        p+=str(f"{i}, ")
    return p
print(array2str([2,5,7,8]))