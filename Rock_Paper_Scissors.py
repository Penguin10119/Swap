import random

player = input("Enter your choice(Rock, Paper, Scissors): " )
Possible_Outcomes = ("Rock", "Paper", "Scissors")
AI_Options = random.choice(Possible_Outcomes)

print("You choose", player, "computer choose", AI_Options)

if player == AI_Options:
    print("Its a draw!")

elif player == 'Rock':
    if AI_Options == 'Scissors':
            print("You win!")
    else:
        print("Computer wins")
    
elif player == 'Scissors':
    if AI_Options == 'Paper':
            print("You win!")
            
    else:
        print("Computer wins!")

elif player == 'Paper':
    if AI_Options == 'Rock':
         print("You win!")
    else:
        print("Computer wins")
