def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Please select one of the following operations")
print("1. Add: ")
print("2. Subtract: ")
print("3. Multiplication: ")
print("4. Division: ")

while True:
    a = input("Enter operation (1/2/3/4): ")

    if a in ('1', '2', '3', '4'):
        b = float(input("Enter the first number: "))
        c = float(input("Enter the second number: "))

        if a == '1':
            print(b, "+", c, "=", add(b, c))

        elif a == '2':
            print(b, "-", c, "=", subtract(b, c))

        elif a == '3':
            print(b, "x", c, "=", multiply(b, c))

        elif a == '4':
            print(b, "÷", c, "=", divide(b, c))

        e = input("Do you want to continue using the calculator? (yes/no): ")

        if e == 'no':
            print("Thanks for using our service, Have a Nice Day!")
            break


    else:
        print("Enter a valid choice")
