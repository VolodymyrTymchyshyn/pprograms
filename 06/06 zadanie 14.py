d=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"] 
k0=len(d[0])
k1=len(d[1])
k2=len(d[2])
k3=len(d[3])
k4=len(d[4])
c=max(k0,k1,k2,k3,k4)
for ck in d:
    if len(ck)==c:
        print(ck)
