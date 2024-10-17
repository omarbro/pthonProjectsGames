import random

choices=("r","p","s")
emojis={"r":"🪨","p":"📜","s":"✂️"}

while True:
    user_choice=input("Rock, Paper, Scissors? : type r or p or s").lower()
    if user_choice not in choices:
        print("Invalid input, input type r or p or s")
        continue

    comp_choice=random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[comp_choice]}")

    if user_choice == comp_choice:
        print("Game Tied!! Try again!!")
    elif ((user_choice=="r" and comp_choice=="s") or
        (user_choice=="s"  and comp_choice== "p") or
        (user_choice== "p" and comp_choice== "r")):
        print("Congratulations!! You win ...")
    else:
        print("You lose ...")

    continue_game=input("Do you want to play again? (y/n) : ").lower()
    if continue_game=="n":
        break

