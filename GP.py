a = int(input("enter first term of GP: "))
r = int(input("enter common ratio: "))
n = int(input("enter number of terms: "))

for i in range(1, n+1):
    print(a*r**(i-1), end = ",")

print(a*r**(n-1))
