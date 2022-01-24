file=open("index.txt")
s=0
for line in file:
    s+=int(line)
print(s)
file.close()