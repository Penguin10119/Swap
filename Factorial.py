a = int(input("enter a number for factorial: "))
if a < 0:
    print("enter a valid number")
        
else:
    f = 1
    for i in range(a):
        f = f * (i+1)
        
    print("factorial of", a ,"is", f)
