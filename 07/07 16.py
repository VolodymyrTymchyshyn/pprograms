f=open("shoplist.txt", "r")
with open("copyshop.txt", "w") as d:
    for i in f:
        
        d.write(i)