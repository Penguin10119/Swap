a = int(input("enter first term of AP: "))
d = int(input("enter common difference: "))
n = int(input("enter number of terms: "))

for i in range(1, n):
    print(a + (i-1)*d, end = ",")

print(a + (n-1)*d)
