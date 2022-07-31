a = float(input("Enter a number: "))

b = 0

c = a

while c > 0:
    num = c % 10

    b += num ** 3

    c //= 10


if a == b:
    print(a, "is an armstrong number")

else:
    print(a, "is not an armstrong number")

