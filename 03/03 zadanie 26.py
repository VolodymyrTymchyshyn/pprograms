x=input("Enter the pin")
y="0805"
if x==y:
    print("Correct")
elif x!=y:
    print("Incorrect...")
    x=input("Enter the pin")
    if x==y:
        print("Correct")
    if x!=y:
        print("Incorrect...")
        x=input("Enter the pin")
        if x==y:
            print("Correct")
            if x!=y:
                print("Incorrect...")
                print("Your card was blocked")
            elif x==y:
                print("Correct")