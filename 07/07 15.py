inputFileName = input("Enter name of input file: ")
f = open(inputFileName, "r")
c=0
for i in f:
    c+=1
print(c)
f.close()