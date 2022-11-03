d = {}
a = 0
while a < 3:
    print("1.Add to dictionary, 2.Display elements, 3.	Exit: ")
    a = int(input("enter option: "))
    if a == 1:
        num = int(input("enter a number: "))
        d[num] = (num**2, num**3)
    elif a == 2:
        print(d)
print("bye")
