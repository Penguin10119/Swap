import random
import time
import sys


def win():
    print("You win!")


def loss():
    print("Computer wins!")


def draw():
    print("Its a draw!")


def game():
    Possible_Outcomes = ['rock', 'paper', 'scissors']
    print("Welcome to Rock, Paper and Scissors!")
    Attempts = 3
    Player_Score = 0
    Computer_Score = 0
    while True:
        if Attempts == 0:
            print("Game over!")
            time.sleep(3)
            sys.exit(0)

        player = str(input("You chose: ")).lower()
        if player.lower() not in Possible_Outcomes:
            print("Invalid option entered, Choose a valid one!, Abandoning round")
            Attempts -= 1
        else:
            Computer_Options = random.choice(Possible_Outcomes)
            print(f"Computer chose: {Computer_Options}")

            if player == Computer_Options:
                draw()

            elif player == 'rock' and Computer_Options == 'scissors':
                win()

            elif player == 'rock' and Computer_Options == 'paper':
                loss()

            elif player == 'paper' and Computer_Options == 'rock':
                win()

            elif player == 'paper' and Computer_Options == 'scissors':
                loss()
                Computer_Score = Computer_Score + 2
                Player_Score = Player_Score + 0

            elif player == 'scissors' and Computer_Options == 'paper':
                win()

            elif player == 'scissors' and Computer_Options == 'rock':
                loss()

            else:
                pass

            Next_Round = input("Ready for the next round? (yes/no): ")
            if Next_Round.lower() == 'yes':
                game()
            elif Next_Round.lower() == 'no':
                print("Goodbye!")
                time.sleep(2.5)
                sys.exit(0)
            else:
                print("Error, Invalid output, Abandoning game.")
                time.sleep(2.5)
                sys.exit(0)


if __name__ == '__main__':
    game()
