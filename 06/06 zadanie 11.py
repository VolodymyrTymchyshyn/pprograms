def compare(array1,array2):
    if len(array1)==len(array2):
        k=0
        c=0
        for i in array1:
            k=i
        for x in array2:
            c=x
        if k==c:
            return True
    else:
        return False
print(compare(["water"],["water"]))

            
    