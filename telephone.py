Consumer = input("Enter your name: ")
Mobile_Number = float(input("Enter Mobile number: "))
if Mobile_Number > 1000000000:
    Local_Calls = float(input("Enter number of local calls made: "))
    Data_Usage = float(input("Enter amount of Data used in Bytes: "))
    SMS = float(input("Enter number of SMS made: "))
    STD_Calls = float(input("Enter number of STD calls made: "))

else:
    print("Enter a valid mobile number")



if Local_Calls <= 500:
    Bill_Local = Local_Calls * 1.5

else:
    Bill_Local = 750 + (Local_Calls * 2)

if SMS <= 50:
    Bill_SMS = SMS * 1

else:
    Bill_SMS = 50 + (SMS * 0.5)

Bill_STD = STD_Calls * 3

Bill_Data = (Data_Usage/1000000000) * 30


Total_Bill = (Bill_Local + Bill_SMS + Bill_STD + Bill_Data) * 1.05

print("Your total Bill is: ", Total_Bill, "With 5% surcharge on Bill amount")

Amount = float(input("Enter the amount to be paid: "))


print("Select mode of payment ")
print("1. Cash")
print("2. Paytm")
print("3: Visa Card")
Payment = input("Enter mode of payment(1/2/3): ")

if Payment == '1':
    Change = Amount - Total_Bill
    print("You paid", Amount, "via cash and received", Change, "amount of change")

elif Payment == '2':
    Cashback = Amount * 0.02
    print("You paid", Amount, "via Paytm and received", Cashback, "amount of cashback")

elif Payment == '3':
    Money = Amount * 0.3
    print("You paid", Amount, "via Visa card hence you pay", Money, "more")

else:
    print("invalid mode of payment")



