d = {}
a = 0
while a < 5:
    print("1.Add to dictionary, 2.Display elements, 3.	Remove Dictionary, 4. Update Price, 5. Exit: ")
    a = int(input("enter number: "))
    if a == 1:
        b = input("Enter Item Code: ")
        c = input("Enter Item Price: ")
        d[b] = (c)
    elif a == 2:
        print(d)
    elif a == 3:
        del (b)
    elif a == 4:
        c = input("Enter Item Price: ")
        d.update({b:c})
print("bye")
