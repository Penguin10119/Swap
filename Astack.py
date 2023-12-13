#dictiobnary{boookid:list[author, number of pages, price, genre]}
#simukate stack operations
#push- accept genre from user and add book_id and author added to stack. Number of additons made in stack
#pop- removal all elec=ments from stack. give stack empty
#Display

d = {"1234":["JK", 12, 50, "horror"], "5678":["KJ", 13, 51, "Pop"]," 9012":["ui", 14, 52, "horror"], "4521":["KL", 65, 89, "fiction"]}
stack = []

def push():
    genre = input("Enter genre of boook: ")
    n = 0
    if i == genre:
        print("genre not found")
        break
    else:
        for i in d:
            if d[i][-1] == genre:
                stack.append(i)
                n += 1

    print("Added to stack")
    print(n, "number of additions made to stack")

def pop():
    n = 0
    if len(stack) == 0:
        print("underflow")
    else:
        while len(stack) != 0:
            stack.pop()
            n += 1
    print("Stack empty")
    print(n, "number of deletetions made from stack")

ch = "y"
while ch == "y":
    choices = int(input("Enter chi=oice: 1:Push, 2:Pop, 3: Display: "))
    if choices == 1:
        push()
    elif choices == 2:
        pop()
    elif choices == 3:
        print(stack)

    ch = input("Do you want to continue (y/n): ")
    
