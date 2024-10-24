from termcolor import colored
X= 'X'
O= 'O'
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def cell(mark):
    color= 'red' if mark == X else 'green'
    return colored(mark, color)


def print_board(board):
    i=1
    for row in board:
        print(f" {cell(row[0])} | {cell(row[1])} | {cell(row[2])}")
        if(i<3):
            print("---|---|---")
        i=i+1


def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2] != ' ' :
            return True

    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] != ' ' :
            return True

    if board[0][0]==board[1][1]==board[2][2] != ' ' or \
       board[0][2]==board[1][1]==board[2][0] != ' ' :
        return True

    return False


def board_is_full(board):
    for row in board:
        if ' ' in row:
            return False

    return True


def get_position(prompt):
    try:
        position =int(input(prompt))
        if position < 0 or position > 2:
            raise ValueError
        return position
    except ValueError:
        print("Please enter a valid number 0-2")


def get_move(current_player):
    while True:
        print(f"Player: {current_player}'s turn")
        row=get_position("Enter a row (0-2) : ")
        col=get_position("Enter a column (0-2) : ")

        if board[row][col] == ' ':
            board[row][col]= current_player
            break

        print("The place is already occupied")


def main():
    print_board(board)
    current_player= X
    while True:
        get_move(current_player)
        print_board(board)
        if check_winner(board):
            print(f"Congratulations! {current_player} won!")
            break

        if board_is_full(board):
            print("The board is full. Match tie..")
            break

        current_player= O if current_player== X else X


if __name__ == "__main__":
    main()