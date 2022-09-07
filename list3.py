l=[]
for i in range(10):
    l.append(int(input("enter a number: ")))
    
l2=[i for i in l if i%3 == 0]
l3=[i for i in l if i%5 == 0]

print(l)
print(l2)
print(l3)
