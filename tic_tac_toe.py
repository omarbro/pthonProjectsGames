board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def print_board(board):
    line= "---|---|---"
    print(line)
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print(line)
