import random

while True:
    user_ans = input("Dice the roll? (y/n): ").lower()
    if user_ans == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f" Your dices are {dice1} and {dice2} .")
    elif user_ans == "n":
        print("Thank you for playing !!!")
        break
    else:
        print("Invalid Input. Please input Y or N")


