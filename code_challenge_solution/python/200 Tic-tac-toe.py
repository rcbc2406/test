import numpy as np

def create_board():
    return np.zeros((3, 3), dtype=int)

def is_board_full(board):
    return np.count_nonzero(board) == 9

def is_valid_move(board, row, col):
    return board[row, col] == 0

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row, col] = player
        return True
    else:
        return False

def check_winner(board, player):
    # Check rows
    for i in range(3):
        if np.all(board[i] == player):
            return True

    # Check columns
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check diagonal
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def print_board(board):
    symbols = {0: "-", 1: "X", 2: "O"}

    for i in range(3):
        row = [symbols[val] for val in board[i]]
        print("|".join(row))
        if i < 2:
            print("-----")

def play_game():
    board = create_board()
    player = 1

    while True:
        print_board(board)
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if make_move(board, row, col, player):
            if check_winner(board, player):
                print_board(board)
                print("Player", player, "wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player = 2 if player == 1 else 1
        else:
            print("Invalid move. Try again.")

play_game()