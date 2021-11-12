for i in range(1,31):
    if i%3==0 and i%5==0:
        print("Bingo", end=" ")
    elif i%5==0:
        print("Five", end=" ")
    elif i%3==0:
        print("Three", end=" ")
    else:
        print(i, end=" ")