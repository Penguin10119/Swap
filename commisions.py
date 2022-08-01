a = float(input("enter number of sales for Q1: "))
b = float(input("enter number of sales for Q2: "))
c = float(input("enter number of sales for Q3: "))
d = float(input("enter number of sales for Q4: "))
e = a+b+c+d
if (e >= 250000):
    print("commission is: ", 0.07*e)

elif (e <= 25000):
    print("commision is: ", 0.05 *e)

elif (e <= 100000):
    print("commission is: ", 0.02*e)

else:
    print("no commission")
