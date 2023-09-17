import tkinter as tk
from tkinter import ttk

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, or 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
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

def update_board_gui(board):
    for i in range(9):
        for j in range(9):
            cell_value = board[i][j]
            cell_entries[i][j].delete(0, tk.END)
            if cell_value != 0:
                cell_entries[i][j].insert(0, str(cell_value))

def solve_button_click():
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            entry_value = cell_entries[i][j].get()
            if entry_value.isdigit():
                board[i][j] = int(entry_value)
    
    if solve_sudoku(board):
        update_board_gui(board)
    else:
        result_label.config(text="No solution exists.")

root = tk.Tk()
root.title("Sudoku Solver")

cell_entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        entry = ttk.Entry(root, width=2, font=('Arial', 16))
        entry.grid(row=i, column=j)
        cell_entries[i][j] = entry

solve_button = ttk.Button(root, text="Solve", command=solve_button_click)
solve_button.grid(row=9, column=4)

result_label = ttk.Label(root, text="", font=('Arial', 16))
result_label.grid(row=10, column=0, columnspan=9)

root.mainloop()
