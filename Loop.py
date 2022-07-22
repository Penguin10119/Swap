Oddnum = 0
Evennum = 0
Oddsum = 0
Evensum = 0

for i in range(10):
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
    print("There are", Evennum, "The average is", Evensum/Evennum)

elif Oddsum > 0:
    print("There are", Oddnum, "The average is", Oddsum/Oddnum)

else:
    print("error")

              
