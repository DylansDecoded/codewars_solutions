'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, 
and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, 
which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
'''
def valid_solution(board):
    return True if rows_check(board) and columns_check(board) and boxes_check(board) else False

def rows_check(board):
    '''
    Check if the rows are
    valid within the board
    '''
    v = 0
    correct_row_count = 9
    
    for row in board:
        r = set(row)
        condition = len(r) == len(board[0])
        not_empty_row = 0 not in r
        sum_of_rows = sum(row) == 45
        
        if condition and not_empty_row and sum_of_rows:
            v += 1
    
    return True if v == correct_row_count else False

def columns_check(board):
    '''
    Similar to the rows check
    method, validate columns
    of board
    '''
    # invert the boards columns
    columns =[[] for c in range(len(board[0]))]
    for row in board:
        for count, num in enumerate(row):
            columns[count].append(row)
    
    return rows_check(columns)

def boxes_check(board):
    '''
    Again, validate the boxes
    of the board.
    '''
    boxes_list = []
    
    for b in range(0, len(board[0]), 3):
        for d in range(0, len(board[0]), 3):
            end = d + 3
            box = board[b][d:end] + board[b+1][d:end] + board[b+2][d:end]
            boxes_list.append(box)
    for box in boxes_list:
        if sum(box) != 45:
            return False
    return True