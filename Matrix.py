def matrix():
    m = []
    m1 = []
    for i in range(3):
        num = []
        for j in range(3):
            num1 = int(input(f'Enter a number for {i+1}st row and {j+1}st spot: '))
            num.append(num1)
        m.append(num)

    for i in range(3):
        num2 = []
        for j in range(3):
            num3 = int(input(f'Enter a number for {i+1}st row and {j+1}st spot: '))
            num2.append(num3)
        m1.append(num2)

    for i in range(3):
        for j in range(3):
            m[i][j] += m1[i][j]
    print(m)

matrix()


    
            

