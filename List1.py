list=[]
l = int(input("enter number of elements:"))

print("enter elements:")

for i in range(l):
    data = int(input())
    list.append(data)
    
print("Alternate elements are: ")

for i in range(0, l, 2):
    print(list[i])
