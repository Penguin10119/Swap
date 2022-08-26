list=[]
l = int(input("enter number of elements:"))

print("enter elements:")

for i in range(l):
    data = int(input())
    list.append(data)

maximum_value = 0
for data in list:
    if data > maximum_value:
        maximum_value = data

print('The largest number in list is', maximum_value)
