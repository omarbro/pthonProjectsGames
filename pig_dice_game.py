import random

def roll_dice():
    return random.randint(1, 6)

def play_turn(player_name):
    score = 0
    print(f"{player_name}'s turn")

    while True:
        roll = roll_dice()
        print(f"You rolled {roll}")
        if roll == 1:
            return 0
        score = score + roll
        choice = input( "do you want to play again? (y/n) :").lower()
        if choice != 'y':
            return score


def main():
    score = [0,0]
    current_player = 0
    line= "--------------------------------------"

    while True:
        player_name = f" Player {current_player + 1}"
        turn_score  = play_turn(player_name)
        score[current_player] += turn_score

        print(f"\n{player_name}'s score is: {score[current_player]}")
        print(line)
        print(f"Score Board: Player 1: {score[0]}  Player 2: {score[1]}")
        print(line)
        if score[current_player] >= 20:
            print(f"{player_name} wins!")
            break

        current_player = 1 if current_player == 0 else 0


if __name__ == '__main__':
    main()