def multiply(x, y):
    return 0.5 * x * y


def multiply2(x, y):
    return x * y


def multiply3(x):
    return 3.14 * x * x


print("Please select one if the following operations: ")
print("1: Area of Triangle")
print("2: Area of Rectangle")
print("3: Area of Circle")

while True:
    a = input("Choose (1/2/3): ")

    if a in ('1', '2', '3'):

        if a == '1':
            b = float(input("Enter Base of Triangle: "))
            c = float(input("Enter Height of Triangle: "))
            print("Area of Triangle is: ", multiply(b, c))

        elif a == '2':
            b = float(input("Enter Length of Rectangle: "))
            c = float(input("Enter Breadth of Rectangle: "))
            print("Area of Rectangle is:", multiply2(b, c))

        elif a == '3':
            b = float(input("Enter a Radius of Circle: "))
            print("Area OF Circle is:", multiply3(b))

        else:
            print("Enter a valid choice")

        F = input("Do you want to continue operation? (yes/no): ")
        if F == 'no':
            print("Thanks for using our service, Have a Nice Day!")
            break

    else:
        print("Error, enter a valid choice")
