

board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def print_board(board):
    i=1
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]}")
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

def main():
    print_board(board)
    current_player= "X"
    while True:
        print(f"Player: {current_player}'s turn")
        row=int(input("Enter row (0-2) :"))
        col=int(input("Enter column (0-2) :"))

        if board[row][col] == ' ':
            board[row][col]= current_player
        else:
            print("The place is already occupied")
            continue
        print_board(board)
        if check_winner(board):
            print(f"Congratulations! {current_player} won!")
            break

        if board_is_full(board):
            print("The board is full. Match tie..")
            break

        current_player= "O" if current_player=="X" else "X"


if __name__ == "__main__":
    main()