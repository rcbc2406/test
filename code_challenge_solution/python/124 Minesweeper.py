import random

def create_board(size, num_mines):
    board = [[0] * size for _ in range(size)]
    mines_placed = 0
    
    while mines_placed < num_mines:
        row = random.randint(0, size-1)
        col = random.randint(0, size-1)
        
        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1
            
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < size and j >= 0 and j < size and board[i][j] != '*':
                        board[i][j] += 1
    
    return board

def reveal_square(board, revealed, row, col):
    if revealed[row][col] or board[row][col] == '*':
        return
    
    revealed[row][col] = True
    
    if board[row][col] == 0:
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < len(board) and j >= 0 and j < len(board) and not revealed[i][j]:
                    reveal_square(board, revealed, i, j)

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def play_game(size, num_mines):
    board = create_board(size, num_mines)
    revealed = [[False] * size for _ in range(size)]
    game_over = False
    
    while not game_over:
        print_board(revealed)
        
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if row >= 0 and row < size and col >= 0 and col < size:
            if not revealed[row][col]:
                if board[row][col] == '*':
                    print("Game over! You hit a mine.")
                    game_over = True
                else:
                    reveal_square(board, revealed, row, col)
                    
                    if all(all(revealed_row) for revealed_row in revealed):
                        print("Congratulations! You have won.")
                        game_over = True
            else:
                print("The square is already revealed. Try another one.")
        else:
            print("Invalid input. Please enter valid row and column numbers.")
    
    print_board(board)

size = int(input("Enter the size of the board: "))
num_mines = int(input("Enter the number of mines: "))

play_game(size, num_mines)