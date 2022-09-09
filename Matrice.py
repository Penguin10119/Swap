#there is a list of dimension of 4x4, find out the sum of elements on main diagonal and secondary diagonal
l = []
for i in range(3):
    l1=[]
    for j in range(3):
        o = int(input(f'Enter a number for row {i+1}: '))
        l1.append(o)
    l.append(l1)

for i in l:
    print(i)
