def star(n):        
    l=[12, 6, 4, 9, 3]
    p=' '
    for i in l:
        p=i*"*"
        print(f"{i}: {p}")
        if n==i:
            return p
print(star(9))
