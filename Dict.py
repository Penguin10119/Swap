d = {}
a = 0
while a < 6:
    print("1.Add to dictionary, 2.Display elements, 3.	Remove Dictionary, 4. Redeem, 5: Add Points: ")
    a = int(input("enter option: "))
    if a == 1:
        Customer_ID = input("Enter Customer_ID: ")
        Points = int(input("Enter Points: "))
        if Points < 0:
            break
        d[Customer_ID] = (Points)
    elif a == 2:
        l = list(d.items())
        q = input("Do you want to print as a list? ")
        if q == 'yes':
             print(l)
        else:
            print(d)
    elif a == 3:
        del d[Customer_ID]
    elif a == 4:
        Redeem_Points = int(input("Enter number of points to redeem: "))
        Points = Points - Redeem_Points
        if Points < 0:
            print("Insufficient points")
            break
        d.update({Customer_ID:Points})
    elif a == 5:
        Add_Points = int(input("Add number of points: "))
        Points = Points + Add_Points
        d.update({Customer_ID:Points})
print("bye")
