Oddnum = 0
Evennum = 0
Oddsum = 0
Evensum = 0

for i in range(20):
    a = float(input("enter numnbers: "))

    if (a%2 == 1):
              Oddnum += 1
              Oddsum += a

    elif a%2 == 0:
        Evennum += 1
        Evensum += a

    else:
        print("error")

if Evensum > 0:
    print("There are", Evennum, "Even numbers, The average is", Evensum/Evennum)

elif Oddsum > 0:
    print("There are", Oddnum, "Odd numbers, The average is", Oddsum/Oddnum)

else:
    print("error")
