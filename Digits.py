a = int(input("Enter a number"))

digits = 0

while a > 0:
    digits = digits + 1
    
    a = a//10

print("the number of digits in the number are", digits)    
    
