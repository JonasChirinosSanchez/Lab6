def initialize_board(num_rows, num_cols):
    board = [["-" for i in range(num_rows)] for i in range(num_cols)]
    return board


def print_board(board):
    for row in board:
        for entry in row:
            print(entry, end=" ")
        print()


def insert_chip(board, col, chip_type):
    for i in range(0, len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            row = len(board)-i-1
            break
        else:
            continue
    return row

def check_if_winner(board, col, row, chip_type):
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


def is_board_full(board, row, col, chip_type):
    e = True
    for row in board:
        for item in row:
            if item == "-":
                e = False
    return e



def main():
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    token_1 = "x"
    token_2 = "o"
    turn = 1
    board = initialize_board(length, height)
    print_board(board)
    print()
    print(f"Player 1: {token_1}")
    print(f"Player 2: {token_2}")
    print()
    while True:
        if turn == 1:
            chip_type = "x"
        elif turn == 2:
            chip_type = "o"
        col = int(input(f"Player {turn}: Which column would you like to choose? "))
        row = insert_chip(board, col, chip_type)
        board.reverse()
        print_board(board)
        if check_if_winner(board, col, row, chip_type) == True:
            print(f"Player {turn} won the game!")
            break
        elif is_board_full(board, height, length, chip_type):
            print("Draw. Nobody wins.")
            break

        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
        board.reverse()

if __name__ == "__main__":
    try:
        main()
    except:
        EOFError
