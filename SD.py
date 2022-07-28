f = 1
s = 1
x = int(input("Enter a number: "))
n = int(input("Enter range: "))
for i in range(1, n):
    f = f*1
    z = (x**i)/f
    s = s+z
    print(s)
