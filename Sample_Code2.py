ch = "y"
while ch == "y":
    n= input ("enter name")
    q = int (input ("enter qty"))
    u = int (input("enter unit"))
    a = q*u
    print ("select the category")
    print ("1. electronics")
    print ("2. groceries")
    c = int(input("please select the category"))
    if c == 1:
        a = q*u - (a*0.02)
    elif c==2:
        a = q*u - (a*0.05)
        
    else:
        print("no discount")
    print ("amount payble", str(a))
    ch = input("press 'y' to continue and 'n' to stop")
             
else:
    print ("loop terminated")
