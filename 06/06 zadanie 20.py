def occurs(number, array):
    print (f"Number:{number}",end=" ")
    print (f"\nArray:",end=" ")
    for i in array:
        print (i,end=" ")
    if number in array:
        print(f"\nResult: number {number} appears in the array")
        return True
occurs(3,[23,4,2,1,3])