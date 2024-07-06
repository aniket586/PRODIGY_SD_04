def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def input_sudoku():
    board = []
    print("Enter the Sudoku puzzle row by row, with 0 representing empty cells:")
    for _ in range(9):
        while True:
            row = list(map(int, input().strip().split()))
            if len(row) != 9:
                print("Each row must have 9 numbers. Please try again.")
            else:
                board.append(row)
                break
    return board

# Input the Sudoku puzzle
board = input_sudoku()

# Solve the puzzle and print the result
if solve_sudoku(board):
    print("Sudoku puzzle solved successfully:")
    print_board(board)
else:
    print("No solution exists for the Sudoku puzzle")
