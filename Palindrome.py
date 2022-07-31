a = float(input("Enter a number: "))

temp = a

rev = 0

while a > 0:

    pal = a % 10
    rev = rev * 10 + pal
    a = a // 10


if temp == rev:
    print("Then number is a palindrome")
else:
    print("The Number is a palindrome")
