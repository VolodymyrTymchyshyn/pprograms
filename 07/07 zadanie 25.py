def minmax(array):
    array.sort()
    kmin=array[0]
    kmax=array[-1]
    l=[kmin,kmax]
    return l
print(minmax([4,2,8,4,7,9,5]))
    