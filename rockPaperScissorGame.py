import random

ROCK="r"
PAPER="p"
SCISSOR="s"

emojis={ROCK:"🪨",PAPER:"📜",SCISSOR:"✂️"}
choices= tuple(emojis.keys())
def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors? : type r or p or s").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input, input type r or p or s")

def print_choices(user_choice, comp_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[comp_choice]}")

def determine_result(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("Game Tied!! Try again!!")
    elif ((user_choice==ROCK and comp_choice==SCISSOR) or
          (user_choice==SCISSOR  and comp_choice== PAPER) or
          (user_choice== PAPER and comp_choice== ROCK)):
        print("Congratulations!! You win ...")
    else:
        print("You lose ...")

def play():
    while True:
        user_choice = get_user_choice()
        comp_choice=random.choice(choices)
        print_choices(user_choice, comp_choice)
        determine_result(user_choice, comp_choice)

        continue_game=input("Do you want to play again? (y/n) : ").lower()
        if continue_game=="n":
            break




play()