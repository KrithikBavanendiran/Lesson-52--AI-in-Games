from colorama import init, Fore
import random
init(autoreset=True)
choices = ['Rock', 'Paper', 'Scissors']

while True:
    player=input(Fore.CYAN+"Choose from Rock(R), Paper(P), Scissors(S): ").upper()
    AI_choice = random.choice(choices)

    print(Fore.CYAN+f"AI chose: {AI_choice}")

    def winner(player, AI_choice):
        if player == AI_choice:
            print(Fore.YELLOW+"It's a Draw!")
        elif (player == 'R' and AI_choice == 'Scissors') or \
            (player == 'P' and AI_choice == 'Rock') or \
            (player == 'S' and AI_choice == 'Paper'):
            print(Fore.GREEN+"You Win!")
        else:
            print(Fore.RED+"You Lose!")
    winner(player, AI_choice)
    again=input("Do you want to play again? Y/N: ").upper()
    if again=="Y":
        continue
    else:
        break
    




    


