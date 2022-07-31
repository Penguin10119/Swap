a = int(input("Please Enter any Number: "))
b = 0
while a > 0:
    c = a % 10
    b = (b * 10) + c
    a = a // 10

print("Reverse of entered number is =", b)
